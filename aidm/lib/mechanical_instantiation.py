"""
Mechanical Meta-Schema Instantiation System

This module converts profile mechanical configs (10-15 line blocks) into
full system objects ready for gameplay. Handles parameter expansion,
validation, and default population.

Usage:
    from aidm.lib.mechanical_instantiation import MechanicalInstantiator
    
    instantiator = MechanicalInstantiator()
    systems = instantiator.load_from_profile(profile_config)
    # Returns: {economy: {...}, crafting: {...}, progression: {...}, downtime: {...}}
"""

import json
import os
from typing import Dict, Any, Optional
from pathlib import Path


class MechanicalInstantiator:
    """Expands profile mechanical configs into full system objects."""
    
    def __init__(self, schema_dir: Optional[str] = None):
        """
        Initialize instantiator with meta-schema definitions.
        
        Args:
            schema_dir: Path to schemas directory (default: ../../aidm/schemas)
        """
        if schema_dir is None:
            # Default to workspace schemas
            base_path = Path(__file__).parent.parent.parent
            schema_dir = base_path / "aidm" / "schemas"
        
        self.schema_dir = Path(schema_dir)
        self.meta_schemas = self._load_meta_schemas()
    
    def _load_meta_schemas(self) -> Dict[str, Dict]:
        """Load all meta-schema definitions."""
        schemas = {}
        schema_files = [
            "economy_meta_schema.json",
            "crafting_meta_schema.json",
            "progression_meta_schema.json",
            "downtime_meta_schema.json"
        ]
        
        for filename in schema_files:
            schema_path = self.schema_dir / filename
            if schema_path.exists():
                with open(schema_path, 'r', encoding='utf-8') as f:
                    system_name = filename.replace('_meta_schema.json', '')
                    schemas[system_name] = json.load(f)
            else:
                print(f"Warning: Schema {filename} not found")
        
        return schemas
    
    def load_from_profile(self, profile_config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert profile mechanical config into full system objects.
        
        Args:
            profile_config: Dict with keys: economy, crafting, progression, downtime
        
        Returns:
            Dict of instantiated systems ready for world_state.mechanical_systems
        """
        systems = {}
        
        if "economy" in profile_config:
            systems["economy"] = self.instantiate_economy(profile_config["economy"])
        
        if "crafting" in profile_config:
            systems["crafting"] = self.instantiate_crafting(profile_config["crafting"])
        
        if "progression" in profile_config:
            systems["progression"] = self.instantiate_progression(profile_config["progression"])
        
        if "downtime" in profile_config:
            systems["downtime"] = self.instantiate_downtime(profile_config["downtime"])
        
        return systems
    
    def instantiate_economy(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Expand economy config into full system object.
        
        Args:
            config: Profile economy config with 'type' and 'parameters'
        
        Returns:
            Full economy system object
        """
        economy_type = config.get("type")
        parameters = config.get("parameters", {})
        
        # Base structure
        system = {
            "type": economy_type,
            "active": True
        }
        
        # Type-specific expansion
        if economy_type == "fiat_currency":
            system["currency_name"] = parameters.get("currency_name", "Gold")
            system["starting_amount"] = parameters.get("starting_amount", 200)
            system["scarcity"] = parameters.get("scarcity", "normal")
            system["inflation_rate"] = parameters.get("inflation_rate", "none")
            system["special_mechanics"] = parameters.get("special_mechanics", [])
            system["mechanics"] = {
                "transactions": "standard_merchant_system",
                "loot_generation": "currency_drops",
                "quest_rewards": "currency_based"
            }
        
        elif economy_type == "barter":
            system["trade_goods"] = parameters.get("trade_goods", [])
            system["value_ratios"] = parameters.get("value_ratios", {})
            system["mechanics"] = {
                "transactions": "negotiation_system",
                "loot_generation": "item_drops_only",
                "quest_rewards": "item_based"
            }
        
        elif economy_type == "abstract_wealth":
            system["wealth_levels"] = parameters.get("wealth_levels", 
                                                     ["Poor", "Modest", "Comfortable", "Wealthy", "Rich"])
            system["lifestyle_costs"] = parameters.get("lifestyle_costs", {})
            system["mechanics"] = {
                "transactions": "wealth_check_system",
                "loot_generation": "wealth_tier_increases",
                "quest_rewards": "lifestyle_upgrades"
            }
        
        elif economy_type == "reputation_based":
            system["reputation_name"] = parameters.get("reputation_name", "Reputation")
            system["gain_methods"] = parameters.get("gain_methods", [])
            system["loss_methods"] = parameters.get("loss_methods", [])
            system["mechanics"] = {
                "transactions": "reputation_check_system",
                "loot_generation": "reputation_gains",
                "quest_rewards": "reputation_based"
            }
        
        elif economy_type == "none":
            system["mechanics"] = {
                "transactions": "disabled",
                "loot_generation": "narrative_only",
                "quest_rewards": "non_monetary"
            }
        
        return system
    
    def instantiate_crafting(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Expand crafting config into full system object.
        
        Args:
            config: Profile crafting config with 'type' and 'parameters'
        
        Returns:
            Full crafting system object
        """
        crafting_type = config.get("type")
        parameters = config.get("parameters", {})
        
        system = {
            "type": crafting_type,
            "active": crafting_type != "none"
        }
        
        if crafting_type == "recipe_based":
            system["craft_focus"] = parameters.get("craft_focus", "items")
            system["recipe_source"] = parameters.get("recipe_source", "learned")
            system["failure_chance"] = parameters.get("failure_chance", False)
            system["material_categories"] = parameters.get("material_categories", [])
            system["mechanics"] = {
                "crafting_action": "combine_materials_with_recipe",
                "success_determination": "skill_check_or_guaranteed",
                "output": "fixed_item_from_recipe"
            }
        
        elif crafting_type == "skill_based":
            system["craft_focus"] = parameters.get("craft_focus", "items")
            system["skill_stat"] = parameters.get("skill_stat", "INT")
            system["quality_tiers"] = parameters.get("quality_tiers", 
                                                     ["Poor", "Common", "Fine", "Masterwork"])
            system["mechanics"] = {
                "crafting_action": "skill_check_with_materials",
                "success_determination": "roll_vs_difficulty",
                "output": "variable_quality_item"
            }
        
        elif crafting_type == "experimental":
            system["craft_focus"] = parameters.get("craft_focus", "alchemy")
            system["discovery_mode"] = parameters.get("discovery_mode", True)
            system["side_effects"] = parameters.get("side_effects", True)
            system["mechanics"] = {
                "crafting_action": "combine_materials_freely",
                "success_determination": "emergent_system",
                "output": "unpredictable_with_patterns"
            }
        
        elif crafting_type == "equivalent_exchange":
            system["craft_focus"] = parameters.get("craft_focus", "alchemy")
            system["exchange_law"] = parameters.get("exchange_law", 
                                                    "To create, something of equal value must be lost")
            system["forbidden_transmutations"] = parameters.get("forbidden_transmutations", [])
            system["mechanics"] = {
                "crafting_action": "sacrifice_equal_value",
                "success_determination": "law_of_equivalent_exchange",
                "output": "transformation_with_cost"
            }
        
        elif crafting_type == "none":
            system["mechanics"] = {
                "crafting_action": "disabled"
            }
        
        return system
    
    def instantiate_progression(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Expand progression config into full system object.
        
        Args:
            config: Profile progression config with 'type' and 'parameters'
        
        Returns:
            Full progression system object
        """
        progression_type = config.get("type")
        parameters = config.get("parameters", {})
        
        system = {
            "type": progression_type,
            "active": progression_type != "static_op"
        }
        
        if progression_type == "mastery_tiers":
            system["system_name"] = parameters.get("system_name", "Power System")
            system["mastery_levels"] = parameters.get("mastery_levels", 
                                                      ["Novice", "Initiate", "Practitioner", "Expert", "Master"])
            system["categories"] = parameters.get("categories", [])
            system["advancement_method"] = parameters.get("advancement_method", "practice_hours")
            system["mechanics"] = {
                "leveling": "tier_based_unlock",
                "skills": "mastery_level_determines_access",
                "power_curve": "exponential_with_conditions"
            }
        
        elif progression_type == "class_based":
            system["available_classes"] = parameters.get("available_classes", [])
            system["multiclass_allowed"] = parameters.get("multiclass_allowed", False)
            system["max_level"] = parameters.get("max_level", 20)
            system["stat_growth"] = parameters.get("stat_growth", "fixed")
            system["mechanics"] = {
                "leveling": "xp_threshold_system",
                "skills": "class_skill_trees",
                "power_curve": "linear_with_capstone_abilities"
            }
        
        elif progression_type == "quirk_awakening":
            system["power_name"] = parameters.get("power_name", "Power")
            system["awakening_stages"] = parameters.get("awakening_stages", [])
            system["evolution_triggers"] = parameters.get("evolution_triggers", [])
            system["mechanics"] = {
                "leveling": "narrative_milestone_unlocks",
                "skills": "power_evolution_tree",
                "power_curve": "steep_at_awakening_moments"
            }
        
        elif progression_type == "milestone_based":
            system["milestone_events"] = parameters.get("milestone_events", [])
            system["power_grants"] = parameters.get("power_grants", {})
            system["mechanics"] = {
                "leveling": "narrative_only",
                "skills": "story_unlocked",
                "power_curve": "dm_controlled"
            }
        
        elif progression_type == "static_op":
            system["starting_power_tier"] = parameters.get("starting_power_tier", 5)
            system["growth_focus"] = parameters.get("growth_focus", "none")
            system["mechanics"] = {
                "leveling": "disabled",
                "skills": "all_unlocked_or_static",
                "power_curve": "flat_maximum"
            }
        
        return system
    
    def instantiate_downtime(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Expand downtime config into full system object.
        
        Args:
            config: Profile downtime config with 'enabled_modes'
        
        Returns:
            Full downtime system object
        """
        system = {
            "enabled_modes": config.get("enabled_modes", []),
            "default_mode": config.get("default_mode"),
            "time_tracking": config.get("time_tracking", True),
            "active": len(config.get("enabled_modes", [])) > 0
        }
        
        # Add activity-specific parameters if provided
        if "training_arcs" in system["enabled_modes"]:
            system["training_config"] = config.get("training_config", {
                "time_requirement": "weeks",
                "mentor_required": False,
                "breakthrough_chance": True
            })
        
        if "social_links" in system["enabled_modes"]:
            system["social_config"] = config.get("social_config", {
                "time_slots": 2,
                "benefits": ["affinity_bonuses", "story_unlocks"]
            })
        
        if "faction_building" in system["enabled_modes"]:
            system["faction_config"] = config.get("faction_config", {
                "automation_level": "semi_automated"
            })
        
        return system
    
    def validate_config(self, config: Dict[str, Any]) -> tuple[bool, list[str]]:
        """
        Validate profile config against meta-schemas.
        
        Args:
            config: Profile mechanical config
        
        Returns:
            Tuple of (is_valid: bool, errors: list[str])
        """
        errors = []
        
        # Validate economy
        if "economy" in config:
            economy_type = config["economy"].get("type")
            if economy_type not in ["fiat_currency", "barter", "abstract_wealth", "reputation_based", "none"]:
                errors.append(f"Invalid economy type: {economy_type}")
        
        # Validate crafting
        if "crafting" in config:
            crafting_type = config["crafting"].get("type")
            if crafting_type not in ["recipe_based", "skill_based", "experimental", "equivalent_exchange", "none"]:
                errors.append(f"Invalid crafting type: {crafting_type}")
        
        # Validate progression
        if "progression" in config:
            progression_type = config["progression"].get("type")
            if progression_type not in ["mastery_tiers", "class_based", "quirk_awakening", "milestone_based", "static_op"]:
                errors.append(f"Invalid progression type: {progression_type}")
        
        # Validate downtime
        if "downtime" in config:
            enabled_modes = config["downtime"].get("enabled_modes", [])
            valid_modes = ["training_arcs", "social_links", "investigation", "travel", "faction_building", "slice_of_life"]
            for mode in enabled_modes:
                if mode not in valid_modes:
                    errors.append(f"Invalid downtime mode: {mode}")
        
        return (len(errors) == 0, errors)


# Convenience function
def instantiate_mechanical_systems(profile_config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Quick function to instantiate mechanical systems from profile config.
    
    Args:
        profile_config: Dict with economy, crafting, progression, downtime configs
    
    Returns:
        Dict of instantiated systems
    """
    instantiator = MechanicalInstantiator()
    return instantiator.load_from_profile(profile_config)


if __name__ == "__main__":
    # Example usage
    test_config = {
        "economy": {
            "type": "fiat_currency",
            "parameters": {
                "currency_name": "Jenny",
                "starting_amount": 200,
                "scarcity": "normal"
            }
        },
        "crafting": {
            "type": "skill_based",
            "parameters": {
                "craft_focus": "cards",
                "skill_stat": "INT"
            }
        },
        "progression": {
            "type": "mastery_tiers",
            "parameters": {
                "system_name": "Nen",
                "mastery_levels": ["Novice", "Practitioner", "Expert", "Master"],
                "categories": ["Enhancement", "Transmutation", "Emission"]
            }
        },
        "downtime": {
            "enabled_modes": ["training_arcs", "social_links"],
            "default_mode": "training_arcs"
        }
    }
    
    instantiator = MechanicalInstantiator()
    
    # Validate
    is_valid, errors = instantiator.validate_config(test_config)
    if not is_valid:
        print("Validation Errors:")
        for error in errors:
            print(f"  - {error}")
    else:
        print("✓ Config is valid")
    
    # Instantiate
    systems = instantiator.load_from_profile(test_config)
    
    print("\nInstantiated Systems:")
    print(json.dumps(systems, indent=2))
