# AIDM v2 System Architecture

## Overview

AIDM v2 is a modular instruction set architecture designed to transform high-quality LLMs into sophisticated AI Dungeon Masters for anime-inspired JRPG experiences. This document describes the complete system design, component interactions, and data flow.

---

## Design Philosophy

### Core Principles

1. **Instruction-Based, Not Code-Based**: Everything is markdown/JSON files uploaded to LLMs, not standalone software
2. **Modular by Design**: Each system operates independently but communicates through standardized interfaces
3. **State as Truth**: All game state is explicitly tracked in structured data, never assumed
4. **Fail Gracefully**: System degrades gracefully when components are unavailable
5. **Player in Control**: AI assists and enhances, never overrides player agency

### System Invariants

These rules MUST remain true across all sessions:

- **Memory Persistence**: All significant interactions are recorded in memory threads
- **State Validation**: Game state (HP, inventory, relationships) is checked for consistency
- **Intent Classification**: Every player input is analyzed before generating narrative
- **Verbatim Dialogue**: Player-spoken words are echoed exactly as written (enhanced, not changed)
- **Research Verification**: All anime research findings are confirmed with player before integration
- **Export Completeness**: Session exports contain everything needed to resume play

---

## Module Structure

### Module 1: Core AIDM Instructions
**Location**: `/aidm/CORE_AIDM_INSTRUCTIONS.md`  
**Purpose**: Master control file that governs all AIDM behavior  
**Dependencies**: None (loaded first)  
**Size Limit**: <3500 words  
**Key Responsibilities**:
- Define AIDM identity and role
- Establish behavioral rules (check instructions before EVERY reply)
- Direct to appropriate instruction modules
- Define meta-command interface
- Establish session state management protocol

**Forbidden**:
- Contains NO anime lore or specific game content
- Does NOT implement any mechanics directly
- Never references specific instruction filenames (uses concepts instead)

---

### Module 2: Cognitive Engine
**Location**: `/aidm/instructions/01_cognitive_engine.md`  
**Purpose**: Process all player input and classify intent  
**Dependencies**: None (pure processing)  
**Key Responsibilities**:
- Distinguish verbal dialogue, internal thought, meta-commands, narrative prompts
- Apply 6-stage processing pipeline (lexical → tone → context → emotion → classification → validation)
- Build player communication profiles (Drift Signature Cache)
- Detect jailbreak/manipulation attempts

**Key Files**:
- `01_cognitive_engine.md`: Complete intent classification system

**Data Flow**:
```
Player Input → Lexical Analysis → Tone Analysis → Context Check → 
Emotion Mapping → Intent Classification → Validation → Directive Output
```

---

### Module 3: Learning Engine
**Location**: `/aidm/instructions/02_learning_engine.md`  
**Purpose**: Manage memory and adapt to player behavior  
**Dependencies**: cognitive_engine (receives classified input)  
**Key Responsibilities**:
- Maintain hierarchical memory threads (Core, Character, Relationship, Quest, World, Consequence)
- Compress inactive memories when approaching token limits
- Track memory importance via Heat Index
- Self-improve through reinforcement learning patterns

**Key Files**:
- `02_learning_engine.md`: Memory management and adaptive learning
- `/aidm/schemas/memory_thread_schema.json`: Memory thread structure

**Data Flow**:
```
Classified Input → Memory Thread Creation/Update → Priority Calculation → 
Heat Index Update → Compression Check → Storage
```

---

### Module 4: State Manager
**Location**: `/aidm/instructions/03_state_manager.md`  
**Purpose**: Track all game mechanics, world state, and enable persistence  
**Dependencies**: learning_engine (stores state in memory threads)  
**Key Responsibilities**:
- Track HP/MP/SP, inventory, skills, experience
- Manage world state (time, location, factions, weather)
- Validate state consistency
- Generate session exports
- Import and reconstruct saved states

**Key Files**:
- `03_state_manager.md`: State tracking and management
- `/aidm/schemas/character_schema.json`: Player character structure
- `/aidm/schemas/world_state_schema.json`: World state structure
- `/aidm/schemas/session_export_schema.json`: Complete export format

