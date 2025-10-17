# Deep Research AI Analysis Prompt - AIDM v2 System

## Project Context

You are analyzing **AIDM v2 (Anime Inspired Dungeon Master)** - an AI-powered tabletop RPG system that enables Large Language Models to run authentic anime-style campaigns. This is a comprehensive modular framework designed for use with Claude, GPT-4, and other advanced LLMs.

**Project Repository**: https://github.com/deusversus/animerpg  
**Current Version**: 2.0  
**Last Major Update**: October 13, 2025  
**Development Stage**: Production-ready beta, actively maintained

---

## Accessing the Repository

**IMPORTANT**: Since you cannot interact with GitHub's HTML interface, use **raw file URLs** to access content directly.

### Raw File URL Structure

All files can be accessed using this pattern:
```
https://raw.githubusercontent.com/deusversus/animerpg/main/<file_path>
```

### Core System Files (Priority Access)

**Root Documentation**:
- System Architecture: `https://raw.githubusercontent.com/deusversus/animerpg/main/AIDM_System_Architecture.md`
- README: `https://raw.githubusercontent.com/deusversus/animerpg/main/README.md`
- Improvement Proposals: `https://raw.githubusercontent.com/deusversus/animerpg/main/AIDM_Improvement_Proposal_2025.md`

**Core Instructions** (14 modules in `/aidm/instructions/`):
- Module 00: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/instructions/00_system_initialization.md`
- Module 01: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/instructions/01_cognitive_engine.md`
- Module 02: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/instructions/02_learning_engine.md`
- Module 03: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/instructions/03_state_manager.md`
- Module 04: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/instructions/04_npc_intelligence.md`
- Module 05: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/instructions/05_narrative_systems.md`
- Module 06: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/instructions/06_session_zero.md`
- Module 07: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/instructions/07_anime_integration.md`
- Module 08: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/instructions/08_combat_resolution.md`
- Module 09: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/instructions/09_progression_systems.md`
- Module 10: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/instructions/10_error_recovery.md`
- Module 11: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/instructions/11_dice_resolution.md`
- Module 12: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/instructions/12_player_agency.md`
- Module 13: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/instructions/13_narrative_calibration.md`

**Loader Files**:
- AIDM Loader: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/AIDM_LOADER.md`
- Core Instructions: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/CORE_AIDM_INSTRUCTIONS.md`

**Index Files (Optimized Oct 13, 2025)**:
- Profile Index: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/libraries/narrative_profiles/PROFILE_INDEX.md`
- Genre Tropes Index: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/libraries/genre_tropes/GENRE_TROPES_INDEX.md`

**Schemas** (8 JSON files in `/aidm/schemas/`):
- Character: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/schemas/character_schema.json`
- World State: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/schemas/world_state_schema.json`
- Session Export: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/schemas/session_export_schema.json`
- NPC: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/schemas/npc_schema.json`
- Memory Thread: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/schemas/memory_thread_schema.json`
- Power System: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/schemas/power_system_schema.json`
- Anime World: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/schemas/anime_world_schema.json`
- Narrative Profile: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/schemas/narrative_profile_schema.json`

**Archive Documentation** (Recent optimization work):
- Optimization Summary: `https://raw.githubusercontent.com/deusversus/animerpg/main/archive/index_optimization_2025-10-13/OPTIMIZATION_SUMMARY.md`
- Index Optimization Plan: `https://raw.githubusercontent.com/deusversus/animerpg/main/archive/index_optimization_2025-10-13/INDEX_OPTIMIZATION_PLAN.md`

### Libraries (Load Specific Files as Needed)

**Narrative Profiles** (21 files in `/aidm/libraries/narrative_profiles/`):
- Example: Hunter x Hunter profile at `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/libraries/narrative_profiles/hunter_x_hunter_profile.md`
- Pattern: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/libraries/narrative_profiles/{anime_name}_profile.md`
- Available profiles: Hunter x Hunter, Death Note, Jujutsu Kaisen, Attack on Titan, DanDaDan, Demon Slayer, My Hero Academia, Naruto, One Piece, One Punch Man, Konosuba, Re:Zero, Fullmetal Alchemist Brotherhood, Steins;Gate, Code Geass, Cowboy Bebop, Neon Genesis Evangelion, Vinland Saga, Mushishi, Haikyuu, plus EXPANSION_ROADMAP.md
- Full list available in PROFILE_INDEX.md (linked above)

**Genre Tropes** (16 files in `/aidm/libraries/genre_tropes/`):
- Example: Shonen tropes at `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/libraries/genre_tropes/shonen_tropes.md`
- Pattern: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/libraries/genre_tropes/{genre}_tropes.md`
- Available genres: Shonen, Seinen, Isekai, Slice of Life, Comedy, Horror, Mystery/Thriller, Romance (Shoujo), Sports, Mecha, Magical Girl, Sci-Fi, Supernatural, Historical, Music, plus GENRE_TROPES_INDEX.md
- Full list available in GENRE_TROPES_INDEX.md (linked above)

**Power Systems** (6 files in `/aidm/libraries/power_systems/`):
- Pattern: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/libraries/power_systems/{system}_systems.md`
- Available: mana_magic_systems.md, ki_lifeforce_systems.md, soul_spirit_systems.md, psionic_psychic_systems.md, power_tier_reference.md, power_scaling_narrative.md

**Common Mechanics** (3 files in `/aidm/libraries/common_mechanics/`):
- Pattern: `https://raw.githubusercontent.com/deusversus/animerpg/main/aidm/libraries/common_mechanics/{mechanic}.md`
- Available: stat_frameworks.md, leveling_curves.md, skill_taxonomies.md

### Recommended Loading Sequence

**Phase 1** (System Understanding):
1. Load README.md (project overview)
2. Load AIDM_System_Architecture.md (architectural design)
3. Load AIDM_LOADER.md (loading protocol)
4. Load CORE_AIDM_INSTRUCTIONS.md (operational framework)

