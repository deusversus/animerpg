# AIDM v2.0 Library System Design

**Purpose**: Explain how libraries work, when they load, and how they support the AIDM system  
**Audience**: Developers/designers refining the library architecture  
**Date**: October 3, 2025

---

## System Overview

**Libraries are Tier 3 reference files** that provide pre-built knowledge to prevent:
1. **LLM Hallucination** - Using documented mechanics instead of guessing
2. **Research Overhead** - Avoiding web searches for common anime elements
3. **Inconsistency** - Stable, documented systems across campaigns
4. **Copyright Issues** - Generalized mechanics, not exact canon reproductions

**Key Distinction**: Libraries are **NOT** loaded by default. They are **on-demand references** triggered by specific player requests.

---

## Loading Architecture

### Three-Tier Loading System

```
TIER 1: CORE MODULES (Always Loaded ~8,000 tokens)
├── system_initialization.md    ← Bootstrap + lazy-loading orchestration
├── cognitive_engine.md          ← Intent classification
├── learning_engine.md           ← Memory management
├── state_manager.md             ← Game state tracking
├── error_recovery.md            ← Consistency checking
└── dice_resolution.md           ← Dice rolling protocol

TIER 2: BEHAVIORAL MODULES (Lazy-Loaded ~12,000 tokens when needed)
├── npc_intelligence.md          ← Loads on: SOCIAL intent
├── narrative_systems.md         ← Loads on: Story generation
├── session_zero.md              ← Loads on: Character creation
├── anime_integration.md         ← Loads on: CREATIVE intent (anime research)
├── combat_resolution.md         ← Loads on: COMBAT intent
└── progression_systems.md       ← Loads on: XP/level-up events

TIER 3: REFERENCE LIBRARIES (On-Demand, individual sections only)
├── libraries/power_systems/
│   ├── chakra_system.md         ← Loads on: Player requests chakra/Naruto mechanics
│   ├── mana_system.md           ← Loads on: Player requests traditional magic
│   ├── ki_system.md             ← Loads on: Player requests martial arts energy
│   └── unique_systems.md        ← Loads on: Player requests Nen/Stand/Quirk/Devil Fruit
├── libraries/genre_tropes/
│   ├── isekai_tropes.md         ← Loads on: Isekai campaign setup
│   ├── shonen_tropes.md         ← Loads on: Battle-focused campaign
│   ├── seinen_tropes.md         ← Loads on: Mature/complex campaign
│   └── slice_of_life_tropes.md  ← Loads on: Low-stakes, relationship-focused campaign
└── libraries/common_mechanics/
    ├── stat_frameworks.md       ← Loads on: Character creation (stat allocation questions)
    ├── leveling_curves.md       ← Loads on: Designing progression balance
    └── skill_taxonomies.md      ← Loads on: Creating custom skill systems
```

**Token Budget Impact**:
- Without libraries: Core + Behavioral = ~20,000 tokens (sustainable)
- With 1 library loaded: +2,000-3,000 tokens (still under 80%)
- Libraries **replace** web research context (which would be ~5,000+ tokens)

---

## Library Loading Flow

### Trigger: Player Requests Anime Element

**Example Scenario: Player Wants Chakra System**

