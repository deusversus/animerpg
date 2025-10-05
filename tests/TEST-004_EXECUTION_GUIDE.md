# TEST-004 Execution Guide: Combat Mechanics

**Test Date**: October 4, 2025  
**Status**: 🔄 READY TO EXECUTE  
**Tester**: AIDM Development Team  
**Priority**: CRITICAL (Phase 1 - Core Functionality)

---

## Quick Start Instructions

### Step 1: Prepare Fresh LLM Session

⚠️ **CRITICAL**: Open a **completely new LLM conversation**

**Recommended Platforms**:
- Claude Sonnet 4.5 (preferred)
- ChatGPT-4o (acceptable)

---

### Step 2: Load AIDM Files

**Core Files** (21 files - updated from TEST-001):
```
📁 aidm/CORE_AIDM_INSTRUCTIONS.md
📁 aidm/instructions/00-12 (all 13 instruction files)
📁 aidm/schemas/ (all 7 schema files)
```

**Additional for Combat Test**:
```
📁 aidm/libraries/common_mechanics/stat_frameworks.md (HP/MP/SP formulas)
📁 aidm/libraries/common_mechanics/skill_taxonomies.md (skill costs, cooldowns)
```

**Total Files**: 23 files

---

### Step 3: System Initialization

Send this after loading all files:
```
System initialized. AIDM v2.0 ready with combat module loaded.

Awaiting player input for combat test.
```

---

## TEST-004 Execution Script

### Turn 1: Quick Character Creation

**Player Input**:
```
Quick combat test setup. I'm a Level 6 warrior named Kael with 80 HP, 40 MP, 60 SP. Skills: Power Strike (20 SP, 3d8 damage), Healing Light (15 MP, heal 2d10), Defend (10 SP, +5 AC for 1 turn). Let's skip Session Zero and jump to combat.
```

**Watch For**:
- [ ] Character sheet displays HP: 80/80, MP: 40/40, SP: 60/60
- [ ] All 3 skills listed with costs
- [ ] AIDM confirms ready for combat

---

### Turn 2: Initiate Combat

**Player Input**:
```
I'm ambushed by 2 Orc Warriors (each ~50 HP) in a forest clearing. Roll initiative!
```

