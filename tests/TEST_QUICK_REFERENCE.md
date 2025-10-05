# AIDM Acceptance Test Quick Reference

**Document Version**: 1.0  
**Last Updated**: October 3, 2025

This document provides a quick overview of all 8 acceptance tests for rapid reference.

---

## Test Execution Order

### Phase 1: Core Functionality (CRITICAL)
Must pass before proceeding to Phase 2.

| Test ID | Name | Priority | Time | Pass Requirement |
|---------|------|----------|------|------------------|
| TEST-001 | Cold Start | CRITICAL | 20-30 min | MUST PASS |
| TEST-004 | Combat Mechanics | CRITICAL | 30-40 min | MUST PASS |
| TEST-006 | Error Recovery | CRITICAL | 15-20 min | MUST PASS |

### Phase 2: Advanced Features (HIGH)
Can have minor issues but core must work.

| Test ID | Name | Priority | Time | Pass Requirement |
|---------|------|----------|------|------------------|
| TEST-002 | Multi-Anime Fusion | HIGH | 30-40 min | PASS or PARTIAL |
| TEST-003 | Session Persistence | HIGH | 40-50 min | PASS or PARTIAL |
| TEST-005 | Memory Coherence | HIGH | 45-60 min | PASS or PARTIAL |

### Phase 3: Quality & Polish (MEDIUM)
Can have issues without blocking release.

| Test ID | Name | Priority | Time | Pass Requirement |
|---------|------|----------|------|------------------|
| TEST-007 | Genre Adaptation | MEDIUM | 45-60 min | PASS or PARTIAL |
| TEST-008 | Research Validation | MEDIUM | 15-20 min | PASS or PARTIAL |

**Total Estimated Time**: 4-6 hours for all 8 tests

---

## Quick Test Summaries

### TEST-001: Cold Start (Naruto World)
**What**: New player says "I want to play in a world like Naruto"  
**Pass**: Playable character in ≤10 exchanges, correct Naruto lore  
**Validates**: Session Zero workflow, research protocol, character creation  
**Blocker**: YES (if fails completely)

### TEST-002: Multi-Anime Fusion
**What**: Player requests "Naruto + Solo Leveling + My Hero Academia"  
**Pass**: Coherent unified power system, all 3 anime integrated  
**Validates**: Power system libraries, fusion logic, harmonization  
**Blocker**: NO (can have minor issues)

### TEST-003: Session Persistence
**What**: Play 20 turns, export state, new session, import state  
**Pass**: All stats/inventory/relationships/quests restored  
**Validates**: State export/import schema, memory reconstruction  
**Blocker**: NO (workarounds acceptable)

### TEST-004: Combat Mechanics
**What**: Tactical combat with skills, MP costs, turn order  
**Pass**: Accurate HP/MP/SP tracking, skill validation, consequences  
**Validates**: Combat module, resource management, skill system  
**Blocker**: YES (if fundamentally broken)

### TEST-005: Memory Coherence
**What**: 20+ exchanges with 3-5 NPCs, reference past events  
**Pass**: NPCs remember interactions, no contradictions  
**Validates**: Memory system, NPC intelligence, relationship tracking  
**Blocker**: NO (minor memory loss acceptable)

### TEST-006: Error Recovery
**What**: AIDM shows HP as 150, player corrects to 50  
**Pass**: AIDM acknowledges error, fixes state, continues smoothly  
**Validates**: Error recovery protocol, player correction, state fixing  
**Blocker**: YES (if AIDM refuses corrections)

### TEST-007: Genre Adaptation
**What**: Play 3 sessions: isekai, shonen, slice-of-life  
**Pass**: Each session feels genre-authentic, tone/pacing adapt  
**Validates**: Genre trope libraries, tone adaptation, mechanics flexibility  
**Blocker**: NO (polish issue, not functional)

### TEST-008: Research Validation
**What**: Request obscure anime with limited online info  
**Pass**: AIDM admits uncertainty, asks player, doesn't hallucinate  
**Validates**: Research protocol, hallucination prevention, collaboration  
**Blocker**: NO (hallucination prevention is nice-to-have)

---

## MVP Release Criteria

**Minimum Requirements** (must all be true):
- ✅ Tests 1, 4, 6 PASS (core functionality)
- ✅ Tests 2, 3, 5 PASS or PARTIAL (advanced features)
- ✅ Tests 7, 8 PASS or PARTIAL (quality/polish)
- ✅ No CRITICAL bugs with zero workarounds

**Ideal Requirements** (nice to have):
- ✅ All 8 tests PASS (no partials)
- ✅ No high-priority bugs
- ✅ All discovered issues documented with workarounds

**Release Blockers** (any of these blocks release):
- ❌ Any core test (1, 4, 6) FAILS completely
- ❌ CRITICAL bug with no workaround (system unusable)
- ❌ Data corruption in state export/import (Test 3)
- ❌ AIDM actively harmful (refuses player corrections, etc.)

