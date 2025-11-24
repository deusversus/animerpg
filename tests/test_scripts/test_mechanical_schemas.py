"""
Comprehensive Test Suite for Mechanical Meta-Schema System

Tests all system types, parameter validation, instantiation logic,
and edge cases. Ensures schemas and instantiation work correctly.

Run with: python test_mechanical_schemas.py
"""

import json
import sys
import os
from pathlib import Path

# Add parent directory to path to import mechanical_instantiation
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from aidm.lib.mechanical_instantiation import MechanicalInstantiator, instantiate_mechanical_systems


class TestResults:
    """Track test results."""
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.errors = []
    
    def add_pass(self, test_name):
        self.passed += 1
        print(f"✓ {test_name}")
    
    def add_fail(self, test_name, error):
        self.failed += 1
        self.errors.append((test_name, error))
        print(f"✗ {test_name}: {error}")
    
    def summary(self):
        total = self.passed + self.failed
        print(f"\n{'='*60}")
        print(f"Test Results: {self.passed}/{total} passed")
        if self.failed > 0:
            print(f"\nFailures:")
            for test_name, error in self.errors:
                print(f"  - {test_name}: {error}")
        print(f"{'='*60}")
        return self.failed == 0


results = TestResults()


def test_economy_fiat_currency():
    """Test fiat currency economy instantiation."""
    config = {
        "economy": {
            "type": "fiat_currency",
            "parameters": {
                "currency_name": "Jenny",
                "starting_amount": 200,
                "scarcity": "normal"
            }
        }
    }
    
    try:
        instantiator = MechanicalInstantiator()
        systems = instantiator.load_from_profile(config)
        
        assert systems["economy"]["type"] == "fiat_currency"
        assert systems["economy"]["currency_name"] == "Jenny"
        assert systems["economy"]["starting_amount"] == 200
        assert systems["economy"]["scarcity"] == "normal"
        assert systems["economy"]["mechanics"]["transactions"] == "standard_merchant_system"
        
        results.add_pass("Economy: Fiat Currency")
    except Exception as e:
        results.add_fail("Economy: Fiat Currency", str(e))


def test_economy_none():
    """Test no economy system."""
    config = {
        "economy": {
            "type": "none",
            "parameters": {}
        }
    }
    
    try:
        instantiator = MechanicalInstantiator()
        systems = instantiator.load_from_profile(config)
        
        assert systems["economy"]["type"] == "none"
        assert systems["economy"]["mechanics"]["transactions"] == "disabled"
        
        results.add_pass("Economy: None")
    except Exception as e:
        results.add_fail("Economy: None", str(e))


def test_economy_barter():
    """Test barter economy system."""
    config = {
        "economy": {
            "type": "barter",
            "parameters": {
                "trade_goods": ["food", "water", "ammo"],
                "value_ratios": {"food": 1, "water": 2, "ammo": 3}
            }
        }
    }
    
    try:
        instantiator = MechanicalInstantiator()
        systems = instantiator.load_from_profile(config)
        
        assert systems["economy"]["type"] == "barter"
        assert "food" in systems["economy"]["trade_goods"]
        assert systems["economy"]["mechanics"]["transactions"] == "negotiation_system"
        
        results.add_pass("Economy: Barter")
    except Exception as e:
        results.add_fail("Economy: Barter", str(e))


def test_crafting_skill_based():
    """Test skill-based crafting system."""
    config = {
        "crafting": {
            "type": "skill_based",
            "parameters": {
                "craft_focus": "weapons",
                "skill_stat": "INT",
                "quality_tiers": ["Poor", "Common", "Fine", "Masterwork"]
            }
        }
    }
    
    try:
        instantiator = MechanicalInstantiator()
        systems = instantiator.load_from_profile(config)
        
        assert systems["crafting"]["type"] == "skill_based"
        assert systems["crafting"]["craft_focus"] == "weapons"
        assert systems["crafting"]["skill_stat"] == "INT"
        assert len(systems["crafting"]["quality_tiers"]) == 4
        assert systems["crafting"]["mechanics"]["output"] == "variable_quality_item"
        
        results.add_pass("Crafting: Skill-Based")
    except Exception as e:
        results.add_fail("Crafting: Skill-Based", str(e))


