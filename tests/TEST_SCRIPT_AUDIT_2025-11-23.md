# Test Script Audit & Modernization Plan

**Date**: 2025-11-23  
**Auditor**: GitHub Copilot  
**Context**: Phase 4 complete, preparing for Phase 5 comprehensive testing

---

## Executive Summary

**Finding**: 9 older test scripts (TEST-1 through TEST-9) need significant updates to reflect current system architecture.

**Key Issues**:
1. **Outdated file references**: Tests reference old file structure (12 instruction files instead of 14, 7 schemas instead of 15+)
2. **Missing mechanical integration**: Tests don't validate Phase 3-4 mechanical systems (economy, progression, downtime)
3. **Obsolete module names**: References to old module numbering/names
4. **Schema changes**: Tests reference v2.0 schemas, now at v2.3.0+ with new fields (death_saves, injuries, tier_xp)
5. **Missing meta-schemas**: Tests don't reference 4 meta-schemas (economy, crafting, progression, downtime)

**Recommendation**: Modernize all 9 tests before executing comprehensive Phase 5 test suite.

---

## Test Script Inventory

### ✅ Up-to-Date (Phase 4, Recent)
- **TEST-10**: Economy Integration (2025-11-22) - Current system state ✅
- **TEST-11**: Downtime Integration (2025-11-22) - Current system state ✅
- **TEST-12**: Combat Progression (2025-11-22) - Current system state ✅
- **TEST-13**: Leveling Mechanics (2025-11-22) - Current system state ✅

### ⚠️ Needs Modernization (Pre-Phase 4)
- **TEST-1**: Cold Start (Naruto World) - Created early v2.0, needs updates
- **TEST-2**: Multi-Anime Fusion - Missing mechanical systems validation
- **TEST-3**: Session Persistence - Missing mechanical systems in export/import
- **TEST-4**: Combat Mechanics - Missing progression type integration
- **TEST-5**: Memory Coherence - Up-to-date (NPC/memory focus)
- **TEST-6**: Error Recovery - Up-to-date (error handling focus)
- **TEST-7**: Genre Adaptation - Up-to-date (narrative focus)
- **TEST-8**: Research Validation - Up-to-date (anime research focus)
- **TEST-9**: Session Zero Mechanical Integration - Good foundation, needs Phase 4 updates

---

## Detailed Audit by Test

### TEST-1: Cold Start (Naruto World)

**Status**: ⚠️ MODERATE UPDATES NEEDED  
**Priority**: CRITICAL (fundamental user flow)  
**Lines**: 282

**Issues Found**:

1. **Outdated File Counts** (Lines 19-23):
   ```markdown
   **Required** (load in this order):
   1. `aidm/CORE_AIDM_INSTRUCTIONS.md`
   2. All files in `aidm/instructions/` (12 files)  ❌ NOW 14 FILES
   3. All files in `aidm/schemas/` (7 files)       ❌ NOW 15+ FILES
   ```

2. **Missing Mechanical Validation**:
   - Test doesn't verify Hunter x Hunter gets Jenny currency (not gold)
   - Doesn't validate Nen mastery_tiers progression type loaded
   - Doesn't check downtime modes (training_arcs, investigation)
   - Should validate Module 00 loads mechanical_instantiation.py

3. **Schema Version Outdated**:
   - References v2.0 character schema
   - Missing new fields: death_saves, injuries, tier_xp, awakening_stage

4. **Session Zero Structure Changed**:
   - Test references "5-phase character creation"
   - Now has Phase 3: MECHANICAL BUILD (not mentioned)
   - Should validate mechanical systems displayed to player

**Required Updates**:
- [ ] Update file counts (14 instruction modules, 15 schemas)
- [ ] Add 4 meta-schema references (economy, crafting, progression, downtime)
- [ ] Add mechanical_instantiation.py reference
- [ ] Add validation for Jenny currency (not gold)
- [ ] Add validation for mastery_tiers progression
- [ ] Add validation for Session Zero Phase 3 mechanical display
- [ ] Update character schema to v2.3.0 references
- [ ] Add tier_xp field validation (for Nen tiers)

**Estimated Effort**: 1-2 hours (moderate rewrite)

---

### TEST-2: Multi-Anime Fusion

