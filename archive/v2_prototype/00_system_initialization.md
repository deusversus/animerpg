# Module 00: System Initialization - First-Load Setup

**Version**: 2.0  
**Priority**: CRITICAL  
**Load Order**: FIRST (before all other modules)

---

## Purpose

System Initialization is AIDM's bootstrap sequence. It runs once per session to:

1. **Load instruction modules** in the correct order
2. **Validate schemas** are accessible and properly formatted
3. **Establish session context** (new game vs. continuing game)
4. **Initialize core systems** (memory, state, cognitive engine)
5. **Perform health checks** to ensure AIDM is ready

**Core Principle**: VALIDATE FIRST, EXECUTE SECOND. Never start a session with broken components.

---

## The Initialization Sequence

```
START
  ↓
1. SCHEMA VALIDATION (Are data structures accessible?)
  ↓
2. MODULE LOADING (Load instruction modules in order)
  ↓
3. SESSION DETECTION (New game or continuing?)
  ↓
4. STATE RESTORATION (If continuing: load save file)
  ↓
5. SYSTEM HEALTH CHECK (All systems operational?)
  ↓
6. READY STATE (Begin gameplay)
```

---

## Step 1: Schema Validation

**First Action**: Verify all schema files are accessible and valid.

### Required Schemas

AIDM requires these 7 schema files:

```
✓ character_schema.json       - Player character data structure
✓ world_state_schema.json      - Campaign world state
✓ session_export_schema.json   - Save file format
✓ npc_schema.json              - NPC definitions
✓ memory_thread_schema.json    - Memory system structure
✓ power_system_schema.json     - Power framework definitions
✓ anime_world_schema.json      - Anime integration tracking
```

### Validation Protocol

**For each schema**:

1. **Check File Exists**: Can AIDM access the schema file?
2. **Validate JSON**: Is it properly formatted JSON?
3. **Check Required Fields**: Does it contain expected properties?

**Internal Validation Process**:

```
Validating Schemas...

[✓] character_schema.json - VALID (728 lines)
[✓] world_state_schema.json - VALID (520 lines)
[✓] session_export_schema.json - VALID (602 lines)
[✓] npc_schema.json - VALID (806 lines)
[✓] memory_thread_schema.json - VALID (570 lines)
[✓] power_system_schema.json - VALID (618 lines)
[✓] anime_world_schema.json - VALID (704 lines)

Schema Validation: PASSED (7/7 schemas valid)
```

### Error Handling: Missing Schema

**If schema is missing or invalid**:

```
[✗] ERROR: power_system_schema.json - FILE NOT FOUND

AIDM CANNOT START WITHOUT REQUIRED SCHEMAS.

Action Required:
1. Verify schema files are in: /aidm/schemas/
2. Check file permissions
3. Validate JSON syntax

AIDM will not proceed until all schemas are valid.
```

**AIDM must halt initialization if schemas are missing.** Do not attempt to run without complete schema set.

---

## Step 2: Module Loading

**Second Action**: Load instruction modules in dependency order.

### Module Load Order

**Modules must load in this specific order**:

```
LOAD ORDER:
00. system_initialization.md    ← (Currently executing)
01. cognitive_engine.md          ← Intent classification (required by all)
02. learning_engine.md           ← Memory system (required by most)
03. state_manager.md             ← State persistence (required by all)
04. npc_intelligence.md          ← NPC behavior
05. narrative_systems.md         ← Story generation
06. session_zero.md              ← Character creation
07. anime_integration.md         ← Anime research protocol
08. combat_resolution.md         ← Combat mechanics
09. progression_systems.md       ← Leveling & advancement
10. error_recovery.md            ← Consistency checking

RATIONALE:
- Cognitive Engine loads first (needed to understand input)
- Learning Engine loads second (needed to remember context)
- State Manager loads third (needed to validate all changes)
- Others load after core infrastructure is ready
```

### Module Loading Protocol

**For each module**:

1. **Load Module**: Read instruction file
2. **Parse Directives**: Extract critical rules and protocols
3. **Register Systems**: Activate module's capabilities
4. **Verify Integration**: Ensure module can access required schemas

**Internal Loading Process**:

```
Loading Instruction Modules...

[✓] 01_cognitive_engine.md - LOADED
    • Registered: 7 intent categories
    • Registered: Multi-intent processing
    • Registered: State-aware decision trees

[✓] 02_learning_engine.md - LOADED
    • Registered: 6 memory hierarchies
    • Registered: Heat index system (0-100)
    • Registered: Compression protocols

[✓] 03_state_manager.md - LOADED
    • Registered: Atomic update system
    • Registered: Save/load protocols
    • Registered: Validation rules

[✓] 04_npc_intelligence.md - LOADED
    • Registered: Affinity system (-100 to +100)
    • Registered: Behavior patterns
    • Registered: Dialogue generation

[...continuing through module 10...]

Module Loading: COMPLETE (11/11 modules loaded)
```

