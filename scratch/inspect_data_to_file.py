import json
from pathlib import Path

with open("out/.work/skeleton.json", "r", encoding="utf-8") as f:
    sk = json.load(f)

# Let's inspect important sections
sections = [
    "meta", "liq", "tge", "alloc", "cex_trace", "multi_chain", 
    "decision_summary", "verdict", "decision_action_block"
]

with open("scratch/data_summary.txt", "w", encoding="utf-8") as out:
    out.write("=== OVERVIEW DATA ===\n")
    for sec in sections:
        if sec in sk:
            out.write(f"\n[{sec}]\n")
            out.write(json.dumps(sk[sec], indent=2, ensure_ascii=False))
            out.write("\n")

    out.write("\n=== HOLDINGS DISTRIBUTION ===\n")
    if "holdings_distribution" in sk:
        out.write(json.dumps(list(sk["holdings_distribution"].keys()), indent=2))
        out.write("\n")
        if "roles" in sk["holdings_distribution"]:
            out.write("\n[Roles]\n")
            for role, data in sk["holdings_distribution"]["roles"].items():
                out.write(f" - {role}: balance={data.get('balance')}, pct={data.get('supply_pct')}, value_usd={data.get('value_usd')}\n")

    out.write("\n=== ANOMALY SUMMARY ===\n")
    if "anomaly" in sk:
        for k, v in sk["anomaly"].items():
            if k != "waves":
                out.write(f" - {k}: {v}\n")
            else:
                out.write(f" - waves count: {len(v)}\n")
                for idx, wave in enumerate(v):
                    out.write(f"   Wave {idx}: title={wave.get('title')}, events={len(wave.get('events', []))}\n")
                    for e_idx, ev in enumerate(wave.get('events', [])):
                        out.write(f"     Event {e_idx}: {json.dumps(ev, ensure_ascii=False)}\n")

    out.write("\n=== LINEAGE DATA ===\n")
    if "lineage" in sk:
        out.write(json.dumps(list(sk["lineage"].keys()), indent=2))
        out.write("\n")
        if "m6" in sk["lineage"] and "rows" in sk["lineage"]["m6"]:
            out.write(f"m6 rows count: {len(sk['lineage']['m6']['rows'])}\n")
            for idx, r in enumerate(sk["lineage"]["m6"]["rows"][:10]):
                out.write(f" - Row {idx}: address={r.get('address')}, initial_tokens={r.get('initial_tokens')}, current_balance={r.get('current_balance')}, dumped_pct={r.get('dumped_pct')}\n")

    out.write("\n=== MONITORING WALLETS ===\n")
    if "monitoring_wallets" in sk:
        out.write(f"Wallets count: {len(sk['monitoring_wallets'])}\n")
        for idx, w in enumerate(sk["monitoring_wallets"]):
            out.write(f" - {w.get('address')}: role={w.get('role')}, balance={w.get('balance')}, label={w.get('label')}\n")

print("Wrote summary to scratch/data_summary.txt")