**Status**: ⚠️ MODERATE UPDATES NEEDED  
**Priority**: HIGH (complex feature validation)  
**Lines**: 360

**Issues Found**:

1. **Outdated File Counts** (Lines 15-18):
   ```markdown
   **Required**:
   1. `aidm/CORE_AIDM_INSTRUCTIONS.md`
   2. All files in `aidm/instructions/` (12 files)  ❌ NOW 14 FILES
   3. All files in `aidm/schemas/` (7 files)       ❌ NOW 15+ FILES
   ```

2. **Missing Mechanical Fusion Validation**:
   - Test validates power system fusion (Naruto chakra + Solo Leveling System + MHA Quirks)
   - BUT doesn't validate **mechanical system fusion**:
     - Economy: Naruto (Jenny) + Solo Leveling (multi-currency gates) + MHA (Yen + hero salary)
     - Progression: mastery_tiers (Naruto) vs class_based (Solo Leveling) vs quirk_awakening (MHA)
     - Downtime: training_arcs (all 3) but different mechanics each
   - Should validate how AIDM resolves conflicting mechanical configs

3. **Test Case Missing Economic Fusion**:
   - Example: Player buys from shop - what currency? (Jenny vs Yen vs Gold)
   - Example: Player levels up - which system? (Nen tiers vs MMORPG levels vs MHA levels+quirk)

**Required Updates**:
- [ ] Update file counts (14 modules, 15 schemas)
- [ ] Add 4 meta-schema references
- [ ] Add mechanical_instantiation.py reference
- [ ] Add new test section: "Mechanical System Fusion Validation"
  - [ ] Currency resolution test (which currency used?)
  - [ ] Progression type resolution (which leveling system?)
  - [ ] Downtime mode fusion (overlapping modes like training_arcs)
- [ ] Add validation criteria for mechanical fusion coherence
- [ ] Update expected fusion output to include mechanical systems

**Estimated Effort**: 2-3 hours (new test section needed)

---

### TEST-3: Session Persistence

**Status**: ⚠️ MODERATE UPDATES NEEDED  
**Priority**: HIGH (critical data integrity)  
**Lines**: 444

**Issues Found**:

1. **Outdated File References** (Lines 10-14):
   ```markdown
   **Required**:
   1. `aidm/CORE_AIDM_INSTRUCTIONS.md`
   2. All files in `aidm/instructions/` (12 files)  ❌ NOW 14 FILES
   3. All files in `aidm/schemas/` (7 files)       ❌ NOW 15+ FILES
      - **Critical**: `game_state_schema.json` (defines export format)  ❌ NOW session_export_schema.json
   ```

2. **Missing Mechanical Systems in Export**:
   - Test validates HP/MP/SP, relationships, inventory, quests
   - BUT doesn't validate **mechanical_systems export**:
     - session_state.mechanical_systems.economy (currency_name, type, scarcity)
     - session_state.mechanical_systems.progression (type, tier_system, advancement_rules)
     - session_state.mechanical_systems.downtime (enabled_modes, activity_configs)
   - Export/import should preserve all mechanical configs

3. **Character Schema Changes**:
   - Test assumes generic "Level 5" character
   - Now progression type matters: Level 5 (class_based) vs Journeyman tier (mastery_tiers)
   - Test should validate progression-type-specific fields persist

4. **Currency Assumption**:
   - Test uses "100 gold" hardcoded
   - Should use currency_name from mechanical_systems (Jenny/Eris/Yen)

**Required Updates**:
- [ ] Update file counts (14 modules, 15 schemas)
- [ ] Update schema reference: game_state_schema.json → session_export_schema.json
- [ ] Add 4 meta-schema references
- [ ] Add mechanical_instantiation.py reference
- [ ] Add mechanical_systems export validation section:
  - [ ] Economy config persists (currency_name, type, scarcity, special_mechanics)
  - [ ] Progression config persists (type, tier_system/awakening_triggers)
  - [ ] Downtime config persists (enabled_modes, activity_configs)
- [ ] Update character to use profile-specific currency (not "gold")
- [ ] Add progression-type-specific field validation (tier_xp OR character_xp)
- [ ] Add test case: Export HxH character (Jenny, tiers), import to fresh session

**Estimated Effort**: 2-3 hours (new validation section)

---

### TEST-4: Combat Mechanics

