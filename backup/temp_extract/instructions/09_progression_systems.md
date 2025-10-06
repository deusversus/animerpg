# Module 09: Progression Systems - Leveling & Advancement

**Version**: 2.0  
**Priority**: HIGH  
**Load Order**: After Combat Resolution

---

## Purpose

Progression Systems govern how characters grow stronger through experience. This module ensures:

1. **Fair XP Awards** - Experience matches challenge and achievement
2. **Meaningful Leveling** - Each level feels rewarding and impactful
3. **Skill Advancement** - Skills grow through use and training
4. **Build Diversity** - Multiple viable character paths
5. **Progression Pacing** - Neither too fast nor too slow

**Core Principle**: GROWTH IS EARNED, NOT GIVEN. Every level tells a story.

---

## The Progression Workflow

```
Player Completes Challenge (combat, quest, discovery, roleplay)
    ↓
1. AWARD XP (based on challenge difficulty)
    ↓
2. CHECK LEVEL-UP (has player reached threshold?)
    ↓
3. LEVEL-UP SEQUENCE (if threshold reached)
    ↓
4. DISTRIBUTE REWARDS (attribute points, skill points, new abilities)
    ↓
5. UPDATE CHARACTER STATE (apply changes atomically)
    ↓
6. NARRATIVE MOMENT (celebrate growth)
```

---

## XP Award System

### XP Sources

**COMBAT**:
```
XP = Enemy Base XP × Challenge Modifier

Base XP by Enemy Level:
• Level 1: 50 XP
• Level 2: 100 XP
• Level 3: 200 XP
• Level 4: 350 XP
• Level 5: 550 XP
• Level 6+: (Level × 100) XP

Challenge Modifier:
• Trivial (enemy 3+ levels below player): ×0.1
• Easy (enemy 1-2 levels below): ×0.5
• Fair (enemy same level ± 0): ×1.0
• Hard (enemy 1-2 levels above): ×1.5
• Deadly (enemy 3+ levels above): ×2.0
• Boss enemy: ×3.0
```

**Example**:
```
Aria (Level 5) defeats Goblin Warrior (Level 4):

Base XP: 350
Challenge: Fair (level 4 vs level 5, -1 level = Easy)
Modifier: ×0.5
Total XP: 350 × 0.5 = 175 XP

AIDM: "The goblin falls. [+175 XP]"
```

**QUESTS**:
```
XP = Quest Difficulty × Completion Quality

Quest Difficulty:
• Minor: 100 XP
• Standard: 300 XP
• Major: 750 XP
• Epic: 2,000 XP

Completion Quality:
• Partial (objectives incomplete): ×0.5
• Complete (all objectives): ×1.0
• Exceptional (bonus objectives): ×1.5
```

**Example**:
```
Quest: "Deliver Goro's Letter" (Minor quest)

Base XP: 100
Completion: Exceptional (delivered within time limit + comforted sister)
Modifier: ×1.5
Total XP: 150 XP

AIDM: "[Quest Complete: Deliver Goro's Letter]
[+150 XP (Exceptional completion)]"
```

**ROLEPLAY & DISCOVERY**:
```
• Excellent roleplay moment: 25-100 XP
• Major discovery (location, secret): 150 XP
• Solved puzzle/riddle: 50-200 XP
• Successful negotiation (avoided combat): 100 XP
• Creative problem solving: 75-150 XP
```

**Example**:
```
Player uses Life Transfer creatively to detect poison in drink (not combat use)

AIDM: "Your healing magic reacts to the poison, glowing faintly red. You 
sense the corruption in the wine.

Clever use of your abilities! [+75 XP - Creative Problem Solving]"
```

**MILESTONES**:
```
• First time using new skill: 50 XP
• Relationship milestone (NPC reaches new affinity tier): 100 XP
• Faction reputation milestone: 150 XP
• Story beat completion: 200-500 XP
```

---

## Level-Up System

### XP Requirements per Level

```
Level 1 → 2: 1,000 XP
Level 2 → 3: 2,000 XP
Level 3 → 4: 3,500 XP
Level 4 → 5: 5,500 XP
Level 5 → 6: 8,000 XP
Level 6 → 7: 11,000 XP
Level 7 → 8: 15,000 XP
Level 8 → 9: 20,000 XP
Level 9 → 10: 26,000 XP
Level 10+: (Level × 3,000) XP

RATIONALE:
• Early levels come quickly (player gets hooked)
• Mid levels slow down (player feels each level matters)
• Late levels require commitment (legendary status earned)
```

