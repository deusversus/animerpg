# Mechanical Meta-Schema Implementation Plan

**Project**: AIDM Generative Mechanical Systems  
**Date**: November 23, 2025  
**Goal**: Enable profile-driven mechanical systems through parameterized meta-schemas  
**Architects**: Claude Sonnet 4.5 + Gemini 1.5 Pro  
**Status**: Design Complete → Implementation Pending

---

## Executive Summary

**Problem**: Current architecture has rigid, universal schemas (economy, crafting, factions) that don't adapt to anime-specific mechanics. This creates the illusion of "missing components" when in reality different anime need fundamentally different systems.

**Solution**: Replace universal schemas with **4 Parameterized Meta-Schemas** that get instantiated at Session Zero based on tiny configuration blocks in narrative profiles.

**Impact**:
- ✅ Each anime has mechanically distinct gameplay
- ✅ No timeout risk (config blocks are 5-10 lines)
- ✅ Infinite scalability (reuse 4 meta-schemas across 1000+ anime)
- ✅ Fills perceived gaps (crafting, downtime, social, etc.)
- ✅ Maintains validation/consistency (meta-schemas are pre-built and tested)

---

## Phase 1: Meta-Schema Design & Creation (Week 1-2)

### 1.1 Economy Meta-Schema

**File**: `aidm/libraries/mechanical_modules/economy_meta_schema.json`

**Supported Types**:
```json
{
  "schema_id": "meta_economy",
  "version": "1.0",
  "types": {
    "fiat_currency": {
      "description": "Standard currency system with named currency",
      "parameters": {
        "currency_name": { "type": "string", "required": true, "example": "Jenny" },
        "starting_amount": { "type": "number", "default": 200 },
        "scarcity": { "type": "enum", "values": ["abundant", "normal", "scarce"], "default": "normal" },
        "inflation_rate": { "type": "enum", "values": ["none", "low", "moderate", "high"], "default": "none" },
        "special_mechanics": { "type": "array", "items": "string", "optional": true }
      },
      "mechanics": {
        "transactions": "standard_merchant_system",
        "loot_generation": "currency_drops",
        "quest_rewards": "currency_based"
      }
    },
    "barter": {
      "description": "Trade goods directly without currency",
      "parameters": {
        "trade_goods": { "type": "array", "items": "string", "required": true },
        "value_ratios": { "type": "object", "required": true }
      },
      "mechanics": {
        "transactions": "negotiation_system",
        "loot_generation": "item_drops_only",
        "quest_rewards": "item_based"
      }
    },
    "abstract_wealth": {
      "description": "Wealth levels instead of exact currency",
      "parameters": {
        "wealth_levels": { "type": "array", "default": ["Poor", "Modest", "Comfortable", "Wealthy", "Rich"] },
        "lifestyle_costs": { "type": "object", "required": true }
      },
      "mechanics": {
        "transactions": "wealth_check_system",
        "loot_generation": "wealth_tier_increases",
        "quest_rewards": "lifestyle_upgrades"
      }
    },
    "reputation_based": {
      "description": "Social credit/reputation as currency",
      "parameters": {
        "reputation_name": { "type": "string", "required": true, "example": "Social Credit" },
        "gain_methods": { "type": "array", "items": "string", "required": true },
        "loss_methods": { "type": "array", "items": "string", "required": true }
      },
      "mechanics": {
        "transactions": "reputation_check_system",
        "loot_generation": "reputation_gains",
        "quest_rewards": "reputation_based"
      }
    },
    "none": {
      "description": "No economy system",
      "parameters": {},
      "mechanics": {
        "transactions": "disabled",
        "loot_generation": "narrative_only",
        "quest_rewards": "non_monetary"
      }
    }
  }
}
```

**Implementation Tasks**:
- [ ] Create JSON schema with all 5 types
- [ ] Define parameter validation rules
- [ ] Write instantiation logic (replace `{currency_name}` with config value)
- [ ] Create examples for each type
- [ ] Document integration with State Manager (Module 03)

