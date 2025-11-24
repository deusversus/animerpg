# Mechanical Meta-Schema Implementation Review & Fix Plan

**Reviewer**: Claude Sonnet 4.5  
**Review Date**: November 23, 2025  
**Implementation By**: Gemini 1.5 Pro  
**Status**: Phase 1 Partially Complete - Fixes Required

---

## Executive Summary

**Overall Assessment**: ✅ **Functional Foundation with Critical Bugs**

Gemini successfully created the core infrastructure for mechanical meta-schemas, but the implementation is **simplified** compared to the original plan and contains **critical bugs** that will break validation. The work represents approximately **40% of Phase 1** completion.

**Recommendation**: **Option A - Fix & Ship MVP** (8 hours) rather than full rebuild (60+ hours)

---

## What Was Completed ✅

### 1. Core Schema Files Created
- `aidm/schemas/economy_meta_schema.json` (28 lines)
- `aidm/schemas/crafting_meta_schema.json` (24 lines)
- `aidm/schemas/progression_meta_schema.json` (31 lines)
- `aidm/schemas/downtime_meta_schema.json` (24 lines)

**Quality**: Simplified but functional. These are validation schemas, not the full meta-schema system with instantiation logic.

### 2. World State Integration
- `world_state_schema.json` updated with `mechanical_systems` field (lines 350-358)
- References all 4 new meta-schemas via `$ref`

**Quality**: Structurally correct, but has reference bug (see Issues).

### 3. State Manager Documentation
- `aidm/instructions/03_state_manager.md` updated with mechanical config tracking
- Shows structure for how profiles will store mechanical configs
- Documents integration with narrative profiles

**Quality**: Well-documented, aligns with design intent.

### 4. Verification Infrastructure
- `tests/test_scripts/verify_mechanical_integration.py` (186 lines)
- Custom JSON schema validator with `$ref` support
- Mock system initialization logic
- `tests/test_data/dummy_profile.md` with example config

**Quality**: Functional test harness, but masks bugs through hardcoded fixes.

---

## Critical Issues 🚨

### Issue #1: Incorrect Schema Reference (BLOCKER)

**Location**: `aidm/schemas/world_state_schema.json` line 354

**Current**:
```json
"mechanical_systems": {
  "type": "object",
  "description": "Configuration and state for game mechanics",
  "properties": {
    "economy": { "$ref": "economy_schema.json" },  // ❌ WRONG FILE
    "crafting": { "$ref": "crafting_meta_schema.json" },
    "progression": { "$ref": "progression_meta_schema.json" },
    "downtime": { "$ref": "downtime_meta_schema.json" }
  }
}
```

**Problem**: References `economy_schema.json` (the existing full economy system with currencies, merchants, market dynamics) instead of `economy_meta_schema.json` (the new configuration schema).

**Impact**: 
- Semantic confusion: mixing full system schema with config schema
- Validation will expect full economy object instead of config
- Breaks the meta-schema architecture design

**Fix**:
```json
"economy": { "$ref": "economy_meta_schema.json" },
```

**Severity**: 🔴 **CRITICAL** - Must fix before any integration

---

### Issue #2: Enum Mismatches (BLOCKER)

**Problem**: Test data uses enum values that don't exist in schemas.

#### 2a. Economy Type Mismatch

**Schema** (`economy_meta_schema.json` line 8):
```json
"enum": ["fiat_currency", "resource_barter", "reputation_based", "post_scarcity", "none", "abstract_wealth"]
```

**Test Data** (`dummy_profile.md`):
```json
"economy": {
  "type": "scarcity_based",  // ❌ NOT IN ENUM
  ...
}
```

