# AIDM Comprehensive Test Execution Guide

**Document Version**: 2.0 (Phase 4 Integration)  
**Last Updated**: November 23, 2025  
**System Version**: AIDM v2.5 (Phase 4 Complete)

---

## Overview

This guide provides step-by-step instructions for executing all 13 AIDM test scripts. These tests validate the complete system from basic onboarding through advanced mechanical integration.

**Test Categories**:
- **Legacy Tests** (TEST-1 through TEST-9): Core functionality, updated for Phase 4
- **Phase 4 Tests** (TEST-10 through TEST-13): Mechanical systems integration

---

## System Requirements

### LLM Platform Requirements

**Recommended Platforms**:
- Claude Sonnet 4.5 (preferred - best reasoning + web search)
- ChatGPT-4o (acceptable - good performance)
- Claude Opus 3.5 (acceptable - high quality)

**Required Capabilities**:
- **Context Window**: 128K+ tokens (200K+ preferred)
- **Web Search**: Enabled (for anime research validation)
- **File Support**: Attachment OR copy-paste capability
- **Structured Output**: JSON generation for export tests

### Workspace Setup

**Required Files** (Current System State):

#### A. Core Instructions (1 file)
```
📁 aidm/CORE_AIDM_INSTRUCTIONS.md
```

#### B. Instruction Modules (14 files - Phase 4 Complete)
```
📁 aidm/instructions/00_system_initialization.md
📁 aidm/instructions/01_cognitive_engine.md
📁 aidm/instructions/02_learning_engine.md
📁 aidm/instructions/03_state_manager.md
📁 aidm/instructions/04_npc_intelligence.md
📁 aidm/instructions/05_narrative_systems.md
📁 aidm/instructions/06_session_zero.md
📁 aidm/instructions/07_anime_integration.md
📁 aidm/instructions/08_combat_resolution.md
📁 aidm/instructions/09_progression_systems.md
📁 aidm/instructions/10_error_recovery.md
📁 aidm/instructions/11_dice_resolution.md
📁 aidm/instructions/12_narrative_scaling.md
📁 aidm/instructions/13_narrative_calibration.md
```

#### C. Schema Definitions (15+ files - Phase 4 Complete)
```
📁 aidm/schemas/character_schema.json (v2.3.0)
📁 aidm/schemas/npc_schema.json
📁 aidm/schemas/quest_schema.json
📁 aidm/schemas/world_state_schema.json
📁 aidm/schemas/faction_schema.json
📁 aidm/schemas/anime_world_schema.json
📁 aidm/schemas/power_system_schema.json
📁 aidm/schemas/narrative_profile_schema.json
📁 aidm/schemas/memory_thread_schema.json
📁 aidm/schemas/economy_schema.json
📁 aidm/schemas/session_export_schema.json
```

#### D. Meta-Schemas (4 files - Phase 4 Mechanical Systems)
```
📁 aidm/schemas/economy_meta_schema.json
📁 aidm/schemas/crafting_meta_schema.json
📁 aidm/schemas/progression_meta_schema.json
📁 aidm/schemas/downtime_meta_schema.json
```

#### E. Python Libraries (1 file - Phase 4)
```
📁 aidm/libraries/common_mechanics/mechanical_instantiation.py
```

#### F. Support Libraries (Load as needed)
```
📁 aidm/libraries/power_systems/ (5 files: mana, ki, soul, psionic, scaling)
📁 aidm/libraries/genre_tropes/ (4+ files: isekai, shonen, seinen, slice_of_life)
📁 aidm/libraries/narrative_profiles/ (anime-specific configs, if available)
📁 aidm/libraries/common_mechanics/ (leveling curves, skill taxonomies)
```

**Total Core Files**: 31+ files (~60,000+ lines)

---

## File Loading Protocol

### Standard Loading Sequence

For all tests, load files in this order:

1. **Core Instructions** (1 file)
2. **Instruction Modules** (14 files, in numerical order 00-13)
3. **Schemas** (15+ files, alphabetical)
4. **Meta-Schemas** (4 files, for mechanical system tests)
5. **Python Libraries** (mechanical_instantiation.py for Phase 4 tests)
6. **Support Libraries** (as needed per test)

### Quick Load Command (Copy-Paste Template)

```
AIDM System Loading...

Core Instructions: ✅ CORE_AIDM_INSTRUCTIONS.md
Modules (14): ✅ 00-13 loaded
Schemas (15+): ✅ All standard schemas loaded
Meta-Schemas (4): ✅ Economy, Crafting, Progression, Downtime
Python Libraries: ✅ mechanical_instantiation.py

System Status: READY
AIDM Version: v2.5 (Phase 4 Complete)
Mechanical Systems: ENABLED

Awaiting player input to begin Session Zero.
```