**Data Flow**:
```
Game Events → State Updates → Validation → Memory Thread Storage → 
[On Export] → JSON Generation → Player Save File
[On Import] → JSON Parsing → Validation → State Reconstruction
```

---

### Module 5: NPC Intelligence
**Location**: `/aidm/instructions/04_npc_intelligence.md`  
**Purpose**: Realistic NPC behavior, relationships, and social networks  
**Dependencies**: cognitive_engine, learning_engine, state_manager  
**Key Responsibilities**:
- Track NPC affinity (-100 to +100) and relationship flags
- Implement reflection-based response evolution
- Simulate social network influence (faction echo system)
- Manage information propagation and knowledge boundaries

**Key Files**:
- `04_npc_intelligence.md`: NPC behavior systems
- `/aidm/schemas/npc_schema.json`: NPC data structure

**Data Flow**:
```
Player Action → Initial NPC Reaction → Reflection Process → 
Refined Response → Affinity Update → Social Network Propagation → 
Reputation Changes
```

---

### Module 6: Narrative Systems
**Location**: `/aidm/instructions/05_narrative_systems.md`  
**Purpose**: Generate emergent storytelling, manage drift, ensure consistency  
**Dependencies**: All previous modules  
**Key Responsibilities**:
- Implement narrative drift (autonomous world evolution)
- Process meta-commands (world modification, difficulty control)
- Validate narrative consistency
- Archive significant events
- Generate story hooks and complications

**Key Files**:
- `05_narrative_systems.md`: Emergent narrative framework
- `/instructions/10_error_recovery.md`: Consistency checking

**Data Flow**:
```
World State → Narrative Pressure Calculation → Event Generation → 
Player Action Integration → Consistency Validation → Archive Update
```

---

### Module 7: Session Zero System
**Location**: `/instructions/06_session_zero.md`  
**Purpose**: Guide player through character creation and world setup  
**Dependencies**: anime_integration (for research), state_manager (for initialization)  
**Key Responsibilities**:
- Conduct 5-phase setup (System Check → Calibration → World Building → Character Creation → Opening Scene)
- Gather player preferences (content, gameplay, difficulty, pacing)
- Generate initial character sheet and world state
- Create opening narrative hook

**Key Files**:
- `06_session_zero.md`: Session 0 procedures
- `/templates/session_zero_template.md`: Example flow
- `/templates/character_sheet_template.md`: Character creation template

**Data Flow**:
```
Player Start Request → Anime Research → Preference Gathering → 
World Framework → Character Creation → Initial State Generation → 
Opening Scene
```

---

### Module 8: Anime Integration
**Location**: `/instructions/07_anime_integration.md`  
**Purpose**: Research anime, fuse settings, harmonize power systems  
**Dependencies**: None (uses LLM web search)  
**Key Responsibilities**:
- Execute web research protocol for anime references
- Verify findings with player (prevent hallucinations)
- Identify fusion challenges (conflicting power systems)
- Generate power system harmonization
- Adapt to anime genres

**Key Files**:
- `07_anime_integration.md`: Research and integration protocols
- `/schemas/power_system_schema.json`: Power system framework
- `/libraries/genre_tropes/*`: Pre-built genre knowledge
- `/libraries/power_systems/*`: Power framework references
- `/templates/anime_world_template.md`: World generation guide

**Data Flow**:
```
Anime Reference → Web Search → Findings Compilation → 
Player Verification → Integration → Power System Harmonization → 
World State Creation
```

---

### Module 9: Combat & Progression
**Location**: `/aidm/instructions/08_combat_resolution.md`, `/aidm/instructions/09_progression_systems.md`  
**Purpose**: Manage tactical combat and character advancement
**Dependencies**: state_manager, npc_intelligence  
**Key Responsibilities**:
- Resolve combat encounters (turn-based or narrative)
- Track HP/MP/SP consumption and recovery
- Process skill usage and cooldowns
- Calculate experience and leveling
- Manage skill progression and mastery

**Key Files**:
- `08_combat_resolution.md`: Combat mechanics
- `09_progression_systems.md`: Leveling and advancement
- `/libraries/common_mechanics/*`: Stat frameworks, leveling curves, skill taxonomies

**Data Flow**:
```
Combat Initiation → Turn Order → Skill Usage → Damage/Effect Calculation → 
State Update → Victory/Defeat → Experience Award → Level Check → 
Skill Progression Update
```

