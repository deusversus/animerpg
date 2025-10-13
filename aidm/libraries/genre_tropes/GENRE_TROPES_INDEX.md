# Genre Tropes Library - Master Index

**Library Version**: 1.0  
**Last Updated**: 2025-10-13  
**Total Libraries**: 15  
**Library Location**: `aidm/libraries/genre_tropes/`

---

## Purpose

**Genre trope libraries** provide structural templates, narrative patterns, and storytelling conventions for specific anime genres. Unlike narrative profiles (which calibrate tone/pacing/style), genre tropes define **what happens** in the story (arc structures, character archetypes, plot beats, world-building conventions).

**Usage**: Auto-loaded based on campaign type (see Module 13 auto-load rules) OR manually selected during Session Zero.

---

## Quick Reference Guide

**For Players (Session Zero)**: Browse by genre → Select 1-3 matching tropes → AIDM applies structural templates to campaign

**For AIDM**: 
1. Detect campaign type keywords during profile generation
2. Check auto-load triggers (Module 13)
3. Load matching genre trope libraries
4. Store in `narrative_profile.active_libraries`
5. Reference during gameplay (arc structure, plot beats, world-building)

**Format**: Files = `{genre}_tropes.md` | IDs = `{genre}_tropes`

---

## Genre Tropes Library

### Action & Combat

**shonen_tropes.md** (`shonen_tropes`):
- **Core Patterns**: Training arcs, tournament structure, power of friendship, escalating threats, rival dynamics, mentor death, "I won't give up!", declaring attacks
- **Arc Templates**: Training → Tournament → Villain Arc → Timeskip → Final Battle
- **Character Archetypes**: Hot-blooded protagonist, cool rival, mentor figure, comic relief sidekick
- **Best For**: Battle shonen campaigns (Naruto, MHA, Demon Slayer style)
- **Auto-Loaded By**: Tournament/competition campaigns

**seinen_tropes.md** (`seinen_tropes`):
- **Core Patterns**: Moral ambiguity, realistic violence consequences, political intrigue, mature themes, slow character development, pyrrhic victories
- **Arc Templates**: Setup → Complications → Moral Dilemma → Consequences → Reflection
- **Character Archetypes**: Flawed protagonist, morally grey antagonist, tragic figures
- **Best For**: Mature campaigns with complex themes (Vinland Saga, Berserk style)
- **Auto-Loaded By**: Spy/espionage, historical/period campaigns

---

### Mystery & Investigation

**mystery_thriller_tropes.md** (`mystery_thriller_tropes`):
- **Core Patterns**: Clue management, red herrings, revelation pacing, conspiracy frameworks, "just as planned" moments, cat-and-mouse dynamics
- **Arc Templates**: Mystery Established → Investigation → False Leads → Breakthrough → Confrontation → Revelation
- **Investigation Structure**: Clue tracking, evidence analysis, interview sequences, deduction scenes
- **Best For**: Detective, spy, psychological thriller campaigns (Death Note, Detective Conan style)
- **Auto-Loaded By**: Spy/espionage, detective/investigation, supernatural (if investigation focus), sci-fi (if conspiracy)

---

### Horror & Tension

**horror_tropes.md** (`horror_tropes`):
- **Core Patterns**: Atmosphere building, dread pacing, unknown threats, body horror, isolation, helplessness, jump scares vs slow dread
- **Arc Templates**: Normal Life → First Encounter → Escalation → Desperation → Climax → Aftermath
- **Tension Tools**: Environmental horror, sound design descriptions, limited information, countdown timers
- **Best For**: Horror survival campaigns (Another, Higurashi, Parasyte style)
- **Auto-Loaded By**: Horror/survival campaigns