**Status**: ⚠️ SIGNIFICANT UPDATES NEEDED  
**Priority**: CRITICAL (core gameplay)  
**Lines**: 524

**Issues Found**:

1. **Outdated File References** (Lines 10-16):
   ```markdown
   **Required**:
   1. `aidm/CORE_AIDM_INSTRUCTIONS.md`
   2. All files in `aidm/instructions/` (12 files)            ❌ NOW 14 FILES
      - **Critical**: `combat_resolution.md`                 ❌ NOW 08_combat_resolution.md
   3. All files in `aidm/schemas/` (7 files)                 ❌ NOW 15+ FILES
      - **Critical**: `character_schema.json`
   ```

2. **Missing Progression Type Integration**:
   - Test creates "Level 6 warrior" with generic combat
   - **Phase 4 Issue**: Combat XP now depends on progression.type
     - mastery_tiers: base_xp + technique_bonus, tier bonuses in combat
     - class_based: base_xp + class_feature_bonus
     - quirk_awakening: base_xp + (quirk_uses × 10), awakening trigger checks
     - milestone_based: base_xp × 0.1 (minimal combat XP)
     - static_op: 0 XP (no progression)
   - Test should validate progression-type-specific XP calculation

3. **Missing Tier Bonus Validation**:
   - If using mastery_tiers, combat should apply tier bonuses (+2 attack/defense for Journeyman)
   - Test currently has generic "+5 AC" skill, doesn't test tier system

4. **Missing Awakening Trigger Tests**:
   - If using quirk_awakening, near-death scenarios should detect triggers
   - Test has HP damage but doesn't validate awakening trigger detection

5. **No Special Mechanics**:
   - Test doesn't validate profile-specific combat mechanics
   - Example: Hunter License bonuses, hero license requirements, etc.

**Required Updates**:
- [ ] Update file counts (14 modules, 15 schemas)
- [ ] Update module reference: combat_resolution.md → 08_combat_resolution.md
- [ ] Add 4 meta-schema references
- [ ] Add mechanical_instantiation.py reference
- [ ] **Major Rewrite**: Add 5 progression type test scenarios
  - [ ] Scenario A: mastery_tiers combat (tier bonuses, technique XP, tier advancement detection)
  - [ ] Scenario B: class_based combat (standard XP, class feature bonus)
  - [ ] Scenario C: quirk_awakening combat (quirk usage tracking, awakening trigger at HP < 10%)
  - [ ] Scenario D: milestone_based combat (minimal XP × 0.1, narrative emphasis)
  - [ ] Scenario E: static_op combat (0 XP, token quest XP only)
- [ ] Add validation for Module 08 reading progression.type
- [ ] Add expected XP calculations for each type
- [ ] Add tier bonus application validation
- [ ] Add awakening trigger detection validation

**Estimated Effort**: 4-5 hours (significant rewrite with 5 new scenarios)

---

### TEST-5: Memory Coherence

**Status**: ✅ MINIMAL UPDATES NEEDED  
**Priority**: MEDIUM (NPC/memory specific)  
**Lines**: 590

**Issues Found**:

1. **Outdated File Counts** (Lines 10-14):
   ```markdown
   **Required**:
   1. `aidm/CORE_AIDM_INSTRUCTIONS.md`
   2. All files in `aidm/instructions/` (12 files)  ❌ NOW 14 FILES
      - **Critical**: `npc_intelligence.md`, `memory_management.md`  ❌ NOW 04_npc_intelligence.md, (memory in other modules)
   3. All files in `aidm/schemas/` (7 files)       ❌ NOW 15+ FILES
      - **Critical**: `npc_schema.json`, `memory_schema.json`  ❌ memory_thread_schema.json
   ```

2. **Good News**: Test focuses on NPC memory/relationships, which are largely unchanged by Phase 4
   - Affinity system still works the same
   - Memory threads still work the same
   - Emotional flags still work the same

**Required Updates**:
- [ ] Update file counts (14 modules, 15 schemas)
- [ ] Update module references: npc_intelligence.md → 04_npc_intelligence.md
- [ ] Update schema reference: memory_schema.json → memory_thread_schema.json
- [ ] Add note: NPC memory systems independent of mechanical meta-schemas

**Estimated Effort**: 30 minutes (minor reference updates)

---

### TEST-6: Error Recovery

