# AIDM v2.0 → v2.1 - Development Continuation Guide

**Last Updated**: 2025-10-27  
**Current Version**: v2.0 MVP (Production Ready)  
**Next Target**: v2.1 Core Systems (Q4 2025 - Q1 2026)

## 📊 System Status Overview

**Core Foundation Complete** ✅:
- 14 instruction modules (~54k tokens after 62.3% optimization)
- 8 JSON schemas (~33k tokens)  
- 20 narrative profiles (Naruto, HxH, AoT, Death Note, MHA, Demon Slayer, etc.)
- 15 genre trope libraries (isekai, shonen, seinen, shoujo_romance, slice_of_life, mecha, sports, dark_fantasy, psychological, action, comedy, drama, horror, mystery, supernatural)
- Token Budget: ~87k base (43% of 200k context) - Highly efficient ✅

**Validation Status** ⚠️:
- ✅ 2/8 acceptance tests PASSED (TEST-001 Session Zero, TEST-004 Player Agency)
- ⚠️ 6/8 tests INCOMPLETE (Multi-Anime Fusion, Session Persistence, Memory Coherence, Error Recovery, Genre Adaptation, Research Protocol)
- ⚠️ Long-term play (10+ sessions) untested
- ⚠️ Extreme scale (100+ NPCs/quests) theoretical

**Primary Guide**: `docs/ROADMAP.md` (comprehensive Phase 1-9 deep research integration)

---

## 🎯 CURRENT PRIORITY: Production Validation (4 weeks)

**WHY THIS FIRST**: System has strong architectural foundation but only 2/8 acceptance tests passed. Cannot add new features until validation baseline complete.

### Immediate Tasks (Priority 1)

1. **TEST-002: Multi-Anime Fusion** (1 week)
   - Test 3-anime blend (Naruto + MHA + Solo Leveling)
   - Verify power system harmonization
   - Check for rule contradictions
   - Document edge cases

2. **TEST-003: Session Persistence** (1 week)
   - Run 20+ turn session with save/load cycles
   - Verify all state preserved (NPCs, quests, memory)
   - Test schema validation on import
   - Check memory compression triggers

3. **TEST-005: Memory Coherence** (1 week)
   - Validate heat_index decay over extended play
   - Test memory retrieval accuracy
   - Verify compression doesn't lose critical info
   - Check 100+ thread handling

4. **TEST-006: Error Recovery** (3 days)
   - Test edge cases (invalid inputs, corrupted state)
   - Verify graceful degradation
   - Check fallback modes
   - Validate error messages

5. **TEST-007: Genre Adaptation** (3 days)
   - Test genre switching mid-campaign
   - Verify trope library loading
   - Check narrative consistency
   - Validate profile blending

6. **TEST-008: Research Protocol** (3 days)
   - Test with fake anime (must not hallucinate)
   - Verify web research protocol
   - Check player confirmation loop
   - Validate fallback behavior

**Success Criteria**:
- All 8 tests show PASS status
- Root cause analysis documented for failures
- Prompt adjustments implemented
- Known limitations documented

---

## � NEXT PRIORITY: Phase 2.1 - Core Systems (4-6 months)

**Context**: v2.0 focused on narrative authenticity. Now restoring critical gameplay mechanics intentionally deferred.


**High Priority Systems** (After P1 validation complete):

1. **Quest Management System** (~2-3 weeks)
   - Create quest_schema.json (branching, dependencies, time limits)
   - Expand Module 03 (State Manager) with quest tracking
   - Integrate Module 05 (Narrative Systems) for quest generation
   - Module 09 automated quest XP integration
   - **Current Gap**: Simple objective arrays, no branching/dependencies

2. **Faction/Reputation System** (~2 weeks)
   - Create faction_schema.json (player reputation, faction politics)
   - Expand Module 04 (NPC Intelligence) with faction-influenced disposition
   - Automated faction standing cascades
   - **Current Gap**: Individual NPC affinity exists, faction-level missing

3. **Economy System** (~2 weeks)
   - Create economy_schema.json (currency, transactions, pricing)
   - Expand Module 03 state tracking for monetary transactions
   - Merchant NPC integration with Module 04
   - **Current Gap**: Inventory exists but no monetary mechanics

4. **Combat Enhancements** (~3 weeks)
   - Death/resurrection mechanics (death saves, injury tables)
   - Combat maneuvers (grapple, disarm, called shots)
   - Training system formalization
   - Tournament framework