**supernatural_tropes.md** (`supernatural_tropes`):
- **Core Patterns**: Hidden world rules, spirit lore, curses mechanics, exorcism/purification, balance between worlds, yokai/monster encyclopedias
- **Arc Templates**: Discovery → Learning Rules → First Confrontation → Training → Major Threat → Resolution
- **World-Building**: Supernatural hierarchies, curse origins, spirit types, power sources
- **Best For**: Urban fantasy, supernatural action (JJK, Bleach, Mob Psycho style)
- **Auto-Loaded By**: Supernatural/urban fantasy campaigns

---

### Comedy & Parody

**comedy_tropes.md** (`comedy_tropes`):
- **Core Patterns**: Slapstick, misunderstandings, comedic timing, bathos (undercut drama), failure comedy, awkward situations, exaggerated reactions
- **Arc Templates**: Setup → Escalating Misunderstandings → Chaos Peak → Resolution (often anticlimactic)
- **Comedy Types**: Physical comedy, wordplay, situational irony, character-based humor
- **Best For**: Comedy campaigns (Konosuba, Gintama style)
- **Auto-Loaded By**: Isekai/reincarnation (if comedic)

**slice_of_life_tropes.md** (`slice_of_life_tropes`):
- **Core Patterns**: Mundane activities, character bonding, atmosphere over plot, seasonal events, daily routines, found family
- **Arc Templates**: Introduction → Daily Life Montage → Small Conflict → Resolution → Return to Routine
- **Pacing**: Slow, contemplative, episodic, low stakes
- **Best For**: Relaxed campaigns focusing on relationships (K-On!, Mushishi style)
- **Auto-Loaded By**: Romance-focused, music/performance campaigns

---

### Isekai & Reincarnation

**isekai_tropes.md** (`isekai_tropes`):
- **Core Patterns**: Transported to another world, status screens, cheat skills, power progression, culture shock, guild systems, leveling mechanics
- **Arc Templates**: Arrival → Adaptation → Power Discovery → Guild Registration → First Quest → Escalating Adventures
- **Power Systems**: Skill trees, stat allocation, unique abilities, broken mechanics
- **Best For**: Isekai campaigns (Re:Zero, Konosuba, Overlord style)
- **Auto-Loaded By**: Isekai/reincarnation campaigns

---

### Romance & Relationships

**shoujo_romance_tropes.md** (`shoujo_romance_tropes`):
- **Core Patterns**: Love triangles, misunderstandings, confession scenes, rival love interests, childhood friends, relationship progression beats
- **Arc Templates**: Meet Cute → Growing Feelings → Obstacles → Confession → Resolution
- **Relationship Beats**: First meeting, realization, jealousy, confession, first kiss, commitment
- **Best For**: Romance-focused campaigns (Kaguya-sama, Toradora style)
- **Auto-Loaded By**: Romance-focused, magical girl (if romantic elements) campaigns

---

### Mecha & Sci-Fi

**mecha_tropes.md** (`mecha_tropes`):
- **Core Patterns**: Pilot-machine bonding, mecha customization, tactical mecha combat, military hierarchies, mecha activation sequences
- **Arc Templates**: Pilot Selection → First Sortie → Training → Major Battle → Personal Crisis → Final Battle
- **Combat Mechanics**: Mecha stats, weapon systems, energy management, formation tactics
- **Best For**: Mecha campaigns (Code Geass, Gundam, Evangelion style)
- **Auto-Loaded By**: Mecha/pilot campaigns

**scifi_tropes.md** (`scifi_tropes`):
- **Core Patterns**: Technology systems, space travel, alien encounters, dystopian themes, AI ethics, time paradoxes
- **Arc Templates**: Discovery → Investigation → Ethical Dilemma → Consequences → Resolution
- **World-Building**: Tech levels, space opera politics, cyberpunk aesthetics, transhumanism
- **Best For**: Sci-fi campaigns (Cowboy Bebop, Steins;Gate, Psycho-Pass style)
- **Auto-Loaded By**: Sci-fi/space opera campaigns

---

### Magical Girl

