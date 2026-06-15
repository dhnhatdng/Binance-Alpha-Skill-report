"""screen_summary.py — v0.8.7.0

Deterministic 6-dimension "一屏结论" summary for report top.

# Why this exists

ChatGPT review (2026-06-12 BEAT v0.8.6.6 report): "第一屏没有把信息压成
交易者真正要的 3 个判断 (阶段 / 筹码 / 最近动). 数据已有, 但分散在
速读 / 行为画像 / 真实派发 / 风险聚合多段, 用户得拼."

This helper builds a deterministic 6-dimension TL;DR table emitted to
skeleton.screen_summary, rendered as `## 0. 一屏结论` at report top.

# 6 维度

| 维度 | Source | Label / Evidence |
|---|---|---|
| 1. 当前阶段 | chain_state (5-tier) + risk_score | 派发进行中 / 派完离场 / 潜伏未派 / 蓄筹观察 |
| 2. 筹码结构 | op_pct + retail_pct + cex_pool_pct | 高控盘+外部抛压低 / 中等控盘 / 分散散户主导 |
| 3. 成交质量 | wash_top_bot_share + wash_swap_count | 24h vol 不可信 / 部分 wash / 成交相对真实 |
| 4. 供应风险 | mint_authorities + mint_pct_supply_sum | 高供应源 / 存在供应源 / 无 mint |
| 5. 盘口阶段 | mcap + lp/mcap + vol/lp + price_change_24h | 高市值+薄承接 / 中等承接 / 低位 |
| 6. 监控重点 | 综合上述 5 维度 | "盯继续派发路径" / "盯首次派发" / "盯拉盘信号" |

# Determinism

All thresholds pre-registered (M35). No LLM input. Single source of
truth for first-screen narrative.

# Thresholds (pre-registered)

- 高控盘 op_pct ≥ 70%
- 中等控盘 op_pct 40-70%
- 分散 op_pct < 40%
- 外部抛压低 retail_pct < 8%
- 中等抛压 retail_pct 8-25%
- 高抛压 retail_pct ≥ 25%
- vol 不可信 wash_top_bot_share > 10%
- 部分 wash share 5-10%
- 高供应源 mint_pct_supply_sum > 20%
- 高市值 mcap > 1B USD
- 中市值 mcap 100M - 1B
- 低市值 mcap < 100M
- 薄承接 lp_usd/mcap < 0.01
- 拉升中 price_change_24h > 15%
- 大跌 price_change_24h < -10%
"""

from __future__ import annotations

from typing import Any