**Phase 2** (Core Modules):
5. Load all 14 module files (00-13) from `/aidm/instructions/`
6. Load both index files (PROFILE_INDEX.md, GENRE_TROPES_INDEX.md)

**Phase 3** (Schemas & Structure):
7. Load all 8 JSON schemas from `/aidm/schemas/`
8. Review archive documentation for optimization context

**Phase 4** (Deep Dive):
9. Load specific narrative profiles (2-3 examples for quality assessment)
10. Load specific genre trope libraries (2-3 examples for coverage assessment)
11. Load any additional files identified during analysis

### Navigation Tips

- **File names**: Use lowercase with underscores (e.g., `hunter_x_hunter_profile.md`, not `Hunter-X-Hunter-Profile.md`)
- **Directory structure**: All paths relative to repository root
- **Branch**: Use `main` branch in URLs (already included in examples above)
- **404 errors**: If you get a 404, check file name capitalization and path structure
- **Index files**: Start with index files to identify which specific libraries to load

---

## Your Research Objective

Conduct a **systematic, comprehensive, and deeply critical analysis** of the AIDM v2 system across all relevant dimensions. Your goal is to identify:

1. **Architectural strengths and weaknesses**
2. **Functional gaps and missing capabilities**
3. **Structural inefficiencies and technical debt**
4. **Scaling limitations and performance bottlenecks**
5. **User experience issues and accessibility barriers**
6. **Documentation quality and completeness**
7. **Integration risks and module interdependencies**
8. **Future development priorities and strategic oversights**
9. **Industry best practices violations or opportunities**
10. **Innovation potential and competitive positioning**

Do not assume this is an exhaustive list. Apply your full analytical capabilities to discover issues, opportunities, and insights the development team may not have considered.

---

## System Architecture Overview

### Core Structure

**AIDM v2** is a modular system consisting of:

- **14 Core Modules** (00-13): System initialization, cognitive engine, learning engine, state manager, NPC intelligence, narrative systems, session zero, anime integration, combat resolution, progression systems, error recovery, dice resolution, player agency, narrative calibration
- **21 Narrative Profiles**: Anime-specific calibration files defining tone, pacing, dialogue style, combat narratives for specific series:
  - Shonen: Hunter x Hunter, My Hero Academia, Naruto, One Piece, Demon Slayer, Haikyuu, Fullmetal Alchemist Brotherhood
  - Seinen: Attack on Titan, Vinland Saga, Death Note, Code Geass
  - Isekai/Fantasy: Re:Zero, Konosuba, DanDaDan
  - Psychological/Thriller: Death Note, Steins;Gate, Neon Genesis Evangelion, Code Geass
  - Action/Adventure: One Punch Man, Cowboy Bebop, Jujutsu Kaisen
  - Atmospheric: Mushishi
- **16 Genre Trope Libraries**: Structural templates for shonen, seinen, isekai, slice-of-life, comedy, horror, mystery/thriller, romance (shoujo), sports, mecha, magical girl, sci-fi, supernatural, historical, music
- **6 Power System Libraries**: Universal 4-energy taxonomy (mana/magic external, ki/lifeforce internal, soul/spirit metaphysical, psionic/psychic mental) + power tier reference + power scaling narrative guidance
- **3 Common Mechanics Libraries**: Stat frameworks, leveling curves, skill taxonomies
- **8 JSON Schemas**: character_schema, world_state_schema, session_export_schema, npc_schema, memory_thread_schema, power_system_schema, anime_world_schema, narrative_profile_schema
- **Supporting Systems**: Lazy-loading architecture, tier-based context management (TIER 1/2/3), auto-loading rules, profile blending (2-3 profiles), optimization protocols, research enforcement gates

### Design Philosophy

1. **Lazy-Loading**: Only load 20-30K tokens active at any time (out of 180-200K total library)
2. **Modular Independence**: Each module can function standalone or integrate seamlessly
3. **Narrative Authenticity**: Profiles capture real anime storytelling patterns, not generic fantasy
4. **LLM-Agnostic**: Designed to work with Claude, GPT-4, and future models
5. **Session Persistence**: Full state export/import via JSON schemas
6. **Profile Blending**: Combine 2-3 anime profiles for hybrid genres

### Recent Optimizations (Oct 13, 2025)

- Index files optimized: 62.3% token reduction (16,921 → 6,386 tokens)
- Session Zero load reduced 36.2% (29,100 → 18,565 tokens)
- 100% information parity maintained during compression

---

## Research Methodology

### Phase 1: Architectural Analysis

**Examine the module structure and interdependencies:**

1. **Module Cohesion**: Are modules properly scoped? Any violations of single responsibility?
2. **Coupling Analysis**: Which modules are tightly coupled? Does this create brittleness?
3. **Lazy-Loading Effectiveness**: Is the TIER 1/2/3 system optimal? Are there better approaches?
4. **Context Management**: How does the 20-30K active token budget hold up under stress?
5. **Module Redundancy**: Are there overlapping responsibilities between modules?
6. **Missing Modules**: What critical systems are absent? (e.g., economy, factions, timekeeping?)
7. **Scalability**: Can the system handle 100+ NPCs? 50+ quests? Complex multi-faction campaigns?
8. **Integration Points**: Where do modules interact? Are these interfaces well-defined?

**Key Files to Analyze**:
- `aidm/00_system_initialization.md` through `aidm/13_narrative_calibration.md`
- Module cross-references and loading sequences
- State management schemas in `aidm/schemas/`

### Phase 2: Narrative Profile System Analysis

**Evaluate the anime profile library:**

