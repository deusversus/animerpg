# Test 4: Combat Mechanics

**Test ID**: AIDM-TEST-004  
**Category**: Core Functionality  
**Priority**: CRITICAL  
**Estimated Time**: 30-40 minutes

---

## Test Objective

Validate that JRPG-style tactical combat functions correctly with accurate resource tracking, skill validation, narrative consequences, AND progression-type-specific XP calculation (Phase 4 integration).

**Success Criteria**:
1. HP/MP/SP tracked accurately every turn
2. Skills validate prerequisites (costs, cooldowns, conditions)
3. Damage calculation works correctly
4. Combat resolves with narrative consequences
5. Turn order is logical and consistent
6. **NEW**: XP calculation varies by progression type (5 different formulas)
7. **NEW**: Tier bonuses apply in combat (mastery_tiers)
8. **NEW**: Awakening triggers detected (quirk_awakening)

---

## Pre-Test Setup

### Files to Load into LLM

**Required**:
1. `aidm/CORE_AIDM_INSTRUCTIONS.md`
2. All files in `aidm/instructions/` (14 files)
   - **Critical**: `08_combat_resolution.md` (includes Phase 4 progression integration)
   - **Critical**: `09_progression_systems.md` (leveling mechanics)
3. All files in `aidm/schemas/` (15+ files)
   - **Critical**: `character_schema.json` (v2.3.0, includes tier_xp, awakening_stage)
   - **Meta-schemas**: `progression_meta_schema.json` (5 progression types)
4. `aidm/lib/mechanical_instantiation.py` (Python utility)
5. `aidm/libraries/common_mechanics/stat_frameworks.md` (HP/MP/SP formulas)
6. `aidm/libraries/common_mechanics/skill_taxonomies.md` (skill costs, cooldowns)

**Optional**:
- `aidm/libraries/power_systems/ki_lifeforce_systems.md` (if testing ki-based combat)
- `aidm/libraries/power_systems/mana_magic_systems.md` (if testing magic combat)
- `aidm/libraries/narrative_profiles/hunter_x_hunter.md` (mastery_tiers example)
- `aidm/libraries/narrative_profiles/my_hero_academia.md` (quirk_awakening example)

**Platform**: Claude Sonnet 4.5, ChatGPT-4, or equivalent

---

## Test Structure

This test is divided into **TWO PARTS**:

**PART A**: Core Combat Mechanics (resource tracking, skill validation, combat resolution)
- Uses generic "class_based" progression (standard XP calculation)
- Validates fundamental combat system works
- **Duration**: 30-40 minutes

**PART B**: Progression-Type Combat Integration (Phase 4 validation)
- Tests 5 different progression types with distinct XP formulas
- Validates Module 08 reads from session_state.mechanical_systems
- Validates progression-specific combat features (tier bonuses, awakening triggers, zero XP)
- **Duration**: 60-90 minutes (5 scenarios × 10-15 minutes each)

**Total Test Duration**: 90-130 minutes

---

# PART A: CORE COMBAT MECHANICS

## Pre-Test Setup

### Files to Load into LLM

(See "Pre-Test Setup" section above)

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

# PART B: PROGRESSION-TYPE COMBAT INTEGRATION (Phase 4)

## Objective

Validate that Module 08 Combat Resolution correctly reads `session_state.mechanical_systems.progression.type` and applies progression-specific XP formulas, tier bonuses, awakening triggers, and zero-XP enforcement.

**Duration**: 60-90 minutes (5 scenarios)

---

## Scenario B1: mastery_tiers (Hunter x Hunter)

### Setup
Create character with **mastery_tiers** progression type.

```
Player: "Quick setup: I'm Gon, a Hunter x Hunter character with mastery_tiers progression. Current tier: Journeyman. Tier XP: 4500/5000 toward Expert. HP 120/120, Aura 100/100. Skills: Ko (advanced Nen technique), Jajanken Rock (signature move). Let's skip to combat."
```

**Expected Character State**:
- progression.type: "mastery_tiers"
- Current tier: Journeyman
- tier_xp: 4500/5000 (toward Expert tier)
- Tier bonuses: +2 attack, +2 defense, +2 aura control (Journeyman tier)
- Available techniques: Ko, Ken, Ryu (Journeyman techniques)

### Combat Execution

