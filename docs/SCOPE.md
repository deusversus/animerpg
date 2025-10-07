# AIDM v2 Project Scope

## Document Purpose

This document explicitly defines what IS and IS NOT included in AIDM v2. When in doubt about whether to implement a feature or accept a suggested change, refer to this document first.

**What is AIDM v2?** See `README.md` for complete system overview.

---

## In Scope (MVP Features)

### ✅ Core AIDM Functionality

**Narrative Intelligence**
- Intent classification (dialogue, thought, meta, narrative)
- Multi-stage processing pipeline
- Player communication profiling
- Drift recognition and adaptation

**Memory Management**
- Hierarchical memory threads (Core, Character, Relationship, Quest, World, Consequence)
- Memory compression and heat indexing
- Context-triggered memory expansion
- Memory integrity validation

**State Tracking**
- Complete game state persistence (HP/MP/SP, inventory, skills, XP)
- World state management (time, location, factions, weather)
- Session export/import (JSON/YAML)
- Cross-session state reconstruction

**NPC Intelligence**
- Affinity system (-100 to +100)
- Relationship flags (emotional, persistent, historical, trauma)
- Reflection-based response evolution
- Social network simulation
- Information propagation and knowledge boundaries

**Narrative Systems**
- Autonomous world evolution (narrative drift)
- Failure integration mechanics
- Meta-command interface
- Consistency checking and validation
- Event generation framework

---

### ✅ Anime Integration

**Research Capabilities**
- Web search protocol for anime/manga research
- Multi-source verification system
- Hallucination prevention (player confirmation loops)
- Citation and source tracking

**World Generation**
- Single-anime world creation
- Multi-anime fusion and harmonization
- Power system integration frameworks
- Genre-appropriate tone adaptation

**Pre-Built Knowledge**
- Trope libraries (isekai, shonen, seinen, slice-of-life)
- **Power system frameworks (universal 4-category taxonomy)**:
  - `mana_magic_systems.md`: External energy (Fairy Tail, Black Clover, Overlord, etc.) - ~30-35% coverage
  - `ki_lifeforce_systems.md`: Internal energy (Dragon Ball, Naruto, Hunter x Hunter, etc.) - ~30-35% coverage
  - `soul_spirit_systems.md`: Metaphysical/death powers (Jujutsu Kaisen, Bleach, Soul Eater, etc.) - ~15-20% coverage
  - `psionic_psychic_systems.md`: Mental powers (Mob Psycho, Saiki K, Railgun, etc.) - ~10-15% coverage
  - `power_tier_reference.md`: VS Battles tier mapping (OP handling in Module 12 Player Agency)
- Common anime mechanics documentation

---

### ✅ JRPG Mechanics

**Character Systems**
- HP/MP/SP resource tracking
- Unified skill system (physical, magical, psionic, unique)
- Experience and leveling
- Inventory and equipment management
- Status effects and conditions

**Combat**
- Turn-based tactical combat
- Narrative-focused combat (simplified)
- Skill usage and cooldowns
- Damage calculation and resistance
- Combat consequence integration

**Progression**
- Experience gain and level-up
- Skill mastery and advancement
- Stat allocation
- Equipment upgrades

---

### ✅ Player Experience

**Session Zero**
- Guided character creation (5-phase process)
- World setup and faction initialization
- Player preference calibration
- Opening scene generation

**Gameplay Calibration**
- Content preferences (tragedy, romance, violence, explicitness)
- Gameplay balance (combat complexity, puzzle difficulty, social depth)
- Difficulty scaling (power fantasy to brutal challenge)
- Pacing preferences (episodic vs. long arcs)

**Quality of Life**
- Meta-command system for out-of-character control
- State export/import for session persistence
- Error correction and recovery
- Consistency validation

---

## Explicitly Out of Scope

### ❌ NOT Included in MVP

**Standalone Applications**
- ❌ Desktop apps with GUIs
- ❌ Web applications or servers
- ❌ Mobile apps
- ❌ Databases or persistent storage infrastructure
- ❌ Custom LLM training or fine-tuning

**Real-Time Features**
- ❌ Multiplayer synchronization
- ❌ Real-time voice interaction
- ❌ Live video streaming
- ❌ Concurrent multi-player sessions