**Status**: ✅ MINIMAL UPDATES NEEDED  
**Priority**: MEDIUM (error handling specific)  

**Assessment**: Test focuses on error recovery protocols (invalid commands, impossible actions, state corruption). These are largely independent of Phase 4 mechanical changes.

**Required Updates**:
- [ ] Update file counts (14 modules, 15 schemas)
- [ ] Update module reference: error_recovery.md → 10_error_recovery.md
- [ ] Add test case: Invalid mechanical system (economy.type = "invalid_type")

**Estimated Effort**: 30 minutes (minor updates)

---

### TEST-7: Genre Adaptation

**Status**: ✅ MINIMAL UPDATES NEEDED  
**Priority**: MEDIUM (narrative focus)

**Assessment**: Test validates genre-appropriate narratives (shonen, seinen, isekai, slice-of-life). Phase 4 mechanical systems complement this but don't fundamentally change it.

**Required Updates**:
- [ ] Update file counts (14 modules, 15 schemas)
- [ ] Add note: Mechanical systems should match genre (slice-of-life might have minimal progression, shonen has mastery_tiers)

**Estimated Effort**: 30 minutes (minor updates)

---

### TEST-8: Research Validation

**Status**: ✅ MINIMAL UPDATES NEEDED  
**Priority**: MEDIUM (research protocol specific)

**Assessment**: Test validates anime research accuracy (web search, library lookup, fact-checking). Phase 4 adds mechanical research but doesn't change core research protocol.

**Required Updates**:
- [ ] Update file counts (14 modules, 15 schemas)
- [ ] Add test case: Research mechanical systems from profile (extract mechanical_configuration section)

**Estimated Effort**: 1 hour (add mechanical research test case)

---

### TEST-9: Session Zero Mechanical Integration

**Status**: ⚠️ MODERATE UPDATES NEEDED  
**Priority**: HIGH (validates Phase 3, needs Phase 4 extension)  
**Lines**: 417

**Issues Found**:

1. **Good Foundation**: Test already validates Session Zero Phase 3 mechanical loading (Hunter x Hunter example)

2. **Missing Phase 4 Gameplay Validation**:
   - Test validates systems displayed in Session Zero
   - **BUT doesn't validate Module 03/05/08/09 actually USE those systems**
   - Should extend test to gameplay turns validating:
     - Module 03 uses Jenny (not gold)
     - Module 05 offers only enabled_modes (training_arcs + investigation)
     - Module 08 calculates XP with mastery_tiers formula
     - Module 09 uses tier advancement (not standard levels)

3. **Missing Test Cases**:
   - TC-9.1: Hunter x Hunter (done)
   - TC-9.2: My Hero Academia (done)
   - TC-9.3: Konosuba (done)
   - **MISSING TC-9.4**: Multi-anime fusion mechanical resolution
   - **MISSING TC-9.5**: Custom mechanical config (player overrides profile defaults)

**Required Updates**:
- [ ] Add "Part 2: Gameplay Validation" section (after Session Zero)
  - [ ] Turn 1-5: Economy transactions (validate currency_name used)
  - [ ] Turn 6-10: Downtime activity (validate only enabled_modes offered)
  - [ ] Turn 11-15: Combat XP (validate progression type formula)
  - [ ] Turn 16-20: Level up (validate progression-specific advancement)
- [ ] Add TC-9.4: Multi-anime fusion mechanical resolution test
- [ ] Add TC-9.5: Custom config override test
- [ ] Update validation criteria to include gameplay integration

**Estimated Effort**: 2-3 hours (extend with gameplay validation)

---

## Modernization Priority Matrix

### CRITICAL (Must Update Before Phase 5)

| Test | Priority | Effort | Reason |
|------|----------|--------|--------|
| TEST-1 | CRITICAL | 1-2h | Fundamental user flow, referenced by other tests |
| TEST-4 | CRITICAL | 4-5h | Core combat, major Phase 4 integration changes |
| TEST-9 | HIGH | 2-3h | Validates Phase 3-4, needs gameplay extension |

**Total Critical**: 7-10 hours

### HIGH (Important for Comprehensive Testing)

| Test | Priority | Effort | Reason |
|------|----------|--------|--------|
| TEST-2 | HIGH | 2-3h | Complex fusion, mechanical system conflicts |
| TEST-3 | HIGH | 2-3h | Data persistence, mechanical systems in export |