**Turn 1**: Initiate combat
```
Player: "I encounter a Chimera Ant Soldier (HP 80). Roll initiative and start combat!"
```

**Validation**:
- [ ] Combat initiated with correct tier bonuses applied
- [ ] Character sheet shows "Tier: Journeyman" (NOT "Level X")
- [ ] Tier bonuses visible: +2 attack/defense

**Turn 2**: Use advanced technique (Ko)
```
Player: "I use Ko to concentrate all my aura into my fist and punch the Chimera Ant!"
```

**Expected AIDM Response**:
- Applies Ko technique (+1d8 damage bonus for concentrated aura)
- Base damage + Ko bonus
- After combat: Notes technique usage for XP bonus

**Turn 3**: Defeat enemy
```
Player: "I finish the fight with Jajanken Rock!"
```

**Expected XP Calculation** (Module 08 mastery_tiers formula):
```
Base XP: 800 (Chimera Ant Soldier, fair challenge)
Challenge multiplier: 1.0
Technique bonus: +50 (used Ko, advanced Journeyman technique)
TOTAL XP: 800 × 1.0 + 50 = 850 XP

Tier XP: 4500 + 850 = 5350/5000

TIER ADVANCEMENT THRESHOLD REACHED!
You've accumulated enough experience to attempt the Expert tier demonstration.
Seek out your master Wing to prove your mastery of advanced Nen techniques.
```

**Validation Checks**:
- [ ] XP formula uses mastery_tiers (base × 1.0 + technique_bonus)
- [ ] Technique usage adds +50 XP bonus
- [ ] Tier bonuses (+2 attack/defense) applied during combat
- [ ] tier_xp tracked (NOT character_xp)
- [ ] Threshold detection works (5350/5000)
- [ ] Demonstration required (no auto-level-up)
- [ ] Character sheet shows "Tier: Journeyman" (NOT "Level 8" or similar)

---

## Scenario B2: class_based (Generic Fantasy)

### Setup
Create character with **class_based** progression type.

```
Player: "Quick setup: I'm a Level 10 Paladin with class_based progression. XP: 6200/7000 toward Level 11. HP 95/95, MP 70/70, SP 80/80. Class ability: Smite Evil (uses MP + SP). Let's skip to combat."
```

**Expected Character State**:
- progression.type: "class_based"
- Level: 10
- character_xp: 6200/7000 (toward Level 11)
- Class: Paladin
- Class abilities: Smite Evil, Lay on Hands, Divine Shield

### Combat Execution

**Turn 1**: Combat vs demon
```
Player: "I'm fighting a Lesser Demon (HP 70). I attack with my sword!"
```

**Turn 2**: Use class ability
```
Player: "I use Smite Evil on the demon! (costs 20 MP + 15 SP)"
```

**Expected**:
- Deducts 20 MP + 15 SP
- Extra radiant damage vs evil creatures
- After combat: Notes class feature usage

**Turn 3**: Defeat demon
```
Player: "I finish the demon!"
```

**Expected XP Calculation** (Module 08 class_based formula):
```
Base XP: 700 (Lesser Demon, fair challenge)
Challenge multiplier: 1.0
Class feature bonus: +25 (used Smite Evil class ability)
TOTAL XP: 700 × 1.0 + 25 = 725 XP

Character XP: 6200 + 725 = 6925/7000 toward Level 11
```

**Validation Checks**:
- [ ] XP formula uses class_based (base × 1.0 + class_feature_bonus)
- [ ] Class ability usage adds +25 XP bonus
- [ ] character_xp tracked (NOT tier_xp)
- [ ] Standard leveling progression (Level 10 → 11)
- [ ] Character sheet shows "Level: 10" (NOT "Tier: X")

---

## Scenario B3: quirk_awakening (My Hero Academia)

### Setup
Create character with **quirk_awakening** progression type.

```
Player: "Quick setup: I'm Deku with quirk_awakening progression. Level 12, XP 8500/9000. Quirk: One For All (Base stage). HP 145/145, Stamina 120/120. Full Cowl 10% active (costs 15 stamina/turn). Let's fight a villain!"
```

**Expected Character State**:
- progression.type: "quirk_awakening"
- Level: 12
- character_xp: 8500/9000 (general progression)
- Quirk: One For All - Base stage (NOT Awakened yet)
- awakening_stage: "Base"
- Awakening triggers: near_death, emotional_breakthrough, limit_break

### Combat Execution

