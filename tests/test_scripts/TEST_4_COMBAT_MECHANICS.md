# Test 4: Combat Mechanics

**Test ID**: AIDM-TEST-004  
**Category**: Core Functionality  
**Priority**: CRITICAL  
**Estimated Time**: 30-40 minutes

---

## Test Objective

Validate that JRPG-style tactical combat functions correctly with accurate resource tracking, skill validation, and narrative consequences.

**Success Criteria**:
1. HP/MP/SP tracked accurately every turn
2. Skills validate prerequisites (costs, cooldowns, conditions)
3. Damage calculation works correctly
4. Combat resolves with narrative consequences
5. Turn order is logical and consistent

---

## Pre-Test Setup

### Files to Load into LLM

**Required**:
1. `aidm/CORE_AIDM_INSTRUCTIONS.md`
2. All files in `aidm/instructions/` (12 files)
   - **Critical**: `combat_resolution.md`
3. All files in `aidm/schemas/` (7 files)
   - **Critical**: `character_schema.json`
4. `aidm/libraries/common_mechanics/stat_frameworks.md` (HP/MP/SP formulas)
5. `aidm/libraries/common_mechanics/skill_taxonomies.md` (skill costs, cooldowns)

**Optional**:
- `aidm/libraries/power_systems/ki_lifeforce_systems.md` (if testing ki-based combat)
- `aidm/libraries/power_systems/mana_magic_systems.md` (if testing magic combat)

**Platform**: Claude Sonnet 4.5, ChatGPT-4, or equivalent

---

## Test Procedure

### Part 1: Combat Setup (Turns 1-2)

**Turn 1: Quick Character Creation**
```
Player: "Quick combat test setup. I'm a Level 6 warrior named Kael with 80 HP, 40 MP, 60 SP. Skills: Power Strike (20 SP, 3d8 damage), Healing Light (15 MP, heal 2d10), Defend (10 SP, +5 AC for 1 turn). Let's skip Session Zero and jump to combat."
```

**Expected AIDM Response**:
- Creates character with specified stats
- Displays character sheet with HP/MP/SP bars
- Lists all skills with costs
- Confirms ready for combat

**Validation**:
- [ ] Character sheet shows HP: 80/80, MP: 40/40, SP: 60/60
- [ ] All 3 skills listed with correct costs
- [ ] AIDM ready to start combat

---

**Turn 2: Initiate Combat**
```
Player: "I'm ambushed by 2 Orc Warriors (each ~50 HP) in a forest clearing. Roll initiative!"
```

**Expected AIDM Response**:
- Creates 2 Orc Warriors with ~50 HP each
- Rolls initiative for all combatants
- Displays turn order
- Describes combat scene
- Announces first turn

**Example Response**:
```
COMBAT INITIATED!

ENEMIES:
- Orc Warrior #1: HP 50/50
- Orc Warrior #2: HP 50/50

INITIATIVE ORDER:
1. Kael (rolled 18)
2. Orc Warrior #1 (rolled 12)
3. Orc Warrior #2 (rolled 9)

[Scene description: Forest clearing, orcs with crude axes...]

TURN 1 - KAEL'S TURN
HP: 80/80 | MP: 40/40 | SP: 60/60

What do you do?
```

**Validation**:
- [ ] Both orcs created with HP bars
- [ ] Initiative rolled for all
- [ ] Turn order displayed
- [ ] Player's turn announced with resource display

---

### Part 2: Resource Tracking Test (Turns 3-6)

**Turn 3: Use SP Skill**
```
Player: "I use Power Strike on Orc Warrior #1! (20 SP cost)"
```

**Expected AIDM Response**:
- Deducts 20 SP (60 → 40)
- Rolls 3d8 damage
- Applies damage to Orc #1
- Updates Orc #1 HP
- Describes result
- Moves to next turn

**Example**:
```
You channel your strength into Power Strike!

ROLL: 3d8 = 18 damage

Orc Warrior #1 takes 18 damage! (50 → 32 HP)

KAEL: HP 80/80 | MP 40/40 | SP 40/60 (used 20)

TURN 2 - ORC WARRIOR #1'S TURN
[Orc attacks you...]
```

**Validation**:
- [ ] SP correctly deducted (60 → 40)
- [ ] Damage rolled (3d8)
- [ ] Orc HP updated (50 → 32)
- [ ] Resource display shows SP 40/60

---

**Turn 4: Enemy Attack**
```
Player: "I take the orc's attack."
```

**Expected AIDM Response**:
- Orc rolls attack and damage
- Kael's HP reduced appropriately (e.g., ~12-15 damage)
- HP bar updated
- Next turn announced

**Example**:
```
Orc Warrior #1 swings its crude axe!

ATTACK ROLL: 14 (hits AC 13)
DAMAGE: 1d10+3 = 12 damage

Kael takes 12 damage! (80 → 68 HP)

KAEL: HP 68/80 | MP 40/40 | SP 40/60

TURN 3 - ORC WARRIOR #2'S TURN
[Orc #2 attacks...]
```