### Level-Up Rewards

**Every Level**:
```
• +10 HP
• +10 MP
• +5 SP
• +2 Attribute Points (player distributes)
• +1 Skill Point
```

**Milestone Levels** (every 5 levels):
```
Level 5, 10, 15, 20:
• Standard rewards (above)
• +1 BONUS Skill Point (total 2 skill points)
• Unlock new ability tier
• Narrative moment (power surge, vision, etc.)
```

### Level-Up Sequence

**Example: Aria reaches Level 6**

```
Current State:
• Level: 5
• XP: 7,850/8,000
• HP: 145/145
• MP: 220/220
• SP: 130/130

Player defeats boss (Captain Darius):
+1,500 XP → 9,350 XP (over threshold!)

AIDM Triggers Level-Up:

"As Captain Darius falls, something shifts within you. Power surges through 
your body - raw, electric, overwhelming.

✨ LEVEL UP! ✨

Aria: Level 5 → Level 6

[HP Maximum: 145 → 155]
[MP Maximum: 220 → 230]
[SP Maximum: 130 → 135]

You feel stronger, faster, more capable.

[+2 Attribute Points available]
[+1 Skill Point available]

How do you want to grow?

ATTRIBUTES:
• STR: 8  [+]
• DEX: 12 [+]
• CON: 14 [+]
• INT: 13 [+]
• WIS: 16 [+]
• CHA: 12 [+]

You have 2 points to distribute."
```

**Player Chooses**:
```
Player: "I put 1 point in WIS and 1 point in CON."

AIDM: "Your wisdom deepens, your resilience grows.

[WIS: 16 → 17]
[CON: 14 → 15]
[HP Maximum adjusted: 155 → 160 (CON increase = +5 HP)]

[+1 Skill Point available]

SKILLS:
Current Skills:
• Life Transfer (Unique, Level 2) - Can level to 3 [Cost: 1 point]
• Stealth (Physical, Level 2) - Can level to 3 [Cost: 1 point]
• Survival (Physical, Level 2) - Can level to 3 [Cost: 1 point]
• First Aid (Hybrid, Level 2) - Can level to 3 [Cost: 1 point]

OR

New Skills Available:
• Mana Sense (Magical, Level 1) [Cost: 1 point]
• Athletics (Physical, Level 1) [Cost: 1 point]
• Persuasion (Social, Level 1) [Cost: 1 point]

What do you choose?"
```

**Player Chooses**:
```
Player: "I level up Life Transfer to Level 3."

AIDM: "Your healing magic grows stronger. You feel the connection between 
life and energy deepen.

[Life Transfer: Level 2 → Level 3]

NEW MASTERY UNLOCKED:
• Cost Reduced: Transfer now costs 0.75 HP per 1 HP healed (was 1:1)
• Range Extended: Can heal from 2 meters away (was touch only)

[Level-Up Complete!]

Current Stats:
• Level: 6
• HP: 160/160 (full heal on level-up)
• MP: 230/230
• SP: 135/135
• XP: 1,350/11,000 (350 overflow carried forward)

You've grown stronger. The path ahead feels clearer."
```

---

## Skill Advancement

### Skill Leveling Paths

**ACTIVE LEVELING** (spend skill points):
```
Immediate, player-controlled advancement.

Cost: 1 skill point per level

Example:
Life Transfer Level 2 → Level 3: 1 skill point
Life Transfer Level 3 → Level 4: 1 skill point
```

**PASSIVE LEVELING** (through use):
```
Skills gain XP when used successfully.

Skill XP per use:
• Trivial use: +5 XP
• Standard use: +15 XP
• Challenging use: +30 XP
• Critical success: +50 XP

XP to next level:
• Level 1 → 2: 200 XP
• Level 2 → 3: 400 XP
• Level 3 → 4: 700 XP
• Level 4 → 5: 1,100 XP
• Level 5+: (Level × 250) XP
```

**Example: Stealth Skill Progression**

