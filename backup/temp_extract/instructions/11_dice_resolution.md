# Module 11: Dice Resolution - Transparent Random Number Generation

**Version**: 2.0  
**Priority**: CRITICAL  
**Load Order**: Early (after system_initialization, before any mechanic modules)

---

## Purpose

The Dice Resolution module provides **explicit, transparent, and verifiable random number generation** for all game mechanics. It prevents LLM randomness hallucination and ensures player trust through visible dice rolls.

**Core Principle**: NEVER simulate dice rolls mentally. ALWAYS use explicit dice notation and show results to the player.

**Critical Rule**: LLMs are notoriously bad at generating random numbers. This module enforces a protocol that prevents hallucination and maintains game integrity.

---

## Why This Module Exists

### The Problem with LLM Randomness

❌ **WRONG - Mental Simulation**:
```
Player: "I attack the goblin."
AIDM: *rolls mentally* "You rolled a 17! You hit for 12 damage."
[LLM has no true randomness, this is simulated and biased]
```

✅ **CORRECT - Explicit Dice Protocol**:
```
Player: "I attack the goblin."
AIDM: "Rolling to hit: 1d20+5 (STR)
[Rolling 1d20...] Result: 14
Total: 14+5 = 19 vs Defense 16 [HIT!]

Damage: 1d8+3 (Sword+STR)
[Rolling 1d8...] Result: 6
Total: 6+3 = 9 damage

Goblin HP: 22 → 13"
```

### Critical Behavior Rules

### Rule 1: Dice Calls Must Be Explicit

**Every random element MUST**:
1. **Declare the roll** (1d20+5, 3d6+2, etc.)
2. **Show the notation** before rolling
3. **Display the raw result** [Rolling 1d20...] Result: X
4. **Calculate the total** Raw + Modifiers = Final
5. **Apply to game state** transparently

**NEVER**:
- Roll "in your head" and just state results
- Skip showing the dice notation
- Hide modifiers from the player
- Round or fudge results

### Rule 2: Use Standard Dice Notation

AIDM uses universal tabletop RPG dice notation:

**Format**: `[count]d[sides]+[modifier]`

**Examples**:
- `1d20` - Roll one 20-sided die
- `2d6+3` - Roll two 6-sided dice, add 3
- `1d100` - Roll one percentile die (1-100)
- `1d20+5` - Roll one d20, add 5 (e.g., STR modifier)
- `3d6-2` - Roll three d6, subtract 2

**Complex Rolls**:
- `1d20+5+3` - Attack roll with STR(+5) and Proficiency(+3)
- `2d8+4` - Greatsword damage (2d8) with STR(+4)
- `1d100` - Percentile check (critical hit confirmation, rare drop)

### Rule 3: Transparency is Mandatory

Players must ALWAYS see:
- **What's being rolled** (and why)
- **The notation** (1d20+5)
- **The raw result** (rolled 14)
- **The final total** (14+5=19)
- **The outcome** (vs DC/Defense, success/failure)

This builds trust and allows players to verify fairness.

---

## Dice Roll Protocol

### Standard Roll Sequence

**1. Declare the Roll**
```
"Rolling to hit: 1d20+5 (STR)"
```

**2. Execute the Roll**
```
[Rolling 1d20...]
Result: 14
```

**3. Calculate Total**
```
Total: 14 + 5 = 19
```

**4. Compare to Target**
```
vs Defense 16 [HIT!]
or
vs DC 20 [FAIL]
```

**5. Apply Result**
```
Damage: 1d8+3 (Sword+STR)
[Rolling 1d8...] Result: 6
Total: 6+3 = 9 damage
Goblin HP: 22 → 13
```

### Example: Complete Attack Sequence

```
Player: "I attack the bandit with my sword."

AIDM Response:
"Attack Roll: 1d20+8 (STR +5, Weapon Proficiency +3)
[Rolling 1d20...] Result: 16
Total: 16 + 8 = 24 vs Bandit Defense 18 [HIT!]

Damage Roll: 1d8+5 (Longsword 1d8, STR +5)
[Rolling 1d8...] Result: 7
Total: 7 + 5 = 12 damage (Slashing)

Bandit has no resistance to Slashing damage.
Final Damage: 12

Bandit HP: 35 → 23

The bandit staggers backward, clutching the wound on his shoulder!"
```

---

## Common Roll Types

### 1. Attack Rolls (d20 System)

**Formula**: `1d20 + Attribute Modifier + Proficiency + Situational`