```
PLAYER INPUT:
"I want to use chakra from Naruto. Can I be a ninja who uses fire jutsu?"

↓

STEP 1: COGNITIVE ENGINE (Tier 1)
Detects: CREATIVE intent (player injecting anime element)

↓

STEP 2: LAZY-LOAD ANIME_INTEGRATION.MD (Tier 2)
Loads: 07_anime_integration.md (behavioral module for research/fusion)

↓

STEP 3: SELF-ASSESSMENT (anime_integration.md internal logic)
Check: What is my familiarity with Naruto/chakra?
Result: Familiarity Level 2 (Familiar - know basics, but gaps in mechanics)

↓

STEP 4: RESEARCH AVAILABILITY CHECK
Check: Can I web_search for accurate Naruto mechanics?
Result: No web search available (or insufficient confidence)

↓

STEP 5: FALLBACK DECISION TREE (Graceful Fallback Protocol)
Option 1: Check for pre-built library
Result: ✅ chakra_system.md exists

↓

STEP 6: LOAD LIBRARY (Tier 3 - On-Demand)
Action: Load aidm/libraries/power_systems/chakra_system.md
Content Loaded: 
  • 5 nature types (Fire, Water, Earth, Wind, Lightning)
  • Hand sign mechanics
  • Chakra pool system (MP-based)
  • Jutsu framework
  • Training progression

↓

STEP 7: PRESENT TO PLAYER (Transparency Protocol)
AIDM Response:
"I have a pre-built chakra system inspired by Naruto. It includes:
• 5 basic nature types (Fire, Water, Earth, Wind, Lightning)
• Hand sign mechanics for jutsu casting
• Chakra pool management (like MP, but with nature affinities)
• Progression through training and mastery

This is a generalized system, not 100% canon Naruto. 
Does this work for you, or would you like to customize it together?"

↓

STEP 8: PLAYER CONFIRMATION
Player: "Perfect! I want to start with fire affinity."

↓

STEP 9: INTEGRATION (anime_integration.md continues)
Action: 
  • Create power_system entry in character_schema.json
  • Initialize chakra pool (base MP with fire affinity bonus)
  • Add starting jutsu (Basic Fire Release)
  • Store in memory thread (CORE: Character power system)

↓

STEP 10: LIBRARY STAYS LOADED (Session Duration)
Remains: chakra_system.md stays loaded for reference during session
Unload: If token budget >80%, can unload after session or if unused for 20+ turns
```

---

## Library Structure & Content

### Power System Libraries

**Purpose**: Pre-built anime power frameworks to avoid hallucination and web research.

**Example: chakra_system.md Structure**

