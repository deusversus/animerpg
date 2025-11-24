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
2. All files in `aidm/instructions/` (**14 files** - updated from 12)
3. All files in `aidm/schemas/` (**15+ files** - updated from 7)
   - **Critical**: `session_export_schema.json` (defines export format, renamed from game_state_schema.json)
   - **Critical**: `character_schema.json` v2.3.0 (with tier_xp, awakening_stage, death_saves, injuries)
4. **4 meta-schemas** (for mechanical systems validation):
   - `aidm/schemas/economy_meta_schema.json`
   - `aidm/schemas/progression_meta_schema.json`
   - `aidm/schemas/downtime_meta_schema.json`
   - `aidm/schemas/crafting_meta_schema.json`

**Platform**: Claude Sonnet 4.5, ChatGPT-4, or equivalent  
**Recommended**: LLM with code execution (for JSON validation)

---

## Test Procedure

### Part 1: Create Test State (Turns 1-20)

**Turn 1: Character Creation**
```
Player: "Quick character: I'm a Level 5 fire mage named Ignis in a fantasy isekai world (Hunter x Hunter style with Nen magic). Let's skip Session Zero and jump right in."
```

**Expected**: Character created with stats:
- HP: ~50-75
- MP: ~60-80 (Aura equivalent)
- SP: ~40-60
- **Tier**: Journeyman (Hunter x Hunter mastery_tiers)
- **tier_xp**: ~3500/5000 (mid-Journeyman tier)
- Skills: Fire Bolt (Emission), Fireball (Emission), Flame Shield (Enhancement)
- Inventory: Staff, Health Potion x3, **5,000 Jenny** (NOT "gold" - Hunter x Hunter currency)

**Turns 2-5: Combat Encounter**
```
Turn 2: "I'm exploring a dungeon and encounter 3 goblin scouts."
Turn 3: "I cast Fireball at the goblins. (30 MP cost)"
Turn 4: "I use Fire Bolt on the remaining goblin. (10 MP)"
Turn 5: "I loot the goblin corpses."
```