def test_crafting_recipe_based():
    """Test recipe-based crafting system."""
    config = {
        "crafting": {
            "type": "recipe_based",
            "parameters": {
                "craft_focus": "potions",
                "material_categories": ["herbs", "minerals"],
                "recipe_source": "discovered",
                "failure_chance": True
            }
        }
    }
    
    try:
        instantiator = MechanicalInstantiator()
        systems = instantiator.load_from_profile(config)
        
        assert systems["crafting"]["type"] == "recipe_based"
        assert systems["crafting"]["failure_chance"] is True
        assert systems["crafting"]["mechanics"]["crafting_action"] == "combine_materials_with_recipe"
        
        results.add_pass("Crafting: Recipe-Based")
    except Exception as e:
        results.add_fail("Crafting: Recipe-Based", str(e))


def test_crafting_equivalent_exchange():
    """Test equivalent exchange crafting (FMA-style)."""
    config = {
        "crafting": {
            "type": "equivalent_exchange",
            "parameters": {
                "craft_focus": "alchemy",
                "exchange_law": "To create, something of equal value must be lost",
                "forbidden_transmutations": ["human_life", "gold"]
            }
        }
    }
    
    try:
        instantiator = MechanicalInstantiator()
        systems = instantiator.load_from_profile(config)
        
        assert systems["crafting"]["type"] == "equivalent_exchange"
        assert "human_life" in systems["crafting"]["forbidden_transmutations"]
        assert systems["crafting"]["mechanics"]["success_determination"] == "law_of_equivalent_exchange"
        
        results.add_pass("Crafting: Equivalent Exchange")
    except Exception as e:
        results.add_fail("Crafting: Equivalent Exchange", str(e))


def test_progression_mastery_tiers():
    """Test mastery tier progression (Nen-style)."""
    config = {
        "progression": {
            "type": "mastery_tiers",
            "parameters": {
                "system_name": "Nen",
                "mastery_levels": ["Novice", "Practitioner", "Expert", "Master"],
                "categories": ["Enhancement", "Transmutation"],
                "advancement_method": "training_arc"
            }
        }
    }
    
    try:
        instantiator = MechanicalInstantiator()
        systems = instantiator.load_from_profile(config)
        
        assert systems["progression"]["type"] == "mastery_tiers"
        assert systems["progression"]["system_name"] == "Nen"
        assert len(systems["progression"]["mastery_levels"]) == 4
        assert systems["progression"]["mechanics"]["leveling"] == "tier_based_unlock"
        
        results.add_pass("Progression: Mastery Tiers")
    except Exception as e:
        results.add_fail("Progression: Mastery Tiers", str(e))


def test_progression_class_based():
    """Test class-based progression."""
    config = {
        "progression": {
            "type": "class_based",
            "parameters": {
                "available_classes": ["Warrior", "Mage", "Rogue"],
                "multiclass_allowed": True,
                "max_level": 20,
                "stat_growth": "choice"
            }
        }
    }
    
    try:
        instantiator = MechanicalInstantiator()
        systems = instantiator.load_from_profile(config)
        
        assert systems["progression"]["type"] == "class_based"
        assert systems["progression"]["multiclass_allowed"] is True
        assert systems["progression"]["max_level"] == 20
        assert systems["progression"]["mechanics"]["skills"] == "class_skill_trees"
        
        results.add_pass("Progression: Class-Based")
    except Exception as e:
        results.add_fail("Progression: Class-Based", str(e))