**Watch For**:
- [ ] 2 Orc Warriors created (HP 50/50 each)
- [ ] Initiative rolled for all combatants
- [ ] Turn order displayed (Kael, Orc #1, Orc #2 or similar)
- [ ] First turn announced with resource display

---

### Turn 3: Use SP Skill (Power Strike)

**Player Input**:
```
I use Power Strike on Orc Warrior #1! (20 SP cost)
```

**Watch For**:
- [ ] SP deducted: 60 → 40 ✅
- [ ] Damage rolled: 3d8 (should show dice result)
- [ ] Orc #1 HP reduced appropriately (e.g., 50 → 32)
- [ ] Resource display shows SP 40/60

**Critical**: SP MUST go from 60 to 40 (exactly 20 deducted)

---

### Turn 4-5: Enemy Attacks & MP Skill

**Turn 4 - Let Orcs Attack**:
```
I take the orc's attacks.
```

**Watch For**:
- [ ] Kael's HP reduced (e.g., 80 → 68 after ~12 damage)
- [ ] Attack rolls shown
- [ ] HP bar updates correctly

**Turn 5 - Use Healing Light**:
```
After the orcs' turns, I use Healing Light on myself. (15 MP cost)
```

**Watch For**:
- [ ] MP deducted: 40 → 25 ✅
- [ ] Healing rolled: 2d10 (should show dice result)
- [ ] HP restored but capped at max 80
- [ ] Resource display shows MP 25/40

**Critical**: MP MUST go from 40 to 25 (exactly 15 deducted)

---

### Turn 6: Use Defend Skill

**Player Input**:
```
I use Defend to boost my AC. (10 SP cost)
```

**Watch For**:
- [ ] SP deducted: 30 → 20 (or current SP - 10)
- [ ] +5 AC buff applied
- [ ] Buff duration tracked (1 turn)
- [ ] Next enemy attack likely misses (high AC)

---

### Turn 7-8: Resource Validation Test

**Turn 7a - Use Power Strike (should work)**:
```
I use Power Strike again. I have 20 SP, it costs 20 SP, so I should end at 0 SP.
```

**Watch For**:
- [ ] Allowed (20 SP available, 20 needed) ✅
- [ ] SP goes to 0/60

**Turn 7b - Use Healing Light (should work)**:
```
I use Healing Light. I have 25 MP, it costs 15 MP, so I should have 10 MP left.
```

**Watch For**:
- [ ] Allowed (25 MP available, 15 needed) ✅
- [ ] MP goes to 10/40

**Turn 8 - Try Healing Light Again (SHOULD FAIL)**:
```
I try to use Healing Light again. I only have 10 MP left, but it costs 15 MP.
```

**Watch For**:
- [ ] ❌ **BLOCKED** (insufficient MP) ✅ CRITICAL
- [ ] Error message: "Not enough MP" or similar
- [ ] Suggests alternative actions
- [ ] Does NOT execute skill

**Critical Test**: AIDM MUST block this action. If it allows Healing Light with only 10 MP, test **FAILS**.

---

### Turn 9-12: Combat Resolution

**Continue Combat**:
```
I attack the orcs with basic attacks until both are defeated.
```

**Watch For**:
- [ ] Orcs defeated when HP → 0
- [ ] Defeated orcs removed from initiative
- [ ] Combat ends when all enemies defeated
- [ ] COMBAT VICTORY declared

**Victory Screen**:
- [ ] XP awarded (e.g., 400 XP total)
- [ ] Loot shown (crude axes, gold, etc.)
- [ ] Post-combat status: HP/MP/SP displayed (likely depleted)
- [ ] **Narrative consequences**: Story continues (orcs were scouts, war band nearby, etc.)

**Critical**: Combat must have **narrative impact**, not just "You win."

---

## Validation Checklist

### ✅ PASS Criteria (All Must Be True)

**Resource Tracking**:
- [ ] HP/MP/SP deducted correctly every turn
- [ ] Resources never go negative
- [ ] Healing capped at max (HP can't exceed 80)
- [ ] Resource display accurate (shows current/max)

**Skill Validation**:
- [ ] Skills with sufficient resources execute normally
- [ ] ❌ Skills with insufficient resources **BLOCKED** (CRITICAL)
- [ ] Error messages clear ("Not enough MP")
- [ ] Cooldowns tracked (if tested)

**Damage Calculation**:
- [ ] Dice rolls shown (3d8, 2d10, etc.)
- [ ] Damage applied to correct target
- [ ] HP updates match damage dealt
- [ ] Attack rolls vs AC work

**Combat Flow**:
- [ ] Initiative order logical
- [ ] Turns progress in order
- [ ] Defeated enemies removed
- [ ] Combat ends appropriately

**Narrative Integration**:
- [ ] Combat described with story (not pure mechanics)
- [ ] Victory has consequences (orcs were scouts, etc.)
- [ ] Post-combat state affects narrative (low resources = vulnerability)

### ❌ FAIL Criteria (Any Triggers FAIL)

- [ ] Resources tracked wrong (HP/MP/SP incorrect)
- [ ] ❌ **Skills execute without resources** (CRITICAL FAILURE)
- [ ] Damage calculation broken
- [ ] Combat infinite loop (never ends)
- [ ] No narrative consequences (pure mechanics)

### ⚠️ PARTIAL Criteria (Minor Issues)

- [ ] Resource display ugly but correct
- [ ] Initiative rolls not shown but order works
- [ ] Minor math errors (1-2 HP off, correctable)
- [ ] Generic consequences (but present)

---

## Critical Test Points

### 🔴 **CRITICAL VALIDATION** (Must Pass)

**Turn 8: Insufficient Resources Test**

When player tries to use Healing Light with only 10 MP (needs 15 MP):

**✅ CORRECT RESPONSE**:
```
You attempt to invoke Healing Light, but you don't have enough mana!

HEALING LIGHT requires 15 MP, but you only have 10 MP remaining.

Please choose a different action.
```

**❌ INCORRECT RESPONSE** (TEST FAILS):
```
You invoke Healing Light! [proceeds to execute skill despite insufficient MP]
```

**If AIDM allows skill with insufficient resources, mark TEST-004 as FAIL.**

---

## Troubleshooting

### Issue: Resources not tracked
- **Cause**: Combat module not loaded
- **Fix**: Verify `aidm/instructions/08_combat_resolution.md` loaded

### Issue: Skills execute without resources
- **Cause**: Validation not implemented
- **Fix**: Check `skill_taxonomies.md` loaded
- **If persists**: **CRITICAL BUG** - mark test FAIL

### Issue: Combat never ends
- **Cause**: Victory condition broken
- **Fix**: Manually declare "Both orcs are defeated" and see if AIDM awards XP

### Issue: No narrative consequences
- **Cause**: Narrative integration missing
- **Fix**: Acceptable for combat test, note in results

---

## Results Documentation

**Save to**: `tests/results/test_4_combat_mechanics_2025-10-04.md`

**Include**:
1. Full combat transcript (all turns)
2. Resource tracking table:
   ```
   Turn | HP    | MP    | SP    | Notes
   -----|-------|-------|-------|-------
   1    | 80/80 | 40/40 | 60/60 | Start
   2    | 80/80 | 40/40 | 60/60 | Combat begins
   3    | 80/80 | 40/40 | 40/60 | Power Strike used
   ...
   ```
3. Skill validation results (did insufficient resource blocking work?)
4. Victory screen (XP, loot, consequences)
5. Overall PASS/PARTIAL/FAIL verdict

---

## Expected Timeline

**Total Test Duration**: 30-40 minutes
- Setup: 5-10 minutes (load files)
- Combat execution: 15-20 minutes (12 turns)
- Documentation: 5-10 minutes

---

**Test Status**: ✅ Ready to Execute  
**Confidence Level**: HIGH (based on TEST-001 success)  
**Next Action**: Open fresh LLM session and begin

---

## Quick Command Reference

**Character Setup**:
```
Quick combat test setup. I'm a Level 6 warrior named Kael with 80 HP, 40 MP, 60 SP. Skills: Power Strike (20 SP, 3d8 damage), Healing Light (15 MP, heal 2d10), Defend (10 SP, +5 AC for 1 turn). Let's skip Session Zero and jump to combat.
```

**Combat Start**:
```
I'm ambushed by 2 Orc Warriors (each ~50 HP) in a forest clearing. Roll initiative!
```

**Critical Test**:
```
I try to use Healing Light again. I only have 10 MP left, but it costs 15 MP.
```

**Expected Block**: "You don't have enough mana!" (MUST block action)