**Fix Options**:
- **Option A**: Add "scarcity_based" to enum (if it's a valid economy type)
- **Option B**: Change test data to "resource_barter" or "fiat_currency"

#### 2b. Crafting Type Mismatch

**Schema** (`crafting_meta_schema.json` line 8):
```json
"enum": ["skill_based", "recipe_based", "experimental", "industrial", "none", "ritual_based"]
```

**Verification Script** (line 134):
```python
mechanical_systems["crafting"] = {
    "type": "skill_based",  # ✅ Hardcoded override to fix enum
    ...
}
```

**Issue**: Script manually fixes the mismatch, hiding the problem. Original profile may have used invalid type.

#### 2c. Downtime Type Confusion

**Schema** (`downtime_meta_schema.json`):
- Expects `enabled_modes` array with enum values
- No "type" field defined

**Test Data** (`dummy_profile.md`):
```json
"downtime": {
  "type": "training_arcs",  // ❌ Schema doesn't validate 'type'
  ...
}
```

**Fix**: Test data should use schema structure:
```json
"downtime": {
  "enabled_modes": ["training"],
  "default_mode": "training"
}
```

**Severity**: 🔴 **CRITICAL** - Validation will fail on real profiles

---

### Issue #3: Simplified Schemas vs. Plan Specification (DESIGN DRIFT)

**Original Plan** (`MECHANICAL_META_SCHEMA_IMPLEMENTATION_PLAN.md`):

```json
{
  "schema_id": "meta_economy",
  "version": "1.0",
  "types": {
    "fiat_currency": {
      "description": "Standard currency system with named currency",
      "parameters": {
        "currency_name": { "type": "string", "required": true, "example": "Jenny" },
        "starting_amount": { "type": "number", "default": 200 },
        "scarcity": { "type": "enum", "values": ["abundant", "normal", "scarce"], "default": "normal" },
        ...
      },
      "mechanics": {
        "transactions": "standard_merchant_system",
        "loot_generation": "currency_drops",
        ...
      }
    },
    ...
  }
}
```

**Actual Implementation** (`economy_meta_schema.json`):

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Economy Meta-Schema",
  "type": "object",
  "properties": {
    "type": { "enum": ["fiat_currency", ...] },
    "currency_name": { "type": "string" },
    "starting_amount": { "type": "number" },
    "scarcity": { "enum": ["high", "medium", "low", "none", "variable"] },
    "special_mechanics": { "type": "array", "items": { "type": "string" } }
  },
  "required": ["type", "scarcity"],
  "if": { "properties": { "type": { "const": "fiat_currency" } } },
  "then": { "required": ["currency_name", "starting_amount"] }
}
```

**Gap Analysis**:

| Feature | Plan | Implementation | Status |
|---------|------|----------------|--------|
| Schema Structure | Nested by type | Flat with conditionals | ⚠️ Different approach |
| Parameter Schemas | Per-type definitions | Global properties | ⚠️ Simplified |
| Type Descriptions | Detailed docs per type | Single title/description | ❌ Missing |
| Mechanics Definitions | Explicit per type | Not included | ❌ Missing |
| Examples | Per type | Not included | ❌ Missing |
| Defaults | Specified per param | Not specified | ❌ Missing |
| Instantiation Logic | Documented | Not implemented | ❌ Missing |

**Impact**:
- ✅ **PRO**: Simpler to validate, less verbose
- ❌ **CON**: Missing parameter guidance for profile creators
- ❌ **CON**: No instantiation logic = manual expansion needed
- ❌ **CON**: Less self-documenting than plan specified

**Severity**: 🟡 **MEDIUM** - Functional but incomplete

---

### Issue #4: Verification Script Masks Problems (TESTING ISSUE)

**Location**: `verify_mechanical_integration.py` lines 119-158

**Problem**: Script hardcodes valid values instead of testing actual profile data:

```python
# Line 134: Hardcoded override instead of using config
mechanical_systems["crafting"] = {
    "type": "skill_based",  # ✅ Valid enum
    "categories": ["monster_parts"],
    "special_mechanics": ["harvesting"]
}

