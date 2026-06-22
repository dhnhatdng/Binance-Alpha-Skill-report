import json
from pathlib import Path

with open("out/.work/skeleton.json", "r", encoding="utf-8") as f:
    sk = json.load(f)

# Let's inspect important sections
sections = [
    "meta", "liq", "tge", "alloc", "cex_trace", "multi_chain", 
    "decision_summary", "verdict", "decision_action_block"
]

print("=== OVERVIEW DATA ===")
for sec in sections:
    if sec in sk:
        print(f"\n[{sec}]")
        # Print a clean representation of the dictionary
        print(json.dumps(sk[sec], indent=2, ensure_ascii=False)[:1000])

print("\n=== HOLDINGS DISTRIBUTION KEY TAKEAWAYS ===")
if "holdings_distribution" in sk:
    print(json.dumps(sk["holdings_distribution"].keys(), indent=2))
    if "roles" in sk["holdings_distribution"]:
        print("\n[Roles]")
        for role, data in sk["holdings_distribution"]["roles"].items():
            print(f" - {role}: balance={data.get('balance')}, pct={data.get('supply_pct')}")

print("\n=== ANOMALY SUMMARY ===")
if "anomaly" in sk:
    for k, v in sk["anomaly"].items():
        if k != "waves":
            print(f" - {k}: {v}")
        else:
            print(f" - waves count: {len(v)}")
            for idx, wave in enumerate(v):
                print(f"   Wave {idx}: title={wave.get('title')}, events={len(wave.get('events', []))}")

print("\n=== MONITORING WALLETS ===")
if "monitoring_wallets" in sk:
    print(f"Wallets count: {len(sk['monitoring_wallets'])}")
    for idx, w in enumerate(sk["monitoring_wallets"][:5]):
        print(f" - {w.get('address')}: role={w.get('role')}, balance={w.get('balance')}")