### Verification Checklist

Before starting any test, verify:

- [ ] All 14 instruction modules loaded (00-13)
- [ ] All 15+ schemas loaded (including session_export_schema.json)
- [ ] 4 meta-schemas loaded (economy, crafting, progression, downtime)
- [ ] mechanical_instantiation.py loaded (for Phase 4 tests)
- [ ] Support libraries loaded (per test requirements)
- [ ] LLM confirms system ready

---

## Test Execution Procedures

### TEST-1: Cold Start (Naruto World)

**File**: `tests/test_scripts/TEST_1_COLD_START.md`  
**Priority**: CRITICAL  
**Phase 4 Focus**: Session Zero Phase 3 (MECHANICAL BUILD)

**Key Validation Points**:
- 6-phase Session Zero process (includes Phase 3: MECHANICAL BUILD)
- Currency: Ryo (NOT gold)
- Progression: mastery_tiers (ninja ranks, NOT D&D levels)
- tier_xp field present (NOT character_xp)
- Downtime: training_arcs + investigation

**Quick Start**:
1. Load all core files + ki_lifeforce_systems.md
2. Player: "I want to play in a world like Naruto"
3. Proceed through Session Zero (6 phases)
4. Validate mechanical systems display (Phase 3)
5. Complete character creation
6. Check character sheet for Ryo, tier_xp, ninja rank

---

### TEST-2: Multi-Anime Fusion

**File**: `tests/test_scripts/TEST_2_MULTI_ANIME_FUSION.md`  
**Priority**: HIGH  
**Phase 4 Focus**: Mechanical system fusion resolution

**Key Validation Points**:
- Currency conflict resolution (Ryo vs Gold vs Yen → ONE currency)
- Progression conflict resolution (mastery_tiers vs class_based vs quirk_awakening → coherent system)
- Downtime overlap resolution (enabled_modes clearly defined)
- Session Zero Phase 3 displays mechanical fusion
- Character sheet uses unified currency

**Quick Start**:
1. Load all core files + all 5 power system libraries
2. Player: "I want Naruto + Solo Leveling + My Hero Academia fusion"
3. Watch for Session Zero Phase 3 mechanical conflict resolution
4. Verify AIDM proposes coherent fusion
5. Check character sheet for unified currency (Yen in example)
6. Validate hybrid progression tracks (XP + demonstrations + awakenings)

---

### TEST-3: Session Persistence

**File**: `tests/test_scripts/TEST_3_SESSION_PERSISTENCE.md`  
**Priority**: HIGH  
**Phase 4 Focus**: mechanical_systems export/import

**Key Validation Points**:
- mechanical_systems section in export JSON
- Currency: Jenny (NOT gold) preserved
- Progression: mastery_tiers (tier_xp field) preserved
- tier_xp value correct (4200/5000 in example)
- Downtime: enabled_modes preserved

**Quick Start**:
1. **Session 1**: Load files, create HxH character (Jenny, mastery_tiers)
2. Play 20 turns (combat, NPCs, quests)
3. Export state (meta-command for JSON)
4. **Session 2**: Fresh LLM, load files again
5. Import state (paste JSON)
6. Verify mechanical_systems restored (Jenny, mastery_tiers, tier_xp)

---

### TEST-4: Combat Mechanics

**File**: `tests/test_scripts/TEST_4_COMBAT_MECHANICS.md`  
**Priority**: CRITICAL  
**Phase 4 Focus**: Progression-type-specific XP formulas

**Key Validation Points**:
- **PART A**: Core combat (HP/MP/SP tracking, skill validation)
- **PART B**: 5 progression type scenarios:
  - mastery_tiers: Tier bonuses (+2 attack), technique XP, tier_xp tracking
  - class_based: Standard XP formula, class feature bonus
  - quirk_awakening: Near-death trigger, awakening sequence, dual tracks
  - milestone_based: Minimal combat XP (×0.1), massive milestone rewards
  - static_op: Zero combat XP, token quest XP, no leveling

**Quick Start**:
1. Load all core files + progression_meta_schema.json
2. **Part A**: Standard combat test (~30 min)
3. **Part B**: Run 5 separate progression type scenarios (~60-90 min)
4. Validate XP formulas match progression type
5. Check tier bonuses, awakening triggers, zero-XP enforcement

---

### TEST-5: Memory Coherence

**File**: `tests/test_scripts/TEST_5_MEMORY_COHERENCE.md`  
**Priority**: HIGH  
**Phase 4 Note**: NPC memory independent of mechanical systems

