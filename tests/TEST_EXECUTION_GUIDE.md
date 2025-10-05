# TEST-001 Execution Guide: Cold Start (Naruto World)

**Test Date**: October 3, 2025  
**Status**: 🔄 IN PROGRESS  
**Tester**: AIDM Development Team

---

## Quick Start Instructions

### Step 1: Prepare Fresh LLM Session

⚠️ **CRITICAL**: Open a **completely new LLM conversation** (not this one!)

**Recommended Platforms**:
- Claude Sonnet 4.5 (preferred - best reasoning)
- ChatGPT-4o (acceptable)
- Claude Opus 3.5 (acceptable)

**Required Capabilities**:
- Long context window (100k+ tokens)
- Web search enabled (for Naruto research)
- File attachment support OR copy-paste capability

---

### Step 2: Load AIDM Core Files (In Order)

Copy and paste these files into the fresh LLM session **in this exact order**:

#### A. Core Instructions (1 file)
```
📁 aidm/CORE_AIDM_INSTRUCTIONS.md
```

#### B. Instruction Modules (12 files - load all)
```
📁 aidm/instructions/00_session_zero.md
📁 aidm/instructions/01_world_research.md
📁 aidm/instructions/02_character_creation.md
📁 aidm/instructions/03_narrative_engine.md
📁 aidm/instructions/04_combat_system.md
📁 aidm/instructions/05_memory_management.md
📁 aidm/instructions/06_npc_intelligence.md
📁 aidm/instructions/07_quest_management.md
📁 aidm/instructions/08_progression_system.md
📁 aidm/instructions/09_genre_adaptation.md
📁 aidm/instructions/10_error_recovery.md
📁 aidm/instructions/11_state_management.md
```

#### C. Schema Definitions (7 files - load all)
```
📁 aidm/schemas/character_schema.json
📁 aidm/schemas/npc_schema.json
📁 aidm/schemas/quest_schema.json
📁 aidm/schemas/world_state_schema.json
📁 aidm/schemas/combat_schema.json
📁 aidm/schemas/item_schema.json
📁 aidm/schemas/session_schema.json
```

**Total Files to Load**: 20 files (~41,500 lines)

⏱️ **Estimated Load Time**: 5-10 minutes (depending on copy-paste speed)

---

### Step 3: Load Support Libraries (Optional but Recommended)

These libraries help with Naruto-specific content:

```
📁 aidm/libraries/power_systems/ki_lifeforce_systems.md (contains chakra system)
📁 aidm/libraries/genre_tropes/shonen_tropes.md (ninja tropes)
📁 aidm/libraries/world_building/faction_templates.md (village structures)
```

**Optional**: Can be loaded on-demand if AIDM requests them

---

### Step 4: Initiate AIDM System

Once all files are loaded, send this initialization message:

```
System initialized. AIDM v2.0 ready. All core instructions, schemas, and libraries loaded.

Awaiting player input to begin Session Zero.
```

**Expected Response**: AIDM confirms ready state

---

### Step 5: Begin TEST-001 Execution

Now follow the test script exactly as written in `TEST_1_COLD_START.md`:

#### Exchange 1: Initial Request
**Player says**:
```
I want to play in a world like Naruto.
```

**Watch for**:
- AIDM recognizes "Naruto" as anime
- Session Zero protocol initiates
- Research attempt (may search web for Naruto info)
- Clarifying questions asked

---

#### Exchanges 2-4: World Setup + Preferences

**Player responds to AIDM questions with**:
```
Exchange 2: "Let's do an original timeline, a few years after the Fourth Great Ninja War. I'll start in Konohagakure (Hidden Leaf Village)."

Exchange 3: "Canon characters exist and are alive, but I want to play an original character, not a canon one."

Exchange 4: "Medium violence is fine (blood but not gore), open to tragedy and romance. I like tactical combat with jutsu variety. Moderate pacing."
```

**Watch for**:
- Correct recognition of "Konohagakure" (not "Konoha Village")
- Understanding of "Fourth Great Ninja War" context
- Appropriate preference questions

---

#### Exchanges 5-7: Character Creation

**Player provides character details**:
```
Exchange 5: "I want to be from a mid-tier clan (not Uchiha/Hyuga level, but not civilian). Maybe a skilled jonin or ANBU member."

Exchange 6: "Let's go with a Lightning Style (Raiton) specialist with some medical ninjutsu training. Stats around mid-jonin level."

Exchange 7: "Name is Takeshi Kaminari, 28 years old, calm and analytical personality. Has a friendly rivalry with Kakashi. Wears standard ANBU gear but with Lightning Style modifications."
```

**Watch for**:
- Clan options offered are Naruto-appropriate
- "Chakra" used (not "mana" or "MP")
- "Raiton" recognized (Lightning Style)
- Stats assigned appropriately (jonin ~Level 12-15)

---

#### Exchanges 8-10: Opening Scene + First Action

**Player requests scene start**:
```
Exchange 8: "I'm ready to start! Let's begin with me receiving a mission briefing from the Hokage."

Exchange 9-10: (Respond to opening scene with an action)
Example: "I accept the mission and prepare to head out."
```

