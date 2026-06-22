import json
from pathlib import Path

with open("out/.work/skeleton.json", "r", encoding="utf-8") as f:
    sk = json.load(f)

with open("scratch/more_details.txt", "w", encoding="utf-8") as out:
    out.write("=== LINEAGE M4 NOTES ===\n")
    if "lineage" in sk:
        out.write(json.dumps(sk["lineage"].get("m4_notes"), indent=2))
        out.write("\n")
        
    out.write("\n=== CROSS SYM ===\n")
    if "cross_sym" in sk:
        out.write(json.dumps(sk["cross_sym"], indent=2, ensure_ascii=False))
        out.write("\n")

    out.write("\n=== WASH INFRASTRUCTURE ===\n")
    if "wash_infrastructure" in sk:
        out.write(json.dumps(sk["wash_infrastructure"], indent=2, ensure_ascii=False))
        out.write("\n")

    out.write("\n=== FLOW OPERATORS ===\n")
    if "flow_operators" in sk:
        out.write(json.dumps(sk["flow_operators"], indent=2, ensure_ascii=False))
        out.write("\n")

    out.write("\n=== MONITORING WALLETS (ALL) ===\n")
    if "monitoring_wallets" in sk:
        out.write(json.dumps(sk["monitoring_wallets"], indent=2, ensure_ascii=False))
        out.write("\n")

print("Wrote details to scratch/more_details.txt")