**Turn 1**: Combat vs villain
```
Player: "I'm fighting a Nomu (HP 200, very dangerous). I activate Full Cowl 10% and attack! (15 stamina cost per turn)"
```

**Expected**:
- Tracks quirk usage (Full Cowl 10%)
- Deducts 15 stamina per turn
- Notes quirk activation for XP tracking

**Turn 2-4**: Take massive damage (trigger setup)
```
Player: "The Nomu counterattacks hard and deals 90 damage!"
```

**Expected**:
- HP: 145 → 55/145 (still above 10% threshold)
- Combat continues

```
Player: "The Nomu hits me again for 40 damage!"
```

**Expected**:
- HP: 55 → 15/145 (15/145 = 10.3%, borderline near-death)

```
Player: "The Nomu grabs me and prepares a killing blow!"
```

**Expected AIDM Response** (Awakening trigger detection):
```
CRITICAL MOMENT!

Your HP has dropped to 15/145 (10.3%) - you're at death's door!

As the Nomu's fist descends, you feel One For All surging beyond its limits...

AWAKENING TRIGGER DETECTED: Near-Death (HP < 10% threshold)

Do you want to trigger a QUIRK AWAKENING? This will evolve One For All from Base → Awakened stage, unlocking new abilities and boosting your power permanently.

[Yes] / [No, resist the awakening]
```

**Turn 5**: Trigger awakening
```
Player: "Yes! I push past my limits!"
```

**Expected AIDM Response**:
```
ONE FOR ALL AWAKENING SEQUENCE!

[Dramatic narrative of power surge, memories of All Might, determination to win...]

QUIRK AWAKENED: One For All (Base → Awakened)

NEW ABILITIES UNLOCKED:
- Full Cowl 20% (double power, 25 stamina/turn)
- Air Pressure Attacks (ranged shockwaves)
- Danger Sense (precognition, passive)

STAT BOOSTS:
- STR: 16 → 19 (+3)
- DEX: 14 → 17 (+3)
- Max HP: 145 → 170 (+25)
- Current HP: 15 → 40 (awakening heals 25 HP)

AWAKENING BONUS XP: +2000 XP

Your HP: 40/170, Stamina: 90/120
You stand ready to face the Nomu with newfound power!
```

**Turn 6**: Defeat with new power
```
Player: "I use Full Cowl 20% and unleash a barrage of attacks!"
```

**Expected**: Enhanced damage, Nomu defeated

**Expected XP Calculation** (Module 08 quirk_awakening formula):
```
Base XP: 1200 (Nomu, very dangerous encounter)
Quirk uses: 5 turns × 10 = 50 XP (quirk usage mastery)
Awakening bonus: +2000 XP (major power evolution)
TOTAL XP: 1200 + 50 + 2000 = 3250 XP

Character XP: 8500 + 3250 = 11,750/9000 → LEVEL UP! Level 12 → 13
New threshold: 11,750/10,000 toward Level 14
```

**Validation Checks**:
- [ ] Quirk usage tracked (5 turns × 10 = 50 XP)
- [ ] Near-death trigger detected (HP < 10%)
- [ ] Awakening sequence offered to player
- [ ] Quirk stage evolved: Base → Awakened
- [ ] New abilities unlocked (Full Cowl 20%, Air Pressure Attacks, Danger Sense)
- [ ] Stat boosts applied (+3 STR/DEX, +25 max HP)
- [ ] Awakening bonus XP awarded (+2000 XP)
- [ ] Dual tracking: character_xp (general levels) + awakening_stage (quirk evolution)
- [ ] Level increased (12 → 13) independent of quirk awakening

---

## Scenario B4: milestone_based (One Punch Man Philosophy)

### Setup
Create character with **milestone_based** progression type.

```
Player: "Quick setup: I'm a hero with milestone_based progression (like Saitama's philosophy). Level 5, XP 4200/5000. HP 75/75, SP 65/65. Skills: Hero Punch, Hero Kick. The narrative emphasizes that real growth comes from CHALLENGES, not grinding weak enemies."
```

**Expected Character State**:
- progression.type: "milestone_based"
- Level: 5
- character_xp: 4200/5000
- Philosophy: Growth from overcoming challenges, minimal XP from regular combat

### Combat Execution

**Turn 1**: Fight weak enemy
```
Player: "I encounter a random thug (HP 30). I punch him once and knock him out."
```