# Line 145: Hardcoded override
mechanical_systems["progression"] = {
    "type": "milestone_based",  # ✅ Valid enum
    ...
}
```

**Result**: Test passes even though original config would fail validation.

**Fix**: Either:
1. Test should use actual config values and expect validation errors
2. dummy_profile.md should use valid enum values
3. Add schema enhancement pass to normalize values

**Severity**: 🟡 **MEDIUM** - False positive in testing

---

## Plan Scope Analysis

**Original Plan**: 180 hours over 6 phases
**Current Progress**: ~30 hours (Phase 1 partial)

| Phase | Status | Completion % | Notes |
|-------|--------|--------------|-------|
| **Phase 1: Meta-Schema Design & Creation** | 🟡 Partial | 40% | Files created, bugs present, simplified |
| **Phase 2: Narrative Profile Enhancement** | ⚪ Not Started | 0% | 20 profiles need mechanical configs |
| **Phase 3: Session Zero Integration** | ⚪ Not Started | 0% | Module 06 updates, loading logic |
| **Phase 4: Module Integration** | ⚪ Not Started | 0% | 48 hours of integration work |
| **Phase 5: Testing & Validation** | ⚪ Not Started | 0% | 48 hours of test scenarios |
| **Phase 6: Deployment & Rollout** | ⚪ Not Started | 0% | Documentation, migration |

**Estimated Remaining Work**:
- Fix Critical Issues: 8 hours
- Complete Phase 1: 30 hours (if following original plan detail)
- Phases 2-6: 150 hours

---

## Recommendation: Two-Path Strategy

### Path A: MVP Fix & Ship (RECOMMENDED) ⚡

**Goal**: Fix critical bugs, ship functional system, iterate later

**Effort**: ~8 hours

**Tasks**:

1. **Fix Schema Reference** (30 min)
   - Change `economy_schema.json` → `economy_meta_schema.json` in world_state_schema.json
   - Validate no other reference issues

2. **Align Enums with Reality** (2 hours)
   - Audit what economy/crafting/progression types actually exist in anime profiles
   - Update meta-schema enums to include real-world types
   - Suggested additions:
     - Economy: "scarcity_based", "quest_reward", "found_items"
     - Crafting: "monster_harvesting", "alchemy", "synthesis"
     - Progression: "milestone" (shorthand for milestone_based)
     - Downtime: Keep current structure

3. **Fix Test Data** (1 hour)
   - Update `dummy_profile.md` to match schema structure
   - Create 2-3 more test profiles (different anime types)
   - Remove hardcoded fixes from verification script

4. **Add Conditional Validation** (2 hours)
   - Use JSON Schema `if/then` to enforce required fields per type
   - Example: If economy type = "fiat_currency", require currency_name
   - Test all type combinations

5. **Documentation Pass** (2 hours)
   - Add comments to each schema explaining types
   - Create quick reference guide: "Which type for my anime?"
   - Update Module 03 with integration examples

6. **Validation Test Suite** (30 min)
   - Test valid configs (should pass)
   - Test invalid configs (should fail with clear errors)
   - Test edge cases (empty arrays, missing fields)

**Deliverables**:
- ✅ Bug-free meta-schemas
- ✅ Working validation
- ✅ 3+ test profiles
- ✅ Integration documentation
- ✅ Ready for Phase 2 (profile enhancement)

**Pros**:
- Fast time-to-value
- Unblocks Phase 2 work
- Validates approach before heavy investment
- Can iterate based on real usage

**Cons**:
- Simpler than original vision
- Manual instantiation still needed
- Less guidance for profile creators

---

### Path B: Full Plan Implementation (DEFERRED)

**Goal**: Build complete system as originally specified

**Effort**: ~120 hours (remaining from original 180)

**Tasks**:
- Rebuild meta-schemas with nested type structures
- Add per-type parameter schemas
- Add mechanics definitions
- Build instantiation engine
- Complete Phases 2-6 as planned

**When to Choose This**:
- After MVP validates the approach
- When profile creation becomes a bottleneck
- When instantiation logic is needed for automation
- When 3rd party profile creators need better guidance

**Pros**:
- Matches original architecture vision
- Self-documenting for profile creators
- Automatic config expansion
- Scales to 100+ profiles

**Cons**:
- 3-4 weeks additional work
- Over-engineering risk (YAGNI)
- Delays testing with real profiles
- May need refactoring after user feedback

---

## Immediate Action Plan (Next 8 Hours)

### Fix #1: Schema Reference Bug (30 min)

**File**: `aidm/schemas/world_state_schema.json`

```json
// Line 354: BEFORE
"economy": { "$ref": "economy_schema.json" },