```
Aria (Stealth Level 2, 150/400 XP) sneaks past guards

AIDM: "You press yourself against the wall, moving silently through the shadows. 
The guards pass within meters, oblivious.

[Stealth check: Success!]
[Stealth XP: +30 (challenging use)]
[Stealth: 150 → 180 / 400 XP]"

[Many sessions later, after repeated use...]

"You slip past the final guard, silent as a ghost.

[Stealth XP: +30]
[Stealth: 390 → 420 / 400 XP]

✨ SKILL MASTERY! ✨

Your Stealth has reached Level 3 through practice!

NEW MASTERY:
• Shadow Blend: When in darkness, gain +5 to Stealth checks
• Silent Movement: No penalty to Stealth when moving quickly

[Stealth: Level 2 → Level 3]"
```

### Skill Mastery Bonuses

**Every skill has milestones at levels 3, 5, 7, 10**:

**Life Transfer Mastery**:
```
Level 1: Basic (1:1 HP cost, touch range)
Level 3: Efficient (0.75:1 cost, 2m range)
Level 5: Advanced (0.5:1 cost, 5m range, cure poison/disease)
Level 7: Expert (0.25:1 cost, 10m range, cure status effects)
Level 10: ULTIMATE (Resurrection - revive recently dead within 1 minute)
```

**Stealth Mastery**:
```
Level 1: Basic (standard stealth checks)
Level 3: Shadow Blend (+5 in darkness, silent movement)
Level 5: Expert (can hide in plain sight if distraction available, +10 in darkness)
Level 7: Master (invisibility for 1 turn after successful stealth, 1/day)
Level 10: ULTIMATE (Shadowstep - teleport 10m to any shadow, 3/day)
```

---

## Build Diversity: Character Paths

**AIDM encourages multiple playstyles** through attribute and skill choices.

### Example Builds

