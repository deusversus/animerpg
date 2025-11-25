# AIDM v2.5 Project Plan

## Document Purpose

Consolidated, actionable project plan for implementing all findings from the comprehensive review of AIDM's 14 core instruction files. This plan is designed for execution by a Claude-based agentic model within VS Code.

**Generated**: November 25, 2025  
**Source Reviews**: 14 module reviews + 1 core review (`/docs/*_REVIEW.md`)  
**Target**: AIDM v2.5 instruction file improvements

---

## Execution Context

### Agent Operating Principles

1. **Identity Firewall**: Agent is DEVELOPER, not AIDM. Write instructions in imperative 3rd person ("AIDM must...").
2. **Edit In Place**: Modify existing files; do not create `_v2` duplicates.
3. **STATE.md Updates**: Update `/dev/STATE.md` after significant changes.
4. **Token Optimization**: All changes must maintain or improve token efficiency.
5. **Validation Required**: Changes require dry-run testing per `/tests/TEST_EXECUTION_GUIDE.md`.

### Key Constraints

- **AIDM is a prompting system**, not code—leverages pseudo-code for determinism but story remains paramount.
- **Generative, not static**: Instruction files generate profiles; extant profiles are examples, not the system.
- **Modular TTRPG systems serve narrative**: Mechanics support adaptive, tonally-accurate storytelling.

---

## Review Findings Index

| Review File | Module | Status | Key Themes |
|-------------|--------|--------|------------|
| `CORE_REVIEW.md` | CORE_AIDM_INSTRUCTIONS | ✅ Processed | Human-centric language, token overrun (133-183%), Rule 1.5 verbosity |
| `MODULE_00_REVIEW.md` | 00_system_initialization | ✅ Processed | Schema count discrepancy, human-centric language, strong foundation |
| `MODULE_01_REVIEW.md` | 01_cognitive_engine | ✅ Processed | Token overrun (83%), integration extraction needed, Rule 2.1 excellence |
| `MODULE_02_REVIEW.md` | 02_learning_engine | ✅ Processed | Category count mismatch (6→8), heat floor ambiguity, token overrun (50-66%) |
| `MODULE_03_REVIEW.md` | 03_state_manager | ✅ Processed | CRITICAL token overrun (400-466%), needs mandatory restructuring |
| `MODULE_04_REVIEW.md` | 04_npc_intelligence | ✅ Processed | Merchant-economy integration gaps, excellent disposition formula |
| `MODULE_05_REVIEW.md` | 05_narrative_systems | ✅ Processed | High token count (283-317%) but justified, foreshadowing protocol excellence |
| `MODULE_06_REVIEW.md` | 06_session_zero | ✅ Processed | Tier misclassification (Tier 1→Tier 2), Phase 0.7 load order unclear |
| `MODULE_07_REVIEW.md` | 07_anime_integration | ✅ Processed | Human-centric language exemplar, token overrun (240-280%) justified |
| `MODULE_08_REVIEW.md` | 08_combat_resolution | ✅ Processed | CRITICAL token (267-317%), duplication M09/M12, architecture misalign |
| `MODULE_09_REVIEW.md` | 09_progression_systems | ✅ Processed | CRITICAL duplication with M08, token (217-250%), authoritative source |
| `MODULE_10_REVIEW.md` | 10_error_recovery | ✅ Processed | Token (117-150%) ACCEPTABLE for critical infra, human-centric lang |
| `MODULE_11_REVIEW.md` | 11_dice_resolution | ✅ Processed | Token (33-50%) VERY ACCEPTABLE, critical LLM randomness fix |
| `MODULE_12_REVIEW.md` | 12_narrative_scaling | ✅ Processed | CRITICAL token (217-267%), M08 authoritative, optimization needed |
| `MODULE_13_REVIEW.md` | 13_narrative_calibration | ✅ Processed | WORST token (267-333%), aggressive optimization needed |

---

## Consolidated Action Items

### Phase 1: Critical Fixes (BLOCKING)
*Issues blocking correct AIDM operation - Must complete before Phase 2*

| ID | Module | Issue | Action | Token Impact | Priority |
|----|--------|-------|--------|--------------|----------|
| P1-01 | M03 | 400-466% token overrun | Extract export formats to EXPORT_FORMAT_GUIDE.md, condense state operations | -8,000 to -10,000 | 🔴 CRITICAL |
| P1-02 | M08 | Duplicates M09 progression content (3K tokens) | Remove, add 200-token reference to M09 | -2,800 | 🔴 CRITICAL |
| P1-03 | M08 | Duplicates M12 tier language (2K tokens) | Remove, add 200-token reference to M12 | -1,800 | 🔴 CRITICAL |
| P1-04 | M08 | Stamina vs Resource contradiction | Align with M09 authoritative "Resource" terminology | 0 | 🔴 CRITICAL |
| P1-05 | M09 | Duplicates M08 combat content (2K tokens) | Remove, add reference to M08 for combat | -1,800 | 🔴 CRITICAL |
| P1-06 | CORE | Rule 1.5 verbosity (1,400 tokens) | Condense operational examples | -800 to -1,000 | 🟡 HIGH |
| P1-07 | M02 | Category count mismatch (6 stated → 8 exist) | Update header to state 8 categories | 0 | 🟡 HIGH |
| P1-08 | M00 | Schema count mismatch (13 stated → 15+ exist) | Update to actual count | 0 | 🟡 HIGH |

**Phase 1 Total Token Savings**: ~15,200-16,400 tokens

---

### Phase 2: Structural Improvements
*Architecture and integration enhancements - Cross-module coordination*

| ID | Module(s) | Issue | Action | Token Impact |
|----|-----------|-------|--------|--------------|
| P2-01 | M06 | Tier 1 misclassification | Reclassify as Tier 2 (on-demand) | 0 (load order) |
| P2-02 | M06 | Phase 0.7 load order unclear | Add explicit ordering: world→power→profile→character | +50 |
| P2-03 | M01 | Integration section 1,500 tokens inline | Extract to INTEGRATION_GUIDE.md | -1,200 |
| P2-04 | M04 | Merchant-economy integration gaps | Add economy_schema.json cross-references | +100 |
| P2-05 | M07→M13 | Research auto-triggers calibration | Document M07→M13 handoff explicitly | +50 |
| P2-06 | M12→M08 | Tier scaling authoritative source | Add note: M12 = authoritative for tier language | +30 |
| P2-07 | M09→M08 | Progression authoritative source | Add note: M09 = authoritative for progression types | +30 |
| P2-08 | M13→M07 | Profile extraction depends on research | Document M13←M07 dependency | +30 |

**Phase 2 Net Token Change**: -910 tokens

---

### Phase 3: System-Wide Language Audit
*Human-centric → AI-directive operational format*

**Scope**: 9 of 15 modules (60% of AIDM)
- CORE, M00, M07, M08, M09, M10, M11, M12, M13

| Pattern | Current | Target | Example |
|---------|---------|--------|---------|
| Prohibitions | "NEVER do X", "❌ WRONG" | `if X: reject()` | "NEVER improvise" → `if no_schema_match: halt_and_query()` |
| Requirements | "ALWAYS do Y", "✅ CORRECT" | `require: Y` | "ALWAYS show work" → `output_format: include_reasoning` |
| Warnings | "Common mistake:", "Don't forget" | `validation_check:` | "Don't forget heat decay" → `validate: heat_floor >= 0` |
| Examples | "Wrong way: ... Right way: ..." | `valid_pattern:` / `invalid_pattern:` | Structural, not instructional |

**Estimated Token Impact**: -500 to -1,000 (removal of verbose warning text)

---

### Phase 4: Token Optimization
*Efficiency improvements without functional loss*

#### Tier 1 Overrun Analysis (Target: ~3,000 tokens each)

| Module | Current | Target | % Over | Action | Post-Opt Target |
|--------|---------|--------|--------|--------|-----------------|
| M03 | 15,000-17,000 | 3,000 | 400-466% | **MANDATORY restructure** | ~5,000-7,000 |
| M13 | 11,000-13,000 | 3,000 | 267-333% | Aggressive condensation | ~8,000-8,500 |
| M08 | 11,000-12,500 | 3,000 | 267-317% | Remove duplications | ~6,500-7,500 |
| M12 | 9,500-11,000 | 3,000 | 217-267% | Condense scaffolding examples | ~6,500-7,500 |
| M09 | 9,500-10,500 | 3,000 | 217-250% | Remove M08 duplication | ~7,500-8,500 |
| M05 | 11,500-12,500 | 3,000 | 283-317% | **JUSTIFIED** (narrative core) | ~10,000-11,000 |
| M07 | 10,200-11,400 | 3,000 | 240-280% | **JUSTIFIED** (research engine) | ~9,000-10,000 |
| CORE | 7,000-8,500 | 3,000 | 133-183% | **ACCEPTABLE** (coordinator) | ~6,000-7,000 |

#### Acceptable Overruns (No Action Required)

| Module | Current | % Over | Justification |
|--------|---------|--------|---------------|
| M10 | 4,500-5,500 | 50-83% | Critical error recovery infrastructure |
| M11 | 4,000-4,500 | 33-50% | Critical LLM randomness solution |
| M04 | 4,500-5,000 | 50-67% | Essential NPC intelligence |
| M02 | 4,500-5,000 | 50-67% | Learning system foundation |
| M01 | 5,500-6,500 | 83-117% | Cognitive core |
| M00 | 3,500-4,000 | 17-33% | Near target |
| M06 | 3,000-3,500 | 0-17% | On target |

#### Specific Optimization Actions

| ID | Module | Section | Current | Target | Savings |
|----|--------|---------|---------|--------|---------|
| P4-01 | M03 | Export format examples | ~6,000 | 500 (reference) | -5,500 |
| P4-02 | M03 | State operation verbose examples | ~3,000 | 1,500 | -1,500 |
| P4-03 | M13 | Mechanical Scaffolding section | 3,500 | 1,500-2,300 | -1,200 to -2,000 |
| P4-04 | M13 | Scale-Specific Adjustments | 2,000 | 800-1,000 | -1,000 to -1,200 |
| P4-05 | M13 | Profile Library inline docs | 1,500 | 500 (→ PROFILE_INDEX.md) | -1,000 |
| P4-06 | M12 | Scaffolding examples verbose | 2,500 | 1,500 | -1,000 |
| P4-07 | M08 | After P1-02/P1-03 removals | — | — | -4,600 (from P1) |
| P4-08 | M09 | After P1-05 removal | — | — | -1,800 (from P1) |
| P4-09 | CORE | Rule 1.5 operational examples | 1,400 | 600 | -800 |

**Phase 4 Additional Savings**: ~11,000-13,000 tokens (beyond Phase 1)

