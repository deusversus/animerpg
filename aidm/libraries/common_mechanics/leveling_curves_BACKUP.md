# Leveling Curves Library

## Purpose

This library provides AIDM with comprehensive frameworks for **character progression and experience systems** across different anime campaign types. Leveling curves determine how quickly characters grow in power, creating pacing and long-term progression arcs.

**Coverage**: XP requirements, progression speeds, level scaling, prestige systems, milestone progression, genre-specific curves

**Use This Library When**:
- Designing campaign progression pacing
- Awarding experience after encounters
- Determining level-up thresholds
- Balancing rapid vs gradual growth
- Implementing prestige/paragon systems

---

## Core Leveling Philosophy

### Why Leveling Matters

**Leveling provides**:
- **Tangible Progress**: Visible growth (Level 1 → Level 50)
- **Pacing Control**: Slow = long campaign, fast = power fantasy
- **Reward Feedback**: "You leveled up!" = dopamine hit
- **Power Gating**: Lock content behind levels (can't fight demon lord at Lv 1)
- **Narrative Milestones**: Level 10 = veteran, Level 50 = legend

**AIDM Principle**: Leveling speed should match **campaign tone** and **player expectations**.

---

## XP (Experience Points) Systems

### 1. Kill XP (Classic D&D)

**Concept**: Earn XP by defeating enemies, completing quests

**XP Awards**:
```
Enemy CR (Challenge Rating) = XP Value

CR 1/8 (Goblin): 25 XP
CR 1/4 (Kobold): 50 XP
CR 1/2 (Orc): 100 XP
CR 1 (Dire Wolf): 200 XP
CR 2 (Ogre): 450 XP
CR 3 (Wight): 700 XP
CR 5 (Air Elemental): 1,800 XP
CR 10 (Stone Golem): 5,900 XP
CR 15 (Purple Worm): 13,000 XP
CR 20 (Pit Fiend): 25,000 XP
CR 30 (Tarrasque): 155,000 XP

Formula: XP = Enemy Level² × 100
Example: Level 5 enemy = 5² × 100 = 2,500 XP
```

**Quest XP**:
```
Minor Quest: 100-500 XP
Major Quest: 1,000-5,000 XP
Story Milestone: 10,000+ XP

Example:
"Defeat bandit leader" = 1,500 XP (major quest)
"Save village from raiders" = 3,000 XP (story milestone)
```

**Party Split**:
```
Total XP ÷ Party Size = Individual XP

Example:
Defeated CR 5 Air Elemental (1,800 XP)
Party of 4: 1,800 ÷ 4 = 450 XP each
```

**AIDM Implementation**:
```markdown
After Combat:
1. Tally enemy CR values
2. Add quest XP (if applicable)
3. Divide by party size
4. Award XP: "You gain 450 XP!"
5. Check if level-up threshold reached
6. If yes → Trigger level-up sequence
```

---

### 2. Milestone Leveling (Narrative-Driven)

**Concept**: Level up at story milestones, ignore XP tracking

**Level-Up Triggers**:
```
Session Count:
- Level 2: After Session 1 (tutorial complete)
- Level 3: After Session 2-3
- Level 4: After Session 4-5
- Continue: Every 2-3 sessions = +1 level

Story Milestones:
- Defeat arc boss → +1 level
- Complete major quest → +1 level
- Survive deadly encounter → +1 level
- Master new technique → +1 level

Example Campaign (20 sessions):
Session 1: Level 1 → 2 (first quest)
Session 3: Level 2 → 3 (defeat bandit king)
Session 6: Level 3 → 4 (rescue village)
Session 9: Level 4 → 5 (tournament victory)
Session 12: Level 5 → 6 (uncover conspiracy)
Session 15: Level 6 → 7 (face betrayer)
Session 18: Level 7 → 8 (assault demon fortress)
Session 20: Level 8 → 9 (defeat demon lord)
```

**AIDM Implementation**:
```markdown
No XP tracking, just:
"You've overcome the Shadow Lord. You feel your power surge. Level up!"

Advantage: Simple, story-driven, no math
Drawback: Less granular control, no "halfway to next level" tension
Use When: Narrative > mechanics, new players, story-heavy campaigns
```

---

### 3. Session-Based Leveling (Fixed Pace)

**Concept**: Gain set XP per session, predictable progression

**XP per Session**:
```
Slow Progression: 500 XP/session
Medium Progression: 1,000 XP/session
Fast Progression: 2,000 XP/session

Level Requirements (Medium):
Level 1→2: 1,000 XP (1 session)
Level 2→3: 2,000 XP (2 sessions)
Level 3→4: 3,000 XP (3 sessions)
Level 4→5: 5,000 XP (5 sessions)

Total: 11 sessions to reach Level 5
```

**AIDM Implementation**:
```markdown
End of Session:
"You gain 1,000 XP for today's adventures. [Current: 3,500/5,000 to Level 5]"

Advantage: Predictable, fair, consistent pacing
Use When: Want reliable progression, group play
```

---

## Leveling Curves (XP Requirements)

### Linear Curve (Consistent)

**Formula**: XP Required = Level × 1,000

```
Level 1→2: 1,000 XP
Level 2→3: 2,000 XP
Level 3→4: 3,000 XP
Level 4→5: 4,000 XP
Level 5→6: 5,000 XP
...
Level 19→20: 20,000 XP

Total to Level 20: 210,000 XP
```

**Characteristics**:
- **Steady Pace**: Each level takes proportionally longer
- **Predictable**: Players can estimate progress
- **Balance**: Good for long campaigns (50+ sessions)

**AIDM Usage**:
```markdown
Good for: Traditional fantasy, balanced progression
Drawback: Can feel grindy at high levels
```

---

### Exponential Curve (Accelerating)

**Formula**: XP Required = (Level²) × 100

```
Level 1→2: 100 XP
Level 2→3: 400 XP
Level 3→4: 900 XP
Level 4→5: 1,600 XP
Level 5→6: 2,500 XP
Level 10→11: 10,000 XP
Level 15→16: 22,500 XP
Level 20→21: 40,000 XP

Total to Level 20: ~134,000 XP
```

**Characteristics**:
- **Early Fast, Late Slow**: Quick early gains, steep later
- **Dramatic**: High levels feel epic (took forever to reach)
- **Endgame Focus**: Level 15-20 is majority of campaign time

**AIDM Usage**:
```markdown
Good for: Shonen (fast start, slow mastery), long campaigns
Drawback: High levels take VERY long (can stall)
```

---

### Fibonacci Curve (Smooth Acceleration)

**Formula**: XP Required = Previous XP + XP Before That

```
Level 1→2: 100 XP
Level 2→3: 200 XP (100+100)
Level 3→4: 300 XP (200+100)
Level 4→5: 500 XP (300+200)
Level 5→6: 800 XP (500+300)
Level 6→7: 1,300 XP (800+500)
Level 7→8: 2,100 XP (1,300+800)
Level 10→11: 8,900 XP
Level 15→16: 144,000 XP

Total to Level 15: ~376,000 XP
```

**Characteristics**:
- **Natural Growth**: Smooth, organic-feeling progression
- **Balanced**: Not too fast, not too slow
- **Mathematically Elegant**: Pleasing pattern

**AIDM Usage**:
```markdown
Good for: Realistic growth, balanced campaigns
Niche: Math enthusiasts appreciate Fibonacci elegance
```

---

### Tiered Curve (Plateau System)

**Formula**: XP jumps at tier breaks, flat within tiers

```
Tier 1 (Levels 1-5): 1,000 XP per level
Tier 2 (Levels 6-10): 5,000 XP per level
Tier 3 (Levels 11-15): 10,000 XP per level
Tier 4 (Levels 16-20): 20,000 XP per level

Total to Level 20:
- Tier 1: 5,000 XP (5 levels)
- Tier 2: 25,000 XP (5 levels)
- Tier 3: 50,000 XP (5 levels)
- Tier 4: 100,000 XP (5 levels)
Total: 180,000 XP
```

**Characteristics**:
- **Clear Milestones**: Tiers = power plateaus
- **Predictable**: Know exactly how long each tier takes
- **Narrative Alignment**: Tier = story arc (Tier 1 = apprentice, Tier 4 = master)

**AIDM Usage**:
```markdown
Good for: Arc-based campaigns, clear power brackets
Advantage: Easy to balance encounters per tier
```

---

## Progression Speeds (Campaign Pacing)

### Slow Progression (Gritty, Realistic)

**Target**: Level 1-10 over 50+ sessions

**XP Requirements**:
```
Level 1→2: 2,000 XP
Level 2→3: 5,000 XP
Level 3→4: 10,000 XP
Level 4→5: 20,000 XP
Level 5→6: 35,000 XP

Sessions per Level: 5-10 sessions
Total: 50-100 sessions to max level
```

**Characteristics**:
- **Grounded**: Each level feels earned
- **Incremental**: Small, frequent improvements (skills, gear) between levels
- **Campaign Focus**: Long-term character investment

**AIDM Usage**:
```markdown
Good for: Seinen (realism), West Marches (slow burn), low magic
Drawback: Can feel grindy, impatient players may quit
Use When: Players value journey > destination
```

---

### Medium Progression (Balanced)

**Target**: Level 1-20 over 40-60 sessions

**XP Requirements**: D&D 5e standard
```
Level 1→2: 300 XP
Level 2→3: 600 XP
Level 3→4: 1,200 XP
Level 4→5: 2,100 XP
Level 5→6: 3,000 XP
Level 10→11: 14,000 XP
Level 15→16: 48,000 XP
Level 20: 355,000 XP total

Sessions per Level: 2-4 sessions average
Total: 40-60 sessions to max level
```

**Characteristics**:
- **Steady**: Regular level-ups (every few sessions)
- **Balanced**: Time to explore abilities before next level
- **Industry Standard**: Most familiar to TTRPG players

**AIDM Usage**:
```markdown
Good for: Most campaigns, balanced tone, mixed experience players
Default: Use this unless specific reason for slow/fast
```

---

### Fast Progression (Power Fantasy)

**Target**: Level 1-20 over 15-25 sessions

**XP Requirements**:
```
Level 1→2: 500 XP
Level 2→3: 1,000 XP
Level 3→4: 1,500 XP
Level 4→5: 2,500 XP
Level 5→10: 3,000 XP per level
Level 10→20: 5,000 XP per level

Sessions per Level: 1-2 sessions
Total: 15-25 sessions to max level
```

**Characteristics**:
- **Rapid Growth**: Constant level-ups, always progressing
- **Power Fantasy**: "Overpowered protagonist" feel (isekai, Solo Leveling)
- **Short Campaigns**: Burn bright, fast resolution

**AIDM Usage**:
```markdown
Good for: Isekai (rapid growth trope), short campaigns, power fantasy
Drawback: Outgrow content quickly, less time to explore abilities
Use When: Player wants Solo Leveling-style exponential growth
```

---

### Instant Progression (Narrative Jumps)

**Target**: Level up whenever dramatically appropriate

**Triggers**:
```
Defeated major villain → +3 levels
Completed training arc → +5 levels
Unlocked hidden power → +2 levels
Time skip (1 year) → +10 levels

Example Campaign:
Session 1: Level 1 (rookie adventurer)
Session 5: Defeat bandit king → Level 8 (seasoned fighter)
Session 10: Training montage → Level 20 (master warrior)
Session 15: Unlock ancient power → Level 35 (legendary hero)
Session 20: Final battle → Level 50+ (god-slayer)
```

**AIDM Usage**:
```markdown
Good for: Shonen (training arcs), cinematic campaigns, narrative > mechanics
Drawback: No XP tracking, pure GM discretion
Use When: Story-first approach, abilities matter more than levels
```

---

## Level Caps & Endgame

### Standard Level Cap (20)

**Reasoning**: D&D tradition, clear endpoint

**Power Tiers**:
```
Levels 1-4: Local Heroes (village threats)
Levels 5-10: Regional Heroes (kingdom threats)
Levels 11-16: National Heroes (continental threats)
Levels 17-20: World Heroes (planar/cosmic threats)
```

**Post-20**: Campaign ends OR switch to epic rules

---

### Extended Level Cap (50-100)

**Reasoning**: Anime protagonists grow beyond mortal limits

**Power Tiers**:
```
Levels 1-10: Street Tier (see power_scaling_narrative.md Tier 1)
Levels 11-20: City Tier (Tier 2)
Levels 21-35: National Tier (Tier 3)
Levels 36-50: Global Tier (Tier 4)
Levels 51-100: Cosmic Tier (Tier 5 - god-slayers, reality-warpers)
```

**Progression**: Exponential curve, each tier takes longer

---

### No Level Cap (Infinite Growth)

**Reasoning**: Some anime have no upper limit (Dragon Ball)

**Power Level**: Replaces traditional levels
```
Power Level 1-1,000: Mortal tier
PL 1,000-10,000: Superhuman
PL 10,000-100,000: Planetary threat
PL 100,000-1,000,000: Galactic threat
PL 1,000,000+: Universal threat
```

**AIDM Usage**:
```markdown
Track Power Level instead of discrete levels
Growth: Defeat enemy, absorb % of their PL (Saiyan zenkai boost)
Example: Defeat PL 50,000 enemy → Gain 10,000 PL (20% boost)
```

---

## Prestige & Paragon Systems

### Prestige Classes (D&D 3.5)

**Concept**: Unlock advanced classes at high levels

**Requirements**:
```
Level 10+ to qualify
Meet prerequisites (stats, skills, achievements)

Examples:
- Arcane Archer: DEX 15+, WIS 13+, Point-Blank Shot, Weapon Focus (bow), cast 1st-level arcane spells
- Dragon Disciple: Must have draconic bloodline, cast 1st-level arcane spells
- Assassin: Alignment (evil), Hide 8 ranks, Move Silently 8 ranks, Disguise 4 ranks, kill someone for money
```

**Benefit**: Specialized, powerful abilities (narrow but deep)

---

### Paragon Levels (Post-Cap)

**Concept**: After max level, earn "Paragon" levels (slow, powerful)

**XP Requirements**: 10× normal
```
Level 20→P1: 500,000 XP (50 sessions)
P1→P2: 1,000,000 XP (100 sessions)

Paragon Benefits per Level:
- +10 to all stats
- +1 Legendary Ability (resurrect dead, stop time, etc.)
- +100 HP/MP/SP
```

**AIDM Usage**:
```markdown
Endgame content for groups that won't stop playing
Paragon = god-tier (see power_scaling_narrative.md Tier 5)
```

---

### Rebirth/New Game+ (Loop System)

**Concept**: Reset to Level 1, keep some bonuses, harder enemies

**Mechanics**:
```
Reach Level 50 → Option to Rebirth
Reset to Level 1, keep:
- 10% of stats (permanent growth)
- 1 Ultimate Skill
- Titles/Achievements

New Cycle:
- Enemies 2× stronger
- New content unlocks
- Faster leveling (know what to do)

Example:
Cycle 1: Level 1-50 (100 sessions)
Cycle 2: Level 1-50 (50 sessions, harder enemies)
Cycle 3: Level 1-50 (25 sessions, brutal enemies)
```

**AIDM Usage**:
```markdown
For: Roguelike campaigns, infinite replayability
Inspired by: Dark Souls NG+, roguelikes, cultivation novels
```

---

## Genre-Specific Leveling

### Isekai Leveling (Rapid Growth)

**Pattern**: Exponential growth via cheat skills

**Curve**:
```
Session 1: Level 1 → 5 (tutorial, first quests)
Session 3: Level 5 → 15 (first dungeon)
Session 5: Level 15 → 25 (training arc)
Session 10: Level 25 → 50 (tournament victory)
Session 15: Level 50 → 75 (demon general defeated)
Session 20: Level 75 → 100 (demon lord defeated)

Growth Rate: ~5 levels per session (Accelerated model)
```

**AIDM Implementation**:
```markdown
Use Fast Progression curve
Frequent power-ups: New skills every 2-3 levels
Unique Skills: Isekai cheat abilities (Appraisal, Item Box, Auto-Translate)
```

---

### Shonen Leveling (Training Arcs)

**Pattern**: Plateaus + sudden breakthroughs

**Curve**:
```
Arc 1 (Sessions 1-5): Level 1 → 10 (apprentice)
Training Arc (Sessions 6-10): No levels, skill mastery
Arc 2 (Sessions 11-15): Level 10 → 15 (breakthrough, new technique)
Tournament Arc (Sessions 16-20): Level 15 → 20 (rivals push growth)
Power-Up (Sessions 21-25): Unlock transformation → Level 20 → 30
Final Arc (Sessions 26-30): Level 30 → 40 (master level)

Growth Pattern: Slow grind → Sudden jump (emotional breakthrough)
```

**AIDM Implementation**:
```markdown
Use Milestone Leveling
Training arcs = no levels, but unlock new skills/techniques
Breakthroughs = multiple levels at once (emotional trigger)
```

---

### Seinen Leveling (Slow, Realistic)

**Pattern**: Incremental, hard-earned growth

**Curve**:
```
Sessions 1-10: Level 1 → 3 (learn basics)
Sessions 11-20: Level 3 → 5 (first real combat)
Sessions 21-30: Level 5 → 7 (veteran status)
Sessions 31-50: Level 7 → 10 (master level)

Growth Rate: ~1 level per 5-10 sessions
```

**AIDM Implementation**:
```markdown
Use Slow Progression curve
Levels rare, precious (each one is milestone)
Growth via: Skill mastery, tactics, equipment (not stat inflation)
```

---

### Slice-of-Life Leveling (Optional)

**Pattern**: No combat levels, relationship/skill levels instead

**Curve**:
```
Relationships (1-100%):
- Gain 5-10% per meaningful interaction
- 40% = Friend
- 60% = Close Friend
- 80% = Best Friend / Romantic Interest
- 100% = Soulmate

Skills (1-10):
- Cooking: Start 2/10 → Practice → 5/10 (competent) → 8/10 (excellent)
- Academic: Start 7/10 → Study → 9/10 (top student)
```

**AIDM Implementation**:
```markdown
No XP/combat levels
Track: Relationship percentages, skill ratings
Progression: Via repeated practice, meaningful scenes
```

---

## AIDM Implementation Guidelines

### Awarding XP
```markdown
After Combat:
1. Tally enemy XP (CR × multiplier)
2. Add quest XP (if applicable)
3. Divide by party size
4. Award: "You gain 750 XP! [Current: 3,250/5,000 to Level 6]"

After Session:
1. Session XP (fixed amount)
2. Bonus XP (good RP, clever tactics, heroic moment)
3. Award: "Total session XP: 1,200. [Current: 4,450/5,000 to Level 6]"

After Milestone:
1. Narrative event (defeat boss, complete arc)
2. Award: "You've slain the Shadow Lord! +5,000 XP! LEVEL UP!"
```

### Level-Up Sequence
```markdown
1. Announce: "LEVEL UP! You are now Level 6!"
2. Grant stat increases (system-dependent)
3. Grant new abilities/skills (class features, spell slots, etc.)
4. Recalculate derived stats (HP, MP, SP)
5. Update character sheet
6. Narrate growth: "You feel your power surge. Your reflexes sharpen, your magic deepens."
```

### Tracking XP Mid-Campaign
```markdown
Display Format:
"[Current XP: 3,250 / 5,000 to Level 6]"

Update after every XP gain:
Before: [2,500 / 5,000]
Award: +750 XP
After: [3,250 / 5,000]

When level reached:
[5,000 / 5,000] → LEVEL UP! → [0 / 7,500 to Level 7]
```

---

## Cross-Reference

**Related Libraries**:
- `stat_frameworks.md` - Stats that increase on level-up
- `skill_taxonomies.md` - Skills unlocked via levels
- `power_scaling_narrative.md` - Level tiers (1-10, 11-20, 21+, etc.)
- Genre trope libraries - Genre-specific progression patterns

**Schema References**:
- `character_schema.json` - Level, XP, progression tracking
- `session_state_schema.json` - Session XP awards
- `world_state_schema.json` - Campaign level curve settings

**Instruction Modules**:
- `09_progression_systems.md` - Full progression rules
- `06_session_zero.md` - Starting level determination
- `08_combat_resolution.md` - Combat XP awards

---

**AIDM: Use this library to create satisfying progression pacing. Leveling speed should match campaign tone (slow = gritty, fast = power fantasy). Award XP transparently, celebrate level-ups dramatically. Remember: Progression is the reward for player investment—make it feel good.**

**Most Important**: Leveling is psychological reward. Each level-up should feel **earned** (via challenge) and **exciting** (new abilities, stat boosts). Balance pacing: Too slow = frustration, too fast = trivializes content. Find the sweet spot where players constantly progress BUT still have time to enjoy each power plateau before the next. The journey from Level 1 to max level IS the campaign—pace it wisely.