**COMBAT HEALER** (Aria's current path):
```
Primary Attributes: WIS, CON
Primary Skills: Life Transfer, First Aid, Combat (Basic)
Playstyle: Support/tank hybrid, heals allies while surviving frontline
```

**GLASS CANNON MAGE**:
```
Primary Attributes: INT, WIS
Primary Skills: Elemental Magic, Magic Theory, Mana Sense
Playstyle: High damage, low HP, control battlefield
```

**TANK/DEFENDER**:
```
Primary Attributes: STR, CON
Primary Skills: Shield Mastery, Taunt, Armor Proficiency
Playstyle: Protect allies, soak damage, control enemy targeting
```

**ROGUE/INFILTRATOR**:
```
Primary Attributes: DEX, CHA
Primary Skills: Stealth, Lockpicking, Persuasion
Playstyle: Avoid combat, infiltrate, negotiate, critical strikes
```

**HYBRID (Jack-of-All-Trades)**:
```
Balanced Attributes: All moderate
Diverse Skills: Mix of combat, magic, social
Playstyle: Adaptable, can handle any situation decently
```

---

## Progression Pacing

### Session-Based XP Guidelines

**Typical 2-hour session should award**:
```
• Low-activity session (roleplay-heavy): 300-500 XP
• Standard session (mix of combat/story): 600-900 XP
• High-activity session (multiple combats, major quest): 1,000-1,500 XP
• Epic session (boss fight, story climax): 2,000+ XP
```

**Level Progression Estimate**:
```
• Levels 1-3: ~2-3 sessions per level (fast, get player engaged)
• Levels 4-6: ~4-5 sessions per level (moderate, player building identity)
• Levels 7-9: ~6-8 sessions per level (slow, each level is achievement)
• Level 10+: ~10+ sessions per level (legendary, hard-earned)
```

---

## Achievements & Milestones

**Track player accomplishments for extra rewards and narrative recognition**:

### Achievement Categories

**COMBAT**:
```
• "First Blood" - First combat victory (+50 XP, unlocked automatically)
• "Boss Slayer" - Defeat first boss (+200 XP)
• "Untouchable" - Win combat without taking damage (+150 XP)
• "Combo Master" - Execute 3+ combo attacks in one fight (+100 XP)
```

**SOCIAL**:
```
• "Trusted Friend" - Reach TRUSTED status with an NPC (+100 XP)
• "Devoted Companion" - Reach DEVOTED status with an NPC (+250 XP)
• "Silver Tongue" - Successfully negotiate out of 5 combats (+150 XP)
```

**EXPLORATION**:
```
• "Discoverer" - Find 10 hidden locations (+100 XP)
• "Treasure Hunter" - Find rare/legendary item (+200 XP)
• "Lorekeeper" - Uncover 5 world secrets (+150 XP)
```

**PROGRESSION**:
```
• "Adept" - Reach Level 5 (+250 XP bonus)
• "Expert" - Reach Level 10 (+500 XP bonus, special title)
• "Master of [Skill]" - Reach skill level 10 (+300 XP)
```

**NARRATIVE**:
```
• "Hero's Sacrifice" - Save NPC at great personal cost (+200 XP)
• "Villain's Bane" - Defeat major antagonist (+500 XP)
• "World Changer" - Complete campaign-altering quest (+1,000 XP)
```

### Achievement Announcement

```
Player successfully negotiates peace between two gangs, avoiding bloodshed

AIDM: "The two gang leaders shake hands reluctantly. The tension breaks. 
Blood will not be shed today - because of you.

🏆 ACHIEVEMENT UNLOCKED: Silver Tongue 🏆
'Successfully negotiate out of 5 combats'
[+150 XP bonus]

[Current XP: 6,450 / 8,000]

Your reputation as a peacemaker grows."
```

---

## Multi-Classing (Advanced)

**At Level 10+, players can branch into secondary classes**:

### Example: Aria Multi-Classes

```
Aria reaches Level 10 (Primary Class: Healer)

AIDM: "✨ MILESTONE ACHIEVED: LEVEL 10 ✨

You've mastered the path of the Healer. But your journey doesn't end here.

You may now choose a SECONDARY CLASS to complement your abilities:

AVAILABLE CLASSES:
• Warrior (Melee combat, tanking)
• Mage (Elemental magic, arcane knowledge)
• Rogue (Stealth, critical strikes)
• Paladin (Holy magic, combat healing hybrid)
• Monk (Unarmed combat, spiritual energy)

Secondary class starts at Level 1 and levels alongside your primary.

Benefits:
• Access to new skill trees
• Hybrid abilities (combine classes)
• Build uniqueness

Choose Secondary Class OR remain pure Healer (single-class bonuses)."

Player: "I choose Paladin."

AIDM: "The path of the Paladin opens to you. Holy warrior, defender of the 
weak, healer AND fighter.

[Secondary Class: Paladin (Level 1)]
[New Skills Available: Holy Strike, Divine Shield, Righteous Fury]
[Hybrid Ability Unlocked: Healing Strike - Attack that heals you for 50% damage dealt]

Your power has diversified. The world trembles."
```

---

## Stat Caps & Diminishing Returns

**To maintain balance, attributes have caps**:

```
Soft Cap: 20 (normal maximum for mortals)
Hard Cap: 25 (requires legendary equipment/blessings)

Diminishing Returns after 18:
• Attribute 18 → 19: Costs 2 attribute points (instead of 1)
• Attribute 19 → 20: Costs 3 attribute points
• Attribute 20 → 21+: Costs 4 points + requires special quest/item
```

---

## Integration with Other Modules

Progression Systems coordinate with:

- **State Manager (03)**: Atomic updates to level, XP, attributes, skills
- **Combat Resolution (08)**: XP awards after combat
- **Narrative Systems (05)**: XP for roleplay, quests, discoveries
- **Learning Engine (02)**: Create PROGRESSION memory for milestones

---

## Module Completion Criteria

Progression Systems is successful when:

1. ✅ XP awards are fair and match challenge difficulty
2. ✅ Level-ups feel rewarding and impactful
3. ✅ Skill advancement reflects usage and training
4. ✅ Multiple character builds are viable
5. ✅ Progression pacing maintains engagement (not too fast/slow)
6. ✅ Achievements recognize player accomplishments
7. ✅ Milestones create memorable narrative moments

---

## Common Mistakes to Avoid

### ❌ WRONG: Arbitrary XP Awards

```
AIDM: "You defeated the goblin. +1,000,000 XP."
[Player jumps from Level 1 to Level 50 instantly]

Result: No sense of achievement, broken progression.
```

### ✅ CORRECT: Scaled XP Rewards

```
AIDM: "You defeated the goblin. [+50 XP]"
[Player gradually progresses, earning each level]

Result: Meaningful growth, earned power.
```

---

### ❌ WRONG: Level-Up Without Choices

```
AIDM: "You leveled up! I've automatically increased your stats."

Result: Player has no agency in character development.
```

### ✅ CORRECT: Player-Driven Advancement

```
AIDM: "You leveled up! You have 2 attribute points and 1 skill point. 
How do you want to grow?"

Result: Player shapes their character, investment increases.
```

---

**End of Module 09: Progression Systems**

*Next Module: 10_error_recovery.md (Consistency Checking & Correction)*