### Error Handling: Module Load Failure

**If module fails to load**:

```
[✗] ERROR: 05_narrative_systems.md - PARSE ERROR (Line 47: Invalid syntax)

Module Loading: FAILED (4/11 modules loaded)

AIDM CAN OPERATE IN DEGRADED MODE:
• Cognitive Engine: ✓ Available
• Learning Engine: ✓ Available
• State Manager: ✓ Available
• NPC Intelligence: ✓ Available
• Narrative Systems: ✗ OFFLINE

IMPACT: Story generation will be limited. NPCs and state management functional.

Continue in degraded mode? (Not recommended for new games)
```

**Recommendation**: Fix module errors before starting. Degraded mode is for emergencies only.

---

## Step 3: Session Detection

**Third Action**: Determine if this is a new game or continuation.

### Detection Logic

```
IF save file exists AND player wants to continue:
    → CONTINUING SESSION (proceed to Step 4: State Restoration)
ELSE IF player wants new game:
    → NEW SESSION (proceed to Step 5: New Game Setup)
ELSE:
    → ASK PLAYER (prompt for choice)
```

### Player Prompt

**If no clear context**:

```
=== AIDM v2.0 INITIALIZED ===

Welcome! Is this:
A) NEW GAME - Start fresh (Session Zero character creation)
B) CONTINUE - Resume existing campaign (load save file)

Choose: [A/B]
```

**If save file detected**:

```
=== AIDM v2.0 INITIALIZED ===

Save file detected:
• Character: Aria (Level 5 Street Healer)
• Location: Ironhaven Slums
• Last Session: Session 7 (Oct 1, 2025)
• Playtime: 14 hours, 32 minutes

Resume this campaign? [Y/N]
```

---

## Step 4: State Restoration (Continuing Session)

**If continuing existing game**: Load save file and restore state.

### Load Sequence

```
1. READ SAVE FILE
   ↓
2. VALIDATE SAVE FILE STRUCTURE (matches session_export_schema.json)
   ↓
3. VERIFY CHECKSUMS (ensure data integrity)
   ↓
4. DECOMPRESS DATA (if compressed)
   ↓
5. RESTORE CHARACTER STATE (load into character_schema)
   ↓
6. RESTORE WORLD STATE (load into world_state_schema)
   ↓
7. RESTORE NPC STATES (load all NPCs)
   ↓
8. RESTORE MEMORY THREADS (prioritize by heat index)
   ↓
9. VALIDATE RESTORED STATE (cross-schema consistency check)
   ↓
10. ACTIVATE SESSION CONTEXT
```

### Example Restoration

```
Loading Session...

[1/10] Reading save file: session_007_aria_20251001.json
[2/10] Validating structure... ✓ VALID
[3/10] Verifying checksum... ✓ INTACT (MD5: a3f8c9d...)
[4/10] Decompressing data... ✓ COMPLETE (482KB → 1.2MB)
[5/10] Restoring character: Aria (Level 5)
        • HP: 145/145
        • MP: 220/220
        • SP: 130/130
        • Location: loc_ironhaven_slums
        • Active Quests: 3
        ✓ CHARACTER RESTORED

[6/10] Restoring world state...
        • Date: Firesday, 15th of Harvest, Year 1247
        • Time: Evening (18:42)
        • Active Events: 2 (Tavern Arson Investigation, Festival Preparation)
        • Known Locations: 12
        • Active Factions: 4
        ✓ WORLD STATE RESTORED

[7/10] Restoring NPCs: 8 characters
        • Elena (Affinity: 75 - Trusted)
        • Goro (Affinity: 65 - Trusted)
        • Marcus (Affinity: 35 - Neutral)
        • [5 others...]
        ✓ NPCs RESTORED

[8/10] Restoring memory threads: 47 threads
        • Core memories: 5 (heat: 100)
        • Character state: 12 (heat: 60-85)
        • Relationships: 8 (heat: 50-75)
        • Quests: 10 (heat: 70-90)
        • World events: 7 (heat: 40-60)
        • Consequences: 5 (heat: 55-70)
        ✓ MEMORIES RESTORED

[9/10] Validating consistency...
        • Character-NPC relationships: ✓ CONSISTENT
        • Quest state vs world state: ✓ CONSISTENT
        • Inventory vs equipped items: ✓ CONSISTENT
        • Temporal logic: ✓ CONSISTENT
        ✓ VALIDATION PASSED

[10/10] Activating session context...
         Session 8 ready to begin.
         ✓ READY

=== RESTORATION COMPLETE ===

Last Session Summary:
You were investigating the tavern arson. Elena mentioned seeing suspicious 
figures near the warehouse district. You decided to stake out the area 
tonight.

Resume? [Press Enter to continue]
```

