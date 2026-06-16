#!/usr/bin/env python3
"""section_liq.py — Section LIQ: Alpha 5% depth + DEX main pool + LP 24h flow.

Output:
- current_price_usd (from DexScreener best pair)
- dex_pool_addr (highest-liquidity pair for the token)
- dex_pool_liquidity_usd
- dex_pool_volume_24h_usd
- alpha_5pct_depth_usd_est (heuristic from alpha_vol_24h, since no public
  order-book API for Alpha-only tokens is documented in v0.6)
- lp_24h_flow_pct (% change in pool token balance via surf)
- liq_rows[] for report
- decision_action numeric slots (pipeline replaces stubs in decision_action_block)
- decision_anchors_partial[] entries

v0.6 (2026-05-24, Phase B.1)
"""

from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path
from typing import Any
import sys

sys.path.insert(0, str(Path(__file__).parent))
from parallel_surf import run_parallel
from i18n import t   # v0.6.2 i18n
from chain_router import (  # v0.7.20 / v0.7.21.7 / v0.7.21.8
    transfers_table,
    dex_trades_table,
    get_active_chain as _chain_get_active,
    sql_supported as _sql_supported,
    decimals_factor_str,
)


def _curl_json(url: str, timeout: int = 8) -> dict | None:
    try:
        proc = subprocess.run(
            ["curl", "-sS", "--max-time", str(timeout), url],
            capture_output=True, text=True, encoding="utf-8", errors="replace", check=False,
        )
        if proc.returncode != 0:
            return None
        return json.loads(proc.stdout)
    except (subprocess.SubprocessError, json.JSONDecodeError):
        return None


def discover_main_pool(
    ca: str,
    scope_chain_lp: dict[str, dict[str, Any]] | None = None,
    scope_realtime_token_info: dict[str, Any] | None = None,
    primary_chain: str | None = None,
) -> dict[str, Any]:
    """v0.7.10: Pick main DEX pool from surf real-time data (no DexScreener).

    Reads pre-computed `chain_lp_realtime` (surf token-holders + DEX-label
    classification per chain) and `realtime_token_info` (surf project-detail
    aggregate price/vol/FDV). Falls back to "no pool" only when surf returned
    no DEX-labeled holders.

    Returns same shape as v0.6/v0.7.9:
        {
            "pool_addr": "0x..." or None,
            "price_usd": float or None,
            "liquidity_usd": float or None,
            "volume_24h_usd": float or None,   # aggregate cross-chain (CEX+DEX)
            "fdv": float or None,
            "_status": "OK" | "NOT_FOUND" | "API_DOWN",
        }
    """
    chain_lp = scope_chain_lp or {}
    rti = scope_realtime_token_info or {}

    # Pick pool from the primary chain's surf top_pool_addr; if primary not
    # set, fall back to the chain with the highest lp_usd across all entries.
    chain_entry: dict[str, Any] = {}
    if primary_chain and primary_chain in chain_lp:
        chain_entry = chain_lp[primary_chain] or {}
    if not chain_entry or not chain_entry.get("top_pool_addr"):
        # Pick max-lp_usd chain that has a top_pool_addr.
        cands = [
            (p, v) for p, v in chain_lp.items()
            if v.get("top_pool_addr") and (v.get("lp_usd") or 0) > 0
        ]
        if cands:
            cands.sort(key=lambda kv: kv[1].get("lp_usd") or 0, reverse=True)
            _, chain_entry = cands[0]

    pool_addr = chain_entry.get("top_pool_addr")
    lp_usd = chain_entry.get("lp_usd")
    price_usd = rti.get("price_usd")
    vol_24h_usd = rti.get("volume_24h_usd")
    fdv = rti.get("fdv_usd")

    if not pool_addr and (not rti or not rti.get("fetch_ok")):
        # Neither surf token-holders nor project-detail produced anything.
        return {"pool_addr": None, "price_usd": None, "liquidity_usd": None,
                "volume_24h_usd": None, "fdv": None, "_status": "API_DOWN"}
    if not pool_addr:
        return {"pool_addr": None, "price_usd": price_usd, "liquidity_usd": None,
                "volume_24h_usd": vol_24h_usd, "fdv": fdv, "_status": "NOT_FOUND"}

    return {
        "pool_addr": pool_addr,
        "price_usd": price_usd,
        "liquidity_usd": lp_usd,
        "volume_24h_usd": vol_24h_usd,
        "fdv": fdv,
        "_status": "OK",
    }