1. **Profile Coverage**: Are major anime genres/styles adequately represented? Current coverage includes 21 profiles spanning shonen (7), seinen (4), isekai/comedy (3), psychological (4), action (3), atmospheric (1). Are there critical gaps (e.g., pure shoujo romance, sports anime depth, idol anime, battle shounen diversity)?
2. **Profile Quality**: Do profiles capture authentic anime storytelling patterns? Verify against source material accuracy.
3. **Profile Depth**: Each profile should define 11 narrative scales (Introspection, Comedy vs Drama, Plot Complexity, Power Fantasy, Mystery, Pacing, Story Structure, Absurdity, Combat Style, Tone, POV Distribution). Are all scales properly calibrated?
4. **Trope Completeness**: Each profile should enable/disable relevant tropes from a master list. Verify trope selection matches source anime authenticity.
5. **Blending Mechanics**: Is the 2-3 profile blending system robust? Test edge cases (e.g., Konosuba comedy + Attack on Titan grimness, Mushishi slow-burn + One Punch Man action).
6. **Profile Conflicts**: How are conflicting scales reconciled when blending? (e.g., Comedy:9 + Comedy:1, Pacing:Fast + Pacing:Slow)
7. **Custom Profiles**: How difficult is it for users to create their own profiles? Is the narrative_profile_schema.json clear enough? Are there templates or examples?
8. **Profile Maintenance**: Are profiles versioned? How do schema updates (e.g., adding Scale 12) propagate to existing profiles?
9. **Scale Integration**: Are all 11 scales properly integrated across Module 13 (Narrative Calibration), Module 05 (Narrative Systems), Module 04 (NPC dialogue), Module 08 (combat narration)?
10. **Profile-Trope Integration**: Do narrative profiles and genre tropes work seamlessly together? Can a profile auto-load tropes (e.g., Hunter x Hunter → shonen_tropes.md)?
11. **Genre Coverage vs Profile Coverage**: The system has 16 genre trope libraries but only 21 specific anime profiles. Is this balance optimal? Should there be more generic "genre starter profiles" (e.g., "Generic Sports Anime Profile")?
12. **Profile Discovery**: Given 21 profiles, how do users find the right one? Is PROFILE_INDEX.md sufficient, or is a recommendation system needed?

**Key Files to Analyze**:
- `aidm/libraries/narrative_profiles/PROFILE_INDEX.md`
- Individual profile files (e.g., `hunter_x_hunter_profile.md`, `death_note_profile.md`)
- `aidm/libraries/genre_tropes/GENRE_TROPES_INDEX.md`
- `aidm/13_narrative_calibration.md` (integration logic)

### Phase 3: Combat & Progression Systems Analysis

**Evaluate mechanical systems:**

1. **Combat Depth**: Does Module 08 support tactical anime combat (e.g., Hunter x Hunter strategy)?
2. **Power Scaling**: How does the system handle anime power escalation (weak → godlike)?
3. **Dice Integration**: Is the Fate/Fudge dice system appropriate for anime campaigns?
4. **Progression Curves**: Are leveling/skill systems flexible enough for different anime styles?
5. **Advanced Classes**: Are the 8 advanced classes (Artifact Hunter, Demon Slayer, etc.) balanced?
6. **Combat Pacing**: Can the system replicate sakuga moments, tournament arcs, training montages?
7. **Death Mechanics**: How are character deaths handled? Permanent vs. resurrection?
8. **Party Balance**: Does the system support solo, duo, quartet, and ensemble campaigns equally?

**Key Files to Analyze**:
- `aidm/08_combat_system.md`
- `aidm/09_progression_and_skills.md`
- `aidm/11_dice_mechanics.md`
- `aidm/system_advanced_classes.md`
- Combat narrative sections in narrative profiles

### Phase 4: State Management & Persistence Analysis

**Evaluate session continuity and data integrity:**