// Line 354: AFTER
"economy": { "$ref": "economy_meta_schema.json" },
```

**Test**: Run verification script, should still pass

---

### Fix #2: Expand Enums (1 hour)

**File**: `aidm/schemas/economy_meta_schema.json`

```json
// Line 8: BEFORE
"enum": ["fiat_currency", "resource_barter", "reputation_based", "post_scarcity", "none", "abstract_wealth"]

// Line 8: AFTER
"enum": [
  "fiat_currency",        // Named currency (Jenny, Berries, etc.)
  "resource_barter",      // Direct trade of goods
  "reputation_based",     // Social credit as currency
  "abstract_wealth",      // Wealth tiers instead of exact amounts
  "scarcity_based",       // Resource scarcity drives economy
  "quest_reward",         // No trading, only quest rewards
  "found_items",          // Loot-based, no currency
  "post_scarcity",        // Unlimited resources
  "none"                  // No economy system
]
```

**File**: `aidm/schemas/crafting_meta_schema.json`

```json
// Line 8: BEFORE
"enum": ["skill_based", "recipe_based", "experimental", "industrial", "none", "ritual_based"]

// Line 8: AFTER
"enum": [
  "skill_based",          // Success based on skill checks
  "recipe_based",         // Fixed recipes with materials
  "experimental",         // Unknown results, discovery
  "monster_harvesting",   // Harvest from defeated enemies
  "alchemy",              // Potion/elixir creation
  "synthesis",            // Combine items to create new ones
  "industrial",           // Large-scale manufacturing
  "ritual_based",         // Ceremonial/magical crafting
  "none"                  // No crafting system
]
```

**File**: `aidm/schemas/progression_meta_schema.json`

```json
// Add "milestone" as alias for "milestone_based"
"enum": ["xp_based", "milestone_based", "milestone", "mastery_tiers", "usage_based", "narrative_unlock", "hybrid"]
```

**Test**: Update dummy_profile.md to use valid enums, verify passes

---

### Fix #3: Fix Downtime Schema Structure (30 min)

**File**: `tests/test_data/dummy_profile.md`

```json
// BEFORE
"downtime": {
  "type": "training_arcs",
  "config": {
    "training_efficiency": 1.0,
    "risk_of_injury": true
  }
}

// AFTER
"downtime": {
  "enabled_modes": ["training", "social"],
  "default_mode": "training",
  "special_mechanics": ["injury_risk", "efficiency_boost"]
}
```

**Test**: Verify validation passes with correct structure

---

### Enhancement #1: Add Schema Comments (1 hour)

**File**: `aidm/schemas/economy_meta_schema.json`

Add `description` fields for each enum value:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Economy Meta-Schema",
  "description": "Defines economic system configuration for anime worlds. Choose the type that best matches your anime's economy.",
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "description": "The primary economic system type:\n- fiat_currency: Named currency (Hunter x Hunter Jenny, One Piece Berries)\n- resource_barter: Direct trade (attack on Titan supplies)\n- scarcity_based: Resource scarcity drives story (Dr. Stone)\n- quest_reward: No trading, only mission rewards (Mission-focused anime)\n- none: No economy system (Death Note, Haikyuu)",
      "enum": [...]
    },
    ...
  }
}
```

Repeat for all 4 meta-schemas.

---

### Enhancement #2: Create Validation Test Suite (2 hours)

**File**: `tests/test_scripts/test_mechanical_validation.py`