**Key Validation Points**:
- NPCs remember previous conversations
- Affinity changes persist
- No contradictions in NPC knowledge
- Information propagates between NPCs

**Quick Start**:
1. Load all core files + npc_schema.json + memory_thread_schema.json
2. Create traveling merchant character
3. Meet 3-4 NPCs, build relationships
4. Test affinity progression (0 → +5 → +20)
5. Verify NPCs remember player across 20+ exchanges

---

### TEST-6: Error Recovery

**File**: `tests/test_scripts/TEST_6_ERROR_RECOVERY.md`  
**Priority**: CRITICAL  
**Phase 4 Focus**: Mechanical system error correction

**Key Validation Points**:
- HP/math errors corrected gracefully
- Inventory errors fixed immediately
- Lore/name corrections accepted
- Quest/plot errors acknowledged
- Tone/genre errors corrected
- **NEW**: Mechanical errors fixed (XP → tier_xp, gold → Jenny, Level → Tier)

**Quick Start**:
1. Load all core files
2. Run 6 error scenarios (HP, inventory, lore, plot, tone, mechanical)
3. For mechanical test: Setup mastery_tiers, inject error (uses XP/gold), correct
4. Validate correction persists

---

### TEST-7: Genre Adaptation

**File**: `tests/test_scripts/TEST_7_GENRE_ADAPTATION.md`  
**Priority**: MEDIUM  
**Phase 4 Focus**: Mechanical systems match genre

**Key Validation Points**:
- **Isekai**: class_based progression, stat screens, fast pacing
- **Shonen**: mastery_tiers progression, training arcs, dramatic battles
- **Slice-of-Life**: minimal progression (milestone_based or static_op), slow pacing

**Quick Start**:
1. Load all core files + all 4 genre trope libraries
2. **Session A**: Isekai (Solo Leveling style) - validate class_based progression
3. **Session B**: Shonen (Naruto style) - validate mastery_tiers progression
4. **Session C**: Slice-of-Life (school setting) - validate minimal progression
5. Check mechanical systems adapt to genre

---

### TEST-8: Research Validation

**File**: `tests/test_scripts/TEST_8_RESEARCH_VALIDATION.md`  
**Priority**: MEDIUM  
**Phase 4 Focus**: Mechanical systems research

**Key Validation Points**:
- Known anime recognized correctly (Attack on Titan)
- Obscure anime uncertainty admitted (Land of the Lustrous)
- Fake anime NO hallucination (Neo-Tokyo 2099)
- **NEW**: Mechanical systems research (Hunter x Hunter → Jenny, mastery_tiers, training_arcs)

**Quick Start**:
1. Load all core files + narrative_profiles (if available)
2. Test known anime research (Attack on Titan walls)
3. Test obscure anime (Land of the Lustrous)
4. Test fake anime (Neo-Tokyo 2099) - MUST NOT hallucinate
5. **NEW**: Test mechanical research (HxH → Jenny, mastery_tiers)
6. Test custom override (HxH with D&D leveling)

---

### TEST-9: Session Zero Mechanical Integration

**File**: `tests/test_scripts/TEST_9_SESSION_ZERO_MECHANICAL_INTEGRATION.md`  
**Priority**: CRITICAL  
**Phase 4 Focus**: Phase 3 validation + gameplay integration

**Key Validation Points**:
- **PART 1**: Session Zero Phase 3 displays (TC-9.1 through TC-9.6)
  - Hunter x Hunter: Jenny, mastery_tiers, training_arcs
  - My Hero Academia: Yen, quirk_awakening, slice_of_life
  - Konosuba: Eris, debt, class_based
- **PART 2**: Gameplay validation (TC-9.7 through TC-9.12)
  - Module 03: Economy (loot with Jenny, quest rewards)
  - Module 05: Downtime (activity_configs, enabled_modes)
  - Module 08: Combat Progression (mastery_tiers XP, tier bonuses)
  - Module 09: Leveling (tier advancement demonstration)

**Quick Start**:
1. Load all core files + 4 meta-schemas
2. Run TC-9.1: Hunter x Hunter Session Zero
3. Validate Phase 3 displays (Jenny, mastery_tiers, training_arcs)
4. Continue gameplay (TC-9.7 through TC-9.10)
5. Validate all 4 modules read from session_state.mechanical_systems

---

### TEST-10: Economy Integration

**File**: `tests/test_scripts/TEST-10_ECONOMY_INTEGRATION.md`  
**Priority**: HIGH  
**Phase 4 Integration**: Module 03 validation

