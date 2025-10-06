# Stat Frameworks Library

## Purpose

This library provides AIDM with comprehensive frameworks for **character statistics and attributes** across different anime power systems. Stats quantify character capabilities, enable mechanical resolution, and create meaningful progression.

**Coverage**: Attribute systems, derived stats, stat scaling, allocation methods, genre-specific variations

**Use This Library When**:
- Creating character during Session Zero
- Designing custom stat systems for anime worlds
- Converting anime characters to mechanical stats
- Balancing power levels across different systems
- Implementing progression mechanics

---

## Core Stat Philosophy

### Why Stats Matter

**Stats provide**:
- **Mechanical Resolution**: Objective way to resolve actions (attack vs defense)
- **Character Identity**: Stats differentiate characters (warrior vs mage)
- **Progression Tracking**: Visible growth (level 1 → level 50)
- **Balance Framework**: Prevent "god mode" without trade-offs
- **Player Agency**: Choose how to build character

**AIDM Principle**: Stats should **enable** storytelling, not replace it. Numbers serve narrative, not vice versa.

---

## Primary Attribute Systems

### 1. Classic 6-Stat System (D&D-Inspired)

**The Foundation**: Most versatile, widely understood

**Stats**:

#### **STR (Strength)** - Physical Power
- **Governs**: Melee damage, carrying capacity, physical feats
- **Skills**: Athletics, intimidation, breaking objects
- **Anime Examples**: 
  - Goku (Dragon Ball): STR 20+ (lifts mountains)
  - All Might (My Hero): STR 18+ (punch changes weather)
  - Tanjiro (Demon Slayer): STR 14 (above-average swordsman)

#### **DEX (Dexterity)** - Agility & Precision
- **Governs**: Ranged attacks, dodge, speed, initiative
- **Skills**: Acrobatics, stealth, sleight of hand
- **Anime Examples**:
  - Killua (Hunter x Hunter): DEX 20+ (FTE movement)
  - Zenitsu (Demon Slayer): DEX 18+ (Thunder Breathing speed)
  - Saitama (One Punch Man): DEX 15 (not his strong suit, but still superhuman)

#### **CON (Constitution)** - Endurance & Vitality
- **Governs**: HP, stamina, poison resistance, survival
- **Skills**: Endurance, concentration, resisting damage
- **Anime Examples**:
  - Luffy (One Piece): CON 20+ (survives impossible injuries)
  - Deku (My Hero): CON 16+ (breaks own bones repeatedly)
  - Subaru (Re:Zero): CON 8 (weak human, dies easily)

#### **INT (Intelligence)** - Knowledge & Reasoning
- **Governs**: Magic power, skill learning, strategy, puzzle-solving
- **Skills**: Arcana, investigation, tactics
- **Anime Examples**:
  - Light (Death Note): INT 20+ (genius strategist)
  - Senku (Dr. Stone): INT 20+ (scientific knowledge)
  - Shikamaru (Naruto): INT 18+ (tactical genius, IQ 200+)

#### **WIS (Wisdom)** - Perception & Insight
- **Governs**: Awareness, instinct, willpower, spiritual power
- **Skills**: Perception, insight, survival, medicine
- **Anime Examples**:
  - Jiraiya (Naruto): WIS 18+ (battle experience, sage wisdom)
  - Netero (Hunter x Hunter): WIS 20+ (enlightenment)
  - Mob (Mob Psycho): WIS 16 (emotional intelligence despite youth)

#### **CHA (Charisma)** - Force of Personality
- **Governs**: Leadership, persuasion, intimidation, inspiration
- **Skills**: Persuasion, deception, performance
- **Anime Examples**:
  - Lelouch (Code Geass): CHA 20+ (commands armies)
  - Naruto (Naruto): CHA 18+ ("talk no jutsu", changes hearts)
  - Ainz (Overlord): CHA 16+ (inspires loyalty despite being skeleton)

**Stat Ranges**:
```
1-3: Severely impaired (crippled, very young child)
4-7: Below average (weak human)
8-11: Average human
12-15: Above average (trained professional)
16-18: Exceptional (Olympic athlete, genius)
19-21: Superhuman (anime protagonist tier)
22-25: Legendary (world-class, near-mythical)
26-30: Godlike (reality-bending power)
30+: Cosmic (Saitama, Goku UI, etc.)
```

