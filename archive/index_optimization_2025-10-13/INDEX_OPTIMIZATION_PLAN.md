# INDEX FILES OPTIMIZATION PLAN

**Date**: October 13, 2025
**Target Files**: PROFILE_INDEX.md, GENRE_TROPES_INDEX.md
**Methodology**: →OPTIMIZATION_CHECKLIST.md, →docs/TOKEN_OPTIMIZATION_METHODOLOGY.md

---

## Baseline Measurements

### Current State
- **PROFILE_INDEX.md**: 3,893 words → ~10,628 tokens
- **GENRE_TROPES_INDEX.md**: 2,305 words → ~6,293 tokens
- **Total**: 6,198 words → ~16,921 tokens

### Target Reductions (Library File Category)
- **Conservative**: 40-50% reduction → ~10,153 tokens
- **Aggressive**: 60-70% reduction → ~5,076 tokens
- **Target**: 60% reduction → **~6,768 tokens** (save ~10,153 tokens)

---

## Optimization Strategy

### Pass 1: Structural (Target: 35-40% reduction)

**PROFILE_INDEX.md**:
- [ ] Header consolidation: `**Library Version**: 2.0` + 3 more lines → `| v2.0 | Updated:2025-10-13 | 20 Profiles | →path`
- [ ] Remove emoji: None present (already using text)
- [ ] Compress profile listings: `**Hunter x Hunter** (\`narrative_hxh\`) [CORE]: Long description | *Best for*: Details` → `**HxH** (\`narrative_hxh\`) [CORE]: Tactical:10/10, Nen, strategic | *Best*: Strategy wins`
- [ ] Inline genre sections: Reduce whitespace between sections
- [ ] Cross-reference matrix: Table format → inline `"Tactical→HxH | JJK, Code Geass"`

**GENRE_TROPES_INDEX.md**:
- [ ] Similar header consolidation
- [ ] Compress trope descriptions (15 entries × verbose descriptions)
- [ ] Auto-load trigger table: Already compact, minor tweaks
- [ ] Blending guidelines: Prose → structured data

**Estimated Pass 1 Result**: ~3,720 words (~10,156 tokens) - **40% reduction**

---

### Pass 2: Content (Target: 55-60% reduction)

**PROFILE_INDEX.md**:
- [ ] Scale 11 POV Distribution section: **MASSIVE SECTION** (~1,500 words alone)
  - Compress level descriptions: `**1/10: Solo Protagonist** | 80-95% POV single | Ex: Death Note (Light 90%) | *Use*: Solo campaigns, psych horror | *Pitfall*: Spotlight hogging`
  - Progression models: Reduce from full paragraphs to compact examples
  - Session Zero questions: List format → inline `Q1: Solo or shared? (Solo=1-3 | Balanced=4-6 | Ensemble=7-11)`
  - Common Mistakes: Reduce from paragraphs to `Mistake→Cause→Fix` inline format
  - AIDM Guidance: Compress from detailed prose to checklist format

- [ ] Blending Profiles section: Examples verbose → compact
- [ ] Quick Start Workflows: 4 examples with line breaks → compact inline format
- [ ] Appendix file structure: Already compact, minor tweaks

**GENRE_TROPES_INDEX.md**:
- [ ] Genre Tropes Library (15 entries): Each entry ~150 words → ~50 words
  - Core Patterns: Bullet lists → inline pipes
  - Arc Templates: Verbose → abbreviated
  - Character Archetypes: Full descriptions → compact references
  - Best For: Already short, keep
  - Auto-Loaded By: Keep as-is

- [ ] Usage Patterns (4 types): Paragraphs → single line each
- [ ] Blending Tropes: Compatible/incompatible lists → inline format
- [ ] Integration with Module 13: Reduce explanation prose

**Estimated Pass 2 Result**: ~2,475 words (~6,757 tokens) - **60% reduction ✓**

---

