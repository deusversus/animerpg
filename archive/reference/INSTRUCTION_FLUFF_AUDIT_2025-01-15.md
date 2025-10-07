# AIDM Instruction Module Fluff Audit

**Date**: January 15, 2025  
**Scope**: `/aidm/` instruction modules and libraries  
**Purpose**: Identify redundancy, verbosity, excessive examples in AIDM system files

---

## Executive Summary

**Total AIDM Files**: 30 active instruction/library files (excluding backups)  
**Total Word Count**: ~38,000 words  
**Estimated Fluff**: ~8,000-10,000 words (21-26% reduction potential)  
**Primary Issues**: 
- Verbose examples with full JSON schemas embedded
- Repetitive scenario walkthroughs
- Excessive meta-commentary
- Redundant "WRONG vs CORRECT" examples
- Verbose checklists with redundant items

---

## Priority Targets

### P0: Critical Fluff (Highest Impact)

#### 1. **07_anime_integration.md** (5,402w → target 3,500w = 1,900w reduction)

**Major Issues**:
- **Lines 221-441 (220 lines)**: Full Devil Fruits JSON schema example
  - Problem: Embeds complete `power_system_schema.json` structure (120 lines)
  - Solution: Replace with "See power_system_schema.json format" + 10-line summary
  - Savings: ~1,500 words

- **Regression section (lines 700-1000)**: Repetitive temporal model examples
  - Problem: 3 separate 40-50 line scenario walkthroughs (Stable/Butterfly/Fixed Points)
  - Solution: Compress to comparison table + 1 example
  - Savings: ~400 words

**Specific Fluff**:
- Lines 52-76: Self-Assessment example (Naruto chakra) - 25 lines for simple concept
- Lines 136-170: Method 1 example - verbose player dialogue
- Lines 447-490: Harmonization examples - repetitive power balancing scenarios
- Lines 582-650: Integration methods - 4 separate 15-line examples (can be table)

**Recommended Compression**:
1. Devil Fruits example: 220 lines → 30 lines (reference schema, show verification flow only)
2. Regression examples: Compress 3 walkthroughs → 1 table + 1 short example
3. Self-Assessment: Reduce example verbosity (25 lines → 8 lines)
4. Integration Methods: Convert 4 examples to table with brief notes

**Estimated Savings**: 1,900 words (35% reduction)

---

#### 2. **05_narrative_systems.md** (2,377w → target 1,800w = 577w reduction)

**Major Issues** (requires file read to confirm):
- Likely verbose drift calculation examples
- Redundant meta-command walkthroughs
- Excessive consistency validation prose

**Estimated Savings**: 577 words (24% reduction)

---

#### 3. **06_session_zero.md** (2,352w → target 1,800w = 552w reduction)

**Major Issues** (requires file read):
- 5-phase process likely has repetitive "Step X" structures
- Verbose preference gathering examples
- Excessive calibration walkthroughs

**Estimated Savings**: 552 words (23% reduction)

---

#### 4. **12_player_agency.md** (2,107w → target 1,500w = 607w reduction)

**Major Issues** (requires file read):
- Sacred Rule likely has repetitive violation warnings
- Multiple redundant examples of PRESENT→ASK→STOP→WAIT
- Verbose Emergency Override Protocol

**Estimated Savings**: 607 words (29% reduction)

---

### P1: High-Value Targets

#### 5. **01_cognitive_engine.md** (1,834w → target 1,400w = 434w reduction)

**Issues**:
- 6-stage pipeline likely has verbose stage descriptions
- Redundant intent classification examples
- Drift Signature Cache may have excessive explanation

**Estimated Savings**: 434 words (24% reduction)

---

#### 6. **Genre Trope Libraries** (seinen/slice_of_life/shonen/isekai - combined 5,480w → target 4,100w = 1,380w reduction)

**Issues**:
- Verbose trope descriptions (1-2 paragraphs when 2-3 sentences suffice)
- Redundant anime examples (listing 5-6 when 2-3 demonstrates concept)
- Excessive "How to Use" meta-commentary

**Specific Files**:
- `seinen_tropes.md` (1,733w) → 1,300w (433w savings)
- `slice_of_life_tropes.md` (1,430w) → 1,100w (330w savings)
- `shonen_tropes.md` (1,212w) → 900w (312w savings)
- `isekai_tropes.md` (1,105w) → 900w (305w savings)

**Estimated Savings**: 1,380 words (25% avg reduction)

---

### P2: Moderate Targets

#### 7-14. **Remaining Instruction Modules** (combined 8,200w → target 6,700w = 1,500w reduction)

