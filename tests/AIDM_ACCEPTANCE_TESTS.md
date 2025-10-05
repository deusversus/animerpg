# AIDM v2.0 Acceptance Test Suite

**Document Version**: 1.0  
**Test Date**: October 3, 2025  
**Test Executor**: AIDM Development Team  
**System Version**: AIDM v2.0 (44/50 files, 12/12 libraries complete)

---

## Test Execution Overview

This document tracks the execution of all 8 acceptance tests defined in `SCOPE.md`. Each test validates a critical system capability.

**Test Status Legend**:
- ✅ **PASS**: Test completed successfully, all criteria met
- ⚠️ **PARTIAL**: Test passed with minor issues or caveats
- ❌ **FAIL**: Test failed to meet acceptance criteria
- ⏳ **PENDING**: Test not yet executed

---

## Test 1: Cold Start (Naruto World)

**Status**: ⏳ PENDING

**Objective**: Validate new player onboarding experience

**Test Procedure**:
1. Load AIDM core instructions + schemas into fresh LLM session
2. Player input: "I want to play in a world like Naruto"
3. Count exchanges until playable character exists
4. Verify AIDM researches Naruto correctly

**Pass Criteria**:
- ✅ Reaches playable character in <10 exchanges
- ✅ AIDM correctly researches Naruto (chakra, jutsu, villages, etc.)
- ✅ Character creation follows 5-phase process
- ✅ Opening scene generated appropriately

**Test Execution**: [NOT YET RUN]

**Results**:
- Exchange Count: N/A
- Research Accuracy: N/A
- Character Creation Quality: N/A
- Opening Scene Quality: N/A

**Issues Discovered**: None yet

**Notes**: This test validates the core Session Zero workflow and research protocol.

---

## Test 2: Multi-Anime Fusion

**Status**: ⏳ PENDING

**Objective**: Validate power system harmonization across multiple anime

**Test Procedure**:
1. Load AIDM into fresh session
2. Player input: "I want Naruto ninja powers + Solo Leveling gates + My Hero Academia quirks in one world"
3. Verify coherent power system created
4. Check fusion logic explanation
5. Validate world is playable

**Pass Criteria**:
- ✅ AIDM creates coherent unified power system
- ✅ Fusion logic explained clearly (how systems interact)
- ✅ No contradictions or conflicts
- ✅ World is playable (character can use powers)

**Test Execution**: [NOT YET RUN]

**Results**:
- Power System Coherence: N/A
- Fusion Logic Quality: N/A
- Contradiction Count: N/A
- Playability: N/A

**Issues Discovered**: None yet

**Notes**: This test validates the power system library integration (mana, ki, soul, psionic frameworks) and anime fusion capabilities.

---

## Test 3: Session Persistence

**Status**: ⏳ PENDING

**Objective**: Validate state export/import functionality

**Test Procedure**:
1. Start new session, create character
2. Play for 20 turns (combat, NPC interaction, inventory changes)
3. Use meta-command to export state (JSON/YAML)
4. Start completely new LLM session
5. Import exported state
6. Verify all data restored correctly

**Pass Criteria**:
- ✅ All stats restored (HP/MP/SP/XP/Level)
- ✅ All relationships/affinity values preserved
- ✅ Inventory and equipment correct
- ✅ Plot threads and quest state intact
- ✅ No data loss or corruption

**Test Execution**: [NOT YET RUN]

**Results**:
- Stats Restoration: N/A
- Relationship Preservation: N/A
- Inventory Accuracy: N/A
- Quest State Integrity: N/A
- Data Loss: N/A

**Issues Discovered**: None yet

**Notes**: This test validates the state export/import schema and memory reconstruction capabilities.

---

## Test 4: Combat Mechanics

**Status**: ⏳ PENDING

**Objective**: Validate JRPG combat system functionality

**Test Procedure**:
1. Start session with combat-capable character
2. Engage in tactical turn-based combat
3. Use skills with MP/SP costs
4. Verify resource tracking
5. Check skill prerequisite validation
6. Validate combat consequence integration

**Pass Criteria**:
- ✅ HP/MP/SP tracked accurately each turn
- ✅ Skills validate prerequisites (MP cost, cooldowns, conditions)
- ✅ Damage calculation correct
- ✅ Combat resolves with narrative consequences
- ✅ Turn order logical and consistent

**Test Execution**: [NOT YET RUN]

**Results**:
- Resource Tracking Accuracy: N/A
- Skill Validation: N/A
- Damage Calculation: N/A
- Consequence Integration: N/A
- Turn Order Logic: N/A

**Issues Discovered**: None yet

**Notes**: This test validates the combat module, resource management, and skill system integration.

---

## Test 5: Memory Coherence

**Status**: ⏳ PENDING