---

### Phase 5: Content Enhancements
*Quality, clarity, and completeness improvements*

| ID | Module | Enhancement | Action |
|----|--------|-------------|--------|
| P5-01 | M02 | Heat floor behavior undefined | Add: "heat_floor: 0.1 (never fully forgets)" |
| P5-02 | M02 | Decay rates missing | Add: "decay_rate: 0.05/session for low-heat, 0.02 for high-heat" |
| P5-03 | M04 | Merchant disposition formula | Document: "(loyalty × 0.4) + (reputation × 0.3) + (relationship × 0.3)" |
| P5-04 | M05 | Thread interconnection rules | Add cross-reference logic for parallel threads |
| P5-05 | M06 | Spartan mode documentation | Add: "Minimal onboarding for experienced players" |
| P5-06 | M10 | Recovery confidence thresholds | Add: "auto_recover: confidence ≥ 0.8, prompt_user: < 0.8" |
| P5-07 | M11 | Seed generation method | Add: "seed = hash(session_id + action_count + timestamp)" |
| P5-08 | M12 | M12 vs M13 terminology | Add upfront: "M12 = Power Scaling Modes, M13 = Narrative DNA Scales" |
| P5-09 | M13 | Profile blending undefined | Add: "Average scales, union tropes, primary profile pacing" |
| P5-10 | M13 | Confidence threshold | Add: "<70% = require validation, ≥70% = optional" |

---

### Phase 6: Validation & Testing
*Verification of all changes*

#### Test Execution Order

1. **Unit Tests** (per-module validation)
   - Run each module's Required Tests table
   - Total: ~80 individual test cases across 15 modules

2. **Integration Tests** (cross-module workflows)
   - M00→M06: System initialization → Session Zero flow
   - M07→M13: Research → Calibration handoff
   - M08↔M09↔M12: Combat/Progression/Scaling coordination
   - M01→M03: Cognitive processing → State persistence

3. **Regression Tests** (no functionality loss)
   - Character creation still works
   - Combat resolution still works  
   - NPC interactions still work
   - Session export still works

4. **Token Budget Verification**
   - Post-optimization token count per module
   - Total AIDM token budget check (target: 60-75% reduction)

#### Success Criteria

| Metric | Current | Target | Validation |
|--------|---------|--------|------------|
| Total AIDM Tokens | ~87,000 | ~35,000-52,000 | 60-75% reduction |
| Tier 1 Modules | 5 critical overruns | 0 critical | All within acceptable range |
| Human-centric Language | 9 modules affected | 0 modules | System-wide audit complete |
| Cross-module Duplication | ~8,000 tokens | 0 tokens | All references, no copies |
| Test Pass Rate | — | 100% | All 80+ tests passing |

---

## Execution Priority Matrix

### Immediate (Week 1)
1. **P1-01**: M03 restructure (biggest token savings)
2. **P1-02/P1-03**: M08 duplication removal
3. **P1-05**: M09 duplication removal

### Short-term (Week 2)
4. **Phase 3**: System-wide language audit
5. **P4-03/P4-04/P4-05**: M13 optimization
6. **P4-06**: M12 optimization

### Medium-term (Week 3)
7. **Phase 2**: Structural improvements
8. **Phase 5**: Content enhancements
9. **P1-06**: CORE Rule 1.5 condensation

### Final (Week 4)
10. **Phase 6**: Full validation & testing
11. Token budget verification
12. STATE.md final update

---

## Cross-Module Dependency Map

```
CORE ─────────────────────────────────────────────┐
  │                                               │
  ├─► M00 (Init) ─► M06 (Session Zero) ──────────┤
  │                      │                        │
  │                      ▼                        │
  │                 M07 (Research) ───► M13 (Calibration)
  │                      │                   │
  │                      ▼                   │
  ├─► M01 (Cognitive) ◄──┴───────────────────┘
  │         │
  │         ▼
  ├─► M02 (Learning) ◄──► M03 (State)
  │         │                  │
  │         ▼                  ▼
  ├─► M04 (NPC) ◄───────► M05 (Narrative)
  │         │                  │
  │         ▼                  ▼
  ├─► M08 (Combat) ◄──┬──► M12 (Scaling)
  │         │         │
  │         ▼         │
  ├─► M09 (Progression) ◄─┘
  │
  ├─► M10 (Error Recovery) [cross-cutting]
  │
  └─► M11 (Dice) [cross-cutting]
```

### Authoritative Source Registry

| Domain | Authoritative Module | Referencing Modules |
|--------|---------------------|---------------------|
| Progression Types | M09 | M08 |
| Tier Scaling Language | M12 | M08 |
| Narrative DNA | M13 | M07, M05 |
| State Persistence | M03 | All modules |
| Combat Resolution | M08 | M09, M12 |
| Error Recovery | M10 | All modules |
| Dice/RNG | M11 | M08, M09 |

---

## Token Budget Summary

### Current State
| Category | Tokens | % of 200K |
|----------|--------|-----------|
| AIDM Instructions | ~87,000 | 43.5% |
| Schemas | ~15,000 | 7.5% |
| Templates | ~5,000 | 2.5% |
| **Total System** | ~107,000 | 53.5% |
| **Available for Play** | ~93,000 | 46.5% |

### Target State (Post-Optimization)
| Category | Tokens | % of 200K |
|----------|--------|-----------|
| AIDM Instructions | ~35,000-52,000 | 17.5-26% |
| Schemas | ~12,000 | 6% |
| Templates | ~4,000 | 2% |
| **Total System** | ~51,000-68,000 | 25.5-34% |
| **Available for Play** | ~132,000-149,000 | 66-74.5% |

### Savings Breakdown
| Phase | Token Savings |
|-------|---------------|
| Phase 1 (Critical Fixes) | -15,200 to -16,400 |
| Phase 2 (Structural) | -910 |
| Phase 3 (Language Audit) | -500 to -1,000 |
| Phase 4 (Optimization) | -11,000 to -13,000 |
| Phase 5 (Enhancements) | +500 (net additions) |
| **Total Savings** | ~27,110-30,810 tokens |

---

## Files to Create

| File | Purpose | Source |
|------|---------|--------|
| `/aidm/guides/EXPORT_FORMAT_GUIDE.md` | Extracted from M03 | Export format examples |
| `/aidm/guides/INTEGRATION_GUIDE.md` | Extracted from M01 | Cross-module integration |
| `/aidm/guides/PROFILE_INDEX.md` | Extracted from M13 | Pre-calibrated profile library |
| `/aidm/quick_references/state_quick_ref.md` | Condensed from M03 | Quick state operations |

---

## Validation Checkpoints

- [ ] Phase 1 complete: All critical fixes applied
- [ ] Phase 2 complete: Cross-module references established
- [ ] Phase 3 complete: Language audit finished (9 modules)
- [ ] Phase 4 complete: Token targets met
- [ ] Phase 5 complete: Content enhancements added
- [ ] Phase 6 complete: All tests passing
- [ ] STATE.md updated with v2.5 status
- [ ] Total token budget verified (target: 35K-52K instructions)

---

## Detailed Findings by Module

---

### CORE_AIDM_INSTRUCTIONS.md

**File**: `/aidm/CORE_AIDM_INSTRUCTIONS.md`  
**Token Estimate**: ~7,000-8,500 tokens  
**Target Budget**: ~3,000 tokens (Tier 1)  
**Budget Status**: 🔴 133-183% OVER (acceptable for central coordinator)  
**Approval Status**: ⚠️ APPROVED WITH MODERATE revisions required

#### Critical Issues

**CORE-C1: Human-Centric Instructional Language** `ARCHITECTURAL`
- **Problem**: Uses instructional tone ("Never improvise", "Always show work", "❌ WRONG", "✅ CORRECT") instead of AI-directive operational protocols
- **Impact**: Same issue affects 8 of 15 modules (53% of AIDM)
- **Action**: Rephrase Rules 1-6 to procedural format with code blocks
  - Rule 1 → `process_player_input()` operational loop
  - Rule 2 → `preserve_agency_protocol()` with dialogue/action separation
  - Rule 5 → `calculate_damage()` enforcement protocol

#### Moderate Issues

**CORE-M1: Token Overrun** `BUDGET`
- **Problem**: 7,000-8,500 tokens (133-183% over Tier 1 target)
- **Justification**: Central coordinator orchestrates 15 modules + schemas + libraries; lazy-loading saves 100K+ tokens system-wide
- **Action**: Optimize to ~6,000-7,000 tokens via:
  1. Condense Rule 1.5 Structured Response Protocol (~1,200-1,500 → ~800 tokens) **-400 to -700**
  2. Condense Instruction Loading Protocol (~800 → ~500 tokens, table format) **-300**
  3. Merge Quality Standards + Startup Checklist (~500 → ~350 tokens) **-150**
- **Total Savings**: -850 to -1,150 tokens

**CORE-M2: Rule 1.5 JSON Example Verbosity** `EFFICIENCY`
- **Problem**: Full JSON example consumes ~400-500 tokens (6-7% of CORE)
- **Action**: Compress (flatten nesting, shorten values), reference Module 08 for complete examples

#### Minor Issues

**CORE-N1: "Critical Values" Undefined in Export Validation**
- **Action**: Define explicitly: "Critical: HP/MP/SP/level/location/inventory quantities. Non-critical: quest descriptions, NPC dialogue history, timestamps."

**CORE-N2: Meta-Command Approval Protocol Informal**
- **Action**: Formalize: "Irreversible changes (delete memory, modify stats) → require approval. Queries (show stats, recap) → execute immediately."

#### Key Strengths to Preserve

1. **Central Operational Framework** - Orchestrates 15 modules, lazy-loading architecture
2. **Rule 1.5 Structured Response Protocol** - Validation → Calculation → State → Narrative prevents 90%+ state errors
3. **Change Log Protocol** - Before-value verification, atomic transactions prevent desync
4. **Lazy-Loading via Indexes** - 200K+ → 20-30K active tokens
5. **Startup Checklist** - 7-step systematic initialization
6. **Graceful Degradation** - System functional when files missing

#### Required Tests

| Test ID | Description | Validates |
|---------|-------------|-----------|
| CORE-T1 | Rule 1 module loading by intent | Intent classification → Module loading pipeline |
| CORE-T2 | Rule 1.5 structured response (Fire Bolt cast) | Order of operations, explicit calculations, change logs |
| CORE-T3 | Rule 1.5 validation failure handling | Validation prevents invalid actions, alternatives offered |
| CORE-T4 | Rule 2 verbatim dialogue echo | Player agency, character voice |
| CORE-T5 | Rule 3 before-value verification | Desync detection before corruption |
| CORE-T6 | Rule 3 atomic transactions | Partial state update prevention |
| CORE-T7 | Lazy-loading via indexes | Index navigation → Token efficiency |
| CORE-T8 | Graceful degradation (Module 08 missing) | Continuity prioritized over perfection |
| CORE-T9 | Session export/import integrity | Import validation prevents corruption |
| CORE-T10 | Startup checklist execution | Systematic initialization |