```markdown
# Chakra Power System (Naruto-Inspired)

## Purpose
Generalized chakra system for AIDM campaigns inspired by Naruto.
NOT exact canon - adapted for flexible RPG use.

## Core Mechanics

### Chakra Pool
- Uses MP stat from character_schema.json
- Base pool determined by character level + CON modifier
- Regenerates with rest (full recovery) or meditation (partial)

### Nature Types (5 Basic)
1. **Fire (火)** - Offensive, burning damage
2. **Water (水)** - Defensive, healing, adaptability
3. **Earth (土)** - Defense, resilience, barriers
4. **Wind (風)** - Speed, cutting damage, ranged attacks
5. **Lightning (雷)** - Paralysis, speed burst, precision

### Nature Affinity
- Player chooses 1 primary affinity at character creation
- Primary affinity: -20% chakra cost for that nature
- Secondary affinity unlocked at level 10
- Opposing nature: +20% chakra cost

### Hand Signs
- Required for all jutsu (except basic techniques)
- Complexity scales with jutsu power:
  - Basic jutsu: 3-5 hand signs
  - Advanced jutsu: 6-10 hand signs
  - Master jutsu: 11+ hand signs
- Can be interrupted (combat mechanics integration)

### Jutsu Framework

**Basic Jutsu** (Level 1-5):
- Fire Ball Jutsu (Fire): 15 MP, 2d8 fire damage, single target
- Water Wall Jutsu (Water): 10 MP, +5 DEF for 3 turns
- Earth Spike Jutsu (Earth): 12 MP, 2d6 damage + knockback

**Advanced Jutsu** (Level 6-15):
- Phoenix Fire Jutsu (Fire): 30 MP, 4d8 fire damage, AoE 3 targets
- Water Dragon Jutsu (Water): 35 MP, 5d10 damage + DEF debuff
- Earth Golem Jutsu (Earth): 40 MP, summon defender (20 HP)

**Master Jutsu** (Level 16+):
- Fire Dragon Flame Missile (Fire): 60 MP, 8d10 fire damage, massive AoE
- Water Severing Wave (Water): 55 MP, 7d12 slashing damage, line attack
- Earth Flow Rampart (Earth): 50 MP, create massive barrier (100 HP)

## Integration with AIDM

### Character Schema Fields
```json
{
  "power_system": {
    "type": "chakra",
    "chakra_pool": {
      "current": 85,
      "max": 100,
      "regen_rate": "full_rest"
    },
    "nature_affinity": {
      "primary": "fire",
      "secondary": null,
      "opposing": "water"
    },
    "known_jutsu": [
      {"name": "Fire Ball Jutsu", "cost": 15, "mastery": "proficient"},
      {"name": "Water Wall Jutsu", "cost": 10, "mastery": "novice"}
    ]
  }
}
```

### Combat Integration
- Jutsu treated as skills (combat_resolution.md)
- Hand signs can be interrupted (opportunity attacks)
- Chakra cost deducted from MP pool (state_manager.md validates)

### Progression Integration
- Learn new jutsu through training or scrolls (progression_systems.md)
- Mastery levels: Novice → Proficient → Expert → Master
- Mastery reduces chakra cost: Expert -10%, Master -20%

## Customization Options

**Player can modify**:
- Add custom jutsu (with AIDM approval for balance)
- Change nature affinities (if narrative justification)
- Combine natures (advanced characters, level 15+)

**AIDM should NOT**:
- Create chakra mechanics not in this library (prevents drift)
- Use Naruto canon jutsu names without checking library first
- Hallucinate new nature types (stick to 5 basic + player-approved customs)

## Harmonization Notes

**Compatible with**:
- Mana system (chakra = refined mana in this world)
- Ki system (internal energy, different focus)
- Traditional classes (ninja class uses chakra, wizard uses mana)

**Incompatible with**:
- Quirks (genetic powers conflict with learned chakra techniques)
- Devil Fruits (chakra is internal, Devil Fruit is external transformation)

## Common Mistakes to Avoid

❌ **WRONG**: "You awaken your Sharingan!" (clan-specific, not in this library)
✅ **RIGHT**: "You've mastered fire nature chakra control."

❌ **WRONG**: "Your chakra pool is 500!" (broken balance)
✅ **RIGHT**: "Your chakra pool increased to 120 (level 8, CON +2)."

❌ **WRONG**: "You create a Rasengan!" (Naruto-specific, not generalized)
✅ **RIGHT**: "You develop a rotating chakra sphere technique (custom jutsu)."

---

**End of chakra_system.md**
```

---

### Genre Trope Libraries

**Purpose**: Common anime genre patterns for tone/narrative guidance.

**Example: isekai_tropes.md Structure**

```markdown
# Isekai Genre Tropes

## Common Patterns

### Truck-kun (Transportation Method)
**Description**: Sudden death/transportation to another world
**Examples**: Konosuba (tractor), Re:Zero (mugging), Overlord (game shutdown)
**AIDM Usage**: 
  • Use as campaign opening if player chooses isekai
  • Can be humorous (Konosuba style) or serious (Re:Zero style)
  • Player decides tone

### OP Protagonist (Power Fantasy)
**Description**: Protagonist starts or becomes extremely powerful
**Examples**: Overlord (godlike from start), Slime (gains power rapidly)
**AIDM Usage**:
  • Calibrate difficulty lower (player wants power fantasy)
  • Focus on spectacle over challenge
  • Narrative consequences (political attention, jealousy, responsibility)

### Guild System (Social Structure)
**Description**: Adventurer guilds with ranks, quests, rewards
**Examples**: Danmachi, Goblin Slayer, Konosuba
**AIDM Usage**:
  • Implement guild_system in world_state_schema.json
  • Rank progression (F → E → D → C → B → A → S)
  • Quest board mechanic for player agency

[... continues with more tropes]
```