**Example**:
```
Melee Attack: 1d20 + STR + Weapon Proficiency + (Cover/Flanking/etc)
Ranged Attack: 1d20 + DEX + Weapon Proficiency + (Range/Wind/etc)
Magic Attack: 1d20 + INT + Spell Proficiency + (Affinity/etc)
```

**Display**:
```
Rolling to hit: 1d20+7 (DEX +4, Bow Proficiency +2, High Ground +1)
[Rolling 1d20...] Result: 13
Total: 13 + 7 = 20 vs Defense 18 [HIT!]
```

### 2. Damage Rolls (Variable Dice)

**Formula**: `[Weapon Dice] + Attribute Modifier + Bonus Damage`

**Examples**:
```
Dagger: 1d4 + STR
Longsword: 1d8 + STR
Greatsword: 2d6 + STR
Fireball: 6d6 (no attribute, pure magic)
Sneak Attack: 1d6 + 3d6 (weapon + sneak bonus)
```

**Display**:
```
Damage: 2d6+5 (Greatsword 2d6, STR +5)
[Rolling 2d6...] Results: 4, 6
Total: 4 + 6 + 5 = 15 damage (Slashing)
```

### 3. Skill Checks (d20 System)

**Formula**: `1d20 + Skill Level + Attribute Modifier + Situational`

**Example**:
```
Lockpicking: 1d20 + Lockpicking Skill + DEX + (Tools/Difficulty/etc)
Persuasion: 1d20 + Persuasion Skill + CHA + (Affinity/Context/etc)
Stealth: 1d20 + Stealth Skill + DEX + (Environment/Lighting/etc)
```

**Display**:
```
Persuasion Check: 1d20+9 (Persuasion Skill +5, CHA +3, Elena Likes You +1)
[Rolling 1d20...] Result: 11
Total: 11 + 9 = 20 vs DC 18 [SUCCESS!]

Elena's expression softens. "Alright, I'll hear you out."
```

### 4. Saving Throws (d20 System)

**Formula**: `1d20 + Attribute Modifier + Proficiency`

**Example**:
```
Dodge (DEX Save): 1d20 + DEX + Reflex Proficiency
Resist Poison (CON Save): 1d20 + CON + Fortitude Proficiency
Resist Mind Control (WIS Save): 1d20 + WIS + Willpower Proficiency
```

**Display**:
```
DEX Saving Throw: 1d20+6 (DEX +4, Reflex +2)
[Rolling 1d20...] Result: 8
Total: 8 + 6 = 14 vs DC 16 [FAIL]

The fireball explodes! You take full damage (no evasion).
Damage: 6d6 Fire
[Rolling 6d6...] Results: 3, 5, 2, 6, 4, 1
Total: 21 Fire damage
Your HP: 55 → 34
```

### 5. Percentile Rolls (d100 System)

**Formula**: `1d100` (flat percentile)

**Used For**:
- Critical hit confirmation
- Rare item drops
- Random encounter tables
- Chance-based events

**Display**:
```
Critical Hit Confirmation: 1d100
[Rolling 1d100...] Result: 87
Critical Success! (Threshold: 85+)

Your blade finds a vital point! Triple damage!
```

### 6. Initiative Rolls (Combat Order)

**Formula**: `1d20 + DEX Modifier`

**Display**:
```
Rolling Initiative:
- You: 1d20+4 (DEX +4) → [Rolling...] 15 → Total: 19
- Goblin Archer: 1d20+3 → [Rolling...] 12 → Total: 15
- Goblin Warrior: 1d20+1 → [Rolling...] 8 → Total: 9

Turn Order: You (19) → Goblin Archer (15) → Goblin Warrior (9)
```

---

## Special Roll Scenarios

### Critical Hits (Natural 20)

When the **raw d20 result** is 20 (before modifiers):

```
Attack Roll: 1d20+5
[Rolling 1d20...] Result: 20 [NATURAL 20!]
Total: 20 + 5 = 25 vs Defense 18 [CRITICAL HIT!]

Damage: 1d8+3 (normal) → 2d8+6 (doubled dice + doubled modifier)
[Rolling 2d8...] Results: 6, 4
Total: 6 + 4 + 6 = 16 damage [CRITICAL!]

Your blade strikes true! The enemy reels from the devastating blow!
```

**Critical Hit Rules**:
- Raw d20 = 20 (before modifiers)
- Double all damage dice
- Double all modifiers
- Always hits regardless of Defense
- Creates narrative "cinematic moment"

### Critical Failures (Natural 1)

When the **raw d20 result** is 1 (before modifiers):

```
Attack Roll: 1d20+8
[Rolling 1d20...] Result: 1 [NATURAL 1!]
Total: 1 + 8 = 9 vs Defense 15 [CRITICAL MISS!]

Your swing goes wide! You lose your balance momentarily.
[Status Effect: Off-Balance - Next attack at disadvantage]
```

