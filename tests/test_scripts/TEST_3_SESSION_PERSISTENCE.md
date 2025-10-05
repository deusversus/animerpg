# Test 3: Session Persistence

**Test ID**: AIDM-TEST-003  
**Category**: Advanced Functionality  
**Priority**: HIGH  
**Estimated Time**: 40-50 minutes

---

## Test Objective

Validate that complete game state can be exported, then imported into a fresh session with no data loss.

**Success Criteria**:
1. All stats restored correctly (HP/MP/SP/XP/Level)
2. All relationships/affinity values preserved
3. Inventory and equipment intact
4. Plot threads and quest state maintained
5. No data corruption or loss

---

## Pre-Test Setup

### Files to Load (Session 1)

**Required**:
1. `aidm/CORE_AIDM_INSTRUCTIONS.md`
2. All files in `aidm/instructions/` (12 files)
3. All files in `aidm/schemas/` (7 files)
   - **Critical**: `game_state_schema.json` (defines export format)

**Platform**: Claude Sonnet 4.5, ChatGPT-4, or equivalent  
**Recommended**: LLM with code execution (for JSON validation)

---

## Test Procedure

### Part 1: Create Test State (Turns 1-20)

**Turn 1: Character Creation**
```
Player: "Quick character: I'm a Level 5 fire mage named Ignis in a fantasy isekai world. Let's skip Session Zero and jump right in."
```

**Expected**: Character created with stats:
- HP: ~50-75
- MP: ~60-80  
- SP: ~40-60
- XP: ~6500/7500 (mid-Level 5)
- Skills: Fire Bolt, Fireball, Flame Shield
- Inventory: Staff, Health Potion x3, 100 gold

**Turns 2-5: Combat Encounter**
```
Turn 2: "I'm exploring a dungeon and encounter 3 goblin scouts."
Turn 3: "I cast Fireball at the goblins. (30 MP cost)"
Turn 4: "I use Fire Bolt on the remaining goblin. (10 MP)"
Turn 5: "I loot the goblin corpses."
```

**Expected State Changes**:
- HP: 50/75 (took some damage)
- MP: 20/80 (used 60 MP total)
- XP: 7200/7500 (gained 700 XP)
- Inventory: +Goblin Ears x3, +15 gold

**Turns 6-10: NPC Interaction**
```
Turn 6: "I leave the dungeon and head to the nearby town of Riverside."
Turn 7: "I visit the tavern and meet a friendly blacksmith named Thorn."
Turn 8: "I chat with Thorn about weapon upgrades and buy him an ale."
Turn 9: "I also meet a mysterious hooded figure who warns me about the dungeon boss."
Turn 10: "I thank them both and rest at the inn to recover."
```

**Expected State Changes**:
- HP: 75/75 (rested)
- MP: 80/80 (rested)
- Gold: 90 (spent 25 on ale and inn)
- **NEW NPCs**:
  - Thorn (Blacksmith): Affinity +15 (friendly)
  - Hooded Figure: Affinity +5 (neutral, mysterious)

**Turns 11-15: Quest Acceptance**
```
Turn 11: "The next morning, the town mayor approaches me with an urgent quest."
Turn 12: "I accept the quest to defeat the Flame Wraith in the dungeon depths."
Turn 13: "I buy a Mana Potion x2 from Thorn's shop before heading out."
Turn 14: "I return to the dungeon, descending deeper."
Turn 15: "I reach the boss chamber and prepare for battle."
```

**Expected State Changes**:
- Gold: 40 (spent 50 on Mana Potions)
- Inventory: +Mana Potion x2
- **NEW QUEST**: "Defeat the Flame Wraith" (Active, 0/1 progress)
- Location: Dungeon Boss Chamber
- Thorn Affinity: +20 (purchased from him)

