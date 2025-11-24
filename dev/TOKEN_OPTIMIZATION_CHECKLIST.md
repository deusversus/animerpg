# Token Optimization Quick Reference

**For AIDM Developers**: Use this checklist when creating or modifying files  
**Full Guide**: See `dev/TOKEN_OPTIMIZATION_METHODOLOGY.md`

**⚠️ CRITICAL**: "Expected ranges" are observations from past work, NOT goals or limits. Continue optimizing until information parity risk emerges, regardless of ranges. Stopping at an "expected range" is bad praxis.

---

## Critical Concept: Two-Dimensional Information Parity

**Module 05 Lesson**: Information parity has TWO dimensions, not one.

### Dimension 1: Implementation Completeness (WHAT to code)

**Formulas + Values + Logic**:
- All numeric values: 1.5x, 0.5x, DC16, tier_3@100
- All formulas: `skill_xp = base × rate`
- All branching: success→X, fail→Y
- All mappings: "deep"/"superficial", "high"=2-3

**Test**: Can implementer write correct code?

### Dimension 2: Pedagogical Sufficiency (HOW to apply)

**Examples + Tone + Style**:
- Narrative examples showing tone (serious/comedic/dramatic)
- Pacing patterns (summary/detail/montage)
- Style per profile (HxH vs Konosuba vs MHA)
- Formula → output transformation

**Test**: Can implementer generate appropriate narrative matching source anime style?

### The False Positive Pattern

```
❌ VALIDATION FAIL (Module 05 initial):
✓ Formulas present (Dimension 1)
✗ No narrative examples (Dimension 2)
Claimed: 100% parity | Reality: 60-70% parity

✅ VALIDATION PASS (Module 05 restored):
✓ Formulas present (Dimension 1)
✓ 2-3 narrative examples per system (Dimension 2)
Result: TRUE 100% parity at 66.4% reduction
```

**Both dimensions required for TRUE 100% parity.**

---

## Quick Technique Reference

| Technique | Before | After | Savings |
|-----------|--------|-------|---------|
| **Emoji Replace** | ✅ Success | [OK] | 2-4 tokens |
| **Header Consolidate** | Version: 2.0 / Priority: High | v2.0 \| P:High | ~10 tokens |
| **Verbose Compress** | "ranges from 0 (unknown) to 4 (expert)" | "0=UNKNOWN→4=EXPERT" | ~8 tokens |
| **List Compress** | Multiple bullet items | Item1 \| Item2 \| Item3 | ~5 tokens |
| **Example Reduce** | 4 anime examples × 6 lines each | 2 iconic examples × 1 line | ~100 tokens |
| **Formula Inline** | "XP = (Level × 1000) + (Level² × 100)" | XP=Lv×1k+Lv²×100 | ~6 tokens |

---

## Multi-Pass Optimization Process

### Pass 1: Structural (Expected Range: 30-40% reduction)

- [ ] Replace ALL emojis with text brackets ([OK]/[NO]/[!]/[*]/[i])
- [ ] Consolidate headers (metadata: 3-4 lines → 1 line with pipes)
- [ ] Remove obvious redundancy (duplicate explanations)
- [ ] Compress basic lists (bullets → inline with pipes)
- [ ] **Checkpoint**: Run word count (expected ~35-40%, continue optimizing)

### Pass 2: Content (Expected Range: 50-60% reduction)

- [ ] Verbose→compact transformations (prose → structured data)
- [ ] Reduce examples (keep 1-2 iconic anime references only)
- [ ] Compress tables (merge columns, abbreviate)
- [ ] Inline formulas (remove verbose explanations)
- [ ] **Checkpoint**: Run word count (expected ~50-60%, continue optimizing)

### Pass 3: Refinement (Expected Range: 60-75% reduction)

- [ ] Merge related sections (eliminate intermediate headers)
- [ ] Eliminate excess whitespace (max 1 blank line between sections)
- [ ] Shorten cross-references (verbose paths → →filename)
- [ ] Final polish (review every line for compression opportunities)
- [ ] **Checkpoint**: Run word count (expected 60-75%, continue optimizing)

### Pass 4: Validation (CRITICAL - 100% information parity)

**⚠️ WARNING**: Dry tests check CONCEPT PRESENCE (keywords), not IMPLEMENTATION COMPLETENESS (formulas/values) or PEDAGOGICAL SUFFICIENCY (narrative examples). A file can PASS dry tests while MISSING critical implementation details OR lacking examples showing HOW to apply them.

**⚠️ MODULE 05 LESSON**: File had formulas (WHAT to implement) but no narrative examples (HOW to apply with appropriate tone/style). Achieved 78.4% reduction but only 60-70% parity. True 100% parity required restoring narrative examples → 66.4% reduction with TRUE parity.