---

### Module 10: Error Recovery
**Location**: `/instructions/10_error_recovery.md`  
**Purpose**: Detect and correct inconsistencies, handle LLM limitations  
**Dependencies**: All modules (validates their output)  
**Key Responsibilities**:
- Automated consistency checking (HP ranges, timeline, inventory)
- Player correction protocol
- Graceful degradation when anime research fails
- State repair mechanisms

**Key Files**:
- `10_error_recovery.md`: Error detection and correction
- `/tools/state_validator.py`: Python validation script

**Data Flow**:
```
State Change → Validation Checks → [If Invalid] → Flag Error → 
Request Player Correction → Apply Fix → Re-validate
```

---

## Data Flow Diagrams

### Player Input Processing
```
Player Input
    ↓
Cognitive Engine (Intent Classification)
    ├→ Verbal Dialogue → Echo in Narrative → NPC Response
    ├→ Internal Thought → Narrative Flavor (no NPC reaction)
    ├→ Meta Command → Route to Meta Interpreter
    └→ Narrative Prompt → Scene Generation
    ↓
Learning Engine (Memory Update)
    ↓
State Manager (Update Game State)
    ↓
Narrative Generator (Create Response)
    ↓
Error Recovery (Validate Output)
    ↓
Player Response
```

### Session Persistence
```
Active Play Session
    ↓
Continuous State Updates (Character, World, NPCs, Memory)
    ↓
[Player: "META: Export state"]
    ↓
State Manager → Gather All Data
    ↓
Generate JSON Export
    ↓
Player Saves Locally
    
[New Session]
    ↓
Player Pastes Saved JSON
    ↓
State Manager → Parse JSON
    ↓
Validation Check
    ↓
Reconstruct All Systems
    ↓
Resume Play
```

### Anime Integration Flow
```
Player: "I want a world like [Anime X]"
    ↓
Anime Integration → Web Research
    ↓
Compile Findings (Setting, Power System, Themes, Tropes)
    ↓
Present to Player for Verification
    ↓
Player Confirms/Corrects
    ↓
[If Multiple Anime] → Power System Harmonization
    ↓
Generate World State
    ↓
Create Power System Rules
    ↓
Initialize Factions/NPCs
    ↓
Ready for Character Creation
```

---

## External Dependencies

### Required LLM Capabilities
- **Web Search**: For anime research (Session 0 and ongoing)
- **JSON Processing**: Parse schemas, generate exports
- **Extended Context**: 32K+ tokens (128K+ recommended)
- **File Upload**: Accept instruction and schema files

### Optional LLM Capabilities
- **Image Generation**: Visual scene creation (future enhancement)
- **Code Execution**: Run state_validator.py for validation
- **Multi-turn Memory**: Better for long sessions (supplements export system)

---

## Deployment Model

AIDM v2 runs entirely within an LLM conversation. There is no server, no database, no installation.

### Deployment Steps
1. Player uploads core instructions and essential schemas to LLM
2. LLM internalizes instructions as behavioral directives
3. Player initiates Session 0
4. AIDM guides character creation and world setup
5. Play proceeds through natural conversation
6. State exported periodically for persistence
7. New sessions resume by importing saved state

### Scaling Considerations
- **Token Limits**: Use memory compression when approaching context limits
- **Session Length**: Export state after major story beats to prevent loss
- **Complexity**: Add optional instruction files only when needed (progressive loading)

---

## File Inventory

### Core Documentation (5 files)
- `README.md`: Project overview and quick start
- `docs/ARCHITECTURE.md`: This file
- `docs/SCOPE.md`: What's in/out of scope
- `docs/DEVELOPMENT.md`: Guidelines for modification
- `docs/STATE.md`: Current project status

### AIDM Project Files (33 files in `/aidm/`)

**Core Instructions (1 file)**
- `aidm/CORE_AIDM_INSTRUCTIONS.md`: Master control (<3500 words)

