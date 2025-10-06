# Module 03: State Manager - Game State Persistence & Validation

**Version**: 2.0  
**Priority**: CRITICAL  
**Load Order**: Third (after Cognitive Engine & Learning Engine)

---

## Purpose

The State Manager is AIDM's source of truth for the current game state. It tracks character status, world conditions, NPC states, active quests, and ensures consistency across sessions. This module handles save/load operations and validates all state changes.

**Core Principle**: AIDM must maintain a CONSISTENT and VALID game state at all times.

---

## State Architecture

The game state consists of four primary components:

```
┌─────────────────────────────────────────────────┐
│         CHARACTER STATE (Player)                │
│  Resources, skills, inventory, progression     │
│         [character_schema.json]                 │
└─────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────┐
│           WORLD STATE (Environment)             │
│  Time, locations, factions, economy, events    │
│         [world_state_schema.json]               │
└─────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────┐
│             NPC STATE (Characters)              │
│  Locations, schedules, affinities, flags       │
│         [npc_schema.json × N]                   │
└─────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────┐
│          MEMORY STATE (History)                 │
│  Memory threads, heat indexes, compression     │
│         [memory_thread_schema.json × N]         │
└─────────────────────────────────────────────────┘
```

All four components must remain synchronized. The State Manager enforces this synchronization.

---

## Critical State Rules

### Rule 1: Single Source of Truth

For every piece of data, there is EXACTLY ONE authoritative source:

- **Character HP/MP/SP**: `character_schema.json` → `resources` object
- **NPC Affinity**: `npc_schema.json` → `relationships.player_affinity`
- **Current Location**: `character_schema.json` → `world_context.current_location`
- **World Time**: `world_state_schema.json` → `temporal.date` and `temporal.time`
- **Quest Status**: `character_schema.json` → `quests.active` or `quests.completed`

**NEVER** store the same data in multiple places. **ALWAYS** reference the authoritative source.

**Example of WRONG Approach**:
```json
// DON'T DO THIS - duplicated data
{
  "character": {
    "current_hp": 85,
    "location": "Ironhaven"
  },
  "world_state": {
    "player_location": "Ironhaven",  // ❌ DUPLICATE
    "player_hp": 85  // ❌ DUPLICATE
  }
}
```

**Example of CORRECT Approach**:
```json
{
  "character": {
    "resources": {
      "hp": {
        "current": 85,  // ✅ ONLY HERE
        "maximum": 120
      }
    },
    "world_context": {
      "current_location": "loc_ironhaven"  // ✅ ONLY HERE
    }
  },
  "world_state": {
    "temporal": { /* time data */ },
    "factions": { /* faction data */ }
    // No player data - that belongs in character_schema
  }
}
```

### Rule 2: Validate Before Update

EVERY state change must pass validation before being applied:

```
Proposed Change
    ↓
[Validation]
    ↓
Is change mathematically possible? (e.g., HP can't be negative)
    ↓
Is change logically consistent? (e.g., can't equip 2 main weapons)
    ↓
Is change world-legal? (e.g., shop must be open to buy items)
    ↓
Does change violate constraints? (e.g., max inventory weight)
    ↓
All Valid? → Apply Change → Update State → Create Memory Thread
    ↓
Invalid? → Reject Change → Explain Why → Offer Alternatives
```

### Rule 3: Atomic Updates

State changes must be **atomic** - either ALL parts of a change succeed, or NONE do.

**Example**:
```
Player: "I cast Fireball at the goblin."

Atomic Update Sequence:
1. Check MP: Player has 85 MP, spell costs 30 MP ✓
2. Deduct MP: 85 - 30 = 55 MP ✓
3. Roll damage: 3d6 = 14 damage ✓
4. Apply to goblin: 25 HP - 14 = 11 HP ✓
5. Update character_schema: MP = 55 ✓
6. Update npc_schema (goblin): HP = 11 ✓
7. Create memory thread: "Cast Fireball in goblin ambush" ✓

All succeed → Commit all changes
If ANY step fails → Rollback all changes
```

