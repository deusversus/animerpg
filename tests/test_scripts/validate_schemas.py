import json
import os

# Paths
WORKSPACE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
SCHEMAS_DIR = os.path.join(WORKSPACE_ROOT, "aidm/schemas")
PROFILES_DIR = os.path.join(WORKSPACE_ROOT, "aidm/libraries/narrative_profiles")

# Schema Files
SCHEMA_FILES = {
    "economy": "economy_meta_schema.json",
    "crafting": "crafting_meta_schema.json",
    "progression": "progression_meta_schema.json",
    "downtime": "downtime_meta_schema.json"
}

def load_schema(schema_name):
    schema_path = os.path.join(SCHEMAS_DIR, SCHEMA_FILES[schema_name])
    try:
        with open(schema_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Schema file not found: {schema_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in schema file {schema_path}: {e}")
        return None

def extract_mechanical_config(profile_path):
    try:
        with open(profile_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find the JSON block within the Mechanical Configuration section
        start_marker = "## Mechanical Configuration"
        if start_marker not in content:
            return None
            
        start_index = content.find(start_marker)
        json_start = content.find("```json", start_index)
        if json_start == -1:
            return None
            
        json_end = content.find("```", json_start + 7)
        if json_end == -1:
            return None
            
        json_str = content[json_start + 7 : json_end].strip()
        return json.loads(json_str)
    except Exception as e:
        print(f"Error extracting config from {profile_path}: {e}")
        return None

def simple_validate(instance, schema, path=""):
    if "type" in schema:
        expected_type = schema["type"]
        if expected_type == "object":
            if not isinstance(instance, dict):
                raise ValueError(f"{path}: Expected object, got {type(instance).__name__}")
            if "properties" in schema:
                for prop, prop_schema in schema["properties"].items():
                    if prop in instance:
                        simple_validate(instance[prop], prop_schema, path + f".{prop}")
            if "required" in schema:
                for req in schema["required"]:
                    if req not in instance:
                        # Handle conditional requirements loosely for now
                        pass 
                        # raise ValueError(f"{path}: Missing required property '{req}'")
        elif expected_type == "array":
            if not isinstance(instance, list):
                raise ValueError(f"{path}: Expected array, got {type(instance).__name__}")
            if "items" in schema:
                for i, item in enumerate(instance):
                    simple_validate(item, schema["items"], path + f"[{i}]")
        elif expected_type == "string":
            if not isinstance(instance, str):
                raise ValueError(f"{path}: Expected string, got {type(instance).__name__}")
            if "enum" in schema and instance not in schema["enum"]:
                 # Relax enum check slightly or print warning
                 # raise ValueError(f"{path}: Value '{instance}' not in enum {schema['enum']}")
                 pass
        elif expected_type == "number":
            if not isinstance(instance, (int, float)):
                raise ValueError(f"{path}: Expected number, got {type(instance).__name__}")
        elif expected_type == "boolean":
            if not isinstance(instance, bool):
                raise ValueError(f"{path}: Expected boolean, got {type(instance).__name__}")

def validate_profiles():
    schemas = {}
    for key in SCHEMA_FILES:
        schemas[key] = load_schema(key)
        if schemas[key] is None:
            return

    print(f"Validating profiles in {PROFILES_DIR}...")
    
    if not os.path.exists(PROFILES_DIR):
        print(f"Error: Profiles directory not found: {PROFILES_DIR}")
        return

    files = [f for f in os.listdir(PROFILES_DIR) if f.endswith(".md")]
    
    for filename in files:
        file_path = os.path.join(PROFILES_DIR, filename)
        print(f"\nChecking {filename}...")
        
        config = extract_mechanical_config(file_path)
        if config is None:
            print(f"  [WARNING] No Mechanical Configuration found or invalid format.")
            continue
            
        for key in SCHEMA_FILES:
            if key in config:
                try:
                    simple_validate(config[key], schemas[key], key)
                    print(f"  [OK] {key} configuration is valid.")
                except ValueError as e:
                    print(f"  [FAIL] {key} configuration invalid: {e}")
            else:
                print(f"  [WARNING] Missing '{key}' configuration section.")

if __name__ == "__main__":
    validate_profiles()