**Key Validation Points**:
- Currency by profile (Jenny/Eris/Yen)
- Loot generation with profile currency
- Quest rewards with profile currency
- Scarcity mechanics apply
- Special mechanics (debt, barter) work

**Quick Start**:
1. Load all core files + economy_meta_schema.json
2. Test 3 anime: HxH (Jenny), MHA (Yen), Konosuba (Eris + debt)
3. Validate loot/quest rewards use correct currency
4. Check scarcity affects prices
5. Test special mechanics (Konosuba debt system)

---

### TEST-11: Downtime Integration

**File**: `tests/test_scripts/TEST-11_DOWNTIME_INTEGRATION.md`  
**Priority**: HIGH  
**Phase 4 Integration**: Module 05 validation

**Key Validation Points**:
- 6 downtime modes: training_arcs, investigation, slice_of_life, travel, faction_building, social_links
- Only enabled_modes offered
- activity_configs apply (time, DC, XP rate, bonuses)
- Training arcs essential for mastery_tiers progression

**Quick Start**:
1. Load all core files + downtime_meta_schema.json
2. Test 3 profiles: HxH (training_arcs), MHA (slice_of_life), Solo Leveling (all modes)
3. Validate only enabled_modes offered
4. Execute training arc (2 weeks, WIS DC 16, 1.5× XP, Ko unlock)
5. Check activity_configs apply

---

### TEST-12: Combat Progression Integration

**File**: `tests/test_scripts/TEST-12_COMBAT_PROGRESSION_INTEGRATION.md`  
**Priority**: HIGH  
**Phase 4 Integration**: Module 08 validation

**Key Validation Points**:
- 5 progression types validated in combat
- XP formulas match progression type
- Tier bonuses apply (mastery_tiers)
- Awakening triggers detected (quirk_awakening)
- Zero XP enforced (static_op)

**Quick Start**:
1. Load all core files + progression_meta_schema.json
2. Test 5 progression types (same as TEST-4 Part B)
3. Validate XP calculation per type
4. Check tier bonuses in combat (+2 attack/defense)
5. Test awakening trigger (HP < 10%)
6. Verify zero XP for static_op

---

### TEST-13: Leveling Mechanics

**File**: `tests/test_scripts/TEST-13_LEVELING_MECHANICS.md`  
**Priority**: HIGH  
**Phase 4 Integration**: Module 09 validation

**Key Validation Points**:
- Type-specific advancement rules
- mastery_tiers: Demonstration required, NO auto-level
- class_based: Standard XP threshold, auto-level
- quirk_awakening: Dual tracks (levels + awakenings)
- milestone_based: Story grants, bypass XP
- static_op: No advancement ever

**Quick Start**:
1. Load all core files + progression_meta_schema.json
2. Test mastery_tiers advancement (threshold exceeded → demonstration quest)
3. Test class_based advancement (threshold exceeded → auto-level)
4. Test quirk_awakening (near-death → awakening sequence)
5. Test milestone_based (major story → direct level grant)
6. Test static_op (combat → 0 XP, no advancement)

---

## Common Issues & Troubleshooting

### File Loading Issues

**Issue**: "Files too large to paste"  
**Solution**: Use file attachment feature OR load in batches (core → modules → schemas)

**Issue**: "LLM doesn't recognize AIDM instructions"  
**Solution**: Re-paste CORE_AIDM_INSTRUCTIONS.md, confirm with "You are AIDM. Confirm ready status."

**Issue**: "Missing meta-schemas"  
**Solution**: Verify 4 meta-schemas loaded: economy, crafting, progression, downtime

### Phase 4 Mechanical Issues

**Issue**: "Currency defaults to gold instead of profile-specific"  
**Solution**: Check economy_meta_schema.json loaded, verify Session Zero Phase 3 completed

**Issue**: "Progression uses XP/Level instead of tier_xp/Tier"  
**Solution**: Check progression_meta_schema.json loaded, verify profile type is mastery_tiers

**Issue**: "Tier advancement auto-levels (ignores demonstration requirement)"  
**Solution**: Check advancement_rules in progression config (demonstration_required: true, auto_level: false)

**Issue**: "mechanical_systems not in export JSON"  
**Solution**: Check session_export_schema.json loaded, explicitly request mechanical_systems section

### Test Execution Issues

**Issue**: "Test takes too long (>estimated time)"  
**Solution**: Be concise in player responses, combine answers, skip optional validation

**Issue**: "AIDM asks too many questions"  
**Solution**: Provide comprehensive answers upfront, use test script examples

**Issue**: "Character sheet not displaying"  
**Solution**: Explicitly request "Show my character sheet" after creation

