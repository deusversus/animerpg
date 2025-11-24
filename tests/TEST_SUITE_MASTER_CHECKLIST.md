# AIDM Test Suite Master Checklist

**Document Version**: 1.0 (Phase 4 Complete)  
**Last Updated**: November 23, 2025  
**Total Tests**: 13 (9 legacy + 4 Phase 4 integration)

---

## Pre-Execution Setup

### File Loading Verification

**Required Files**: 31+ files (~60,000+ lines)

#### Core Files ✅
- [ ] CORE_AIDM_INSTRUCTIONS.md loaded

#### Instruction Modules (14 files) ✅
- [ ] 00_system_initialization.md
- [ ] 01_cognitive_engine.md
- [ ] 02_learning_engine.md
- [ ] 03_state_manager.md
- [ ] 04_npc_intelligence.md
- [ ] 05_narrative_systems.md
- [ ] 06_session_zero.md
- [ ] 07_anime_integration.md
- [ ] 08_combat_resolution.md
- [ ] 09_progression_systems.md
- [ ] 10_error_recovery.md
- [ ] 11_dice_resolution.md
- [ ] 12_narrative_scaling.md
- [ ] 13_narrative_calibration.md

#### Schema Definitions (15+ files) ✅
- [ ] character_schema.json (v2.3.0)
- [ ] npc_schema.json
- [ ] quest_schema.json
- [ ] world_state_schema.json
- [ ] faction_schema.json
- [ ] anime_world_schema.json
- [ ] power_system_schema.json
- [ ] narrative_profile_schema.json
- [ ] memory_thread_schema.json
- [ ] economy_schema.json
- [ ] session_export_schema.json

#### Meta-Schemas (4 files - Phase 4) ✅
- [ ] economy_meta_schema.json
- [ ] crafting_meta_schema.json
- [ ] progression_meta_schema.json
- [ ] downtime_meta_schema.json

#### Python Libraries (1 file - Phase 4) ✅
- [ ] mechanical_instantiation.py

#### System Verification
- [ ] LLM confirms "AIDM System READY"
- [ ] Phase 4 mechanical systems: ENABLED
- [ ] All 14 modules acknowledged
- [ ] All 15+ schemas acknowledged
- [ ] 4 meta-schemas acknowledged

---

## Test Execution Matrix

### Critical Path Tests (MUST PASS)

#### TEST-1: Cold Start
- [ ] **Status**: [ ] PASS / [ ] PARTIAL / [ ] FAIL / [ ] PENDING
- [ ] Session Zero 6 phases complete
- [ ] Phase 3: MECHANICAL BUILD displayed
- [ ] Currency: Ryo (NOT gold)
- [ ] Progression: mastery_tiers (ninja ranks)
- [ ] Character has tier_xp field (NOT character_xp)
- [ ] Downtime: training_arcs + investigation enabled
- [ ] Character sheet displays correctly
- [ ] **Result File**: tests/results/test_1_cold_start_[DATE].md

#### TEST-4: Combat Mechanics
- [ ] **Status**: [ ] PASS / [ ] PARTIAL / [ ] FAIL / [ ] PENDING
- [ ] **PART A**: Core combat (HP/MP/SP tracking, skills, enemies)
- [ ] **PART B - Scenario 1**: mastery_tiers (tier bonuses, technique XP)
- [ ] **PART B - Scenario 2**: class_based (standard XP, class features)
- [ ] **PART B - Scenario 3**: quirk_awakening (near-death trigger, dual tracks)
- [ ] **PART B - Scenario 4**: milestone_based (minimal combat XP ×0.1)
- [ ] **PART B - Scenario 5**: static_op (ZERO combat XP)
- [ ] All 5 XP formulas match progression type
- [ ] **Result File**: tests/results/test_4_combat_mechanics_[DATE].md