**AIDM Implementation**:
```markdown
Character Creation (Session Zero):
1. Point Buy: 27 points to distribute (max 15 in any stat before bonuses)
2. Standard Array: 15, 14, 13, 12, 10, 8 (assign to stats)
3. Roll: 4d6 drop lowest, 6 times (random but fair)

Racial/Background Bonuses: +2 to one stat, +1 to another (or +1/+1/+1)

Example:
Player chooses Point Buy: STR 15, DEX 13, CON 14, INT 8, WIS 10, CHA 12
Plus Human (+1 all stats): STR 16, DEX 14, CON 15, INT 9, WIS 11, CHA 13
```

---

### 2. Simplified 3-Stat System (Streamlined)

**Purpose**: Faster gameplay, less complexity, good for narrative-heavy campaigns

**Stats**:

#### **BODY** (Physical)
- Combines STR, DEX, CON
- Governs: All physical actions (combat, athletics, endurance)

#### **MIND** (Mental)
- Combines INT, WIS
- Governs: Magic, strategy, perception, willpower

#### **SOUL** (Social/Spiritual)
- Combines CHA, spiritual power
- Governs: Leadership, inspiration, spiritual techniques

**Stat Ranges**: 1-10 scale
```
1-2: Poor
3-4: Average
5-6: Good
7-8: Exceptional
9-10: Legendary
```

**AIDM Usage**:
```markdown
Good for: Slice-of-life, narrative-focused, beginners
Drawback: Less granular character building
```

---

### 3. Anime-Specific Stat Systems

#### A. **Dragon Ball Z Style** (Power Level)
```
Single Stat: POWER LEVEL (PL)

Ranges:
5-10: Normal human (farmer, civilian)
100-500: Trained martial artist (Krillin early DB)
1,000-5,000: Elite fighter (Raditz, early Saiyans)
10,000-100,000: Planetary threat (Frieza forms)
1,000,000+: Galactic threat (Cell, Buu)
Unmeasurable: God-tier (Goku UI, Beerus)

Formula: PL determines everything (speed, strength, durability, energy)
```

**AIDM Implementation**:
```markdown
Advantage: Simple, iconic
Drawback: Power creep issues, lacks nuance (everyone just gets stronger)
Use When: Player wants pure power fantasy escalation
```

#### B. **Hunter x Hunter Style** (Nen Stats)
```
Six Aura Types:
- Enhancement: Physical boost, healing
- Emission: Ranged attacks, projectiles
- Transmutation: Shape/property change
- Manipulation: Control objects/people
- Conjuration: Create objects
- Specialization: Unique abilities

Plus Stats:
- Aura Pool: Total Nen capacity
- Efficiency: 100% in native type, 80% adjacent, 60% opposite, 40% opposite-diagonal
- Control: Mastery of Ten, Zetsu, Ren, Hatsu

Formula: Type + Aura Pool + Conditions = Ability strength
```

**AIDM Implementation**:
```markdown
Advantage: Deep customization, strategic depth
Drawback: Complex, requires player understanding of Nen
Use When: Player wants tactical, strategic power system
```

#### C. **My Hero Academia Style** (Quirk + Stats)
```
Quirk: Unique superpower (define ability)

Base Stats (1-6 scale):
- Power: Raw strength of quirk
- Speed: Movement and reaction
- Technique: Skill and control
- Intelligence: Strategy and tactics
- Cooperativeness: Teamwork ability

Plus Gear: Support items enhance quirk/stats
```

**AIDM Implementation**:
```markdown
Advantage: Unique abilities + quantifiable growth
Drawback: Quirk can overshadow stats
Use When: Player wants superhero-style unique power
```

---

## Derived Stats (Universal)

### HP (Hit Points) - Health
```
Formula Options:

Classic: HP = (CON × 5) + (Level × CON modifier)
Example: CON 14 (+2 mod) at Level 5 = (14×5) + (5×2) = 70 + 10 = 80 HP

Simplified: HP = CON × Level × 5
Example: CON 14 at Level 5 = 14 × 5 × 5 = 350 HP

Anime (High Numbers): HP = (CON × 10) + (Level × 10)
Example: CON 14 at Level 5 = (14×10) + (5×10) = 140 + 50 = 190 HP

Genre-Specific:
- Shonen: High HP (survive many hits, dramatic comebacks)
- Seinen: Low HP (realism, lethality)
- Slice-of-life: HP optional (narrative resolution, not combat)
```