def lp_24h_flow(ca: str, pool_addr: str | None, workdir: Path | None = None) -> dict[str, Any]:
    """Surf query: pool token in/out in last 24h.

    Returns {lp_in_tokens, lp_out_tokens, net_pct} or empty dict if no pool.

    v0.7.21.8: skip on chains without surf onchain-sql coverage (Solana).
    The query would hit UNKNOWN_TABLE and waste a credit.
    """
    if not pool_addr:
        return {}
    if not _sql_supported():
        return {"_skip_reason": "surf_no_sql_solana"}
    if workdir is None:
        workdir = Path(tempfile.mkdtemp(prefix="lp24_"))
    workdir = Path(workdir)
    workdir.mkdir(exist_ok=True, parents=True)

    q = workdir / "q_lp24.json"
    q.write_text(json.dumps({
        "max_rows": 2,
        "sql": (
            f"SELECT "
            f"sum(if(\"to\" = '{pool_addr}', toFloat64(toDecimal256(amount_raw,0))/{decimals_factor_str()}, 0)) AS lp_in, "
            f"sum(if(\"from\" = '{pool_addr}', toFloat64(toDecimal256(amount_raw,0))/{decimals_factor_str()}, 0)) AS lp_out "
            f"FROM {transfers_table()} "
            f"WHERE contract_address = '{ca if _chain_get_active() == 'solana' else ca.lower()}' "
            f"AND block_time >= now() - INTERVAL 1 DAY "
            f"AND block_date >= today() - 2"
        ),
    }), encoding="utf-8")
    results, _ = run_parallel([str(q)])
    resp = results[str(q)]
    if "error" in resp:
        return {"_error": resp["error"]}
    data = (resp.get("data") or [{}])[0]
    lp_in = float(data.get("lp_in", 0) or 0)
    lp_out = float(data.get("lp_out", 0) or 0)
    net_pct = ((lp_in - lp_out) / lp_in * 100.0) if lp_in > 1 else 0.0
    return {"lp_in_tokens": lp_in, "lp_out_tokens": lp_out, "net_pct": round(net_pct, 2)}