#### TEST-9: Session Zero Mechanical
- [ ] **Status**: [ ] PASS / [ ] PARTIAL / [ ] FAIL / [ ] PENDING
- [ ] **TC-9.1**: Hunter x Hunter (Jenny, mastery_tiers, training_arcs)
- [ ] **TC-9.2**: My Hero Academia (Yen, quirk_awakening, slice_of_life)
- [ ] **TC-9.3**: Konosuba (Eris, debt, class_based)
- [ ] Phase 3 displays all 3 mechanical components
- [ ] **TC-9.7**: Module 03 (loot with profile currency)
- [ ] **TC-9.8**: Module 05 (downtime activity_configs)
- [ ] **TC-9.9**: Module 08 (progression-specific XP)
- [ ] **TC-9.10**: Module 09 (type-specific advancement)
- [ ] All 4 modules read from session_state.mechanical_systems
- [ ] **Result File**: tests/results/test_9_session_zero_mechanical_[DATE].md

#### TEST-3: Session Persistence
- [ ] **Status**: [ ] PASS / [ ] PARTIAL / [ ] FAIL / [ ] PENDING
- [ ] Session 1: Character created (Jenny, mastery_tiers, tier_xp)
- [ ] Export JSON generated
- [ ] mechanical_systems section present in export
- [ ] Currency: Jenny preserved (NOT "gold")
- [ ] Progression: mastery_tiers preserved
- [ ] tier_xp value correct (4200/5000 in example)
- [ ] Session 2: Import successful
- [ ] All mechanical systems restored
- [ ] **Result File**: tests/results/test_3_session_persistence_[DATE].md

---

### High Priority Tests (SHOULD PASS)

#### TEST-2: Multi-Anime Fusion
- [ ] **Status**: [ ] PASS / [ ] PARTIAL / [ ] FAIL / [ ] PENDING
- [ ] 3+ anime combined (Naruto + Solo Leveling + MHA)
- [ ] Currency conflict resolved (Ryo vs Gold vs Yen → ONE currency)
- [ ] Progression conflict resolved (3 types → coherent system)
- [ ] Phase 3 displays mechanical fusion
- [ ] Character sheet uses unified currency
- [ ] Hybrid progression tracks clear
- [ ] **Result File**: tests/results/test_2_multi_anime_fusion_[DATE].md

#### TEST-10: Economy Integration
- [ ] **Status**: [ ] PASS / [ ] PARTIAL / [ ] FAIL / [ ] PENDING
- [ ] Hunter x Hunter: Jenny currency, loot/quest rewards
- [ ] My Hero Academia: Yen currency, loot/quest rewards
- [ ] Konosuba: Eris currency + debt mechanics
- [ ] Scarcity affects pricing
- [ ] Special mechanics work (debt, barter)
- [ ] Module 03 reads from session_state.mechanical_systems.economy
- [ ] **Result File**: tests/results/test_10_economy_integration_[DATE].md

#### TEST-11: Downtime Integration
- [ ] **Status**: [ ] PASS / [ ] PARTIAL / [ ] FAIL / [ ] PENDING
- [ ] 6 modes validated: training_arcs, investigation, slice_of_life, travel, faction_building, social_links
- [ ] Only enabled_modes offered
- [ ] activity_configs apply (time, DC, XP rate, bonuses)
- [ ] Training arc essential for mastery_tiers
- [ ] Module 05 reads from session_state.mechanical_systems.downtime
- [ ] **Result File**: tests/results/test_11_downtime_integration_[DATE].md

#### TEST-12: Combat Progression
- [ ] **Status**: [ ] PASS / [ ] PARTIAL / [ ] FAIL / [ ] PENDING
- [ ] 5 progression types in combat:
  - [ ] mastery_tiers: Tier bonuses +2, technique XP
  - [ ] class_based: Standard XP formula
  - [ ] quirk_awakening: Near-death trigger, awakening sequence
  - [ ] milestone_based: Minimal XP ×0.1
  - [ ] static_op: ZERO XP
- [ ] Module 08 reads from session_state.mechanical_systems.progression
- [ ] **Result File**: tests/results/test_12_combat_progression_[DATE].md

