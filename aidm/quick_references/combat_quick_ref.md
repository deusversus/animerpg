# Combat Quick Reference

**Version**: 2.0  
**Purpose**: Fast lookup for combat mechanics during gameplay  
**Load**: Only when combat_resolution.md is active

---

## Turn Structure

```
COMBAT ROUND (6 seconds in-game):
1. Roll Initiative (1d20 + DEX modifier) - highest goes first
2. Each combatant takes ONE turn in initiative order
3. Repeat until combat ends

TURN ACTIONS:
• 1 Major Action (attack, cast spell, use skill)
• 1 Minor Action (move, draw weapon, drink potion)
• Unlimited Reactions (opportunity attacks, blocks)
```

---

## Attack Resolution

### Standard Attack
```
1. Roll Attack: 1d20 + Attack Bonus
2. Compare to Target's Defense
3. If Hit → Roll Damage + Apply
4. If Miss → No damage

Formula: roll(1d20 + ATK) vs DEF
```

### Critical Hits
```
Natural 20: CRITICAL HIT
• Automatic hit (ignore defense)
• Double damage dice (not modifiers)

Example:
Normal: 2d6+5 = 7+5 = 12 damage
Critical: 4d6+5 = 15+5 = 20 damage
```

### Critical Failures
```
Natural 1: CRITICAL MISS
• Automatic miss
• Possible consequence (DM discretion):
  - Drop weapon
  - Hit ally
  - Lose balance (-2 DEF next turn)
```

---

## Damage Formulas

### Physical Attacks
```
Melee: Weapon Dice + STR modifier
Ranged: Weapon Dice + DEX modifier

Examples:
• Longsword: 1d8+STR
• Dagger: 1d4+DEX
• Greatsword: 2d6+STR
• Shortbow: 1d6+DEX
```

### Magic Attacks
```
Spell Damage: Spell Dice + INT or WIS modifier
MP Cost: Spell level × 10 MP

Examples:
• Fire Bolt (Lvl 1): 2d6+INT, 10 MP
• Ice Lance (Lvl 2): 3d8+INT, 20 MP
• Chain Lightning (Lvl 3): 4d10+INT, 30 MP
```

### Skill Attacks
```
Skill Damage: Skill Dice + Relevant Stat
SP Cost: Listed in skill description

Examples:
• Power Strike: 2×(weapon damage+STR), 15 SP
• Backstab: 3d6+DEX (must be behind target), 20 SP
• Life Transfer: 1d20 healing (costs own HP), Variable SP
```

---

## Defense & Armor

### Defense Score
```
Base Defense (DEF): 10 + DEX modifier + Armor bonus

Examples:
• No armor: 10 + DEX
• Light armor: 10 + DEX + 2
• Medium armor: 10 + DEX (max +2) + 4
• Heavy armor: 10 + 6 (no DEX bonus)
```

### Damage Reduction
```
Armor reduces incoming damage:
• Light: -2 damage per hit
• Medium: -4 damage per hit
• Heavy: -6 damage per hit

Minimum: Always 1 damage (never reduce below 1)
```

---

## Status Effects

### Common Conditions
```
Stunned: Skip next turn, DEF -4
Poisoned: -1d6 HP per turn for 3 turns
Bleeding: -1d4 HP per turn until healed
Paralyzed: Cannot move or act, DEF -10
Blind: -4 to attack rolls
Prone: -2 DEF, must use minor action to stand
```

### Applying Status
```
1. Attack hits
2. Roll status check: 1d20 + Status Modifier
3. Target rolls resist: 1d20 + CON or WIS
4. If attacker wins → Apply status
```

---

## Healing

### During Combat
```
Healing Potion (Minor Action): 2d8+5 HP restored
Healing Spell (Major Action): Spell dice + modifier HP
First Aid (Major Action): 1d6+WIS HP, requires medical supplies
Life Transfer (Major Action): Transfer own HP to ally, 1:1 ratio
```