---

## When Libraries ARE Loaded

### Power System Libraries

| Library | Trigger | Example |
|---------|---------|---------|
| `chakra_system.md` | Player requests Naruto-style mechanics, chakra, ninja techniques | "I want to be a ninja with chakra" |
| `mana_system.md` | Player requests traditional magic, spell schools, wizards | "I want to be a mage with mana spells" |
| `ki_system.md` | Player requests Dragon Ball-style energy, martial arts power | "I want to use ki blasts like Goku" |
| `unique_systems.md` | Player requests Nen, Stands, Quirks, Devil Fruits | "I want a Stand like JoJo" |

### Genre Trope Libraries

| Library | Trigger | Example |
|---------|---------|---------|
| `isekai_tropes.md` | Session Zero: Player chooses isekai genre | "I want an isekai adventure" |
| `shonen_tropes.md` | Session Zero: Player wants battle-focused, power-of-friendship tone | "I want a battle shonen campaign" |
| `seinen_tropes.md` | Session Zero: Player wants mature, morally complex narrative | "I want a dark, political campaign" |
| `slice_of_life_tropes.md` | Session Zero: Player wants low-stakes, relationship-focused | "I want a cozy school life campaign" |

### Common Mechanics Libraries

| Library | Trigger | Example |
|---------|---------|---------|
| `stat_frameworks.md` | Session Zero: Character creation, stat allocation questions | "How should I allocate my stats?" |
| `leveling_curves.md` | Session Zero: AIDM designing XP progression for campaign | (AIDM internal reference) |
| `skill_taxonomies.md` | Player creating custom skill or AIDM clarifying skill types | "What kinds of skills are there?" |

---

## When Libraries ARE NOT Loaded

### Player Requests Covered by Web Research

```
Player: "I want to use the Geass from Code Geass."

AIDM Check:
  • Familiarity: Level 1 (aware of Geass concept)
  • Research available: Yes (web_search enabled)
  • Pre-built library: No (too specific)

AIDM Action:
  → Research Code Geass and Geass mechanics
  → Verify findings with player
  → DO NOT load library (none exists for Geass)
```

**Reason**: Libraries are for **common, generalizable** systems. Specific anime mechanics (Geass, Alchemy from FMA, etc.) require research or player collaboration.

---

### Player Requests Known Canon Without Gaps

```
Player: "I want to use the Hunter exam format from Hunter x Hunter."

AIDM Check:
  • Familiarity: Level 4 (expert - AIDM knows Hunter exam well)
  • Research available: Not needed (already confident)
  • Pre-built library: Not needed (AIDM can handle it)

AIDM Action:
  → Use existing knowledge to create Hunter exam arc
  → DO NOT load library (unnecessary overhead)
```

**Reason**: Libraries are **fallback** for gaps in knowledge, not required when AIDM already has expertise.

---

### Simple Requests Not Needing Full System

```
Player: "I want my sword to glow blue like in anime."

AIDM Check:
  • Request: Visual flavor, not mechanical
  • Library needed: No (cosmetic detail)

AIDM Action:
  → Add visual description to weapon
  → DO NOT load library (overkill for cosmetic request)
```

**Reason**: Libraries are for **mechanical frameworks**, not cosmetic details.

---

## Library Design Philosophy

### 1. Generalized, Not Canon

**BAD Library Content** (Too specific):
```markdown
## Sharingan (Uchiha Clan Bloodline)
- Awakens from trauma
- Tomoe stages (1-tomoe, 2-tomoe, 3-tomoe)
- Mangekyo Sharingan (causes blindness)
- Amaterasu, Tsukuyomi techniques
```

**GOOD Library Content** (Generalized):
```markdown
## Ocular Powers (Visual Kekkei Genkai Template)
- Triggered by emotion or training
- Stages of mastery (Basic → Advanced → Master)
- Cost: Strain/exhaustion with heavy use
- Abilities: Enhanced perception, illusion resistance, copy techniques
- Player can flavor as Sharingan-inspired if desired
```