#### TEST-13: Leveling Mechanics
- [ ] **Status**: [ ] PASS / [ ] PARTIAL / [ ] FAIL / [ ] PENDING
- [ ] mastery_tiers: Demonstration required, NO auto-level
- [ ] class_based: Auto-level at threshold
- [ ] quirk_awakening: Dual tracks (levels + awakenings)
- [ ] milestone_based: Story grants, bypass XP
- [ ] static_op: No advancement ever
- [ ] Module 09 reads from session_state.mechanical_systems.progression
- [ ] **Result File**: tests/results/test_13_leveling_mechanics_[DATE].md

---

### Medium Priority Tests (NICE TO PASS)

#### TEST-5: Memory Coherence
- [ ] **Status**: [ ] PASS / [ ] PARTIAL / [ ] FAIL / [ ] PENDING
- [ ] NPCs remember previous conversations
- [ ] Affinity progression tracked (0 → +5 → +20)
- [ ] No contradictions in NPC knowledge
- [ ] Information propagates between NPCs
- [ ] memory_thread_schema.json used
- [ ] **Result File**: tests/results/test_5_memory_coherence_[DATE].md

#### TEST-6: Error Recovery
- [ ] **Status**: [ ] PASS / [ ] PARTIAL / [ ] FAIL / [ ] PENDING
- [ ] HP/math errors corrected
- [ ] Inventory errors fixed
- [ ] Lore/name errors acknowledged
- [ ] Quest/plot errors corrected
- [ ] Tone/genre errors fixed
- [ ] **Mechanical error**: XP → tier_xp, gold → Jenny corrected
- [ ] Correction persists across exchanges
- [ ] **Result File**: tests/results/test_6_error_recovery_[DATE].md

#### TEST-7: Genre Adaptation
- [ ] **Status**: [ ] PASS / [ ] PARTIAL / [ ] FAIL / [ ] PENDING
- [ ] **Isekai**: class_based progression, stat screens, fast pacing
- [ ] **Shonen**: mastery_tiers progression, training arcs, dramatic battles
- [ ] **Slice-of-Life**: minimal progression (milestone/static), slow pacing
- [ ] Mechanical systems adapt to genre
- [ ] **Result File**: tests/results/test_7_genre_adaptation_[DATE].md

#### TEST-8: Research Validation
- [ ] **Status**: [ ] PASS / [ ] PARTIAL / [ ] FAIL / [ ] PENDING
- [ ] Known anime recognized (Attack on Titan)
- [ ] Obscure anime uncertainty admitted (Land of the Lustrous)
- [ ] Fake anime NO hallucination (Neo-Tokyo 2099)
- [ ] **Mechanical research**: HxH → Jenny, mastery_tiers, training_arcs
- [ ] Custom override accepted (HxH with D&D leveling)
- [ ] **Result File**: tests/results/test_8_research_validation_[DATE].md

---

## Test Suite Summary

### Overall Execution Status

**Total Tests**: 13

**Status Breakdown**:
- ✅ **PASS**: [ ] tests (critical systems working)
- ⚠️ **PARTIAL**: [ ] tests (minor issues, acceptable)
- ❌ **FAIL**: [ ] tests (major blockers)
- ⏳ **PENDING**: [ ] tests (not yet executed)

### Critical Blockers (❌ FAIL)

| Test | Issue | Severity | Notes |
|------|-------|----------|-------|
|      |       |          |       |

### Partial Passes (⚠️ PARTIAL)

| Test | Issue | Severity | Notes |
|------|-------|----------|-------|
|      |       |          |       |

### Success Rate

**Critical Path** (4 tests):
- PASS: [ ] / 4 ([ ]%)
- Required: 4 / 4 (100%)
- **Status**: [ ] READY FOR RELEASE / [ ] BLOCKERS PRESENT

**High Priority** (5 tests):
- PASS: [ ] / 5 ([ ]%)
- Required: 4 / 5 (80%)
- **Status**: [ ] ACCEPTABLE / [ ] NEEDS WORK