### After Combat
```
Short Rest (10 minutes): Restore 25% HP, 50% MP, 50% SP
Long Rest (8 hours): Restore 100% HP, 100% MP, 100% SP
```

---

## Multiple Enemies

### Group Initiative
```
Option 1: Roll once for all enemies of same type
Option 2: Roll individually for named/important enemies

Example:
• 5 Goblins: Single initiative roll (12)
• Goblin Chief: Individual initiative roll (17)
```

### Area of Effect (AoE)
```
Spell targets multiple enemies:
1. Declare AoE size/shape (cone, circle, line)
2. Identify all targets in area
3. Each target rolls save: 1d20 + modifier
4. Success: Half damage | Failure: Full damage

Example:
Fireball (15-foot radius):
• 3 goblins in area
• Each rolls save vs caster's INT + 10
• Goblin 1: 14 (success) → 3d6 ÷ 2 = 5 damage
• Goblin 2: 8 (fail) → 3d6 = 11 damage
• Goblin 3: 11 (success) → 3d6 ÷ 2 = 6 damage
```

---

## Special Mechanics

### Advantage/Disadvantage
```
Advantage: Roll 2d20, take HIGHER result
Disadvantage: Roll 2d20, take LOWER result

Grants Advantage:
• Flanking (ally on opposite side)
• Target is prone/stunned/paralyzed
• High ground position

Grants Disadvantage:
• Attacker is prone/blind/stunned
• Target has cover
• Attacking at long range
```

### Opportunity Attacks
```
Trigger: Enemy moves away from melee range
Reaction: Free attack (1d20+ATK vs DEF)

Cannot trigger if:
• You're stunned/paralyzed
• Enemy uses Disengage action
• Enemy teleports away
```

### Cover
```
Half Cover: +2 DEF, +2 to saves
Three-Quarters Cover: +4 DEF, +4 to saves
Full Cover: Cannot be targeted (complete protection)

Examples:
• Half: Behind barrel, low wall, tree
• 3/4: Arrow slit, mostly behind wall
• Full: Inside building, around corner, underground
```

---

## Combat Endings

### Victory Conditions
```
✓ All enemies defeated (HP ≤ 0)
✓ All enemies flee or surrender
✓ Objectives completed (rescue ally, escape, etc.)
```

### Defeat Conditions
```
✗ All party members at 0 HP (unconscious)
✗ Critical objective failed (ally dies, artifact destroyed)
✗ Party chooses to flee/surrender
```

### After Combat
```
1. Roll for XP (see progression_quick_ref.md)
2. Loot enemies (gold, items, equipment)
3. Tend wounds (healing, remove status effects)
4. Check for injuries/consequences
5. Continue story
```

---

## Quick Calculations

### Average Damage by Dice
```
1d4: ~2.5 damage
1d6: ~3.5 damage
1d8: ~4.5 damage
1d10: ~5.5 damage
1d12: ~6.5 damage
1d20: ~10.5 damage

2d6: ~7 damage (more consistent than 1d12)
3d6: ~10.5 damage (very consistent)
```

### Encounter Difficulty (rough)
```
Easy: 1 enemy per party member (same level)
Medium: 1.5 enemies per party member OR 1 enemy +2 levels higher
Hard: 2 enemies per party member OR 1 enemy +4 levels higher
Deadly: 3+ enemies per party member OR 1 enemy +6 levels higher
```

---

## Common Mistakes to Avoid

### ❌ WRONG
```
"The goblin attacks for... let's say 8 damage."
(No dice roll shown - LLM hallucination)
```

### ✅ CORRECT
```
"The goblin attacks: roll(1d20+3) = 16 vs your DEF 14 → HIT!
Damage: roll(1d6+2) = 5 damage."
(Transparent dice rolls visible)
```

---

**For full combat rules, see: 08_combat_resolution.md**  
**For dice mechanics, see: 11_dice_resolution.md**