**Medium Priority** (Phase 2.5 - Q1 2026):
- Romance mechanics, timekeeping automation, mass combat
- Crafting, guilds, base building (port from v1 as TIER 3 libraries)

**See**: `docs/ROADMAP.md` for complete Phase 2.1 breakdown with all Phase 1-9 tracking details

---

## 📋 System Architecture Quick Reference

### Core Instruction Modules (14 files)
- `00_system_initialization.md` - Bootstrap & lazy-loading
- `01_cognitive_engine.md` - Intent classification
- `02_learning_engine.md` - Memory management
- `03_state_manager.md` - State validation/persistence
- `04_npc_intelligence.md` - NPC behavior/affinity
- `05_narrative_systems.md` - Story hooks/pacing
- `06_session_zero.md` - Character creation
- `07_anime_integration.md` - Research & harmonization
- `08_combat_resolution.md` - Battle mechanics
- `09_progression_systems.md` - XP & leveling
- `10_error_recovery.md` - Error handling
- `11_dice_resolution.md` - RNG transparency
- `12_player_agency.md` - Sacred choice rule
- `13_narrative_calibration.md` - Narrative DNA system
- `CORE_AIDM_INSTRUCTIONS.md` - Master control

### Schemas (8 JSON files)
- `character_schema.json` - Stats/inventory/skills/quests
- `world_state_schema.json` - Time/locations/factions/economy
- `npc_schema.json` - 40+ field NPC profiles
- `memory_thread_schema.json` - Heat_index system
- `narrative_profile_schema.json` - Anime DNA
- `anime_world_schema.json` - External anime integration
- `power_system_schema.json` - Power mechanics
- `session_export_schema.json` - Holistic save format

### Content Libraries
**Power Systems** (5 files): mana/magic, ki/lifeforce, soul/spirit, psionic/psychic, power tier reference

**Genre Tropes** (15 files): isekai, shonen, seinen, shoujo_romance, slice_of_life, mecha, sports, dark_fantasy, psychological, action, comedy, drama, horror, mystery, supernatural

**Common Mechanics** (3 files): stat_frameworks, leveling_curves, skill_taxonomies

**Narrative Profiles** (20 files): Naruto, Hunter x Hunter, Attack on Titan, Death Note, My Hero Academia, Demon Slayer, Fullmetal Alchemist, Sword Art Online, Tokyo Ghoul, Steins;Gate, Code Geass, JoJo, One Punch Man, Solo Leveling, Neon Genesis Evangelion, Haikyuu!!, Pokemon, Konosuba, Overlord, Re:Zero

---

## 🔑 Key Design Principles

1. **Player Agency is Sacred** - Choices must matter, railroading forbidden
2. **Emergent > Predetermined** - React to players, don't force plots
3. **Consistency is Critical** - State must remain logically coherent
4. **Fail Safely** - Errors handled gracefully, never crash
5. **Research First** - Never fake anime knowledge (AUTOMATIC, BLOCKING)
6. **Yes, And...** - Default to enabling creativity, not blocking it
7. **100% Information Parity** - Zero lossy compression during optimization
8. **Machine-Interpreter Oriented** - Optimize for LLM parsing, not decoration

---

## 📚 Essential Documentation

- **ROADMAP.md**: Complete Phase 1-9 deep research integration, all priorities with full tracking details
- **ARCHITECTURE.md**: Complete system design
- **STATE.md**: Current status, comprehensive changelog
- **SCOPE.md**: v2.0 features and acceptance tests
- **CORE_AIDM_INSTRUCTIONS.md**: Master control file

---

## 🎯 Where to Start

**RIGHT NOW**: 
1. Review `docs/ROADMAP.md` Phase 2.1 section
2. Begin Phase 2.1a: Architectural fixes (schema migration, automated cascades)
3. Implement Phase 2.1b: Quest Management System
4. Continue through Phase 2.1c-f (Faction, Economy, Combat, Validation)

**Testing Deferred**: 6 remaining acceptance tests shelved until after Phase 2.1 feature work complete

**GitHub Repository**: https://github.com/deusversus/animerpg

---

**CURRENT CONTEXT: v2.0 MVP complete with strong architectural foundation (62.3% token optimization, 20 profiles, 15 genre libraries, 8 schemas, 14 modules). Testing shelved (2/8 passed, 6 deferred to post-Phase 2.1). Current priority: Phase 2.1 core systems development (Quest, Faction, Economy, Combat). See ROADMAP.md for comprehensive guidance with ALL Phase 1-9 tracking details preserved.** 🎯