**Instruction Files (11 files in `/aidm/instructions/`)**
- `aidm/instructions/00_system_initialization.md`: First-load setup
- `aidm/instructions/01_cognitive_engine.md`: Intent processing
- `aidm/instructions/02_learning_engine.md`: Memory and adaptation
- `aidm/instructions/03_state_manager.md`: Game mechanics and persistence
- `aidm/instructions/04_npc_intelligence.md`: NPC behavior and relationships
- `aidm/instructions/05_narrative_systems.md`: Emergent storytelling
- `aidm/instructions/06_session_zero.md`: Character creation flow
- `aidm/instructions/07_anime_integration.md`: Research and world generation
- `aidm/instructions/08_combat_resolution.md`: Combat mechanics
- `aidm/instructions/09_progression_systems.md`: Leveling and advancement
- `aidm/instructions/10_error_recovery.md`: Consistency checking

**Schema Files (7 files in `/aidm/schemas/`)**
- `aidm/schemas/character_schema.json`: Player character structure
- `aidm/schemas/world_state_schema.json`: World and environment data
- `aidm/schemas/npc_schema.json`: NPC data structure
- `aidm/schemas/memory_thread_schema.json`: Memory storage format
- `aidm/schemas/session_export_schema.json`: Complete save file format
- `aidm/schemas/power_system_schema.json`: Power framework definition
- `aidm/schemas/anime_world_schema.json`: Anime world generation

**Library Files (12 files in `/aidm/libraries/`)**

**Genre Trope Libraries (4 files, ~10,000 lines)**:
- `aidm/libraries/genre_tropes/isekai_tropes.md` (~2,500 lines)
  - 5 isekai variants: reincarnation, summoning, gate/portal, VRMMO, reverse isekai
  - Cheat skills, status screens, guild systems, harem tropes
  - Story structures, overpowered protagonist patterns
- `aidm/libraries/genre_tropes/shonen_tropes.md` (~2,500 lines)
  - Training arcs (time-skip, gravity, mentor-student, survival)
  - Tournament arcs (single-elimination, battle royale, team battles, exams)
  - Power of friendship mechanics, rival dynamics, transformations
  - Beam clashes, mentor sacrifice, underdog heroes
- `aidm/libraries/genre_tropes/seinen_tropes.md` (~2,500 lines)
  - Psychological thriller/horror (unreliable narrators, paranoia, sanity mechanics)
  - Death games (battle royale, puzzles, gambling, werewolf formats)
  - Anti-heroes (pragmatist, avenger, sociopath, broken survivor archetypes)
  - Political intrigue, war atrocities, moral complexity, tragic arcs
- `aidm/libraries/genre_tropes/slice_of_life_tropes.md` (~2,500 lines)
  - School life (classes, clubs, exams, festivals, social hierarchies)
  - Romance (6 structures, 10 romantic moments, 7 dere archetypes)
  - Coming-of-age themes, workplace dynamics, iyashikei healing
  - Seasonal activities, relationship mechanics, vignette structures

**Power System Libraries (5 files, ~12,500 lines)**:
- `aidm/libraries/power_systems/mana_magic_systems.md` (~2,500 lines, ~30-35% anime coverage)
  - External energy manipulation, spell schools, MP management, casting mechanics
  - Examples: Fairy Tail, Black Clover, Overlord, Mushoku Tensei, Frieren
- `aidm/libraries/power_systems/ki_lifeforce_systems.md` (~2,500 lines, ~30-35% anime coverage)
  - Internal energy cultivation, chakra, Nen, Haki, breathing techniques
  - Examples: Dragon Ball, Naruto, Hunter x Hunter, One Piece, Demon Slayer
- `aidm/libraries/power_systems/soul_spirit_systems.md` (~2,500 lines, ~15-20% anime coverage)
  - Metaphysical/death powers, cursed energy, soul weapons, spiritual pressure
  - Examples: Jujutsu Kaisen, Bleach, Soul Eater, Yu Yu Hakusho, Noragami
- `aidm/libraries/power_systems/psionic_psychic_systems.md` (~2,500 lines, ~10-15% anime coverage)
  - Mental energy projection, esper systems, Geass, telekinesis, reality warping
  - Examples: Mob Psycho, Saiki K, Railgun/Index, Code Geass, Elfen Lied