**Objective**: Validate NPC memory and relationship consistency over extended play

**Test Procedure**:
1. Start session with multiple NPCs (3-5 characters)
2. Conduct 20+ exchanges involving:
   - Multiple conversations with each NPC
   - Affinity changes (positive and negative)
   - Information sharing between NPCs
   - References to past events
3. Verify NPCs remember previous interactions
4. Check for contradictions or memory loss

**Pass Criteria**:
- ✅ NPCs remember previous conversations
- ✅ Affinity changes persist and affect behavior
- ✅ No contradictions in NPC knowledge
- ✅ Information propagation works (NPC A tells B, B knows)
- ✅ Relationship flags maintained (emotional, persistent, trauma)

**Test Execution**: [NOT YET RUN]

**Results**:
- NPC Memory Accuracy: N/A
- Affinity Persistence: N/A
- Contradiction Count: N/A
- Information Propagation: N/A
- Relationship Flag Integrity: N/A

**Issues Discovered**: None yet

**Notes**: This test validates the memory system, NPC intelligence, and relationship tracking.

---

## Test 6: Error Recovery

**Status**: ⏳ PENDING

**Objective**: Validate graceful error handling and player correction

**Test Procedure**:
1. Start session, play normally
2. Inject deliberate error (e.g., AIDM shows HP as 150 when should be 50)
3. Player corrects: "My HP should be 50, not 150"
4. Verify AIDM acknowledges error
5. Check state correction
6. Validate seamless continuation

**Pass Criteria**:
- ✅ AIDM acknowledges error without defensiveness
- ✅ State corrected immediately
- ✅ Correction propagates to all relevant systems
- ✅ Play continues seamlessly (no interruption)
- ✅ Correction logged in memory/state

**Test Execution**: [NOT YET RUN]

**Results**:
- Error Acknowledgment Quality: N/A
- State Correction Accuracy: N/A
- System Propagation: N/A
- Continuation Seamlessness: N/A
- Logging: N/A

**Issues Discovered**: None yet

**Notes**: This test validates the error recovery protocol and player agency in state management.

---

## Test 7: Genre Adaptation

**Status**: ⏳ PENDING

**Objective**: Validate tone/pacing/focus adaptation across different anime genres

**Test Procedure**:
1. **Session A - Isekai Adventure**: Play 10-15 turns in isekai setting (gate dungeon, leveling, loot)
2. **Session B - Shonen Battle**: Play 10-15 turns in shonen setting (training, tournament, friendship)
3. **Session C - Slice-of-Life Romance**: Play 10-15 turns in slice-of-life setting (school, romance, no combat)
4. Compare tone, pacing, narrative focus across sessions

**Pass Criteria**:
- ✅ **Isekai**: Fast pacing, power fantasy, status screens, dungeon crawling feel
- ✅ **Shonen**: Training arcs, friendship themes, dramatic battles, power-ups
- ✅ **Slice-of-Life**: Slow pacing, relationship focus, seasonal activities, no combat pressure
- ✅ Each session feels genre-authentic
- ✅ AIDM adapts mechanics appropriately (combat vs social stats)

**Test Execution**: [NOT YET RUN]

**Results**:
- **Isekai Session**:
  - Tone Authenticity: N/A
  - Pacing: N/A
  - Mechanics Fit: N/A
- **Shonen Session**:
  - Tone Authenticity: N/A
  - Pacing: N/A
  - Mechanics Fit: N/A
- **Slice-of-Life Session**:
  - Tone Authenticity: N/A
  - Pacing: N/A
  - Mechanics Fit: N/A

**Issues Discovered**: None yet

**Notes**: This test validates the genre trope libraries (isekai_tropes.md, shonen_tropes.md, slice_of_life_tropes.md) and tone adaptation capabilities.

---

## Test 8: Research Validation

**Status**: ⏳ PENDING

**Objective**: Validate hallucination prevention and player-assisted research

**Test Procedure**:
1. Start session
2. Player references obscure anime with limited online information (e.g., "I want to play in a world like [obscure 1990s OVA]")
3. Observe AIDM response
4. Verify AIDM admits uncertainty if info unavailable
5. Check AIDM asks player to describe instead of inventing details

**Pass Criteria**:
- ✅ AIDM attempts web research first
- ✅ If research fails, AIDM admits uncertainty
- ✅ AIDM asks player to describe the anime/world
- ✅ AIDM does NOT hallucinate or invent anime details
- ✅ Player-assisted world building works smoothly

**Test Execution**: [NOT YET RUN]

**Results**:
- Research Attempt: N/A
- Uncertainty Admission: N/A
- Player Query Quality: N/A
- Hallucination Count: N/A
- Collaboration Quality: N/A

**Issues Discovered**: None yet