**Estimated Time**: 8 hours

---

### 1.2 Crafting Meta-Schema

**File**: `aidm/libraries/mechanical_modules/crafting_meta_schema.json`

**Supported Types**:
```json
{
  "schema_id": "meta_crafting",
  "version": "1.0",
  "types": {
    "recipe_based": {
      "description": "Fixed recipes (MMO/RPG style)",
      "parameters": {
        "craft_focus": { "type": "string", "required": true, "example": "cards" },
        "recipe_source": { "type": "enum", "values": ["learned", "discovered", "innate"], "default": "learned" },
        "failure_chance": { "type": "boolean", "default": false },
        "material_categories": { "type": "array", "items": "string", "required": true }
      },
      "mechanics": {
        "crafting_action": "combine_materials_with_recipe",
        "success_determination": "skill_check_or_guaranteed",
        "output": "fixed_item_from_recipe"
      }
    },
    "skill_based": {
      "description": "Narrative skill checks determine outcome",
      "parameters": {
        "craft_focus": { "type": "string", "required": true, "example": "weapons" },
        "skill_stat": { "type": "enum", "values": ["INT", "WIS", "DEX"], "default": "INT" },
        "quality_tiers": { "type": "array", "default": ["Poor", "Common", "Fine", "Masterwork"] }
      },
      "mechanics": {
        "crafting_action": "skill_check_with_materials",
        "success_determination": "roll_vs_difficulty",
        "output": "variable_quality_item"
      }
    },
    "experimental": {
      "description": "Combine materials with unknown results (BotW style)",
      "parameters": {
        "craft_focus": { "type": "string", "required": true, "example": "alchemy" },
        "discovery_mode": { "type": "boolean", "default": true },
        "side_effects": { "type": "boolean", "default": true }
      },
      "mechanics": {
        "crafting_action": "combine_materials_freely",
        "success_determination": "emergent_system",
        "output": "unpredictable_with_patterns"
      }
    },
    "equivalent_exchange": {
      "description": "Sacrifice-based crafting (FMA style)",
      "parameters": {
        "craft_focus": { "type": "string", "required": true, "example": "alchemy" },
        "exchange_law": { "type": "string", "required": true },
        "forbidden_transmutations": { "type": "array", "items": "string", "optional": true }
      },
      "mechanics": {
        "crafting_action": "sacrifice_equal_value",
        "success_determination": "law_of_equivalent_exchange",
        "output": "transformation_with_cost"
      }
    },
    "none": {
      "description": "No crafting system",
      "parameters": {},
      "mechanics": {
        "crafting_action": "disabled"
      }
    }
  }
}
```

**Implementation Tasks**:
- [ ] Create JSON schema with all 5 types
- [ ] Define crafting mechanics for each type
- [ ] Write validation for material requirements
- [ ] Create recipe/formula storage system
- [ ] Document integration with Progression Systems (Module 09)

**Estimated Time**: 10 hours

---

### 1.3 Progression Meta-Schema

**File**: `aidm/libraries/mechanical_modules/progression_meta_schema.json`