1. **Schema Completeness**: Do the 8 schemas cover all necessary game state? Current schemas: character_schema.json, world_state_schema.json, session_export_schema.json, npc_schema.json, memory_thread_schema.json, power_system_schema.json, anime_world_schema.json, narrative_profile_schema.json. Missing: quest_schema.json, faction_schema.json, economy_schema.json, calendar_schema.json?
2. **Export/Import Robustness**: Can sessions be saved and restored without data loss? Test session_export_schema.json completeness. Does it capture: all NPCs, all memory threads, all world state, active narrative profile, loaded tropes, quest state, faction reputation, currency, calendar?
3. **Version Compatibility**: What happens when schemas change between versions? Is there schema versioning? Migration scripts? Backward compatibility guarantees? What if Scale 12 is added to narrative_profile_schema.json—do old profiles break?
4. **State Synchronization**: How are conflicts resolved when state updates across modules? Example: Module 04 (NPC Intelligence) updates affinity, Module 02 (Learning Engine) records memory, Module 03 (State Manager) updates world state. Are these atomic transactions? Can race conditions occur?
5. **Memory System**: Does Module 02 (Learning Engine) effectively summarize past sessions? Memory threads have heat index (0-100) for priority, but how effective is compression at 50+ sessions? Does information decay appropriately or create amnesia?
6. **NPC Persistence**: Are NPC states, relationships, and goals properly tracked in npc_schema.json? Missing: NPC inventories, NPC quest involvement, NPC locations over time, NPC knowledge boundaries (what NPC knows vs doesn't know).
7. **World Evolution**: Does the world state change dynamically based on player actions? Module 05 (Narrative Systems) handles narrative drift, but is world_state_schema.json updated systematically? Example: Player destroys a city—does this propagate to all NPCs, quests, factions?
8. **Quest Tracking**: Are active/completed quests properly managed across sessions? No quest_schema.json exists. Quests tracked in memory threads (Module 02), but this is informal. Is this sufficient for complex multi-quest campaigns?
9. **Active Narrative Profile Persistence**: Does session_export_schema.json save the active narrative profile (which anime profile was loaded)? If blending 2-3 profiles, are all blend weights saved?
10. **Loaded Library Tracking**: When TIER 2/3 libraries are loaded (tropes, power systems), is this state saved? On session restore, which libraries need to be reloaded?

**Key Files to Analyze**:
- `aidm/schemas/session_export_schema.json`
- `aidm/schemas/world_state_schema.json`
- `aidm/schemas/npc_tracker_schema.json`
- `aidm/02_memory_management.md`
- `aidm/03_state_management.md`

### Phase 5: User Experience & Accessibility Analysis

**Evaluate ease of use for both AIDMs (LLMs) and players:**

1. **Session Zero Complexity**: Is the initial setup too complex? Too many decisions?
2. **Player Onboarding**: How steep is the learning curve for new players?
3. **GM Onboarding**: Can non-technical users understand and modify the system?
4. **Documentation Quality**: Are instructions clear, comprehensive, and well-organized?
5. **Error Handling**: What happens when players make invalid requests or edge case inputs?
6. **Cognitive Load**: Does the system overwhelm players with too many options/mechanics?
7. **Profile Discovery**: Can players easily find the right anime profile for their campaign?
8. **Mid-Campaign Adjustments**: How easy is it to change tone, add NPCs, or shift narrative direction?
9. **Accessibility**: Are there barriers for non-anime fans? Non-TTRPG players?
10. **Tooling**: Are there any UI tools, character sheets, or companion apps needed?

**Key Files to Analyze**:
- `aidm/00_system_initialization.md` (Session Zero process)
- `aidm/libraries/narrative_profiles/PROFILE_INDEX.md` (profile discovery)
- All "Usage Notes" sections in profiles and modules
- `AIDM_System_Architecture.md`

### Phase 6: Documentation & Code Quality Analysis

**Evaluate technical quality and maintainability:**

1. **Documentation Completeness**: Are all modules fully documented? Missing sections?
2. **Code Comments**: Where code exists (schemas, logic), is it well-commented?
3. **Consistency**: Do modules follow consistent formatting, terminology, and structure?
4. **Examples**: Are there sufficient examples of system usage in practice?
5. **Edge Cases**: Are edge cases and failure modes documented?
6. **Versioning**: Is there a clear versioning strategy? Changelog maintenance?
7. **Deprecation**: Are deprecated features properly marked and archived?
8. **Cross-References**: Are module interdependencies clearly documented?
9. **Technical Debt**: Where has the system accumulated shortcuts or "TODO" items?
10. **Testing**: Is there any validation protocol for system changes? Dry tests?

**Key Files to Analyze**:
- All markdown files in `aidm/` directory
- `archive/` folder for historical context
- Recent optimization work in `archive/index_optimization_2025-10-13/`
- `AIDM_System_Architecture.md`
- `AIDM_Improvement_Proposal_2025.md`

### Phase 7: Performance & Scalability Analysis

**Evaluate system efficiency and limits:**

1. **Token Efficiency**: Is 20-30K active tokens sustainable? What's the ceiling?
2. **Loading Performance**: How long does Session Zero take? Module loading?
3. **Memory Leaks**: Can the system run indefinitely without context bloat?
4. **Concurrent Sessions**: Can one LLM instance handle multiple campaigns?
5. **Large Parties**: How does the system perform with 6-8 PCs? 10+?
6. **Complex Worlds**: Can it handle multi-city, multi-faction, epic-scale campaigns?
7. **Long Campaigns**: What happens after 50 sessions? 100 sessions?
8. **Profile Library Size**: At what point does the 180-200K token library become unwieldy?
9. **Auto-Loading Overhead**: Does Module 13's auto-loading create bottlenecks?
10. **Optimization Limits**: Have we reached the practical compression limit for index files?

**Key Files to Analyze**:
- `archive/index_optimization_2025-10-13/OPTIMIZATION_SUMMARY.md`
- Module loading sequences in `aidm/00_system_initialization.md`
- Lazy-loading logic in `aidm/13_narrative_calibration.md`
- State management overhead in schemas

### Phase 8: Innovation & Competitive Analysis

**Evaluate positioning and uniqueness:**

1. **Market Differentiation**: What makes AIDM v2 unique compared to other AI TTRPG systems?
2. **Anime Authenticity**: Does this truly capture anime storytelling better than generic fantasy systems?
3. **LLM Evolution**: How future-proof is the system? Will it work with GPT-5, Claude 4?
4. **Industry Trends**: Are there emerging AI TTRPG trends AIDM v2 isn't addressing?
5. **Monetization**: Could this be commercialized? What would that require?
6. **Community Potential**: Is the system designed for community contributions (profiles, modules)?
7. **Cross-Media**: Could AIDM v2 integrate with other media (audio, visuals, VTT tools)?
8. **Educational Value**: Could this teach anime storytelling patterns to writers/GMs?
9. **Research Applications**: Are there academic or research applications for this framework?
10. **Patent/IP**: Are there novel innovations worth protecting or publishing?

**Key Files to Analyze**:
- Entire system architecture
- Unique features (lazy-loading, profile blending, Scale 11 POV, anime-specific calibration)
- `AIDM_Improvement_Proposal_2025.md`

### Phase 9: Library Content Quality Analysis

**Evaluate the quality and usability of the 46 library files:**

1. **Narrative Profile Consistency**: All 21 profiles should follow narrative_profile_schema.json structure (11 scales, trope toggles, pacing parameters, tone signature, dialogue style, combat narrative style, example scenes, usage notes). Verify consistency across all profiles.

2. **Genre Trope Library Depth**: All 16 genre trope libraries should provide sufficient structural templates for campaigns. Evaluate depth and usability of each genre file (shonen_tropes.md, seinen_tropes.md, isekai_tropes.md, etc.).

3. **Power System Coverage Verification**: The 6 power system libraries claim 85-90% anime coverage. Verify this claim by testing against popular anime:
   - **mana_magic_systems.md**: Should cover Fairy Tail, Black Clover, Overlord, Frieren, Mushoku Tensei magic.
   - **ki_lifeforce_systems.md**: Should cover Dragon Ball ki, Naruto chakra, Hunter x Hunter Nen, One Piece Haki.
   - **soul_spirit_systems.md**: Should cover Jujutsu Kaisen cursed energy, Bleach spiritual pressure, Soul Eater soul wavelength.
   - **psionic_psychic_systems.md**: Should cover Mob Psycho 100 esper powers, Code Geass Geass, A Certain Scientific Railgun electromaster.
   - **power_tier_reference.md**: Should map anime power levels to VS Battles Wiki tiers (10-C to 2-A+).
   - **power_scaling_narrative.md**: Should guide handling OP protagonists (Saitama, Ainz, Rimuru, Sung Jin-Woo).

4. **Common Mechanics Usability**: The 3 common mechanics libraries (stat_frameworks.md, leveling_curves.md, skill_taxonomies.md) should provide clear frameworks for mechanical implementation. Are these libraries actionable for LLMs? Do they have sufficient examples?

5. **Cross-Library Integration**: Do libraries reference each other appropriately? Example: Does hunter_x_hunter_profile.md reference ki_lifeforce_systems.md for Nen? Does shonen_tropes.md reference leveling_curves.md for progression?

6. **Library Auto-Loading Logic**: Module 13 (Narrative Calibration) handles auto-loading of profiles and tropes. Is the trigger logic robust? Example: Player says "I want a Naruto campaign" → Should auto-load naruto_profile.md, shonen_tropes.md, ki_lifeforce_systems.md. Does this work?

7. **Profile Example Scenes**: Each profile should include example scenes demonstrating narrative style. Verify quality and representativeness of these examples across all 21 profiles.

8. **Trope Toggle Definitions**: Each profile enables/disables tropes from a master list. Is there a definitive master trope list? Are trope definitions consistent across profiles?

9. **Usage Notes Quality**: Each profile and library file should have "Usage Notes" sections guiding LLM application. Evaluate clarity and completeness of usage notes.

10. **Profile Expansion Roadmap**: There's an EXPANSION_ROADMAP.md in narrative_profiles/. Does this document future profile additions? Is it maintained?

---

### Phase 10: Missing Systems & Future Development

**Identify critical gaps and roadmap priorities:**

1. **What's Missing?**: What critical systems are absent from the current architecture?
   - **Quest Management System**: No dedicated quest_schema.json. Quests tracked in memory threads (Module 02) but lack structured framework. No quest log, quest branching, quest success/failure tracking, multi-objective quests, timed quests.
   - **Faction/Reputation System**: NPC affinity exists (Module 04) but no faction-level reputation. Multi-faction campaigns (e.g., Hunter Association vs Phantom Troupe vs Chimera Ants) lack mechanical support.
   - **Economy System**: No currency tracking, item pricing, merchant systems, inflation, economic simulation. Inventory exists (character_schema) but no monetary mechanics.
   - **Timekeeping/Calendar**: World state (world_state_schema) has time of day but no calendar, seasons, holidays, long-term time tracking, aging, time-sensitive events.
   - **Weather/Environment**: No environmental hazards, weather systems, terrain effects on combat/travel, survival mechanics.
   - **Crafting System**: No crafting schema, resource gathering, item creation recipes, crafting skills, enchanting, alchemy.
   - **Vehicle/Mount/Companion Systems**: No mount mechanics, vehicle combat, animal companions, familiars, summoned creatures (beyond NPC schema).
   - **Mass Combat**: Individual combat (Module 08) exists but no army-scale battles, war mechanics, unit management, strategic combat.
   - **Political Intrigue**: No intrigue mechanics, diplomacy systems, espionage, political maneuvering frameworks.
   - **Romance Mechanics**: NPC affinity (Module 04) covers relationships but lacks romance-specific mechanics: confession systems, dating, jealousy, love triangles, romance flags (common in anime).
   - **Downtime Activities**: No structured downtime framework for training montages, side jobs, hobbies, relationship building, base management.
   - **Base Building**: Mentioned in old v1 files (`system_basebuilding.md` in `isekairpg_old/`) but not in v2. Guild halls, player homes, strongholds absent.
   - **Social Link Systems**: Persona-style social links (deepening relationships through structured events) could enhance NPC depth.
   - **Training Systems**: Training arcs (shonen trope) exist conceptually but lack mechanical framework: skill XP systems, breakthrough mechanics, training montage time-skips.
   - **Tournament Arc Framework**: Common in shonen but no dedicated structure for bracket management, tournament pacing, spectator reactions, upset victories.
   - **Death/Resurrection Mechanics**: How do character deaths work? Permanent? Resurrection rules? Death save mechanics? This is vague in current modules.

2. **Module Priorities**: Which existing modules need the most work? Candidates:
   - Module 03 (State Manager): Needs quest management, faction tracking, economy integration.
   - Module 04 (NPC Intelligence): Needs NPC knowledge boundaries, NPC inventories, NPC quest involvement.
   - Module 06 (Session Zero): May be too complex with 21 profiles + 16 genres + scale calibration.
   - Module 08 (Combat Resolution): Needs tournament arc structure, mass combat, sakuga moment mechanics.
   - Module 09 (Progression Systems): Needs training montage mechanics, breakthrough systems, skill mastery depth.

3. **Profile Gaps**: Which major anime series are missing from the 21-profile library? Current profiles: Hunter x Hunter, Death Note, Jujutsu Kaisen, Attack on Titan, DanDaDan, Demon Slayer, MHA, Naruto, One Piece, One Punch Man, Konosuba, Re:Zero, FMA:B, Steins;Gate, Code Geass, Cowboy Bebop, Evangelion, Vinland Saga, Mushishi, Haikyuu. Potential gaps:
   - **Pure Romance**: Kaguya-sama, Your Name, Toradora, Clannad
   - **Idol Anime**: Love Live, Idolmaster
   - **Mecha Depth**: Gundam, Gurren Lagann, Darling in the Franxx (only Evangelion currently)
   - **Battle Shonen Diversity**: Bleach, Dragon Ball, Fairy Tail, Black Clover
   - **Sports Diversity**: Kuroko's Basketball, Hajime no Ippo, Blue Lock (only Haikyuu currently)
   - **Isekai Diversity**: Overlord, That Time I Got Reincarnated as a Slime, Mushoku Tensei, Shield Hero
   - **Magical Girl**: Madoka Magica, Sailor Moon
   - **Atmospheric/Slow**: Violet Evergarden, March Comes in Like a Lion

4. **Genre Trope Gaps**: Are there anime genres not covered by the 16 trope libraries? Current genres: shonen, seinen, isekai, slice-of-life, comedy, horror, mystery/thriller, romance (shoujo), sports, mecha, magical girl, sci-fi, supernatural, historical, music. Potential gaps:
   - **Battle Royale**: Death game structures (though mystery/thriller may cover)
   - **Cultivation/Wuxia**: Xianxia-inspired progression (though not strictly anime)
   - **Ecchi/Fanservice**: Harem mechanics, fanservice tropes (deliberately excluded?)
   - **Post-Apocalyptic**: Survival, rebuilding, resource scarcity (partially in sci-fi?)
   - **Time Loop**: Looping mechanics, Groundhog Day structures (Steins;Gate profile exists but no dedicated trope library)
   - **Tournament Arc Specifics**: Bracket management, upset victories, training between rounds (should this be its own trope library vs embedded in shonen_tropes.md?)
5. **Advanced Features**: What "version 3.0" features should be considered?
6. **Automation Opportunities**: Where could the system automate more (NPC dialogue, quest generation)?
7. **Integration Opportunities**: What external systems could AIDM v2 integrate with?
8. **Accessibility Improvements**: How can the system become easier to use?
9. **Performance Improvements**: Where are the biggest optimization opportunities?
10. **Community Features**: How could the system support user-generated content?

**Key Files to Analyze**:
- All modules for "TODO" comments and incomplete sections
- `AIDM_Improvement_Proposal_2025.md`
- `archive/aidm_v2_development/` for historical context
- Module cross-references to identify gaps

### Phase 10: Risk Assessment & Mitigation

**Identify potential failures and vulnerabilities:**

1. **LLM Dependency**: What happens if Claude/GPT-4 change their APIs or capabilities?
2. **Context Limits**: What if LLM context windows shrink or become more expensive?
3. **Hallucination Risks**: Where is the system most vulnerable to LLM hallucinations?
4. **State Corruption**: What could cause session state to become corrupted?
5. **Module Conflicts**: Where could module interactions cause unexpected behaviors?
6. **Profile Conflicts**: What happens with incompatible profile blends?
7. **User Error**: Where are users most likely to break the system?
8. **Scalability Walls**: At what point does the system become unmanageable?
9. **Version Migration**: How risky are updates? Can old sessions migrate forward?
10. **Maintenance Burden**: Is the system sustainable for a small team to maintain?

**Key Files to Analyze**:
- All integration points between modules
- State management and export/import logic
- Error handling sections (or lack thereof)
- Validation protocols

---

## Specific Analysis Questions

### Critical Questions to Answer

1. **Does it actually work?** Based on the architecture and documentation, would this system successfully run anime-style campaigns? Where would it fail?

2. **Is the lazy-loading architecture optimal?** Could TIER 1/2/3 be restructured? Are there better approaches to context management? Current system: TIER 1 (always loaded: ~8K tokens), TIER 2 (lazy-loaded modules: ~12K when needed), TIER 3 (libraries: load sections on-demand).

3. **Are the 21 narrative profiles sufficient?** What major anime series/genres are missing? Current profiles cover shonen/seinen/isekai/psychological well, but gaps may exist in: pure romance (shoujo), idol anime, pure comedy without action, sports depth beyond Haikyuu, magical girl, pure slice-of-life without supernatural elements.

4. **Are the 11 narrative scales properly integrated?** The scales are: Introspection vs Action (0-10), Comedy vs Drama (0-10), Plot Complexity (0-10), Power Fantasy vs Struggle (0-10), Explained vs Mysterious (0-10), Pacing (0-10), Story Structure (0-10), Absurdity (0-10), Combat Style (0-10), Tone (0-10), POV Distribution (0-11). Are these applied consistently in Module 05, 08, 04, 13?

5. **Can the system scale?** Would it work for a 2-year, 100-session epic campaign? A 10-player party? A multi-city world? Current context management: 20-30K active tokens out of 200K. Memory compression and state export/import are critical at scale.

6. **Is the combat system deep enough?** Can it replicate tactical anime battles (Hunter x Hunter Nen strategy), sakuga moments (Demon Slayer fluid choreography), psychological duels (Death Note mind games), tournament arcs (My Hero Academia structure)?

7. **Are the 8 schemas complete?** Would session export/import actually preserve all critical game state? Schemas: character, world_state, session_export, npc, memory_thread, power_system, anime_world, narrative_profile. Missing: quest log schema? faction schema? timeline/calendar schema?

8. **Is Session Zero too complex?** Module 06 runs a 5-phase setup process. Would new players be overwhelmed by profile selection (21 options), scale calibration (11 scales), trope loading (16 genres)?

9. **What's the biggest architectural flaw?** If you had to point to one systemic weakness, what would it be? (Possibilities: module coupling, context management brittleness, profile maintenance burden, schema versioning, LLM dependency, research enforcement reliability)

10. **What's the most important thing to build next?** What single addition would have the greatest impact on system quality? (Possibilities: quest management system, faction/reputation system, relationship romance mechanics beyond NPC affinity, downtime/crafting systems, mass combat, political intrigue frameworks)

11. **Is the 16-genre trope library sufficient?** Current genres: shonen, seinen, isekai, slice-of-life, comedy, horror, mystery/thriller, romance (shoujo), sports, mecha, magical girl, sci-fi, supernatural, historical, music. Missing: battle royale, post-apocalyptic, time loop, cultivation/wuxia-inspired, tournament arc specifics?

12. **Power system coverage**: The 6 power system libraries claim 85-90% anime coverage using 4 energy types (mana/magic, ki/lifeforce, soul/spirit, psionic/psychic) + power tier reference + scaling narrative. Is this accurate? Test cases: Stands (JoJo), Alchemy (FMA), Devil Fruits (One Piece), Quirks (MHA), Nen (HxH), Cursed Energy (JJK), Titans (AoT).

13. **Research enforcement reliability**: The system claims "P1 research enforcement" with ABORT gates to prevent hallucination. In Module 06 (Session Zero) and Module 07 (Anime Integration), are these gates robust enough to stop an LLM from proceeding without web research?

14. **Token optimization impact**: Recent optimization (Oct 13, 2025) achieved 62.3% reduction in index files. Did this compression lose information, reduce clarity, or create usability issues? Is 100% information parity claim accurate?

15. **Cross-LLM compatibility**: The system is designed for Claude, GPT-4, Gemini. Do all 14 modules work equally well across these LLMs? Are there LLM-specific issues (e.g., Claude's context handling vs GPT-4's instruction following)?

### Comparative Analysis Questions

1. How does AIDM v2 compare to generic AI TTRPG systems (e.g., AI Dungeon, NovelAI)?
2. How does it compare to traditional TTRPG systems adapted for anime (e.g., Big Eyes Small Mouth)?
3. How does it compare to narrative-focused TTRPGs (e.g., Powered by the Apocalypse, Fate)?
4. What innovations does AIDM v2 introduce that don't exist elsewhere?
5. Where does AIDM v2 fall behind industry best practices?

### Future-Proofing Questions

1. Will this system work with GPT-5, Claude 4, Gemini 2.0?
2. What if context windows expand to 1 million tokens? How would the architecture change?
3. What if multimodal AI becomes standard? How could AIDM v2 leverage images/audio?
4. What if AI agents become more autonomous? Could AIDM v2 modules become AI agents?
5. What emerging AI capabilities could revolutionize this system?

---

## Deliverables

Please provide the following in your analysis:

### 1. Executive Summary (2-3 pages)
- Overall system assessment (feasibility, quality, innovation)
- Top 5 strengths
- Top 5 weaknesses
- Critical path for improvement
- Recommended immediate actions

### 2. Architectural Analysis (10-15 pages)
- Module-by-module review
- Interdependency mapping
- Cohesion and coupling analysis
- Lazy-loading effectiveness
- Context management optimization
- Scalability assessment
- Identified architectural flaws
- Proposed architectural improvements

### 3. Narrative System Analysis (8-12 pages)
- Profile library coverage and quality
- Scale system completeness (11 scales)
- Trope library effectiveness (15 libraries)
- Profile blending mechanics
- Anime authenticity assessment
- Genre coverage gaps
- Scale 11 (POV) integration review
- Recommended profile additions

### 4. Technical Quality Analysis (5-8 pages)
- Documentation quality and completeness
- Code/schema quality
- Consistency and maintainability
- Technical debt inventory
- Testing and validation protocols
- Version management assessment
- Recommended technical improvements

### 5. User Experience Analysis (5-8 pages)
- Player onboarding assessment
- GM/user complexity evaluation
- Session Zero analysis
- Profile discovery usability
- Mid-campaign flexibility
- Accessibility barriers
- Recommended UX improvements

### 6. Performance & Scalability Analysis (5-8 pages)
- Token efficiency review
- Loading performance analysis
- Scalability limits identification
- Long-term campaign viability
- Optimization opportunities
- Bottleneck identification
- Recommended performance improvements

### 7. Gap Analysis & Roadmap (8-12 pages)
- Missing critical systems
- Incomplete module sections
- Profile/trope library gaps
- Feature prioritization matrix
- Version 2.1 recommendations (quick wins)
- Version 3.0 recommendations (major features)
- 12-month development roadmap
- 24-month strategic roadmap

### 8. Risk Assessment (5-8 pages)
- Identified vulnerabilities
- Failure mode analysis
- LLM dependency risks
- State corruption risks
- Module conflict risks
- Mitigation strategies
- Contingency planning

### 9. Competitive Analysis (5-8 pages)
- Market positioning
- Unique value propositions
- Industry comparison
- Innovation assessment
- Monetization potential
- Community potential
- Cross-media opportunities

### 10. Recommendations Summary (3-5 pages)
- Prioritized action items (top 20)
- Quick wins (implementable in 1-2 weeks)
- Medium-term improvements (1-3 months)
- Long-term strategic initiatives (6-12 months)
- Critical path to version 3.0
- Resource requirements
- Success metrics

---

## Analysis Standards

### Depth of Analysis
- Do not superficially review. Dig into specifics.
- Identify concrete examples of issues, not just abstract critiques.
- Provide actionable recommendations, not just observations.
- Consider edge cases, stress tests, and failure modes.
- Think systematically about cascading effects and unintended consequences.

### Critical Thinking
- Challenge assumptions in the system design.
- Identify hidden dependencies and brittleness.
- Question whether "best practices" are actually followed.
- Look for innovation opportunities the team may have missed.
- Consider perspectives from different user types (players, GMs, developers).

### Evidence-Based Analysis
- Reference specific files, line numbers, or sections.
- Compare against industry standards and best practices.
- Use concrete examples from the codebase.
- Quantify issues where possible (token counts, complexity metrics).

### Future-Oriented Thinking
- Consider how AI technology will evolve in 1-2 years.
- Anticipate user needs the system doesn't yet address.
- Identify architectural decisions that will age poorly.
- Propose innovative features that could differentiate the system.

---

## Context and Constraints

### What You Have Access To
- Full GitHub repository: https://github.com/deusversus/animerpg
- All markdown documentation files
- All JSON schemas
- Archive folder with historical development context
- Recent optimization work (October 13, 2025)

### What You Should Know
- The system is designed for use by LLMs (Claude, GPT-4), not direct human interaction
- The primary use case is running authentic anime-style TTRPG campaigns
- The development team is small (1-2 people) and resource-constrained
- The system is in production beta but actively maintained
- Recent work focused on token optimization (62.3% reduction in index files)
- The system uses a lazy-loading architecture to manage context efficiently
- Scale 11 (POV Distribution) is a recent addition (January 2025)

### Constraints to Consider
- LLM context windows (200K tokens typical, but only 20-30K active)
- Token costs ($0.01-0.10 per 1K tokens depending on model)
- Development resource limits (small team, limited time)
- Need for backward compatibility with existing campaigns
- User technical skill variance (from coding experts to non-technical players)

---

## Output Format

Please structure your analysis as a **comprehensive research report** with:

1. **Table of Contents** with page numbers
2. **Executive Summary** at the beginning
3. **Detailed sections** as outlined in Deliverables
4. **Appendices** for detailed data (file lists, token counts, dependency graphs)
5. **Bibliography** of referenced files and external sources
6. **Glossary** of technical terms and abbreviations

Use **clear headers, bullet points, tables, and diagrams** where appropriate. Prioritize readability and actionability.

---

## Final Notes

This is a **comprehensive deep research task**. Do not rush. Do not skim. The development team is seeking:

1. **Brutal honesty** - Point out flaws, even if they're fundamental
2. **Deep expertise** - Apply best practices from software engineering, game design, AI systems, and narrative theory
3. **Actionable insights** - Every critique should come with a proposed solution
4. **Innovation** - Identify opportunities the team hasn't considered
5. **Strategic thinking** - Consider long-term viability and competitive positioning

The goal is to produce a **definitive analysis** that will guide the next 12-24 months of development. Treat this as if you were a hired consultant producing a $50,000 research report.

---

## Additional Research Directives

### Test Case Scenarios

To validate system effectiveness, consider running these test scenarios mentally:

1. **Scenario 1: Hunter x Hunter Campaign**
   - Load hunter_x_hunter_profile.md + shonen_tropes.md + ki_lifeforce_systems.md
   - Create 4 PCs with Nen abilities (Enhancer, Emitter, Manipulator, Conjurer)
   - Run a 3-session arc: Hunter Exam → Nen training → Phantom Troupe encounter
   - Verify: Tactical combat depth, Nen condition mechanics, tournament arc structure, power scaling (from Gon/Killua weak → Meruem godlike)

2. **Scenario 2: Profile Blending - Attack on Titan + My Hero Academia**
   - Blend attack_on_titan_profile.md (grim, militaristic, low power fantasy) with my_hero_academia_profile.md (hopeful, school life, high power fantasy)
   - How do contradictory scales reconcile? (Tone: Cynical 8 vs Hopeful 7, Power Fantasy: Struggle 3 vs Power Fantasy 7)
   - Does the blend create a coherent world or incoherent mess?

3. **Scenario 3: 100-Session Epic Campaign**
   - Start Session Zero with naruto_profile.md
   - Simulate 100 sessions of memory accumulation
   - At what point does memory compression lose critical information?
   - Can session_export_schema.json handle 100 NPCs, 50 completed quests, 20 active quests, faction reputation with 10 factions?

4. **Scenario 4: Research Enforcement Test**
   - Player requests: "I want to play in the world of obscure anime 'Kaiju No. 8'"
   - Does Module 06 (Session Zero) + Module 07 (Anime Integration) force web research BEFORE character creation?
   - If research fails, does the system gracefully degrade or hallucinate?

5. **Scenario 5: Cross-LLM Compatibility**
   - Load identical AIDM setup on Claude, GPT-4, and Gemini
   - Run same Session Zero scenario
   - Compare: Research enforcement reliability, profile blending behavior, combat narration quality, memory management
   - Identify LLM-specific failure modes

6. **Scenario 6: New Player Onboarding**
   - Simulate a player with zero anime knowledge and zero TTRPG experience
   - Is Session Zero overwhelming? (21 profile choices, 16 genre options, 11 scale calibration)
   - Can PROFILE_INDEX.md help, or does it add cognitive load?

7. **Scenario 7: Mid-Campaign Tone Shift**
   - Start campaign with konosuba_profile.md (comedy, parody)
   - After 20 sessions, player requests tone shift to darker (jujutsu_kaisen_profile.md)
   - Can Module 13 hot-swap profiles mid-campaign? Does memory reconcile the shift?

### Edge Case Testing

Identify edge cases where the system might break:

1. **Power System Conflicts**: Player wants to blend Naruto chakra + Jujutsu Kaisen cursed energy. Do ki_lifeforce_systems.md and soul_spirit_systems.md conflict or harmonize?

2. **Profile Contradiction Limits**: What happens if blending 3 maximally contradictory profiles? (Mushishi slow contemplative + One Punch Man absurd action + Death Note psychological thriller)

3. **NPC Knowledge Boundaries**: Player tells NPC secret. Later, asks different NPC who shouldn't know. Does npc_schema.json track knowledge boundaries, or will LLM leak information?

4. **Quest State Corruption**: Player completes Quest A which unlocks Quest B. Then player reloads old save where Quest A was incomplete. Does the system detect inconsistency?

5. **Faction Reputation Without Schema**: Factions exist in world_state_schema.json, but no faction reputation mechanics. How does Module 04 (NPC Intelligence) handle faction-affiliated NPCs reacting to player reputation?

6. **Context Window Overflow**: If campaign hits 200K token context limit, which modules get unloaded? Does TIER 3 library unloading work gracefully, or does it cause amnesia?

7. **Schema Version Migration**: Player has save file from AIDM v2.0 (8 schemas). AIDM v2.1 adds quest_schema.json (9 schemas). Can old save load into new system?

### Comparative Benchmarks

Compare AIDM v2 against these systems to identify strengths/weaknesses:

1. **AI Dungeon / NovelAI**: How does AIDM's structure compare to freeform AI narrative generators?
2. **Big Eyes Small Mouth (BESM)**: Traditional anime TTRPG. Does AIDM capture anime feel better than BESM?
3. **Powered by the Apocalypse (PbtA)**: Narrative-focused TTRPG engine. Does AIDM's narrative systems match PbtA quality?
4. **Fate Core**: Universal RPG system. Does AIDM's modularity compare to Fate's flexibility?
5. **Persona 5 Social Link System**: Video game social mechanics. Could AIDM implement Persona-style relationship building?

---

**Begin your comprehensive analysis. Apply maximum analytical rigor. The development team depends on your expertise to guide the next 12-24 months of AIDM v2 evolution.**