**Validation**:
- [ ] Kael's HP reduced (~12 damage)
- [ ] HP bar updated (80 → 68)
- [ ] Attack/damage rolled clearly
- [ ] Turn progresses logically

---

**Turn 5: Use MP Skill**
```
Player: "After Orc #2's turn, I use Healing Light on myself. (15 MP cost)"
```

**Expected AIDM Response**:
- Deducts 15 MP (40 → 25)
- Rolls 2d10 healing
- Restores HP (up to max 80)
- Updates HP/MP display
- Describes healing effect

**Example**:
```
You invoke Healing Light, divine energy mending your wounds!

HEAL: 2d10 = 14 HP restored

Kael heals 14 HP! (68 → 80 HP, capped at max)

KAEL: HP 80/80 | MP 25/40 (used 15) | SP 40/60

TURN 5 - KAEL'S TURN
What do you do?
```

**Validation**:
- [ ] MP correctly deducted (40 → 25)
- [ ] Healing rolled (2d10)
- [ ] HP restored but capped at max (80/80)
- [ ] Resource display shows MP 25/40

---

**Turn 6: Use Defend Skill**
```
Player: "I use Defend to boost my AC. (10 SP cost)"
```

**Expected AIDM Response**:
- Deducts 10 SP (40 → 30)
- Applies +5 AC for 1 turn
- Tracks buff duration
- Updates resource display

**Example**:
```
You raise your shield defensively!

Defend activated: +5 AC for this turn (AC 13 → 18)

KAEL: HP 80/80 | MP 25/40 | SP 30/60 (used 10)
ACTIVE BUFFS: Defend (+5 AC, 1 turn remaining)

TURN 6 - ORC WARRIOR #1'S TURN
[Orc attacks, likely misses due to high AC...]
```

**Validation**:
- [ ] SP correctly deducted (40 → 30)
- [ ] Buff applied (+5 AC)
- [ ] Buff duration tracked (1 turn)
- [ ] Next enemy attack likely misses (AC 18)

---

### Part 3: Skill Validation Test (Turns 7-9)

**Turn 7: Insufficient Resources**
```
Player: "I try to use Power Strike again, but I only have 30 SP left. (Power Strike costs 20 SP)"
```

**Expected AIDM Response**:
- Allows Power Strike (30 SP available, 20 needed)
- Deducts 20 SP (30 → 10)
- Executes attack normally

**Then Test Actual Insufficient Resources**:
```
Player: "Can I use Healing Light? I only have 25 MP, it costs 15 MP, so I should have 10 MP left."
```

**Expected**: Should work (25 MP available, 15 needed)

**Then**:
```
Player: "Now try using Healing Light again with only 10 MP left."
```

**Expected AIDM Response**:
- BLOCKS the action (insufficient MP)
- Explains resource shortage
- Asks for alternative action

**Example**:
```
You attempt to invoke Healing Light, but you don't have enough mana!

HEALING LIGHT requires 15 MP, but you only have 10 MP remaining.

Please choose a different action (you can still use Power Strike if you have 20 SP, or Defend if you have 10 SP, or basic attack for free).
```

**Validation**:
- [ ] AIDM tracks resources accurately
- [ ] AIDM prevents actions with insufficient resources
- [ ] AIDM explains why action blocked
- [ ] AIDM suggests valid alternatives

---

**Turn 8: Cooldown Test (if applicable)**

If using a skill with cooldowns:
```
Player: "Let me use my ultimate skill 'Berserker Rage' (50 SP, 3 turn cooldown). Then try to use it again next turn."
```

**Expected AIDM Response - Turn 1**:
- Allows first use (if SP available)
- Applies cooldown (3 turns)
- Tracks cooldown duration

**Expected AIDM Response - Turn 2**:
- BLOCKS second use (on cooldown)
- Shows cooldown remaining (2 turns left)
- Asks for alternative action

**Example**:
```
You attempt Berserker Rage, but the skill is still on cooldown!

BERSERKER RAGE: 2 turns remaining before available again

Please choose a different action.
```

**Validation**:
- [ ] Cooldowns applied correctly
- [ ] Cooldowns tracked per skill
- [ ] Cooldowns prevent re-use
- [ ] Cooldown countdown works (3 → 2 → 1 → 0)

---

### Part 4: Combat Resolution (Turns 10-12)

**Turn 10: Defeat First Orc**
```
Player: "I focus attacks on Orc Warrior #1 until defeated."
```

**Expected AIDM Response**:
- Continues combat turns
- Tracks orc HP reduction
- When orc HP → 0, declares defeat
- Removes orc from initiative order
- Continues with remaining orc

**Example**:
```
Your strike lands true! Orc Warrior #1 takes 20 damage! (12 → 0 HP)

ORC WARRIOR #1 DEFEATED!

Remaining enemies:
- Orc Warrior #2: HP 35/50

TURN 11 - ORC WARRIOR #2'S TURN
```

