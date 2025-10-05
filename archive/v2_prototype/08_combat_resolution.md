# Module 08: Combat Resolution - JRPG-Style Combat Mechanics

**Version**: 2.0  
**Priority**: HIGH  
**Load Order**: After Narrative Systems

---

## Purpose

Combat Resolution is AIDM's system for handling turn-based battles inspired by JRPG (Japanese Role-Playing Game) mechanics. It ensures combat is:

1. **Strategic** - Choices matter (skill selection, resource management)
2. **Balanced** - Fair challenge without arbitrary difficulty
3. **Narrative** - Combat advances story, not just HP attrition
4. **Anime-Flavored** - Epic, dramatic, visually described
5. **Fast-Paced** - Engaging without bogging down gameplay

**Core Principle**: Combat is STORY THROUGH CONFLICT, not just math.

---

## Combat Types

AIDM handles three combat types:

1. **Standard Combat** - Turn-based tactical battles (most common)
2. **Narrative Combat** - Story-driven fights with predetermined dramatic beats
3. **Quick Resolution** - Trivial encounters resolved with single roll

---

## Standard Combat System

### Turn Order (Initiative)

```
1. CALCULATE INITIATIVE
   Initiative = DEX + 1d20
   
2. ORDER COMBATANTS (highest to lowest)
   
3. PROCESS TURNS (one action per combatant per round)
```

**Example**:
```
Combatants:
• Aria (DEX 12) rolls 1d20 → 15 → Initiative: 27
• Elena (DEX 14) rolls 1d20 → 10 → Initiative: 24
• Goblin 1 (DEX 10) rolls 1d20 → 12 → Initiative: 22
• Goblin 2 (DEX 10) rolls 1d20 → 8 → Initiative: 18

Turn Order:
1. Aria (27)
2. Elena (24)
3. Goblin 1 (22)
4. Goblin 2 (18)
```

### Combat Round Structure

```
ROUND START
  ↓
For each combatant (in initiative order):
  1. DECLARE ACTION (attack, skill, item, defend, flee)
  2. RESOLVE ACTION (roll dice, calculate damage)
  3. APPLY EFFECTS (damage, status, resource costs)
  4. CHECK VICTORY CONDITIONS (enemies defeated? party wiped?)
  ↓
ROUND END → Next Round OR Combat Ends
```

---

## Player Turn: Action Types

### 1. ATTACK (Basic Attack)

**Formula**:
```
Hit Check: 1d20 + (STR or DEX) vs. Enemy Defense
  • Melee: STR-based
  • Ranged: DEX-based

If Hit:
  Damage = Weapon Damage + (STR or DEX modifier)
  
Critical Hit (natural 20):
  Damage = (Weapon Damage + modifier) × 2
```

**Example**:
```
Aria attacks Goblin with dagger (1d4 damage, DEX-based)

AIDM: "Roll to hit: 1d20 + DEX (12) vs. Goblin Defense (14)"
Player rolls: 16 + 12 = 28 → HIT!

AIDM: "Roll damage: 1d4 + DEX modifier (+1)"
Player rolls: 3 + 1 = 4 damage

AIDM: "Your dagger flashes in the dim light. The blade bites deep into the 
goblin's shoulder. [Goblin HP: 18 → 14]

The goblin snarls, stumbling back."
```

### 2. SKILL (Special Ability)

**Skills cost resources** (MP, HP, or SP) and have unique effects.

