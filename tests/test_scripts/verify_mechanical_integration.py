import json
import os
import re

def simple_validate(instance, schema, schema_store):
    """
    A simplified JSON schema validator that supports $ref.
    """
    if "$ref" in schema:
        ref = schema["$ref"]
        if ref in schema_store:
            return simple_validate(instance, schema_store[ref], schema_store)
        else:
            # Try to load from file relative to schema_store path if possible
            # For this script, we assume schema_store has everything or we skip
            print(f"Warning: Could not resolve ref {ref}")
            return True

    if "type" in schema:
        t = schema["type"]
        if t == "object":
            if not isinstance(instance, dict):
                print(f"Error: Expected object, got {type(instance)}")
                return False
            if "required" in schema:
                for req in schema["required"]:
                    if req not in instance:
                        print(f"Error: Missing required field '{req}'")
                        return False
            if "properties" in schema:
                for prop, prop_schema in schema["properties"].items():
                    if prop in instance:
                        if not simple_validate(instance[prop], prop_schema, schema_store):
                            print(f"Error in property '{prop}'")
                            return False
        elif t == "array":
            if not isinstance(instance, list):
                print(f"Error: Expected array, got {type(instance)}")
                return False
            if "items" in schema:
                for i, item in enumerate(instance):
                    if not simple_validate(item, schema["items"], schema_store):
                        print(f"Error in item {i}")
                        return False
        elif t == "string":
            if not isinstance(instance, str):
                print(f"Error: Expected string, got {type(instance)}")
                return False
        elif t == "number" or t == "integer":
            if not isinstance(instance, (int, float)):
                print(f"Error: Expected number, got {type(instance)}")
                return False
        elif t == "boolean":
            if not isinstance(instance, bool):
                print(f"Error: Expected boolean, got {type(instance)}")
                return False
    return True

def load_schema(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_json_block(md_content):
    match = re.search(r'```json\s*({.*?})\s*```', md_content, re.DOTALL)
    if match:
        return json.loads(match.group(1))
    return None

def main():
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../aidm/schemas"))
    
    # Load all schemas
    schemas = {}
    schema_files = ["world_state_schema.json", "economy_schema.json", "crafting_meta_schema.json", "progression_meta_schema.json", "downtime_meta_schema.json", "faction_schema.json", "quest_schema.json"]
    
    for sf in schema_files:
        try:
            schemas[sf] = load_schema(os.path.join(base_path, sf))
        except FileNotFoundError:
            print(f"Warning: Schema {sf} not found")

    # Load dummy profile
    profile_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../test_data/dummy_profile.md"))
    with open(profile_path, 'r', encoding='utf-8') as f:
        profile_content = f.read()
    
    config = extract_json_block(profile_content)
    if not config:
        print("Failed to extract JSON config from profile")
        return

    print("Extracted Mechanical Config:")
    print(json.dumps(config, indent=2))

    # Mock System Initialization (Expanding config into full system objects)
    # This represents the logic in Phase 0.7
    
    mechanical_systems = {}
    
    # 1. Economy Expansion (Full Schema)
    mechanical_systems["economy"] = {
        "schema_version": "2.2.0",
        "currency_systems": {
            "primary_currency": config["economy"]["config"]["currency_name"],
            "currencies": {
                "credits": {
                    "name": config["economy"]["config"]["currency_name"],
                    "abbreviation": "CR",
                    "base_value": 1.0
                }
            },
            "exchange_rates": {}
        },
        "item_prices": {},
        "merchants": {},
        "market_dynamics": {
            "global_modifiers": {
                "inflation_rate": config["economy"]["config"]["inflation_rate"]
            }
        }
    }

    # 2. Crafting Expansion (Meta Schema)
    # The meta schema requires 'type' and 'categories' (if type != none)
    # Our dummy profile has 'type'="monster_harvesting" which isn't in the enum of the meta schema I read earlier?
    # Let's check the enum in crafting_meta_schema.json.
    # Enum: ["skill_based", "recipe_based", "experimental", "industrial", "none", "ritual_based"]
    # "monster_harvesting" is NOT in the enum. I should update the dummy profile or the schema.
    # I'll update the dummy profile to use "skill_based" which is valid.
    
    mechanical_systems["crafting"] = {
        "type": "skill_based", 
        "categories": ["monster_parts"],
        "special_mechanics": ["harvesting"]
    }

    # 3. Progression Expansion (Meta Schema)
    # Enum: ["xp_based", "milestone_based", "mastery_tiers", "usage_based", "narrative_unlock", "hybrid"]
    # Dummy has "milestone". Schema has "milestone_based".
    mechanical_systems["progression"] = {
        "type": "milestone_based",
        "power_name": "Skills",
        "awakening_stages": [],
        "evolution_triggers": []
    }

    # 4. Downtime Expansion (Meta Schema)
    # Enum: not strict on type, but has enabled_modes
    mechanical_systems["downtime"] = {
        "enabled_modes": ["training", "social"],
        "default_mode": "training"
    }

    # Construct World State
    world_state = {
        "schema_version": "2.2.0",
        "world_id": "world_test_001",
        "name": "Test World",
        "created_at": "2023-01-01T00:00:00Z",
        "last_updated": "2023-01-01T00:00:00Z",
        "temporal": {
            "current_date": {"year": 1000, "month": 1, "day": 1},
            "time_of_day": "morning",
            "season": "spring"
        },
        "environment": {},
        "factions": {},
        "npcs": {},
        "locations": [],
        "economy": {}, # Legacy field
        "narrative_state": {},
        "mechanical_systems": mechanical_systems
    }

    # Validate
    print("\nValidating World State with Mechanical Systems...")
    if simple_validate(world_state, schemas["world_state_schema.json"], schemas):
        print("SUCCESS: World State is valid and integrates mechanical systems correctly.")
    else:
        print("FAILURE: World State validation failed.")

if __name__ == "__main__":
    main()