**Supported Types**:
```json
{
  "schema_id": "meta_progression",
  "version": "1.0",
  "types": {
    "mastery_tiers": {
      "description": "Skill-based mastery progression (Hunter x Hunter Nen)",
      "parameters": {
        "system_name": { "type": "string", "required": true, "example": "Nen" },
        "mastery_levels": { "type": "array", "required": true, "example": ["Novice", "Initiate", "Practitioner", "Expert", "Master"] },
        "categories": { "type": "array", "items": "string", "required": true },
        "advancement_method": { "type": "enum", "values": ["practice_hours", "breakthrough", "training_arc"], "default": "practice_hours" }
      },
      "mechanics": {
        "leveling": "tier_based_unlock",
        "skills": "mastery_level_determines_access",
        "power_curve": "exponential_with_conditions"
      }
    },
    "class_based": {
      "description": "Traditional class/level system (D&D style)",
      "parameters": {
        "available_classes": { "type": "array", "items": "string", "required": true },
        "multiclass_allowed": { "type": "boolean", "default": false },
        "max_level": { "type": "number", "default": 20 },
        "stat_growth": { "type": "string", "enum": ["fixed", "random", "choice"], "default": "fixed" }
      },
      "mechanics": {
        "leveling": "xp_threshold_system",
        "skills": "class_skill_trees",
        "power_curve": "linear_with_capstone_abilities"
      }
    },
    "quirk_awakening": {
      "description": "Single power that evolves (MHA style)",
      "parameters": {
        "power_name": { "type": "string", "required": true, "example": "Quirk" },
        "awakening_stages": { "type": "array", "required": true, "example": ["Base", "Plus Ultra", "Awakened"] },
        "evolution_triggers": { "type": "array", "items": "string", "required": true }
      },
      "mechanics": {
        "leveling": "narrative_milestone_unlocks",
        "skills": "power_evolution_tree",
        "power_curve": "steep_at_awakening_moments"
      }
    },
    "milestone_based": {
      "description": "Story beats grant power (campaign-driven)",
      "parameters": {
        "milestone_events": { "type": "array", "items": "string", "required": true },
        "power_grants": { "type": "object", "required": true }
      },
      "mechanics": {
        "leveling": "narrative_only",
        "skills": "story_unlocked",
        "power_curve": "dm_controlled"
      }
    },
    "static_op": {
      "description": "No progression, already overpowered (Saitama)",
      "parameters": {
        "starting_power_tier": { "type": "number", "required": true, "min": 1, "max": 10 },
        "growth_focus": { "type": "string", "enum": ["none", "technique_variety", "control"], "default": "none" }
      },
      "mechanics": {
        "leveling": "disabled",
        "skills": "all_unlocked_or_static",
        "power_curve": "flat_maximum"
      }
    }
  }
}
```

**Implementation Tasks**:
- [ ] Create JSON schema with all 5 types
- [ ] Define XP/advancement calculations for each type
- [ ] Write tier/level unlock logic
- [ ] Create progression tracking system
- [ ] Document integration with Combat Resolution (Module 08)

**Estimated Time**: 12 hours

---

### 1.4 Downtime Meta-Schema

**File**: `aidm/libraries/mechanical_modules/downtime_meta_schema.json`