### Pass 3: Refinement (Target: 65-70% reduction if possible)

**Both Files**:
- [ ] Merge related subsections (eliminate intermediate headers)
- [ ] Eliminate excess whitespace (max 1 blank line between sections)
- [ ] Shorten all cross-references: `aidm/libraries/narrative_profiles/` → `→profiles/`
- [ ] Final polish: Review every line for additional compression

**Conservative Target Pass 3**: ~2,163 words (~5,905 tokens) - **65% reduction**
**Aggressive Target Pass 3**: ~1,860 words (~5,076 tokens) - **70% reduction**

---

## Validation Protocol

### Dry Tests (CRITICAL - Must PASS 100%)

**PROFILE_INDEX.md Tests**:
```powershell
# Test 1: Verify all 20 profiles listed
grep -i "hunter_x_hunter|jujutsu_kaisen|demon_slayer|attack_on_titan|code_geass|death_note|konosuba|mushishi|rezero|vinland_saga|haikyuu|dandadan|naruto|mha|one_piece|cowboy_bebop|fmab|nge|opm|steins" PROFILE_INDEX.md

# Test 2: Verify cross-reference matrix entries
grep -i "tactical.*hxh|dark.*aot|comedy.*konosuba|mind.*death.*note" PROFILE_INDEX.md

# Test 3: Verify Scale 11 levels present
grep -i "1/10.*solo|5/10.*balanced|7/10.*dual|11/10.*peak.*ensemble" PROFILE_INDEX.md

# Test 4: Verify all profile IDs
grep -i "narrative_hxh|narrative_jjk|narrative_aot|narrative_konosuba" PROFILE_INDEX.md

# Test 5: Verify blending examples
grep -i "tactical dark fantasy|comedic isekai|psychological horror isekai" PROFILE_INDEX.md
```

**GENRE_TROPES_INDEX.md Tests**:
```powershell
# Test 1: Verify all 15 trope libraries listed
grep -i "shonen|seinen|mystery_thriller|horror|supernatural|comedy|slice_of_life|isekai|shoujo_romance|mecha|scifi|magical_girl|historical|sports|music" GENRE_TROPES_INDEX.md

# Test 2: Verify auto-load triggers
grep -i "spy.*mystery_thriller|detective.*mystery|horror.*horror.*mystery|tournament.*shonen" GENRE_TROPES_INDEX.md

# Test 3: Verify blending compatibility
grep -i "compatible|incompatible|mystery_thriller.*supernatural" GENRE_TROPES_INDEX.md

# Test 4: Verify usage patterns
grep -i "campaign type determines|profile.*tropes.*complete|multiple tropes.*hybrid" GENRE_TROPES_INDEX.md

# Test 5: Verify Module 13 integration
grep -i "module 13|narrative calibration|auto-load" GENRE_TROPES_INDEX.md
```

### Information Parity Check
```powershell
# Compare optimized vs backup
git diff aidm/libraries/narrative_profiles/PROFILE_INDEX_BACKUP.md aidm/libraries/narrative_profiles/PROFILE_INDEX.md

git diff aidm/libraries/genre_tropes/GENRE_TROPES_INDEX_BACKUP.md aidm/libraries/genre_tropes/GENRE_TROPES_INDEX.md
```

**Checklist**:
- [ ] All 20 profiles present (12 CORE + 8 Extended)
- [ ] All Scale 11 levels documented (1/10 → 11/10)
- [ ] All cross-reference matrix entries intact
- [ ] All blending examples present
- [ ] All 15 genre trope libraries present
- [ ] All 12 auto-load triggers documented
- [ ] Blending guidelines (compatible/incompatible) present
- [ ] Module 13 integration notes intact

---

## Implementation Schedule

### Immediate (High Priority)
1. **PROFILE_INDEX.md Pass 1** (Structural) - Est: 2 hours
   - Focus: Scale 11 POV section compression (largest target)
   - Checkpoint: ~40% reduction → 3,720 words