```python
"""
Test suite for mechanical meta-schema validation.
Tests valid configs, invalid configs, and edge cases.
"""

import json
from verify_mechanical_integration import simple_validate, load_schema

def test_valid_economy_configs():
    """Test valid economy configurations"""
    schema = load_schema("../../aidm/schemas/economy_meta_schema.json")
    
    # Test 1: Fiat Currency (requires currency_name, starting_amount)
    config = {
        "type": "fiat_currency",
        "currency_name": "Jenny",
        "starting_amount": 200,
        "scarcity": "medium"
    }
    assert simple_validate(config, schema, {})
    
    # Test 2: None (minimal config)
    config = {
        "type": "none",
        "scarcity": "none"
    }
    assert simple_validate(config, schema, {})
    
    print("✅ Valid economy configs passed")

def test_invalid_economy_configs():
    """Test invalid economy configurations should fail"""
    schema = load_schema("../../aidm/schemas/economy_meta_schema.json")
    
    # Test 1: Fiat currency without currency_name
    config = {
        "type": "fiat_currency",
        "scarcity": "medium"
        # Missing currency_name
    }
    assert not simple_validate(config, schema, {})
    
    # Test 2: Invalid enum value
    config = {
        "type": "invalid_type",
        "scarcity": "medium"
    }
    assert not simple_validate(config, schema, {})
    
    print("✅ Invalid economy configs correctly rejected")

# Similar tests for crafting, progression, downtime
```

Run tests before and after fixes to verify improvements.

---

### Enhancement #3: Create Profile Creator Guide (2 hours)

**File**: `dev/MECHANICAL_CONFIG_GUIDE.md`

```markdown
# Mechanical Configuration Guide for Profile Creators

When creating a new narrative profile, add a mechanical configuration section to define gameplay systems.

## Quick Decision Tree

### Economy System
**Question**: How do characters acquire resources?
- Named currency (Jenny, Berries) → `"type": "fiat_currency"`
- Trade goods directly → `"type": "resource_barter"`
- Scarcity is plot point → `"type": "scarcity_based"`
- Find/loot everything → `"type": "found_items"`
- No economy relevant → `"type": "none"`

### Crafting System
**Question**: Can characters create items?
- Build from recipes → `"type": "recipe_based"`
- Harvest from enemies → `"type": "monster_harvesting"`
- Skill-based outcomes → `"type": "skill_based"`
- No crafting → `"type": "none"`

### Progression System
**Question**: How do characters get stronger?
- XP from battles/quests → `"type": "xp_based"`
- Story milestones only → `"type": "milestone_based"`
- Practice skills → `"type": "usage_based"`
- Mastery tiers (Nen, Alchemy) → `"type": "mastery_tiers"`

### Downtime Activities
**Question**: What can characters do between missions?
- Training montages → Include `"training"` in enabled_modes
- Social links/romance → Include `"social"` in enabled_modes
- Research/investigation → Include `"research"` in enabled_modes
- No downtime focus → `"enabled_modes": []`

## Example Configs

### Hunter x Hunter
\`\`\`json
{
  "economy": {
    "type": "fiat_currency",
    "currency_name": "Jenny",
    "starting_amount": 200,
    "scarcity": "medium"
  },
  "crafting": {
    "type": "skill_based",
    "categories": ["Greed Island cards", "Nen abilities"]
  },
  "progression": {
    "type": "mastery_tiers",
    "power_name": "Nen",
    "awakening_stages": ["Initiate", "Practitioner", "Expert", "Master"]
  },
  "downtime": {
    "enabled_modes": ["training", "social"],
    "default_mode": "training"
  }
}
\`\`\`

### Death Note (Minimal Systems)
\`\`\`json
{
  "economy": { "type": "none", "scarcity": "none" },
  "crafting": { "type": "none" },
  "progression": {
    "type": "milestone_based",
    "power_name": "Strategic Thinking",
    "evolution_triggers": ["major_plot_beats"]
  },
  "downtime": {
    "enabled_modes": ["research", "social"],
    "default_mode": "research"
  }
}
\`\`\`
```

---

## Testing Strategy

### Validation Tests (Fix Phase)
1. ✅ All meta-schemas are syntactically valid JSON
2. ✅ world_state_schema.json references correct files
3. ✅ Dummy profile validates successfully
4. ✅ Invalid configs are rejected with clear errors