**Supported Types**:
```json
{
  "schema_id": "meta_downtime",
  "version": "1.0",
  "activity_modes": {
    "training_arcs": {
      "description": "Structured training for skill improvement",
      "parameters": {
        "training_types": { "type": "array", "items": "string", "required": true, "example": ["combat", "magic", "physical"] },
        "time_requirement": { "type": "string", "enum": ["days", "weeks", "months"], "default": "weeks" },
        "mentor_required": { "type": "boolean", "default": false },
        "breakthrough_chance": { "type": "boolean", "default": true }
      },
      "mechanics": {
        "activity": "extended_skill_training",
        "rewards": "stat_increases_skill_unlocks",
        "narrative_weight": "montage_or_detailed"
      }
    },
    "social_links": {
      "description": "Building relationships with NPCs (Persona style)",
      "parameters": {
        "link_types": { "type": "array", "items": "string", "required": true, "example": ["friendship", "romance", "rivalry"] },
        "benefits": { "type": "array", "items": "string", "required": true },
        "time_slots": { "type": "number", "default": 2 }
      },
      "mechanics": {
        "activity": "npc_interaction_scenes",
        "rewards": "affinity_bonuses_story_unlocks",
        "narrative_weight": "character_development"
      }
    },
    "investigation": {
      "description": "Research, clue-gathering, mystery-solving",
      "parameters": {
        "investigation_types": { "type": "array", "items": "string", "required": true, "example": ["research", "surveillance", "interrogation"] },
        "clue_system": { "type": "boolean", "default": true },
        "time_pressure": { "type": "boolean", "default": false }
      },
      "mechanics": {
        "activity": "skill_checks_for_information",
        "rewards": "knowledge_clues_plot_advancement",
        "narrative_weight": "detective_work"
      }
    },
    "travel": {
      "description": "Journeys between locations",
      "parameters": {
        "encounter_chance": { "type": "number", "min": 0, "max": 1, "default": 0.3 },
        "travel_mechanics": { "type": "enum", "values": ["abstract", "detailed", "montage"], "default": "abstract" },
        "resource_drain": { "type": "boolean", "default": true }
      },
      "mechanics": {
        "activity": "movement_with_events",
        "rewards": "discovery_encounters",
        "narrative_weight": "journey_focus"
      }
    },
    "faction_building": {
      "description": "Managing organization/nation (Overlord, Slime)",
      "parameters": {
        "management_focus": { "type": "array", "items": "string", "required": true, "example": ["military", "economy", "diplomacy"] },
        "automation_level": { "type": "enum", "values": ["manual", "semi_automated", "fully_automated"], "default": "semi_automated" }
      },
      "mechanics": {
        "activity": "strategic_decisions",
        "rewards": "faction_growth_resources",
        "narrative_weight": "kingdom_management"
      }
    },
    "slice_of_life": {
      "description": "Daily mundane activities",
      "parameters": {
        "activity_types": { "type": "array", "items": "string", "required": true, "example": ["cooking", "shopping", "hobbies"] },
        "narrative_focus": { "type": "boolean", "default": true }
      },
      "mechanics": {
        "activity": "character_moments",
        "rewards": "emotional_development",
        "narrative_weight": "quiet_scenes"
      }
    }
  },
  "configuration": {
    "description": "Anime profiles specify which modes are available",
    "parameters": {
      "enabled_modes": { "type": "array", "items": "string", "required": true },
      "default_mode": { "type": "string", "optional": true },
      "time_tracking": { "type": "boolean", "default": true }
    }
  }
}
```

**Implementation Tasks**:
- [ ] Create JSON schema with all 6 activity modes
- [ ] Define time management system
- [ ] Write reward calculation for each mode
- [ ] Create activity unlocking logic
- [ ] Document integration with NPC Intelligence (Module 04)

**Estimated Time**: 10 hours

---

## Phase 2: Narrative Profile Enhancement (Week 2-3)

### 2.1 Add Mechanical Config Sections

**Target**: All existing narrative profiles (20 profiles)

**New Section Template**:
```markdown
## Mechanical Configuration

```json
{
  "economy": {
    "type": "fiat_currency",
    "currency_name": "Jenny",
    "starting_amount": 200,
    "scarcity": "normal",
    "special_mechanics": ["hunter_licenses", "greed_island_cards"]
  },
  "crafting": {
    "type": "skill_based",
    "craft_focus": "cards",
    "skill_stat": "INT",
    "quality_tiers": ["Common", "Rare", "Legendary"]
  },
  "progression": {
    "type": "mastery_tiers",
    "system_name": "Nen",
    "mastery_levels": ["Novice", "Initiate", "Practitioner", "Expert", "Master"],
    "categories": ["Enhancement", "Transmutation", "Emission", "Conjuration", "Manipulation", "Specialization"],
    "advancement_method": "training_arc"
  },
  "downtime": {
    "enabled_modes": ["training_arcs", "social_links", "investigation"],
    "default_mode": "training_arcs"
  }
}
```
```

**Implementation Tasks**:
- [ ] Review each of 20 narrative profiles
- [ ] Determine appropriate config for each anime
- [ ] Add mechanical config section (10-15 lines per profile)
- [ ] Validate JSON syntax
- [ ] Cross-reference with anime source material

**Per Profile**: ~30 minutes  
**Total Time**: 10 hours

---

### 2.2 Update Narrative Profile Generator

**File**: `aidm/instructions/07_anime_integration.md` (already exists)

**Enhancement**: Add step to Research Protocol

**Current Research Output**:
```
MECHANICS: [power systems, world rules]
NARRATIVE DNA: [scales, tropes, styles]
```