def _compute_chip_3way(skel: dict[str, Any]) -> tuple[float, float, float, float]:
    """Compute 庄家 / 交易所中转池 / 可验证非庄家方抛压 的 % 流通.

    v0.8.7.3: mirrors render_report.py top-100 classifier (jinja chunk
    line 700-1040) so 一屏结论 段可以显示跟"真实派发"段一致的 3 桶 %.
    Simplified: skips fanout/wcg-vs-top100 overlap subtraction (≤0.5pp
    rounding vs render-side output). Validated against velvet_v0872 case:
    op=96.4 vs render 96.5, cex=2.4 vs 2.4, retail=1.1 vs 1.1.

    Returns: (operator_pct, cex_pct, retail_pct, implied_circ_tokens)
    """
    meta = skel.get("meta") or {}
    primary_chain = meta.get("primary_chain")
    clp = meta.get("chain_lp_realtime") or {}
    thc = (clp.get(primary_chain) or {}).get("top_holders_classified") or {}

    # Build vest_set (vesting + mint_authority — render line 811-834)
    vest_addrs = set()
    for h in (thc.get("vesting") or {}).get("top") or []:
        vest_addrs.add((h.get("addr") or "").lower())
    auths = (skel.get("funding_attribution") or {}).get("mint_authorities", {}).get(
        "authorities"
    ) or []
    for auth in auths:
        vest_addrs.add((auth.get("addr") or "").lower())

    # Build op_union: deployer + detector-hits + clusters + section_a operator
    # categories (multisig / treasury / airdrop_platform / lp from
    # top_holders_classified). Render line 765-846.
    OP_ROLES = {
        "deployer", "suspected_operator_reserve", "fake_mining_cluster_member",
        "cross_alpha_inactive_whale", "anomaly_participant",
        "public_cex_hot_wallet", "cex_fanout_hub", "cex_fanout_recipient",
        "flow_operator", "high_throughput_dumper", "mining_fed_operator",
        "mint_authority",
    }
    op_union = set()
    for w in skel.get("monitoring_wallets") or []:
        if w.get("monitor_role_enum") in OP_ROLES:
            op_union.add((w.get("addr_full") or "").lower())
    for cat in ("multisig", "treasury", "airdrop_platform", "lp"):
        for h in (thc.get(cat) or {}).get("top") or []:
            op_union.add((h.get("addr") or "").lower())
    for cluster in (skel.get("wallet_cluster_graph") or {}).get("clusters") or []:
        for a in cluster.get("addrs") or []:
            op_union.add(a.lower())

    # Classify top-100 (vest first → cex by category → operator by union →
    # retail fallthrough). Render line 857-879.
    op_tok = cex_tok = retail_tok = 0.0
    for cat in ("vesting", "multisig", "treasury", "airdrop_platform",
                "cex", "lp", "unclassified"):
        for h in (thc.get(cat) or {}).get("top") or []:
            addr = (h.get("addr") or "").lower()
            bal = float(h.get("balance") or 0)
            if addr in vest_addrs:
                continue  # vest, skip
            if cat == "cex":
                cex_tok += bal
            elif addr in op_union:
                op_tok += bal
            else:
                retail_tok += bal

    # Tail additions (cex_fanout net + wcg cluster total balance) — render
    # line 918-964. We skip overlap subtraction here; render does it strictly.
    cfh = (skel.get("funding_attribution") or {}).get("cex_fanout_hubs") or {}
    fanout_net = float(
        (cfh.get("summary") or {}).get("net_structured_fanout_tokens_total") or 0
    )
    wcg_total = 0.0
    for cluster in (skel.get("wallet_cluster_graph") or {}).get("clusters") or []:
        wcg_total += float(cluster.get("total_balance") or 0)

    op_with_tail = op_tok + fanout_net + wcg_total
    implied_circ = op_with_tail + cex_tok + retail_tok
    if implied_circ == 0:
        return 0.0, 0.0, 0.0, 0.0
    return (
        op_with_tail / implied_circ * 100,
        cex_tok / implied_circ * 100,
        retail_tok / implied_circ * 100,
        implied_circ,
    )