**Turns 16-20: Boss Fight Start**
```
Turn 16: "The Flame Wraith appears! I cast Flame Shield to protect myself. (20 MP)"
Turn 17: "I attack with Fireball! (30 MP)"
Turn 18: "The Wraith counters with dark flames, hitting me hard."
Turn 19: "I drink a Health Potion to recover."
Turn 20: "I prepare my ultimate spell, Inferno Burst, for next turn."
```

**Expected Final State**:
- HP: 55/75 (damaged, then healed)
- MP: 30/80 (used 50 MP)
- SP: 35/60 (tired from boss fight)
- XP: 7200/7500 (no XP from incomplete boss fight)
- Inventory: Health Potion x2, Mana Potion x2, Goblin Ears x3, 40 gold
- Active Quest: "Defeat the Flame Wraith" (in progress, boss at ~60% HP)
- NPCs: Thorn (Affinity +20), Hooded Figure (Affinity +5), Mayor (Affinity +10)
- Location: Dungeon Boss Chamber (mid-combat)
- Combat State: Turn-based combat active, Wraith's turn next

---

### Part 2: Export State (Turn 21)

**Player Input**:
```
[META] Please export my complete game state as JSON so I can continue this session later.
```

**Expected AIDM Response**:
- Generates JSON or YAML export following `game_state_schema.json`
- Export includes:
  - Character stats (HP/MP/SP/XP/Level/Skills)
  - Inventory (all items, quantities, equipped gear)
  - NPCs (names, affinity, flags, last known location)
  - Quests (name, status, progress, description)
  - World state (location, time, weather, faction states)
  - Combat state (if in combat)
  - Memory threads (recent events, important moments)

**Example Export** (abbreviated):
```json
{
  "character": {
    "name": "Ignis",
    "level": 5,
    "xp": {"current": 7200, "next_level": 7500},
    "hp": {"current": 55, "max": 75},
    "mp": {"current": 30, "max": 80},
    "sp": {"current": 35, "max": 60},
    "stats": {"STR": 8, "DEX": 10, "CON": 12, "INT": 16, "WIS": 11, "CHA": 9},
    "skills": [
      {"name": "Fire Bolt", "cost": 10, "type": "attack"},
      {"name": "Fireball", "cost": 30, "type": "attack"},
      {"name": "Flame Shield", "cost": 20, "type": "defense"},
      {"name": "Inferno Burst", "cost": 60, "type": "ultimate", "cooldown": 0}
    ]
  },
  "inventory": {
    "items": [
      {"name": "Health Potion", "quantity": 2},
      {"name": "Mana Potion", "quantity": 2},
      {"name": "Goblin Ears", "quantity": 3}
    ],
    "equipment": {"weapon": "Flame Staff", "armor": "Mage Robes"},
    "currency": {"gold": 40}
  },
  "npcs": [
    {"name": "Thorn", "role": "Blacksmith", "affinity": 20, "location": "Riverside Town"},
    {"name": "Hooded Figure", "role": "Mysterious Stranger", "affinity": 5, "flags": ["mysterious", "dungeon_warning"]},
    {"name": "Mayor", "role": "Quest Giver", "affinity": 10, "location": "Riverside Town Hall"}
  ],
  "quests": [
    {
      "name": "Defeat the Flame Wraith",
      "status": "active",
      "progress": "Boss fight in progress, Wraith at ~60% HP",
      "giver": "Mayor"
    }
  ],
  "world_state": {
    "location": "Ancient Dungeon - Boss Chamber",
    "time": "Day 2, Late Morning",
    "weather": "N/A (underground)"
  },
  "combat_state": {
    "active": true,
    "enemy": "Flame Wraith",
    "enemy_hp": {"current": 120, "max": 200},
    "turn_order": ["Flame Wraith", "Ignis"],
    "current_turn": "Flame Wraith"
  },
  "memory_highlights": [
    "Met Thorn the blacksmith and built friendly relationship",
    "Received warning about dungeon boss from Hooded Figure",
    "Accepted quest from Mayor to defeat Flame Wraith",
    "Currently mid-boss fight in dungeon depths"
  ]
}
```