---

### 00_system_initialization.md

**File**: `/aidm/instructions/00_system_initialization.md`  
**Token Estimate**: ~2,000 tokens  
**Target Budget**: ~2,000 tokens (Tier 1)  
**Budget Status**: ✅ WITHIN BUDGET  
**Approval Status**: ✅ APPROVED WITH MINOR RECOMMENDATIONS

#### Critical Issues

**NONE** - No critical issues blocking system operation.

#### Moderate Issues

**M00-M1: Schema Count Discrepancy** `CONSISTENCY`
- **Location**: "Required Schemas (15)" vs "Schema Validation (7 schemas)" in completion checklist
- **Problem**: Completion checklist incorrectly states 7 schemas when 15 are required
- **Action**: Update checklist to "Schema Validation (15 schemas)"

**M00-M2: Missing Tier 2 Module Count** `CLARITY`
- **Location**: Tier 2 section
- **Problem**: Lists 7 modules but doesn't explicitly state the count
- **Action**: Add count: "TIER 2 - LAZY-LOAD ON INTENT (7 modules, ~12,000 tokens when needed)"

#### Minor Issues

**M00-N1: Human-Centric Instructional Language** `ARCHITECTURAL`
- **Problem**: Uses instructional tone ("DON'T load all modules", "VALIDATE FIRST, EXECUTE SECOND") vs AI-directive protocols
- **Note**: Same pattern in all 16 AIDM files - address in system-wide language audit

**M00-N2: Token Budget Assertion Unverified**
- **Action**: Add measurement verification in testing framework

**M00-N3: Step 5 Formatting Artifact**
- **Problem**: "[4/5] Setting session context... ✓" copy-paste error
- **Action**: Remove formatting artifact

**M00-N4: Module Unloading Threshold Arbitrary**
- **Problem**: "80% threshold" not tied to specific context window size
- **Action**: Specify "80% of [X token] context window" or reference configurable threshold

**M00-N5: Incomplete Error Recovery Integration**
- **Action**: Add: "Error Recovery (10) - logs initialization failures, provides emergency rollback if health check fails"

#### Key Strengths to Preserve

1. **Clear 7-step sequence** - Logically ordered bootstrap
2. **Comprehensive schema validation** - All 15 schemas verified
3. **Proper dependency ordering** - Tier 1: 00→01→02→03→10→11→12→mechanical_instantiation
4. **3-tier lazy loading** - Token optimization architecture
5. **Special scenarios** - Version migration, emergency recovery documented
6. **mechanical_instantiation.py integration** - Python script correctly referenced

#### Required Tests

| Test ID | Description | Validates |
|---------|-------------|-----------|
| M00-T1 | Schema validation with missing/malformed schemas | Error handling |
| M00-T2 | Module loading order verification | Dependency chain |
| M00-T3 | Session detection logic (new/continuing/corrupted) | State routing |
| M00-T4 | Full init chain (00→01→02→03) | Integration |
| M00-T5 | Lazy-load trigger (COMBAT → Module 08) | Intent-based loading |
| M00-T6 | Cold-start full campaign | End-to-end bootstrap |
| M00-T7 | Save/load cycle integrity | Session persistence |

---

### 01_cognitive_engine.md

**File**: `/aidm/instructions/01_cognitive_engine.md`  
**Token Estimate**: ~5,500-6,000 tokens  
**Target Budget**: ~2,000-3,000 tokens (Tier 1)  
**Budget Status**: 🔴 83-100% OVER BUDGET  
**Approval Status**: ✅ APPROVED WITH MODERATE - Most sophisticated module, token optimization required

#### Critical Issues

**NONE** - Rule 2.1 (Sacred Rule) is industry-leading player agency protection.

#### Moderate Issues

**M01-M1: Token Overrun - Priority 1 Fix** `BUDGET`
- **Problem**: ~5,500-6,000 tokens (83-100% over Tier 1 target)
- **Major Consumers**:
  - Narrative Profile Integration (Module 13): ~1,200 tokens (22%)
  - CREATIVE Intent examples: ~800 tokens (14%)
  - Coherence Validation: ~800 tokens (14%)
  - Rule 2.1 examples: ~600 tokens (11%)
- **Actions**:
  1. Extract Narrative Profile Integration → `docs/MODULE_01_13_INTEGRATION_GUIDE.md` (save ~1,000 tokens)
  2. Move 7-step Module 12 Workflow to Module 12 itself (save ~200 tokens)
  3. Reduce CREATIVE Intent sub-examples from 5 to 2 (save ~300 tokens)
  4. Condense Rule 2.1 examples: 4→2 violations, 4→2 correct (save ~200 tokens)
- **Target**: ~3,800 tokens (30% reduction)

**M01-M2: Module Dependency Ambiguity** `CLARITY`
- **Problem**: Workflow shown but "01 MUST load before all others except 00" not explicit
- **Action**: Add: "**Load Order**: Module 00 → Module 01 → All other modules. Tier 1 (always loaded), processes EVERY input."

**M01-M3: CREATIVE Intent Detection Ambiguity** `FUNCTIONALITY`
- **Problem**: "commonly EMBEDDED" emphasized but no detection heuristics
- **Action**: Add explicit pattern list:
  - Past tense PC statements ("I grew up in...")
  - Relationship declarations ("X is my mentor")
  - Faction/organization claims ("I'm part of...")
  - Historical references ("During the war...")

**M01-M4: Research Gate Trigger Unclear** `INTEGRATION`
- **Problem**: Module 07 research trigger timing unspecified (Session Zero only? Mid-campaign?)
- **Action**: Add triggering rules:
  - Session Zero media reference → MANDATORY
  - Mid-campaign power system reference → MANDATORY
  - Mid-campaign flavor reference → OPTIONAL (ask player)

**M01-M5: Narrative Profile Integration Over-Integration** `ARCHITECTURE`
- **Problem**: ~1,200 tokens (30% of module) for Module 13 integration details
- **Action**: Extract to separate guide, keep 200-token summary

#### Minor Issues

**M01-N1: Human-Centric Language (Heavy)** `ARCHITECTURAL`
- **Problem**: Particularly heavy usage ("NEVER assume", "MANDATORY HARD STOP", "FORBIDDEN")
- **Note**: Higher priority than Module 00 due to volume - address in system-wide audit

**M01-N2: Rule Numbering Inconsistency**
- **Problem**: Rule 2.1 is sub-rule but equally critical to Rule 1
- **Action**: Rename to "Rule 2: The Sacred Rule" with 2.1 as implementation details

**M01-N3: Priority Marker Contradiction**
- **Problem**: Rule 2.1 = "Sacred Rule" but Rule 4 claims "HIGHEST PRIORITY"
- **Action**: Clarify hierarchy: Rule 2.1 > Rule 4 > Rule 1 > Rule 3

**M01-N4: Multi-Intent Priority Unexplained**
- **Problem**: META > COMBAT > SOCIAL > ... order given without justification
- **Action**: Add brief justification for each priority level

**M01-N5: Missing Implicit Continuation Guidance**
- **Problem**: Rule 2.1 unclear on when to stop vs continue without asking
- **Action**: Add guidance for implicit continuation (ongoing combat, routine actions) vs explicit stop (new encounters, resource expenditure)

#### Key Strengths to Preserve

1. **Rule 2.1 (Sacred Rule)** - Industry-leading player agency protection with excellent violation examples
2. **Comprehensive Intent Taxonomy** - 7 types covering all gameplay scenarios
3. **Embedded CREATIVE Detection** - Recognizes implicit world-building (major innovation)
4. **Narrative Coherence Validation** - 4-category validation (power tier, scale, archetype, progression)
5. **Response Layer Separation** - Solves "Session Issue #1" (system updates breaking immersion)
6. **Emergency Override Protocol** - Handles Rule 2.1 violations gracefully mid-response

#### Required Tests

| Test ID | Description | Validates |
|---------|-------------|-----------|
| M01-T1 | Rule 2.1 detection (20 scenarios: 10 violations, 10 correct) | Agency protection reliability |
| M01-T2 | Intent classification with ambiguous input | Intent detection accuracy |
| M01-T3 | Multi-intent priority with 3+ intents | Priority ordering |
| M01-T4 | Embedded CREATIVE detection | Implicit world-building integration |
| M01-T5 | Module 01→13→12→05 chain | Narrative profile flow |
| M01-T6 | Module 01→07→13 chain | Anime detection→research→profile |
| M01-T7 | 50-turn session Rule 2.1 audit | Zero violations target |
| M01-T8 | Layer separation (system updates hidden) | Immersion preservation |

---

### 02_learning_engine.md

**File**: `/aidm/instructions/02_learning_engine.md`  
**Token Estimate**: ~4,000-4,500 tokens  
**Target Budget**: ~2,000-3,000 tokens (Tier 1)  
**Budget Status**: 🟡 50-66% OVER BUDGET  
**Approval Status**: ✅ APPROVED WITH MINOR RECOMMENDATIONS

#### Critical Issues

**NONE** - Heat-based prioritization is elegant; 8-category system comprehensive.

#### Moderate Issues

**M02-M1: Category Count Inconsistency** `DOCUMENTATION`
- **Problem**: Header says "6 Hierarchies" but 8 categories listed (CORE, CHARACTER_STATE, RELATIONSHIPS, QUESTS, WORLD_EVENTS, CONSEQUENCES, NARRATIVE_STYLE, FACTION_DYNAMICS)
- **Action**: Update heading to "Memory Categories (8 Categories)" with "(v2.0: Added NARRATIVE_STYLE and FACTION_DYNAMICS)" note

**M02-M2: Heat Floor Definition Ambiguity** `SPECIFICATION`
- **Problem**: "Never decays below base_score" but base_score calculation unexplained
- **Action**: Add explicit definition with formula:
  - Base range by category (CORE:100, CHARACTER_STATE:40-80, RELATIONSHIPS:30-70)
  - + emotional_weight modifier (Trivial+0 to Profound+20)
  - Include calculation example

**M02-M3: Memory Creation Trigger Overlap** `CLARITY`
- **Problem**: "Character state changes" and "Significant event" may trigger on same event (boss victory → XP → level up)
- **Action**: Add multi-trigger event clarification: "Single event may spawn multiple memory types, linked via event_id"