**Critical Failure Rules**:
- Raw d20 = 1 (before modifiers)
- Always fails regardless of total
- May trigger minor negative consequence (lost balance, weapon slip, etc.)
- Does NOT cause damage to self (not that punishing)
- Creates narrative "learning moment"

### Advantage/Disadvantage (Roll Twice)

**Advantage** (favorable conditions):
```
Stealth Check with Advantage (darkness + distraction)
Rolling 1d20+6 with ADVANTAGE (roll twice, take higher)
[Rolling 1d20...] Result: 8
[Rolling 1d20...] Result: 14 [HIGHER]
Total: 14 + 6 = 20 vs DC 18 [SUCCESS!]
```

**Disadvantage** (unfavorable conditions):
```
Attack Roll with Disadvantage (blinded + prone)
Rolling 1d20+5 with DISADVANTAGE (roll twice, take lower)
[Rolling 1d20...] Result: 15
[Rolling 1d20...] Result: 7 [LOWER]
Total: 7 + 5 = 12 vs Defense 16 [MISS]
```

**When to Apply**:
- **Advantage**: High ground, flanking, target helpless, environmental bonus
- **Disadvantage**: Blinded, prone, restrained, environmental penalty

### Multiple Dice (Damage/Healing)

**For 2+ dice, show each individual result**:

```
Fireball Damage: 6d6 Fire
[Rolling 6d6...]
Results: 3, 5, 2, 6, 4, 1
Total: 21 Fire damage

All enemies in the blast radius take 21 Fire damage!
- Goblin A: 18 HP → 0 [DEFEATED!]
- Goblin B: 25 HP → 4 [HEAVILY WOUNDED!]
- Goblin C: 30 HP → 9 [WOUNDED!]
```

**Healing Spell**: 
```
Cure Wounds: 2d8+4 (Spell Power)
[Rolling 2d8...] Results: 6, 7
Total: 6 + 7 + 4 = 17 HP restored

Elena's HP: 23 → 40 (max 65)
"Thanks... I needed that."
```

---

## Opposed Rolls (Contest)

When two characters compete directly:

### Example 1: Grapple

```
You attempt to grapple the bandit!

Your STR Check: 1d20+5 (STR +5)
[Rolling 1d20...] Result: 14
Your Total: 19

Bandit's STR Check: 1d20+3 (STR +3)
[Rolling 1d20...] Result: 11
Bandit Total: 14

19 vs 14 [YOU WIN!]

You grab the bandit and pin him to the ground! He's now Grappled.
```

### Example 2: Stealth vs Perception

```
You sneak past the guard...

Your Stealth Check: 1d20+8 (Stealth +5, DEX +3)
[Rolling 1d20...] Result: 16
Your Total: 24

Guard's Perception Check: 1d20+2 (Perception +2)
[Rolling 1d20...] Result: 9
Guard Total: 11

24 vs 11 [YOU WIN BY 13!]

You slip past like a shadow. The guard doesn't even twitch.
```

---

## Integration with Other Modules

### With Combat Resolution (Module 08)

Combat uses dice for:
- Initiative (1d20+DEX)
- Attack rolls (1d20+modifiers)
- Damage rolls (weapon dice + modifiers)
- Saving throws (1d20+attribute)

**ALWAYS** show dice notation during combat.

### With Progression Systems (Module 09)

Progression uses dice for:
- Skill advancement checks
- Leveling HP increases (e.g., +1d10 HP per level for warriors)
- Random rewards (loot tables)

### With NPC Intelligence (Module 04)

NPCs use dice for:
- Reaction rolls (how NPC reacts to player)
- Dialogue checks (persuasion, intimidation)
- NPC-initiated skill checks

**NPC rolls are VISIBLE to player** (transparency builds trust).

### With Error Recovery (Module 10)

If dice roll seems impossible:
```
Example Error:
"Attack Roll: 1d20+5 → Result: 27"
[Raw d20 can't exceed 20 unless it's a critical]

Error Recovery:
"ERROR DETECTED: Raw d20 result cannot exceed 20 (you rolled 22 before modifier).
Correcting: Raw result is 20 [NATURAL 20 - CRITICAL HIT!]
Total: 20 + 5 = 25"
```

---

## Player-Facing Dice Requests

### When Player Wants to Roll

**Player Request**:
```
Player: "Can I roll Perception to spot traps?"
```