**Validation**:
- [ ] Export is valid JSON/YAML (no syntax errors)
- [ ] All required fields present (per schema)
- [ ] Data matches expected state (HP 55/75, MP 30/80, etc.)
- [ ] NPCs with affinity values listed
- [ ] Quest state preserved
- [ ] Combat state saved (boss HP, turn order)

---

### Part 3: New Session Import (Turn 1 of Session 2)

**Setup**:
1. **Close current LLM session completely**
2. **Start brand new LLM session** (fresh context)
3. **Load AIDM files again** (same as Session 1)
4. **Do NOT give any context about previous session**

**Player Input** (in new session):
```
[META] I have a saved game state I want to continue. Here's the JSON export:

[PASTE FULL EXPORT FROM PART 2]

Please restore my game and let me continue from where I left off.
```

**Expected AIDM Response**:
- Acknowledges import request
- Parses JSON/YAML export
- Validates data integrity
- Restores all game state
- Displays character sheet to confirm restoration
- **Resumes narrative exactly where left off** (mid-boss fight)

**Example AIDM Response**:
```
[AIDM confirms] Game state imported successfully!

CHARACTER: Ignis (Level 5 Fire Mage)
HP: 55/75 | MP: 30/80 | SP: 35/60
XP: 7200/7500

You are in the Ancient Dungeon Boss Chamber, locked in fierce combat with the Flame Wraith. The spectral creature writhes before you, dark flames flickering around its form (~60% HP remaining). You've just prepared to cast your ultimate spell, Inferno Burst.

It's currently the Flame Wraith's turn. The wraith raises its arms, gathering dark fire energy...

[Combat continues from exact state]
```

