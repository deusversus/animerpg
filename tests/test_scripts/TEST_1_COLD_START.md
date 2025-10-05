# Test 1: Cold Start (Naruto World)

**Test ID**: AIDM-TEST-001  
**Category**: Core Functionality  
**Priority**: CRITICAL  
**Estimated Time**: 20-30 minutes

---

## Test Objective

Validate that a new player can go from zero to playable character in <10 exchanges when requesting a Naruto-inspired world.

**Success Criteria**:
1. Playable character exists within 10 exchanges
2. AIDM correctly researches Naruto concepts (chakra, jutsu, villages)
3. 5-phase character creation process followed
4. Opening scene generated appropriately

---

## Pre-Test Setup

### Files to Load into LLM

**Required** (load in this order):
1. `aidm/CORE_AIDM_INSTRUCTIONS.md`
2. All files in `aidm/instructions/` (12 files)
3. All files in `aidm/schemas/` (7 files)

**Optional** (can be loaded on-demand):
- `aidm/libraries/power_systems/ki_lifeforce_systems.md` (contains Naruto chakra info)
- `aidm/libraries/genre_tropes/shonen_tropes.md` (contains ninja tropes)

**Platform**: Claude Sonnet 4.5, ChatGPT-4, or equivalent  
**Required Features**: Web search (for Naruto research)

---

## Test Procedure

### Exchange 1: Initial Request

**Player Input**:
```
I want to play in a world like Naruto.
```

**Expected AIDM Response**:
- Acknowledges request
- Initiates Session Zero protocol
- May perform web research on Naruto
- Asks clarifying questions about player preferences

**Validation Checks**:
- [ ] AIDM recognizes Naruto as anime/manga
- [ ] Session Zero workflow initiated
- [ ] No hallucinated Naruto details (if research performed)

---

### Exchange 2-4: Session Zero (Phase 1-2)

**Expected Flow**:
- **Phase 1: World Setup**
  - AIDM asks: Setting period (canon era vs original timeline)
  - AIDM asks: Village/faction starting location
  - AIDM asks: Canon characters present or all-original cast
  
**Player Inputs** (adapt as needed):
```
Exchange 2: "Let's do an original timeline, a few years after the Fourth Great Ninja War. I'll start in Konohagakure (Hidden Leaf Village)."

Exchange 3: "Canon characters exist and are alive, but I want to play an original character, not a canon one."
```

**Validation Checks**:
- [ ] AIDM understands Konohagakure reference
- [ ] AIDM knows Fourth Great Ninja War context
- [ ] Phase 1 questions appropriate for Naruto world

---

### Exchange 5-7: Session Zero (Phase 2-3)

**Expected Flow**:
- **Phase 2: Gameplay Preferences**
  - Content preferences (violence, tragedy, romance)
  - Combat complexity preference
  - Pacing preference
  
- **Phase 3: Character Creation Start**
  - Background selection
  - Clan/bloodline options
  - Basic stats/skills

**Player Inputs** (example):
```
Exchange 4: "Medium violence is fine (blood but not gore), open to tragedy and romance. I like tactical combat with jutsu variety. Moderate pacing."

Exchange 5: "I want to be from a mid-tier clan (not Uchiha/Hyuga level, but not civilian). Maybe a skilled jonin or ANBU member."

Exchange 6: "Let's go with a Lightning Style (Raiton) specialist with some medical ninjutsu training. Stats around mid-jonin level."
```

**Validation Checks**:
- [ ] AIDM offers appropriate clan options (Naruto-specific clans)
- [ ] Chakra/jutsu system referenced correctly
- [ ] Stats assigned appropriately (jonin ~Level 12-15 in D&D equivalent)

---

### Exchange 8-9: Session Zero (Phase 4-5)

**Expected Flow**:
- **Phase 4: Character Finalization**
  - Name, appearance, personality
  - Starting equipment/jutsu
  - Relationships/connections
  
- **Phase 5: Opening Scene**
  - World state established
  - Character positioned in world
  - Opening scene narrated

**Player Inputs** (example):
```
Exchange 7: "Name is Takeshi Kaminari, 28 years old, calm and analytical personality. Has a friendly rivalry with Kakashi. Wears standard ANBU gear but with Lightning Style modifications."

Exchange 8: "I'm ready to start! Let's begin with me receiving a mission briefing from the Hokage."
```

**Expected Opening Scene**:
- Set in Hokage's office or mission briefing room
- Naruto (as Hokage) or another canon character present
- Mission or scenario introduced
- Character can take action

