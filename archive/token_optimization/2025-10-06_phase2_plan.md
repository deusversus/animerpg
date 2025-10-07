# Phase 2 Token Optimization - Library Files
**Date**: October 6, 2025  
**Scope**: 12 library files (~27,000 tokens estimated)  
**Goal**: 20-30% reduction (~3,000-4,500 tokens saved) while maintaining reference utility

---

## Library File Analysis

### Total Inventory (12 files)

| Category | File | Lines | Words | Est. Tokens | Priority |
|----------|------|-------|-------|-------------|----------|
| **Common Mechanics** (3 files) | | | | | |
| | skill_taxonomies.md | 591 | 3,165 | ~2,374 | P0 (largest) |
| | stat_frameworks.md | 513 | 2,869 | ~2,152 | P0 |
| | leveling_curves.md | 539 | 2,712 | ~2,034 | P1 |
| **Genre Tropes** (4 files) | | | | | |
| | slice_of_life_tropes.md | 580 | 3,642 | ~2,732 | P0 (largest) |
| | shonen_tropes.md | 473 | 3,113 | ~2,335 | P1 |
| | seinen_tropes.md | 485 | 3,122 | ~2,342 | P1 |
| | isekai_tropes.md | 388 | 2,485 | ~1,864 | P2 |
| **Power Systems** (5 files) | | | | | |
| | power_scaling_narrative.md | 391 | 3,183 | ~2,387 | P0 (largest) |
| | psionic_psychic_systems.md | 449 | 3,134 | ~2,350 | P1 |
| | soul_spirit_systems.md | 401 | 2,674 | ~2,006 | P2 |
| | ki_lifeforce_systems.md | 414 | 2,706 | ~2,030 | P2 |
| | mana_magic_systems.md | 371 | 2,301 | ~1,726 | P2 |
| **TOTALS** | **12 files** | **5,595** | **35,106** | **~26,332** | |

**Current Token Budget**: ~26,332 tokens (13.2% of 200K)  
**Phase 2 Target**: 20-30% reduction = ~5,266-7,900 tokens saved  
**Goal**: Reduce libraries to ~18,400-21,000 tokens (9.2-10.5% of 200K)

---

## Phase 2 Strategy

### Approach

**Conservative Start**: Begin with 2-3 files to validate optimization techniques work for reference content (different from instruction modules).

**Key Differences from Phase 1**:
- Libraries are reference content (not behavioral instructions)
- Must preserve ALL data (examples, mechanics, formulas)
- Focus on formatting/redundancy reduction (not content reduction)
- Users need to quickly scan/search libraries

**Optimization Techniques for Libraries**:
1. **Header Consolidation**: Multi-line metadata → single line
2. **Table Compression**: Verbose tables → compact format
3. **Example Reduction**: Keep best examples, remove redundant ones
4. **List Compression**: Bullet verbosity → compact format
5. **Section Merging**: Related subsections → unified sections
6. **Formatting Simplification**: Reduce whitespace, code blocks, dividers

### Phase 2 P0 - Conservative Batch (Validate Approach)

**Files**: 3 largest files, one from each category  
**Target**: 20% reduction (~1,370 tokens saved)

| File | Current | Target (20%) | Techniques |
|------|---------|-------------|------------|
| slice_of_life_tropes.md | ~2,732 | ~2,186 | Example reduction, table compression |
| skill_taxonomies.md | ~2,374 | ~1,899 | List compression, header consolidation |
| power_scaling_narrative.md | ~2,387 | ~1,910 | Format simplification, section merging |
| **P0 TOTALS** | **~7,493** | **~5,995** | **~1,498 saved** |

**Validation**: After P0, verify:
- ✅ Reference utility maintained (easy to scan/search)
- ✅ All mechanical data preserved (formulas, examples)
- ✅ Information parity at 100%
- ✅ Performance meets/exceeds 20% target

**Decision Point**: If P0 successful → Continue to P1/P2. If issues → adjust technique.

---

## Conservative Batch Execution Plan

### File 1: slice_of_life_tropes.md (~2,732 tokens)

**Current Issues** (preliminary scan):
- Verbose romance structures (likely 200+ words per type)
- Detailed event descriptions (repetitive patterns)
- Multiple examples for same concept
- Extensive character archetype lists

**Optimization Targets**:
- Romance structures: Compress to compact format
- Event descriptions: Streamline to essentials
- Examples: Keep 1-2 best, remove rest
- Archetypes: Table format instead of verbose bullets

**Estimated Savings**: ~546 tokens (20% of 2,732)

---

### File 2: skill_taxonomies.md (~2,374 tokens)

**Current Issues** (preliminary scan):
- Detailed skill category descriptions
- Extensive mastery level explanations
- Multiple anime examples per skill type
- Verbose balance guidelines

**Optimization Targets**:
- Skill categories: Compact list format
- Mastery levels: Formula/table compression
- Examples: Reduce to iconic representatives only
- Balance: Streamline formulas to essentials

**Estimated Savings**: ~475 tokens (20% of 2,374)

---

### File 3: power_scaling_narrative.md (~2,387 tokens)

**Current Issues** (preliminary scan):
- Detailed tier descriptions (5 tiers)
- Extensive ensemble cast pivot explanations
- Multiple character examples per tier
- Verbose growth model comparisons

**Optimization Targets**:
- Tier descriptions: Compact format
- Ensemble pivot: Streamline protocol
- Examples: Iconic characters only (Saitama, Ainz, etc.)
- Growth models: Table comparison vs verbose

**Estimated Savings**: ~477 tokens (20% of 2,387)

---

## Success Criteria

### Technical Metrics
- ✅ 20%+ reduction achieved (~1,498+ tokens)
- ✅ 100% information parity (all mechanics preserved)
- ✅ All formulas/tables/examples intact (no data loss)

### Usability Metrics
- ✅ Libraries remain easy to scan
- ✅ Examples still illustrate concepts clearly
- ✅ No loss of reference utility

### Process Metrics
- ✅ Same optimization time as Phase 1 (~1-2 hours for 3 files)
- ✅ No new issues introduced
- ✅ Validation confirms equivalence

---

## Next Steps

1. **Read slice_of_life_tropes.md** - Full file review
2. **Optimize conservatively** - Apply techniques
3. **Verify word count** - Confirm 20% reduction
4. **Repeat for files 2-3** - skill_taxonomies, power_scaling_narrative
5. **Validate batch** - Quick scan for data loss
6. **Commit P0** - Git checkpoint
7. **User review** - Confirm approach before P1/P2

---

**Phase 2 P0 Ready to Execute** ✅