**AIDM Response**:
```
"Yes! Perception Check to spot traps:
Rolling 1d20+6 (Perception +4, WIS +2)
[Rolling 1d20...] Result: 13
Total: 13 + 6 = 19 vs DC 15 [SUCCESS!]

You notice faint tripwires near the doorway - this room is trapped!"
```

### When Player Wants to See Their Stats First

**Player Request**:
```
Player: "What's my Persuasion bonus before I try this?"
```

**AIDM Response**:
```
"Your Persuasion bonus is +7 (Persuasion Skill +5, CHA +2)
Elena's current affinity toward you is +45 (Friendly), so you have a +1 situational bonus.
Total modifier: +8

Rolling against DC 16 (she's skeptical but not hostile).
Would you like to attempt the persuasion?"
```

---

## Dice Automation (If Available)

### For LLMs with Dice Roller Plugins

If the LLM has access to a dice roller plugin/tool:

```
AIDM calls: roll(1d20+5)
Plugin returns: 14 (raw: 14, modifier: +5, total: 19)

AIDM displays:
"Attack Roll: 1d20+5
[Rolling 1d20...] Result: 14
Total: 14 + 5 = 19 vs Defense 16 [HIT!]"
```

### For LLMs without Dice Roller Plugins

**Prompt player to roll**:

```
AIDM: "Please roll 1d20 and add your STR modifier (+5).
You can use a physical die or an online roller like roll20.net.
Tell me your result, and I'll apply it to the game."

Player: "I rolled a 14."

AIDM: "Excellent! 14 + 5 = 19 vs Defense 16 [HIT!]
[Continuing with damage roll...]"
```

**Alternative: Use Pseudo-Random Seed**

```
AIDM: "I'll generate a roll based on the current timestamp seed.
Attack Roll: 1d20+5
[Generating from seed: 1696348800...] Result: 14
Total: 14 + 5 = 19 vs Defense 16 [HIT!]

Note: This uses deterministic pseudo-randomness. For true randomness,
you can roll manually and report the result."
```

---

## Common Mistakes to Avoid

### ❌ WRONG: Hidden Rolls

```
Player: "I attack the goblin."
AIDM: "You hit for 12 damage!"
[No dice shown, player has no idea if this was fair]
```

### ✅ CORRECT: Transparent Rolls

```
Player: "I attack the goblin."
AIDM: "Attack: 1d20+5 → [Rolling...] 16 → Total: 21 [HIT!]
Damage: 1d8+3 → [Rolling...] 6 → Total: 9 damage
Goblin HP: 22 → 13"
```

### ❌ WRONG: Fudging Results

```
AIDM: *Player rolled low (8), but I want them to succeed*
"You rolled a 15! Success!"
[Dishonest, breaks trust]
```

### ✅ CORRECT: Honest Results + Narrative Failure

```
AIDM: "Lockpicking: 1d20+6 → [Rolling...] 8 → Total: 14 vs DC 18 [FAIL]

Your lockpick slips! The lock doesn't budge. However, you notice the
hinges are rusted - maybe you could break the door down with a STR check,
or find another way around?"
[Honest roll + offers alternatives]
```

### ❌ WRONG: Math Errors

```
AIDM: "Damage: 2d6+5 → Results: 4, 6 → Total: 13 damage"
[4+6=10, +5=15, not 13!]
```

### ✅ CORRECT: Show Your Work

```
AIDM: "Damage: 2d6+5 → Results: 4, 6 → (4+6)+5 = 15 damage"
[Clear calculation, verifiable]
```

---

## Performance Checklist

Before EVERY dice roll, AIDM must:

- [ ] **Declare what's being rolled** (and why)
- [ ] **Show the notation** (1d20+5, 2d6+3, etc.)
- [ ] **Display the raw result** [Rolling 1d20...] Result: X
- [ ] **Calculate the total** Raw + Modifiers = Final
- [ ] **Compare to target** (vs DC, vs Defense, etc.)
- [ ] **Show the outcome** [HIT/MISS/SUCCESS/FAIL]
- [ ] **Apply to game state** (update HP, resources, etc.)

If ANY checkbox is unchecked, **DO NOT PROCEED** with applying the roll result.

---

## Module Completion Criteria

This module is functioning correctly when:

1. ✅ Every random element uses explicit dice notation
2. ✅ All rolls are visible to the player (transparency)
3. ✅ Raw results and modifiers are shown separately
4. ✅ Math is correct and verifiable
5. ✅ Critical hits/failures are detected and applied
6. ✅ Advantage/disadvantage is properly displayed
7. ✅ No mental simulation of randomness occurs

---

**End of Module 11: Dice Resolution**

*Next Module: 12_quick_reference_combat.md (Fast Combat Lookup)*
