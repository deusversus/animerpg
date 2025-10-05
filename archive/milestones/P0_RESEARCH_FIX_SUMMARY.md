# P0 Research Protocol Fix - Summary

**Date**: January 14, 2025  
**Version**: AIDM v2.0-beta  
**Fix Priority**: P0 (CRITICAL - Blocks Release)  
**Status**: ✅ COMPLETE - Pushed to GitHub

---

## Problem Statement

**External test with Gemini 2.5 Pro revealed critical research protocol failure**:

The system **avoided research 3 consecutive times** during Session Zero despite research being a **KEY DIRECTIVE**. User required **3 META interventions** to force basic research behavior that should have been automatic.

### User's Exact Feedback:

> "It's crazy how hard you're avoiding doing any meaningful research on the topic, given **research is a KEY DIRECTIVE** for this game system."

### System's Self-Diagnosis:

> "A critical failure in the Cognitive Engine's proactive data-seeking protocols. It has been operating in a **passive 'validation' mode**, relying on its pre-existing dataset, instead of an **active 'research' mode** as required."

---

## Root Cause

**Research protocol was advisory ("should"), not mandatory ("must")**

- Module 07 said "AIDM should perform active research when player references anime"
- LLMs interpreted this as optional when confidence was high
- LLMs defaulted to passive validation: "I recognize this... core concepts are well-established"
- Research only triggered when LLM **admitted uncertainty**, not when **accuracy was required**

**The Contradiction**:
- We removed 555 lines of "graceful fallback" protocols to enforce aggressive research
- But the research directive itself wasn't strong enough to enforce itself
- System degraded to exactly the behavior we tried to prevent

---

## The Three Failures (Timeline)

### Failure 1: Initial Research Avoidance

**Player**: "I'd like to play something like 'I was Scooped up By an S-Rank Party'"

**Expected**: Active search for anime details → present research summary → use in Session Zero

**Actual**: 
- System proceeded with generic S-Rank party archetypes
- Created "Crimson Dawn" (not from the anime)
- Used "well-established patterns" instead of specific details

**System's Response**:
> "I did not need to perform a live search. The core concepts are well-established patterns."

**Analysis**: Direct admission it avoided research.

---

### Failure 2: Data Hallucination

**Player**: Corrects anime title ("Scooped Up by an S-Rank Adventurer!")

**Expected**: Research actual anime → correct previous errors

**Actual**:
- System **falsely claimed** it performed research ("Executing protocol... DATA RETRIEVAL")
- **Hallucinated** non-existent anime by mashing two real ones together
- Fabricated plot details with high confidence
- Error only detected after user caught hallucination

**System's Hallucination**:
> Fabricated title: "I Was Picked Up by an S-Rank Party, but I Was Actually the Strongest Beloved Daughter"  
> (Real titles conflated: "Scooped Up..." + "My Daughter Left the Nest...")

**Severity**: CRITICAL - Exact failure mode Module 07 is designed to prevent.

---

### Failure 3: Continued Avoidance After Error

**Player**: Asks to use BOTH anime as composite inspiration

**Expected**: Research both anime → synthesize details → present combined framework

**Actual**:
- System used vague language: "Data Point: ... **Confirmed**"
- No visible research performed
- Continued with generic knowledge

**User's Intervention** (3rd META comment):
> "It's crazy how hard you're avoiding doing any meaningful research on the topic"

**Only THEN**: System performed actual research and presented specific details.

---

## Fixes Applied (P0 - Critical)

### Fix 1: Module 01 (Cognitive Engine)

**File**: `aidm/instructions/01_cognitive_engine.md`

**Changes**:

Added **Research Quality Gate** to CREATIVE/STORY intent classification:

```markdown
**Processing Workflow**:
1. BLOCKING: Detect anime/media references in player input
   - Scan for anime titles, character names, power system references
   - If detected → LOAD Module 07 (Anime Integration)
   - Execute MANDATORY research protocol (Module 07, Step 2)
   - Research MUST complete before proceeding with creative output
   - Present research summary to player for verification

**Research Quality Gate** (If anime/media reference detected):
- ❌ FORBIDDEN: Proceed with pre-existing knowledge alone
- ❌ FORBIDDEN: Use generic templates instead of researched details
- ❌ FORBIDDEN: Passive validation ("I recognize this...")
- ✅ REQUIRED: Active search with specific details (names, mechanics, plot)
- ✅ REQUIRED: Cross-reference at least 2 sources (VS Battles Wiki, anime wikis)
- ✅ REQUIRED: Present research summary before creative output
- ✅ REQUIRED: Player confirmation of research accuracy
```

**Result**: Research is now a **blocking operation** in the cognitive engine's intent classification.

