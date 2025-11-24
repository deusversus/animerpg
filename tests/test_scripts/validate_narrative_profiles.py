"""
Validation script for all 20 narrative profiles.
Ensures mechanical configs match rebuilt meta-schema structure.

Run with: python validate_narrative_profiles.py
"""

import json
import re
from pathlib import Path

# Profile directory
PROFILE_DIR = Path(__file__).parent.parent.parent / "aidm" / "libraries" / "narrative_profiles"

# Expected 20 profiles
EXPECTED_PROFILES = [
    "attack_on_titan_profile.md",
    "code_geass_profile.md",
    "cowboy_bebop_profile.md",
    "dandadan_profile.md",
    "death_note_profile.md",
    "demon_slayer_profile.md",
    "fullmetal_alchemist_brotherhood_profile.md",
    "haikyuu_profile.md",
    "hunter_x_hunter_profile.md",
    "jujutsu_kaisen_profile.md",
    "konosuba_profile.md",
    "mushishi_profile.md",
    "my_hero_academia_profile.md",
    "naruto_profile.md",
    "neon_genesis_evangelion_profile.md",
    "one_piece_profile.md",
    "one_punch_man_profile.md",
    "rezero_profile.md",
    "steins_gate_profile.md",
    "vinland_saga_profile.md"
]

# Valid enum values
VALID_ECONOMY_TYPES = ["fiat_currency", "barter", "abstract_wealth", "reputation_based", "none"]
VALID_CRAFTING_TYPES = ["skill_based", "recipe_based", "experimental", "equivalent_exchange", "none"]
VALID_PROGRESSION_TYPES = ["mastery_tiers", "class_based", "quirk_awakening", "milestone_based", "static_op"]
VALID_DOWNTIME_MODES = ["training_arcs", "slice_of_life", "investigation", "travel", "faction_building", "social_links"]


class ValidationResults:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.errors = []
    
    def add_pass(self, profile_name):
        self.passed += 1
        print(f"✓ {profile_name}")
    
    def add_fail(self, profile_name, error):
        self.failed += 1
        self.errors.append((profile_name, error))
        print(f"✗ {profile_name}: {error}")
    
    def summary(self):
        total = self.passed + self.failed
        print(f"\n{'='*70}")
        print(f"Validation Results: {self.passed}/{total} profiles valid")
        if self.failed > 0:
            print(f"\nFailures:")
            for profile_name, error in self.errors:
                print(f"  - {profile_name}: {error}")
        print(f"{'='*70}")
        return self.failed == 0


def extract_mechanical_config(profile_path):
    """Extract mechanical configuration JSON from markdown file."""
    content = profile_path.read_text(encoding='utf-8')
    
    # Find mechanical configuration section
    match = re.search(r'## Mechanical Configuration\s*```json\s*(\{.*?\})\s*```', content, re.DOTALL)
    if not match:
        return None, "No mechanical configuration found"
    
    try:
        config = json.loads(match.group(1))
        return config, None
    except json.JSONDecodeError as e:
        return None, f"Invalid JSON: {e}"


def validate_nested_structure(config, profile_name):
    """Validate that config uses nested parameters structure."""
    errors = []
    
    # Check economy
    if "economy" not in config:
        errors.append("Missing 'economy' section")
    else:
        economy = config["economy"]
        if "type" not in economy:
            errors.append("economy: missing 'type' field")
        elif economy["type"] not in VALID_ECONOMY_TYPES:
            errors.append(f"economy: invalid type '{economy['type']}'")
        
        if "parameters" not in economy:
            errors.append("economy: missing 'parameters' object (flat structure detected)")
        
        # Check for old flat structure fields at root level
        flat_fields = ["currency_name", "starting_amount", "scarcity", "trade_goods"]
        for field in flat_fields:
            if field in economy:
                errors.append(f"economy: flat structure field '{field}' at root (should be in 'parameters')")
    
    # Check crafting
    if "crafting" not in config:
        errors.append("Missing 'crafting' section")
    else:
        crafting = config["crafting"]
        if "type" not in crafting:
            errors.append("crafting: missing 'type' field")
        elif crafting["type"] not in VALID_CRAFTING_TYPES:
            errors.append(f"crafting: invalid type '{crafting['type']}'")
        
        if "parameters" not in crafting:
            errors.append("crafting: missing 'parameters' object (flat structure detected)")
        
        # Check for old flat structure fields
        flat_fields = ["craft_focus", "skill_stat", "categories", "material_categories"]
        for field in flat_fields:
            if field in crafting:
                errors.append(f"crafting: flat structure field '{field}' at root (should be in 'parameters')")
    
    # Check progression
    if "progression" not in config:
        errors.append("Missing 'progression' section")
    else:
        progression = config["progression"]
        if "type" not in progression:
            errors.append("progression: missing 'type' field")
        elif progression["type"] not in VALID_PROGRESSION_TYPES:
            errors.append(f"progression: invalid type '{progression['type']}'")
        
        if "parameters" not in progression:
            errors.append("progression: missing 'parameters' object (flat structure detected)")
        
        # Check for old flat structure fields
        flat_fields = ["power_name", "system_name", "mastery_levels", "awakening_stages", "milestone_events"]
        for field in flat_fields:
            if field in progression:
                errors.append(f"progression: flat structure field '{field}' at root (should be in 'parameters')")
    
    # Check downtime
    if "downtime" not in config:
        errors.append("Missing 'downtime' section")
    else:
        downtime = config["downtime"]
        if "enabled_modes" not in downtime:
            errors.append("downtime: missing 'enabled_modes' field")
        else:
            for mode in downtime["enabled_modes"]:
                if mode not in VALID_DOWNTIME_MODES:
                    errors.append(f"downtime: invalid mode '{mode}'")
        
        # Check for activity_configs if modes are enabled
        if downtime.get("enabled_modes") and len(downtime.get("enabled_modes", [])) > 0:
            if "activity_configs" not in downtime:
                # This is a warning, not an error (optional field)
                pass
    
    return errors


def validate_all_profiles():
    """Validate all 20 narrative profiles."""
    results = ValidationResults()
    
    print("="*70)
    print("Narrative Profile Validation Suite")
    print("Validating 20 profiles for nested parameters structure")
    print("="*70)
    print()
    
    for profile_name in EXPECTED_PROFILES:
        profile_path = PROFILE_DIR / profile_name
        
        if not profile_path.exists():
            results.add_fail(profile_name, "File not found")
            continue
        
        # Extract config
        config, error = extract_mechanical_config(profile_path)
        if error:
            results.add_fail(profile_name, error)
            continue
        
        # Validate structure
        errors = validate_nested_structure(config, profile_name)
        if errors:
            results.add_fail(profile_name, "; ".join(errors))
        else:
            results.add_pass(profile_name)
    
    return results.summary()


if __name__ == "__main__":
    import sys
    success = validate_all_profiles()
    sys.exit(0 if success else 1)
