import os
import re
import json

profiles_dir = r"c:\Users\admin\Downloads\workspace\aidm\libraries\narrative_profiles"
schema_enums = {
    "economy": ["fiat_currency", "barter", "abstract_wealth", "reputation_based", "none"],
    "crafting": ["recipe_based", "skill_based", "experimental", "equivalent_exchange", "none"],
    "progression": ["mastery_tiers", "class_based", "quirk_awakening", "milestone_based", "static_op"]
}

report = []

for filename in os.listdir(profiles_dir):
    if not filename.endswith("_profile.md"):
        continue
    
    filepath = os.path.join(profiles_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract JSON block
    match = re.search(r"## Mechanical Configuration\s+```json\s+({.*?})\s+```", content, re.DOTALL)
    if not match:
        report.append(f"❌ {filename}: No 'Mechanical Configuration' JSON block found.")
        continue
    
    try:
        data = json.loads(match.group(1))
    except json.JSONDecodeError as e:
        report.append(f"❌ {filename}: Invalid JSON. {e}")
        continue
    
    file_errors = []
    
    # Check Economy
    if "economy" not in data:
        file_errors.append("Missing 'economy' section")
    elif "type" not in data["economy"]:
        file_errors.append("Missing 'economy.type'")
    elif data["economy"]["type"] not in schema_enums["economy"]:
        file_errors.append(f"Invalid economy.type: '{data['economy']['type']}'. Allowed: {schema_enums['economy']}")

    # Check Crafting
    if "crafting" not in data:
        file_errors.append("Missing 'crafting' section")
    elif "type" not in data["crafting"]:
        file_errors.append("Missing 'crafting.type'")
    elif data["crafting"]["type"] not in schema_enums["crafting"]:
        file_errors.append(f"Invalid crafting.type: '{data['crafting']['type']}'. Allowed: {schema_enums['crafting']}")

    # Check Progression
    if "progression" not in data:
        file_errors.append("Missing 'progression' section")
    elif "type" not in data["progression"]:
        file_errors.append("Missing 'progression.type'")
    elif data["progression"]["type"] not in schema_enums["progression"]:
        file_errors.append(f"Invalid progression.type: '{data['progression']['type']}'. Allowed: {schema_enums['progression']}")

    if file_errors:
        report.append(f"⚠️ {filename}:")
        for err in file_errors:
            report.append(f"  - {err}")
    else:
        report.append(f"✅ {filename}: Compliant")

print("\n".join(report))