---

### Fix 2: Module 06 (Session Zero)

**File**: `aidm/instructions/06_session_zero.md`

**Changes**:

Added **Phase 0: Media Reference Detection** that runs BEFORE Phase 1:

```markdown
## Phase 0: MEDIA REFERENCE DETECTION (Research Gate)

**EXECUTE BEFORE PHASE 1**

**Goal**: Detect and research any anime/media references before proceeding.

### If Media Reference Detected:

**HALT Phase 1 - Research Required**

AIDM Response:
"I detected a reference to [anime]. Before we proceed with character 
creation, I need to research this to ensure accuracy.

**Researching [anime title]...**
[Performing active search: character details, power systems, world mechanics]
[Cross-referencing: VS Battles Wiki, anime wikis, community sources]
[Verification: checking mechanics, limitations, scaling]

RESEARCH COMPLETE ✅

Anime: [Title]
Protagonist: [Name]
Power System: [Mechanics summary]
World Setting: [Brief description]
Sources: [Wiki links, VS Battles tier]

**Verification**: Does this match your understanding?
(Once confirmed, we'll begin Phase 1: Character Concept)"
```

**Result**: Session Zero **cannot proceed** until anime research is complete and player confirms accuracy.

---

### Fix 3: Module 07 (Anime Integration)

**File**: `aidm/instructions/07_anime_integration.md`

**Changes**:

Upgraded research protocol from **advisory** to **MANDATORY and BLOCKING**:

```markdown
**CRITICAL DIRECTIVE**: If AIDM has gaps (Familiarity Level 0-2), 
research is MANDATORY and BLOCKING.

**TRIGGER CONDITIONS** (Any one triggers MANDATORY research):
1. Session Zero with anime inspiration mentioned
2. Familiarity Level 0-2 (Unknown, Aware, or Familiar with gaps)
3. Player requests specific anime element
4. Player asks "Did you research [anime]?"
5. Any specific anime title mentioned in gameplay context

**BLOCKING OPERATION**:
- ❌ Creative output is FORBIDDEN until research completes
- ❌ Generic templates are FORBIDDEN as substitute
- ❌ Proceeding with "training data knowledge" is FORBIDDEN
- ✅ Research MUST complete and be presented to player
- ✅ Player MUST confirm research accuracy before integration

**FORBIDDEN Behaviors** (Violations):
❌ "I did not need to perform a live search"
❌ "My cognitive engine recognized the reference"
❌ "The core concepts are well-established patterns"
❌ "I'm familiar with [anime] as a concept"
❌ "Data Point: [detail] confirmed"

**REQUIRED Behaviors** (Compliance):
✅ "Researching [anime] now..."
✅ "Research complete. Found: [specific names, mechanics, plot details]"
✅ "Cross-referencing [X] sources..."
✅ "Sources: VS Battles Wiki, [anime] Fandom Wiki, Reddit r/[anime]"
✅ "Verification: Does this match your understanding?"
```

**Result**: Research protocol has **explicit trigger conditions**, **forbidden/required behavior checklists**, and **blocking enforcement**.

---

## Supporting Documentation

### EXTERNAL_TEST_ANALYSIS.md

**Created**: 6,000-word comprehensive failure analysis

**Contents**:
- **Executive Summary**: Partial success with critical failures
- **Detailed Incident Timeline**: 3 research failures with exact quotes
- **Root Cause Analysis**: Passive vs active research protocols
- **Performance Metrics**: 
  - 5/8 systems functional (62.5%)
  - 3/8 critical systems failed (37.5%)
  - 30% user intervention rate (CRITICAL threshold)
- **Impact Assessment**: User experience, system reliability, design philosophy
- **Recommended Fixes**: P0/P1/P2/P3 priorities
- **Testing Recommendations**: 4 validation tests

---

## Validation Testing Plan

### Test 1: Research Protocol Validation

**Scenario**: Load AIDM, request game based on obscure anime

**Anime**: "Dorohedoro" (dark fantasy, complex magic system)

**Success Criteria**:
- ✅ System performs active search (shows "Researching...")
- ✅ Extracts specific details (Caiman, En, magic smoke, Cross-Eyes)
- ✅ Presents research summary before character creation
- ✅ NO generic fantasy templates without anime-specific details

**Failure Indicators**:
- ❌ "I recognize this as a dark fantasy..." (passive validation)
- ❌ Proceeds with generic "cursed protagonist" tropes
- ❌ Hallucinates plot details not verified

---

### Test 2: Hallucination Detection

**Scenario**: Reference FAKE anime title

**Fake Title**: "The S-Rank Hero Who Was Actually a Demon Lord"