2. **PROFILE_INDEX.md Pass 2** (Content) - Est: 3 hours
   - Focus: POV level descriptions, Session Zero questions, workflows
   - Checkpoint: ~60% reduction → 2,475 words → **PRIMARY TARGET**

3. **Validation** (PROFILE_INDEX.md) - Est: 1 hour
   - Run all 5 dry tests
   - Information parity check
   - Decision: If 100% parity → commit. If <100% → adjust.

### Secondary (Medium Priority)
4. **GENRE_TROPES_INDEX.md Pass 1** (Structural) - Est: 1.5 hours
   - Focus: 15 trope library descriptions
   - Checkpoint: ~40% reduction → 1,383 words

5. **GENRE_TROPES_INDEX.md Pass 2** (Content) - Est: 2 hours
   - Focus: Core patterns, arc templates, usage patterns
   - Checkpoint: ~60% reduction → 922 words → **PRIMARY TARGET**

6. **Validation** (GENRE_TROPES_INDEX.md) - Est: 30 min
   - Run all 5 dry tests
   - Information parity check
   - Decision: Commit or adjust

### Optional (If Time Permits)
7. **Pass 3 Refinement** (Both Files) - Est: 2 hours
   - Push to 65-70% reduction if possible
   - Final polish
   - Re-validation

---

## Key Compression Targets

### PROFILE_INDEX.md Hotspots (Biggest Savings)

**1. Scale 11 POV Distribution Section** (~1,500 words → ~450 words)
- 11 level descriptions (verbose paragraphs → compact single lines)
- Progression models (multiple examples → 2 key examples)
- Session Zero questions (5 Q&A blocks → inline format)
- Common Mistakes (5 mistake blocks → compact list)
- AIDM Guidance (3 prose sections → checklist)
**Potential**: ~1,050 words saved (~2,867 tokens)

**2. Profile Listings by Genre** (~800 words → ~400 words)
- Compress each profile description (remove redundancy)
- Abbreviate anime names where recognizable (Hunter x Hunter → HxH)
- *Best for* sections already compact
**Potential**: ~400 words saved (~1,092 tokens)

**3. Cross-Reference Matrix** (~300 words → ~150 words)
- Already inline format, minimal compression
- Remove "→Recommend" verbose format
**Potential**: ~150 words saved (~410 tokens)

**4. Blending Profiles** (~200 words → ~100 words)
- Examples already compact
- Guidelines prose → structured format
**Potential**: ~100 words saved (~273 tokens)

**Total Aggressive Target**: ~1,700 words saved (~4,642 tokens) = **65% reduction**

### GENRE_TROPES_INDEX.md Hotspots

**1. Genre Tropes Library (15 entries)** (~900 words → ~450 words)
- Core Patterns: Lists → inline pipes
- Arc Templates: Verbose → compact
- Character Archetypes: Full → abbreviated
**Potential**: ~450 words saved (~1,229 tokens)

**2. Usage Patterns** (~400 words → ~150 words)
- 4 patterns with examples → compact inline
**Potential**: ~250 words saved (~683 tokens)

**3. Blending Tropes** (~300 words → ~150 words)
- Compatible/incompatible examples → inline lists
**Potential**: ~150 words saved (~410 tokens)

**4. Integration with Module 13** (~200 words → ~100 words)
- Explanatory prose → structured data
**Potential**: ~100 words saved (~273 tokens)

**Total Aggressive Target**: ~950 words saved (~2,595 tokens) = **60% reduction**

---

## Expected Outcomes

### After Pass 2 (Primary Target)
- **PROFILE_INDEX.md**: 3,893 → 1,557 words (~4,251 tokens) - **60% reduction**
- **GENRE_TROPES_INDEX.md**: 2,305 → 922 words (~2,517 tokens) - **60% reduction**
- **Combined**: 6,198 → 2,479 words (~6,768 tokens) - **60% reduction**
- **Tokens Saved**: ~10,153 tokens