def build_screen_summary(skel: dict[str, Any]) -> dict[str, Any]:
    """Build deterministic 7-dimension TL;DR summary.

    v0.8.7.3: split old "筹码结构" dim into two:
      - 筹码结构 — 3 buckets (庄家 / 交易所 / 非庄家) as % of circ
      - 内幕/庄家现货套现情况 — 已确认 insider 变现 + 交易所提币分发 净 %

    Also translates all English jargon (cex_fanout / insider / recipients /
    ht_dumper / bot / mint authority) to Chinese in user-facing evidence.

    Returns:
        {
          "dimensions": [
            {"name": "当前阶段", "label": "🔴 派发进行中", "evidence": "..."},
            ...  # 7 dims total
          ],
          "one_sentence": "...",  # deterministic 1-sentence summary
        }
    """
    meta = skel.get("meta") or {}
    dump_tracking = skel.get("dump_tracking") or {}
    dump_tracking_mining = skel.get("dump_tracking_mining") or {}
    # v0.8.6.7 mining fallback: prefer larger net_sellout
    base_net = dump_tracking.get("confirmed_net_sellout_usd") or 0
    mining_net = dump_tracking_mining.get("confirmed_net_sellout_usd") or 0
    if mining_net > base_net and not dump_tracking_mining.get("_error"):
        dump_tracking = dump_tracking_mining

    fa = skel.get("funding_attribution") or {}
    bp = skel.get("behavior_profile") or {}
    anomaly = skel.get("anomaly") or {}
    chain_state = skel.get("chain_state") or "CLEAN"
    risk_score = skel.get("chain_state_risk_score") or 0
    holders = skel.get("holdings_distribution") or {}

    # Numbers — fields prefixed `alpha_` (from Alpha API response)
    circ = float(meta.get("circulating_supply") or 0)
    total_supply = float(meta.get("total_supply") or 0)
    mcap = float(meta.get("alpha_market_cap_usd") or meta.get("market_cap_usd") or 0)
    lp_usd = float(meta.get("alpha_liquidity_usd") or meta.get("lp_usd") or 0)
    vol_24h = float(meta.get("alpha_vol_24h_usd") or meta.get("alpha_volume_24h_usd") or 0)
    price_change_24h = float(meta.get("alpha_percent_change_24h") or 0)
    depth_5pct = float(meta.get("liq_5pct_depth_usd") or (vol_24h / 96 * 0.05) or 0)

    # Confirmed sell
    net_sellout = float(dump_tracking.get("confirmed_net_sellout_usd") or 0)
    sell_pct_circ = float(dump_tracking.get("confirmed_total_pct") or 0)
    wash_dominated = bool(dump_tracking.get("wash_dominated") or False)
    wash_swap_count = int(dump_tracking.get("total_dex_swaps") or 0)
    top_seller_swaps = int(dump_tracking.get("top_seller_swaps") or 0)
    wash_top_bot_share = (top_seller_swaps / wash_swap_count) if wash_swap_count else 0.0

    # Mint
    mint_auths = (fa.get("mint_authorities") or {}).get("authorities") or []
    n_mint_auth = sum(1 for a in mint_auths if not a.get("is_excluded"))
    total_mint_sum = sum(float(a.get("total_minted") or 0)
                         for a in mint_auths if not a.get("is_excluded"))
    mint_pct_supply = (total_mint_sum / total_supply * 100) if total_supply else 0

    # ht dumpers throughput
    ht_dumpers = (fa.get("high_throughput_dumpers") or {}).get("dumpers") or []
    ht_throughput_total = sum(float(d.get("total_out") or 0) for d in ht_dumpers)
    ht_throughput_pct = (ht_throughput_total / circ * 100) if circ else 0

    # cex fanout
    cfh_sum = (fa.get("cex_fanout_hubs") or {}).get("summary") or {}
    fanout_net = float(cfh_sum.get("net_structured_fanout_tokens_total") or 0)
    fanout_recipients = int(cfh_sum.get("net_structured_unique_recipients") or 0)

    # Anomaly waves
    recent_n_72h = 0
    for d in (anomaly.get("detector_summary") or []):
        lbl = d.get("label") or ""
        if "72h" in lbl or "近期" in lbl:
            recent_n_72h = int(d.get("count") or 0)
            break

    # Chip structure (from holdings_distribution-derived or render-side calc)
    # Pipeline does NOT pre-compute these; we use skel's chip pcts if added,
    # otherwise fall back to dump_tracking + meta heuristics.
    # NOTE: render-side computes _operator_topdown_in_circ_pct via jinja —
    # we need a Python-side equivalent. For now, infer from confirmed sells +
    # cex_fanout net + ht throughput as proxy.
    # TODO: better to wire render's _operator_topdown_in_circ to skel; for v0.8.7.0
    # MVP, use confirmed_sell + net_fanout as proxy "operator visible footprint".
    operator_pct_proxy = min(100.0, sell_pct_circ + (fanout_net / circ * 100 if circ else 0))

    # ==================== Dimension 1: 当前阶段 ====================
    dim_phase = _dim_phase(chain_state, risk_score, sell_pct_circ, recent_n_72h, net_sellout)

    # ==================== Dimension 2: 筹码结构 (v0.8.7.3 new) ============
    op_pct, cex_pct, retail_pct, _implied_circ = _compute_chip_3way(skel)
    dim_chip_struct = _dim_chip_struct(op_pct, cex_pct, retail_pct)

    # ==================== Dimension 3: 内幕/庄家现货套现情况 (was 筹码结构) ====
    dim_insider_dump = _dim_insider_dump(op_pct, sell_pct_circ, fanout_net, circ)

    # ==================== Dimension 4: 成交质量 ====================
    dim_volume = _dim_volume(wash_dominated, wash_swap_count, top_seller_swaps,
                             wash_top_bot_share)

    # ==================== Dimension 5: 供应风险 ====================
    dim_supply = _dim_supply(n_mint_auth, mint_pct_supply, ht_throughput_pct,
                             len(ht_dumpers))

    # ==================== Dimension 6: 盘口阶段 ====================
    dim_market = _dim_market(mcap, lp_usd, vol_24h, depth_5pct, price_change_24h)

    # ==================== Dimension 7: 监控重点 ====================
    dim_monitor = _dim_monitor(dim_phase, dim_chip_struct, dim_supply,
                               fanout_recipients, n_mint_auth, recent_n_72h,
                               len(ht_dumpers))

    dims = [dim_phase, dim_chip_struct, dim_insider_dump, dim_volume,
            dim_supply, dim_market, dim_monitor]

    # ==================== One-sentence summary ====================
    one_sentence = _one_sentence(dim_phase, dim_chip_struct, dim_volume,
                                  dim_supply, dim_market)

    return {
        "dimensions": dims,
        "one_sentence": one_sentence,
    }