**magical_girl_tropes.md** (`magical_girl_tropes`):
- **Core Patterns**: Transformation sequences, team dynamics, dual identity, emotional power sources, mascot characters, friendship power-ups
- **Arc Templates**: Discovery → First Transformation → Team Formation → Major Threat → Sacrifice → Victory
- **Combat Structure**: Transformation sequences, signature attacks, combined attacks, emotional power boosts
- **Best For**: Magical girl campaigns (Sailor Moon, Madoka Magica, Precure style)
- **Auto-Loaded By**: Magical girl campaigns

---

### Historical & Period

**historical_tropes.md** (`historical_tropes`):
- **Core Patterns**: Period authenticity, historical accuracy, honor codes, class systems, political intrigue, warfare tactics
- **Arc Templates**: Political Setup → Rising Tension → Conflict → Battle → Aftermath → New Status Quo
- **World-Building**: Historical factions, period weapons/armor, social hierarchies, cultural norms
- **Best For**: Historical campaigns (Vinland Saga, Kingdom, Rurouni Kenshin style)
- **Auto-Loaded By**: Historical/period campaigns

---

### Sports & Competition

**sports_tropes.md** (`sports_tropes`):
- **Core Patterns**: Training montages, team dynamics, rivalry, underdog victories, practice = results, losses teach lessons
- **Arc Templates**: Team Formation → Training → First Match → Rivalry → Tournament → Finals
- **Match Structure**: Pre-game setup, match tension beats, comeback mechanics, teamwork moments
- **Best For**: Sports campaigns (Haikyuu, Kuroko's Basketball style)
- **Auto-Loaded By**: Tournament/competition, sports campaigns

---

### Music & Performance

**music_tropes.md** (`music_tropes`):
- **Core Patterns**: Creative process, performance mechanics, artistic growth, stage fright, ensemble dynamics, emotional expression through art
- **Arc Templates**: Formation → Practice → First Performance → Growth → Competition → Breakthrough
- **Performance Structure**: Pre-show nerves, performance descriptions, audience reactions, post-show reflection
- **Best For**: Music/band campaigns (Your Lie in April, K-On!, Bocchi the Rock style)
- **Auto-Loaded By**: Music/performance campaigns

---

## Auto-Load Trigger Reference

**Quick lookup for Module 13 auto-loading rules**:

| Campaign Type | Keywords | Auto-Load Tropes |
|--------------|----------|------------------|
| **Spy/Espionage** | spy, espionage, intelligence, secret agent, undercover | mystery_thriller + seinen |
| **Detective** | detective, investigation, murder mystery, clues | mystery_thriller |
| **Horror/Survival** | horror, survival, zombie, monster hunting | horror + mystery_thriller (if investigation) |
| **Tournament/Sports** | tournament, competition, sports, championship | shonen + sports |
| **Isekai** | isekai, reincarnation, transported, game world | isekai + comedy (if comedic) OR seinen (if serious) |
| **Mecha** | mecha, giant robot, pilot, mobile suit | mecha + scifi |
| **Magical Girl** | magical girl, transformation, guardian | magical_girl + shoujo_romance (if romantic) |
| **Romance** | romance, love story, dating, harem | shoujo_romance + slice_of_life |
| **Supernatural** | supernatural, yokai, spirits, curses, exorcist | supernatural + mystery_thriller (if investigation) |
| **Historical** | historical, samurai, feudal, warring states | historical + seinen |
| **Music** | music, band, idol, performance | music + slice_of_life OR shoujo_romance |
| **Sci-Fi** | space, futuristic, cyberpunk, dystopia | scifi + mystery_thriller (if conspiracy) |

---

## Usage Patterns

### Pattern 1: Campaign Type Determines Core Tropes

**Example**: Player requests "detective noir campaign"
1. Module 13 detects keywords: "detective"
2. Auto-loads: `mystery_thriller_tropes.md`
3. AIDM applies: Clue management, red herrings, revelation pacing
4. Campaign uses mystery arc templates for quest structure

### Pattern 2: Narrative Profile + Genre Tropes = Complete System

**Example**: Player selects "Death Note profile + mystery_thriller tropes"
- **Profile provides**: Tone (serious), pacing (strategic), dialogue (inner monologue), scales (tactical 10/10)
- **Tropes provide**: Investigation structure, clue tracking, cat-and-mouse beats, "just as planned" moments
- **Result**: Authentic psychological thriller campaign

### Pattern 3: Multiple Tropes for Hybrid Genres

**Example**: Player requests "supernatural detective campaign"
1. Module 13 detects: "supernatural" + "detective"
2. Auto-loads: `supernatural_tropes.md` + `mystery_thriller_tropes.md`
3. AIDM applies: Spirit lore + clue management, curse investigation structure
4. Campaign blends both genre conventions

### Pattern 4: Tropes Override Generic Mechanics

**Example**: Campaign uses `isekai_tropes.md`
- **Generic**: "You gain a level" → Generic XP system
- **With Isekai Tropes**: "STATUS SCREEN: LEVEL UP! +5 STR, +3 AGI. New Skill Unlocked: [Shadow Step]" → Status screen UI, skill trees, visible stats
- **Difference**: Tropes add genre-specific presentation and mechanics

---

## Blending Tropes (Advanced)

**Compatible Combinations**:
- ✅ `mystery_thriller` + `supernatural` (supernatural detective)
- ✅ `seinen` + `historical` (mature period drama)
- ✅ `shonen` + `sports` (competitive battle tournament)
- ✅ `comedy` + `isekai` (parody isekai like Konosuba)
- ✅ `shoujo_romance` + `slice_of_life` (romance daily life)
- ✅ `horror` + `mystery_thriller` (horror investigation)

**Incompatible Combinations** (tonal clash):
- ❌ `comedy` + `horror` (unless intentional horror-comedy)
- ❌ `slice_of_life` + `shonen` (conflicting pacing: slow vs fast)
- ❌ `shoujo_romance` + `seinen` (conflicting tone: light vs dark)

**Blending Guidelines**:
1. Choose **1 primary trope** (dominant structure)
2. Add **1-2 secondary tropes** (specific elements)
3. Avoid tonal contradictions
4. Use primary trope's arc templates, secondary trope's specific mechanics

---

## Integration with Module 13 (Narrative Calibration)

**Relationship**:
- **Narrative Profiles** (e.g., Death Note profile) = **HOW** story is told (tone, pacing, dialogue style)
- **Genre Tropes** (e.g., mystery_thriller_tropes.md) = **WHAT** happens in story (arc structure, plot beats)

**Example Integration**:
```
Player: "I want Death Note vibes with detective mystery"

AIDM Process:
1. Load Death Note profile → Extract tone (serious), pacing (strategic), dialogue (inner monologue)
2. Auto-load mystery_thriller_tropes.md → Extract investigation structure, clue management
3. Combine: Strategic inner monologue + clue tracking + "just as planned" moments
4. Result: Psychological thriller detective campaign with Death Note feel
```

**Storage**:
- Narrative profile scales/tropes: `narrative_profile_schema.json`
- Active genre tropes: `narrative_profile.active_libraries: ["mystery_thriller_tropes", "seinen_tropes"]`
- Referenced during: Arc planning (Module 05), world-building (Module 03), quest structure (Module 04)

---

## Module References

**Module 13 (Narrative Calibration)**:
- Lines 243-335: Genre Library Auto-Loading Rules
- Uses this index to determine which trope libraries to load based on campaign keywords

**Module 01 (Cognitive Engine)**:
- Lines 285-291: Genre Library Selection (narrative profile integration)
- References trope libraries when applying narrative profiles

**Module 05 (Narrative Systems)**:
- Uses loaded genre tropes for arc structure templates
- References during quest generation, plot beat timing, world-building

**Module 00 (System Initialization)**:
- Should reference this index during initial load (TODO: Add reference)

---

## File Structure

```
aidm/libraries/genre_tropes/
├── comedy_tropes.md           (comedy_tropes)        [Slapstick, misunderstandings, bathos]
├── historical_tropes.md       (historical_tropes)    [Period authenticity, honor codes]
├── horror_tropes.md           (horror_tropes)        [Atmosphere, dread pacing, unknown threats]
├── isekai_tropes.md           (isekai_tropes)        [Status screens, cheat skills, guilds]
├── magical_girl_tropes.md     (magical_girl_tropes)  [Transformation, team dynamics, dual identity]
├── mecha_tropes.md            (mecha_tropes)         [Pilot bonding, tactical combat, activation]
├── music_tropes.md            (music_tropes)         [Creative process, performance, growth]
├── mystery_thriller_tropes.md (mystery_thriller_tropes) [Clue management, revelation pacing]
├── scifi_tropes.md            (scifi_tropes)         [Tech systems, space travel, dystopia]
├── seinen_tropes.md           (seinen_tropes)        [Moral ambiguity, realistic violence]
├── shonen_tropes.md           (shonen_tropes)        [Training arcs, power of friendship]
├── shoujo_romance_tropes.md   (shoujo_romance_tropes) [Love triangles, confession scenes]
├── slice_of_life_tropes.md    (slice_of_life_tropes) [Mundane activities, daily routines]
├── sports_tropes.md           (sports_tropes)        [Training montages, rivalry, teamwork]
├── supernatural_tropes.md     (supernatural_tropes)  [Spirit lore, curses, hidden world]
└── GENRE_TROPES_INDEX.md      (This file - master index)
```

**Total**: 15 genre trope libraries  
**Estimated Size**: ~3,000-5,000 words per library (~45,000-75,000 words total)  
**Estimated Tokens**: ~60,000-100,000 tokens (entire library)

---

## Common Mistakes

**❌ Mistake 1: Confusing Profiles with Tropes**
- Wrong: "Load Death Note profile" → Expect clue management structure
- Right: "Load Death Note profile (tone/pacing) + mystery_thriller_tropes (structure)"

**❌ Mistake 2: Overloading Tropes**
- Wrong: Load 5+ trope libraries simultaneously
- Right: 1 primary + 1-2 secondary tropes maximum

**❌ Mistake 3: Ignoring Tonal Clashes**
- Wrong: comedy + horror without intentional horror-comedy setup
- Right: Check compatibility table before blending

**❌ Mistake 4: Static Trope Usage**
- Wrong: Load tropes at Session Zero, never adjust
- Right: Can add/remove tropes mid-campaign (e.g., comedy campaign becomes serious → add seinen, remove comedy)

---

## Future Enhancements

### Priority 1: Add Trope Content Examples
- Each trope library should include 3 example scenarios
- Show how tropes apply to actual gameplay

### Priority 2: Create Trope Cheat Sheets
- Quick reference cards for each trope
- Key patterns, arc templates, character archetypes

### Priority 3: Add Cross-Genre Blending Recipes
- Pre-tested combinations (e.g., "Supernatural Detective" = supernatural 60% + mystery_thriller 40%)
- Recommended primary/secondary splits

### Priority 4: Integration with Module 05 (Narrative Systems)
- Explicit trope references in arc generation
- Template system for applying trope structures

---

## Completion Checklist

**For AIDM (Module 13 integration)**:
- ✅ Check campaign keywords during Session Zero
- ✅ Match keywords to auto-load triggers (see table above)
- ✅ Load matching genre trope libraries
- ✅ Store in `narrative_profile.active_libraries`
- ✅ Reference during arc planning (Module 05)
- ✅ Apply trope-specific structures (investigation beats, tournament brackets, etc.)

**For Players (Session Zero)**:
- ✅ Browse genre tropes by category
- ✅ Select 1-3 matching campaign tone/structure
- ✅ Confirm with AIDM (auto-loaded or manual selection)
- ✅ Understand trope patterns will guide story structure

---

**End of Genre Tropes Index**  
**For trope library content, open individual `.md` files in `aidm/libraries/genre_tropes/` directory**