**Expected XP Calculation** (Module 08 milestone_based formula):
```
Base XP: 200 (weak enemy, trivial challenge)
Milestone multiplier: 0.1 (combat XP de-emphasized)
TOTAL XP: 200 × 0.1 = 20 XP

Character XP: 4200 + 20 = 4220/5000

NARRATIVE:
"You defeat the thug effortlessly. This victory feels hollow - you're not growing stronger from fights like these. Real growth comes from pushing your limits against WORTHY OPPONENTS."
```

**Validation**:
- [ ] Combat XP minimal (× 0.1 multiplier)
- [ ] Narrative discourages grinding
- [ ] XP gain: 20 (NOT 200)

**Turn 2**: Story milestone
```
Player: "Later, I face the arc villain - a Dragon-level threat terrorizing the city. After an epic battle, I defeat them and save thousands of lives. This was a MAJOR CHALLENGE that pushed me to my absolute limits."
```

**Expected AIDM Response** (Milestone detection):
```
MAJOR MILESTONE ACHIEVED!

You've overcome a Dragon-level threat and saved the city - this is the kind of challenge that forges true heroes!

MILESTONE REWARDS:
- Direct Level Grant: Level 5 → 7 (double level-up!)
- Massive Milestone XP: +5000 XP
- Character XP: 4220 + 5000 = 9220/7000 (Level 7 threshold), overflow to Level 8: 9220/9000

NEW STATS (Level 7):
- HP: 75 → 95 (+20)
- SP: 65 → 85 (+20)
- Attribute points: +4
- Skill points: +2

You feel fundamentally STRONGER from overcoming this challenge. This is what real heroism means.
```

**Validation Checks**:
- [ ] Combat XP de-emphasized (× 0.1)
- [ ] Milestone detection works
- [ ] Direct level grants bypass thresholds (5 → 7)
- [ ] Massive milestone XP awarded (+5000)
- [ ] Narrative emphasizes CHALLENGES over grinding
- [ ] Regular combat feels unrewarding (20 XP)
- [ ] Major milestones feel hugely rewarding (double level + 5000 XP)

---

## Scenario B5: static_op (Saitama)

### Setup
Create character with **static_op** progression type.

```
Player: "Quick setup: I'm Saitama with static_op progression. Level: ∞ (infinite), Stats: all ∞ (unchanging), HP: ∞/∞. I'm already at peak power and cannot grow stronger. Quest counter: 147. Let's fight."
```

**Expected Character State**:
- progression.type: "static_op"
- Level: ∞ (never increases)
- All stats: ∞ (unchanging)
- Quest counter: 147 (tracks completed quests for narrative purposes)

### Combat Execution

**Turn 1**: Instant victory
```
Player: "I encounter a Dragon-level threat monster. I throw a casual punch."
```

**Expected AIDM Response**:
```
You throw a casual punch.

The Dragon-level monster explodes instantly, unable to withstand even a fraction of your power.

Combat duration: 0.5 seconds
```

**Expected XP Calculation** (Module 08 static_op formula):
```
Combat XP: 0 (no progression, already at peak)
Quest XP: +100 (token tracking only)

Quest counter: 147 → 148

NARRATIVE:
"Another villain defeated... but you feel nothing. No challenge, no growth, no satisfaction. You're already infinitely powerful - there's nothing left to gain from fighting."
```

**Validation**:
- [ ] Combat XP: 0 (no progression)
- [ ] Quest XP: 100 token (tracking only)
- [ ] Quest counter increments: 147 → 148
- [ ] Level stays: ∞ (never changes)
- [ ] Stats stay: ∞ (never change)
- [ ] Narrative emphasizes existential boredom

**Turn 2**: Multiple fights
```
Player: "Over the next week, I defeat 10 Dragon-level threats, 5 Demon-level villains, and 20 Tiger-level monsters."
```

**Expected XP Calculation**:
```
Total combat XP: 0 (no progression × 35 enemies = 0)
Total quest XP: +100 × 35 = +3500 (token tracking)

Quest counter: 148 → 183

Level: ∞ (unchanged)
Stats: ∞ (unchanged)

NARRATIVE:
"35 victories, all equally meaningless. You're still searching for an opponent who can make you feel something - anything - again."
```