- `aidm/libraries/power_systems/power_tier_reference.md` (compact tier reference)
  - OP character handling: 5 power tiers (Street → City → National → Global → Cosmic)
  - Ensemble cast pivot at Tier 4+, 3 growth models (Modest, Accelerated, Instant OP)
  - Examples: One Punch Man, Overlord, That Time I Got Reincarnated as a Slime, Solo Leveling

**Common Mechanics Libraries (3/3 Complete)** ✅:
- `aidm/libraries/common_mechanics/stat_frameworks.md` (~2,700 lines: 6-stat D&D STR/DEX/CON/INT/WIS/CHA, 3-stat BODY/MIND/SOUL, anime-specific Power Level/Nen/Quirk, derived stats HP/MP/SP/DEF/SPD/ATK, stat ranges 1-30+, allocation methods point buy/array/rolling/hybrid, genre variations isekai/shonen/seinen/slice-of-life)
- `aidm/libraries/common_mechanics/leveling_curves.md` (~2,700 lines: XP systems kill/milestone/session, curves linear/exponential/Fibonacci/tiered, speeds slow/medium/fast/instant, level caps 20/50-100/infinite, prestige classes/paragon/rebirth/NG+, genre curves isekai rapid/shonen plateaus/seinen slow/slice-of-life relationships)
- `aidm/libraries/common_mechanics/skill_taxonomies.md` (~2,700 lines: active attack/utility/buff/heal, passive stat/resistance/efficiency, ultimate signature abilities, acquisition level/points/training/trees, mastery Novice→Apprentice→Adept→Expert→Master 5 ranks, resources MP/SP/cooldowns/conditions, combos sequential/stacking, genre implementations isekai/shonen/seinen/slice-of-life, balance guidelines damage/cost/cooldowns)

**Template Files (5 files in `/aidm/templates/`)**
- `aidm/templates/session_zero_template.md`
- `aidm/templates/anime_world_template.md`
- `aidm/templates/character_sheet_template.md`
- `aidm/templates/npc_template.md`
- `aidm/templates/session_export_template.md`

### Tools (1 file)
- `tools/state_validator.py`: Python state validation

**Power System Library Design** (NEW - October 2025):
Redesigned from 4 narrow categories (chakra/mana/ki/unique) to 5 universal frameworks:
- **4 Energy Type Categories**: External (mana/magic), Internal (ki/lifeforce), Metaphysical (soul/spirit), Mental (psionic/psychic)
- **Coverage**: ~85-90% of anime power systems (vs 40% in old design)
- **Plus Power Scaling Library**: Handles OP characters (Tier 1-5 framework, ensemble cast pivot, growth models)
- **Design Philosophy**: Embrace power fantasy, not restrict it

**Total: 41 files (5 docs + 1 core + 11 instructions + 7 schemas + 12 libraries + 5 templates + 1 tool)**

---

## Version History

### v2.0 (October 2025) - Current
- Complete AIDM architecture from v1
- Anime integration and multi-fusion system
- JRPG mechanics implementation
- Session persistence via export/import
- Genre libraries and power system frameworks
- Error recovery and validation

### v1.0 (Archived: `isekairpg_old/`)
- Original Isekai RPG system
- 20 instruction files
- Lore-bound to Vantiel world
- D20-based mechanics
- Foundation for v2 architecture

---

## Success Criteria

The architecture succeeds if:

1. **Cold Start**: New player can go from zero to playable character in <10 exchanges
2. **Research Accuracy**: Anime integration correctly identifies and verifies details
3. **State Persistence**: Exported saves fully restore game across sessions/LLMs
4. **Multi-Anime Fusion**: Conflicting power systems harmonize into playable mechanics
5. **Memory Coherence**: 20+ exchanges maintain consistent NPC relationships and plot threads
6. **Error Recovery**: Inconsistencies detected and player can correct them
7. **Genre Adaptation**: Same system handles isekai, shonen, slice-of-life with appropriate tone
8. **Scalability**: System works across different LLMs with minimal modification

---

## Future Enhancements

Planned additions from AIDM Improvement Proposal:
- Constitutional AI ethics framework
- Multimodal integration (images, audio)
- Advanced emotional intelligence
- Tree-structured narrative planning
- Federated learning across sessions
- Curiosity-driven exploration mechanics

---

**This architecture provides a complete, modular foundation for AI-driven anime RPG experiences while remaining flexible enough to extend and customize.**
