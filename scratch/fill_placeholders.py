import json
from pathlib import Path

# Load skeleton.json
skeleton_path = Path("out/.work/skeleton.json")
with open(skeleton_path, "r", encoding="utf-8") as f:
    sk = json.load(f)

# Extract key statistics
meta = sk.get("meta", {})
symbol = meta.get("symbol", "O")
chain = meta.get("chain", "BSC")
alpha_listing_date = meta.get("alpha_listing_date_utc", "2026-06-17")
current_price = meta.get("alpha_price_usd", 0.6756)

liq = sk.get("liq", {})
dex_liq = liq.get("dex_pool_liquidity_usd", 2895107.50)
depth_5pct = liq.get("alpha_5pct_depth_usd_est", 7812)

verdict = sk.get("verdict", {})
verdict_enum = verdict.get("enum", "ADVISORY")
verdict_label = verdict.get("cn_label", "Observe")

action = sk.get("decision_action_block", {})
tranche_max = action.get("immediate_action", {}).get("tranche_max_usd", 2604)
stop_loss_trigger = action.get("stop_loss", {}).get("trigger_price_usd", 0.57171)
stop_loss_pct = action.get("stop_loss", {}).get("delta_pct", -15.0)

# CEX trace details
cex_trace = sk.get("cex_trace", {})
cex_rows = cex_trace.get("rows", [])
is_s2_or_s3 = False
s2_date = "—"
for r in cex_rows:
    if r.get("exchange") == "Binance" and r.get("status") == "Listed":
        is_s2_or_s3 = True
        s2_date = r.get("ts", "—")

# Skip reasons
cross_sym_skip_reason = sk.get("cross_sym", {}).get("_skip_reason", "surf_no_sql_solana")
wash_infra_skip_reason = sk.get("wash_infrastructure", {}).get("_skip_reason", "surf_no_sql_solana")
flow_ops_skip_reason = sk.get("flow_operators", {}).get("_skip_reason", "surf_no_sql_solana")

# Top CEX holdings percentage calculation
cex_pct = 0.0
cex_wallets = 0
if "chain_lp_realtime" in meta and "binance-smart-chain" in meta["chain_lp_realtime"]:
    bsc_info = meta["chain_lp_realtime"]["binance-smart-chain"]
    if "top_holders_classified" in bsc_info and "cex" in bsc_info["top_holders_classified"]:
        cex_tokens = bsc_info["top_holders_classified"]["cex"].get("tokens", 0)
        cex_wallets = bsc_info["top_holders_classified"]["cex"].get("n_wallets", 0)
        total_supply = meta.get("total_supply", 1000000000)
        cex_pct = (cex_tokens / total_supply) * 100

# Unclassified holdings percentage
unclassified_pct = 0.0
if "chain_lp_realtime" in meta and "binance-smart-chain" in meta["chain_lp_realtime"]:
    bsc_info = meta["chain_lp_realtime"]["binance-smart-chain"]
    if "top_holders_classified" in bsc_info and "unclassified" in bsc_info["top_holders_classified"]:
        unclass_tokens = bsc_info["top_holders_classified"]["unclassified"].get("tokens", 0)
        total_supply = meta.get("total_supply", 1000000000)
        unclassified_pct = (unclass_tokens / total_supply) * 100

# Fill placeholders in sk dict
sk["verdict"]["one_liner"] = (
    f"The token {symbol} has an estimated 5% slippage entry cap of ${depth_5pct} and is classified as "
    f"{verdict_label} ({verdict_enum}) with inactive 72h large transfer anomalies."
)

sk["lineage"]["m4_notes"] = [
    f"The pre-launch phase for {symbol} shows no early wallet deployments or allocations.",
    f"No pre-launch OTC seeding was detected on BSC for {symbol}, which means there are zero verified early insider recipients.",
    f"Without any pre-launch deployment trace, the initial allocation remains highly concentrated in the creator/unlabeled reserves."
]