**Watch for**:
- Character sheet displayed (HP/Chakra/Stamina, jutsu list, equipment)
- Opening scene in Hokage's office or similar Naruto location
- Naruto (as Hokage) or another canon character may appear
- Player can take meaningful action

---

### Step 6: Validation Checklist

After Exchange 10, evaluate against these criteria:

#### ✅ PASS Criteria (All must be true)

- [ ] **Exchange count**: Player has playable character in ≤10 exchanges
- [ ] **Chakra system**: Referenced as "chakra" (NOT "mana" or generic magic)
- [ ] **Village names**: "Konohagakure" spelled correctly
- [ ] **Jutsu terms**: "Raiton" used (NOT "Lightning Magic")
- [ ] **Rank system**: Genin/Chunin/Jonin/ANBU referenced correctly
- [ ] **Character creation**: 5-phase process followed
- [ ] **Stats assigned**: HP/Chakra/Stamina (or equivalent) present
- [ ] **Skills listed**: Jutsu/abilities documented
- [ ] **Equipment present**: Inventory/gear shown
- [ ] **Opening scene**: Naruto-appropriate (ninja village, missions, etc.)
- [ ] **Player agency**: Can take meaningful action

#### ❌ FAIL Criteria (Any triggers FAIL)

- [ ] Takes >10 exchanges to playability
- [ ] Calls chakra "mana" or "magic points"
- [ ] Wrong village names ("Konoha Village of Leaves" instead of "Konohagakure")
- [ ] Character creation skipped
- [ ] No character sheet provided
- [ ] Generic fantasy opening (not Naruto-like)
- [ ] Player stuck in dialog loop (cannot act)

#### ⚠️ PARTIAL Criteria (Minor issues)

- [ ] Exactly 10 exchanges (borderline acceptable)
- [ ] Minor timeline inaccuracies
- [ ] Character sheet formatting ugly but data present

---

### Step 7: Document Results

Create file: `tests/results/test_1_cold_start_2025-10-03.md`

**Copy and save**:
1. Full conversation transcript (all exchanges)
2. Final character sheet (exact text)
3. Opening scene narrative (exact text)
4. Any errors or issues encountered
5. Screenshots (if applicable)

**Fill out results template** (from TEST_1_COLD_START.md):

```markdown
**Test Execution Date**: October 3, 2025
**LLM Platform**: [Claude/ChatGPT/Other]
**LLM Version**: [Sonnet 4.5/GPT-4o/etc]

### Exchange Count
- Total exchanges to playable: [NUMBER]
- Breakdown:
  - World setup: [NUMBER]
  - Preferences: [NUMBER]
  - Character creation: [NUMBER]
  - Opening scene: [NUMBER]

### Research Accuracy
- [✅/❌] Chakra system correct
- [✅/❌] Village names correct
- [✅/❌] Jutsu terminology correct
- [✅/❌] Rank system correct
- **Errors Found**: [LIST ANY]

### Character Creation Quality
- [✅/❌] 5-phase process followed
- [✅/❌] Stats assigned correctly
- [✅/❌] Skills/jutsu listed
- [✅/❌] Equipment present
- **Issues Found**: [LIST ANY]

### Opening Scene Quality
- [✅/❌] Naruto-appropriate setting
- [✅/❌] Canon integration (if requested)
- [✅/❌] Player agency present
- **Issues Found**: [LIST ANY]

### Overall Result
- [ ] ✅ PASS
- [ ] ⚠️ PARTIAL PASS
- [ ] ❌ FAIL

**Notes**: [DETAILED OBSERVATIONS]
```

---

## Troubleshooting Common Issues

### Issue: "I don't have web search in my LLM"
**Solution**: Pre-load ki_lifeforce_systems.md (contains Naruto chakra details)

### Issue: "Files are too large to paste"
**Solution**: Use file attachment feature OR load in smaller batches

### Issue: "AIDM doesn't recognize it's a game master"
**Solution**: Re-paste CORE_AIDM_INSTRUCTIONS.md and confirm with "You are AIDM, an AI game master. Confirm ready status."

### Issue: "AIDM asks too many questions (>10 exchanges)"
**Solution**: Be concise in responses, combine answers ("I want X, Y, and Z")

### Issue: "Character sheet not displaying"
**Solution**: Explicitly ask "Please show my character sheet" after creation

---

## Test Status Tracking

**Current Phase**: 🔄 Preparation  
**Files Loaded**: 0/20 core files  
**Exchange Count**: 0  
**Issues Encountered**: None yet

**Next Action**: Open fresh LLM session and load files

---

## Quick File Path Reference

All files are in: `c:\Users\admin\Downloads\workspace\aidm\`

**Core**: `CORE_AIDM_INSTRUCTIONS.md`  
**Instructions**: `instructions/00_session_zero.md` through `11_state_management.md`  
**Schemas**: `schemas/character_schema.json` through `session_schema.json`  
**Libraries**: `libraries/power_systems/ki_lifeforce_systems.md` (Naruto chakra)

---

**Ready to Execute**: Yes ✅  
**Estimated Test Duration**: 30-45 minutes  
**Confidence Level**: HIGH (comprehensive test script prepared)

