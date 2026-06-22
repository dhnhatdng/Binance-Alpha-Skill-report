import json
from pathlib import Path

def find_placeholders(data, path=""):
    placeholders = []
    if isinstance(data, dict):
        for k, v in data.items():
            current_path = f"{path}.{k}" if path else k
            if isinstance(v, str) and v == "<LLM_NARRATIVE_PLACEHOLDER>":
                placeholders.append(current_path)
            else:
                placeholders.extend(find_placeholders(v, current_path))
    elif isinstance(data, list):
        for idx, item in enumerate(data):
            current_path = f"{path}[{idx}]"
            if isinstance(item, str) and item == "<LLM_NARRATIVE_PLACEHOLDER>":
                placeholders.append(current_path)
            else:
                placeholders.extend(find_placeholders(item, current_path))
    return placeholders

skeleton_path = Path("out/.work/skeleton.json")
if skeleton_path.exists():
    with open(skeleton_path, "r", encoding="utf-8") as f:
        sk = json.load(f)
    places = find_placeholders(sk)
    print("Found placeholders:")
    for p in places:
        print(f" - {p}")
else:
    print("skeleton.json not found")