# ---- Per-dimension builders ----

def _dim_phase(chain_state: str, risk: int, sell_pct: float, recent_72h: int,
               net_sellout: float) -> dict:
    """Dimension 1: 当前阶段 — reuse chain_state 5-tier + augment with net_sellout."""
    if chain_state == "RECENT_DISTRIBUTION":
        if sell_pct > 5 or net_sellout > 1_000_000:
            label = "🔴 派发进行中 / 拉盘中出货"
        else:
            label = "🟠 近期异动 — 尚未确认大额变现"
        evidence = f"近 72h {recent_72h} 笔大额异动"
        if net_sellout > 0:
            evidence += f"; 已确认变现 ${net_sellout:,.0f}"
    elif chain_state == "OPERATOR_DUMPED":
        label = "🟢 派完离场 — 历史庄家已离场"
        evidence = "m6 谱系已派完, 当前无活跃 insider"
    elif chain_state == "DORMANT_INSIDER_RISK":
        label = "🟠 潜伏未派 — 风险未释放"
        evidence = "潜伏 insider 持仓集中, 时点 不可预测"
    elif chain_state == "WATCH":
        label = "🟡 观察 — 部分异动未触发主信号"
        evidence = f"近 72h {recent_72h} 笔异动 < 阈值"
    else:  # CLEAN
        label = "🟢 蓄筹 / 观察 — 无显著触发信号"
        evidence = "尚未触发 5 档主信号"
    return {"name": "当前阶段", "label": label, "evidence": evidence}


def _dim_chip_struct(op_pct: float, cex_pct: float, retail_pct: float) -> dict:
    """Dimension 2 (v0.8.7.3 new): 筹码结构 — 3 桶 % only.

    User feedback (velvet_v0872 review 2026-06-13): 每一项后面只要给 %,
    绝对值让用户到下方 "真实派发" 段自己看. Same algorithm as render-side
    top-100 chip classifier (see _compute_chip_3way docstring).
    """
    if op_pct >= 70:
        label = "🟣 高控盘"
    elif op_pct >= 40:
        label = "🟠 中等控盘"
    elif op_pct > 0:
        label = "🟢 分散"
    else:
        label = "⚪ 数据缺失"
    evidence = (
        f"庄家/项目方可控筹码 {op_pct:.1f}% / "
        f"交易所中转池 {cex_pct:.1f}% / "
        f"可验证非庄家方抛压 {retail_pct:.1f}%"
    )
    return {"name": "筹码结构", "label": label, "evidence": evidence}


