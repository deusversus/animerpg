# Token Optimization Plan - Narrative Profile Library Integration

**Created**: 2025-01-15  
**Scope**: All files modified/created during narrative profile library creation  
**Baseline**: ~22,990 tokens  
**Target**: 6,000-9,000 tokens (60-75% reduction)  
**Estimated Savings**: ~14,000-17,000 tokens

---

## Files to Optimize

### Priority 1: Instruction Modules (Target: 60-75% reduction)

| File | Current | Target | Strategy |
|------|---------|--------|----------|
| `13_narrative_calibration.md` | ~2,194 tokens | 550-880 tokens | Remove all inline profile examples (point to library), compress extraction methods, condense scale descriptions |
| `06_session_zero.md` | ~2,228 tokens | 560-890 tokens | Compress Phase 0.5 narrative calibration (added), optimize existing phases |
| `00_system_initialization.md` | ~562 tokens | 225-280 tokens | Already optimized, minimal touch-up |

**Subtotal**: 4,984 tokens → 1,335-2,050 tokens (60-73% reduction, ~3,000 tokens saved)

---

### Priority 2: Profile Library Index (Target: 50-60% reduction)

| File | Current | Target | Strategy |
|------|---------|--------|----------|
| `PROFILE_INDEX.md` | ~1,591 tokens | 640-795 tokens | Compress genre descriptions, condense cross-reference matrix, inline workflows |

**Subtotal**: 1,591 tokens → 640-795 tokens (50-60% reduction, ~800-950 tokens saved)

---

### Priority 3: Individual Profiles (Target: 40-50% reduction per file)

| File | Current | Target | Technique |
|------|---------|--------|-----------|
| `rezero_profile.md` | ~1,630 tokens | 815-980 tokens | Compress example scenes (longest), condense scale notes |
| `haikyuu_profile.md` | ~1,585 tokens | 795-950 tokens | Compress sports terminology, condense match scenes |
| `vinland_saga_profile.md` | ~1,568 tokens | 785-940 tokens | Compress historical violence descriptions |
| `mushishi_profile.md` | ~1,518 tokens | 760-910 tokens | Condense contemplative scene descriptions |
| `code_geass_profile.md` | ~1,503 tokens | 750-900 tokens | Compress strategic planning examples |
| `demon_slayer_profile.md` | ~1,415 tokens | 710-850 tokens | Condense breathing technique descriptions |
| `death_note_profile.md` | ~1,402 tokens | 700-840 tokens | Compress dual inner monologue examples |
| `jujutsu_kaisen_profile.md` | ~1,340 tokens | 670-800 tokens | Condense cursed technique explanations |
| `attack_on_titan_profile.md` | ~1,265 tokens | 635-760 tokens | Compress military tactics scenes |
| `konosuba_profile.md` | ~1,237 tokens | 620-740 tokens | Condense comedy examples |
| `hunter_x_hunter_profile.md` | ~1,126 tokens | 565-675 tokens | Compress Nen explanations |
| `dandadan_profile.md` (existing) | ~826 tokens | 415-495 tokens | Light optimization (already created earlier) |

**Subtotal**: 16,415 tokens → 8,220-9,850 tokens (40-50% reduction, ~6,565-8,195 tokens saved)

---

## Total Projected Savings

**Baseline**: 22,990 tokens  
**After Optimization**: 10,195-12,695 tokens  
**Reduction**: 44-56% (10,295-12,795 tokens saved)

**Note**: Conservative estimate due to profile format standardization (harder to compress without information loss). Actual may achieve 50-60% if aggressive techniques applied.

---

## Optimization Strategy by File Type

### Instruction Modules (13, 06, 00)

**Pass 1** - Remove Redundancy:
- Module 13: Delete all inline profile examples (DanDaDan, HxH, Konosuba, AoT) → point to library
- Module 06: Phase 0.5 already concise, compress examples only
- Module 00: Minimal changes (already optimized)

**Pass 2** - Compress Structure:
- Header consolidation (Version/Priority/Load → single line)
- Scale descriptions: verbose → compact bullets
- Extraction methods: prose → structured steps

**Pass 3** - Final Polish:
- Whitespace elimination
- Cross-reference shortening (→file notation)
- Example reduction (keep 1-2 per concept max)

---

### Profile Library Index

**Pass 1** - Structural:
- Genre tables: verbose descriptions → terse bullets
- Cross-reference matrix: full sentences → inline format
- Workflow examples: step-by-step prose → numbered compact

**Pass 2** - Content:
- Remove "How to Use" verbose explanations → terse bullets
- Compress blending guidelines → table format
- Inline profile summaries → compress to 1-line per profile

**Pass 3** - Polish:
- Merge similar sections (Quick Reference + Workflows)
- Whitespace reduction
- File path references → terse notation