**M02-M4: FACTION_DYNAMICS Integration Unclear** `IMPLEMENTATION`
- **Problem**: State Manager auto-generation mentioned but trigger conditions unspecified
- **Action**: Add protocol: "create_faction() → FACTION_DYNAMICS memory (heat:80); modify_reputation() threshold crossing → memory (heat:75)"

#### Minor Issues

**M02-N1: Human-Centric Language (Moderate)** `ARCHITECTURAL`
- **Problem**: "REMEMBER what matters, FORGET what doesn't", "Core memories NEVER change"
- **Note**: Moderate priority in system-wide audit

**M02-N2: Heat Boost Stacking Unclear**
- **Action**: Add: "Boosts stack additively. +15 reference max once per session."

**M02-N3: Compression Threshold Ambiguous**
- **Action**: Clarify: "100+ threads per-category, not total"

**M02-N4: Emotional Weight Scale Undefined**
- **Action**: Add scale definition: Trivial → Minor → Moderate → Significant → Profound with guidelines

**M02-N5: Hidden Memory Usage Protocol Missing**
- **Action**: Add: How to use without revealing, trigger reveal conditions (Affinity >70 OR discovery event)

**M02-N6: PLAYER_ESTABLISHED_RULE Detection Patterns Limited**
- **Action**: Expand from 5 patterns to 10+ (add "To be clear", "Rule:", "Note:", etc.)

**M02-N7: Decay Rate Inconsistency**
- **Problem**: 4 decay types defined but NARRATIVE_STYLE uses "moderate" not in list
- **Action**: Standardize to 5 types (None/Slow/Moderate/Normal/Fast)

**M02-N8: Player vs Player Conflict Unaddressed**
- **Action**: Add rule for player contradicting own earlier established rule

#### Key Strengths to Preserve

1. **8-category system** - Comprehensive memory type coverage (v2.0 additions)
2. **Heat index prioritization** - Elegant context window management
3. **PLAYER_ESTABLISHED_RULE subcategory** - Critical for Module 01 agency protection
4. **PLAYER_FEEDBACK subcategory** - Solves "Session Issue #2" (corrections persistence)
5. **Power tier tracking** - Excellent Module 12 integration
6. **Hidden memories** - Sophisticated dramatic reveal system
7. **Conflict resolution priority** - Core > Player-initiated > Recent > Schema

#### Required Tests

| Test ID | Description | Validates |
|---------|-------------|-----------|
| M02-T1 | Heat decay over 20 sessions (100 threads) | Decay calculation accuracy |
| M02-T2 | Heat floor enforcement | Critical memory preservation |
| M02-T3 | Compression trigger at 100+ per-category | Memory management |
| M02-T4 | Player-initiated persistence (Session 1→50) | Long-term memory integrity |
| M02-T5 | PLAYER_ESTABLISHED_RULE detection (20 phrases) | Rule detection accuracy |
| M02-T6 | Module 02→01 PLAYER_FEEDBACK flow | Feedback application |
| M02-T7 | Module 03→02 FACTION_DYNAMICS auto-gen | State Manager integration |
| M02-T8 | 50-session campaign memory management | Long-term compression efficacy |
| M02-T9 | Hidden memory reveal trigger | Dramatic reveal system |

---

### 03_state_manager.md

**File**: `/aidm/instructions/03_state_manager.md`  
**Token Estimate**: ~12,000-14,000 tokens  
**Target Budget**: ~3,000 tokens (Tier 1)  
**Budget Status**: 🔴 **CRITICAL** 400-466% OVER BUDGET  
**Approval Status**: ⚠️ **NEEDS REVISION** - Mandatory restructuring required

#### Critical Issues

**M03-C1: Massive Token Budget Overrun** `CRITICAL - ARCHITECTURE BREAKING`
- **Problem**: 12,000-14,000 tokens (400-466% over Tier 1 target)
- **Impact**: Single module = 150-175% of entire Tier 1 budget; breaks lazy-loading architecture
- **Token Distribution**:
  - Mechanical Systems Integration: ~3,500 tokens (25%)
  - Pre-Commit Validation Hooks: ~3,000 tokens (21%)
  - Narrative Profile State Tracking: ~2,500 tokens (18%)
  - Rollback Protocol: ~1,500 tokens (11%)
  - Change Log Format: ~1,500 tokens (11%) - KEEP
  - State Architecture: ~1,000 tokens (7%) - KEEP
- **Action**: MANDATORY RESTRUCTURING (see Phase 1-3 below)

#### Mandatory Restructuring Plan

**Phase 1: Extract to Guides** (Save ~5,800 tokens)
1. Create `docs/STATE_NARRATIVE_PROFILE_GUIDE.md` → Extract 2,300 tokens
2. Create `docs/STATE_VALIDATION_GUIDE.md` → Extract 2,500 tokens  
3. Create `docs/STATE_ROLLBACK_GUIDE.md` → Extract 1,000 tokens

**Phase 2: Move to Responsible Modules** (Save ~3,500 tokens)
4. Move mechanical systems instantiation → Module 06 (Session Zero)
5. Move economy integration examples → Module 08/09

**Phase 3: Consolidate Core** (Save ~500 tokens)
6. Merge redundant Change Log operation examples
7. Condense Critical State Rules

**Target After Restructuring**: ~4,500 tokens (50% over, acceptable for most critical module)

#### Moderate Issues

**M03-M1: Structural Organization Problems** `ARCHITECTURE`
- **Problem**: Mixes 6+ concerns without clear separation (state architecture, narrative profiles, validation hooks, mechanical systems, economy)
- **Action**: Reorganize into: I. State Architecture → II. Validation Overview → III. Change Log Protocol → IV. Integration Summaries

**M03-M2: Narrative Profile Section Belongs in Module 13** `RESPONSIBILITY`
- **Problem**: 2,500 tokens (18%) defining profile structure that Module 13 owns
- **Action**: Module 03 keeps only: "Store narrative_profile in character_schema, validate profile_type, load on restart" (~200 tokens)

**M03-M3: Pre-Commit Validation Overlaps Module 10** `REDUNDANCY`
- **Problem**: Detailed validation logic duplicates Error Recovery module
- **Action**: Module 03 = pre-commit structural validation; Module 10 = semantic validation & error recovery

**M03-M4: Mechanical Systems = Session Zero Responsibility** `RESPONSIBILITY`
- **Problem**: 3,500 tokens (25%) describing Session Zero Phase 0.7 workflow
- **Action**: Move instantiation workflow to Module 06

**M03-M5: Change Log Operation Definitions Incomplete** `SPECIFICATION`
- **Problem**: `multiply` uses `factor` but text suggests `delta`; batch selector logic underspecified
- **Action**: Standardize fields, define selector matching rules (exact match only, no wildcards)

#### Minor Issues

**M03-N1: Human-Centric Language (HIGHEST PRIORITY)** `ARCHITECTURAL`
- **Problem**: "MUST sync", "NEVER approximate", "FORBIDDEN", "MANDATORY" throughout
- **Note**: Critical module - state management requires precision; highest priority in system-wide audit

**M03-N2: State Architecture Component Mismatch**
- **Problem**: "5 Components" lists NARRATIVE_PROFILE separately but it's in CHARACTER
- **Action**: Clarify actual component structure

**M03-N3: Field Path Notation Inconsistency**
- **Action**: Standardize: dot notation for objects, ID-based selectors for arrays (deprecate index-based)

**M03-N4: Missing Concurrency Control**
- **Problem**: No mechanism for concurrent state modifications
- **Action**: Add transaction locking or optimistic concurrency control

**M03-N5: Rollback Failure Handling Missing**
- **Action**: Add handling for when rollback itself fails (freeze state, notify player, offer recovery options)

#### Key Strengths to Preserve

1. **Change Log format** - Elegant token optimization + validation enabler (BEST technical design in AIDM)
2. **Before/after values** - Enables both pre-commit validation and atomic rollback
3. **9 operation types** - Comprehensive coverage (set, add, subtract, multiply, append, remove, replace, remove_batch, update_batch)
4. **Pre-commit validation concept** - Prevents invalid data propagation
5. **Atomic transactions** - All-or-nothing updates ensure consistency
6. **Safe array modification** - ID-based selectors prevent index fragility

#### Required Tests

| Test ID | Description | Validates |
|---------|-------------|-----------|
| M03-T1 | All 9 Change Log operations | Operation correctness |
| M03-T2 | Before-value desync detection | Validation accuracy |
| M03-T3 | Range validation (negative prevention) | Constraint enforcement |
| M03-T4 | Delta verification (calculation errors) | Math validation |
| M03-T5 | Rollback for all 9 operations | Reversal correctness |
| M03-T6 | 100-turn combat state consistency | Long-term stability |
| M03-T7 | Multi-level progression cascade | Atomic transaction integrity |
| M03-T8 | Save/load cycle integrity | Export/import fidelity |
| M03-T9 | 6-change cascade rollback | Complex rollback reliability |

---

### 04_npc_intelligence.md

**File**: `/aidm/instructions/04_npc_intelligence.md`  
**Token Estimate**: ~3,800-4,200 tokens  
**Target Budget**: ~3,000 tokens (Tier 1)  
**Budget Status**: 🟡 27-40% OVER (acceptable for critical module)  
**Approval Status**: ✅ APPROVED WITH MINOR RECOMMENDATIONS

#### Critical Issues

**NONE** - High-quality, well-structured module with excellent disposition formula.

#### Moderate Issues

**M04-M1: Merchant-Economy Integration Incomplete** `INTEGRATION`
- **Problem**: Merchant workflow doesn't link to economy_schema structure
- **Missing**: merchant_id storage location, scarcity_level stacking, special_mechanics integration
- **Action**: Add subsection detailing:
  - merchant_id storage in npc_schema.merchant_context
  - Price calculation: base × vendor_sell × scarcity × affinity_modifier × special_mechanics
  - Validation via Module 03 Change Log

**M04-M2: Example Calculation Missing Scarcity** `ACCURACY`
- **Problem**: "50g × 1.2 × 0.9 = 54g" doesn't include scarcity_level
- **Action**: Add "assumes balanced economy (scarcity=1.0)" or show full calculation

**M04-M3: NPC Death Cascade Ownership Unclear** `INTEGRATION`
- **Problem**: Automated cascade mentioned but Module 03 doesn't define npc_death cascade
- **Action**: Clarify: Module 03 auto-executes on status="dead" OR Module 04 manually triggers each update

#### Minor Issues

**M04-N1: Human-Centric Language (Light)** `ARCHITECTURAL`
- **Problem**: "NPCs are PEOPLE, not quest dispensers", ✅ checkmarks throughout
- **Note**: Low priority - light usage compared to other modules

**M04-N2: Behavior Generation Truncated**
- **Problem**: "to kids→AGGRESSIVE (immediate" cuts off mid-sentence
- **Action**: Complete sentence