**Issue**: "Export/import fails"  
**Solution**: Verify JSON syntax valid, check session_export_schema.json loaded, use YAML if JSON fails

---

## Results Documentation

### Results File Template

For each test, create file: `tests/results/test_[NUMBER]_[NAME]_[DATE].md`

**Standard Template**:

```markdown
# TEST-[NUMBER]: [NAME] Results

**Test Execution Date**: YYYY-MM-DD  
**LLM Platform**: [Claude Sonnet 4.5 / ChatGPT-4o / Other]  
**LLM Version**: [Specific version]  
**Tester**: [Name]

## Test Summary

**Duration**: [TIME]  
**Result**: [✅ PASS / ⚠️ PARTIAL / ❌ FAIL]

## Detailed Results

[Copy results template from test script]

## Issues Discovered

1. [Issue description]
2. [Issue description]

## Conversation Transcript

[Paste full conversation or link to file]

## Character Sheet (if applicable)

[Paste final character sheet]

## Export Data (if applicable)

[Paste export JSON/YAML]

## Notes

[Additional observations]
```

### Results Storage

Store all results in: `tests/results/`

**Naming Convention**: `test_[NUMBER]_[short_name]_YYYY-MM-DD.md`

**Examples**:
- `test_1_cold_start_2025-11-23.md`
- `test_4_combat_mechanics_2025-11-23.md`
- `test_10_economy_integration_2025-11-23.md`

---

## Test Execution Sequence

### Recommended Execution Order

**Phase 1: Critical Path**
1. TEST-1: Cold Start (validates onboarding + Phase 3)
2. TEST-4: Combat Mechanics (validates 5 progression types)
3. TEST-9: Session Zero Mechanical (validates Phase 3 + gameplay)
4. TEST-3: Session Persistence (validates export/import)

**Phase 2: High Priority**
5. TEST-2: Multi-Anime Fusion (validates mechanical fusion)
6. TEST-10: Economy Integration (validates Module 03)
7. TEST-11: Downtime Integration (validates Module 05)
8. TEST-12: Combat Progression (validates Module 08)
9. TEST-13: Leveling Mechanics (validates Module 09)

**Phase 3: Medium Priority**
10. TEST-5: Memory Coherence (validates NPC memory)
11. TEST-6: Error Recovery (validates corrections)
12. TEST-7: Genre Adaptation (validates tone/pacing)
13. TEST-8: Research Validation (validates research protocol)

---

## Test Status Tracking

Use this checklist to track progress:

### Critical Path Tests
- [ ] TEST-1: Cold Start
- [ ] TEST-4: Combat Mechanics
- [ ] TEST-9: Session Zero Mechanical
- [ ] TEST-3: Session Persistence

### High Priority Tests
- [ ] TEST-2: Multi-Anime Fusion
- [ ] TEST-10: Economy Integration
- [ ] TEST-11: Downtime Integration
- [ ] TEST-12: Combat Progression
- [ ] TEST-13: Leveling Mechanics

### Medium Priority Tests
- [ ] TEST-5: Memory Coherence
- [ ] TEST-6: Error Recovery
- [ ] TEST-7: Genre Adaptation
- [ ] TEST-8: Research Validation

### Documentation
- [ ] All results documented
- [ ] Issues logged
- [ ] Test suite summary created

---

## Quick Reference

### File Paths

**Root**: `c:\Users\admin\Downloads\workspace\aidm\`

**Core**: `CORE_AIDM_INSTRUCTIONS.md`  
**Modules**: `instructions/00_system_initialization.md` through `13_narrative_calibration.md`  
**Schemas**: `schemas/character_schema.json` through `session_export_schema.json`  
**Meta-Schemas**: `schemas/economy_meta_schema.json`, `progression_meta_schema.json`, etc.  
**Python**: `libraries/common_mechanics/mechanical_instantiation.py`

### Key Validation Points (Phase 4)

- **Currency**: Profile-specific (Jenny/Ryo/Yen), NOT "gold"
- **Progression**: Type-specific (mastery_tiers/class_based/quirk_awakening/milestone_based/static_op)
- **XP Field**: tier_xp (mastery_tiers), character_xp (class_based), dual tracks (quirk_awakening)
- **Tier Display**: "Journeyman tier" NOT "Level 5"
- **Session Zero**: 6 phases (includes Phase 3: MECHANICAL BUILD)
- **Export**: mechanical_systems section required

---

**Document Status**: READY FOR USE  
**Next Update**: After Phase 5 integration (if applicable)  
**Confidence Level**: HIGH (all 13 tests validated, Phase 4 complete)
