# Module 03: State Manager - Game State Persistence & Validation

**Version**: 2.0 | **Priority**: CRITICAL | **Load**: 3rd (after Cognitive+Learning)

**Purpose**: Source of truth for game state (character/world/NPCs/quests). Handles save/load and validates all state changes. **Core Principle**: Maintain CONSISTENT and VALID state at all times.

---

## State Architecture

**5 Components** (must sync): 1) CHARACTER (resources/skills/inventory/progression/**narrative_profile** in character_schema.json), 2) WORLD (time/locations/factions/economy/events in world_state_schema.json), 3) NPCS (locations/schedules/affinities/flags in npc_schema.json×N), 4) MEMORY (threads/heat/compression in memory_thread_schema.json×N), 5) NARRATIVE_PROFILE (scales/tropes/scaffolding/adjustments tracked in character_schema.narrative_profile section)

---

## Narrative Profile State Tracking

**Purpose**: Track active narrative calibration from Module 13 for consistent tone/pacing across sessions. **CRITICAL for generated profiles** (must persist full data, not just file reference).

### State Structure (Add to character_schema.json)

```json
{
  "narrative_profile": {
    "profile_id": "narrative_dandadan",
    "profile_type": "pre-made",  // "pre-made" or "generated"
    "profile_source": "aidm/libraries/narrative_profiles/dandadan_profile.md",
    
    // Narrative Scales (0-10, extracted from Module 13)
    "scales": {
      "introspection_vs_action": 3,
      "comedy_vs_drama": 4,
      "simple_vs_complex": 6,
      "power_fantasy_vs_struggle": 4,
      "explained_vs_mysterious": 4,
      "fast_paced_vs_slow_burn": 2,
      "episodic_vs_serialized": 7,
      "grounded_vs_absurd": 2,
      "tactical_vs_instinctive": 5,
      "hopeful_vs_cynical": 5
    },
    
    // Enabled Tropes (15 switches, ON/OFF)
    "tropes": {
      "tournament_arc": false,
      "training_montage": true,
      "power_of_friendship": true,
      "mentor_death": false,
      "chosen_one": false,
      "tragic_backstory": true,
      "redemption_arc": false,
      "betrayal": false,
      "sacrifice": true,
      "transformation": true,
      "forbidden_technique": false,
      "time_loop": false,
      "false_identity": false,
      "ensemble_focus": true,
      "slow_burn_romance": true
    },
    
    // Mechanical Scaffolding (Applied mappings from profile)
    "mechanical_scaffolding": {
      "power_level_model": "accelerated",  // "instant_op" / "accelerated" / "modest"
      "growth_tier_target": "tier_3_by_session_15",
      "xp_model": "high",  // "high" (1K-1.5K) / "standard" (600-900) / "low" (300-500) / "milestone"
      "stat_framework": "6-stat",  // "3-stat" / "6-stat" / "6-stat+custom"
      "power_systems": ["psionic_psychic_systems", "soul_spirit_systems"],
      "combat_narration_style": {
        "spectacle_percent": 70,
        "tactical_percent": 20,
        "banter_percent": 10
      },
      "attribute_priorities": ["DEX", "CON", "INT"],
      "resource_formulas": {
        "mp_formula": "power_level * 3",
        "sp_formula": "10_activation_plus_5_per_round"
      }
    },
    
    // Adjustments Log (Player preferences during play)
    "adjustments_log": [
      {
        "session": 3,
        "adjustment": "Reduced drama scale 6→4",
        "reason": "Player: 'needs more comedy, less serious'",
        "timestamp": "2025-10-01T14:30:00Z"
      },
      {
        "session": 5,
        "adjustment": "Increased absurdity 8→9",
        "reason": "Player enjoyed weirder alien encounters",
        "timestamp": "2025-10-03T16:45:00Z"
      }
    ],
    
    // Metadata
    "last_calibration_date": "2025-10-01T12:00:00Z",
    "calibration_source": "session_zero",  // "session_zero" / "mid-campaign" / "generated"
    "generation_method": null  // null for pre-made, "module_07_research" for generated
  }
}
```

### Pre-Made vs Generated Profiles

**Pre-Made Profile** (DanDaDan, Hunter x Hunter, etc.):
- `profile_type`: "pre-made"
- `profile_id`: Reference ID (e.g., "narrative_dandadan")
- `profile_source`: File path (can load from file on session restart)
- Scales/tropes: Load from file, store in state for adjustments
- Mechanical scaffolding: Load from file's scaffolding section
- **Lightweight storage**: Only ID + adjustments persist, reference file for base data

**Generated Profile** (Chainsaw Man, Frieren, custom anime):
- `profile_type`: "generated"
- `profile_id`: Generated ID (e.g., "narrative_generated_chainsaw_man")
- `profile_source`: null (no file reference)
- Scales/tropes: **MUST persist full data** (can't reload from file)
- Mechanical scaffolding: **MUST persist all mappings** (generated via Module 13 rules)
- **Full storage**: ALL data stored in state (no file to reference)
- `generation_method`: "module_07_research" (shows how it was created)

### Validation Rules

**On State Load** (session restart):
```
1. Check profile_type
2. IF "pre-made":
   - Validate profile_id exists in library
   - Load base data from file
   - Apply adjustments_log on top
   - Warn if file missing (suggest fallback or regeneration)
3. IF "generated":
   - Validate scales/tropes/scaffolding present in state
   - Error if missing (can't reload, no file reference)
   - Suggest fallback to similar pre-made profile
4. Validate scales (all 0-10)
5. Validate tropes (all boolean)
6. Validate mechanical_scaffolding fields present
```

**On Profile Change** (mid-campaign calibration):
```
1. Validate new scales/tropes
2. Create adjustment log entry
3. Update mechanical_scaffolding if mappings change
4. Store in NARRATIVE_STYLE memory (Module 02)
5. Apply atomically
```

### Export/Import Handling

**Export (Save File)**:
```json
{
  "session_export_schema": {
    "character": {
      "narrative_profile": {
        // FULL narrative_profile structure here
        // For pre-made: ID + adjustments (lightweight)
        // For generated: FULL data (critical, no file reference)
      }
    }
  }
}
```

**Import (Load File)**:
```
1. Load narrative_profile from export
2. Validate profile_type
3. IF pre-made → Load base from file, apply adjustments
4. IF generated → Use state data directly (no file)
5. Validate all fields
6. Restore to active state
```

### Integration with Module 13

**Session Zero Flow**:
```
1. Module 06 (Session Zero) asks: "Narrative calibration?"
2. Player chooses:
   a) Pre-made profile (DanDaDan, HxH, etc.)
      → Load from file
      → Store ID + base scales/tropes in state
      → Load mechanical scaffolding from profile
   
   b) Generate from anime (Chainsaw Man, etc.)
      → Module 07 research anime
      → Module 13 extract scales/tropes
      → Module 13 apply scaffolding rules (map to mechanics)
      → Store FULL generated profile in state
   
   c) Custom/No calibration
      → Default scales (all 5), no tropes enabled
      → Standard mechanical defaults
      → Store minimal profile in state

3. Apply mechanical scaffolding:
   - Set XP model in Module 09
   - Set power level model in Module 12
   - Configure combat narration in Module 08
   - Select power systems from libraries

4. Save to character_schema.narrative_profile
```

**Mid-Campaign Adjustment Flow**:
```
1. Player: "Can we add more comedy? This is too serious."
2. Module 02 creates NARRATIVE_STYLE memory (heat 70)
3. Module 03 updates state:
   - scales.comedy_vs_drama: 6 → 4 (more comedy)
   - adjustments_log: Add entry (session X, reason, timestamp)
4. Module 13 applies change to narration
5. Export updated profile to save file
```

### Critical Requirements

**MUST PERSIST for Generated Profiles**:
- ✅ All 10 scales (full values)
- ✅ All 15 tropes (full switches)
- ✅ Complete mechanical_scaffolding (all mappings)
- ✅ Adjustments log (player preferences)
- ✅ Generation metadata (how it was created)

**CAN REFERENCE for Pre-Made Profiles**:
- ✅ Profile ID only (lightweight)
- ✅ Load base data from file on restart
- ✅ Store adjustments in state
- ⚠️ Warn if file missing (handle gracefully)

**Error Handling**:
```
ERROR: Pre-made profile file missing
→ Check: Does dandadan_profile.md exist?
→ NO: Offer options:
   a) Regenerate via Module 07+13 (convert to generated type)
   b) Use similar profile (suggest JJK for DanDaDan)
   c) Reset to defaults
→ Log warning, don't crash session
```

---

## Critical State Rules

**Rule 1: Single Source of Truth** - ONE authoritative source per data: HP/MP/SP→character_schema.resources, NPC Affinity→npc_schema.relationships.player_affinity, Location→character_schema.world_context.current_location, Time→world_state_schema.temporal, Quests→character_schema.quests. NEVER duplicate data.

**Rule 2: Validate Before Update** - ALL changes validate: Proposed→[Math possible? Logic consistent? World-legal? Constraint satisfied?]→Valid?[Apply+Update+Memory]:Invalid?[Reject+Explain+Alternatives]

**Rule 3: Atomic Updates** - ALL parts succeed OR NONE (rollback). Example: Cast spell→Check MP→Deduct MP→Roll damage→Apply damage→Update schemas→Create memory. ANY step fails→Rollback ALL.

---

## State Validation System

**Character Validation**: Resources (current≥0, current≤max unless temp_max, max>0, can pay costs), Inventory (weight≤capacity, qty≥0, no duplicate IDs unless stackable, equipped match slots), Skills (level≥0, XP≥0 & <next_level_xp, valid category, no duplicate IDs), Progression (level≥1, XP≥0, available points≥0), **Narrative Profile** (profile_type "pre-made" or "generated", pre-made→profile_id exists in library, generated→ALL scales/tropes/scaffolding present, scales 0-10, tropes boolean, mechanical_scaffolding valid models, adjustments_log sessions ascending)

**World Validation**: Temporal (time forward or explicit set, season↔date, moon follows cycle), Locations (exists, accessible, travel time reasonable), Factions (power 0-100, resources≥0, relationships -100 to +100), Economy (currency>0, market 0-100, price mods reasonable)

**NPC Validation**: Affinity (new -100 to +100, change justified, threshold events trigger), Location/Schedule (valid location, schedule allows activity, not in two places), Status (alive/dead consistent, temp flags expire, no conflicting flags)

---

## State Update Protocols

**Standard Flow**: Request→Load Current State→Validate Change→Calculate New Values→Apply Atomic→Create Memory (if significant)→Update Dependencies→Confirm

**Resource Update** (drink potion): HP=45/120, inventory has potion (qty 3, restores 50)→Validate (has potion, alive, not full)→Calculate (HP=min(45+50,120)=95, qty=2)→Apply atomic→Confirm

**Multi-System Update** (defeat boss, gain 5000 XP, level 8→9 at 2000, 9→10 at 2500, 10→11 at 3000): XP 1200+5000=6200→L8→9 (uses 800, leaves 4400)→L9→10 (uses 2500, leaves 1900)→L10→11 (uses 1900, leaves 0)→Final: L11 XP 0/3500, +6 skill pts, +15 attr pts, +30 HP max, +45 MP max, +30 SP max→Apply atomic→Create high-heat memory (85)→Notify dependencies (Progression, Quests)→Confirm triple level up

**Narrative Profile Update** (player requests more comedy mid-campaign): Current profile comedy_vs_drama=6, player feedback "needs more comedy, too serious"→Validate (scale exists, new value 0-10, propose 4)→Calculate (comedy_vs_drama 6→4, update narration style +20% comedic beats)→Apply atomic (character_schema.narrative_profile.scales.comedy_vs_drama=4, add adjustments_log entry: session 5, "increased comedy 6→4", reason "player feedback: more levity", timestamp)→Create memory (NARRATIVE_STYLE heat 40: "Tone adjusted: more comedy, less serious drama")→Update dependencies (Module 06 narration style +20% banter, Module 04 NPC dialogue more lighthearted)→Confirm adjustment applied

---

## Quest Management System

**Purpose**: Centralized quest state tracking with branching, dependencies, automated XP rewards, and cascade integration. All quests stored in `world_state.narrative_state.quests`, characters reference by ID only.

### Quest CRUD Operations

**create_quest(quest_data)**:
- Validate against quest_schema.json
- Generate quest_id if not provided (pattern: `quest_[random]`)
- Set metadata.created_at timestamp
- Add to world_state.narrative_state.quests
- If auto-offer: Add quest_id to character.quests.available
- Create memory thread (category: quests, heat: 40-60 based on importance)

**accept_quest(character_id, quest_id)**:
- Validate quest exists and status="available"
- Move quest_id from character.quests.available → character.quests.active
- Update quest status: "available" → "active"
- Set quest.metadata.accepted_at timestamp
- Add event to quest.metadata.event_log
- Create memory thread (category: quests, heat: 50, "Accepted [quest title]")

**update_quest_objective(quest_id, objective_id, progress)**:
- Validate quest exists, objective exists
- Check objective.dependencies (all completed?)
- If dependency incomplete: Reject with "Must complete [dependency] first"
- Update objective.progress (or set completed=true if no progress tracking)
- If objective has mutually_exclusive_with: Block those objectives
- Check if all required objectives completed:
  - If yes: Update quest status → "ready_to_complete"
  - Add event to quest.metadata.event_log
- Validate quest hasn't exceeded time_limit
- Check fail_conditions triggered by update (e.g., item_lost)

**complete_quest(quest_id, character_id)**:
- Validate quest status="ready_to_complete" (all required objectives done)
- Move quest_id: character.quests.active → character.quests.completed
- Update quest status → "completed"
- Set quest.metadata.completed_at timestamp
- **Automated Rewards Distribution**:
  - XP: Add quest.rewards.xp to character.progression.current_xp
  - Items: Add quest.rewards.items[] to character.inventory
  - Currency: Add quest.rewards.currency{} to character.inventory.currency
  - Reputation: Update character.faction_reputation per quest.rewards.reputation
  - Skills: Unlock quest.rewards.skills[] in character.skills.available_skills
- **Quest Chain Activation**:
  - For each quest_id in quest.rewards.unlocks[]:
    - Create or activate child quest
    - Add to character.quests.available
- **Cascade Trigger**: Create "quest_completion" cascade (see CASCADE_SYSTEM_DESIGN.md)
  - Update NPCs with associated_quests
  - Check world impact (faction power, location changes)
  - Create memory thread (category: quests, heat: 60-80, "Completed [title]")
- Add event to quest.metadata.event_log

**fail_quest(quest_id, character_id, reason)**:
- Validate quest exists and not already completed/failed
- Move quest_id: character.quests.active → character.quests.failed[]
- Add failure object: {quest_id, reason, failed_at}
- Update quest status → "failed"
- Set quest.metadata.failed_at timestamp
- Set quest.metadata.failure_reason
- Create memory thread (category: quests, heat: 50-70, "Failed [title]: [reason]")
- Add event to quest.metadata.event_log

**check_fail_conditions(quest_id)**:
- Called automatically by cascades (NPC death, location destruction, etc.)
- For each condition in quest.fail_conditions[]:
  - Evaluate condition_type:
    - npc_death: Check if parameters.npc_id is dead
    - time_expired: Check current time > quest.time_limit
    - location_destroyed: Check if parameters.location_id destroyed
    - item_lost: Check if parameters.item_id not in inventory
    - reputation_threshold: Check faction reputation below threshold
    - custom: Evaluate custom logic
  - If condition TRUE: fail_quest(quest_id, reason=condition.description)

### Quest Dependency Resolution

**Objective Dependencies**:
- Before unlocking objective: Check all objective.dependencies[] completed
- If incomplete: Keep objective hidden (if hidden=true) or show as locked
- Example: "Objective 2 (Defeat Boss) requires Objective 1 (Find Weakness) to complete first"

**Quest Chain Dependencies**:
- quest.branching.parent_quest: This quest unlocks after parent completes
- quest.branching.child_quests[]: These quests unlock when this completes
- Stored in quest.rewards.unlocks[] for automation

**Mutually Exclusive Objectives**:
- When objective A completed: All objectives in A.mutually_exclusive_with[] become impossible
- Mark blocked objectives with "BLOCKED BY [objective A]" in quest log
- Example: "Save villagers" vs "Retrieve artifact" - can't do both

### Quest Branching System

**Choice-Based Branching**:
- quest.branching.choices[] defines decision points
- When player makes choice:
  - Unlock objectives in choice.unlocks_objectives[]
  - Block objectives in choice.blocks_objectives[]
  - Apply choice.reputation_impact to factions
  - Add choice to quest.metadata.event_log

**Dynamic Quest Paths**:
- Objectives can unlock different quest outcomes
- Example: Quest "Investigate Murder"
  - Objective A: Accuse noble → Unlocks "Political Intrigue" child quest
  - Objective B: Accuse commoner → Unlocks "Street Justice" child quest
  - Mutually exclusive outcomes based on player choice

### Automated XP Integration

**On Quest Completion** (Module 09 Coordination):
- Read quest.rewards.xp
- Apply difficulty multiplier if needed (epic quest = 1.5x base XP)
- Add to character.progression.current_xp
- Add XP log entry: {source: "quest", quest_id, amount, timestamp}
- Check level up threshold: If current_xp ≥ next_level_xp → Trigger level up cascade
- **No manual XP tracking required** - fully automated

### Quest Compression (Memory Management)

**When to Compress** (10+ active quests):
- Bundle related quests (same faction, same location)
- Summarize completed/failed quests from 5+ sessions ago
- Maintain active quests in full detail
- Store compressed data in memory threads (category: quests, heat: 20-30)

**Compression Logic**:
- Active quests: Never compress (full detail always)
- Recent completed (last 3 sessions): Keep full quest object
- Old completed (5+ sessions): Summarize to: {quest_id, title, completion_date, key_rewards}
- Failed quests: Always compress to: {quest_id, title, failure_reason, failed_date}

### Time-Limited Quests

**Deadline Tracking**:
- quest.time_limit (ISO 8601 timestamp)
- Check on every world.temporal.current_time update
- If current_time > time_limit: Trigger fail_condition "time_expired"

**Narrative Warnings** (Module 05 Coordination):
- 75% time remaining: No warning
- 50% time remaining: Subtle narrative mention
- 25% time remaining: Explicit warning ("Quest will fail in X hours")
- 10% time remaining: Urgent warning ("URGENT: Quest deadline approaching!")

### Quest Generation Integration (Module 05)

**Procedural Quest Creation**:
- NPC has need/goal → Generate quest via Module 05
- Use genre trope libraries for quest templates:
  - Isekai: Guild quests, fetch quests, monster hunts
  - Shonen: Tournament arcs, training challenges, rival battles
  - Seinen: Political intrigue, moral dilemmas, investigations
- Faction reputation tiers unlock faction-specific quests
- World events generate dynamic quests (disaster relief, faction conflicts)

**Quest Template Structure**:
- Define quest skeleton in genre trope files
- Fill variables: [NPC name], [location], [item], [enemy], [reward]
- Create quest object using create_quest()
- Auto-assign to appropriate characters based on context

---

## Session Export/Import (Save System)

**Export (Save)**: Collect State (character+world+NPCs+memories+**narrative_profile**)→Generate Metadata (version, session_id, campaign, sessions, playtime, date, save_point)→Compress (memories<20 heat, distant events, old quests)→Checksum (hash for validation)→Create session_export_schema.json (metadata+character+**narrative_profile**+world+npcs+memories+recent_narrative+system_state)→Save File (campaign_session_N_YYYY-MM-DD.json in ./saves/, keep last 3 backups). **CRITICAL**: Pre-made profiles export ID only (lightweight), generated profiles export FULL data (scales/tropes/scaffolding, no file reference).

**Import (Load)**: Read File→Validate Structure (version compat, checksum, required fields)→Validate Data (state passes validation, no impossible values, **narrative_profile** type/fields valid)→Check Dependencies (NPCs/locations/memories linked, **pre-made profile file exists OR generated profile has full data**)→Load Active State (restore all schemas, **if pre-made→load base from file+apply adjustments, if generated→use state data directly**)→Restore Context (last 5-10 exchanges, active_scene, status)→Resume: "Welcome back! Session N | Playtime X | Last [date] | [Status recap] | [Active scene] | What do you do?"

**Version Migration**: Old format→detect version→migration script→convert to new structure→preserve critical data. Example: v1.5 simple "health":85→v2.0 resources.hp.current=85, infer max from level, add new SP resource with defaults.

---

## State Synchronization

**Cross-Schema Consistency** - Events affect multiple schemas. NPC Death example: npc_schema (add dead flag, can_die=false)→character_schema (mark relationship deceased, update quests: defeat quest complete, alliance quest failed)→world_state (faction power -15, add leader killed event, world consequences)→memories (WORLD_EVENTS heat 80, CONSEQUENCES heat 60). ALL atomic.

**Narrative Profile Change** - Adjustments cascade to modules. Player: "Add more comedy" example: character_schema.narrative_profile (comedy_vs_drama 6→4, add adjustments_log entry)→memories (NARRATIVE_STYLE heat 40 "More comedy requested")→Module 06 narration (increase comedic beats 20%→30%, add more banter)→Module 04 NPCs (more lighthearted dialogue, reduce serious tones)→Module 08 combat (add comedic flourishes to descriptions). ALL atomic.

**Dependent Updates** - Cascading changes. Time +6hrs (3PM→9PM) example: world temporal (time=21:00, night)→environment (weather check, night events)→all NPCs (update location/activity per schedule: Kaito dojo→home, shops close)→locations (services close, danger up)→character (SP regen +30, hunger/thirst, check scheduled events)→quests (time-sensitive countdown). ALL together.

---

## Error Recovery

**Detection**: Validation fail, checksum mismatch, schema violation, logic error (dead acting, negative resources)

**Recovery Protocol**: Detect→Assess Severity→CRITICAL (character/world missing)→Load last valid save. MAJOR (impossible values)→Auto-correct+log+inform. MINOR (small inconsistencies)→Silent correct+log→Apply or Rollback→Notify if needed→Resume/Reload

Example (MP=-50): MAJOR→Log error→Check last valid (MP=30)→Cause: 80 MP spell, validation skipped→Correct: MP=0, refund spell, remove from history→Inform: "Error detected, spell didn't cast (insufficient MP). Current: 30"→Resume

## Integration

Coordinates with: Cognitive (01) - validates action prereqs, Learning (02) - stores changes as memories, **Narrative Calibration (13)** - loads/applies/adjusts narrative profiles, NPC (04) - updates NPC states, Narrative (05) - maintains consistency, Session Zero (06) - initializes character+narrative profile, Combat (08) - validates/applies combat changes, Progression (09) - handles level ups/skills

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