sk["anomaly"]["rhythm"]["title"] = f"On-chain transfer rhythm for {symbol}."
sk["anomaly"]["verdict_impact"] = (
    f"No on-chain transfer anomalies were detected in the last 72 hours, resulting in a low impact on the verdict of {verdict_label}."
)

sk["anomaly"]["detector_summary"][0]["detail"] = f"No pre-launch distribution to early wallets was identified on {chain}."
sk["anomaly"]["detector_summary"][1]["detail"] = f"No fully-distributed insider wallets were recorded on {chain}."
sk["anomaly"]["detector_summary"][2]["detail"] = f"No quiet insider wallets holding supply were identified on {chain}."
sk["anomaly"]["detector_summary"][3]["detail"] = f"No anomalous large transfers were observed in the past 72 hours on {chain}."

sk["multi_chain"]["interpretation"] = f"The token {symbol} is deployed as a single-chain asset on {chain} with no cross-chain bridge activity."
sk["tge"]["interpretation"] = f"The token was first listed on Binance Alpha on {alpha_listing_date} UTC. The current price is ${current_price:.4f}."
sk["alloc"]["interpretation"] = f"No verified early insider distributions were detected on-chain, indicating supply remains inside reserve clusters."

if is_s2_or_s3:
    sk["cex_trace"]["interpretation"] = f"The token is currently listed on Binance with perps active since {s2_date}, representing S2 classification."
else:
    sk["cex_trace"]["interpretation"] = f"The token has no active CEX perpetual listings on Binance, Aster, or Bitget, keeping it in S1 classification."

sk["liq"]["interpretation"] = f"DEX liquidity is ${dex_liq:,.2f} but estimated 5% depth is extremely low at ${depth_5pct}, limiting trade sizing."

sk["cross_sym"]["summary_narrative"] = f"Cross-symbol analysis was skipped for {symbol} due to the {cross_sym_skip_reason} flag on BSC."
sk["wash_infrastructure"]["summary_narrative"] = f"Wash-infrastructure scanning was skipped for {symbol} due to the {wash_infra_skip_reason} flag."
sk["flow_operators"]["summary_narrative"] = f"Flow-operators detection was skipped for {symbol} due to the {flow_ops_skip_reason} flag on BSC."

sk["holdings_distribution"]["key_takeaways"] = [
    f"Top CEX holdings account for {cex_pct:.2f}% of supply, showing moderate exchange listing concentration.",
    f"Unclassified wallets hold {unclassified_pct:.2f}% of supply, indicating a significant portion of token distribution is not Arkham labeled.",
    f"The total DEX main pool liquidity is ${dex_liq:,.2f}, representing a stable but moderate trading depth on-chain."
]

sk["decision_summary"]["narrative"] = f"Based on the analysis of {symbol}, the trade sizing is restricted to a max of ${depth_5pct} due to shallow depth."

sk["decision_action_block"]["immediate_action"]["narrative"] = (
    f"Due to the current Observe ({verdict_label}) rating, we advise a waiting stance with a max tranche size of ${tranche_max}."
)
sk["decision_action_block"]["stop_loss"]["rationale"] = (
    f"Set stop-loss trigger price at ${stop_loss_trigger:.5f} which is {stop_loss_pct}% below the current market price."
)
sk["decision_action_block"]["re_entry_conditions"][0]["narrative"] = (
    f"Wait until the anomaly 72h large transfer count drops to {sk['decision_action_block']['re_entry_conditions'][0]['threshold']}."
)

n_wallets = len(sk.get("monitoring_wallets", []))
for w in sk.get("monitoring_wallets", []):
    w["alert"] = f"Monitor this suspected {w['role']} for transfers into DEX or CEX deposit addresses."

sk["monitoring_footer"] = (
    f"Monitoring these {n_wallets} wallets helps track active operator reserves and potential sell-out actions for {symbol}."
)

# Write to out/.work/filled.json
filled_path = Path("out/.work/filled.json")
with open(filled_path, "w", encoding="utf-8") as f:
    json.dump(sk, f, ensure_ascii=False, indent=2)

print("Successfully wrote out/.work/filled.json")