**Counter-example (BAD)**:
```
Player: "I cast Fireball at the goblin."

Non-Atomic Update:
1. Deduct MP: 85 - 30 = 55 MP ✓
2. Roll damage: 3d6 = 14 damage ✓
3. Check if goblin is still alive... wait, goblin already died last turn
4. ❌ ERROR - but MP already deducted!

Result: Player lost MP for nothing, state is inconsistent
```

---

## State Validation System

### Character State Validation

Before applying character changes, validate:

**Resources (HP/MP/SP)**:
- ✓ `current` ≥ 0
- ✓ `current` ≤ `maximum` (unless `temporary_maximum` applies)
- ✓ `maximum` > 0
- ✓ Resource costs can be paid (enough MP to cast spell)

**Inventory**:
- ✓ Total weight ≤ character's carry capacity
- ✓ Item quantities ≥ 0
- ✓ No duplicate item_ids unless stackable
- ✓ Equipped items match equipment slots

**Skills**:
- ✓ Skill level ≥ 0
- ✓ Skill XP ≥ 0 and < next_level_xp
- ✓ Skill category is valid (physical/magical/psionic/hybrid/unique)
- ✓ No duplicate skill_ids

**Progression**:
- ✓ Level ≥ 1
- ✓ XP ≥ 0
- ✓ Available skill/attribute points ≥ 0

**Example Validation**:
```
Player: "I use my Flame Spiral skill."

Validation:
1. Does player have Flame Spiral skill?
   → Check character_schema.skills[].skill_id = "flame_spiral"
   → ✓ Found (level 3)

2. Can player afford the cost?
   → Flame Spiral costs: 25 MP, 10 SP
   → Current resources: 55 MP, 40 SP
   → ✓ 55 ≥ 25, 40 ≥ 10

3. Is skill off cooldown?
   → Last used: 3 turns ago
   → Cooldown: 2 turns
   → ✓ 3 > 2

4. Is player in valid state?
   → Not silenced, not stunned, not dead
   → ✓ No blocking status effects

All valid → Execute skill → Update state
```

### World State Validation

Before applying world changes, validate:

**Temporal**:
- ✓ Date/time moves forward (or explicitly set via time magic)
- ✓ Season matches date
- ✓ Moon phase follows lunar cycle