**Enhanced Research Output**:
```
MECHANICS: [power systems, world rules]
NARRATIVE DNA: [scales, tropes, styles]
MECHANICAL CONFIG: [economy type, crafting type, progression type, downtime modes]
```

**New Prompt Addition** (for AI generators):
```markdown
### Step 2.5: Mechanical System Classification

After extracting mechanics and narrative DNA, classify the anime's mechanical systems:

**ECONOMY SYSTEM**: 
- Type: fiat_currency | barter | abstract_wealth | reputation_based | none
- If fiat: What's the currency name?
- Special mechanics? (bounties, licenses, etc.)

**CRAFTING SYSTEM**:
- Type: recipe_based | skill_based | experimental | equivalent_exchange | none
- If exists: What's the craft focus? (weapons, cards, potions, etc.)

**PROGRESSION SYSTEM**:
- Type: mastery_tiers | class_based | quirk_awakening | milestone_based | static_op
- System name? (Nen, Quirks, Chakra, etc.)
- How do characters advance?

**DOWNTIME ACTIVITIES**:
- Which modes are present? training_arcs | social_links | investigation | travel | faction_building | slice_of_life
- What's the primary downtime focus?

Output as JSON config block (see template).
```

**Implementation Tasks**:
- [ ] Add Mechanical System Classification section to Module 07
- [ ] Create decision tree for each meta-schema type
- [ ] Add examples for 5 common anime
- [ ] Update Research Protocol checklist
- [ ] Test on 3 new anime profiles

**Estimated Time**: 6 hours

---

## Phase 3: Session Zero Integration (Week 3-4)

### 3.1 Update Module 06 (Session Zero)

**File**: `aidm/instructions/06_session_zero.md`

**New Phase**: Phase 0.7 - Mechanical System Loading (After Phase 0.6 OP Protagonist Detection)

**Addition**:
```markdown
### Phase 0.7: MECHANICAL SYSTEM LOADING (After Narrative Calibration)

**Goal**: Load profile-specific mechanical systems based on narrative profile config

**Trigger**: Automatically after narrative profile loaded

**Process**:
1. Read `mechanical_config` from loaded narrative profile
2. For each system (economy, crafting, progression, downtime):
   - Load corresponding meta-schema
   - Instantiate with profile parameters
   - Validate configuration
   - Store in campaign state
3. Present mechanical summary to player
4. Proceed to Phase 1 (Character Concept)

**Example Output**:
```
AIDM: "Hunter x Hunter profile loaded! Here are the mechanical systems 
for this campaign:

💰 ECONOMY: Jenny currency system (you'll start with 200 Jenny)
🛠️ CRAFTING: Skill-based card creation (Greed Island style)
📈 PROGRESSION: Nen mastery system (6 categories, 5 mastery tiers)
⏰ DOWNTIME: Training arcs, social links, and investigation available

These systems will shape how you interact with the world. Ready to create 
your character?"
```

**Completion Criteria**:
- ✅ All 4 meta-schemas instantiated with profile parameters
- ✅ Campaign state populated with mechanical configs
- ✅ Player aware of active systems
- ✅ Systems ready for gameplay integration
```

**Implementation Tasks**:
- [ ] Add Phase 0.7 to Module 06
- [ ] Write meta-schema loading logic
- [ ] Create instantiation validation
- [ ] Design player-facing summary format
- [ ] Update phase completion checklist

**Estimated Time**: 6 hours

---

### 3.2 State Manager Integration

**File**: `aidm/instructions/03_state_manager.md`

**New Schema Fields**:
```json
{
  "world_state": {
    "mechanical_systems": {
      "economy": {
        "type": "fiat_currency",
        "config": { /* instantiated from meta-schema */ },
        "active": true
      },
      "crafting": {
        "type": "skill_based",
        "config": { /* instantiated from meta-schema */ },
        "active": true
      },
      "progression": {
        "type": "mastery_tiers",
        "config": { /* instantiated from meta-schema */ },
        "active": true
      },
      "downtime": {
        "enabled_modes": ["training_arcs", "social_links"],
        "config": { /* instantiated from meta-schema */ },
        "active": true
      }
    }
  }
}
```

**Implementation Tasks**:
- [ ] Update `world_state_schema.json` with mechanical_systems field
- [ ] Create validation rules for instantiated configs
- [ ] Write getter/setter methods for mechanical system access
- [ ] Document integration points for other modules
- [ ] Create state migration script for existing campaigns

**Estimated Time**: 8 hours

---

## Phase 4: Module Integration (Week 4-5)

### 4.1 Economy System Integration

**Affected Modules**:
- Module 03 (State Manager): Currency tracking
- Module 04 (NPC Intelligence): Merchant behavior
- Module 08 (Combat Resolution): Loot drops
- Module 09 (Progression Systems): Quest rewards

**Implementation Tasks**:
- [ ] Update merchant transaction logic to read economy config
- [ ] Modify loot generation to respect economy type
- [ ] Add currency conversion for multi-currency worlds
- [ ] Create economy-specific validation rules
- [ ] Test with all 5 economy types

**Estimated Time**: 10 hours

---

### 4.2 Crafting System Integration

**Affected Modules**:
- Module 03 (State Manager): Inventory management
- Module 09 (Progression Systems): Crafting skill progression
- Module 05 (Narrative Systems): Crafting scene generation

**Implementation Tasks**:
- [ ] Create crafting action handler for each type
- [ ] Add material tracking system
- [ ] Write recipe/formula storage system
- [ ] Implement skill check logic for skill_based type
- [ ] Test with all 5 crafting types

**Estimated Time**: 12 hours

---

### 4.3 Progression System Integration

**Affected Modules**:
- Module 09 (Progression Systems): Primary integration point
- Module 08 (Combat Resolution): Power scaling in combat
- Module 12 (Narrative Scaling): Adjust narrative to power tier

**Implementation Tasks**:
- [ ] Update XP/advancement calculation to respect progression type
- [ ] Create mastery tier tracking for mastery_tiers type
- [ ] Implement class skill tree logic for class_based type
- [ ] Add milestone tracking for milestone_based type
- [ ] Handle static_op type (disable progression)
- [ ] Test with all 5 progression types

**Estimated Time**: 14 hours

---

### 4.4 Downtime System Integration

**Affected Modules**:
- Module 04 (NPC Intelligence): Social links
- Module 09 (Progression Systems): Training rewards
- Module 05 (Narrative Systems): Downtime scene generation

**Implementation Tasks**:
- [ ] Create downtime activity menu generator
- [ ] Implement time tracking system
- [ ] Write reward calculation for each activity mode
- [ ] Add activity unlocking logic
- [ ] Create downtime scene templates
- [ ] Test with all 6 activity modes

**Estimated Time**: 12 hours

---

## Phase 5: Testing & Validation (Week 5-6)

### 5.1 Unit Tests

**Test Coverage**:
- [ ] Meta-schema validation (all types load correctly)
- [ ] Parameter instantiation (replace placeholders with config values)
- [ ] Config validation (reject invalid configurations)
- [ ] State persistence (mechanical systems save/load)
- [ ] Module integration (each module accesses correct config)

**Estimated Time**: 16 hours

---

### 5.2 Integration Tests

**Test Scenarios**:
1. **Full Hunter x Hunter Campaign** (fiat economy, skill crafting, mastery progression, training downtime)
2. **Death Note Campaign** (no economy, no crafting, milestone progression, investigation downtime)
3. **Overlord Campaign** (fiat economy, experimental crafting, static_op progression, faction_building downtime)
4. **Multi-Anime Fusion** (mixed systems from 3 different anime)
5. **Custom Anime Profile** (create new anime, generate config, run campaign)

**For Each Scenario**:
- [ ] Session Zero completes successfully
- [ ] Mechanical systems load correctly
- [ ] Character creation uses appropriate mechanics
- [ ] Gameplay respects system constraints
- [ ] State updates persist correctly
- [ ] No timeout or performance issues

**Estimated Time**: 20 hours

---

### 5.3 Documentation

**Create**:
- [ ] Meta-Schema Reference Guide (for developers)
- [ ] Mechanical Config Guide (for profile creators)
- [ ] Session Zero Mechanical Loading Guide (for players)
- [ ] Troubleshooting Guide (common issues)
- [ ] Migration Guide (updating existing profiles)

**Estimated Time**: 12 hours

---

## Phase 6: Deployment & Rollout (Week 6)

### 6.1 Existing Profile Migration

**Target**: 20 existing narrative profiles

**Process**:
1. Review profile for anime-specific mechanics
2. Determine appropriate meta-schema types
3. Add mechanical config section
4. Validate JSON syntax
5. Test in Session Zero
6. Document any edge cases

**Estimated Time**: 10 hours (30 min per profile)

---

### 6.2 User Communication

**Announcements**:
- [ ] Update README.md with new capabilities
- [ ] Create "What's New" document
- [ ] Write migration guide for existing campaigns
- [ ] Update quickstart guide

**Estimated Time**: 4 hours

---

## Total Effort Estimation

| Phase | Task | Hours |
|-------|------|-------|
| **Phase 1** | Economy Meta-Schema | 8 |
| | Crafting Meta-Schema | 10 |
| | Progression Meta-Schema | 12 |
| | Downtime Meta-Schema | 10 |
| **Phase 2** | Enhance 20 Profiles | 10 |
| | Update Generator | 6 |
| **Phase 3** | Session Zero Integration | 6 |
| | State Manager Integration | 8 |
| **Phase 4** | Economy Integration | 10 |
| | Crafting Integration | 12 |
| | Progression Integration | 14 |
| | Downtime Integration | 12 |
| **Phase 5** | Unit Tests | 16 |
| | Integration Tests | 20 |
| | Documentation | 12 |
| **Phase 6** | Profile Migration | 10 |
| | User Communication | 4 |
| **TOTAL** | | **180 hours** |

**Timeline**: 6 weeks (30 hours/week)  
**Team Size**: 2 developers (or 1 developer, 12 weeks)

---

## Success Criteria

**System is successful when**:
1. ✅ All 4 meta-schemas are complete and validated
2. ✅ 20 existing profiles have mechanical configs
3. ✅ Session Zero loads mechanical systems automatically
4. ✅ All modules respect mechanical system configs
5. ✅ 5 test scenarios pass without errors
6. ✅ Documentation is complete
7. ✅ No timeout issues during profile generation
8. ✅ Players report distinct mechanical experience per anime
9. ✅ New profiles can be created in <1 hour (including mechanical config)
10. ✅ System scales to 100+ profiles without performance degradation

---

## Risk Mitigation

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Meta-schema too complex | Medium | High | Start with minimal viable types, expand later |
| Timeout during loading | Low | Medium | Lazy-load meta-schemas, cache in memory |
| Config validation errors | Medium | Medium | Extensive unit tests, clear error messages |
| Module integration breaks | Medium | High | Incremental integration, test after each module |
| User confusion | Medium | Low | Clear documentation, examples in every profile |
| Performance degradation | Low | High | Profile loading performance, optimize if needed |

---

## Next Steps

1. **Review & Approve Plan**: Stakeholder sign-off
2. **Create GitHub Issues**: Break down tasks into trackable issues
3. **Set Up Development Environment**: Clone repo, set up testing framework
4. **Begin Phase 1**: Start with Economy Meta-Schema (simplest)
5. **Weekly Check-ins**: Progress review, adjust timeline as needed

---

## Appendix A: Example Mechanical Configs

### Hunter x Hunter
```json
{
  "economy": {
    "type": "fiat_currency",
    "currency_name": "Jenny",
    "starting_amount": 200,
    "scarcity": "normal",
    "special_mechanics": ["hunter_licenses", "greed_island_cards"]
  },
  "crafting": {
    "type": "skill_based",
    "craft_focus": "cards",
    "skill_stat": "INT",
    "quality_tiers": ["Common", "Rare", "Legendary"]
  },
  "progression": {
    "type": "mastery_tiers",
    "system_name": "Nen",
    "mastery_levels": ["Novice", "Initiate", "Practitioner", "Expert", "Master"],
    "categories": ["Enhancement", "Transmutation", "Emission", "Conjuration", "Manipulation", "Specialization"],
    "advancement_method": "training_arc"
  },
  "downtime": {
    "enabled_modes": ["training_arcs", "social_links", "investigation"],
    "default_mode": "training_arcs"
  }
}
```

### Death Note
```json
{
  "economy": {
    "type": "none"
  },
  "crafting": {
    "type": "none"
  },
  "progression": {
    "type": "milestone_based",
    "milestone_events": ["obtain_death_note", "discover_L", "yotsuba_arc", "final_confrontation"],
    "power_grants": {
      "obtain_death_note": ["death_note_rules", "shinigami_eyes_option"],
      "discover_L": ["investigation_skills", "tactical_thinking"],
      "yotsuba_arc": ["memory_manipulation", "strategic_planning"],
      "final_confrontation": ["master_manipulator", "endgame_abilities"]
    }
  },
  "downtime": {
    "enabled_modes": ["investigation", "social_links"],
    "default_mode": "investigation"
  }
}
```

### Overlord (Ainz Ooal Gown)
```json
{
  "economy": {
    "type": "fiat_currency",
    "currency_name": "Gold",
    "starting_amount": 1000000,
    "scarcity": "abundant",
    "special_mechanics": ["nazarick_treasury", "yggdrasil_items"]
  },
  "crafting": {
    "type": "experimental",
    "craft_focus": "magic_items",
    "discovery_mode": true,
    "side_effects": true
  },
  "progression": {
    "type": "static_op",
    "starting_power_tier": 8,
    "growth_focus": "technique_variety"
  },
  "downtime": {
    "enabled_modes": ["faction_building", "social_links", "investigation"],
    "default_mode": "faction_building"
  }
}
```

### One Piece
```json
{
  "economy": {
    "type": "fiat_currency",
    "currency_name": "Berry",
    "starting_amount": 100,
    "scarcity": "normal",
    "special_mechanics": ["bounties", "treasure_hunting"]
  },
  "crafting": {
    "type": "none"
  },
  "progression": {
    "type": "quirk_awakening",
    "power_name": "Devil Fruit",
    "awakening_stages": ["Base", "Gear Second", "Gear Third", "Gear Fourth", "Awakening"],
    "evolution_triggers": ["life_threatening_battle", "emotional_breakthrough", "training_with_mentor", "understanding_power_nature"]
  },
  "downtime": {
    "enabled_modes": ["training_arcs", "social_links", "travel"],
    "default_mode": "travel"
  }
}
```

### Haikyuu (Sports Anime - No Combat)
```json
{
  "economy": {
    "type": "none"
  },
  "crafting": {
    "type": "none"
  },
  "progression": {
    "type": "class_based",
    "available_classes": ["Setter", "Spiker", "Libero", "Middle Blocker"],
    "multiclass_allowed": false,
    "max_level": 20,
    "stat_growth": "choice"
  },
  "downtime": {
    "enabled_modes": ["training_arcs", "social_links", "slice_of_life"],
    "default_mode": "training_arcs"
  }
}
```

---

## Appendix B: Meta-Schema File Structure

```
aidm/libraries/mechanical_modules/
├── economy_meta_schema.json
├── crafting_meta_schema.json
├── progression_meta_schema.json
├── downtime_meta_schema.json
├── examples/
│   ├── hunter_x_hunter_mechanical_config.json
│   ├── death_note_mechanical_config.json
│   ├── overlord_mechanical_config.json
│   ├── one_piece_mechanical_config.json
│   └── haikyuu_mechanical_config.json
└── README.md (usage guide)
```

---

**END OF IMPLEMENTATION PLAN**