**Total High**: 4-6 hours

### MEDIUM (Minor Updates)

| Test | Priority | Effort | Reason |
|------|----------|--------|--------|
| TEST-5 | MEDIUM | 0.5h | Memory/NPC focus, minimal mechanical impact |
| TEST-6 | MEDIUM | 0.5h | Error recovery, independent of mechanics |
| TEST-7 | MEDIUM | 0.5h | Genre narrative, minimal mechanical changes |
| TEST-8 | MEDIUM | 1h | Research protocol, add mechanical research case |

**Total Medium**: 2.5 hours

### TOTAL EFFORT: 13.5-18.5 hours

---

## Recommended Modernization Sequence

### Phase 5.0: Critical Test Updates (7-10 hours)

**Week 1 Focus**: Get core tests working

1. **TEST-1: Cold Start** (1-2h)
   - Update file references
   - Add mechanical validation
   - Add Session Zero Phase 3 checks
   - Update schema versions

2. **TEST-4: Combat Mechanics** (4-5h)
   - Major rewrite with 5 progression type scenarios
   - Add tier bonus validation
   - Add awakening trigger tests
   - Add progression-specific XP calculations

3. **TEST-9: Session Zero Mechanical Integration** (2-3h)
   - Extend with gameplay validation (Part 2)
   - Add multi-anime fusion test case
   - Add custom config test case

**Deliverable**: 3 fully modernized critical tests ready for execution

---

### Phase 5.1: High-Priority Test Updates (4-6 hours)

**Week 2 Focus**: Complex feature validation

4. **TEST-2: Multi-Anime Fusion** (2-3h)
   - Add mechanical system fusion validation
   - Add currency/progression resolution tests
   - Update power system fusion with mechanical considerations

5. **TEST-3: Session Persistence** (2-3h)
   - Add mechanical_systems export validation
   - Update currency references (gold → profile-specific)
   - Add progression-type-specific field persistence

**Deliverable**: 5 fully modernized tests (critical + high priority)

---

### Phase 5.2: Medium-Priority Test Updates (2.5 hours)

**Week 2 Focus**: Supporting test updates

6. **TEST-5, TEST-6, TEST-7, TEST-8** (2.5h total)
   - Batch update file references
   - Add minor mechanical considerations
   - Add mechanical research test case (TEST-8)

**Deliverable**: All 9 legacy tests modernized and ready

---

### Phase 5.3: Comprehensive Test Execution (40-60 hours)

**Week 3-4 Focus**: Run full test suite

7. **Execute all 13 tests** (TEST-1 through TEST-13)
   - Document results for each
   - Track issues discovered
   - Create TEST_RESULTS_SUMMARY.md

**Deliverable**: Validated system ready for Phase 6 deployment

---

## Alternative Approach: Selective Modernization

If 13.5-18.5 hours is too much effort, consider **selective modernization**:

### Minimal Viable Test Suite (3-4 hours)

**Keep**: TEST-10, TEST-11, TEST-12, TEST-13 (already current)  
**Update**: TEST-1 (1-2h), TEST-9 (2-3h, without gameplay extension)  
**Skip**: TEST-2 through TEST-8 (defer to post-deployment)

**Rationale**:
- TEST-1 validates basic user flow (critical)
- TEST-9 validates Phase 3 mechanical loading (critical)
- TEST-10 through TEST-13 validate Phase 4 integration (already done)
- Other tests validate edge cases that can be caught in production

**Risk**: Missing edge cases (multi-anime fusion, session persistence, complex combat scenarios)

---

## File Structure Changes Summary

### Old Structure (Pre-Phase 4)
```
aidm/
  CORE_AIDM_INSTRUCTIONS.md
  instructions/
    00_session_zero.md through 11_state_management.md (12 files)
  schemas/
    character_schema.json through session_schema.json (7 files)
  libraries/
    power_systems/ (5 files)
    genre_tropes/ (various)
```