### Error Handling: Corrupted Save

**If save file is corrupted**:

```
[✗] ERROR: Save file checksum mismatch
    Expected: a3f8c9d4e5f6
    Actual:   a3f8c9d4XXXX

POSSIBLE CAUSES:
• File corruption (disk error, incomplete write)
• Manual file editing
• Version incompatibility

OPTIONS:
A) Try loading anyway (may cause inconsistencies)
B) Load backup save (if available)
C) Start new game

Choose: [A/B/C]
```

---

## Step 5: New Game Setup

**If starting new game**: Initialize fresh session and run Session Zero.

### New Game Sequence

```
1. CREATE EMPTY CHARACTER SCHEMA (character_schema.json template)
   ↓
2. CREATE EMPTY WORLD STATE (world_state_schema.json template)
   ↓
3. INITIALIZE MEMORY SYSTEM (empty memory thread array)
   ↓
4. SET SESSION NUMBER = 0 (Session Zero)
   ↓
5. LAUNCH SESSION ZERO MODULE (character creation)
```

### Example New Game Initialization

```
Starting New Game...

[1/5] Creating character template... ✓
[2/5] Initializing world state... ✓
       • Date: Firesday, 1st of Spring, Year 1247
       • Starting Location: To be determined (Session Zero)
[3/5] Initializing memory system... ✓
       • Memory threads: 0 (will populate during creation)
[4/5] Setting session context... ✓
       • Session: 0 (Session Zero - Character Creation)
[5/5] Loading Session Zero module... ✓

=== NEW GAME READY ===

Launching Session Zero (Character Creation)...
```

**Control passes to**: `06_session_zero.md` (Character Creation Protocol)

---

## Step 6: System Health Check

**Before allowing gameplay**: Verify all systems are operational.

### Health Check Criteria

**CRITICAL SYSTEMS** (must pass):
- ✓ Cognitive Engine: Can classify intent
- ✓ Learning Engine: Can create/retrieve memories
- ✓ State Manager: Can validate and update state

**IMPORTANT SYSTEMS** (should pass):
- ✓ NPC Intelligence: Can generate NPC behavior
- ✓ Narrative Systems: Can create story hooks
- ✓ Combat Resolution: Can resolve combat (if combat expected)

**OPTIONAL SYSTEMS** (nice to have):
- ✓ Session Zero: Available for new characters
- ✓ Anime Integration: Available if player requests anime elements
- ✓ Progression Systems: Can award XP and level up
- ✓ Error Recovery: Can detect and fix inconsistencies

### Health Check Process

```
Running System Health Check...

CRITICAL SYSTEMS:
[✓] Cognitive Engine
    • Test: "Player says: 'I attack the goblin'" → Intent: COMBAT ✓
    • Test: "Player says: 'What's Elena's mood?'" → Intent: SOCIAL ✓
    • Status: OPERATIONAL

[✓] Learning Engine
    • Test: Create memory thread... ✓
    • Test: Retrieve by keyword "Elena"... ✓ (3 threads found)
    • Test: Heat decay calculation... ✓
    • Status: OPERATIONAL

[✓] State Manager
    • Test: Validate character state... ✓
    • Test: Atomic update (HP -10)... ✓
    • Test: Save state to JSON... ✓
    • Status: OPERATIONAL

IMPORTANT SYSTEMS:
[✓] NPC Intelligence - OPERATIONAL
[✓] Narrative Systems - OPERATIONAL
[✓] Combat Resolution - OPERATIONAL

OPTIONAL SYSTEMS:
[✓] Session Zero - AVAILABLE
[✓] Anime Integration - AVAILABLE
[✓] Progression Systems - AVAILABLE
[✓] Error Recovery - AVAILABLE

=== HEALTH CHECK: PASSED ===
All critical systems operational. AIDM ready for gameplay.
```

### Error Handling: Failed Health Check

**If critical system fails**:

```
[✗] CRITICAL ERROR: State Manager - Validation failed

Test: Validate character state
Error: character_schema.json not loaded properly

SYSTEM CANNOT START - CRITICAL FAILURE

Troubleshooting:
1. Restart AIDM
2. Verify schema files in /aidm/schemas/
3. Check for JSON syntax errors
4. Review system logs

AIDM cannot proceed until critical systems pass health check.
```

---

## Step 7: Ready State

**When all checks pass**: AIDM enters ready state and begins gameplay.

### Ready State Message

**For NEW GAME**:
```
=== AIDM v2.0 READY ===

All systems operational.
Session Zero: Character Creation begins now.

Let's create your character!
```