### After Pass 3 (Stretch Goal)
- **PROFILE_INDEX.md**: 3,893 → 1,362 words (~3,718 tokens) - **65% reduction**
- **GENRE_TROPES_INDEX.md**: 2,305 → 807 words (~2,203 tokens) - **65% reduction**
- **Combined**: 6,198 → 2,169 words (~5,921 tokens) - **65% reduction**
- **Tokens Saved**: ~11,000 tokens

### Impact on System
**Current Active Load** (from Opus test):
- Tier 1: ~12,400 tokens
- Tier 2 (Session Zero): ~16,700 tokens
- **Index files**: ~16,921 tokens (NOT loaded during gameplay, only Session Zero)

**After Optimization**:
- Tier 1: ~12,400 tokens (unchanged)
- Tier 2 (Session Zero): ~16,700 tokens (unchanged)
- **Index files**: ~6,768 tokens (**saved ~10,153 tokens during Session Zero**)

**Session Zero Total**: 29,100 → 18,947 tokens (**35% reduction in Session Zero load**)

---

## Red Flags & Precision Hold

### Don't Compress If:
- Profile ID references become ambiguous (`narrative_hxh` → keep full)
- Cross-reference matrix entries lose clarity
- Scale 11 level distinctions blur (need clear 1/10 vs 5/10 vs 11/10)
- Auto-load triggers become unclear (detective→mystery_thriller must be explicit)
- Blending compatibility contradictions hidden

### Precision Hold Scenarios:
- **Profile IDs**: Keep full format (`narrative_hunter_x_hunter` too long, `narrative_hxh` optimal)
- **Scale 11 Table**: Already compact, minimal further compression
- **Auto-Load Trigger Table**: Already optimal, don't compress
- **File Structure Appendix**: Minimal compression (needed for navigation)

### Rule:
If compressing Scale 11 drops clarity below 90% → STOP at 55% reduction instead of 60%

---

## Post-Optimization Checklist

- [ ] All dry tests PASS (100% required)
- [ ] Information parity check vs backup (100% required)
- [ ] Word count meets target (60% minimum)
- [ ] Token estimate calculated (words × 2.73)
- [ ] Commit with descriptive message
- [ ] Delete backup files (after confirming commit)
- [ ] Update this plan with actual results

---

## Actual Results (Post-Implementation)

*[To be filled after optimization complete]*

**PROFILE_INDEX.md**:
- Baseline: 3,893 words (~10,628 tokens)
- After Pass 1: ___ words (___ tokens) - ___% reduction
- After Pass 2: ___ words (___ tokens) - ___% reduction
- After Pass 3: ___ words (___ tokens) - ___% reduction
- Final: ___ words (___ tokens) - ___% reduction
- Validation: [PASS/FAIL] - ___/5 dry tests passed

**GENRE_TROPES_INDEX.md**:
- Baseline: 2,305 words (~6,293 tokens)
- After Pass 1: ___ words (___ tokens) - ___% reduction
- After Pass 2: ___ words (___ tokens) - ___% reduction
- After Pass 3: ___ words (___ tokens) - ___% reduction
- Final: ___ words (___ tokens) - ___% reduction
- Validation: [PASS/FAIL] - ___/5 dry tests passed

**Combined**:
- Baseline: 6,198 words (~16,921 tokens)
- Final: ___ words (___ tokens) - ___% reduction
- Tokens Saved: ___ tokens
- Information Parity: [100%/PARTIAL] - Notes: ___

---

**Status**: [!] PLAN COMPLETE - READY FOR IMPLEMENTATION
**Priority**: HIGH (Index files loaded during Session Zero, optimization reduces initial context load)
**Est. Time**: 6-8 hours total (both files, all passes + validation)
**Next Step**: Begin Pass 1 on PROFILE_INDEX.md (Scale 11 section compression)
