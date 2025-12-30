# AIDM Instruction Files - Comprehensive Analysis

This document provides a structured analysis of all 14 instruction files found in `aidm/instructions/`. Each file defines a module for an AI Dungeon Master (AIDM) system designed for anime-themed tabletop RPG experiences.

---

## Overview

| File | Core Purpose | Lines | Words |
|------|-------------|-------|-------|
| 00_system_initialization.md | System startup and module loading | 123 | 802 |
| 01_cognitive_engine.md | Intent parsing and response generation | 646 | 4,476 |
| 02_learning_engine.md | Memory management with heat-based prioritization | 325 | 2,054 |
| 03_state_manager.md | Data validation, schemas, and state persistence | 1,595 | 6,122 |
| 04_npc_intelligence.md | NPC behavior, affinity, and ensemble management | 444 | 3,333 |
| 05_narrative_systems.md | Story generation, foreshadowing, and pacing | 1,162 | 6,761 |
| 06_session_zero.md | Character creation workflow | 921 | 4,997 |
| 07_anime_integration.md | External research and anime harmonization | 1,353 | 6,568 |
| 08_combat_resolution.md | Turn-based combat mechanics | 882 | 4,811 |
| 09_progression_systems.md | XP, leveling, and skill advancement | 739 | 3,838 |
| 10_error_recovery.md | Validation, error handling, and recovery | 360 | 2,223 |
| 11_dice_resolution.md | Dice rolling protocols and transparency | 101 | 1,085 |
| 12_narrative_scaling.md | Power imbalance and OP protagonist handling | 440 | 3,106 |
| 13_narrative_calibration.md | Tone/style profiles and mechanical scaffolding | 610 | 3,257 |

---

## File-by-File Analysis

---

### 00_system_initialization.md

**Core Purpose**: Defines the boot sequence for the AIDM system, including schema validation, module loading order, and session detection.

**Key Features**:
- 7-step initialization sequence: Schema Validation → Module Loading → Session Detection → State Restoration → New Game Setup → System Health Check → Ready State
- 3-tier lazy-load protocol for modules:
  - **Tier 1 - Critical Systems**: Core modules loaded immediately
  - **Tier 2 - Optional Systems**: Loaded on demand
  - **Tier 3 - Reference Libraries**: Genre tropes and narrative profiles
- Schema validation for 15+ data structures (character, quest, world_state, economy, crafting, progression, etc.)

**Sub-systems/Components**:
- Schema validation pipeline
- Module loader with lazy-load protocol
- Session detection (new vs continuing)
- State restoration system
- Version migration handler
- Emergency recovery protocol

**Integration Points**:
- References `06_session_zero.md` for new game setup
- References `01_cognitive_engine.md` for load sequence
- Loads schemas from `aidm/schemas/*.json`
- Loads libraries from `aidm/libraries/*.md`

---

### 01_cognitive_engine.md

**Core Purpose**: The "brain" of the system - handles player input parsing, intent classification, and response orchestration across all other modules.

**Key Features**:
- **Intent Taxonomy** with 7 categories: NARRATIVE, MECHANICAL, SOCIAL, META, CREATIVE, EXPLORATION, COMBAT
- **Player Agency Protection** ("Sacred Rule"): Never assume player choices, always stop at decision points
- **Coherence Validation** system with 4 categories:
  - Power tier coherence
  - Archetype consistency
  - World rule coherence
  - Narrative profile alignment
- **Response Layer Separation**: Narrative/System/Mechanical outputs structured differently
- Multi-intent handling for complex player actions
- Complexity assessment for routing

**Sub-systems/Components**:
- Intent classification engine
- Deep read protocol (100% input comprehension)
- Memory check integration (last 5 turns)
- State validation before action
- Coherence warning system
- Decision point detection

**Integration Points**:
- **Module 02 (Learning)**: Retrieve memories, narrative style preferences
- **Module 03 (State)**: Validate actions against world state
- **Module 04 (NPC)**: Route social intents
- **Module 05 (Narrative)**: Generate story responses
- **Module 08 (Combat)**: Combat action processing
- **Module 12 (Narrative Scaling)**: Power tier context
- **Module 13 (Narrative Calibration)**: Load/apply narrative profiles

---

### 02_learning_engine.md

**Core Purpose**: Memory management system with hierarchical storage and heat-based prioritization for relevant information retrieval.