### Current Structure (Post-Phase 4)
```
aidm/
  CORE_AIDM_INSTRUCTIONS.md
  instructions/
    00_system_initialization.md through 13_narrative_calibration.md (14 files)
  schemas/
    character_schema.json (v2.3.0, +death_saves, +injuries, +tier_xp, +awakening_stage)
    economy_meta_schema.json (NEW)
    crafting_meta_schema.json (NEW)
    progression_meta_schema.json (NEW)
    downtime_meta_schema.json (NEW)
    economy_schema.json (NEW, profile-specific instances)
    ... (15+ schemas total)
  libraries/
    power_systems/ (5 files)
    genre_tropes/ (various)
    narrative_profiles/ (20 profiles with mechanical_configuration sections)
  lib/
    mechanical_instantiation.py (NEW, Python utility)
```

---

## Key Validation Criteria for Updated Tests

All updated tests should validate:

### 1. File Loading (Pre-Test Setup)
- [ ] 14 instruction modules (not 12)
- [ ] 15+ schemas (not 7)
- [ ] 4 meta-schemas referenced where relevant
- [ ] mechanical_instantiation.py referenced in tests that use Session Zero

### 2. Mechanical Systems (Session Zero Phase 3)
- [ ] Economy config displayed (type, currency_name, starting_amount)
- [ ] Progression config displayed (type, advancement_rules, tier_system/awakening_triggers)
- [ ] Downtime config displayed (enabled_modes, activity_configs)
- [ ] Systems stored in session_state.mechanical_systems

### 3. Gameplay Integration (Modules 03, 05, 08, 09)
- [ ] Module 03 uses currency_name (Jenny/Eris/Yen, never "gold")
- [ ] Module 05 offers only enabled_modes
- [ ] Module 08 uses progression.type for XP calculation
- [ ] Module 09 uses progression.type for leveling mechanics

### 4. Progression Type Specifics
- [ ] **mastery_tiers**: tier_xp tracking, tier bonuses, demonstrations, NO traditional levels
- [ ] **class_based**: character_xp tracking, standard levels, class abilities at specific levels
- [ ] **quirk_awakening**: dual tracks (character_xp + awakening_stage), trigger detection
- [ ] **milestone_based**: minimal combat XP (× 0.1), massive milestone XP, direct level grants
- [ ] **static_op**: 0 combat XP, token quest XP, no leveling ever

### 5. Character Schema v2.3.0 Fields
- [ ] death_saves (downed state, resurrection)
- [ ] injuries (persistent damage)
- [ ] tier_xp (for mastery_tiers)
- [ ] awakening_stage (for quirk_awakening)
- [ ] training_progress (for skill development)

---

## Next Steps

**Immediate Action**: User decision required

### Option A: Full Modernization (13.5-18.5 hours)
- Update all 9 legacy tests (TEST-1 through TEST-9)
- Execute comprehensive 13-test suite
- Maximum confidence in system validation

### Option B: Selective Modernization (3-4 hours)
- Update TEST-1 (Cold Start) and TEST-9 (Session Zero Mechanical)
- Execute 6-test suite (TEST-1, TEST-9, TEST-10 through TEST-13)
- Acceptable confidence, defer edge cases to production

### Option C: Phased Modernization (7-10 hours + execution)
- **Week 1**: Critical tests (TEST-1, TEST-4, TEST-9)
- **Week 2**: High-priority tests (TEST-2, TEST-3)
- **Week 3**: Execute 8-test suite (5 updated + TEST-10 through TEST-13)
- Balanced approach, covers most critical paths

**Recommendation**: **Option C - Phased Modernization**
- Covers critical user flows (TEST-1, TEST-4, TEST-9)
- Validates complex features (TEST-2, TEST-3)
- 8 tests provide strong validation coverage
- Manageable time investment (7-10 hours update + 25-35 hours execution)
- Remaining tests (TEST-5 through TEST-8) can be updated post-deployment if issues arise

---

## Conclusion

**Current State**: 4 modern tests (TEST-10 through TEST-13), 9 legacy tests needing updates

**Required Effort**: 13.5-18.5 hours for full modernization (or 7-10 hours for phased critical path)

**Recommendation**: Proceed with **Phased Modernization (Option C)**
1. Update TEST-1, TEST-4, TEST-9 (critical path, 7-10 hours)
2. Update TEST-2, TEST-3 if time permits (high priority, +4-6 hours)
3. Execute 8-test comprehensive suite
4. Document results and prepare for Phase 6 deployment

**Decision Point**: User to select modernization approach before proceeding to Phase 5 testing.