**Validation Checks**:
- [ ] Character stats match (HP 55/75, MP 30/80, SP 35/60)
- [ ] XP correct (7200/7500)
- [ ] Inventory intact (Health Potion x2, Mana Potion x2, Goblin Ears x3, 40 gold)
- [ ] Skills present (Fire Bolt, Fireball, Flame Shield, Inferno Burst)
- [ ] NPCs restored (Thorn affinity 20, Hooded Figure affinity 5, Mayor affinity 10)
- [ ] Quest active ("Defeat Flame Wraith", in progress)
- [ ] Location correct (Dungeon Boss Chamber)
- [ ] Combat state preserved (Wraith at ~60% HP, Wraith's turn)

---

### Part 4: Verify State Persistence (Turns 2-5 of Session 2)

**Turn 2: Test Combat Continuity**
```
Player: "I continue the fight as the Wraith attacks me."
```

**Expected**:
- Boss fight continues seamlessly
- HP/MP/SP tracked from restored values
- No reset or discontinuity

**Turn 3: Test NPC Memory**
```
Player: "After defeating the Wraith (assuming I win), I return to Riverside and visit Thorn."
```

**Expected**:
- Thorn recognizes player (affinity 20 maintained)
- References previous interaction ("Good to see you again!" not "Who are you?")
- Relationship intact

**Turn 4: Test Quest Completion**
```
Player: "I report to the Mayor that the Flame Wraith is defeated."
```

**Expected**:
- Quest updates to "Complete"
- Mayor remembers giving quest (affinity 10 maintained)
- Quest reward given
- No "What quest?" confusion

**Turn 5: Test Inventory Persistence**
```
Player: "I check my inventory. Do I still have the Goblin Ears I collected earlier?"
```

**Expected**:
- Goblin Ears x3 present
- All other items intact
- No inventory wipe

**Final Validation**:
- [ ] Combat state restored and playable
- [ ] NPC memory intact (no "new NPC" treatment)
- [ ] Quest completion works (system remembers quest existed)
- [ ] Inventory fully preserved
- [ ] No data loss detected

---

## Success Determination

### PASS Criteria (All must be true)

1. **Export Successful**:
   - Valid JSON/YAML generated
   - All critical data fields present
   - Export matches actual game state

2. **Import Successful**:
   - New session loads export without errors
   - All data restored accurately
   - No parsing failures

3. **Data Integrity**:
   - Stats match exactly (HP/MP/SP/XP/Level)
   - Inventory complete (all items, quantities, gold)
   - NPCs restored (names, affinity, flags)
   - Quests intact (name, status, progress)
   - World state preserved (location, time)
   - Combat state functional (if applicable)

4. **Continuity**:
   - Narrative resumes seamlessly (no "You wake up in a field" reset)
   - NPCs remember player (affinity behavior consistent)
   - Quest system functional (can complete imported quests)
   - No contradictions or discontinuities

### FAIL Criteria (Any triggers failure)

1. ❌ Export fails completely (no JSON generated or corrupted)
2. ❌ Import fails (parser errors, can't load state)
3. ❌ Critical data loss (HP/MP reset, inventory wiped, NPCs forgotten)
4. ❌ Narrative reset (game starts over despite import)
5. ❌ Quest corruption (active quests become "unknown" or "never existed")

### PARTIAL Criteria (Minor issues acceptable)

⚠️ Minor data loss (e.g., weather state not preserved)  
⚠️ Formatting issues (data correct but display ugly)  
⚠️ NPC memory slightly fuzzy (recognize player but forget minor details)  
⚠️ Import requires player clarification (e.g., "Which location were you in?")

---

## Results Template

**Test Execution Date**: ___________  
**LLM Platform**: ___________  
**LLM Version**: ___________

### Export Quality
- [ ] JSON/YAML valid syntax
- [ ] All required fields present
- [ ] Data accuracy (matches game state)
- **Export Issues**: ___________

### Import Quality
- [ ] Import successful (no errors)
- [ ] Data parsed correctly
- [ ] Restoration complete
- **Import Issues**: ___________

### Data Integrity
- [ ] Stats restored (HP/MP/SP/XP)
- [ ] Inventory intact (items/gold)
- [ ] NPCs preserved (affinity/flags)
- [ ] Quests functional
- [ ] Location/world state correct
- **Data Loss**: ___________

### Continuity Quality
- [ ] Narrative seamless
- [ ] NPC memory intact
- [ ] Quest completion works
- [ ] No contradictions
- **Continuity Issues**: ___________

### Overall Result
- [ ] ✅ PASS
- [ ] ⚠️ PARTIAL PASS
- [ ] ❌ FAIL

**Notes**: ___________

---

## Troubleshooting

### If Test Fails

**Issue**: Export fails or generates invalid JSON
- **Cause**: Schema not loaded or LLM can't generate structured data
- **Fix**: Verify game_state_schema.json loaded; try YAML format

**Issue**: Import fails with parser errors
- **Cause**: Malformed export or schema mismatch
- **Fix**: Validate JSON syntax; check schema version compatibility

**Issue**: Stats reset to default
- **Cause**: State not parsed or applied correctly
- **Fix**: Check state_persistence.md loaded; verify character_schema.json

**Issue**: NPCs forgotten
- **Cause**: NPC data not exported or not restored
- **Fix**: Check npc_schema.json; verify memory_management.md loaded

**Issue**: Narrative starts over
- **Cause**: AIDM treats import as "new game"
- **Fix**: Explicitly instruct "CONTINUE from this state, don't start new game"

---

## Test Artifacts to Save

1. **Full Session 1 transcript** (Turn 1-21)
2. **Complete JSON/YAML export** (save to file)
3. **Full Session 2 transcript** (Turn 1-5+)
4. **State comparison table** (Before export vs After import)
5. **Any error messages** (if applicable)

Store in: `tests/results/test_3_session_persistence_[DATE].md`

---

**Test Status**: Ready for execution  
**Next Action**: Execute 20-turn session and export state