**Validation**:
- [ ] Enemy defeated when HP → 0
- [ ] Enemy removed from combat
- [ ] Initiative updates (only remaining combatants)
- [ ] Combat continues with survivors

---

**Turn 11-12: Victory & Consequences**
```
Player: "I finish off Orc Warrior #2."
```

**Expected AIDM Response**:
- Continues combat until final orc defeated
- Declares COMBAT VICTORY
- Awards XP
- Shows loot (if any)
- Displays post-combat character state
- **Narrative consequences**: Describes aftermath

**Example**:
```
Your final blow strikes true! Orc Warrior #2 collapses! (15 → 0 HP)

COMBAT VICTORY!

REWARDS:
- XP Gained: 400 (200 per orc)
- Loot: Crude Axe x2, Orc Ears x2, 20 gold

POST-COMBAT STATUS:
KAEL (Level 6): HP 68/80 | MP 10/40 | SP 10/60
XP: [Updated based on starting XP]

[Narrative consequence: You catch your breath after the fierce battle. The orcs were scouts - their war band might be nearby. You notice tracks leading deeper into the forest...]
```

**Validation**:
- [ ] Combat ends when all enemies defeated
- [ ] XP awarded appropriately
- [ ] Loot distributed
- [ ] Post-combat state shown (depleted resources)
- [ ] **Narrative consequences** described (story continues)

---

## Success Determination

### PASS Criteria (All must be true)

1. **Resource Tracking**:
   - HP/MP/SP deducted correctly every turn
   - Resources never go negative
   - Healing capped at maximum values
   - Resource display updates accurately

2. **Skill Validation**:
   - Skills with sufficient resources execute
   - Skills with insufficient resources blocked
   - Cooldowns prevent premature re-use
   - Error messages clear and helpful

3. **Damage Calculation**:
   - Dice rolled for damage/healing (visible)
   - Damage applied to correct target
   - HP updates match damage dealt
   - Attack rolls vs AC work correctly

4. **Combat Flow**:
   - Initiative order logical and consistent
   - Turns progress in order
   - Defeated enemies removed
   - Combat ends when appropriate

5. **Narrative Consequences**:
   - Victory described narratively (not just "You win")
   - Post-combat state affects story (low resources = vulnerability)
   - World reacts to combat outcome (orcs have war band nearby)

### FAIL Criteria (Any triggers failure)

1. ❌ Resources tracked incorrectly (HP/MP/SP wrong)
2. ❌ Skills execute without sufficient resources
3. ❌ Damage calculation broken (wrong amounts)
4. ❌ Combat doesn't end (infinite loop)
5. ❌ No narrative consequences (pure mechanical combat)

### PARTIAL Criteria (Minor issues acceptable)

⚠️ Resource display formatting ugly (but values correct)  
⚠️ Initiative rolls not shown (but order works)  
⚠️ Minor math errors (1-2 HP difference, correctable)  
⚠️ Consequences generic (but present)

---

## Results Template

**Test Execution Date**: ___________  
**LLM Platform**: ___________  
**LLM Version**: ___________

### Resource Tracking
- [ ] HP tracked accurately
- [ ] MP tracked accurately  
- [ ] SP tracked accurately
- [ ] Resources capped at max
- **Tracking Errors**: ___________

### Skill Validation
- [ ] Cost validation works
- [ ] Cooldown validation works
- [ ] Error messages clear
- **Validation Issues**: ___________

### Combat Mechanics
- [ ] Damage rolls work
- [ ] Initiative order correct
- [ ] Turn progression logical
- [ ] Victory conditions work
- **Mechanical Issues**: ___________

### Narrative Integration
- [ ] Combat described narratively
- [ ] Consequences integrated
- [ ] World reacts to outcome
- **Narrative Quality**: ___/10

### Overall Result
- [ ] ✅ PASS
- [ ] ⚠️ PARTIAL PASS
- [ ] ❌ FAIL

**Notes**: ___________

---

## Troubleshooting

### If Test Fails

**Issue**: Resources tracked incorrectly
- **Cause**: combat_resolution.md not loaded or math errors
- **Fix**: Verify combat module loaded; check HP/MP/SP formulas

**Issue**: Skills execute without resources
- **Cause**: Skill validation not implemented
- **Fix**: Check skill_taxonomies.md loaded; verify prerequisite checks

**Issue**: Combat never ends
- **Cause**: Victory condition not checked
- **Fix**: Verify "HP → 0 = defeated" logic works

**Issue**: Pure mechanical combat (no story)
- **Cause**: Narrative integration missing
- **Fix**: Check consequence_integration.md loaded

---

## Test Artifacts to Save

1. **Full combat transcript** (all turns)
2. **Resource tracking table** (HP/MP/SP per turn)
3. **Skill usage log** (which skills used, costs deducted)
4. **Victory screenshot/text** (post-combat state)
5. **Narrative consequences** (exact text)

Store in: `tests/results/test_4_combat_mechanics_[DATE].md`

---

**Test Status**: Ready for execution  
**Next Action**: Load combat module and begin test