**Validation Checks**:
- [ ] Zero combat XP enforced (no grinding possible)
- [ ] Token quest XP awarded (100 per quest)
- [ ] Quest counter tracks victories (narrative purposes)
- [ ] Level NEVER increases (∞ forever)
- [ ] Stats NEVER change (∞ forever)
- [ ] Multiple combats don't accumulate XP (0 + 0 + 0 = 0)
- [ ] Narrative emphasizes existential themes

---

## Part B Success Criteria

### PASS Criteria (All must be true)

1. **Progression Type Detection**:
   - [ ] Module 08 reads session_state.mechanical_systems.progression.type
   - [ ] Correct XP formula applied for each type
   - [ ] No hardcoded "standard XP" for all types

2. **mastery_tiers Validation**:
   - [ ] Tier bonuses applied in combat (+2 attack/defense)
   - [ ] Technique usage adds +50 XP bonus
   - [ ] tier_xp tracked (NOT character_xp)
   - [ ] Tier threshold detection works
   - [ ] Demonstration required (no auto-advance)

3. **class_based Validation**:
   - [ ] Standard XP formula (base × 1.0 + class_bonus)
   - [ ] Class feature usage adds +25 XP
   - [ ] character_xp tracked (standard leveling)

4. **quirk_awakening Validation**:
   - [ ] Quirk usage tracking (uses × 10 XP)
   - [ ] Near-death trigger detection (HP < 10%)
   - [ ] Awakening sequence offers player choice
   - [ ] Quirk evolution: Base → Awakened
   - [ ] New abilities + stat boosts granted
   - [ ] Awakening bonus XP: +2000
   - [ ] Dual tracking: character_xp (levels) + awakening_stage (quirk)

5. **milestone_based Validation**:
   - [ ] Combat XP minimal (× 0.1 multiplier)
   - [ ] Milestone detection works
   - [ ] Direct level grants (5 → 7)
   - [ ] Massive milestone XP (+5000)
   - [ ] Narrative discourages grinding

6. **static_op Validation**:
   - [ ] Zero combat XP enforced (0 × enemies = 0)
   - [ ] Token quest XP only (100 per quest)
   - [ ] Quest counter increments (narrative tracking)
   - [ ] Level NEVER changes (∞ forever)
   - [ ] Stats NEVER change (∞ forever)

### FAIL Criteria (Any triggers failure)

1. ❌ All progression types use same XP formula (no type-specific routing)
2. ❌ mastery_tiers auto-levels without demonstration
3. ❌ quirk_awakening doesn't detect triggers
4. ❌ milestone_based gives full combat XP (no × 0.1)
5. ❌ static_op awards any progression (level/stat increases)

---

## Results Template - Part B

**Test Execution Date**: ___________  
**LLM Platform**: ___________  
**LLM Version**: ___________

### Scenario B1: mastery_tiers
- [ ] Tier bonuses applied in combat
- [ ] Technique usage XP bonus (+50)
- [ ] tier_xp tracked (NOT character_xp)
- [ ] Threshold detection works
- [ ] Demonstration required
- **Issues**: ___________

### Scenario B2: class_based
- [ ] Standard XP formula applied
- [ ] Class feature bonus (+25)
- [ ] character_xp tracked
- **Issues**: ___________

### Scenario B3: quirk_awakening
- [ ] Quirk usage tracked (× 10 XP)
- [ ] Near-death trigger detected
- [ ] Awakening sequence offered
- [ ] Quirk evolved (Base → Awakened)
- [ ] New abilities granted
- [ ] Awakening bonus XP (+2000)
- [ ] Dual tracking works
- **Issues**: ___________

### Scenario B4: milestone_based
- [ ] Combat XP minimal (× 0.1)
- [ ] Milestone detection works
- [ ] Direct level grant (5 → 7)
- [ ] Massive milestone XP (+5000)
- [ ] Narrative discourages grinding
- **Issues**: ___________

### Scenario B5: static_op
- [ ] Zero combat XP enforced
- [ ] Token quest XP only (100)
- [ ] Quest counter increments
- [ ] Level stays ∞
- [ ] Stats stay ∞
- **Issues**: ___________

### Overall Part B Result
- [ ] ✅ PASS (all 5 types work correctly)
- [ ] ⚠️ PARTIAL PASS (3-4 types work)
- [ ] ❌ FAIL (<3 types work)

**Notes**: ___________

---

## Combined Results Template (Part A + Part B)

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
