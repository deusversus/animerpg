import json
import os
import sys

def load_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

def validate_profile(profile_path, schema_path):
    print(f"Validating {os.path.basename(profile_path)}...")
    profile = load_json(profile_path)
    schema = load_json(schema_path)

    if not profile or not schema:
        return False

    # Basic validation of mechanical_modules
    if "mechanical_modules" not in profile:
        print(f"  [ERROR] 'mechanical_modules' missing in {profile_path}")
        return False

    modules = profile["mechanical_modules"]
    valid = True

    # Check Economy
    if "economy" in modules:
        if "type" not in modules["economy"]:
             print(f"  [ERROR] 'economy.type' missing")
             valid = False
        else:
            print(f"  [OK] Economy type: {modules['economy']['type']}")
    else:
        print(f"  [WARNING] 'economy' module missing (optional?)")

    # Check Crafting
    if "crafting" in modules:
        if "type" not in modules["crafting"]:
             print(f"  [ERROR] 'crafting.type' missing")
             valid = False
        else:
            print(f"  [OK] Crafting type: {modules['crafting']['type']}")

    # Check Progression
    if "progression" in modules:
        if "type" not in modules["progression"]:
             print(f"  [ERROR] 'progression.type' missing")
             valid = False
        else:
            print(f"  [OK] Progression type: {modules['progression']['type']}")

    # Check Downtime
    if "downtime" in modules:
        if "enabled_activities" not in modules["downtime"]:
             print(f"  [ERROR] 'downtime.enabled_activities' missing")
             valid = False
        else:
            print(f"  [OK] Downtime activities: {modules['downtime']['enabled_activities']}")

    return valid

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    schema_path = os.path.join(base_dir, "aidm", "schemas", "narrative_profile_schema.json")
    profiles_dir = os.path.join(base_dir, "aidm", "libraries", "narrative_profiles")

    profiles_to_test = [
        "shonen_battle_profile.json",
        "isekai_fantasy_profile.json",
        "slice_of_life_profile.json"
    ]

    all_passed = True
    for profile_name in profiles_to_test:
        profile_path = os.path.join(profiles_dir, profile_name)
        if os.path.exists(profile_path):
            if not validate_profile(profile_path, schema_path):
                all_passed = False
                print(f"  [FAIL] {profile_name} validation failed.")
            else:
                print(f"  [PASS] {profile_name} validation passed.")
        else:
            print(f"  [ERROR] Profile {profile_name} not found.")
            all_passed = False
        print("-" * 20)

    if all_passed:
        print("\nAll profiles validated successfully against the mechanical schema requirements.")
        sys.exit(0)
    else:
        print("\nSome validations failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