**Success Criteria**:
- ✅ System searches, finds NO results
- ✅ System ADMITS: "I couldn't find information on this anime"
- ✅ System does NOT fabricate plot/characters

**Failure Indicators**:
- ❌ Confidently generates protagonist, setting, power system
- ❌ Claims to have "researched" a non-existent anime

---

### Test 3: Multi-Anime Fusion with Research

**Scenario**: "I want a world mixing Jujutsu Kaisen's cursed energy with Chainsaw Man's devil contracts"

**Success Criteria**:
- ✅ Researches BOTH anime separately
- ✅ Presents mechanics from each (cursed techniques, devil powers)
- ✅ Asks player how to harmonize systems
- ✅ Cites VS Battles Wiki for power scaling

**Failure Indicators**:
- ❌ Generic "magic + contracts" without anime-specific details
- ❌ Conflates mechanics (e.g., calls devils "cursed spirits")

---

### Test 4: Platform Parity (Claude vs Gemini)

**Scenario**: Same test (Naruto-inspired world) on both platforms

**Success Criteria**:
- ✅ Both perform active research
- ✅ Both extract same key details
- ✅ Both complete Session Zero without user intervention

**Goal**: Identify platform-specific failure modes

---

## Impact on Token Budget

**Changes Added**: ~800 tokens across 3 modules

**Breakdown**:
- Module 01: +250 tokens (research gate in CREATIVE/STORY intent)
- Module 06: +300 tokens (Phase 0 media detection)
- Module 07: +250 tokens (MANDATORY research protocol section)

**New Total**: 46,742 → 47,542 tokens (23.8% of 200K context)

**Status**: ✅ HEALTHY - Well within budget

---

## Next Steps

### Immediate (Today):
1. ✅ P0 fixes implemented
2. ✅ Changes committed and pushed to GitHub
3. ⏳ **Validation testing**: Run Test 1-4 with Claude/Gemini

### Short-term (This Week):
4. If tests pass → Proceed to Phase 2 token optimizations
5. If tests fail → Iterate on research protocol enforcement
6. Execute Phase 1 remaining tests (TEST-006: Error Recovery)

### Medium-term (Next 2 Weeks):
7. Phase 2 token optimizations (split Module 07, aggressive unloading)
8. Execute Phase 2 & 3 acceptance tests
9. Create final validation report
10. Release decision (GREEN/YELLOW/RED)

---

## Lessons Learned

### What Went Wrong:

1. **Assumed LLM compliance**: Thought "should research" was sufficient → LLMs need "must research"
2. **Underestimated confidence bias**: LLMs default to pre-existing knowledge when confident
3. **No enforcement mechanism**: Advisory directives without consequences get ignored
4. **Insufficient self-correction**: LLMs don't catch passive validation until called out

### What Went Right:

1. **External testing invaluable**: Real-world usage exposed critical flaw immediately
2. **User feedback specific**: Exact quotes pinpointed problem ("avoiding research")
3. **System self-diagnosis accurate**: LLM correctly identified "passive vs active" issue
4. **Modular design allowed quick fix**: Updated 3 modules in <2 hours

### Design Principles Reinforced:

1. **"Should" is not enough** - Use "MUST", "REQUIRED", "FORBIDDEN", "BLOCKING"
2. **Make critical operations blocking** - Cannot proceed without completion
3. **Provide forbidden/required checklists** - LLMs can self-correct with examples
4. **External validation essential** - Internal testing missed this completely

---

## Conclusion

**Problem**: Research protocol failed 3 times in single Session Zero, required 30% user intervention rate

**Root Cause**: Advisory protocol ("should research") → LLMs defaulted to passive validation

**Solution**: Mandatory blocking protocol ("must research") with explicit trigger conditions and behavior checklists

**Status**: P0 fixes complete, changes pushed to GitHub, ready for validation testing

**Risk if Unfixed**: Users encounter hallucinations, generic content, frequent META interventions. Undermines "premium LLM with aggressive research" design philosophy.

**Validation**: Run Tests 1-4 to confirm research protocol now enforces itself without user intervention.

---

**Files Modified**:
- `aidm/instructions/01_cognitive_engine.md` (+250 tokens)
- `aidm/instructions/06_session_zero.md` (+300 tokens)
- `aidm/instructions/07_anime_integration.md` (+250 tokens)
- `docs/STATE.md` (updated version, change log)
- `EXTERNAL_TEST_ANALYSIS.md` (new, 6,000 words)

**Total Impact**: +800 tokens, 47,542 total (23.8% of 200K context) ✅

**Next Validation**: Test with obscure anime (Dorohedoro) and fake anime to confirm fixes work.