def test_progression_quirk_awakening():
    """Test quirk awakening progression (MHA/One Piece style)."""
    config = {
        "progression": {
            "type": "quirk_awakening",
            "parameters": {
                "power_name": "Devil Fruit",
                "awakening_stages": ["Base", "Gear Second", "Awakening"],
                "evolution_triggers": ["near_death", "emotional_breakthrough"]
            }
        }
    }
    
    try:
        instantiator = MechanicalInstantiator()
        systems = instantiator.load_from_profile(config)
        
        assert systems["progression"]["type"] == "quirk_awakening"
        assert systems["progression"]["power_name"] == "Devil Fruit"
        assert len(systems["progression"]["awakening_stages"]) == 3
        assert systems["progression"]["mechanics"]["power_curve"] == "steep_at_awakening_moments"
        
        results.add_pass("Progression: Quirk Awakening")
    except Exception as e:
        results.add_fail("Progression: Quirk Awakening", str(e))


def test_progression_milestone_based():
    """Test milestone-based progression."""
    config = {
        "progression": {
            "type": "milestone_based",
            "parameters": {
                "milestone_events": ["event1", "event2"],
                "power_grants": {
                    "event1": ["skill1", "skill2"],
                    "event2": ["skill3"]
                }
            }
        }
    }
    
    try:
        instantiator = MechanicalInstantiator()
        systems = instantiator.load_from_profile(config)
        
        assert systems["progression"]["type"] == "milestone_based"
        assert len(systems["progression"]["milestone_events"]) == 2
        assert systems["progression"]["mechanics"]["leveling"] == "narrative_only"
        
        results.add_pass("Progression: Milestone-Based")
    except Exception as e:
        results.add_fail("Progression: Milestone-Based", str(e))


def test_progression_static_op():
    """Test static overpowered progression (Overlord-style)."""
    config = {
        "progression": {
            "type": "static_op",
            "parameters": {
                "starting_power_tier": 8,
                "growth_focus": "technique_variety"
            }
        }
    }
    
    try:
        instantiator = MechanicalInstantiator()
        systems = instantiator.load_from_profile(config)
        
        assert systems["progression"]["type"] == "static_op"
        assert systems["progression"]["starting_power_tier"] == 8
        assert systems["progression"]["active"] is False
        assert systems["progression"]["mechanics"]["leveling"] == "disabled"
        
        results.add_pass("Progression: Static OP")
    except Exception as e:
        results.add_fail("Progression: Static OP", str(e))


def test_downtime_multiple_modes():
    """Test downtime with multiple activity modes."""
    config = {
        "downtime": {
            "enabled_modes": ["training_arcs", "social_links", "investigation"],
            "default_mode": "training_arcs",
            "time_tracking": True
        }
    }
    
    try:
        instantiator = MechanicalInstantiator()
        systems = instantiator.load_from_profile(config)
        
        assert len(systems["downtime"]["enabled_modes"]) == 3
        assert "training_arcs" in systems["downtime"]["enabled_modes"]
        assert systems["downtime"]["default_mode"] == "training_arcs"
        assert systems["downtime"]["active"] is True
        
        results.add_pass("Downtime: Multiple Modes")
    except Exception as e:
        results.add_fail("Downtime: Multiple Modes", str(e))


def test_downtime_no_modes():
    """Test downtime with no activities (action-only anime)."""
    config = {
        "downtime": {
            "enabled_modes": [],
            "time_tracking": False
        }
    }
    
    try:
        instantiator = MechanicalInstantiator()
        systems = instantiator.load_from_profile(config)
        
        assert len(systems["downtime"]["enabled_modes"]) == 0
        assert systems["downtime"]["active"] is False
        
        results.add_pass("Downtime: No Modes")
    except Exception as e:
        results.add_fail("Downtime: No Modes", str(e))


def test_validation_invalid_economy_type():
    """Test validation catches invalid economy type."""
    config = {
        "economy": {
            "type": "invalid_type",
            "parameters": {}
        }
    }
    
    try:
        instantiator = MechanicalInstantiator()
        is_valid, errors = instantiator.validate_config(config)
        
        assert not is_valid
        assert len(errors) > 0
        assert "economy" in errors[0].lower()
        
        results.add_pass("Validation: Invalid Economy Type")
    except Exception as e:
        results.add_fail("Validation: Invalid Economy Type", str(e))