### MP (Mana/Magic Points) - Spell Resource
```
Formula Options:

Classic: MP = (INT × 5) + (Level × INT modifier)
Example: INT 16 (+3 mod) at Level 5 = (16×5) + (5×3) = 80 + 15 = 95 MP

Chakra (Naruto): MP = (INT + WIS) × 10
Example: INT 12, WIS 14 = (12+14) × 10 = 260 Chakra

Slot-Based (D&D): No MP, spell slots by level
Example: Level 5 caster = 4×1st, 3×2nd, 2×3rd level slots

Cooldown-Based (LoL): No MP, abilities have cooldowns
Example: Fireball usable once per 3 turns (no resource cost)
```

### SP (Stamina Points) - Physical Skill Resource
```
Formula Options:

Classic: SP = (CON × 3) + (Level × 2)
Example: CON 14 at Level 5 = (14×3) + (5×2) = 42 + 10 = 52 SP

Ki-Based: SP = (STR + DEX + CON) × 2
Example: STR 16, DEX 14, CON 15 = (16+14+15) × 2 = 90 Ki

Unified Pool: MP and SP are same resource (mana = stamina)
Example: Total Energy = 100, any ability costs from same pool
```

### DEF (Defense) - Damage Mitigation
```
Formula Options:

Armor Class (AC): DEF = 10 + DEX modifier + Armor bonus
Example: DEX 14 (+2), Light Armor (+2) = 10 + 2 + 2 = 14 DEF

Damage Reduction (DR): Armor reduces incoming damage
Example: Heavy Armor = -6 damage per hit (minimum 1)

Evasion (EVA): % chance to dodge
Example: DEX 18 = 30% evasion (roll 1d100, <30 = dodge)

Layered Defense: HP + Shields/Barriers (deplete shields first)
Example: 100 HP + 50 Shield = take 60 damage → 50 shield breaks, 10 HP lost
```

### SPD (Speed) - Turn Order & Movement
```
Formula Options:

Initiative: SPD = DEX modifier + 1d20 (roll each combat)
Example: DEX 16 (+3) + roll(1d20) = 3 + 14 = 17 initiative

Fixed Speed: SPD = DEX score (no randomness)
Example: DEX 16 = 16 SPD (acts before DEX 12 = 12 SPD)

Movement: Squares/feet per turn
Example: Base 30 feet, DEX 16+ = 40 feet, DEX 8- = 20 feet
```

### ATK (Attack) - Hit Chance
```
Formula Options:

To-Hit Bonus: ATK = Proficiency + Stat modifier
Example: Level 5 (+3 prof) + STR 16 (+3 mod) = +6 to hit

Roll: 1d20 + ATK vs target DEF
Example: roll(1d20+6) = 19 → hits DEF 18, misses DEF 20

Autohit: No roll, damage always applies (narrative combat)
Example: "Your sword strikes true. Roll damage: 2d6+3."
```

---

## Stat Scaling & Progression

### Linear Scaling (Predictable Growth)
```
+1 stat per level (slow, steady)
Example: Level 1 STR 14 → Level 20 STR 34

+1 stat every 4 levels (D&D 5e)
Example: Level 1 STR 14 → Level 4 STR 15 → Level 8 STR 16 → Level 20 STR 19

Advantage: Balanced, no power creep
Drawback: Less exciting, slow growth
```

### Exponential Scaling (Dramatic Growth)
```
Stats multiply by level tier
Example: 
- Tier 1 (Lv 1-10): Base stats
- Tier 2 (Lv 11-20): Stats × 1.5
- Tier 3 (Lv 21-30): Stats × 2
- Tier 4 (Lv 31-40): Stats × 3

Advantage: Dramatic power increases (shonen feel)
Drawback: Hard to balance, god-mode at high levels
```

### Milestone Scaling (Narrative Triggers)
```
Stats increase at story milestones, not levels
Example:
- Defeat rival → +2 to primary stat
- Complete training arc → +1 all stats
- Master technique → Unlock new stat (e.g., Chakra Control)

Advantage: Story-driven, meaningful
Drawback: Unpredictable, GM-dependent
```

### Soft Caps (Diminishing Returns)
```
Stats cost more points as they increase
Example Point Buy:
- 8-13: 1 point each
- 14-15: 2 points each
- 16-17: 3 points each
- 18+: 4 points each

Result: Encourages balanced builds, discourages min-maxing
```

---

## Stat Allocation Methods