**M04-N3: "Significant Interaction" Undefined**
- **Problem**: "After 2-3 significant interactions" for archetype assignment - what counts?
- **Action**: Define: "Significant = RELATIONSHIP memory with heat ≥ 50"

**M04-N4: Growth Stage Progression Ambiguous**
- **Action**: Define: "Advance when scene_count reaches threshold AND (affinity change ≥10 OR personal goal addressed)"

**M04-N5: Disposition Rounding Guidance Missing**
- **Action**: Add: "Round disposition to nearest integer for threshold checks"

**M04-N6: merchant_context Field Unverified**
- **Action**: Verify merchant_context.merchant_id exists in npc_schema.json or add to schema

#### Key Strengths to Preserve

1. **Disposition Formula** - Character_Affinity 60% + Faction_Rep 40% + Faction_Modifier (sophisticated, mathematically sound)
2. **Affinity Thresholds** - 6 clear disposition tiers with specific behavioral changes
3. **Knowledge Boundaries** - 3-tier depth system (expert/moderate/basic) + prohibited topics
4. **Ensemble Cast Management** - 7 archetypes (Struggler, Heart, Skeptic, Dependent, Equal, Observer, Rival) solve OP protagonist problem
5. **Spotlight Tracking** - scene_count + growth_stage ensures balanced NPC screen time
6. **Dialogue Style Integration** - Narrative profile parameters applied to NPC base personality
7. **Proactive NPCs** - High-affinity NPCs can initiate quests based on goals

#### Required Tests

| Test ID | Description | Validates |
|---------|-------------|-----------|
| M04-T1 | Disposition calculation (all 3 components) | Formula accuracy |
| M04-T2 | Affinity threshold crossing events | Tier transitions |
| M04-T3 | Knowledge boundary checks (expert/moderate/basic/prohibited) | Info realism |
| M04-T4 | Dialogue style application from narrative profile | Speech pattern consistency |
| M04-T5 | Module 04→02 RELATIONSHIP memory creation | Memory integration |
| M04-T6 | Module 04→05 ensemble archetype→spotlight | Narrative integration |
| M04-T7 | Merchant prices with affinity + faction + scarcity | Economy integration |
| M04-T8 | 100-session NPC affinity evolution | Long-term consistency |
| M04-T9 | Faction war disposition changes (+80 trusted → -50 war modifier) | Political dynamics |

---

### 05_narrative_systems.md

**File**: `/aidm/instructions/05_narrative_systems.md`  
**Token Estimate**: ~8,500-9,500 tokens  
**Target Budget**: ~3,000 tokens (Tier 1)  
**Budget Status**: 🟡 283-317% OVER but JUSTIFIED (4 systems in one module)  
**Approval Status**: ✅ APPROVED WITH MINOR RECOMMENDATIONS

#### Critical Issues

**NONE** - Comprehensive storytelling engine with excellent session issue fixes.

#### Moderate Issues

**M05-M1: Token Budget High But Acceptable** `BUDGET`
- **Problem**: ~8,500-9,500 tokens (283-317% over target)
- **Justification**: Combines 4 major systems:
  - Foreshadowing Protocol (~2,500 tokens) - Session Analysis fix #2
  - Ensemble Cast Management (~2,000 tokens) - OP protagonist solution
  - Core Principles (~2,000 tokens) - Foundation
  - Downtime Activity System (~1,800 tokens) - Mechanical instantiation
- **Recommendation**: ACCEPT AS-IS - All content critical for storytelling quality

**M05-M2: Foreshadowing/Show Don't Tell Overlap** `ORGANIZATION`
- **Problem**: ~500 token redundancy between Narrative Voice and Foreshadowing sections
- **Action**: Consolidate - Narrative Voice keeps principle, Foreshadowing keeps examples, add cross-reference

**M05-M3: Downtime Load Order Unclear** `DEPENDENCY`
- **Problem**: References Session Zero Phase 3 but Module 06 comes later
- **Action**: Add note: "Downtime requires Session Zero completion. If mechanical_systems.downtime missing, offer basic rest/travel only."

#### Minor Issues

**M05-N1: Human-Centric Language (Light)** `ARCHITECTURAL`
- **Problem**: "NEVER breaks character", "NO emoji", etc.
- **Note**: Low priority - light usage