| Module | Current | Target | Savings | Key Issues |
|--------|---------|--------|---------|------------|
| `02_learning_engine.md` | 1,266w | 1,050w | 216w | Verbose memory thread examples |
| `04_npc_intelligence.md` | 1,219w | 1,000w | 219w | Redundant affinity examples |
| `10_error_recovery.md` | 1,535w | 1,200w | 335w | Excessive consistency check prose |
| `11_dice_resolution.md` | 1,042w | 850w | 192w | Verbose probability tables |
| `03_state_manager.md` | 766w | 650w | 116w | JSON export examples |
| `08_combat_resolution.md` | 758w | 650w | 108w | Redundant combat examples |
| `09_progression_systems.md` | 723w | 600w | 123w | Verbose XP formulas |
| `00_system_initialization.md` | 704w | 600w | 104w | Repetitive load order checks |

---

### P3: Low-Priority (Light Touch)

#### 15-20. **Power System & Mechanics Libraries** (combined 4,700w → target 4,100w = 600w reduction)

**Issues**:
- Redundant anime examples
- Verbose framework descriptions
- Excessive "common mistakes" sections

**Files**:
- `psionic_psychic_systems.md` (1,484w) → 1,300w (184w)
- `power_scaling_narrative.md` (1,143w) → 1,000w (143w)
- `ki_lifeforce_systems.md` (1,024w) → 900w (124w)
- `soul_spirit_systems.md` (939w) → 850w (89w)
- `mana_magic_systems.md` (861w) → 800w (61w)

---

#### 21-23. **Common Mechanics Libraries** (combined 2,895w → target 2,600w = 295w reduction)

**Issues**:
- Verbose framework tables
- Redundant leveling curve examples

**Files**:
- `stat_frameworks.md` (1,074w) → 950w (124w)
- `leveling_curves.md` (978w) → 880w (98w)
- `skill_taxonomies.md` (843w) → 770w (73w)

---

#### 24. **CORE_AIDM_INSTRUCTIONS.md** (1,016w → target 950w = 66w reduction)

**Issues**:
- Minimal fluff (master control file)
- Check for verbose meta-command interface
- Redundant behavioral rules

**Estimated Savings**: 66 words (6% reduction - minimal touch)

---

## Compression Strategy

### Phase 1: Module 07 Deep Clean (P0)
1. Replace 220-line Devil Fruits JSON with 30-line reference
2. Compress regression examples (3 scenarios → 1 table + 1 example)
3. Reduce self-assessment verbosity
4. Convert integration methods to table
**Target**: 1,900 words removed

### Phase 2: High-Value Modules (P0 remaining + P1)
1. Audit and compress Modules 05, 06, 12, 01
2. Compress genre trope libraries (4 files)
**Target**: 3,550 words removed

### Phase 3: Moderate Modules (P2)
1. Spot-compress remaining 8 instruction modules
**Target**: 1,500 words removed

### Phase 4: Libraries & Light Touch (P3)
1. Compress power system libraries (5 files)
2. Compress common mechanics (3 files)
3. Light touch on CORE
**Target**: 961 words removed

---

## Total Estimated Impact

**Before**: ~38,000 words  
**After**: ~30,000 words  
**Reduction**: ~8,000 words (21%)  

**Token Estimate** (at 2.73 ratio):
- Before: ~103,700 tokens
- After: ~81,900 tokens
- Savings: ~21,800 tokens

**Critical Note**: This audit focuses on INSTRUCTION modules (the AIDM product). Documentation fluff removal (completed separately) saved ~7,100 words from development docs.

---

## Compression Principles

1. **Replace embedded schemas with references** - "See X_schema.json" instead of full JSON
2. **Convert repetitive examples to tables** - Show pattern once, not 3-4 times
3. **Compress verbose dialogues** - Summarize player/AIDM exchanges, don't script them
4. **Eliminate redundant "WRONG vs CORRECT"** - Show correct pattern, note what to avoid
5. **Reduce anime example lists** - 2-3 examples sufficient, not 5-6
6. **Remove meta-commentary** - Instructions should be directive, not explanatory essays

---

## Next Steps

1. ✅ Create audit document (this file)
2. ⏳ Execute Phase 1: Module 07 deep clean
3. ⏳ Execute Phase 2: High-value modules
4. ⏳ Execute Phase 3: Moderate modules
5. ⏳ Execute Phase 4: Libraries & light touch
6. ⏳ Validate via word count checks
7. ⏳ Update STATE.md with completion
8. ⏳ Archive this audit report

---

**Audit Complete** - Ready for systematic compression