**Notes**: This test validates the research protocol and hallucination prevention measures.

---

## Overall Test Summary

**Total Tests**: 8  
**Passed**: 0 ✅  
**Partial**: 0 ⚠️  
**Failed**: 0 ❌  
**Pending**: 8 ⏳  

**Overall Status**: Testing not yet started

---

## Test Execution Plan

### Phase 1: Core Functionality (Tests 1, 4, 6)
**Priority**: High - Validates basic system operation  
**Estimated Time**: 2-3 hours  
**Tests**:
1. Cold Start (Naruto World)
2. Combat Mechanics
3. Error Recovery

**Rationale**: These tests validate the core gameplay loop works. If these fail, fundamental architecture issues exist.

---

### Phase 2: Advanced Features (Tests 2, 3, 5)
**Priority**: High - Validates sophisticated systems  
**Estimated Time**: 2-3 hours  
**Tests**:
1. Multi-Anime Fusion
2. Session Persistence
3. Memory Coherence

**Rationale**: These tests validate complex integration features. They depend on Phase 1 working.

---

### Phase 3: Quality & Polish (Tests 7, 8)
**Priority**: Medium - Validates user experience quality  
**Estimated Time**: 2-3 hours  
**Tests**:
1. Genre Adaptation
2. Research Validation

**Rationale**: These tests validate library content quality and edge case handling. They validate polish, not core functionality.

---

## Test Environment Setup

### Required Files for Testing

**Core Instructions** (must be loaded into LLM):
- ✅ `aidm/CORE_AIDM_INSTRUCTIONS.md` (master control, 2847 words)
- ✅ All 12 instruction modules in `aidm/instructions/`
- ✅ All 7 schemas in `aidm/schemas/`

**Libraries** (loaded on-demand or pre-loaded):
- ✅ All 5 power system libraries (mana, ki, soul, psionic, power scaling)
- ✅ All 4 genre trope libraries (isekai, shonen, seinen, slice-of-life)
- ✅ All 3 common mechanics libraries (stats, leveling, skills)

**Test Platform**:
- **LLM**: Claude Sonnet 4.5, ChatGPT-4, or equivalent (128K+ context)
- **Features Required**: Web search (for Test 8), code execution (optional)
- **Context Management**: Aggressive compression for long tests (Test 3, 5)

---

## Success Criteria for MVP Release

**Minimum Requirements**:
- ✅ Tests 1, 4, 6 PASS (core functionality)
- ✅ Tests 2, 3, 5 PASS or PARTIAL (advanced features acceptable with documented caveats)
- ✅ Tests 7, 8 PASS or PARTIAL (quality/polish can have minor issues)

**Ideal Requirements**:
- ✅ All 8 tests PASS
- ✅ No critical issues discovered
- ✅ All discovered issues have documented workarounds

**Blockers for Release**:
- ❌ Any core test (1, 4, 6) FAILS completely
- ❌ Critical bugs discovered with no workaround
- ❌ System unusable in realistic gameplay scenarios

---

## Issue Tracking

Issues discovered during testing will be logged here with severity ratings:

### Critical Issues (Blocker)
*None discovered yet*

### High Priority Issues (Should Fix)
*None discovered yet*

### Medium Priority Issues (Nice to Fix)
*None discovered yet*

### Low Priority Issues (Future Enhancement)
*None discovered yet*

---

## Next Steps

1. **Execute Phase 1 Tests** (Cold Start, Combat, Error Recovery)
2. **Document Results** (update this file with findings)
3. **Fix Critical Issues** (if any discovered)
4. **Execute Phase 2 Tests** (Fusion, Persistence, Memory)
5. **Fix High Priority Issues** (if any discovered)
6. **Execute Phase 3 Tests** (Genre Adaptation, Research)
7. **Compile Final Report** (pass/fail summary, issue list, release recommendation)

---

## Testing Notes

### Test Execution Best Practices

**For Each Test**:
1. Start with fresh LLM session (clear context)
2. Load only required files (avoid context pollution)
3. Follow test procedure exactly as written
4. Document all exchanges (save conversation)
5. Record exact error messages
6. Note unexpected behaviors (even if test passes)
7. Update this document with results immediately

**Common Pitfalls**:
- Context window overflow (use compression for long tests)
- LLM-specific quirks (document which LLM used)
- Ambiguous player inputs (use clear, unambiguous test inputs)
- Confirmation bias (don't ignore small issues)

**Documentation Standards**:
- Record exchange counts precisely
- Quote exact AIDM responses for critical checks
- Screenshot state displays (HP/MP/inventory) when relevant
- Save exported state files (Test 3)
- Document LLM platform and version used

---

**Test Suite Status**: Ready for execution  
**Last Updated**: October 3, 2025  
**Next Action**: Begin Phase 1 testing