**Advanced Media**
- ❌ Automatic image generation (unless LLM has native capability)
- ❌ Audio synthesis or music composition
- ❌ 3D rendering or VR integration
- ❌ Animated cutscenes

**Complete Anime Recreations**
- ❌ Pre-built complete worlds for specific anime (e.g., full Naruto world)
- ❌ Exact character stat blocks for canon characters
- ❌ Complete bestiaries for specific anime
- ❌ Official storyline recreation (system generates original stories inspired by anime)

**Code Execution Beyond LLM Capabilities**
- ❌ Complex simulations requiring dedicated compute
- ❌ Real-time physics engines
- ❌ Advanced AI models separate from the LLM
- ❌ External API integrations (except LLM's native web search)

**Advanced AI Features (Deferred to Future)**
- ❌ Constitutional AI framework (from Improvement Proposal)
- ❌ Multimodal generation (images, audio) beyond LLM native
- ❌ Federated learning network
- ❌ Tree-structured narrative planning (MCTS)
- ❌ Curiosity-driven exploration (CDE)
- ❌ Advanced emotional intelligence beyond basic affinity

---

## Boundary Cases (Clarifications)

### Image Generation
**Out of Scope**: Custom image generation systems requiring external tools  
**In Scope**: Using LLM's native image generation (e.g., DALL-E in ChatGPT) when available  
**Rationale**: We don't build image generators, but we'll leverage them if the LLM has them

### Voice Interaction
**Out of Scope**: Custom voice recognition or synthesis  
**In Scope**: Text-based interaction that works with LLM's native voice features  
**Rationale**: Players can use LLM voice features if available, but AIDM is text-first

### Multiplayer
**Out of Scope**: Real-time synchronization or turn-based multiplayer systems  
**In Scope**: Single player with option to share exported states for asynchronous "collaborative" play  
**Rationale**: Each player has their own AIDM instance; they can share saves but don't play simultaneously

### Anime Knowledge
**Out of Scope**: Comprehensive pre-built wikis for hundreds of anime  
**In Scope**: Research protocol + trope libraries for major genres + **5 universal power system frameworks (covers ~85-90% of anime)**  
**Rationale**: LLM researches specific anime on demand; we provide frameworks and common patterns. New 4-category taxonomy (external/internal/metaphysical/mental energy) + OP character guidance covers vast majority of anime power systems without building hundreds of specific libraries.

### Game Balance
**Out of Scope**: Perfectly balanced competitive mechanics  
**In Scope**: Functional mechanics that feel appropriate for narrative play  
**Rationale**: AIDM prioritizes story over competitive balance; mechanics serve narrative

### Python Code
**Out of Scope**: Complex programs requiring installation or dependencies  
**In Scope**: Simple validation scripts that run in LLM sandboxed Python (if available)  
**Rationale**: `state_validator.py` is a convenience tool, not a requirement

---

## Known Limitations

We accept these constraints as inherent to the instruction-set approach:

### Technical Limitations

**Context Window Limits**
- LLMs have finite context (even 128K has limits)
- Memory compression required for long campaigns
- Some detail loss inevitable in very long sessions
- **Mitigation**: Aggressive compression, player-driven memory restoration

**LLM Capability Variance**
- Different LLMs have different capabilities (web search, code execution, etc.)
- System may degrade on less capable models
- **Mitigation**: Graceful degradation, core features work everywhere

**Research Accuracy**
- Web research may return incorrect information
- Obscure anime may have limited online information
- **Mitigation**: Player verification loops, player-assisted world building

**State Persistence Fragility**
- Exported states are large JSON/YAML files
- Manual copy-paste prone to errors
- **Mitigation**: Validation on import, player correction protocol

### Design Limitations

**No True Multiplayer**
- Each player has separate AIDM instance
- No real-time coordination between instances
- **Accepted**: Single-player focus with shareable saves

**Narrative Over Balance**
- Mechanics are approximate, not mathematically balanced
- Player power curves may vary widely
- **Accepted**: Story quality > mechanical perfection

**Genre Constraints**
- Pre-built knowledge focuses on popular anime genres
- Niche genres may need player-assisted setup
- **Accepted**: Core genres covered, others improvised

**LLM Dependency**
- System requires high-quality LLM to function
- May not work well on smaller/older models
- **Accepted**: Designed for cutting-edge LLMs (2024-2025 era)

---

## Success Criteria (Acceptance Tests)

The MVP is "done enough" when these tests pass:

### Test 1: Cold Start
**Test**: New player loads core instructions + schemas, says "I want to play in a world like Naruto"  
**Pass Criteria**: Reaches playable character in <10 exchanges, AIDM correctly researches Naruto

### Test 2: Multi-Anime Fusion
**Test**: Player requests "Naruto ninja powers + Solo Leveling gates + My Hero Academia quirks"  
**Pass Criteria**: AIDM creates coherent power system, explains fusion logic, world is playable

### Test 3: Session Persistence
**Test**: Player plays for 20 turns, exports state, starts new session, imports state  
**Pass Criteria**: All stats, relationships, inventory, and plot threads restored correctly

### Test 4: Combat Mechanics
**Test**: Player engages in tactical combat using skills with MP costs  
**Pass Criteria**: HP/MP/SP tracked accurately, skills validate prerequisites, combat resolves with consequences

### Test 5: Memory Coherence
**Test**: 20+ exchanges with multiple NPCs, reference past events  
**Pass Criteria**: NPCs remember previous interactions, affinity changes persist, no contradictions

### Test 6: Error Recovery
**Test**: AIDM makes mistake (wrong HP value), player says "My HP should be 50, not 150"  
**Pass Criteria**: AIDM acknowledges error, corrects state, continues play seamlessly

### Test 7: Genre Adaptation
**Test**: Play 3 different sessions: isekai adventure, shonen battle, slice-of-life romance  
**Pass Criteria**: Tone, pacing, and focus shift appropriately; each feels genre-authentic

### Test 8: Research Validation
**Test**: Player references obscure anime AIDM can't find reliable info on  
**Pass Criteria**: AIDM admits uncertainty, asks player to describe, doesn't hallucinate details

---

## Future Considerations

Features we might add later, but NOT in MVP:

### Phase 2 (Post-MVP)
- Constitutional AI ethical framework
- Advanced emotional intelligence (multi-dimensional emotion tracking)
- Multimodal scene generation (images, music)
- Expanded genre libraries (10+ anime genres)
- Community-shared world templates

### Phase 3 (Advanced)
- Tree-structured narrative planning (MCTS)
- Curiosity-driven exploration mechanics
- Federated learning across sessions
- Cross-platform state sync
- Collaborative multi-player framework

### Phase 4 (Experimental)
- VR/AR integration
- Advanced NPC autonomy (NPCs pursue independent goals)
- Procedural world generation
- Dynamic difficulty adjustment
- Emergent quest generation

---

## Scope Change Protocol

To maintain project focus, proposed scope changes must:

1. **Align with Core Philosophy**: Enhance player agency, emergent storytelling, or anime integration
2. **Not Require External Dependencies**: Stay within LLM instruction-set paradigm
3. **Pass Cost-Benefit Analysis**: Value added > complexity introduced
4. **Not Break Existing Tests**: All 8 acceptance tests still pass
5. **Have Clear Success Criteria**: Testable, measurable improvement

**Approval Required For**:
- Adding new core systems (beyond 10 instruction modules)
- Changing fundamental architecture (module dependencies)
- Adding external dependencies (databases, APIs, etc.)
- Removing accepted limitations (multiplayer, real-time features)

**No Approval Needed For**:
- New trope libraries (adding genres)
- New power system references (documenting frameworks)
- Template improvements (better examples)
- Documentation clarifications
- Bug fixes and error corrections

---

## Version 2.0 Scope Freeze

**As of October 2025, the v2.0 scope is FROZEN.**

No new features will be added to v2.0 beyond those documented here. All future enhancements go into v2.1+ planning.

This scope freeze ensures:
- MVP ships complete and tested
- No feature creep delays launch
- Clear boundary for "done enough"
- Foundation for future iteration

---

**When proposing new features, always ask: "Is this essential for the core anime RPG experience, or is it a nice-to-have for future versions?"**