**Medium Priority** (4 tests):
- PASS: [ ] / 4 ([ ]%)
- Required: 2 / 4 (50%)
- **Status**: [ ] ACCEPTABLE / [ ] NEEDS WORK

**Overall**:
- PASS: [ ] / 13 ([ ]%)
- Required: 10 / 13 (77%)
- **System Status**: [ ] PRODUCTION READY / [ ] BETA READY / [ ] ALPHA READY / [ ] NOT READY

---

## Phase 4 Validation Checklist

### Mechanical Systems Integration

#### Session Zero Phase 3: MECHANICAL BUILD
- [ ] Currency displayed (profile-specific: Jenny/Ryo/Yen)
- [ ] Progression displayed (5 types: mastery_tiers/class_based/quirk_awakening/milestone_based/static_op)
- [ ] Downtime displayed (enabled_modes from profile)
- [ ] Player can customize each component

#### Character Schema v2.3.0
- [ ] tier_xp field present (for mastery_tiers)
- [ ] character_xp field present (for class_based)
- [ ] awakening_stage field present (for quirk_awakening)
- [ ] death_saves field present (0/3 default)
- [ ] injuries field present (empty array default)

#### Economy Systems (Module 03)
- [ ] Profile currency used (NOT "gold")
- [ ] Loot generation with profile currency
- [ ] Quest rewards with profile currency
- [ ] Scarcity mechanics apply
- [ ] Special mechanics work (debt, barter)

#### Progression Systems (Modules 08 + 09)
- [ ] mastery_tiers: Tier bonuses, technique XP, demonstration required
- [ ] class_based: Standard XP, auto-level
- [ ] quirk_awakening: Dual tracks, near-death trigger
- [ ] milestone_based: Minimal combat XP, story grants
- [ ] static_op: Zero XP, no advancement

#### Downtime Systems (Module 05)
- [ ] Only enabled_modes offered
- [ ] activity_configs apply (time, DC, XP rate)
- [ ] Training arcs essential for mastery_tiers
- [ ] Customization allowed

#### Export/Import (Module 03)
- [ ] mechanical_systems section in export
- [ ] All 3 components preserved (economy, progression, downtime)
- [ ] Import restores mechanical systems
- [ ] No currency/progression loss

---

## Common Issues Tracking

### File Loading Issues

| Issue | Frequency | Resolution |
|-------|-----------|------------|
| Files too large | [ ] | Use attachments or batch loading |
| LLM doesn't recognize AIDM | [ ] | Re-paste CORE_AIDM_INSTRUCTIONS.md |
| Missing meta-schemas | [ ] | Verify 4 meta-schemas loaded |

### Phase 4 Mechanical Issues

| Issue | Frequency | Resolution |
|-------|-----------|------------|
| Currency defaults to "gold" | [ ] | Check economy_meta_schema.json loaded |
| Progression uses XP/Level (not tier_xp/Tier) | [ ] | Check progression_meta_schema.json loaded |
| Tier advancement auto-levels | [ ] | Check advancement_rules: demonstration_required=true |
| mechanical_systems not in export | [ ] | Check session_export_schema.json loaded |

### Test Execution Issues

| Issue | Frequency | Resolution |
|-------|-----------|------------|
| Tests take too long | [ ] | Provide concise answers, combine responses |
| AIDM asks too many questions | [ ] | Use test script examples verbatim |
| Character sheet not displaying | [ ] | Explicitly request "Show character sheet" |
| Export/import fails | [ ] | Verify JSON syntax, use YAML if needed |

---

## Results Aggregation

### Test Results Location

All test results stored in: `tests/results/`

**File Naming**: `test_[NUMBER]_[short_name]_YYYY-MM-DD.md`

### Required Documents

- [ ] Test execution logs (13 files, one per test)
- [ ] Character sheets (where applicable)
- [ ] Export JSON/YAML files (where applicable)
- [ ] Issue logs (separate file per major issue)
- [ ] Final test suite summary (this document completed)