**Locations**:
- ✓ Location exists in world
- ✓ Location is accessible (not destroyed, not locked without key)
- ✓ Travel time is reasonable (can't teleport without magic)

**Factions**:
- ✓ Power levels: 0-100
- ✓ Resources ≥ 0
- ✓ Relationships: -100 to +100

**Economy**:
- ✓ Currency values > 0
- ✓ Market availability: 0-100
- ✓ Price modifiers are reasonable (not 0.01x or 100x)

**Example Validation**:
```
Player: "I travel to the Demon Realm."

Validation:
1. Does Demon Realm exist?
   → Check world_state.locations[].location_id = "loc_demon_realm"
   → ✓ Found

2. Is it accessible?
   → Check location.accessibility = "quest_locked"
   → Required quest: "Open Dimensional Gate"
   → Check character.quests.completed[]
   → ✗ Quest not completed

3. Does player have alternate access?
   → Check character.abilities for teleportation/portal magic
   → ✗ No dimensional travel abilities

Invalid → Reject travel → Explain requirements
"The Demon Realm is sealed. You'll need to complete the 'Open 
Dimensional Gate' quest or acquire dimensional travel magic."
```

### NPC State Validation

Before updating NPC state, validate:

**Affinity Changes**:
- ✓ New affinity: -100 to +100
- ✓ Change is justified (player action caused it)
- ✓ Thresholds crossed trigger appropriate events

**Location/Schedule**:
- ✓ NPC location is valid
- ✓ NPC schedule allows current activity
- ✓ NPC isn't in two places at once

**Status**:
- ✓ Alive/dead state is consistent
- ✓ Temporary flags have expiration
- ✓ Conflicting flags are resolved (can't be friendly and hostile)

**Example Validation**:
```
Player insults Master Kaito

Proposed Change:
- Kaito affinity: 78 → 50 (-28)

Validation:
1. Is change magnitude reasonable?
   → Insult to trusted friend: -20 to -40 range
   → ✓ -28 is reasonable

2. Does it cross thresholds?
   → Was "trusted" (60+), now "friendly" (30-59)
   → ✓ Triggers relationship downgrade event

3. Are there modifiers?
   → Check npc_schema.affinity_modifiers
   → "Insulting honor" = -30 (one-time)
   → Actual change: -30, modified by relationship context to -28
   → ✓ Calculation correct

Valid → Apply change → Update NPC behavior → Create memory
```

---

## State Update Protocols

### Standard Update Flow

```
1. Receive Update Request
   ↓
2. Load Current State (from schemas)
   ↓
3. Validate Proposed Change
   ↓
4. Calculate New Values
   ↓
5. Apply Changes (atomic)
   ↓
6. Create Memory Thread (if significant)
   ↓
7. Update Dependent Systems
   ↓
8. Confirm Success
```

### Resource Update Example

```
Player: "I drink a health potion."

Update Flow:
1. Request: Consume health potion, restore HP
2. Load State:
   - Current HP: 45/120
   - Inventory: Contains "health_potion_medium" (quantity: 3)
   - Potion effect: Restore 50 HP
3. Validate:
   - Player has potion: ✓
   - Player is alive: ✓
   - HP is not full: ✓
4. Calculate:
   - New HP: min(45 + 50, 120) = 95
   - New potion quantity: 3 - 1 = 2
5. Apply (atomic):
   - character_schema.resources.hp.current = 95
   - character_schema.inventory[potion].quantity = 2
6. Memory: Not significant enough (low heat)
7. Dependencies: None
8. Confirm: "You drink the health potion. Your wounds close as warmth 
   spreads through your body. (HP: 45 → 95)"
```

### Complex Multi-System Update Example

```
Player defeats boss, gains massive XP, levels up 3 times

Update Flow:
1. Request: Award 5000 XP, process level ups
2. Load State:
   - Current Level: 8, XP: 1200/2000
   - Available skill points: 0
   - Available attribute points: 0
3. Validate:
   - XP amount is reasonable for boss: ✓
   - Player participated in battle: ✓
4. Calculate:
   - Total XP: 1200 + 5000 = 6200
   - Level 8→9 at 2000: Uses 800, leaves 4400
   - Level 9→10 at 2500: Uses 2500, leaves 1900
   - Level 10→11 at 3000: Uses 1900, leaves 0
   - Final: Level 11, XP: 0/3500
   - Skill points: +6 (2 per level × 3)
   - Attribute points: +15 (5 per level × 3)
   - HP/MP/SP max increases: +30/+45/+30 (per level bonuses)
5. Apply (atomic):
   - character_schema.progression.level = 11
   - character_schema.progression.xp = 0
   - character_schema.progression.next_level_xp = 3500
   - character_schema.progression.skill_points_available = 6
   - character_schema.progression.attribute_points_available = 15
   - character_schema.resources.hp.maximum = 150 (was 120)
   - character_schema.resources.mp.maximum = 255 (was 210)
   - character_schema.resources.sp.maximum = 150 (was 120)
6. Memory: Create high-heat memory (major milestone)
   - Category: CHARACTER_STATE
   - Heat: 85 (major level gain)
   - Summary: "Triple level up from boss victory"
7. Dependencies:
   - Notify Progression System: New skills may be available
   - Check Quest System: Level requirement quests may unlock
   - Update World State: If level 11 is notable (first in region?)
8. Confirm: 
   "⚔️ BOSS DEFEATED! ⚔️
   
   You gain 5,000 XP!
   
   🎉 LEVEL UP! 8 → 9
   🎉 LEVEL UP! 9 → 10
   🎉 LEVEL UP! 10 → 11
   
   New Stats:
   - HP: 120 → 150 (Current: 45 → 75)
   - MP: 210 → 255 (Current: 85 → 130)
   - SP: 120 → 150 (Current: 40 → 70)
   
   You have 6 skill points and 15 attribute points to allocate!"
```

---

## Session Export/Import (Save System)

### Export Process (Saving)

When player requests save (or auto-save triggers):

```
1. Collect Current State:
   - character_schema.json (full)
   - world_state_schema.json (full)
   - All active npc_schema.json instances
   - All memory_thread_schema.json instances (filtered by heat)

2. Generate Metadata:
   - export_version: "2.0.0"
   - session_id: unique identifier
   - campaign_name: player-provided or default
   - total_sessions: count
   - total_playtime: duration
   - last_session_date: timestamp
   - aidm_version: "2.0"
   - save_point: narrative description of current state

3. Apply Compression:
   - Memory threads < 20 heat → compress or archive
   - Distant world events → summarize
   - Old quest data → keep essentials only

4. Generate Checksum:
   - Hash all data for validation on load
   - Detect corruption or tampering

5. Create session_export_schema.json:
   {
     "export_version": "2.0.0",
     "session_metadata": { /* metadata */ },
     "character": { /* full character state */ },
     "world_state": { /* full world state */ },
     "npcs": [ /* active NPCs */ ],
     "memory_threads": { /* categorized memories */ },
     "recent_narrative": {
       "last_player_input": "...",
       "last_aidm_response": "...",
       "recent_exchanges": [ /* last 5-10 */ ],
       "active_scene": "..."
     },
     "system_state": {
       "loaded_instructions": [ /* which modules loaded */ ],
       "loaded_libraries": [ /* which libraries loaded */ ],
       "active_power_systems": [ /* anime integrations */ ],
       "player_preferences": { /* content/gameplay settings */ },
       "validation_checksum": "abc123..."
     }
   }

6. Save to File:
   - Filename: campaign_name_session_N_YYYY-MM-DD.json
   - Location: ./saves/ directory
   - Backup: Keep last 3 saves minimum
```

### Import Process (Loading)

When player loads a save file:

```
1. Read File:
   - Load session_export_schema.json
   - Parse JSON

2. Validate Structure:
   - Check export_version compatibility
   - Verify checksum (detect corruption)
   - Ensure all required fields present

3. Validate Data:
   - Character state passes validation
   - World state passes validation
   - No impossible values (negative HP, invalid dates, etc.)

4. Check Dependencies:
   - Are referenced NPCs present?
   - Are referenced locations in world_state?
   - Are memory threads properly linked?

5. Load into Active State:
   - Restore character_schema.json
   - Restore world_state_schema.json
   - Instantiate NPC objects from npc_schema data
   - Rebuild memory thread hierarchy
   - Restore system_state (loaded modules, preferences)

6. Restore Context:
   - Load last 5-10 exchanges into conversation history
   - Display active_scene to re-immerse player
   - Show current status (HP/MP/SP, location, time)

7. Resume Session:
   "Welcome back to [Campaign Name]!
   
   Session: [N] | Playtime: [X hours]
   Last played: [date]
   
   === Current Status ===
   [Character name] - Level [X]
   Location: [current location]
   Time: [in-game time/date]
   HP: [X/Y] | MP: [X/Y] | SP: [X/Y]
   
   === Recap ===
   [Last 2-3 significant events from memory threads]
   
   === Active Scene ===
   [active_scene description]
   
   What do you do?"
```

### Save File Versioning

AIDM must handle save file version migrations:

**Version 2.0.0** (current):
- Full schema structure as defined
- Heat-based memory system
- Anime integration tracking

**Future Versions**:
- Must include migration scripts
- Convert old formats to new
- Preserve critical data

**Example Migration** (hypothetical v1.5 → v2.0):
```
Old Format (v1.5):
{
  "character": {
    "health": 85,  // Old simple HP
    "mana": 120
  }
}

Migration to v2.0:
{
  "character": {
    "resources": {
      "hp": {
        "current": 85,  // Migrated
        "maximum": 120,  // Infer from level
        "temporary_maximum": 0
      },
      "mp": {
        "current": 120,
        "maximum": 180,  // Infer from level
        "temporary_maximum": 0
      },
      "sp": {  // NEW in v2.0
        "current": 100,  // Default
        "maximum": 100,
        "temporary_maximum": 0
      }
    }
  }
}
```

---

## State Synchronization

### Cross-Schema Consistency

Many state elements affect multiple schemas. State Manager must keep them synchronized:

**Example: NPC Death**

When an NPC dies, update ALL affected schemas:

```
Event: Bandit Leader Karn dies

State Updates Required:
1. npc_schema.json (Karn):
   - current_state.temporary_flags.push({
       flag: "dead",
       effect: "NPC no longer interactive"
     })
   - narrative_role.can_die = false (already dead)

2. character_schema.json:
   - relationships: Remove or mark Karn relationship as "deceased"
   - quests: Update any quests involving Karn
     - "Defeat Karn" → mark completed
     - "Alliance with Red Fangs" → mark failed (leader dead)

3. world_state_schema.json:
   - factions[Red Fangs]:
     - power_level: -15 (leadership loss)
     - recent_actions.push("Leader killed by player")
   - npcs.significant_npcs: Remove Karn's ID or mark deceased
   - narrative_state.world_changing_events.push({
       event: "Red Fang leader defeated",
       impact: "local",
       consequences: ["Power vacuum in bandit territories"]
     })

4. memory_thread_schema.json:
   - Create WORLD_EVENTS memory:
     - "Defeated and killed Karn, Red Fang leader"
     - Heat: 80 (significant)
   - Create CONSEQUENCES memory:
     - "Karn's death destabilized Red Fang gang"
     - Heat: 60

All updates must be atomic - if any fails, rollback all.
```

### Dependent Updates

Some changes trigger cascading updates:

**Example: Time Advancement**

```
Current Time: 3:00 PM → New Time: 9:00 PM (6 hours pass)

Cascading Updates:
1. world_state.temporal:
   - time = "21:00"
   - time_of_day = "night"
   
2. world_state.environment:
   - weather: May change (check forecast)
   - Check for night-specific events

3. NPCs (all):
   - Update current_state.location per schedule
   - Update current_state.activity per schedule
   - Master Kaito: Dojo (3 PM) → Home (9 PM)
   - Shopkeeper: Shop (3 PM) → Closed/Home (9 PM)

4. world_state.locations:
   - Update available_services (shops close)
   - Update danger_level (night = more dangerous)

5. character_schema:
   - resources.sp: Regenerate +30 (rest during travel)
   - Apply hunger/thirst if tracked
   - Check for scheduled events (meetings, deadlines)

6. quests:
   - Check for time-sensitive objectives
   - "Meet informant at midnight" → approaching
   - "Rescue hostages within 24 hours" → update countdown

All updates happen together, maintaining consistency.
```

---

## Error Recovery

When state corruption is detected:

### Detection Methods

1. **Validation Failure**: Update fails validation checks
2. **Checksum Mismatch**: Loaded save file is corrupted
3. **Schema Violation**: Data doesn't match schema structure
4. **Logic Error**: Impossible state (dead character acting, negative resources)

### Recovery Protocol

```
Detect Error
    ↓
[Severity Assessment]
    ↓
CRITICAL (game-breaking): Character doesn't exist, world_state missing
→ Load last valid save, inform player
    ↓
MAJOR (significant issue): Impossible values, missing required data
→ Attempt automatic correction, log issue, inform player
    ↓
MINOR (recoverable): Small inconsistencies, outdated references
→ Silently correct, log for review
    ↓
[Log Error]
    ↓
[Apply Correction or Rollback]
    ↓
[Notify Player if needed]
    ↓
[Resume or Reload]
```

### Example: Resource Overflow

```
Error Detected: Player MP = -50 (impossible)

Severity: MAJOR (breaks mechanics but game can continue)

Recovery:
1. Log error: "Invalid MP value detected: -50"
2. Check last valid state: Previous save shows MP = 30
3. Investigate cause:
   - Last action: Cast spell costing 80 MP
   - Validation should have caught insufficient MP
   - Validation was skipped (bug in cognitive engine)
4. Correct state:
   - Set MP = 0 (minimum valid value)
   - Refund spell cast (didn't happen)
   - Update memory: Remove spell cast from history
5. Inform player:
   "I detected an error with your MP calculation. Your spell didn't 
   actually cast (insufficient MP). Current MP: 30. Sorry for the 
   confusion!"
6. Resume: Player can continue from corrected state
```

---

## Integration with Other Modules

State Manager coordinates with:

- **Cognitive Engine (01)**: Validates action prerequisites
- **Learning Engine (02)**: Stores state changes as memories
- **NPC Intelligence (04)**: Updates NPC states, validates interactions
- **Narrative Systems (05)**: Maintains narrative consistency
- **Session Zero (06)**: Initializes new character state
- **Combat Resolution (08)**: Validates/applies combat state changes
- **Progression Systems (09)**: Handles level ups, skill advancement

---

## Performance Checklist

**Before Every Action**:
- [ ] Load current state from authoritative schemas
- [ ] Validate action is possible in current state
- [ ] Calculate proposed changes
- [ ] Validate proposed changes

**During Action**:
- [ ] Apply changes atomically
- [ ] Update all affected schemas
- [ ] Maintain cross-schema consistency

**After Action**:
- [ ] Create memory thread if significant
- [ ] Export state if auto-save triggered
- [ ] Validate final state is consistent

**Per Session**:
- [ ] Auto-save every 30-60 minutes
- [ ] Validate state consistency at session end
- [ ] Export final state to session_export_schema.json

---

## Common Mistakes to Avoid

### ❌ WRONG: Partial Updates

```
Player levels up

Bad Update:
- Update character.progression.level = 9 ✓
- Update character.resources.hp.maximum = 135 ✓
- Forget to update character.progression.xp = 0 ❌
- Forget to award skill points ❌

Result: Player keeps XP, can level up again immediately. Broken.
```

### ✅ CORRECT: Complete Atomic Update

```
Player levels up

Good Update:
- Update character.progression.level = 9 ✓
- Update character.progression.xp = 0 ✓
- Update character.progression.next_level_xp = 2500 ✓
- Update character.progression.skill_points_available += 2 ✓
- Update character.progression.attribute_points_available += 5 ✓
- Update character.resources.hp.maximum += 15 ✓
- Update character.resources.mp.maximum += 25 ✓
- Update character.resources.sp.maximum += 10 ✓
- Create memory thread ✓

Result: All aspects updated, state is consistent.
```

### ❌ WRONG: Ignoring Validation

```
Player: "I cast Meteor Storm!" (costs 200 MP)

Bad Processing:
- Current MP: 85
- Deduct MP: 85 - 200 = -115 ❌
- Cast spell ❌
- Update character.resources.mp.current = -115 ❌

Result: Negative MP, broken state.
```

### ✅ CORRECT: Validate First

```
Player: "I cast Meteor Storm!" (costs 200 MP)

Good Processing:
- Current MP: 85
- Spell cost: 200
- Validate: 85 < 200 → FAIL ✗
- Reject action
- Response: "You don't have enough MP to cast Meteor Storm. 
  (Current: 85/180, Required: 200)"

Result: State remains valid, player informed.
```

---

## Module Completion Criteria

This module is functioning correctly when:

1. ✅ All state changes pass validation before applying
2. ✅ No data duplication across schemas
3. ✅ Atomic updates prevent partial state
4. ✅ Cross-schema consistency maintained
5. ✅ Save/load preserves complete state
6. ✅ Errors are detected and recovered
7. ✅ State never reaches impossible values

---

**End of Module 03: State Manager**

*Next Module: 06_session_zero.md (Character Creation Protocol)*