**Why**: Generalized content is **reusable** across campaigns and avoids copyright issues.

---

### 2. Balanced for RPG Play

**BAD Library Content** (Broken):
```markdown
## Devil Fruit: Gura Gura no Mi (Quake Fruit)
- Destroy entire islands with one punch
- No cooldown, infinite uses
- Cannot be resisted
```

**GOOD Library Content** (Balanced):
```markdown
## Devil Fruit Template: Paramecia (Environmental Manipulation)
- Unique ability (e.g., create earthquakes)
- MP cost scales with power (minor quake: 20 MP, major: 60 MP)
- Cooldown on strongest abilities (1/day limit for devastating attacks)
- Weakness: Cannot swim, -50% effectiveness in water
- Balancing: Power matches character level progression
```

**Why**: Libraries should create **fun, balanced gameplay**, not god-mode.

---

### 3. Hooks for Player Customization

**BAD Library Content** (Rigid):
```markdown
## Fire Magic
You can only use these 5 spells:
1. Fire Ball
2. Fire Wall
3. Fire Storm
4. Fire Shield
5. Fire Lance
```

**GOOD Library Content** (Flexible):
```markdown
## Fire Magic Framework
**Core Mechanics**:
- Fire spells cost 10-50 MP (scales with power)
- Deal fire damage (resist with DEF or water magic)
- Can ignite environments (create hazards)

**Example Spells**:
- Fire Ball (15 MP, 2d8 damage, single target)
- Fire Wall (20 MP, creates barrier, lasts 3 turns)
- Fire Storm (40 MP, 5d10 damage, AoE)

**Custom Spell Creation**:
Player can design fire spells with AIDM approval:
  • Follow MP cost curve (10-15 MP = basic, 40-60 MP = advanced)
  • Balance: AoE costs +50%, sustained spells cost +30%
  • Creativity encouraged (fire whip, fire clone, fire breath, etc.)
```

**Why**: Libraries are **frameworks**, not straitjackets. Player creativity > rigid rules.

---

### 4. Integration Guidance

**EVERY library should include**:

```markdown
## Integration with AIDM

### Character Schema Fields
[JSON structure for storing library mechanics]

### Combat Integration
[How this system interacts with combat_resolution.md]

### Progression Integration
[How this system scales with progression_systems.md]

### Harmonization Notes
**Compatible with**: [Other systems that work well together]
**Incompatible with**: [Systems that conflict]

## Common Mistakes to Avoid
❌ **WRONG**: [Examples of incorrect usage]
✅ **RIGHT**: [Examples of correct usage]
```

**Why**: Libraries must **integrate smoothly** with existing AIDM architecture.

---

## Library Maintenance & Expansion

### When to Create New Library

**CREATE** if:
- ✅ Element is commonly requested (3+ campaigns need it)
- ✅ Element is generalizable (not anime-specific)
- ✅ Research gaps exist (LLMs struggle with it)
- ✅ Consistency matters (players expect stable mechanics)

**DON'T CREATE** if:
- ❌ Element is rare/niche (one player asked once)
- ❌ Element is too specific (Geass, Alchemy, etc.)
- ❌ Web research works well (no knowledge gaps)
- ❌ Player collaboration is better (custom systems)

---

### Community-Contributed Libraries

**Future Enhancement** (v2.1+):
- Community can submit library files
- Reviewed for balance and quality
- Tagged by anime source, genre, popularity
- Optional downloads (players choose which to include)

**Example**:
```
Community Library: Stand System (JoJo-Inspired)
Author: CommunityUser123
Downloads: 542
Rating: 4.8/5.0
Description: "Generalized Stand mechanics with customization options"
```

---

## Token Budget Impact Analysis

### Scenario: 10-Session Campaign with Chakra System