def _dim_insider_dump(op_pct: float, sell_pct: float, fanout_net: float,
                       circ: float) -> dict:
    """Dimension 3 (v0.8.7.3 renamed from old 筹码结构): 内幕/庄家现货套现情况.

    User feedback (velvet_v0872 review 2026-06-13): 原"筹码结构"label 让位给
    3 桶版, 这里仍显示 insider 已变现 + 交易所提币分发 (cex_fanout) 净 % 流通,
    但 name 改成更准确的"内幕/庄家现货套现情况" + 所有英文术语翻译成中文.
    """
    fanout_pct = (fanout_net / circ * 100) if circ else 0
    if sell_pct >= 20 or fanout_pct >= 30:
        label = "🔴 已大量套现"
    elif sell_pct >= 5 or fanout_pct >= 10:
        label = "🟠 部分套现"
    elif sell_pct > 0 or fanout_pct > 0:
        label = "🟡 少量套现"
    else:
        label = "🟢 暂未套现"
    evidence = (
        f"已确认内幕变现 {sell_pct:.1f}% 流通 + "
        f"交易所提币分发净 {fanout_pct:.1f}% 流通"
    )
    return {"name": "内幕/庄家现货套现情况", "label": label, "evidence": evidence}


def _dim_volume(wash_dominated: bool, wash_swap_count: int, top_seller_swaps: int,
                wash_top_bot_share: float) -> dict:
    """Dimension 4: 成交质量 — wash share. v0.8.7.3: bot → 机器人 中文化."""
    if wash_dominated or wash_top_bot_share > 0.10:
        label = "🔴 24h 成交不可信 — 对敲机器人主导"
        evidence = (f"{wash_swap_count:,} 笔链上撮合, "
                    f"单机器人占 {wash_top_bot_share*100:.1f}%")
    elif wash_top_bot_share > 0.05:
        label = "🟠 部分对敲 — 真实承接需折扣"
        evidence = (f"{wash_swap_count:,} 笔撮合, "
                    f"单机器人 {wash_top_bot_share*100:.1f}%")
    elif wash_swap_count > 0:
        label = "🟢 成交相对真实"
        evidence = (f"{wash_swap_count:,} 笔撮合, "
                    f"单机器人 {wash_top_bot_share*100:.1f}%")
    else:
        label = "⚪ 无成交数据"
        evidence = "真实派发段未捕获链上撮合"
    return {"name": "成交质量", "label": label, "evidence": evidence}


def _dim_supply(n_mint_auth: int, mint_pct_supply: float, ht_throughput_pct: float,
                n_ht: int) -> dict:
    """Dimension 5: 供应风险 — 铸币权限 + 高频清仓累计过账.

    v0.8.7.3: ht_dumper → 高频清仓钱包, mint authority → 铸币权限, bridge → 跨链桥
    全中文化.
    """
    if n_mint_auth > 0 and mint_pct_supply > 20:
        label = "🔴 仍有铸币/跨链桥供应源"
        evidence = (f"{n_mint_auth} 个铸币权限合约, "
                    f"累计铸造占总供应 {mint_pct_supply:.1f}%")
    elif n_mint_auth > 0:
        label = "🟠 存在供应源 — 量级有限"
        evidence = (f"{n_mint_auth} 个铸币权限, "
                    f"累计 {mint_pct_supply:.1f}% 总供应")
    elif n_ht > 50 and ht_throughput_pct > 50:
        label = "🟠 高频清仓已显现 — 但无新铸币源"
        evidence = (f"{n_ht} 个高频清仓钱包, "
                    f"累计过账 {ht_throughput_pct:.0f}% 流通")
    else:
        label = "🟢 无显著供应风险"
        evidence = "无铸币权限 / 高频清仓过账量低"
    return {"name": "供应风险", "label": label, "evidence": evidence}