- [ ] Run 3+ dry tests (grep searches for critical content - concepts only)
- [ ] **IMPLEMENTATION DETAIL VALIDATION** (Required for files with formulas/code):
  - [ ] Extract all numeric values from backup (multipliers, thresholds, rates, DCs)
  - [ ] Verify each numeric value present in optimized (exact or in formula notation)
  - [ ] Check formula structures: `skill_xp = base × rate` patterns preserved
  - [ ] Check branching logic: success→X, fail→Y outcomes documented
  - [ ] Check categorical mappings: "deep"/"superficial", "high"=2-3 preserved
  - [ ] Test: Can implementer write correct code from optimized file alone?
  - [ ] If NO: **CRITICAL FAILURE** - restore missing values
- [ ] **CODE BLOCK CHECK**: Analyze removed code blocks
  - [ ] Were code blocks removed during optimization?
  - [ ] If YES: Categorize each as illustrative or instructive
  - [ ] If INSTRUCTIVE: Verify implementation details preserved (formulas, multipliers, thresholds, branching logic)
  - [ ] Cross-check with Implementation Detail Validation above
  - [ ] If NO: Restore critical details in ultra-compact format
- [ ] **NARRATIVE EXAMPLE VALIDATION** (Required for narrative system files):
  - [ ] Does file describe narrative generation, storytelling, or player-facing content?
  - [ ] If YES: Count narrative examples in backup (how many show tone/style/pacing?)
  - [ ] Verify 2-3 narrative examples preserved per major system/mechanic
  - [ ] Check examples demonstrate: tone variation, pacing patterns, style per profile
  - [ ] Test: Can implementer generate appropriate narrative (not just correct formulas)?
  - [ ] If NO: **PEDAGOGICAL FAILURE** - restore 2-3 key narrative examples
  - [ ] Target: Show formula → narrative transformation (e.g., "success=base×1.5 | Ex: 'Wing nods...' [+300 XP]")
- [ ] Compare to backup (all formulas/examples/cross-refs intact?)
- [ ] Spot-check anime examples (iconic refs still present?)
- [ ] Verify all mechanics explained (even if compressed)
- [ ] **Zero markdown linting errors** (MD022, MD031, MD032, MD033, MD040)
- [ ] **Decision**: If parity < 100% OR implementation details missing OR narrative pedagogy insufficient → rollback and adjust. If TRUE 100% → commit.

---

## Validation Commands (Copy-Paste Ready)

### Word Count Check (PowerShell)

```powershell
# Count words in file
$words = (Get-Content filename.md | Measure-Object -Word).Words
Write-Host "Words: $words"

# Estimate tokens (2.73 conversion ratio - validated via external test)
$tokens = [math]::Round($words * 2.73)
Write-Host "Estimated tokens: $tokens"

# Calculate reduction from baseline
$baseline = 2000  # Replace with actual baseline word count
$reduction = [math]::Round((($baseline - $words) / $baseline) * 100, 1)
Write-Host "Reduction: $reduction%"
```

### Dry Test Example (grep searches)

```powershell
# Test 1: Verify anime examples exist
grep -i "naruto|goku|rimuru|ainz" filename.md

# Test 2: Verify formulas intact
grep -i "xp.*level|hp.*con|damage.*str" filename.md

# Test 3: Verify cross-references work
grep -i "stat_frameworks|power_systems|skill_taxonomies" filename.md
```

### Information Parity Check

```powershell
# Compare with backup (show differences)
git diff filename_BACKUP.md filename.md
```

---

## Expected Ranges by File Type

| File Type | Conservative Range | Aggressive Range | Notes |
|-----------|--------------|------------|-------|
| **Instruction Modules** | 40-55% | 60-75% | Best performers: 70-85% (simple mechanics) |
| **Library Files** | 35-50% | 55-70% | Precision hold: 40-50% (formula-heavy) |
| **Schema Files** | 10-25% | 25-40% | Already terse, diminishing returns |
| **Core/Meta Files** | 40-60% | 60-75% | Similar to instruction modules |

**Campaign Results** (observed achievements, not limits):

- Phase 1 (13 instruction modules): 60.8% avg reduction
- Phase 2 (9 library files): 59.3% avg reduction
- Overall (22 files): 74.3% total reduction with 100% information parity

---

## Red Flags: When to STOP

❌ **DON'T compress if**:

- Formula becomes cryptic or error-prone
- Removing last example would leave concept too abstract
- **Removing narrative examples leaves no tone/style guidance**
- Information parity drops below 100% (implementation OR pedagogy)
- Cross-references become ambiguous

⚠️ **PRECISION HOLD scenarios**:

- Complex mechanics (seinen psychological warfare)
- Formula-heavy content (leveling curves, damage calculations)
- Multi-condition logic (decision trees, state machines)
- First-of-kind examples (establishing new patterns)
- **Narrative systems (need 2-3 examples showing tone/pacing/style)**

**Rule**: If in doubt, preserve clarity. 55% reduction with 100% parity > 75% reduction with 95% parity.

**Module 05 Example**: 78.4% reduction but only 60-70% parity (missing narrative pedagogy) → Restored to 66.4% reduction with TRUE 100% parity (formulas + examples). The extra ~800 words made the difference between "can code" and "can generate appropriate narratives".

---

## Pre-Optimization Checklist

**Step 0: Already-Optimized Detection** ⚠️

**CRITICAL**: Re-optimizing already-optimized files causes information loss. Check first.

**Quick Detection** (5+ markers = STOP):

- [ ] Headers ultra-compact? (v2.0 | P:X | Load:Y)
- [ ] Lists inline? (Item1 | Item2 | Item3)
- [ ] Cross-refs terse? (→filename)
- [ ] Formulas compact? (skill_xp=base×rate)
- [ ] Examples minimal? (2-3 per system)
- [ ] Word count in optimized range? (instruction: 1,500-2,500, library: 800-1,500)
- [ ] Avg word length <6 chars?

**If 5+ markers**: Document "already optimized", run validation, SKIP to next file.

**Step 1-5: Standard Workflow**

- [ ] Create backup (`filename_BACKUP.md` or zip workspace)
- [ ] Document baseline word count
- [ ] Identify file type (instruction/library/schema/core)
- [ ] Note expected range (conservative vs aggressive, not a limit)
- [ ] Plan 3-5 dry tests for validation

---

## Post-Optimization Checklist

- [ ] All dry tests PASS (100% required)
- [ ] Information parity check vs backup (100% required)
- [ ] Word count reduction documented (expected 60-75% for aggressive, continue if possible)
- [ ] Token estimate calculated (words × 2.73)
- [ ] **Zero markdown linting errors** (prevents wasted tokens in future loads)
- [ ] Update tracking documentation (TOKEN_OPTIMIZATION_AUDIT.md)
- [ ] Commit with descriptive message
- [ ] Delete backup file (after confirming commit)

---

## Quick Examples

### Before/After: Header Consolidation

```markdown
❌ BEFORE (4 lines, ~16 tokens):
## Combat Resolution System
**Version**: 2.1
**Priority**: High
**Dependencies**: dice_engine, state_manager

✅ AFTER (1 line, ~10 tokens):
## Combat Resolution | v2.1 | P:High | Deps:dice,state
```

**Savings**: ~6 tokens (38%)

### Before/After: Verbose Compression

```markdown
❌ BEFORE (50 tokens):
The familiarity scale ranges from 0 (completely unknown - the player has never 
heard of the concept) to 4 (expert mastery - the player has deep understanding).

✅ AFTER (18 tokens):
Familiarity: 0=UNKNOWN(never heard)→Full research | 1=HEARD→Quick research | 
2=KNOW→Verify | 3=FLUENT→Apply | 4=EXPERT→Innovate
```

**Savings**: 32 tokens (64%)

### Before/After: Example Reduction

```markdown
❌ BEFORE (~180 tokens):
Shonen Training Arc Examples:
- Naruto's chakra control training (tree climbing, water walking) - 6 lines
- Goku's gravity chamber training with King Kai - 5 lines
- Deku's quirk control with Gran Torino - 7 lines
- Tanjiro's breathing technique refinement - 6 lines

✅ AFTER (~25 tokens):
Training: Naruto(chakra→tree/water) | Goku(gravity×King Kai) | 
Deku(quirk→Gran Torino)
```

**Savings**: 155 tokens (86%)

---

## Emergency Override

**If optimization is taking too long**:

1. Focus on Pass 1 only (30-40% reduction)
2. Mark file as "partially optimized" in STATE.md
3. Return for Passes 2-3 later
4. Document why optimization paused

**Never skip validation**: Even 30% reduction needs 100% information parity check.

---

## Success Metrics

**From 74.3% Reduction Campaign**:

- 22 files optimized (13 instructions + 9 libraries)
- 34,746 tokens saved (46,742 → 13,669)
- 100% information parity maintained (10+ dry tests, all passed)
- Zero functional regressions (5 comprehensive session tests)

**Your goal**: Match or exceed these results for new/modified files.

---

**Full Methodology**: `dev/TOKEN_OPTIMIZATION_METHODOLOGY.md`  
**Current System Status**: 87,031 tokens (43.5% of 200K budget) - Base system ✅  
**Token Budget Alert Threshold**: >100,000 tokens (50% of 200K) ⚠️