---

### Individual Profiles (12 files)

**Standardized Approach** (apply to all):

**Pass 1** - Example Scene Compression (BIGGEST SAVINGS):
- Combat examples: 40-60 lines → 20-30 lines
  - Remove verbose dialogue attribution
  - Compress action descriptions (3 lines → 1 line)
  - Inline inner monologues (3 lines → 1 line inline)
  - Keep core narrative beats only
  
**Pass 2** - Scale/Trope Tables:
- Notes column: Full sentences → terse phrases
- Merge similar entries
- Use abbreviations (introspection→INTRO, tactical→TACT)

**Pass 3** - Metadata/Usage Notes:
- Adjustment logs: Full entries → compact table
- Usage notes: Bullet paragraphs → inline tips
- Common mistakes: Verbose → ❌/✅ pattern

---

## Execution Order

**Session 1** (Now):
1. Module 13 (remove redundant examples)
2. PROFILE_INDEX (compress workflows/matrices)
3. Validate with grep tests

**Session 2**:
4. Optimize 6 profiles (rezero, haikyuu, vinland, mushishi, code_geass, demon_slayer)
5. Validate information parity

**Session 3**:
6. Optimize 6 profiles (death_note, jjk, aot, konosuba, hxh, dandadan)
7. Module 06 final optimization
8. Module 00 touch-up

**Session 4**:
9. Final validation (all dry tests)
10. Token count verification
11. Commit with changelog

---

## Validation Protocol

### Dry Tests (Run After Each File)

**Module 13**:
```powershell
# Test profile library reference exists
grep -i "PROFILE_INDEX|narrative_profiles" 13_narrative_calibration.md

# Test scales still defined
grep -i "Introspection vs Action|Comedy vs Drama" 13_narrative_calibration.md
```

**PROFILE_INDEX**:
```powershell
# Test all 13 profiles listed
grep -i "Hunter x Hunter|Jujutsu Kaisen|Demon Slayer" PROFILE_INDEX.md

# Test cross-reference matrix exists
grep -i "If Player Wants.*Recommend" PROFILE_INDEX.md
```

**Individual Profiles**:
```powershell
# Test key features intact (example for HxH)
grep -i "tactical|Nen|strategy 10/10" hunter_x_hunter_profile.md

# Test example scenes exist
grep -i "Combat Example|Dialogue Example|Exploration Example" hunter_x_hunter_profile.md
```

---

## Information Parity Checklist

For each file, verify:
- [ ] All narrative scales present (10 scales)
- [ ] All trope switches documented (15 tropes)
- [ ] Pacing rhythm parameters complete
- [ ] Dialogue/combat styles intact
- [ ] 3 example scenes per profile (or equivalent for modules)
- [ ] Cross-references functional
- [ ] Usage notes preserved
- [ ] Formulas/mechanics unchanged

---

## Token Counting Commands

```powershell
# Single file
$words = (Get-Content aidm/instructions/13_narrative_calibration.md | Measure-Object -Word).Words
$tokens = [math]::Round($words * 0.75)
Write-Host "Tokens: $tokens"

# All narrative profiles
$total = 0
Get-ChildItem aidm/libraries/narrative_profiles/*.md | ForEach-Object {
    $words = (Get-Content $_ | Measure-Object -Word).Words
    $tokens = [math]::Round($words * 0.75)
    $total += $tokens
}
Write-Host "Total profile tokens: $total"

# All modified modules
$files = @("13_narrative_calibration.md", "06_session_zero.md", "00_system_initialization.md")
$total = 0
foreach ($file in $files) {
    $words = (Get-Content "aidm/instructions/$file" | Measure-Object -Word).Words
    $tokens = [math]::Round($words * 0.75)
    $total += $tokens
}
Write-Host "Total module tokens: $total"
```

---

## Success Criteria

Optimization complete when:
- ✅ Total tokens ≤ 12,000 (47% reduction minimum)
- ✅ All dry tests pass (100%)
- ✅ Information parity verified (checklist 100%)
- ✅ No functional regressions
- ✅ Grep searches for anime examples return hits
- ✅ Cross-references resolve correctly
- ✅ Profile structure standardized across all 13 files

---

## Risk Mitigation

**Backup Strategy**:
- Git commit before starting ("PRE-OPTIMIZATION checkpoint")
- Can revert individual files if parity breaks
- Keep optimization plan for reference

**If Parity Fails**:
1. Identify missing information via checklist
2. Restore from git history
3. Re-optimize with lighter touch (target 40-50% instead of 60-75%)
4. Document what content resists compression

---

## Next Steps

1. Execute Session 1 (Module 13 + PROFILE_INDEX)
2. Run validation tests
3. Verify token counts
4. Proceed to Session 2 if validation passes

**Ready to begin?** → Start with Module 13