def _dim_market(mcap: float, lp_usd: float, vol_24h: float, depth_5pct: float,
                price_change_24h: float) -> dict:
    """Dimension 5: 盘口阶段 — mcap + LP + price + depth."""
    lp_mcap_ratio = (lp_usd / mcap) if mcap else 0
    vol_lp_ratio = (vol_24h / lp_usd) if lp_usd else 0
    parts = []
    if mcap >= 1_000_000_000:
        mcap_label = "高市值"
        parts.append(f"mcap ${mcap/1e6:,.0f}M")
    elif mcap >= 100_000_000:
        mcap_label = "中市值"
        parts.append(f"mcap ${mcap/1e6:,.0f}M")
    elif mcap > 0:
        mcap_label = "低市值"
        parts.append(f"mcap ${mcap/1e6:,.1f}M")
    else:
        mcap_label = "市值未知"
    if depth_5pct > 0:
        parts.append(f"5% 深度 ${depth_5pct:,.0f}")
    if lp_mcap_ratio > 0:
        parts.append(f"LP/mcap {lp_mcap_ratio:.3f}")
    if vol_lp_ratio > 0:
        parts.append(f"vol/LP {vol_lp_ratio:.1f}×")
    if price_change_24h > 15:
        price_label = "拉升中"
    elif price_change_24h < -10:
        price_label = "大跌"
    elif abs(price_change_24h) > 5:
        price_label = "波动"
    else:
        price_label = "稳"
    parts.append(f"24h {price_change_24h:+.1f}%")

    thin = lp_mcap_ratio > 0 and lp_mcap_ratio < 0.01
    if mcap >= 1_000_000_000 and thin:
        label = "🟠 高市值 + 薄承接"
    elif mcap >= 1_000_000_000:
        label = "🟡 高市值"
    elif mcap >= 100_000_000 and thin:
        label = "🟠 中市值 + 薄承接"
    elif mcap >= 100_000_000:
        label = "🟢 中市值"
    elif mcap > 0:
        label = "🟢 低市值"
    else:
        label = "⚪ 数据缺失"
    if price_label == "拉升中":
        label = label + " / 拉升中"
    elif price_label == "大跌":
        label = label + " / 大跌"
    evidence = "; ".join(parts) if parts else "盘口数据缺失"
    return {"name": "盘口阶段", "label": label, "evidence": evidence}


def _dim_monitor(dim_phase: dict, dim_chip: dict, dim_supply: dict,
                 fanout_recipients: int, n_mint_auth: int, recent_72h: int,
                 n_ht: int) -> dict:
    """Dimension 7: 监控重点 — derive from other dims.

    v0.8.7.3: 全部英文术语翻译中文 — mint authority → 铸币权限, CEX fan-out
    hub + recipients → 交易所提币分发集散方 + 接收方, ht_dumper → 高频清仓钱包,
    detector → 检测器, cluster → 集群.
    """
    items = []
    if "派发进行中" in dim_phase["label"] or "近期异动" in dim_phase["label"]:
        items.append("近 72h 异动地址")
    if n_mint_auth > 0:
        items.append("铸币权限合约")
    if fanout_recipients > 5:
        items.append("交易所提币分发集散方 + 接收方")
    if n_ht > 50:
        items.append("高频清仓钱包")
    if "派完离场" in dim_phase["label"]:
        items.append("看是否有新派发周期 (新铸币 / 新集群 出现)")
    if not items:
        items.append("现有检测器未触发主信号, 维持基础监控")

    label = "盯继续派发路径" if "派发" in dim_phase["label"] else "维持基础监控"
    evidence = "、".join(items)
    return {"name": "监控重点", "label": label, "evidence": evidence}


def _one_sentence(dim_phase: dict, dim_chip: dict, dim_volume: dict,
                  dim_supply: dict, dim_market: dict) -> str:
    """Deterministic 1-sentence summary."""
    parts = []
    parts.append(dim_phase["label"].split(" — ")[0].replace("🔴 ", "")
                 .replace("🟠 ", "").replace("🟢 ", "").replace("🟡 ", "")
                 .replace("⚪ ", "").replace("🟣 ", ""))
    chip = dim_chip["label"].split(" — ")[0]
    for emoji in ["🟣 ", "🟠 ", "🟢 ", "🟡 ", "⚪ "]:
        chip = chip.replace(emoji, "")
    parts.append(chip)
    if "不可信" in dim_volume["label"] or "wash" in dim_volume["label"].lower():
        parts.append("成交被 wash 放大")
    if "高" in dim_supply["label"]:
        parts.append("仍有供应源")
    if "高市值" in dim_market["label"]:
        parts.append("已在高位")
    return " + ".join(parts) + "."


__all__ = ["build_screen_summary"]