**Expected State Changes**:
- HP: 50/75 (took some damage)
- MP: 20/80 (used 60 Aura total)
- **tier_xp**: 4200/5000 (gained 700 tier XP from combat)
- Inventory: +Goblin Ears x3, **+150 Jenny** (NOT gold)

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
- **Jenny**: 4,750 (spent 250 on ale and inn)
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
- **Jenny**: 4,250 (spent 500 on Mana Potions)
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
- MP: 30/80 (used 50 Aura)
- SP: 35/60 (tired from boss fight)
- **Tier**: Journeyman (mastery_tiers progression)
- **tier_xp**: 4200/5000 (no XP from incomplete boss fight)
- Inventory: Health Potion x2, Mana Potion x2, Goblin Ears x3, **4,250 Jenny**
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
- Generates JSON or YAML export following `session_export_schema.json` (renamed from game_state_schema.json)
- Export includes:
  - Character stats (HP/MP/SP/tier_xp/Tier/Skills)
  - **Mechanical systems** (economy, progression, downtime configs)
  - Inventory (all items, quantities, equipped gear, **Jenny currency**)
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
    "tier": "Journeyman",
    "tier_xp": {"current": 4200, "next_tier": 5000},
    "hp": {"current": 55, "max": 75},
    "mp": {"current": 30, "max": 80},
    "sp": {"current": 35, "max": 60},
    "stats": {"STR": 8, "DEX": 10, "CON": 12, "INT": 16, "WIS": 11, "CHA": 9},
    "skills": [
      {"name": "Fire Bolt (Emission)", "cost": 10, "type": "attack"},
      {"name": "Fireball (Emission)", "cost": 30, "type": "attack"},
      {"name": "Flame Shield (Enhancement)", "cost": 20, "type": "defense"},
      {"name": "Inferno Burst", "cost": 60, "type": "ultimate", "cooldown": 0}
    ]
  },
  "mechanical_systems": {
    "economy": {
      "type": "fiat_currency",
      "currency_name": "Jenny",
      "scarcity": "moderate",
      "special_mechanics": []
    },
    "progression": {
      "type": "mastery_tiers",
      "tier_system": {
        "tiers": ["Novice", "Journeyman", "Expert", "Master", "Grandmaster"],
        "tier_bonuses": {
          "Journeyman": {"aura_control": 2, "technique_damage": 2}
        }
      },
      "advancement_rules": {
        "demonstration_required": true,
        "auto_level": false
      }
    },
    "downtime": {
      "enabled_modes": ["training_arcs", "investigation"],
      "activity_configs": {}
    }
  },
  "inventory": {
    "items": [
      {"name": "Health Potion", "quantity": 2},
      {"name": "Mana Potion", "quantity": 2},
      {"name": "Goblin Ears", "quantity": 3}
    ],
    "equipment": {"weapon": "Flame Staff", "armor": "Mage Robes"},
    "currency": {"Jenny": 4250}
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
- [ ] All required fields present (per session_export_schema.json)
- [ ] Data matches expected state (HP 55/75, MP 30/80, tier_xp 4200/5000)
- [ ] **mechanical_systems section present** (economy, progression, downtime)
- [ ] **Currency: Jenny (NOT gold)**
- [ ] **Progression type: mastery_tiers**
- [ ] **tier_xp field: 4200/5000 (NOT character_xp or XP)**
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

CHARACTER: Ignis (Journeyman Fire Nen User)
HP: 55/75 | MP: 30/80 (Aura) | SP: 35/60
Tier: Journeyman | Tier XP: 4200/5000
Currency: 4,250 Jenny

You are in the Ancient Dungeon Boss Chamber, locked in fierce combat with the Flame Wraith. The spectral creature writhes before you, dark flames flickering around its form (~60% HP remaining). You've just prepared to cast your ultimate spell, Inferno Burst.

It's currently the Flame Wraith's turn. The wraith raises its arms, gathering dark fire energy...

[Combat continues from exact state]
```

**Validation Checks**:
- [ ] Character stats match (HP 55/75, MP 30/80, SP 35/60)
- [ ] **Tier correct: Journeyman (NOT Level 5)**
- [ ] **tier_xp correct: 4200/5000 (NOT character_xp)**
- [ ] Inventory intact (Health Potion x2, Mana Potion x2, Goblin Ears x3, **4,250 Jenny NOT gold**)
- [ ] Skills present (Fire Bolt, Fireball, Flame Shield, Inferno Burst)
- [ ] **Mechanical systems restored** (economy: Jenny/fiat_currency, progression: mastery_tiers, downtime: training_arcs+investigation)
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
- [ ] **Mechanical systems functional** (tier_xp advances, Jenny currency used in transactions, tier advancement requires demonstration)
- [ ] **Progression type respected** (mastery_tiers rules apply, NOT standard leveling)
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
   - Stats match exactly (HP/MP/SP/tier_xp/Tier)
   - **Mechanical systems preserved** (economy: Jenny, progression: mastery_tiers, downtime: enabled_modes)
   - Inventory complete (all items, quantities, **Jenny currency NOT gold**)
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
4. ❌ **Mechanical systems lost** (currency reverts to "gold", progression reverts to standard leveling, tier_xp becomes character_xp)
5. ❌ **Progression type not respected** (tier advancement auto-levels, demonstration requirement ignored)
6. ❌ Narrative reset (game starts over despite import)
7. ❌ Quest corruption (active quests become "unknown" or "never existed")

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
- [ ] Stats restored (HP/MP/SP/tier_xp/Tier)
- [ ] **Mechanical systems preserved** (economy/progression/downtime)
- [ ] **Currency correct** (Jenny NOT gold)
- [ ] **Progression type correct** (mastery_tiers NOT standard leveling)
- [ ] **tier_xp field present** (NOT character_xp)
- [ ] Inventory intact (items/**Jenny**)
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
- **Fix**: Check session_export_schema.json (renamed from game_state_schema.json) loaded; verify character_schema.json v2.3.0

**Issue**: Currency reverts to "gold" (not Jenny)
- **Cause**: mechanical_systems section not exported or not restored
- **Fix**: Verify mechanical_systems section in export JSON, check economy_meta_schema.json loaded

**Issue**: tier_xp becomes character_xp or XP field
- **Cause**: Progression type not preserved, reverted to class_based default
- **Fix**: Verify mechanical_systems.progression in export, check progression_meta_schema.json loaded

**Issue**: Tier advancement auto-levels (ignores demonstration requirement)
- **Cause**: Progression advancement_rules not preserved
- **Fix**: Check mechanical_systems.progression.advancement_rules in export (demonstration_required: true, auto_level: false)

**Issue**: NPCs forgotten
- **Cause**: NPC data not exported or not restored
- **Fix**: Check npc_schema.json; verify 04_npc_intelligence.md loaded

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