### Integration Tests (Post-Fix)
1. Load profile with mechanical config → Systems initialize correctly
2. Modify config mid-session → State updates persist
3. Multi-anime fusion → Conflicting configs handled gracefully
4. Missing optional fields → Defaults populate correctly

### User Acceptance Tests (Phase 2)
1. Profile creator can determine correct types in <5 minutes
2. Config validates on first try (no trial-and-error)
3. Session Zero displays mechanical systems clearly
4. Players understand available mechanics from summary

---

## Success Criteria (MVP)

**Before marking Phase 1 complete:**
- [ ] All 4 meta-schemas validate correctly
- [ ] Schema reference bug fixed
- [ ] Enum values match real-world usage
- [ ] 3+ diverse test profiles validate successfully
- [ ] Verification script tests actual profile data (no hardcoding)
- [ ] Documentation explains type selection
- [ ] Clear error messages for validation failures
- [ ] Module 03 updated with integration examples
- [ ] No syntax errors in any JSON file
- [ ] Git committed with clear message

**Definition of Done**:
✅ New narrative profile can be created with mechanical config in <15 minutes  
✅ Config validates on first attempt (no debugging)  
✅ Systems load at Session Zero without errors  
✅ State Manager correctly tracks mechanical systems  
✅ Ready to proceed to Phase 2 (profile enhancement)

---

## Risk Assessment

### Low Risk ✅
- Schema syntax errors → Already validated
- Reference bug → Simple find/replace fix
- Test data alignment → Update dummy profile

### Medium Risk ⚠️
- Enum coverage incomplete → May need iteration after testing with real profiles
- Documentation clarity → User testing needed
- Conditional validation complexity → Edge cases may emerge

### High Risk 🔴
- **None identified** - Architecture is sound, bugs are fixable

### Mitigation Strategies
- Start with 5 diverse anime profiles to validate enum coverage
- User test documentation with fresh profile creator
- Add verbose validation error messages
- Create validation debugging tool

---

## Long-Term Roadmap

### Phase 1.5: MVP Stabilization (Current Focus)
- Fix critical bugs ← **YOU ARE HERE**
- Expand enum coverage
- Add documentation
- **Timeline**: 8 hours

### Phase 2: Profile Enhancement (Next)
- Add mechanical configs to 20 existing profiles
- Test diverse anime types
- Identify missing system types
- **Timeline**: 10 hours

### Phase 3: Session Zero Integration
- Module 06 updates
- System loading at Session Zero
- Player-facing summaries
- **Timeline**: 8 hours

### Phase 4: Module Integration
- Combat uses progression config
- Economy affects merchant behavior
- Crafting action handlers
- Downtime activity menus
- **Timeline**: 30 hours (phased rollout)

### Phase 5: Full Meta-Schema System (Optional Future)
- Rebuild with nested type structures
- Add instantiation engine
- Per-type parameter schemas
- Advanced validation
- **Timeline**: 60 hours
- **Trigger**: After 50+ profiles created, if manual approach becomes bottleneck

---

## Conclusion

**Current State**: 40% of Phase 1 complete, critical bugs present, functional foundation

**Recommended Path**: **Fix & Ship MVP** (8 hours) → Test with real profiles → Iterate

**Next Steps**:
1. Fix schema reference bug (30 min)
2. Expand enums to match reality (1 hour)
3. Add schema documentation (1 hour)
4. Create validation tests (2 hours)
5. Write profile creator guide (2 hours)
6. Test with 3 diverse profiles (1 hour)
7. Update Module 03 examples (30 min)

**Total Effort to Shippable State**: 8 hours

**Blockers**: None - all fixes are straightforward

**Sign-off Required**: Approve MVP path vs. full rebuild path

---

**Gemini's Work Quality**: 7/10
- ✅ Fast execution, good foundation
- ✅ Correct architecture direction
- ⚠️ Simplified vs. plan (not necessarily bad)
- ❌ Critical bugs that need fixing
- ❌ Test suite masks problems

**Overall Verdict**: **Ship the fixes, validate with users, iterate based on real needs.**