**M05-N2: Narrative Voice Example Truncated**
- **Problem**: "You feel reverent." (tells feelings" cuts off
- **Action**: Complete sentence

**M05-N3: Faction Goal Attribution Error**
- **Problem**: "Module 03 reviews faction goals" but this is Module 05 responsibility
- **Action**: Rephrase: "Module 05 reviews faction goals from world_state (Module 03)"

**M05-N4: "Yes, And..." Section Minimal**
- **Action**: Add 1 more example showing "No" with alternative offer

**M05-N5: Power-Appropriate Narrative Redundancy**
- **Action**: Condense to Module 12 reference (save ~200 tokens)

**M05-N6: New NPC Spotlight Grace Period Missing**
- **Problem**: New NPCs at scene_count 0 immediately flagged as neglected
- **Action**: Add: "New NPCs get 3-session grace period before spotlight balance applies"

#### Key Strengths to Preserve

1. **Narrative Voice Distinction** - 95% narrator / 5% system split (Session Issue #3 fix)
2. **Foreshadowing Protocol** - Environmental hints, NPC dialogue, world texture, callbacks (Session Analysis #2 fix)
3. **Ensemble Cast Management** - 3 scene distribution modes, spotlight rotation, 5-stage growth system
4. **Downtime Activity System** - 6 mode types with config-driven profile-specific mechanics
5. **Consequence Chains** - Immediate → Short-term → Long-term impact tracking
6. **Faction-Based Narrative** - Dynamic quest generation from faction goals
7. **"Yes, And..." Philosophy** - Rewards creativity, offers alternatives

#### Required Tests

| Test ID | Description | Validates |
|---------|-------------|-----------|
| M05-T1 | Player refuses hook → world continues | Agency preservation |
| M05-T2 | Action triggers → immediate/short/long-term consequences persist | Consequence chains |
| M05-T3 | Plant 2 seeds → 5 sessions → callback acknowledges | Foreshadowing continuity |
| M05-T4 | 3 NPCs unbalanced → auto-generate neglected NPC hook | Spotlight balance |
| M05-T5 | Module 05→02 story beat→CONSEQUENCES memory | Memory integration |
| M05-T6 | Module 05→12 power imbalance >15 → Reverse Ensemble Mode | Mode switching |
| M05-T7 | 20-session foreshadowing (plant S2, payoff S15) | Long-term narrative threads |
| M05-T8 | 4 NPCs across 30 sessions → spotlight_balance >0.6 | Ensemble balance |

---

### 06_session_zero.md

**File**: `/aidm/instructions/06_session_zero.md`  
**Token Estimate**: ~7,500-8,500 tokens  
**Target Budget**: ~12,000 tokens (Tier 2)  
**Budget Status**: ✅ WITHIN BUDGET for Tier 2 (62-71%)  
**Approval Status**: ✅ APPROVED WITH MODERATE RECOMMENDATIONS

#### Critical Issues

**NONE** - Gold standard character creation framework.

#### Moderate Issues

**M06-M1: Tier Misclassification** `ARCHITECTURE`
- **Problem**: Marked as Tier 1 (always loaded) but is intent-triggered (character creation only)
- **Action**: Reclassify as Tier 2 in Module 00 initialization

**M06-M2: Phase 0.7 Load Order Ambiguity** `DEPENDENCY`
- **Problem**: Module 05 downtime needs mechanical_systems from Phase 0.7, but load order unclear
- **Action**: Add validation in Module 05: "If session_state.mechanical_systems missing, direct to complete Session Zero Phase 0.7 first"

**M06-M3: Mechanical Instantiation Execution Unclear** `IMPLEMENTATION`
- **Problem**: References Python script but doesn't explain HOW LLM executes it
- **Action**: Add execution protocol: tool call parameters or manual process specification

**M06-M4: Anime World Import vs Narrative Profile Confusion** `CLARITY`
- **Problem**: Distinction between anime_world_schema and narrative_profile unclear
- **Action**: Clarify:
  - Narrative Profile: Storytelling tone/pacing/mechanics for ANY world
  - Anime World Import: Canon world setting with specific locations/characters/rules

#### Minor Issues

**M06-N1: Human-Centric Language (Moderate-Heavy)** `ARCHITECTURAL`
- **Problem**: Phase 0 has "FORBIDDEN", "NO EXCEPTIONS", "VIOLATION CONSEQUENCE"; 50+ checkmarks
- **Note**: Moderate-high priority in system-wide audit given critical role

**M06-N2: OP Archetype List Could Expand**
- **Problem**: 9 archetypes but missing Accidental Hero, Cursed Power, Reluctant Chosen
- **Action**: Add 2-3 more or note "describe custom for others"

**M06-N3: Currency-Specific Starting Inventory**
- **Action**: Change "200 gold" to "200 [currency]" for economy system compatibility

**M06-N4: Group Session Zero Underdetailed**
- **Action**: Add workflow: "Create characters asynchronously, compile, run shared intro scene"

**M06-N5: Research Timestamp Missing**
- **Action**: Add: "Research executed [date], may be outdated if anime ongoing"

#### Key Strengths to Preserve

1. **Phase 0 Research Protocol** - Mandatory anime reference detection with external sources
2. **External Research Requirement** - VS Battles, wikis, Reddit - not just training data
3. **Narrative Calibration (Phase 0.5)** - Loads narrative profile early, sets tone before creation
4. **OP Protagonist Detection (Phase 0.6)** - 9 archetypes with technique loading
5. **Mechanical System Loading (Phase 0.7)** - Auto-instantiates economy/crafting/progression/downtime
6. **5-Phase Creation** - Concept → Identity → Build → Integration → Intro Scene
7. **Intro Scene Integration** - 15-20min interactive scene tests character

#### Required Tests

| Test ID | Description | Validates |
|---------|-------------|-----------|
| M06-T1 | Detect "Hunter x Hunter" → research → findings → sources | Phase 0 compliance |
| M06-T2 | Load narrative profile → active_narrative_profile populated | Phase 0.5 calibration |
| M06-T3 | Saitama archetype → techniques loaded → expectations set | Phase 0.6 OP detection |
| M06-T4 | 75-point distribution → no attr >18 or <5 | Point-buy validation |
| M06-T5 | Module 06→02 backstory → CORE memory (heat=100, immutable) | Memory integration |
| M06-T6 | Module 06→12 OP mode → narrative_scale set | Scaling integration |
| M06-T7 | Complete Session Zero (Phases 0-5) → playable character | Full creation flow |
| M06-T8 | MHA detection → research → quirk character → UA world | Anime world creation |

---

### 07_anime_integration.md

**File**: `/aidm/instructions/07_anime_integration.md`  
**Token Estimate**: ~11,000-12,000 tokens  
**Target Budget**: ~4,000 tokens (Tier 1)  
**Budget Status**: 🟡 240-280% OVER but JUSTIFIED (CRITICAL priority research protocol)  
**Approval Status**: ✅ APPROVED WITH MODERATE RECOMMENDATIONS

#### Critical Issues

**NONE** - Critical operational protocol preventing trust-breaking hallucination errors.

#### Moderate Issues

**M07-M1: Human-Centric Language (EXEMPLAR CASE)** `ARCHITECTURAL - SYSTEM-WIDE`
- **Problem**: Uses instructional human-centric phrasing throughout:
  - "Let me research...", "Think of me as a GM...", "I'm familiar with..."
- **System Reality**: AIDM is high-end agentic AI with web search, file editing, code execution
- **Action**: Rephrase to AI-directive operational format:
  - "Let me research..." → "Execute research protocol: [steps]"
  - "Think of me as a GM..." → "Execute player consultation protocol: [procedure]"
- **CRITICAL NOTE**: This pattern exists across ALL 16 instruction modules - requires system-wide audit

**M07-M2: Power Tier Mapping Unexplained** `CLARITY`
- **Problem**: Examples reference VSBW tiers (6-C) mapping to AIDM tiers (Tier 6) without explanation
- **Action**: Add note: "VSBW numeric tiers correspond to AIDM narrative tiers. See Module 12 for complete mapping."

**M07-M3: Mechanical Classification Section Verbose** `EFFICIENCY`
- **Problem**: ~2,300 tokens (20% of module) for classification workflow
- **Action**: Add condensed reference table at section start (single-line type mappings)
- **Savings**: ~800-1,000 tokens

#### Minor Issues

**M07-N1: Forbidden Behaviors Buried**
- **Action**: Format as WARNING BOX at top of Research Protocol section

**M07-N2: Temporal Logic Title Misleading**
- **Problem**: "Session Analysis Fix #3" without prior context
- **Action**: Change to "Regression & Time-Loop Mechanics Protocol" (self-contained)

**M07-N3: Premium LLM Section Redundant**
- **Action**: Optional - condense to philosophy + workflow summary (save ~300 tokens)

#### Key Strengths to Preserve

1. **Knowledge Familiarity Scale (L0-L4)** - Honest self-assessment preventing hallucination
2. **Mandatory Blocking Research** - No creative output until research complete + cited + confirmed
3. **Mechanical System Classification** - Economy/Crafting/Progression/Downtime extraction for new profiles
4. **Harmonization Framework** - 4 dimensions (lore, power, genre, cross-system)
5. **Temporal Logic Protocol** - Player-defined regression/time-loop rules (Session Analysis Fix #3)
6. **Error Prevention** - Forbidden behaviors, red flags, common mistakes

#### Required Tests

| Test ID | Description | Validates |
|---------|-------------|-----------|
| M07-T1 | Self-assessment accuracy (L0-L4 evaluation) | Honest gap acknowledgment |
| M07-T2 | Blocking research (L1 knowledge, canon request) | No output before research |
| M07-T3 | Mechanical classification (new DanDaDan profile) | Session Zero Phase 3 compatibility |
| M07-T4 | Power balancing (UBW at Level 3) | OP ability progression gating |
| M07-T5 | Temporal logic (regression without explicit rules) | Player consultation triggered |
| M07-T6 | Cross-anime integration (chakra + Devil Fruits) | Interaction matrix created |
| M07-T7 | Consistency tracking (Devil Fruit + water) | Limitation enforcement |

---

### 08_combat_resolution.md

**File**: `/aidm/instructions/08_combat_resolution.md`  
**Token Estimate**: ~11,000-12,500 tokens  
**Target Budget**: ~3,000 tokens (Tier 1)  
**Budget Status**: ❌ 267-317% OVER (CRITICAL)  
**Approval Status**: ❌ NEEDS REVISION

#### Critical Issues

**M08-C1: Token Budget Catastrophic Failure** `TOKEN-CRITICAL`
- **Problem**: 11,000-12,500 tokens, 267-317% OVER Tier 1 budget
- **Token Violators**:
  - Mechanical Systems Integration: 3,000 tokens (duplicates Module 09)
  - Tier-Appropriate Language: 2,000 tokens (duplicates Module 12)
  - Pre-Combat Validation: 2,500 tokens (overly verbose)
- **Actions**:
  1. Extract Mechanical Systems Integration → `/aidm/guides/combat_progression_integration.md` (Tier 3), leave 200-token summary
  2. Condense Tier Language → 500 tokens (quick reference + M12 reference)
  3. Streamline Pre-Combat Validation → 1,750 tokens (remove instructional repetition)
- **Savings**: -5,050 tokens → Post-optimization ~6,450 tokens (115% over, acceptable)

**M08-C2: Massive Duplication with Module 09** `ARCHITECTURE-CRITICAL`
- **Problem**: 3,000 tokens explaining 5 progression types (mastery_tiers, class_based, quirk_awakening, milestone_based, static_op) that Module 09 will also explain
- **Impact**: 6,000 tokens total for same concepts, maintenance burden, inconsistency risk
- **Action**: Module 08 APPLIES progression rules, Module 09 DEFINES them. Extract to guide or condense to reference.

**M08-C3: Human-Centric Language Throughout** `ARCHITECTURAL - SYSTEM-WIDE`
- **Problem**: Instructional tone ("BEFORE generating ANY combat narrative, ALWAYS validate", "DO NOT proceed", "CHECK character_schema")
- **System Reality**: Agentic AI executor, not human user needing education
- **Action**: Rephrase to AI-directive operational protocols:
  - "BEFORE generating ANY..." → "Pre-combat validation protocol (mandatory): Execute steps 1-5 sequentially"
  - "CHECK character_schema.resources" → Procedural code blocks with pass/fail returns
  - "DO NOT proceed" → "return VALIDATION_FAILED"

#### Moderate Issues

**M08-M1: Tier Language Duplication with Module 12** `DUPLICATION`
- **Problem**: 2,000 tokens repeating Module 12's power tier verb sets (11 tiers × examples)
- **Action**: Condense to 500-token quick reference + "See Module 12 for complete tier framework"
- **Savings**: -1,500 tokens

**M08-M2: Missing Dice Resolution Integration** `INTEGRATION`
- **Problem**: Uses dice notation throughout without referencing Module 11 standards
- **Action**: Add explicit Module 11 reference for notation, advantage/disadvantage, criticals (+100 tokens)

#### Minor Issues

**M08-N1: Enemy AI Priority Tie-Breaking Undefined**
- **Action**: Define rules (if equally weak: closest/most damaged/random)

**M08-N2: Narrative Combat Trigger Conditions Vague**
- **Action**: Clarify when to use narrative vs standard combat

#### Key Strengths to Preserve

1. **5-Step Pre-Combat Validation** - Resource→Prerequisite→Calculation→State→Narrative (bulletproof)
2. **Change Log State Updates** - Atomic execution with rollback on failure
3. **Narrative Profile Combat Integration** - combat_narrative_style parameters (strategy_vs_spectacle, sakuga, named_attacks, destruction)
4. **Death & Resurrection System** - Downed≠Dead, death saves, injury table, resurrection tiers with costs
5. **Boss Battle Framework** - Phased structure (75%/50%/25% HP triggers)
6. **Tournament Framework** - Seeding, fatigue, bracket tracking, spectator reactions
7. **Combat Maneuvers** - Grapple, Disarm, Called Shot, Aid actions

#### Required Tests

| Test ID | Description | Validates |
|---------|-------------|-----------|
| M08-T1 | Skill with insufficient MP → halt + alternatives | Pre-combat validation step 1 |
| M08-T2 | 3-change action, 3rd fails → all rollback | Atomic state updates |
| M08-T3 | Same attack, 3 profiles → 3 different narrations | Narrative Profile integration |
| M08-T4 | Death saves (success, fail, nat 20, nat 1) | Death save mechanics |
| M08-T5 | T9 character "shatter mountain" → mismatch error | Tier language enforcement |
| M08-T6 | Combat victory × 5 progression types | Type-specific XP formulas |
| M08-T7 | Massive damage (≥max HP single hit) → instant death | Edge case handling |

---

### 09_progression_systems.md

**File**: `/aidm/instructions/09_progression_systems.md`  
**Token Estimate**: ~9,500-10,500 tokens  
**Target Budget**: ~3,000 tokens (Tier 1)  
**Budget Status**: ❌ 217-250% OVER (token count acceptable as authoritative progression source)  
**Approval Status**: ❌ NEEDS REVISION (coordination with Module 08 required)

#### Critical Issues

**M09-C1: Module 08 Duplication Resolution** `ARCHITECTURE-CRITICAL`
- **Problem**: Module 08 AND Module 09 both have 3,000-token Mechanical Systems Integration explaining same 5 progression types
- **Resolution**: Module 09 IS THE AUTHORITATIVE SOURCE for progression types
- **Actions**:
  1. **KEEP** Module 09's Mechanical Systems Integration (3K tokens) - this is the correct home
  2. **UPDATE Module 08** to condense its section to 200-token summary + reference to Module 09
  3. Net savings: **2,800 tokens (in Module 08, not Module 09)**
- **5 Progression Types Defined Here**:
  - `mastery_tiers`: Tier-based (Hunter x Hunter), demonstration requirements
  - `class_based`: Standard levels (My Hero Academia), class ability unlocks
  - `quirk_awakening`: Two tracks (levels + awakenings), event-based power evolution
  - `milestone_based`: Story-driven, minimal combat XP
  - `static_op`: No progression ever (Saitama), XP for quest tracking only

**M09-C2: Human-Centric Language Throughout** `ARCHITECTURAL - SYSTEM-WIDE`
- **Problem**: Instructional tone ("BEFORE awarding XP, ALWAYS validate", "DO NOT announce level-up")
- **Action**: Rephrase to AI-directive operational protocols:
  - "BEFORE awarding XP..." → "Pre-progression validation protocol (mandatory): Execute steps 1-5 sequentially"
  - Prose checklists → Procedural code blocks with return codes

#### Moderate Issues

**M09-M1: Pre-Progression Validation Verbose** `TOKEN`
- **Problem**: 2,000 tokens with repeated instructional framing
- **Action**: Condense to 1,250 tokens by removing instructional repetition, replacing prose with code blocks
- **Savings**: -750 tokens (37.5% reduction)

**M09-M2: Missing Error Recovery Integration** `INTEGRATION`
- **Problem**: No reference to Module 10 for validation failure handling
- **Action**: Add explicit Module 10 reference for corrupted schema, overflow errors, constraint violations

#### Minor Issues

**M09-N1: Level-Up Calculation Example Shows Error Then Corrects**
- **Problem**: Pedagogical for humans, confusing for AI pattern matching
- **Action**: Replace with single correct example, move error to commented reference

**M09-N2: Skill Advancement Use Difficulty Undefined**
- **Action**: Reference Module 11 for skill check DCs determining use difficulty

**M09-N3: Milestone XP Range Criteria Unclear**
- **Action**: Define tiers (Minor 200, Standard 300, Major 400, Epic 500) with examples

**M09-N4: Multi-Classing Hybrid Ability Creation Ambiguous**
- **Action**: Clarify (pre-defined list vs player-designed with approval)

#### Key Strengths to Preserve

1. **5-Step Pre-Progression Validation** - XP Calculation→Threshold→Rewards→State→Narrative (bulletproof)
2. **Comprehensive XP Formulas** - Combat, Quest, Roleplay, Discovery, Milestones, Achievements
3. **Downtime Training System** - Quality tiers (50-300 XP/week), anime arcs (Hell Week, Death Train, Hidden Master)
4. **Faction Reputation Milestones** - Automated cascade with State Manager, +200/+500/+1000 XP by tier
5. **Cascade System** - Quest XP auto-awards when status→"completed" (no manual tracking)
6. **Multi-Classing (L10)** - Secondary class, hybrid abilities, build diversity
7. **Progression Type Definitions** - AUTHORITATIVE source for 5 types (Module 08 should reference)

#### Required Tests

| Test ID | Description | Validates |
|---------|-------------|-----------|
| M09-T1 | Award 5000 XP to L8 (16,200/20,000) → level-up + overflow | XP calc, threshold, overflow |
| M09-T2 | Award 15K XP to L5 → multi-level jump (L5→L6→L7→L8) | Iterative level-up sequence |
| M09-T3 | Same 1000 XP × 5 progression types → different results | Type-specific advancement |
| M09-T4 | Sword L2 train 3 weeks Expert → L3 + gold deduction | Downtime training, skill level-up |
| M09-T5 | Quest +200 rep crosses Neutral→Liked → +200 XP auto | Faction cascade system |
| M09-T6 | Level-up 7/8 changes pass, 8th fails → all rollback | Atomic state update |
| M09-T7 | Reputation crosses 2 tiers in one quest | Multi-tier milestone XP |

#### Cross-Module Coordination Note

**Module 08 ↔ Module 09 Duplication Fix**:
- Module 09 = AUTHORITATIVE for progression types (keep 3K tokens)
- Module 08 = APPLIES progression rules (condense to 200-token reference)
- Both modules need coordinated update to resolve 6K token waste

---

### 10_error_recovery.md

**File**: `/aidm/instructions/10_error_recovery.md`  
**Token Estimate**: ~6,500-7,500 tokens  
**Target Budget**: ~3,000 tokens (Tier 1)  
**Budget Status**: 🟡 117-150% OVER but ACCEPTABLE (critical infrastructure)  
**Approval Status**: ✅ APPROVED WITH MINOR RECOMMENDATIONS

#### Why Token Overrun is Acceptable

- **Critical Infrastructure**: Error Recovery monitors ALL other modules, must be robust
- **No Duplication**: Unlike Modules 08-09, no content duplicated from other modules
- **High Value-to-Token Ratio**: Every section serves distinct error recovery function
- **Prevents Catastrophic Failures**: Emergency rollback, state corruption detection, desync handling

#### Moderate Issues

**M10-M1: Human-Centric Language Throughout** `ARCHITECTURAL - SYSTEM-WIDE`
- **Problem**: Instructional tone ("Before ANY change", "ALWAYS check memory", "Check PLAYER_ESTABLISHED_RULE")
- **Action**: Rephrase to AI-directive operational protocols:
  - "Before ANY change, validate legality" → "Pre-action validation protocol (mandatory): Execute validation checks before state changes"
  - Prose instructions → Procedural code blocks with return codes

#### Minor Issues

**M10-N1: Validation Notification Templates Verbose** `TOKEN`
- **Problem**: 800 tokens for 4 full templates with examples
- **Action**: Show template structure once with variations, condense to 500 tokens
- **Savings**: -300 tokens (optional optimization)

**M10-N2: Redundancy in Validation Examples** `TOKEN`
- **Problem**: Fire Bolt scenario repeated in Pre-Action Validation AND Recovery Protocols
- **Action**: Keep full version in one section, reference in other
- **Savings**: -200 tokens (optional optimization)

**M10-N3: "Recent" Rule Undefined for World Rule Contradiction**
- **Action**: Define as "same session or last 2 sessions"

**M10-N4: Error Learning Prevention Protocol Unclear**
- **Problem**: "Implement prevention" - AI can't edit modules
- **Action**: Clarify this is for system developers, not AI executor

#### Key Strengths to Preserve

1. **5-Tier Error Classification** - Critical/Major/Validation/Minor/Trivial with distinct recovery protocols
   - CRITICAL: Emergency rollback (gameplay blocked)
   - MAJOR: Immediate correction + acknowledgment (narrative broken)
   - VALIDATION: Block action + alternatives (pre-commit failure)
   - MINOR: Silent correction (player noticeable)
   - TRIVIAL: Background fix (unnoticeable)
2. **World Rule Contradiction Detection** - Checks PLAYER_ESTABLISHED_RULE memories, prevents ~25% of "I just told you" errors
3. **Player-Memory Conflict Resolution** - 4 strategies (Gentle Reminder, Schema Correction, Ask Clarification, Offer Retcon)
4. **Change Log Desync Detection** - Validates before-value matches current state, catches corruption early
5. **Validation Notification Templates** - Structured, actionable (Insufficient Resources, Prerequisites Not Met, Cooldown Active, Skill Not Learned)
6. **Final System Health Check** - Comprehensive session-end validation, error reporting by severity

#### Required Tests

| Test ID | Description | Validates |
|---------|-------------|-----------|
| M10-T1 | Fire Bolt with 35/50 MP → blocked + alternatives | Pre-action validation |
| M10-T2 | Change Log before=85, state=50 → desync detected | Desync detection |
| M10-T3 | Player "use herbs", schema=0, memory shows purchase | Schema correction strategy |
| M10-T4 | Player "talk to Elena" (DECEASED) | Gentle reminder strategy |
| M10-T5 | "Gates spawn from mana" rule, AI about to say "random" | World rule contradiction |
| M10-T6 | 5 errors with varying severity → correct classification | Decision tree logic |
| M10-T7 | Save corruption → emergency rollback | Critical recovery protocol |
| M10-T8 | Session end with 2 Minor, 3 Trivial errors | System health check |

---

### 11_dice_resolution.md

**File**: `/aidm/instructions/11_dice_resolution.md`  
**Token Estimate**: ~4,000-4,500 tokens  
**Target Budget**: ~3,000 tokens (Tier 1)  
**Budget Status**: ✅ 33-50% OVER (VERY ACCEPTABLE - critical RNG system)  
**Approval Status**: ✅ APPROVED WITH MINOR RECOMMENDATIONS

#### Why This Module is Critical

- **LLMs cannot generate true randomness** - will hallucinate dice results without strict protocol
- **Player trust foundation** - transparent rolls essential for TTRPG integrity
- **No duplication** - content unique to Module 11
- **Minimal overrun** - 33-50% vs 200-300% for Modules 08-09

#### Minor Issues

**M11-N1: Human-Centric Language** `ARCHITECTURAL - SYSTEM-WIDE`
- **Problem**: Instructional warnings ("NEVER simulate dice mentally", "ALWAYS use explicit notation", "DO NOT PROCEED")
- **Action**: Rephrase to AI-directive protocols:
  - "NEVER simulate dice mentally" → "Mental simulation disabled. Execute dice_roll_protocol() for all random elements"
  - "DO NOT PROCEED" → "raise ProtocolViolationError()"

**M11-N2: Common Roll Types Examples Verbose** `TOKEN`
- **Problem**: 1,500 tokens for 6 roll types with full examples each
- **Action**: Use template format + variations, condense to 1,200 tokens
- **Savings**: -300 tokens (optional)

**M11-N3: Redundant Attack Example** `TOKEN`
- **Problem**: Attack example in both Dice Roll Protocol and Common Roll Types
- **Action**: Keep detailed version in Common Roll Types, brief reference in protocol
- **Savings**: -100 tokens (optional)

**M11-N4: Situational Modifiers Undefined**
- **Action**: Add quantification guidelines or reference Module 08

#### Key Strengths to Preserve

1. **Explicit Dice Protocol** - 5-step sequence (Declare→Execute→Calculate→Compare→Apply)
   - Prevents LLM randomness hallucination
   - Shows notation, raw result, calculation, outcome
   - Math verification enabled (player can check arithmetic)
2. **Comprehensive Roll Type Coverage** - 6 types:
   - Attack Rolls (1d20+Attr+Prof+Situational)
   - Damage Rolls (Weapon Dice+Attr)
   - Skill Checks (1d20+Skill+Attr)
   - Saving Throws (1d20+Attr+Prof)
   - Percentile Rolls (1d100)
   - Initiative (1d20+DEX)
3. **Special Roll Scenarios** - 5 edge cases:
   - Critical Hits (Nat 20 = double damage dice, always hits)
   - Critical Failures (Nat 1 = always fails, minor consequence)
   - Advantage/Disadvantage (roll twice, take higher/lower)
   - Multiple Dice (show individual results: 3,5,2,6,4,1)
   - Opposed Rolls (both sides visible)
4. **Performance Checklist** - Pre-roll validation ("If ANY unchecked, DO NOT PROCEED")
5. **Dice Automation Options** - Plugin call, player prompt, pseudo-random seed

#### Required Tests

| Test ID | Description | Validates |
|---------|-------------|-----------|
| M11-T1 | Attack roll with all 5 protocol steps | Protocol compliance |
| M11-T2 | Roll WITHOUT plugin → prompts player, doesn't invent | Hallucination prevention |
| M11-T3 | Damage 2d6+5 with 4,6 → shows "(4+6)+5=15" | Math verification |
| M11-T4 | Attack 1d20+5, raw=20 → NAT 20, damage doubled | Critical hit mechanics |
| M11-T5 | Stealth Advantage → 2 rolls shown, higher taken | Advantage mechanics |
| M11-T6 | Grapple contest → both sides visible | Opposed roll transparency |
| M11-T7 | "1d20+5→Result 27" → impossible, error caught | Error detection integration |
| M11-T8 | Fireball 6d6 → individual results shown | Multiple dice display |

---

### 12_narrative_scaling.md

**File**: `/aidm/instructions/12_narrative_scaling.md`  
**Token Estimate**: ~9,500-11,000 tokens  
**Target Budget**: ~3,000 tokens (Tier 1)  
**Budget Status**: ❌ 217-267% OVER (CRITICAL - needs optimization)  
**Approval Status**: ❌ NEEDS REVISION

#### Core Insight: Power Tier ≠ Narrative Scale

Module 12 solves critical TTRPG problem: **How to run OP characters (Saitama/Rimuru/Deus) without breaking game**. Key insight: Power Tier (T11-T0) and Narrative Scale are **orthogonal** - same tier can run different scales based on **context**.

#### Critical Issues

**M12-C1: Massive Token Budget Overrun** `TOKEN-CRITICAL`
- **Problem**: 9,500-11,000 tokens (217-267% OVER)
- **Optimization Available**: -1,700 tokens via condensation:
  - 9 Narrative Scales: 3,500 → 2,900 (-600)
  - OP Protagonist Archetypes: 2,500 → 1,900 (-600)
  - Dynamic Examples: 1,500 → 1,300 (-200)
  - Progression Section: 1,200 → 900 (-300)
- **Post-Optimization**: ~7,800 tokens (160% over, acceptable for critical framework)

**M12-C2: Module 08 Duplication Resolution** `ARCHITECTURE`
- **Problem**: Module 08 has ~2,000 token "Tier-Appropriate Language" section
- **Resolution**: Module 12 = AUTHORITATIVE SOURCE for tier-appropriate scaling
- **Action**: Module 08 should remove duplication, add ~200-token reference to Module 12
- **Module 12 Responsibility**: NONE (content already present in 9 Narrative Scales)

**M12-C3: Human-Centric Language Throughout** `ARCHITECTURAL - SYSTEM-WIDE`
- **Problem**: Instructional warnings ("[NO] Conflate", "AVOID ignoring context")
- **Action**: Rephrase to AI-directive protocols (select_narrative_scale(), calculate_power_imbalance())

#### Moderate Issues

**M12-M1: Context Modifier Ranges Need Guidance**
- **Problem**: Environmental ×0.1-0.5 (how to choose specific value?)
- **Action**: Add selection examples for each range endpoint

**M12-M2: Multiple Modifier Interaction Unclear**
- **Action**: Clarify: "Context Multiplier = PRODUCT of all modifiers (multiply them)"

#### Key Strengths to Preserve

1. **Power Imbalance Formula** - Effective = (PC Raw × Context) ÷ Threat Raw
   - 6 Context Modifiers: Environmental (×0.1-0.5), Secret ID (×0.1-0.3), Self-Limiter (×0.2-0.5), Mentor (×0.5), Political (×0.3-0.7), Genre (×0.1-0.5)
   - 4 Imbalance Triggers: 0.5-1.5 (Balanced), 1.5-3.0 (Moderate), 3.0-10.0 (Significant), 10.0+ (Overwhelming)
2. **9 Narrative Scales** - Full spectrum from grounded to metafictional:
   - 1. Tactical Survival (death real)
   - 2. Strategic Combat (prep/team key)
   - 3. Ensemble Focus (PC=safety net)
   - 4. Reverse Ensemble (NPC perspective)
   - 5. Mythology Journey (episodic)
   - 6. Faction/Empire Building
   - 7. Mythic Spectacle (HOW>IF)
   - 8. Conceptual Philosophy (existential)
   - 9. Metafictional (T1-0 only)
3. **Compatibility Matrix** - 11 tiers × 9 scales = 99 combinations ([OK]/[!]/[NO]/[X])
4. **9 OP Protagonist Archetypes** - Fully characterized:
   - Saitama (Invincible), Mob (Restraint), Overlord (Roleplaying)
   - Saiki K (Oblivious), Mashle (Absurd), Wang Ling (Secret)
   - Vampire D (Legend), Rimuru (Builder), Deus (Disguised God)
5. **Non-Combat Tension Framework** - When imbalance > 10:
   - REDUCE combat 50%, INCREASE social/existential 200%
   - 3 categories: Social, Existential, Structural
6. **Scale Shift Protocol** - Tier changes create narrative ceremonies, auto-trigger reevaluation

#### Required Tests

| Test ID | Description | Validates |
|---------|-------------|-----------|
| M12-T1 | T6-C with Mentor ×0.5 vs T8-C → imbalance 50× | Formula accuracy |
| M12-T2 | 6 stacked modifiers → combined multiplier | Multi-modifier interaction |
| M12-T3 | T8→T7 crosses 3.0 threshold → scale shift ceremony | Progression protocol |
| M12-T4 | T5 at session 1 → OP Mode + archetype options | OP detection |
| M12-T5 | T11 requests Spectacle ([X]) → blocked/warned | Matrix enforcement |
| M12-T6 | Saitama archetype, imbalance 15× → social encounter | Non-combat tension |
| M12-T7 | 15 sessions, 80% defensive → suggest Mob archetype | Behavior-based suggestion |
| M12-T8 | Gojo 3 contexts → 3 different scales | Dynamic scale selection |

#### Cross-Module Coordination Note

**Module 08 ↔ Module 12 Duplication Fix**:
- Module 12 = AUTHORITATIVE for tier-appropriate scaling/language
- Module 08 should remove ~2,000 token section, add ~200-token reference
- Saves 1,800 tokens from Module 08

---

### 13_narrative_calibration.md

**File**: `/aidm/instructions/13_narrative_calibration.md`  
**Token Estimate**: ~11,000-13,000 tokens  
**Target Budget**: ~3,000 tokens (Tier 1)  
**Budget Status**: ❌ 267-333% OVER (WORST in AIDM - requires aggressive optimization)  
**Approval Status**: ❌ NEEDS REVISION (CRITICAL)

#### Core Insight: MECHANICS ≠ NARRATIVE

Module 13 solves critical problem: **Knowing anime power systems ≠ knowing how to tell stories like that anime**. Without Module 13, AIDM produces "D&D in anime skin" - tactically sound but narratively inauthentic.

#### Critical Issues

**M13-C1: EXTREME Token Overrun** `TOKEN-CRITICAL`
- **Problem**: 11,000-13,000 tokens (WORST overrun in AIDM)
- **Optimization Required**: -3,400 to -4,600 tokens via:
  - Mechanical Scaffolding: 3,500 → 1,500-2,300 (-1,200 to -2,000)
  - Scale-Specific Adjustments: 2,000 → 800-1,000 (-1,000 to -1,200)
  - Profile Library Docs: 1,500 → 500 (-1,000)
  - Extraction Process: (-200)
  - Example Deduplication: (-200)
- **Post-Optimization**: ~7,400-9,600 tokens → target ~8,000-8,500 (167-183% over, acceptable)

**M13-C2: Human-Centric Language Throughout** `ARCHITECTURAL - SYSTEM-WIDE`
- **Problem**: Instructional framing ("❌ Wrong", "✅ Right", "Common Mistakes")
- **Action**: Rephrase to AI-directive protocols (apply_narrative_voice(), validate_profile_match())

#### Moderate Issues

**M13-M1: Module 12/13 Terminology Confusion**
- **Problem**: Both use "narrative scales" for different concepts
- **Action**: Emphasize distinction earlier (M12 = Power Scaling Modes, M13 = DNA Scales)

**M13-M2: Confidence Threshold Undefined**
- **Action**: Define: "<70% = require player validation, ≥70% = optional"

**M13-M3: Profile Blending Method Unspecified**
- **Action**: Define: "Average scales, union tropes (ON if either ON), prioritize primary profile pacing/tone"

#### Key Strengths to Preserve

1. **10 Narrative DNA Scales** (0-10 each):
   - Introspection vs Action
   - Comedy vs Drama
   - Simple vs Complex
   - Power Fantasy vs Struggle
   - Explained vs Mysterious
   - Fast vs Slow
   - Episodic vs Serialized
   - Grounded vs Absurd
   - Tactical vs Instinctive
   - Hopeful vs Cynical

2. **15 Trope Switches** (ON/OFF):
   - Fourth Wall Breaks, Inner Monologue, Visual Metaphor, Rapid Tonal Shifts
   - Tournament Arcs, Power of Friendship, Tragic Backstories, Escalating Threats
   - Slice-of-Life, Mystery Box, Unreliable Narrator, Existential Philosophy
   - Rule of Cool, Mundane→Epic, Tragic Hero

3. **DNA → Mechanical Scaffolding Mapping**:
   - Power Fantasy 0-2 → Instant OP growth model
   - Power Fantasy 3-6 → Accelerated growth model
   - Power Fantasy 7-10 → Modest growth model
   - Fast 0-3 → High XP (1K-1.5K/session)
   - Tactical 7-10 → 6-stat + custom mechanics

4. **Genre Auto-Load Rules** (11 campaign types):
   - Spy/Espionage → mystery_thriller + seinen
   - Horror → horror + mystery_thriller
   - Tournament → shonen + sports
   - Isekai → isekai + comedy OR seinen
   - And 7 more...

5. **Profile Library** (12+ pre-calibrated profiles):
   - DanDaDan, Hunter x Hunter, JJK, Demon Slayer, AoT
   - Konosuba, Death Note, Re:Zero, Mushishi, Vinland Saga
   - Code Geass, Haikyuu
   - Each ~3,000 tokens with scales, tropes, 3 example scenes

6. **3 Extraction Methods**:
   - Research-Derived (Module 07 automatic)
   - Player-Provided (Session Zero questionnaire)
   - Hybrid (player adjusts research)

#### Required Tests

| Test ID | Description | Validates |
|---------|-------------|-----------|
| M13-T1 | Research DanDaDan → extract 10 scales + 15 tropes | Automatic extraction |
| M13-T2 | Same scene × 3 profiles → 3 different narrations | Profile affects voice |
| M13-T3 | Power Fantasy 0 + Fast 2 + Tactical 7 → correct mechanics | DNA→mechanics mapping |
| M13-T4 | "spy thriller" keywords → auto-load mystery_thriller | Genre auto-load |
| M13-T5 | Player: "too much explanation" → adjust + apply | Feedback loop |
| M13-T6 | Player: "HxH vibes" → load library profile | Quick access workflow |
| M13-T7 | Custom world + "Seinen" vibe → <2min setup | Spartan quick calibration |
| M13-T8 | Combat scene + DanDaDan profile → NO D&D checklist | Prevents generic voice |

#### System-Wide Pattern: Human-Centric Language

**Modules Affected**: 07, 08, 09, 10, 11, 12, 13 (7 consecutive modules, 46.7% of AIDM)  
**Recommendation**: After completing all reviews, perform system-wide language audit and rephrase to AI-directive operational format.

---