**Without Library**:
```
Session 1: Research chakra (web_search) → +5,000 tokens
Session 3: Player asks chakra question → Research again → +3,000 tokens
Session 5: Introduce new jutsu → Research again → +2,000 tokens
Session 7: Harmonize with mana system → Re-research → +2,000 tokens

TOTAL RESEARCH OVERHEAD: ~12,000 tokens across campaign
```

**With Library**:
```
Session 1: Load chakra_system.md → +2,500 tokens
Session 1-10: Reference loaded library → 0 additional tokens
Unload if unused for 20 turns → -2,500 tokens (recoverable)

TOTAL LIBRARY OVERHEAD: ~2,500 tokens (stays loaded as needed)
```

**Savings**: ~9,500 tokens (76% reduction in anime knowledge overhead)

---

## Refinement Questions for You

Based on this design, here are questions to refine the system:

### 1. Library Scope

**Q**: Should libraries be:
- **Option A**: Highly detailed (500-800 lines each, comprehensive) → Better quality, but higher token cost
- **Option B**: Concise summaries (200-300 lines each, just frameworks) → Lower token cost, but less guidance
- **Option C**: Modular (split into sections, load only what's needed) → Most flexible, but more complex

**Current Design**: Option B (concise frameworks with customization hooks)

---

### 2. Loading Strategy

**Q**: Should libraries:
- **Option A**: Load entire file when triggered → Simpler, but wastes tokens on unused sections
- **Option B**: Load only relevant sections (e.g., just "Fire Nature" from chakra_system.md) → More efficient, but requires section extraction logic
- **Option C**: Player chooses at Session Zero which libraries to pre-load → Gives player control, but requires upfront decision

**Current Design**: Option A (entire file, but files are concise ~300 lines)

---

### 3. Customization Balance

**Q**: Should libraries:
- **Option A**: Strict mechanics (follow exactly as written) → Consistent, but rigid
- **Option B**: Suggested frameworks (AIDM can modify with player approval) → Flexible, but risks drift
- **Option C**: Core rules + player co-creation zones → Balanced guidance + creativity

**Current Design**: Option C (core mechanics stable, customization encouraged)

---

### 4. Content Priorities

**Q**: Which libraries are most critical to create first?

**Power Systems** (High Priority):
1. chakra_system.md (Naruto - most requested)
2. mana_system.md (universal fantasy magic)
3. ki_system.md (Dragon Ball - common request)
4. unique_systems.md (Nen/Stand/Quirk/Devil Fruit templates)

**Genre Tropes** (Medium Priority):
5. isekai_tropes.md (most popular anime genre)
6. shonen_tropes.md (battle-focused campaigns)
7. seinen_tropes.md (mature campaigns)
8. slice_of_life_tropes.md (low-stakes campaigns)

**Common Mechanics** (Low Priority - AIDM can improvise):
9. stat_frameworks.md (character creation guidance)
10. leveling_curves.md (progression balance)
11. skill_taxonomies.md (skill organization)

**Your Priority Order?**

---

## Summary

**Libraries are**:
- ✅ Tier 3 on-demand reference files
- ✅ Loaded when player requests specific anime element
- ✅ Generalized frameworks, not exact canon
- ✅ Designed to prevent hallucination and save research time
- ✅ Balanced for RPG play with customization hooks
- ✅ Integrated with AIDM architecture (schemas, combat, progression)

**Libraries are NOT**:
- ❌ Loaded by default (on-demand only)
- ❌ Replacements for web research (complement, not replace)
- ❌ Exact anime canon (generalized for flexibility)
- ❌ Required for AIDM to function (fallback option)

**Your Decisions Needed**:
1. Library scope (detailed vs concise)
2. Loading strategy (entire file vs sections)
3. Customization balance (strict vs flexible)
4. Content creation priority (which libraries first)

---

**Ready to discuss refinements or proceed with library creation based on this design?**