### Completion Checklist

- [ ] All 13 tests executed
- [ ] All results documented
- [ ] All issues logged
- [ ] Success rate calculated
- [ ] Production readiness determined
- [ ] Next steps identified

---

## Quick Reference

### Progression Type Quick Lookup

| Type | XP Field | Advancement | Currency Example | Anime Example |
|------|----------|-------------|------------------|---------------|
| mastery_tiers | tier_xp | Demonstration required, NO auto-level | Ryo, Jenny | Naruto, Hunter x Hunter |
| class_based | character_xp | Auto-level at threshold | Gold, Zenny | D&D, Fantasy isekai |
| quirk_awakening | character_xp + awakening_stage | Dual tracks (levels + awakenings) | Yen | My Hero Academia |
| milestone_based | character_xp (minimal) | Story grants, bypass XP | Any | One Punch Man philosophy |
| static_op | N/A | ZERO advancement, ∞ stats | Any | Saitama |

### Currency Quick Lookup

| Anime | Currency | Type | Special Mechanics |
|-------|----------|------|-------------------|
| Naruto | Ryo | fiat_currency | None |
| Hunter x Hunter | Jenny | fiat_currency | None |
| My Hero Academia | Yen | fiat_currency | None |
| Konosuba | Eris | fiat_currency | Debt system (can go negative) |
| Solo Leveling | Gold | fiat_currency | None |

### Downtime Modes Quick Lookup

| Mode | Essential For | Time Required | Example Activity |
|------|---------------|---------------|------------------|
| training_arcs | mastery_tiers progression | 1-4 weeks | Training with mentor to learn Ko |
| investigation | Plot advancement | 1-7 days | Researching villain hideout |
| slice_of_life | Character development | Flexible | School festival, shopping trip |
| travel | World exploration | 1-30 days | Journey to new region |
| faction_building | Political gameplay | Weeks-months | Establish guild headquarters |
| social_links | Relationship building | 1 day per session | Date with companion, hangout with friend |

### Phase 4 File Quick Reference

| File | Purpose | Required For |
|------|---------|--------------|
| economy_meta_schema.json | Currency definitions | Economy tests (TEST-10, TEST-9) |
| progression_meta_schema.json | Progression type definitions | Combat tests (TEST-4, TEST-12, TEST-13) |
| downtime_meta_schema.json | Downtime mode definitions | Downtime tests (TEST-11, TEST-9) |
| crafting_meta_schema.json | Crafting system definitions | (Future tests) |
| mechanical_instantiation.py | Python library for mechanical logic | All Phase 4 tests |

---

## Next Steps

### After Test Suite Completion

1. **Calculate Success Rates**
   - Critical path: [ ] / 4 (needs 100%)
   - High priority: [ ] / 5 (needs 80%)
   - Medium priority: [ ] / 4 (needs 50%)
   - Overall: [ ] / 13 (needs 77%)

2. **Determine Production Readiness**
   - ✅ PRODUCTION READY: All critical pass, 80%+ high priority
   - ⚠️ BETA READY: All critical pass, 60%+ high priority
   - 🔶 ALPHA READY: 3/4 critical pass, 50%+ high priority
   - ❌ NOT READY: <3/4 critical pass

3. **Address Blockers**
   - Log all ❌ FAIL tests in issue tracker
   - Prioritize critical path failures
   - Assign fix estimates
   - Re-test after fixes

4. **Documentation**
   - Update AIDM_ACCEPTANCE_TESTS.md with results
   - Update ROADMAP.md with status
   - Update STATE.md with production readiness
   - Create release notes (if production ready)

5. **Next Phase Planning** (if applicable)
   - Phase 5: Advanced systems (crafting, meta-progression)
   - Additional anime profile coverage
   - Performance optimization
   - LLM platform testing

---

**Document Status**: READY FOR USE  
**Last Review**: 2025-11-23  
**Next Review**: After test suite execution  
**Confidence Level**: HIGH (all 13 tests defined, Phase 4 complete)