### 1. Point Buy (Balanced)
```
Pool: 27 points
Range: 8-15 (before racial bonuses)
Cost: 1:1 ratio (8 costs 0, 9 costs 1, 10 costs 2, etc.)

Example:
STR 15 (9 points), DEX 14 (7 points), CON 13 (5 points)
INT 12 (4 points), WIS 10 (2 points), CHA 8 (0 points)
Total: 27 points

Advantage: Balanced, no luck involved
Use When: Fairness matters, competitive groups
```

### 2. Standard Array (Quick)
```
Assign these values: 15, 14, 13, 12, 10, 8

Example:
STR 15, DEX 13, CON 14, INT 8, WIS 10, CHA 12

Advantage: Fast, balanced
Use When: New players, quick start
```

### 3. Rolling (Random)
```
Roll 4d6, drop lowest, 6 times
Assign results to stats as desired

Example Rolls: 16, 14, 13, 12, 11, 9
Assign: STR 16, CON 14, DEX 13, CHA 12, WIS 11, INT 9

Advantage: Exciting, unique characters
Drawback: Can create weak OR overpowered characters
Use When: Players enjoy randomness, narrative > balance
```

### 4. Hybrid (Controlled Random)
```
Roll 4d6 drop lowest for 3 stats, point buy for 3 stats

Example:
Roll: STR 16, CON 14, DEX 13
Point Buy (15 points): INT 13, WIS 12, CHA 10

Advantage: Mix of excitement and control
```

---

## Genre-Specific Stat Variations

### Isekai Stats (Game-Like)
```
Extended Stats:
- LUK (Luck): Critical hit chance, loot drops, rare encounters
- FAM (Fame): NPC reactions, quest access, prices
- AFF (Affinity): Elemental/weapon specialty bonus

Status Screen:
╔══════════════════════════════════╗
║ NAME: Kazuma Satou               ║
║ LEVEL: 15   CLASS: Adventurer    ║
╠══════════════════════════════════╣
║ STR: 12   INT: 24   LUK: 99     ║
║ DEX: 18   WIS: 16   FAM: 42     ║
║ CON: 14   CHA: 11   AFF: Water  ║
╠══════════════════════════════════╣
║ HP: 450/450   MP: 280/280       ║
║ SP: 320/320   EXP: 12,450       ║
╚══════════════════════════════════╝

AIDM: Display status on request, update after level-ups
```

### Shonen Stats (Power Scaling)
```
Simplified Power Stat + Techniques:

BASE POWER: 1,200
TECHNIQUES:
- Rasengan: 300 power (costs 50 chakra)
- Shadow Clones: 4 clones (costs 100 chakra)
- Sage Mode: 2× power for 5 turns (costs 200 chakra)

TOTAL POTENTIAL: 1,200 + (300×4 clones) + (1,200×2 sage) = ~4,000 burst

AIDM: Track base power + transformations/multipliers
```

### Seinen Stats (Realistic)
```
Granular Stats:

Physical:
- Strength: 7/10 (lift 200 lbs)
- Stamina: 6/10 (run 5 miles)
- Reflexes: 8/10 (trained fighter)

Mental:
- Intelligence: 9/10 (genius)
- Willpower: 7/10 (resist torture)
- Sanity: 4/10 (PTSD, trauma)

Social:
- Charisma: 5/10 (average)
- Reputation: -3/10 (wanted criminal)

AIDM: Track mental health, reputation, realistic limits
```

### Slice-of-Life Stats (Narrative)
```
No combat stats, social/skill stats instead:

Academic: 8/10 (top student)
Athletic: 5/10 (average)
Artistic: 3/10 (can't draw)
Social: 7/10 (popular)
Charm: 9/10 (very attractive)
Cooking: 2/10 (burns water)

Relationships:
- Ayumi: 75% (close friend, developing feelings)
- Hiroshi: 60% (best friend)
- Sensei: 40% (neutral)

AIDM: Track relationships, skills, no HP/combat
```

---

## Stat Synergies & Dependencies

### Primary + Secondary Combos
```
STR + CON = Tank (high HP, heavy armor, melee)
DEX + INT = Spellblade (dodge, magic, versatility)
INT + CHA = Enchanter (buffs, social, control magic)
WIS + CHA = Cleric/Paladin (healing, leadership, inspire)

AIDM: Recognize builds, suggest synergistic skills/equipment
```