**Key Features**:
- **Heat Index System** (0-100): Determines memory relevance and retrieval priority
  - ACTIVE (Hot): 70-100, immediate access
  - WARM (Medium): 30-69, quick retrieval
  - ARCHIVED (Frozen): 0-29, compressed storage
- **8 Memory Categories**:
  1. CORE (Immutable) - Campaign constants
  2. CHARACTER_STATE (Mutable) - Current status
  3. RELATIONSHIPS - NPC interaction history
  4. QUESTS - Progression tracking
  5. WORLD_EVENTS - Environmental changes
  6. CONSEQUENCES - Ripple effects
  7. NARRATIVE_STYLE - Tone/pacing adjustments
  8. FACTION_DYNAMICS - Political changes

**Sub-systems/Components**:
- Memory creation protocol with JSON schema
- Heat decay system (none/slow/normal/fast rates)
- Memory retrieval algorithm (trigger → search → filter → rank)
- Memory compression for old/low-heat memories
- Conflict resolution (priority ranking)
- Special memory types:
  - Player-initiated (explicit "remember this")
  - Hidden memories (character knows, player hasn't discovered)
  - Player feedback memories (immediate application)
  - Narrative scale context memories
  - OP protagonist mode memories

**Integration Points**:
- **Module 03 (State Manager)**: State validates vs schemas, archives to session_export
- Faction operations: `create_faction`, `update_faction`, `modify_reputation`

---

### 03_state_manager.md

**Core Purpose**: Central data management layer - validates all state changes, manages schemas, handles save/load operations, and integrates mechanical systems.

**Key Features**:
- **Pre-Commit Validation Hooks**: Every state change validated before execution
- **Change Log Format**: Atomic transactions with before/after values and rollback capability
- **Narrative Profile State Tracking**: Pre-made vs generated profile handling
- **Mechanical Systems Integration** (Phase 4):
  - Economy system (currency operations, loot generation)
  - Crafting system (recipes, materials, skill checks)
  - Progression system (mastery tiers, class-based, quirk awakening, milestone, static OP)
  - Downtime system (training arcs, social links)

**Sub-systems/Components**:
- State architecture with world_state.mechanical_systems
- Schema validation (character_schema, world_state_schema, etc.)
- Export/import handling for save files
- Mechanical system instantiation flow
- Currency operations and transaction validation
- Rollback protocol (single change, multi-change transaction, cascade failure)
- Token optimization via compact Change Log format
- Safe array modification protocol

**Integration Points**:
- **Module 13**: Session Zero profile loading
- **Module 04 (NPC)**: Social links modify relationships
- **Module 05 (Narrative)**: Downtime scenes, crafting narratives
- **Module 09 (Progression)**: Training arcs, skill improvements
- **Module 12 (Narrative Scaling)**: Challenge adjustment by progression type

---

### 04_npc_intelligence.md

**Core Purpose**: Governs NPC behavior, personality persistence, relationship tracking, and ensemble cast management for overpowered protagonists.

**Key Features**:
- **Affinity & Disposition System**:
  - Character Affinity (-100 to +100): Personal relationship
  - Faction Reputation (-1000 to +1000, normalized): Public standing
  - Faction Relationship Modifier (-50 to +50): Inter-faction politics
  - Disposition Formula: 60% affinity + 40% normalized reputation + modifier
- **Knowledge Boundaries**: NPCs have realistic expertise limits
- **Behavior Generation**: Dialogue style, reaction patterns, decision-making
- **Ensemble Cast Management** (for OP protagonist scenarios):
  - 7 Archetypes: Struggler, Heart, Skeptic, Dependent, Equal, Observer, Rival
  - Spotlight tracking (scene_count per NPC)
  - Growth stages: Introduction → Bonding → Challenge → Growth → Mastery

**Sub-systems/Components**:
- NPC schema (core_identity, knowledge, behavior, relationships, narrative_role, current_state)
- Cognitive evolution stages (Reactive → Contextual → Anticipatory → Autonomous)
- Cognitive bias system (trauma, cultural, belief biases)
- Emotional milestone tracking ("firsts" that make bonds organic)
- Parallel nemesis progression (rivals grow independently)
- Bonded entity framework (familiars, creatures, spirits)

**Integration Points**:
- **Module 03 (State)**: Stores NPCs in world_state.npcs[]
- **Module 02 (Learning)**: Creates RELATIONSHIP memory threads
- **Module 05 (Narrative)**: Scene generation, spotlight balancing

---

### 05_narrative_systems.md

**Core Purpose**: Drives story generation, maintains narrative coherence, implements foreshadowing, manages faction dynamics, and handles ensemble storytelling.

**Key Features**:
- **6 Core Principles**:
  1. Player Agency (Golden Rule)
  2. Emergent Narrative
  3. Consequence Chains
  4. Story Hooks
  5. Pacing
  6. "Yes, And..." improv approach
- **Foreshadowing Protocol**: Every scene contains 1-2 foreshadowing elements
  - Environmental hints (specific details that matter later)
  - NPC dialogue hooks (mentions of future events/people/places)
- **Faction-Based Narrative**:
  - Faction goal system
  - Reputation-gated quests
  - Dynamic world events (faction conflicts, power shifts)
- **Ensemble Cast Management** (when PC power >> party):
  - Spotlight rotation protocol
  - Reverse Ensemble mode (NPCs become viewpoint characters)
  - Archetype-specific scene focus

**Sub-systems/Components**:
- Narrative voice calibration
- Quest generation workflow
- Callback protocol (referencing planted seeds)
- Power-appropriate narrative generation
- Downtime activity system (6 modes):
  - Training arcs
  - Social links
  - Investigation/research
  - Guild/party activities
  - Faction missions
  - Personal projects

**Integration Points**:
- **Module 04 (NPC)**: NPCs drive story, ensemble archetypes assigned there
- **Module 02 (Learning)**: Story beats become QUEST and WORLD_EVENT memories
- **Module 03 (State)**: Consequences update world_state
- **Module 09 (Progression)**: Narrative milestones trigger XP
- **Module 12 (Narrative Scaling)**: Power imbalance triggers ensemble mode
- **Module 13 (Narrative Calibration)**: DNA scales filter tone/pacing

---

### 06_session_zero.md

**Core Purpose**: Comprehensive character creation workflow with 5+ phases, including media research, narrative calibration, and OP protagonist detection.

**Key Features**:
- **5-Phase Process**:
  1. **Phase 0**: Media Reference Detection (mandatory gate)
  2. **Phase 0.5**: Narrative Calibration (tone/storytelling style)
  3. **Phase 0.6**: OP Protagonist Mode Detection
  4. **Phase 0.7**: Mechanical System Loading
  5. **Phases 1-5**: Concept → Identity → Mechanical Build → World Integration → First Scene

**Sub-systems/Components**:
- **Media Detection Protocol**: Scans for anime titles, power systems, character names
- **Research Protocol**: External verification via VS Battles Wiki, Fandom wikis, MAL, Reddit
- **Narrative Profile Selection**: Pre-made library (13+ profiles) or custom generation
- **OP Protagonist Mode**:
  - 9 Archetypes: Saitama, Mob, Overlord, Saiki K, Mashle, Wang Ling, Vampire D, Slime/Rimuru, Deus
  - Archetype-specific technique loading
- **Spartan Mode**: Compressed workflow for experienced players
- **Mechanical System Classification**: Economy, crafting, progression, downtime

**Integration Points**:
- **Module 07 (Anime Integration)**: External research execution
- **Module 13 (Narrative Calibration)**: Profile loading/generation
- **Module 03 (State Manager)**: Stores narrative_profile in character_schema

---

### 07_anime_integration.md

**Core Purpose**: Handles external research for anime elements, ensures accurate power systems and lore integration, and generates narrative profiles for unfamiliar content.

**Key Features**:
- **6-Step Workflow**:
  1. Self-Assessment (knowledge verification)
  2. Research Protocol (filling gaps)
  3. Mechanical System Classification (economy/crafting/progression/downtime)
  4. Verification (confirming understanding)
  5. Harmonization (making it fit campaign)
  6. Tracking (maintaining consistency)
- **Knowledge Familiarity Scale** (L0-L4):
  - L0 UNKNOWN: Full research or decline
  - L1 AWARE: Extensive research
  - L2 FAMILIAR: Targeted research
  - L3 PROFICIENT: Minimal verification
  - L4 EXPERT: Integrate directly
- **Research Extraction** (3 phases): Mechanics → Narrative DNA → Mechanical Config

**Sub-systems/Components**:
- Self-assessment protocol
- FORBIDDEN behaviors (auto-fail conditions)
- Research methods: Direct player collaboration, acknowledge limitations, propose research session
- Harmonization framework (lore, power balance, genre consistency, cross-system interaction)
- Consistency tracking system
- Regression & time-loop mechanics handling
- Multiple anime integration rules

**Integration Points**:
- **Module 00 (System Init)**: References initialization procedures
- Loads genre libraries: `shonen_tropes.md`, `seinen_tropes.md`, etc.
- Power system schemas: `power_system_schema.json`

---

### 08_combat_resolution.md

**Core Purpose**: Comprehensive combat mechanics including turn order, damage calculation, boss battles, death & resurrection, and tier-appropriate narration.

**Key Features**:
- **Combat Types**:
  - Standard (turn-based tactical)
  - Narrative (drama over mechanics)
  - Quick Resolution (trivial encounters)
- **Pre-Combat Validation Protocol**: 5 steps - Resource, Prerequisite, Calculation, State Update, Narrative
- **Combat Narration** (profile-driven):
  - strategy_vs_spectacle (0-10)
  - power_explanations (ON/OFF)
  - sakuga_moments (ON/OFF)
  - named_attacks (ON/OFF)
  - environmental_destruction (HIGH/MODERATE/LOW)

**Sub-systems/Components**:
- Initiative system (DEX + 1d20)
- Player actions: Attack, Skill, Item, Defend, Flee
- Enemy AI priority system
- Damage types & resistances (Physical, Elemental, Magical, Special)
- Status effects (buffs/debuffs)
- Boss battle phases (75%/50%/25% triggers)
- Death saves (0 HP = Downed, not dead)
- Injury table (d20 on 2+ fails)
- Resurrection tiers (Revivify → True Resurrection)
- Combat maneuvers: Grapple, Disarm, Called Shot, Aid
- Tournament framework

**Integration Points**:
- **Module 03 (State)**: Change Log for all updates
- **Module 09 (Progression)**: Combat XP calculation based on progression type
- **Module 13 (Narrative Calibration)**: Combat narration style

**Progression Type-Specific Combat**:
- mastery_tiers: Tier bonuses + technique usage XP
- class_based: Standard XP + class bonus
- quirk_awakening: XP + awakening trigger detection
- milestone_based: Minimal combat XP (10%), story XP
- static_op: No power gain, token XP only

---

### 09_progression_systems.md

**Core Purpose**: Manages XP awards, level-up sequences, skill advancement, and 5 distinct progression type systems based on narrative profile.

**Key Features**:
- **XP Award System**:
  - Combat: Base × Challenge Modifier (Trivial ×0.1 to Boss ×3.0)
  - Quests: Difficulty × Quality
  - Roleplay/Discovery: 25-200 XP
  - Milestones: 50-500 XP
- **Level-Up System**:
  - XP thresholds: L1→2: 1K, escalating to L9→10: 26K
  - Per level: +10 HP, +10 MP, +5 SP, +2 Attribute, +1 Skill Point
  - Milestone levels (5/10/15/20): Bonus skill point, ability tier unlock
- **5 Progression Types**:
  1. mastery_tiers (HxH, Demon Slayer): Tier-based advancement with demonstrations
  2. class_based (MHA, D&D): Standard leveling with class abilities
  3. quirk_awakening (MHA quirks): Two tracks (levels + event-based awakenings)
  4. milestone_based (OPM philosophy): Story-driven, minimal combat XP
  5. static_op (Saitama): No leveling ever, XP for quest tracking only

**Sub-systems/Components**:
- Pre-progression validation protocol
- Skill advancement (active: skill points, passive: use-based XP)
- Mastery bonuses per skill level
- Build diversity examples
- Multi-classing at L10+
- Stat caps (soft 20, hard 25 with diminishing returns)
- Downtime training system
- Training montage generation
- Faction reputation milestones

**Integration Points**:
- **Module 03 (State)**: Atomic updates, automated quest XP cascade
- **Module 08 (Combat)**: XP awards
- **Module 05 (Narrative)**: Roleplay/discovery XP
- **Module 02 (Learning)**: PROGRESSION memories

---

### 10_error_recovery.md

**Core Purpose**: Error detection, classification, recovery protocols, and player-memory conflict resolution.

**Key Features**:
- **Error Categories**:
  - Resource insufficiency
  - Prerequisite not met
  - Cooldown active
  - State desync (Change Log before-value mismatch)
  - Invalid operation type
- **Severity Levels**:
  - CRITICAL: Immediate halt, player notification
  - MAJOR: Offer alternatives, log for review
  - MINOR: Silent correction, internal log
  - TRIVIAL: Background fix, low-priority log
- **Recovery Confidence Thresholds**:
  - Confidence ≥ 0.8: Auto-recovery allowed
  - Formula: (data_clarity × 0.4) + (single_solution × 0.3) + (low_risk × 0.3)

**Sub-systems/Components**:
- Pre-action validation (before every change)
- Post-action validation (after change execution)
- Error classification engine
- Recovery protocols by severity
- Common error scenarios:
  - Duplicate NPC locations
  - Quest state mismatch
  - Resource underflow
  - Dead NPC interaction
  - Change Log desync
- Player-memory conflict resolution (priority ranking)
- Learning from errors system

**Integration Points**:
- All modules feed errors here for resolution
- World rule contradiction detection via memory check

---

### 11_dice_resolution.md

**Core Purpose**: Dice rolling mechanics, transparency requirements, and automation protocols.

**Key Features**:
- **Critical Behavior Rules**:
  - Rule 1: All rolls explicit (`[count]d[sides]+[modifier]`)
  - Rule 2: No hidden rolls (everything transparent)
  - Rule 3: No fudging (honest results always)
- **Common Roll Types**:
  1. Skill Checks (1d20 + modifier vs DC)
  2. Damage Rolls (variable dice per weapon/spell)
  3. Saving Throws (1d20 + modifier vs DC)
  4. Contested Rolls (both roll, higher wins)
  5. Percentile Rolls (d100)
  6. Initiative (1d20 + DEX)

**Sub-systems/Components**:
- Dice roll protocol (format, show work)
- Advantage/Disadvantage (roll twice)
- Critical hits (natural 20) and failures (natural 1)
- Multiple dice handling
- Pseudo-random seed generation: `hash(session_id + action_count + timestamp)`
- Player-facing dice requests (with/without plugin)
- Dice automation rules

**Integration Points**:
- References `12_quick_reference_combat.md`

---

### 12_narrative_scaling.md

**Core Purpose**: Manages power imbalance between PC and world, defines 9 narrative scales, implements OP Protagonist Mode with 9 archetypes.

**Key Features**:
- **Core Philosophy**: Power tier ≠ Narrative scale; different tiers need different storytelling
- **9 Narrative Scales**:
  1. Tactical Survival (death real, struggles)
  2. Strategic Combat (team tactics, flashy moves)
  3. Ensemble Focus (party spotlight, PC enables)
  4. Reverse Ensemble (NPCs as viewpoint, PC as force of nature)
  5. Mythology Journey (episodic, legendary aura)
  6. Faction/Empire Building (management, politics)
  7. Mythic Spectacle (cosmic battles, reality warping)
  8. Conceptual Philosophy (meaning, purpose, existential)
  9. [Various combinations per power tier]
- **Power Imbalance Detection**:
  - Formula based on PC tier vs average threat tier
  - Thresholds: 1.5 → 3.0 → 10.0 trigger scale shifts
  - Context modifiers: Environmental, secret identity, mentor mode
- **9 OP Archetypes**:
  1. Saitama (Invincible, existential)
  2. Mob (Restraint, emotional growth)
  3. Overlord (Roleplaying, dramatic irony)
  4. Saiki K (Oblivious, power as burden)
  5. Mashle (Absurd, earnest simplicity)
  6. Wang Ling (Secret, slice-of-life + cosmic)
  7. Vampire D (Legend, mythology journey)
  8. Slime/Rimuru (Builder, faction management)
  9. Deus (Disguised God, romance/normalcy)

**Sub-systems/Components**:
- Power tier progression (11-10 Human → 0 Boundless)
- Scale shift protocol with ceremonies
- Growth models: Modest (traditional), Accelerated (isekai), Instant OP (godlike start)
- Progressive OP Mode (accelerated growth into OP)
- Non-combat tension generation for high power imbalance
- Tension categories: Social, Existential, Structural
- Scale shift memory template

**Integration Points**:
- **Module 02 (Memory)**: Stores tier changes as high-heat memories
- **Module 05 (Narrative)**: Generates celebration scenes, NPC reactions
- **Module 06 (Session Zero)**: Sets initial growth model
- **Module 09 (Progression)**: Triggers tier bump based on thresholds

---

### 13_narrative_calibration.md

**Core Purpose**: Defines narrative DNA scales, extracts tone/style profiles from anime, maps narrative choices to mechanical systems.

**Key Features**:
- **10 Narrative DNA Scales** (0-10 each):
  1. Introspection vs Action
  2. Comedy vs Drama
  3. Simple vs Complex
  4. Power Fantasy vs Struggle
  5. Explained vs Mysterious
  6. Fast vs Slow (pacing)
  7. Episodic vs Serialized
  8. Grounded vs Absurd
  9. Tactical vs Instinctive
  10. Hopeful vs Cynical
- **15 Trope Switches** (ON/OFF): Rapid tonal shifts, attack names, power of friendship, tragic backstory, transformation sequences, etc.
- **Profile Library**: 13+ pre-made profiles (Hunter x Hunter, DanDaDan, Attack on Titan, etc.)

**Sub-systems/Components**:
- Extraction process:
  - Method 1: Research-derived (automatic from anime)
  - Method 2: Player-provided (Session Zero questions)
  - Method 3: Hybrid (player adjusts research)
- Profile blending rules for multiple influences
- Confidence threshold (≥70% valid, <70% requires player validation)
- Narrative voice calibration (same scenario, different feel)
- **Mechanical Scaffolding**:
  - Power Level Mapping → Growth Models (via Module 12)
  - Progression Pacing → XP Multipliers (via Module 09)
  - Combat System → Stat Framework (via Module 08)
- Genre library auto-loading rules by campaign type:
  - Sci-Fi/Space Opera
  - Mystery/Thriller
  - Horror/Survival
  - Tournament/Competition
  - Isekai/Reincarnation
  - Mecha/Pilot
  - Romance-Focused
  - Supernatural/Urban Fantasy
  - Historical/Period
  - Music/Performance
- Player feedback loop (mid-session calibration, profile evolution)

**Integration Points**:
- **Module 05 (Narrative)**: Generic rules filtered through profile
- **Module 07 (Anime Integration)**: Research mechanics + narrative DNA together
- **Module 04 (NPC Intelligence)**: Dialogue filtered through profile
- **Module 08 (Combat)**: Stat framework from tactical scale
- **Module 09 (Progression)**: XP model from pacing scale
- **Module 12 (Narrative Scaling)**: Growth model from power fantasy scale

---

## System Architecture Summary

### Module Dependency Flow

```
Module 00 (System Init)
    ├── Validates schemas
    └── Loads modules in order

Module 01 (Cognitive Engine) ──[Central Hub]
    ├── Routes to all other modules based on intent
    ├── Validates coherence across systems
    └── Orchestrates multi-module responses

Module 02 (Learning Engine)
    ├── Stores/retrieves memories
    └── Supports all modules with context

Module 03 (State Manager)
    ├── Validates all changes
    ├── Manages mechanical systems
    └── Handles persistence

Modules 04-09 (Gameplay)
    ├── 04: NPC behavior/relationships
    ├── 05: Narrative generation/foreshadowing
    ├── 06: Character creation workflow
    ├── 07: External anime research
    ├── 08: Combat resolution
    └── 09: XP/leveling/skills

Module 10 (Error Recovery)
    └── Catches and resolves errors from all modules

Module 11 (Dice)
    └── Provides randomization for 08, 09

Modules 12-13 (Calibration Layer)
    ├── 12: Power scaling/narrative scale selection
    └── 13: Tone/style/mechanical scaffolding
```

### Key Integration Patterns

1. **Profile-Driven Behavior**: Modules 08, 09, 04, 05 all read narrative profile (Module 13) to calibrate output
2. **Power-Aware Narration**: Module 12 detects power imbalance → adjusts Modules 04, 05 behavior
3. **Atomic State Updates**: All modules use Module 03's Change Log format for validated, rollbackable changes
4. **Memory Threading**: Important events from all modules create memories in Module 02 with appropriate heat values
5. **Session Zero Configuration**: Module 06 initializes all other modules with player preferences via Modules 07, 13

### Shared Schema References

All modules reference these core schemas (validated by Module 03):
- `character_schema.json` - Player character state
- `npc_schema.json` - NPC data with ensemble fields
- `world_state_schema.json` - Global campaign state
- `quest_schema.json` - Quest tracking
- `memory_thread_schema.json` - Memory storage format
- `economy_meta_schema.json` - Currency/transaction rules
- `crafting_meta_schema.json` - Item creation rules
- `progression_meta_schema.json` - Leveling rules
- `downtime_meta_schema.json` - Between-adventure activities
- `power_system_schema.json` - Anime power mechanics