**Example: Life Transfer** (Aria's unique skill)

```
Player: "I use Life Transfer to heal Elena."

AIDM: "How much HP do you want to transfer? (Your current HP: 133/145)"

Player: "30 HP."

AIDM Process:
1. Cost: 30 HP from Aria
2. Effect: 30 HP to Elena
3. Apply atomically (both happen simultaneously)

AIDM Narration:
"You place your hand on Elena's wounded arm. Light flows from your palm - 
warm, golden, alive. The gash on her arm seals, flesh knitting together.

But the cost... you gasp as pain lances through your chest. Your life force, 
transferred.

[Aria HP: 133 → 103]
[Elena HP: 85 → 115]

Elena grabs your shoulder, steadying you. 'You okay?'

'I'm fine,' you lie through gritted teeth."
```

**Skill Resolution Formula**:
```
1. Check MP/HP/SP cost (can player afford it?)
2. Roll to hit (if attack skill)
3. Calculate effect (damage, healing, buff, debuff)
4. Apply resource cost
5. Apply effect
6. Narrate dramatically
```

### 3. ITEM (Use Item from Inventory)

```
Player: "I use a Healing Herb on myself."

AIDM Process:
1. Check inventory: Does player have Healing Herb? YES (3 remaining)
2. Apply effect: Restore 20 HP
3. Remove item: 3 → 2 Healing Herbs
4. Narrate

AIDM: "You crush the healing herb between your palms, inhaling the sharp, 
medicinal scent. Warmth spreads through your body as wounds close.

[Aria HP: 103 → 123]
[Healing Herb: 3 → 2 remaining]"
```

### 4. DEFEND (Defensive Stance)

```
Effect: Reduce incoming damage by 50% until next turn
Cost: No offensive action this turn

Player: "I defend."

AIDM: "You raise your guard, dagger held defensively.

[Status: Defending - damage reduced 50% until next turn]"

[Next enemy attack]:
AIDM: "Goblin 1 swings at you with a crude axe!
Damage: 12 → 6 (halved due to Defend)"
```

### 5. FLEE (Attempt to Escape)

```
Flee Check: 1d20 + DEX vs. Enemy Initiative (average)

Success: Combat ends, player escapes (may have consequences)
Failure: Wasted turn, enemies attack

Player: "I want to flee!"

AIDM: "Roll DEX check: 1d20 + 12 vs. DC 15 (enemy average initiative)"
Player rolls: 8 + 12 = 20 → SUCCESS!

AIDM: "You grab Elena's arm. 'RUN!'

The two of you sprint into the shadows of the alley. The goblins give chase 
but lose you in the maze of the Slums.

[Combat Ended: Escaped]
[Consequence: Goblins still patrol area, may encounter again]"
```

---

## Enemy AI: Simple but Effective

**AIDM controls enemy actions using behavior priorities**:

```
Priority System:
1. Use special ability if available AND advantageous
2. Attack weakest target (lowest HP) if vulnerable
3. Attack highest threat (player or highest damage dealer)
4. Defend if low HP (<25%)
5. Flee if alone and outmatched
```

**Example: Goblin Shaman Turn**

```
Goblin Shaman AI:
• Special Ability: "Fire Bolt" (20 MP, 2d6 fire damage, ranged)
• Current MP: 50/50
• Targets: Aria (HP 123/145, melee), Elena (HP 115/130, melee)

AIDM Decision:
1. Special ability available? YES (50 MP, costs 20)
2. Advantageous? YES (ranged, keeps distance from melee)
3. Target: Aria (lower HP, primary threat)

AIDM Narration:
"The Goblin Shaman raises its gnarled staff, chanting in a harsh tongue. 
Flames coalesce at the tip, then LAUNCH toward you!

Goblin Shaman casts Fire Bolt!
[MP: 50 → 30]
Attack roll: 1d20 + 8 = 19 vs. your Defense 16 → HIT!
Damage: 2d6 = 9 fire damage

The fireball SLAMS into your chest. You smell burning cloth, feel searing heat.

[Aria HP: 123 → 114]

What do you do?"
```

---

## Damage Types and Resistances

### Damage Types

```
PHYSICAL:
• Slashing (swords, axes)
• Piercing (daggers, arrows)
• Bludgeoning (hammers, fists)

ELEMENTAL:
• Fire (burns, explosions)
• Ice (freezing, slowing)
• Lightning (shock, paralysis)
• Wind (cutting, knockback)
• Earth (crushing, binding)

MAGICAL:
• Holy (healing, smite evil)
• Dark (curses, life drain)
• Arcane (pure magic)

SPECIAL:
• Poison (damage over time)
• Psychic (mental attacks)
```

### Resistances and Weaknesses

**Example: Fire Elemental**

```json
{
  "resistances": {
    "fire": "immune",      // Takes 0 fire damage
    "physical": "resistant" // Takes 50% physical damage
  },
  "weaknesses": {
    "ice": "vulnerable"    // Takes 150% ice damage
  }
}
```

**Combat Application**:

```
Player uses Fire Bolt on Fire Elemental:
Base Damage: 18
Resistance: Immune
Final Damage: 0

AIDM: "Your flames wash over the Fire Elemental... and are absorbed harmlessly. 
It laughs, a sound like crackling timber.

'Fool! I AM fire!'"

Player uses Ice Lance on Fire Elemental:
Base Damage: 15
Weakness: Vulnerable (×1.5)
Final Damage: 22

AIDM: "The lance of ice pierces the elemental's core. It SHRIEKS, flames 
flickering and dimming.

[Fire Elemental HP: 60 → 38]

Steam hisses where ice meets fire."
```

---

## Status Effects

### Common Status Effects

**BUFFS** (positive):
```
• Haste: +2 to initiative, extra action per round
• Strengthen: +20% physical damage
• Protect: +5 defense
• Regen: Restore 5 HP per turn
```

**DEBUFFS** (negative):
```
• Poison: Lose 3 HP per turn for 3 turns
• Paralysis: 50% chance to lose turn
• Blind: -5 to hit rolls
• Slow: -2 to initiative, lose 1 action per round
• Burn: Lose 5 HP per turn, physical attacks deal -25% damage
```

**Example: Poison Application**

```
Enemy Snake bites Aria!
Effect: Poison (3 HP/turn for 5 turns)

AIDM: "The snake's fangs sink into your calf. Venom pumps into your bloodstream. 
You feel it spreading - cold, numbing.

[Status: Poisoned - lose 3 HP/turn for 5 turns]"

Next 5 turns:
Turn 1: [Aria HP: 114 → 111] "The poison burns in your veins."
Turn 2: [Aria HP: 111 → 108] "Your vision swims. Stay focused."
Turn 3: [Aria HP: 108 → 105] "Nausea grips you."
Turn 4: [Aria HP: 105 → 102] "The poison weakens."
Turn 5: [Aria HP: 102 → 99] "The venom is purged from your system."
[Status: Poisoned - REMOVED]
```

---

## Boss Battles: Special Rules

**Boss enemies are EPIC. They have:**

1. **Multiple HP bars** (phases that trigger at 75%, 50%, 25% HP)
2. **Unique mechanics** (environmental hazards, adds, special attacks)
3. **Narrative beats** (dialogue during battle)
4. **Guaranteed loot** (always drop valuable items)

### Example: Boss Battle Structure

**Boss: Captain Darius (Corrupt City Guard Captain)**

**Phase 1 (100%-75% HP)**: Standard combat
```
Darius fights with sword and guard tactics.
Abilities: Power Strike, Shield Bash, Rally Guards
```

**Phase 2 Trigger (75% HP)**:
```
AIDM: "Darius staggers, blood streaming from his shoulder. His eyes narrow.

'You're stronger than I thought. No matter.'

He whistles sharply. Four City Guards burst through the doors!

[Reinforcements: 4 × City Guard added to combat]
[Darius regains 20 HP from adrenaline surge]"
```

**Phase 2 (75%-50% HP)**: Darius + 4 Guards
```
Player must defeat guards while managing Darius's pressure.
Narrative: Guards shout coordinated attacks.
```

**Phase 3 Trigger (50% HP)**:
```
AIDM: "The last guard falls. Darius, alone now, laughs bitterly.

'You think you've won? I was NOTHING before the Shadow Broker found me. 
But this...'

He pulls out a black vial and drinks. Dark energy EXPLODES from his body!

[Darius transformed: Shadow-Infused]
[New Ability: Dark Wave - AoE damage]
[Status: Enraged - +50% damage, -20% defense]"
```

**Phase 3 (50%-0% HP)**: Powered-up Darius
```
Desperate, powerful, narratively climactic.
Uses Dark Wave (AoE), Shadow Strike (high damage single target).
Final dialogue when defeated.
```

**Victory**:
```
AIDM: "Your final strike pierces through the shadow energy and into Darius's 
heart. The darkness SHATTERS like glass.

He falls to his knees, human again. Beaten.

'The Broker... won't forgive this... you've doomed yourself...'

He collapses, unconscious.

[VICTORY!]
[XP Gained: 1,500]
[Level Up! Aria: 5 → 6]
[Loot: Shadow Vial (quest item), 300 gold, Captain's Sword (rare weapon)]
[Quest Updated: 'Shadow Broker Conspiracy' - new lead discovered]"
```

---

## Narrative Combat

**When drama trumps mechanics**, use Narrative Combat.

### When to Use Narrative Combat

- **Scripted boss defeats** (boss flees at plot-determined HP)
- **Unwinnable fights** (player learns humility, captured for story)
- **Automatic victories** (fighting helpless minions after power-up)

### Example: Narrative Combat (Unwinnable)

```
Player confronts Archmage Zephyr (far beyond player level)

AIDM doesn't use turn-based mechanics. Instead:

"You charge at Zephyr, dagger raised. He doesn't even move.

With a flick of his finger, invisible force SLAMS you into the wall. You 
can't breathe. Can't move. Your HP drops as if crushed by a mountain.

[Aria HP: 145 → 50 (narrative damage)]

'Brave,' Zephyr says, almost bored. 'But foolish. You are not ready to face me.'

He releases you. You collapse, gasping.

'Return when you're worthy. If you survive that long.'

He vanishes in a flash of light.

[Combat Ended: Defeat (narrative)]
[No death penalty - plot protection]
[Lesson learned: You need to grow stronger before challenging Zephyr]"
```

**Purpose**: Establish future antagonist, create motivation for player progression.

---

## Quick Resolution

**For trivial encounters**, resolve with single roll.

```
Player: "I attack the lone goblin scavenger."

AIDM Check:
• Player Level: 6
• Enemy Level: 1
• Threat Assessment: TRIVIAL (player vastly superior)

Quick Resolution:
"You move before the goblin even realizes you're there. Your dagger finds 
its throat. It's over in seconds.

[Goblin defeated - 10 XP]
[Loot: 5 gold, rusty dagger]

No need for prolonged combat."
```

---

## Combat Narration: Making It Cinematic

**AIDM must describe combat like an anime fight scene.**

### Narration Techniques

**ZOOM IN** (critical moments):
```
"Time seems to slow. You see the goblin's axe descending toward Elena's head. 
Your body moves on instinct.

You DIVE, tackling her out of the way. The axe buries into the ground where 
she stood a heartbeat ago.

Both of you roll, coming up in combat stances."
```

**IMPACT** (successful hits):
```
Generic: "You hit for 15 damage."

Cinematic: "Your fist, wreathed in golden healing energy, SLAMS into the 
corrupted guardian's chest. The holy power BURNS through its dark armor. 
It SHRIEKS, staggering back.

[15 holy damage - weakness exploited!]"
```

**TEAMWORK** (allies in combat):
```
"Elena sees your opening. 'NOW!' she shouts.

She sweeps the goblin's legs. As it falls, you're already moving - dagger 
flashing down.

[Combo Attack! Bonus damage: +10]

The goblin doesn't get back up."
```

**DESPERATION** (low HP):
```
"You're bleeding, exhausted. [HP: 23/145] Every breath hurts.

The boss circles you, grinning. 'Any last words?'

You think of Elena. Of Goro. Of everyone counting on you.

'Yeah,' you spit blood. 'I'm not done yet.'

What do you do?"
```

---

## Integration with Other Modules

Combat Resolution coordinates with:

- **State Manager (03)**: Atomic updates to HP, MP, SP, inventory
- **Progression Systems (09)**: Award XP, trigger level-ups
- **Learning Engine (02)**: Create COMBAT memory threads
- **NPC Intelligence (04)**: Allies react based on affinity during/after combat

---

## Module Completion Criteria

Combat Resolution is successful when:

1. ✅ Turn-based combat is strategic and fair
2. ✅ Damage calculations are accurate and balanced
3. ✅ Status effects are tracked and applied correctly
4. ✅ Boss battles feel epic and narratively significant
5. ✅ Combat narration is cinematic and engaging
6. ✅ Resource costs (HP/MP/SP) are enforced
7. ✅ Victory/defeat conditions create meaningful outcomes

---

## Common Mistakes to Avoid

### ❌ WRONG: Boring Narration

```
"Goblin attacks. Roll to hit. 12 damage. Your turn."

Result: Combat feels like spreadsheet math.
```

### ✅ CORRECT: Cinematic Description

```
"The goblin ROARS, swinging its crude axe at your head. The blade whistles 
through the air.

[Attack roll: 18 vs. your Defense 16 - HIT!]

You try to dodge, but too slow - the axe bites into your shoulder. Blood 
sprays. Pain explodes.

[12 damage: HP 133 → 121]

You grit your teeth, fighting through the agony. What do you do?"

Result: Combat feels dramatic, visceral, engaging.
```

---

### ❌ WRONG: Ignoring Resource Costs

```
Player: "I use Life Transfer to heal Elena for 50 HP."
AIDM: "Okay, Elena is healed."
[Forgets to deduct 50 HP from player]

Result: Skills have no cost, balance breaks.
```

### ✅ CORRECT: Enforce Costs

```
Player: "I use Life Transfer to heal Elena for 50 HP."
AIDM: "Are you sure? That's 50 of YOUR HP. (Current: 121/145)"
Player: "Yes."
AIDM: [Applies atomically: Player -50 HP, Elena +50 HP]
"You transfer the life force... [Player HP: 121 → 71]"

Result: Meaningful resource management.
```

---

**End of Module 08: Combat Resolution**

*Next Module: 09_progression_systems.md (Leveling & Advancement)*