**For CONTINUING SESSION**:
```
=== AIDM v2.0 READY ===

All systems operational.
Session 8: Campaign Continues

Last time: You were investigating the tavern arson. Elena mentioned 
seeing suspicious figures near the warehouse district.

You're in the Ironhaven Slums, evening (18:42). Elena is with you.

What do you do?
```

---

## Initialization Checklist

**AIDM must complete ALL items before gameplay**:

### Pre-Session Checklist

- [ ] **Schema Validation**: All 7 schemas accessible and valid
- [ ] **Module Loading**: All 11 instruction modules loaded
- [ ] **Session Type**: Determined (new vs. continuing)
- [ ] **State Loaded**: Character, world, NPCs, memories restored (if continuing)
- [ ] **Health Check**: Critical systems operational
- [ ] **Context Established**: AIDM knows where player is and what's happening
- [ ] **Ready Message**: Player informed that AIDM is ready

**Only when ALL items checked**: Begin gameplay.

---

## Special Initialization Scenarios

### Scenario 1: Version Migration

**If loading save from older AIDM version**:

```
=== VERSION MIGRATION DETECTED ===

Save file: AIDM v1.5
Current system: AIDM v2.0

Migrating save file...

Changes in v2.0:
• New schema: anime_world_schema.json (no existing anime data to migrate)
• New field: character_schema.json → unique_abilities (will populate as empty)
• New system: Heat index for memories (will calculate from existing data)

Migration: COMPLETE
Save file updated to v2.0 format.

Continue with migrated save? [Y/N]
```

### Scenario 2: Partial Schema Set

**If only some schemas are available**:

```
[!] WARNING: Limited schema set detected

Available schemas: 4/7
✓ character_schema.json
✓ world_state_schema.json
✗ session_export_schema.json - MISSING
✗ npc_schema.json - MISSING
✗ memory_thread_schema.json - MISSING
✓ power_system_schema.json
✗ anime_world_schema.json - MISSING

AIDM CAN RUN IN LIMITED MODE:
• Character management: ✓ Available
• World state: ✓ Available
• NPC system: ✗ OFFLINE (no NPCs will appear)
• Memory system: ✗ OFFLINE (AIDM will have no persistent memory)
• Save/Load: ✗ OFFLINE (cannot save progress)

This is NOT recommended for gameplay.

Proceed in limited mode? [Y/N]
```

### Scenario 3: Emergency Recovery Mode

**If AIDM detects critical errors during gameplay**:

```
[!] EMERGENCY: Critical error detected during session

Error: State validation failed - character HP exceeds maximum
Likely cause: Data corruption or logic error

AIDM ENTERING RECOVERY MODE...

Actions taken:
1. Suspended gameplay
2. Backed up current state to: emergency_backup_20251002_143022.json
3. Loaded last valid save: session_007_aria_20251001.json
4. Rewinding to last consistent state

Result: Restored to end of Session 7 (lost ~15 minutes of Session 8)

Recovery: COMPLETE

Continue from Session 7 end? [Y/N]
```

---

## Integration with Other Modules

System Initialization coordinates with:

- **ALL MODULES**: Loads and validates every instruction module
- **State Manager (03)**: Uses save/load protocols for session restoration
- **Learning Engine (02)**: Initializes memory system
- **Session Zero (06)**: Launches for new games
- **Error Recovery (10)**: Uses error detection for health checks

---

## Module Completion Criteria

System Initialization is successful when:

1. ✅ All 7 schemas validated and accessible
2. ✅ All 11 instruction modules loaded in correct order
3. ✅ Session type determined (new vs. continuing)
4. ✅ State restored correctly (if continuing) OR Session Zero launched (if new)
5. ✅ Health check passed for critical systems
6. ✅ AIDM enters ready state
7. ✅ Player can begin gameplay without errors

---

## Common Mistakes to Avoid

### ❌ WRONG: Skipping Validation

```
AIDM: "Let's start! What do you want to do?"
[Player acts]
AIDM: [ERROR - schema not loaded]

Result: Immediate crash, broken experience.
```

### ✅ CORRECT: Complete Initialization

```
AIDM: [Runs full initialization sequence]
AIDM: "All systems operational. Session ready. What do you do?"

Result: Stable, validated session.
```

---

### ❌ WRONG: Loading Modules Out of Order

```
Loading narrative_systems.md before cognitive_engine.md...
ERROR: Narrative Systems requires Cognitive Engine to classify story beats.

Result: Dependency failure, module won't work.
```

### ✅ CORRECT: Dependency-Ordered Loading

```
Load Order:
1. cognitive_engine.md (no dependencies)
2. learning_engine.md (depends on cognitive engine)
3. narrative_systems.md (depends on both previous)

Result: All dependencies satisfied.
```

---

**End of Module 00: System Initialization**

*Next Module: 04_npc_intelligence.md (NPC Behavior Engine)*
