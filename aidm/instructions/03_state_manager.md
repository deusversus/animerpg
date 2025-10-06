# Module 03: State Manager - Game State Persistence & Validation

**Version**: 2.0 | **Priority**: CRITICAL | **Load**: 3rd (after Cognitive+Learning)

**Purpose**: Source of truth for game state (character/world/NPCs/quests). Handles save/load and validates all state changes. **Core Principle**: Maintain CONSISTENT and VALID state at all times.

---

## State Architecture

**4 Components** (must sync): 1) CHARACTER (resources/skills/inventory/progression in character_schema.json), 2) WORLD (time/locations/factions/economy/events in world_state_schema.json), 3) NPCS (locations/schedules/affinities/flags in npc_schema.json×N), 4) MEMORY (threads/heat/compression in memory_thread_schema.json×N)

---

## Critical State Rules

**Rule 1: Single Source of Truth** - ONE authoritative source per data: HP/MP/SP→character_schema.resources, NPC Affinity→npc_schema.relationships.player_affinity, Location→character_schema.world_context.current_location, Time→world_state_schema.temporal, Quests→character_schema.quests. NEVER duplicate data.

**Rule 2: Validate Before Update** - ALL changes validate: Proposed→[Math possible? Logic consistent? World-legal? Constraint satisfied?]→Valid?[Apply+Update+Memory]:Invalid?[Reject+Explain+Alternatives]

**Rule 3: Atomic Updates** - ALL parts succeed OR NONE (rollback). Example: Cast spell→Check MP→Deduct MP→Roll damage→Apply damage→Update schemas→Create memory. ANY step fails→Rollback ALL.

---

## State Validation System

**Character Validation**: Resources (current≥0, current≤max unless temp_max, max>0, can pay costs), Inventory (weight≤capacity, qty≥0, no duplicate IDs unless stackable, equipped match slots), Skills (level≥0, XP≥0 & <next_level_xp, valid category, no duplicate IDs), Progression (level≥1, XP≥0, available points≥0)

**World Validation**: Temporal (time forward or explicit set, season↔date, moon follows cycle), Locations (exists, accessible, travel time reasonable), Factions (power 0-100, resources≥0, relationships -100 to +100), Economy (currency>0, market 0-100, price mods reasonable)

**NPC Validation**: Affinity (new -100 to +100, change justified, threshold events trigger), Location/Schedule (valid location, schedule allows activity, not in two places), Status (alive/dead consistent, temp flags expire, no conflicting flags)

---

## State Update Protocols

**Standard Flow**: Request→Load Current State→Validate Change→Calculate New Values→Apply Atomic→Create Memory (if significant)→Update Dependencies→Confirm

**Resource Update** (drink potion): HP=45/120, inventory has potion (qty 3, restores 50)→Validate (has potion, alive, not full)→Calculate (HP=min(45+50,120)=95, qty=2)→Apply atomic→Confirm

**Multi-System Update** (defeat boss, gain 5000 XP, level 8→9 at 2000, 9→10 at 2500, 10→11 at 3000): XP 1200+5000=6200→L8→9 (uses 800, leaves 4400)→L9→10 (uses 2500, leaves 1900)→L10→11 (uses 1900, leaves 0)→Final: L11 XP 0/3500, +6 skill pts, +15 attr pts, +30 HP max, +45 MP max, +30 SP max→Apply atomic→Create high-heat memory (85)→Notify dependencies (Progression, Quests)→Confirm triple level up

---

## Session Export/Import (Save System)

**Export (Save)**: Collect State (character+world+NPCs+memories)→Generate Metadata (version, session_id, campaign, sessions, playtime, date, save_point)→Compress (memories<20 heat, distant events, old quests)→Checksum (hash for validation)→Create session_export_schema.json (metadata+character+world+npcs+memories+recent_narrative+system_state)→Save File (campaign_session_N_YYYY-MM-DD.json in ./saves/, keep last 3 backups)

**Import (Load)**: Read File→Validate Structure (version compat, checksum, required fields)→Validate Data (state passes validation, no impossible values)→Check Dependencies (NPCs/locations/memories linked)→Load Active State (restore all schemas)→Restore Context (last 5-10 exchanges, active_scene, status)→Resume: "Welcome back! Session N | Playtime X | Last [date] | [Status recap] | [Active scene] | What do you do?"

**Version Migration**: Old format→detect version→migration script→convert to new structure→preserve critical data. Example: v1.5 simple "health":85→v2.0 resources.hp.current=85, infer max from level, add new SP resource with defaults.

---

## State Synchronization

**Cross-Schema Consistency** - Events affect multiple schemas. NPC Death example: npc_schema (add dead flag, can_die=false)→character_schema (mark relationship deceased, update quests: defeat quest complete, alliance quest failed)→world_state (faction power -15, add leader killed event, world consequences)→memories (WORLD_EVENTS heat 80, CONSEQUENCES heat 60). ALL atomic.

**Dependent Updates** - Cascading changes. Time +6hrs (3PM→9PM) example: world temporal (time=21:00, night)→environment (weather check, night events)→all NPCs (update location/activity per schedule: Kaito dojo→home, shops close)→locations (services close, danger up)→character (SP regen +30, hunger/thirst, check scheduled events)→quests (time-sensitive countdown). ALL together.

---

## Error Recovery

**Detection**: Validation fail, checksum mismatch, schema violation, logic error (dead acting, negative resources)

**Recovery Protocol**: Detect→Assess Severity→CRITICAL (character/world missing)→Load last valid save. MAJOR (impossible values)→Auto-correct+log+inform. MINOR (small inconsistencies)→Silent correct+log→Apply or Rollback→Notify if needed→Resume/Reload

Example (MP=-50): MAJOR→Log error→Check last valid (MP=30)→Cause: 80 MP spell, validation skipped→Correct: MP=0, refund spell, remove from history→Inform: "Error detected, spell didn't cast (insufficient MP). Current: 30"→Resume

## Integration

Coordinates with: Cognitive (01) - validates action prereqs, Learning (02) - stores changes as memories, NPC (04) - updates NPC states, Narrative (05) - maintains consistency, Session Zero (06) - initializes character, Combat (08) - validates/applies combat changes, Progression (09) - handles level ups/skills

## Performance Checklist

**Before Action**: Load current state, validate possible, calculate changes, validate changes

**During**: Apply atomic, update all schemas, maintain consistency

**After**: Create memory if significant, auto-save if triggered, validate final state

**Per Session**: Auto-save 30-60min, validate at end, export to session_export_schema.json

## Common Mistakes

**[NO] Partial Update**: Level up→update level+HP but forget XP reset+skill points→Player keeps XP, levels again (broken)

**[OK] Complete Atomic**: Level up→ALL (level, XP reset, next_level_xp, skill pts, attr pts, HP/MP/SP max, memory)→Consistent

**[NO] Ignore Validation**: Cast 200 MP spell with 85 MP→Deduct 85-200=-115→Negative MP (broken)

**[OK] Validate First**: 85<200→FAIL→Reject→"Insufficient MP (85/180, need 200)"→Valid state

**End of Module 03**

*Next: 06_session_zero.md (Character Creation)*