**Validation Checks**:
- [ ] Character sheet displayed (HP/MP/SP, jutsu list, inventory)
- [ ] Opening scene is Naruto-appropriate (villages, ninja missions)
- [ ] Player can take meaningful action

---

### Exchange 10: Playable Confirmation

**Player Input**:
```
I accept the mission and prepare to head out.
```

**Expected AIDM Response**:
- Processes player action
- Updates world state
- Continues narrative

**Validation Checks**:
- [ ] Character is fully playable (can move, act, make choices)
- [ ] Game state tracked (HP/MP/SP visible if relevant)
- [ ] Naruto world elements present (chakra, jutsu, villages)

---

## Success Determination

### PASS Criteria (All must be true)

1. **Exchange Count**: Player has playable character in ≤10 exchanges
2. **Research Accuracy**: 
   - Chakra system referenced correctly (not "mana" or generic magic)
   - Village names correct (Konohagakure, not "Konoha Village of Leaves")
   - Jutsu terminology accurate (Raiton, not "Lightning Magic")
   - Rank system correct (Genin/Chunin/Jonin/ANBU/Kage)
3. **Character Creation**:
   - 5-phase process followed (World, Preferences, Character, Finalize, Opening)
   - Stats assigned (HP/Chakra/Stamina or equivalent)
   - Jutsu/skills listed
   - Inventory/equipment present
4. **Opening Scene**:
   - Naruto-appropriate setting (ninja village, missions, etc.)
   - Canon elements integrated if requested
   - Player can take meaningful action

### FAIL Criteria (Any triggers failure)

1. ❌ Takes >10 exchanges to reach playable state
2. ❌ Major Naruto lore errors (e.g., calls chakra "mana", wrong village names)
3. ❌ Character creation skipped or incomplete
4. ❌ Opening scene inappropriate (generic fantasy, not Naruto-like)
5. ❌ Player cannot take action (stuck in dialog loop)

### PARTIAL Criteria (Minor issues acceptable)

⚠️ Minor lore inaccuracies (e.g., slightly wrong timeline details)  
⚠️ Takes exactly 10 exchanges (borderline acceptable)  
⚠️ Character sheet formatting issues (data present but ugly)

---

## Results Template

**Test Execution Date**: ___________  
**LLM Platform**: ___________  
**LLM Version**: ___________

### Exchange Count
- Total exchanges to playable: ___________
- Breakdown:
  - World setup: ___________
  - Preferences: ___________
  - Character creation: ___________
  - Opening scene: ___________

### Research Accuracy
- [ ] Chakra system correct
- [ ] Village names correct
- [ ] Jutsu terminology correct
- [ ] Rank system correct
- **Errors Found**: ___________

### Character Creation Quality
- [ ] 5-phase process followed
- [ ] Stats assigned correctly
- [ ] Skills/jutsu listed
- [ ] Equipment present
- **Issues Found**: ___________

### Opening Scene Quality
- [ ] Naruto-appropriate setting
- [ ] Canon integration (if requested)
- [ ] Player agency present
- **Issues Found**: ___________

### Overall Result
- [ ] ✅ PASS
- [ ] ⚠️ PARTIAL PASS
- [ ] ❌ FAIL

**Notes**: ___________

---

## Troubleshooting

### If Test Fails

**Issue**: Takes >10 exchanges
- **Cause**: AIDM may be over-asking questions
- **Fix**: Check if Session Zero module is too verbose; consider streamlining

**Issue**: Wrong Naruto details
- **Cause**: Research failed or hallucination
- **Fix**: Check web search capability; verify ki_lifeforce_systems.md loaded

**Issue**: Character sheet missing
- **Cause**: Schema not loaded or not applied
- **Fix**: Verify character_schema.json loaded; check CORE instructions

**Issue**: Generic fantasy instead of Naruto
- **Cause**: Genre adaptation failed
- **Fix**: Check shonen_tropes.md loaded; verify tone adaptation in instructions

---

## Test Artifacts to Save

After test execution, save these for documentation:

1. **Full conversation transcript** (all 10+ exchanges)
2. **Final character sheet** (copy exact text)
3. **Opening scene text** (copy exact narrative)
4. **Any error messages** (if applicable)
5. **Screenshots** (if using web interface)

Store in: `tests/results/test_1_cold_start_[DATE].md`

---

**Test Status**: Ready for execution  
**Next Action**: Load files into LLM and begin test