def test_validation_invalid_downtime_mode():
    """Test validation catches invalid downtime mode."""
    config = {
        "downtime": {
            "enabled_modes": ["invalid_mode", "training_arcs"]
        }
    }
    
    try:
        instantiator = MechanicalInstantiator()
        is_valid, errors = instantiator.validate_config(config)
        
        assert not is_valid
        assert "downtime" in errors[0].lower()
        
        results.add_pass("Validation: Invalid Downtime Mode")
    except Exception as e:
        results.add_fail("Validation: Invalid Downtime Mode", str(e))


def test_full_profile_hunter_x_hunter():
    """Test complete Hunter x Hunter profile."""
    config = {
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
    
    try:
        instantiator = MechanicalInstantiator()
        
        # Validate
        is_valid, errors = instantiator.validate_config(config)
        assert is_valid, f"Validation failed: {errors}"
        
        # Instantiate
        systems = instantiator.load_from_profile(config)
        
        # Verify all systems present
        assert "economy" in systems
        assert "crafting" in systems
        assert "progression" in systems
        assert "downtime" in systems
        
        # Spot check values
        assert systems["economy"]["currency_name"] == "Jenny"
        assert systems["progression"]["system_name"] == "Nen"
        assert len(systems["downtime"]["enabled_modes"]) == 2
        
        results.add_pass("Full Profile: Hunter x Hunter")
    except Exception as e:
        results.add_fail("Full Profile: Hunter x Hunter", str(e))


def test_full_profile_death_note():
    """Test complete Death Note profile (minimal systems)."""
    config = {
        "economy": {
            "type": "none",
            "parameters": {}
        },
        "crafting": {
            "type": "none",
            "parameters": {}
        },
        "progression": {
            "type": "milestone_based",
            "parameters": {
                "milestone_events": ["obtain_death_note", "discover_L"],
                "power_grants": {
                    "obtain_death_note": ["death_note_rules"],
                    "discover_L": ["investigation_skills"]
                }
            }
        },
        "downtime": {
            "enabled_modes": ["investigation", "social_links"],
            "default_mode": "investigation"
        }
    }
    
    try:
        instantiator = MechanicalInstantiator()
        
        # Validate
        is_valid, errors = instantiator.validate_config(config)
        assert is_valid, f"Validation failed: {errors}"
        
        # Instantiate
        systems = instantiator.load_from_profile(config)
        
        # Verify minimal systems
        assert systems["economy"]["type"] == "none"
        assert systems["crafting"]["type"] == "none"
        assert systems["economy"]["active"] is True  # System exists but disabled
        assert systems["crafting"]["active"] is False
        
        results.add_pass("Full Profile: Death Note")
    except Exception as e:
        results.add_fail("Full Profile: Death Note", str(e))


def run_all_tests():
    """Execute all test functions."""
    print("="*60)
    print("Mechanical Meta-Schema Test Suite")
    print("="*60)
    print()
    
    # Economy tests
    print("ECONOMY SYSTEMS")
    test_economy_fiat_currency()
    test_economy_none()
    test_economy_barter()
    print()
    
    # Crafting tests
    print("CRAFTING SYSTEMS")
    test_crafting_skill_based()
    test_crafting_recipe_based()
    test_crafting_equivalent_exchange()
    print()
    
    # Progression tests
    print("PROGRESSION SYSTEMS")
    test_progression_mastery_tiers()
    test_progression_class_based()
    test_progression_quirk_awakening()
    test_progression_milestone_based()
    test_progression_static_op()
    print()
    
    # Downtime tests
    print("DOWNTIME SYSTEMS")
    test_downtime_multiple_modes()
    test_downtime_no_modes()
    print()
    
    # Validation tests
    print("VALIDATION")
    test_validation_invalid_economy_type()
    test_validation_invalid_downtime_mode()
    print()
    
    # Integration tests
    print("FULL PROFILE INTEGRATION")
    test_full_profile_hunter_x_hunter()
    test_full_profile_death_note()
    print()
    
    # Summary
    success = results.summary()
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(run_all_tests())
