# Token Optimization Quick Reference
**For AIDM Developers**: Use this checklist when creating or modifying files  
**Full Guide**: See `docs/TOKEN_OPTIMIZATION_METHODOLOGY.md`

---

## Quick Technique Reference

| Technique | Before | After | Savings |
|-----------|--------|-------|---------|
| **Emoji Replace** | ✅ Success | [OK] | 2-4 tokens |
| **Header Consolidate** | Version: 2.0<br>Priority: High | v2.0 \| P:High | ~10 tokens |
| **Verbose Compress** | "ranges from 0 (unknown) to 4 (expert)" | "0=UNKNOWN→4=EXPERT" | ~8 tokens |
| **List Compress** | • Item 1<br>• Item 2<br>• Item 3 | Item1 \| Item2 \| Item3 | ~5 tokens |
| **Example Reduce** | 4 anime examples × 6 lines each | 2 iconic examples × 1 line | ~100 tokens |
| **Formula Inline** | "XP = (Level × 1000) + (Level² × 100)" | XP=Lv×1k+Lv²×100 | ~6 tokens |

---

## Multi-Pass Optimization Process

### Pass 1: Structural (30-40% reduction target)
- [ ] Replace ALL emojis with text brackets ([OK]/[NO]/[!]/[*]/[i])
- [ ] Consolidate headers (metadata: 3-4 lines → 1 line with pipes)
- [ ] Remove obvious redundancy (duplicate explanations)
- [ ] Compress basic lists (bullets → inline with pipes)
- [ ] **Checkpoint**: Run word count → verify ~35-40% reduction

### Pass 2: Content (50-60% reduction target)
- [ ] Verbose→compact transformations (prose → structured data)
- [ ] Reduce examples (keep 1-2 iconic anime references only)
- [ ] Compress tables (merge columns, abbreviate)
- [ ] Inline formulas (remove verbose explanations)
- [ ] **Checkpoint**: Run word count → verify ~50-60% reduction

### Pass 3: Refinement (60-75% reduction target)
- [ ] Merge related sections (eliminate intermediate headers)
- [ ] Eliminate excess whitespace (max 1 blank line between sections)
- [ ] Shorten cross-references (verbose paths → →filename)
- [ ] Final polish (review every line for compression opportunities)
- [ ] **Checkpoint**: Run word count → verify 60-75% reduction

### Pass 4: Validation (CRITICAL - 100% information parity)
- [ ] Run 3+ dry tests (grep searches for critical content)
- [ ] Compare to backup (all formulas/examples/cross-refs intact?)
- [ ] Spot-check anime examples (iconic refs still present?)
- [ ] Verify all mechanics explained (even if compressed)
- [ ] **Decision**: If parity < 100% → rollback and adjust. If 100% → commit.

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

## Target Reductions by File Type

| File Type | Conservative | Aggressive | Notes |
|-----------|--------------|------------|-------|
| **Instruction Modules** | 40-55% | 60-75% | Best performers: 70-85% (simple mechanics) |
| **Library Files** | 35-50% | 55-70% | Precision hold: 40-50% (formula-heavy) |
| **Schema Files** | 10-25% | 25-40% | Already terse, diminishing returns |
| **Core/Meta Files** | 40-60% | 60-75% | Similar to instruction modules |

**Campaign Results** (proven achievable):
- Phase 1 (13 instruction modules): 60.8% avg reduction
- Phase 2 (9 library files): 59.3% avg reduction
- Overall (22 files): 74.3% total reduction with 100% information parity

---

## Red Flags: When to STOP

❌ **DON'T compress if**:
- Formula becomes cryptic or error-prone
- Removing last example would leave concept too abstract
- Information parity drops below 100%
- Cross-references become ambiguous

⚠️ **PRECISION HOLD scenarios**:
- Complex mechanics (seinen psychological warfare)
- Formula-heavy content (leveling curves, damage calculations)
- Multi-condition logic (decision trees, state machines)
- First-of-kind examples (establishing new patterns)

**Rule**: If in doubt, preserve clarity. 55% reduction with 100% parity > 75% reduction with 95% parity.

---

## Pre-Optimization Checklist

- [ ] Create backup (`filename_BACKUP.md` or zip workspace)
- [ ] Document baseline word count
- [ ] Identify file type (instruction/library/schema/core)
- [ ] Set reduction target (conservative vs aggressive)
- [ ] Plan 3-5 dry tests for validation

---

## Post-Optimization Checklist

- [ ] All dry tests PASS (100% required)
- [ ] Information parity check vs backup (100% required)
- [ ] Word count reduction meets target (60-75% for aggressive)
- [ ] Token estimate calculated (words × 2.73)
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

**Full Methodology**: `docs/TOKEN_OPTIMIZATION_METHODOLOGY.md`  
**Current System Status**: 87,031 tokens (43.5% of 200K budget) - Base system ✅  
**Token Budget Alert Threshold**: >100,000 tokens (50% of 200K) ⚠️