### MAD vs SAD Builds
```
MAD (Multiple Ability Dependent):
- Paladin needs STR (melee), CHA (spells), CON (survive)
- Requires spreading stats, weaker overall
- Advantage: Versatile

SAD (Single Ability Dependent):
- Wizard only needs INT (spells, defense, utility)
- Can max one stat, stronger in specialty
- Advantage: Focused, powerful

AIDM: Balance encounters for both types
```

---

## Stat Checks & DCs

### Difficulty Classes (DCs)
```
DC 5: Trivial (anyone can do it)
DC 10: Easy (untrained can succeed)
DC 15: Moderate (trained recommended)
DC 20: Hard (expert level)
DC 25: Very Hard (master level)
DC 30: Nearly Impossible (legendary)
DC 35+: Miraculous (anime protagonist moment)

Formula: 1d20 + Stat Modifier + Proficiency ≥ DC
```

### Contested Checks
```
Both sides roll: 1d20 + Modifier
Higher result wins

Example: Arm wrestling
- PC: roll(1d20+STR) = 1d20+5 = 18
- NPC: roll(1d20+STR) = 1d20+3 = 16
- PC wins!
```

---

## AIDM Implementation Guidelines

### Character Creation Workflow
```markdown
1. Choose Stat System (6-stat, 3-stat, or anime-specific)
2. Allocate Stats (point buy, array, or roll)
3. Apply Racial/Background Bonuses
4. Calculate Derived Stats (HP, MP, SP, DEF, SPD, ATK)
5. Note Stat Modifiers (for rolls)
6. Display Character Sheet
```

### During Gameplay
```markdown
Stat Checks:
- Player declares action
- AIDM determines relevant stat
- Roll: 1d20 + modifier vs DC
- Narrate success/failure

Example:
Player: "I try to lift the boulder."
AIDM: "That's a STR check. Roll 1d20+STR."
Player: roll(1d20+5) = 18
AIDM: DC 15. Success! You heave the boulder aside, muscles straining.
```

### Stat Growth
```markdown
Level-Up:
- Grant stat increases (method depends on system)
- Recalculate derived stats (HP, MP, SP)
- Update character sheet
- Narrate growth ("You feel stronger, faster, sharper.")

Temporary Buffs/Debuffs:
- Track duration (3 turns, 1 hour, until rest)
- Apply modifiers (+2 STR, -4 DEX)
- Revert when expired
```

---

## Balancing Stats

### Avoiding Min-Maxing
```markdown
Solutions:
1. Soft Caps: Diminishing returns on high stats
2. Dump Stat Consequences: Low stats create vulnerabilities
   - INT 6: Can't read, easily tricked
   - CHA 6: NPCs dislike you, poor prices
3. Varied Challenges: Force using different stats
   - Combat (STR/DEX), social (CHA), puzzles (INT)
```

### Power Budget
```markdown
Total Power = (Sum of Stats) + (Derived Stats) + (Skills) + (Equipment)

Guidelines:
- Same level characters should have ~similar total power
- Trade-offs: High offense = Low defense (glass cannon)
- Specialization: Focused > Generalist (usually)

Example:
Fighter: High STR/CON, Low INT/CHA = 80 power budget
Wizard: High INT, Medium DEX, Low STR/CON = 80 power budget
Different distributions, same total power
```

---

## Cross-Reference

**Related Libraries**:
- `leveling_curves.md` - Stat growth over levels
- `skill_taxonomies.md` - Skills tied to stats
- `power_scaling_narrative.md` - High-stat tier handling (20+ in stats)
- All power system libraries - System-specific stat variations

**Schema References**:
- `character_schema.json` - Stat storage structure
- `session_state_schema.json` - Temporary stat modifiers
- `power_system_schema.json` - Power stat integration

**Instruction Modules**:
- `06_session_zero.md` - Stat allocation during creation
- `08_combat_resolution.md` - Stat-based combat resolution
- `09_progression_systems.md` - Stat increases on level-up
- `11_dice_resolution.md` - Stat modifier rolls

---

**AIDM: Use this library to create consistent, balanced stat systems. Stats should enable interesting choices, not restrict them. Balance mechanical clarity with narrative flexibility. Remember: Numbers serve the story, not the other way around.**

**Most Important**: Stats make character capabilities tangible and progression visible. A well-designed stat system creates meaningful choices (STR or DEX?), enables fair resolution (roll + modifier vs DC), and rewards player investment (watching stats grow from 10 → 20 feels good). Use stats to empower players, not bog them down in math.