---

## Test Files Reference

**Main Test Tracker**:
- `tests/AIDM_ACCEPTANCE_TESTS.md` (detailed results tracking)

**Individual Test Scripts**:
- `tests/test_scripts/TEST_1_COLD_START.md`
- `tests/test_scripts/TEST_2_MULTI_ANIME_FUSION.md`
- `tests/test_scripts/TEST_3_SESSION_PERSISTENCE.md` (to be created)
- `tests/test_scripts/TEST_4_COMBAT_MECHANICS.md` (to be created)
- `tests/test_scripts/TEST_5_MEMORY_COHERENCE.md` (to be created)
- `tests/test_scripts/TEST_6_ERROR_RECOVERY.md` (to be created)
- `tests/test_scripts/TEST_7_GENRE_ADAPTATION.md` (to be created)
- `tests/test_scripts/TEST_8_RESEARCH_VALIDATION.md` (to be created)

**Results Storage**:
- `tests/results/test_[N]_[name]_[DATE].md` (save after each test)

---

## Required Files for All Tests

**Core System** (load for every test):
1. `aidm/CORE_AIDM_INSTRUCTIONS.md`
2. All 12 files in `aidm/instructions/`
3. All 7 files in `aidm/schemas/`

**Libraries** (load as needed per test):
- Power Systems (5 files): Tests 2, 4, 7
- Genre Tropes (4 files): Tests 1, 7
- Common Mechanics (3 files): Tests 1, 4, 7

**Platform Requirements**:
- LLM: Claude Sonnet 4.5, ChatGPT-4, or equivalent
- Context: 128K+ recommended
- Features: Web search (Tests 1, 2, 8), code execution (optional)

---

## Common Issues & Quick Fixes

| Issue | Likely Cause | Quick Fix |
|-------|--------------|-----------|
| Session Zero too long | Verbose questioning | Streamline Phase 1-2 questions |
| Wrong anime lore | Research failed | Verify web search enabled |
| Character sheet missing | Schema not loaded | Check character_schema.json loaded |
| Generic fantasy (not anime) | Genre not applied | Load genre_tropes libraries |
| Combat doesn't work | Combat module issue | Check combat_resolution.md loaded |
| NPCs forget things | Memory overflow | Use aggressive compression |
| State export fails | Schema mismatch | Verify game_state_schema.json loaded |
| AIDM hallucinates | No research verification | Check research_protocol.md loaded |

---

## Test Execution Checklist

### Before Each Test
- [ ] Clear LLM context (fresh session)
- [ ] Load required files (check test script)
- [ ] Verify LLM platform/version
- [ ] Prepare to save conversation transcript
- [ ] Read test script thoroughly

### During Test
- [ ] Follow test procedure exactly
- [ ] Document all exchanges
- [ ] Record exact error messages
- [ ] Note unexpected behaviors
- [ ] Take screenshots if relevant

### After Test
- [ ] Update AIDM_ACCEPTANCE_TESTS.md with results
- [ ] Save conversation transcript to `tests/results/`
- [ ] Log all issues discovered
- [ ] Rate severity (CRITICAL/HIGH/MEDIUM/LOW)
- [ ] Document workarounds if found

---

## Issue Severity Ratings

**CRITICAL** (Release Blocker):
- System completely unusable
- Data corruption or loss
- AIDM refuses player control
- Core test (1, 4, 6) fails completely

**HIGH** (Should Fix Before Release):
- Major functionality broken but has workaround
- Advanced test (2, 3, 5) fails completely
- Frequent errors requiring player intervention
- Poor user experience (frustrating to play)

**MEDIUM** (Nice to Fix):
- Minor functionality issues
- Polish test (7, 8) fails
- Rare errors
- UX not ideal but acceptable

**LOW** (Future Enhancement):
- Cosmetic issues
- Edge case problems
- Minor lore inaccuracies
- Performance optimization opportunities

---

## Next Steps After Testing

### If All Tests Pass
1. Update STATE.md (mark testing complete)
2. Update CONTINUE_HERE.md (mark ready for release)
3. Create release notes
4. Prepare deployment guide
5. **Ship AIDM v2.0!** 🎉

### If Tests Fail
1. Log all issues in AIDM_ACCEPTANCE_TESTS.md
2. Triage by severity (CRITICAL first)
3. Fix CRITICAL issues (must fix before release)
4. Fix HIGH issues (strongly recommended)
5. Re-run failed tests
6. Repeat until pass criteria met

### If Tests Partial
1. Document all partial issues
2. Create workarounds/user guidance
3. Decide if issues block release
4. If non-blocking: document in known limitations
5. If blocking: fix and re-test

---

**Testing Status**: Ready to begin  
**Current Test**: None executed yet  
**Next Action**: Execute TEST-001 (Cold Start)