def run(
    ca: str,
    symbol: str,
    alpha_vol_24h_usd: float | None = None,
    alpha_price_usd: float | None = None,
    scope_chain_lp: dict[str, dict[str, Any]] | None = None,
    scope_realtime_token_info: dict[str, Any] | None = None,
    primary_chain: str | None = None,
) -> dict[str, Any]:
    """Section LIQ entrypoint.

    v0.7.10: takes surf realtime scope data (chain_lp_realtime,
    realtime_token_info, primary_chain) — no more DexScreener fetch. Same
    output shape as v0.7.9 so downstream consumers (decision_summary,
    decision_anchors) don't need changes.

    Args:
        ca: contract address
        symbol: e.g. "BSB"
        alpha_vol_24h_usd: from Section A, used to estimate Alpha 5% depth
        scope_chain_lp: scope["chain_lp_realtime"] from section_a (surf
            token-holders + DEX-label real-time LP per chain).
        scope_realtime_token_info: scope["realtime_token_info"] (surf
            project-detail aggregate price/vol/FDV).
        primary_chain: scope["primary_chain"] — which chain's pool to surface.

    Returns full LIQ data + decision anchors + decision_action numeric updates.
    """
    pool = discover_main_pool(
        ca,
        scope_chain_lp=scope_chain_lp,
        scope_realtime_token_info=scope_realtime_token_info,
        primary_chain=primary_chain,
    )
    flow = lp_24h_flow(ca, pool.get("pool_addr"))

    # Alpha 5% depth heuristic: vol_24h / 96 (15-min slice) * 0.05 (5% slip)
    # Real API for order book on Alpha-only tokens is not publicly stable;
    # heuristic gives an order-of-magnitude estimate. Phase B+ may replace
    # with verified endpoint or accept INSUFFICIENT_DATA marker.
    alpha_5pct_depth_est = None
    if alpha_vol_24h_usd:
        alpha_5pct_depth_est = int(alpha_vol_24h_usd / 96 * 0.05)

    # Decision action numeric slots (replaces stub $30000 from pipeline alpha.3)
    # Tranche max = Alpha 5% depth ÷ 3 batches (conservative)
    tranche_max_usd = (
        max(int(alpha_5pct_depth_est / 3), 1000)
        if alpha_5pct_depth_est else 10000
    )
    # v0.7.16: price fallback chain. surf project-detail can NOT_FOUND a real
    # listed token (GUA — listed 3 months, still not indexed). In that case
    # `pool["price_usd"]` is None and every downstream price cell (TGE table,
    # stop-loss trigger, ALLOC USD figures) renders as "—". Per the user
    # directive (memory feedback_binance_alpha_vol_must_fetch.md), the Alpha
    # token-list endpoint IS the source of truth for Alpha-listed price/vol —
    # use it as a fallback. (dump_tracker.median_price_usd is wired in by the
    # pipeline as a last-resort fallback after dump_tracker runs.)
    # codex HIGH#2: `or alpha_price_usd` would treat a legit 0 as missing.
    # crypto price = 0 is exotic but possible (paused listing / fresh launch
    # with no swaps yet) → preserve the surf 0 instead of silently swapping to
    # the Alpha API value. Same `is not None` guard on stop_loss.
    _pool_price = pool.get("price_usd")
    current_price = _pool_price if _pool_price is not None else alpha_price_usd
    stop_loss_trigger_price = (current_price * 0.85) if current_price is not None else None

    # v0.6.2: anchors + notes via i18n. Values stay as f-strings (data + format).
    dash = t("common.none_dash")
    liq_rows = [
        {
            "anchor": t("section.liq.label_5pct_depth"),
            "value": f"${alpha_5pct_depth_est:,.0f}" if alpha_5pct_depth_est else dash,
            "note": t("section.liq.note_5pct_depth"),
        },
        {
            "anchor": t("section.liq.label_dex_lp"),
            "value": f"${pool['liquidity_usd']:,.0f}" if pool.get("liquidity_usd") else dash,
            "note": (
                f"surf {pool['pool_addr'][:10]}…" if pool.get("pool_addr")
                else t("section.liq.note_no_pool")
            ),
        },
        {
            "anchor": t("section.liq.label_dex_vol"),
            "value": f"${pool['volume_24h_usd']:,.0f}" if pool.get("volume_24h_usd") else dash,
            "note": "surf project-detail (跨链 CEX+DEX 实时聚合)",
        },
        {
            "anchor": t("section.liq.label_lp_flow"),
            "value": (
                t("section.liq.value_lp_flow_full",
                  net_pct=flow.get("net_pct"),
                  lp_in=flow.get("lp_in_tokens", 0),
                  lp_out=flow.get("lp_out_tokens", 0))
                if flow.get("lp_in_tokens") else dash
            ),
            # v0.7.21.8: don't surface a bogus "surf agent.solana_transfers"
            # source on a chain whose SQL table doesn't exist. The skip is
            # decided by chain_router.sql_supported() rather than the flow
            # dict because lp_24h_flow returns {} (no skip key) when there
            # is no pool_addr to query, which on Solana is the common case.
            "note": (
                "surf 不覆盖 (chain SQL 表不存在), 见顶部 Solana banner"
                if not _sql_supported()
                else f"surf {transfers_table()}"
            ),
        },
        {
            "anchor": t("section.liq.label_dex_addr"),
            "value": f"`{pool['pool_addr']}`" if pool.get("pool_addr") else dash,
            "note": (
                t("section.liq.note_dex_addr", fdv=int(pool['fdv']))
                if pool.get("fdv") else ""
            ),
        },
    ]

    # Decision anchors fragments (pipeline merges into report_data.decision_anchors)
    decision_anchors_partial = [
        {
            "anchor": t("section.liq.decision_anchor_alpha_5pct"),
            "value": f"${alpha_5pct_depth_est:,.0f}" if alpha_5pct_depth_est else t("common.unknown"),
            "status": (
                t("section.liq.status_depth_good") if (alpha_5pct_depth_est or 0) >= 50000
                else t("section.liq.status_depth_medium") if (alpha_5pct_depth_est or 0) >= 5000
                else t("section.liq.status_depth_thin")
            ),
        },
        {
            "anchor": t("section.liq.decision_anchor_dex_lp_usd"),
            "value": f"${pool['liquidity_usd']:,.0f}" if pool.get("liquidity_usd") else dash,
            "status": "🟢" if (pool.get("liquidity_usd") or 0) >= 200000
                     else "🟡" if (pool.get("liquidity_usd") or 0) >= 50000
                     else "🔴",
        },
        {
            "anchor": t("section.liq.label_lp_flow"),
            "value": f"{flow.get('net_pct'):+.2f}%" if "net_pct" in flow else dash,
            "status": "🟢" if abs(flow.get("net_pct") or 0) < 5
                     else "🟡" if abs(flow.get("net_pct") or 0) < 20
                     else "🔴",
        },
    ]

    return {
        "current_price_usd": current_price,
        "dex_pool_addr": pool.get("pool_addr"),
        "dex_pool_liquidity_usd": pool.get("liquidity_usd"),
        "dex_pool_volume_24h_usd": pool.get("volume_24h_usd"),
        "fdv": pool.get("fdv"),
        "alpha_5pct_depth_usd_est": alpha_5pct_depth_est,
        "lp_24h_flow": flow,
        "liq_rows": liq_rows,
        "decision_anchors_partial": decision_anchors_partial,
        # Numeric updates for decision_action_block
        "decision_action_overrides": {
            "tranche_max_usd": tranche_max_usd,
            "stop_loss_trigger_price": round(stop_loss_trigger_price, 6) if stop_loss_trigger_price else None,
        },
        "_probes": {
            "dexscreener": pool["_status"],
            "lp_flow_surf": "OK" if flow else "NO_POOL",
        },
    }


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("ca")
    ap.add_argument("symbol")
    ap.add_argument("--alpha-vol-24h-usd", type=float, default=None)
    args = ap.parse_args()
    result = run(args.ca, args.symbol, alpha_vol_24h_usd=args.alpha_vol_24h_usd)
    print(json.dumps(result, ensure_ascii=False, indent=2))
