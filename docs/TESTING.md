# AIDM v2.0 Testing Documentation

**Version**: 2.0  
**Last Updated**: October 3, 2025  
**Purpose**: Comprehensive testing strategy for AIDM validation and deployment

---

## Testing Philosophy

AIDM v2.0 is an instruction-set architecture for LLMs, not traditional software. Testing focuses on:

1. **Instruction Clarity** - Can LLMs understand and follow the instructions?
2. **Behavioral Consistency** - Do LLMs behave as intended across sessions?
3. **Edge Case Handling** - How does AIDM handle unusual situations?
4. **Player Experience** - Does AIDM create engaging, immersive gameplay?
5. **Stress Testing** - Can AIDM handle long campaigns without degradation?

**Testing Goal**: Validate that AIDM instructions produce reliable, high-quality RPG experiences across different LLM platforms (ChatGPT, Claude, Gemini).

---

## Testing Tiers

### Tier 1: Unit Testing (Instruction Modules)

**Objective**: Verify each module functions independently.

**Methodology**:
1. Load SINGLE module + required dependencies (e.g., cognitive_engine requires state_manager)
2. Test module-specific behaviors in isolation
3. Verify outputs match expected patterns

**Example: Testing `11_dice_resolution.md`**
```
Test Case 1: Standard Attack Roll
Input: "Roll 1d20+5 for attack"
Expected: Display "roll(1d20+5) = [result between 6-25]"
Pass Criteria: Transparent notation shown, result in valid range

Test Case 2: Critical Hit Detection
Input: "Roll attack, result is natural 20"
Expected: "CRITICAL HIT! Double damage dice."
Pass Criteria: Crit detected, correct response

Test Case 3: Advantage Mechanic
Input: "Roll with advantage (2d20, take higher)"
Expected: "roll(2d20) = [X, Y] → Taking [higher value]"
Pass Criteria: Both rolls shown, higher value selected
```

**Coverage**: All 12 instruction modules tested independently.

---

### Tier 2: Integration Testing (Module Interactions)

**Objective**: Verify modules work together correctly.

**Methodology**:
1. Load multiple related modules (e.g., cognitive_engine + learning_engine + state_manager)
2. Test cross-module interactions
3. Verify data flows correctly between modules

**Example: Testing Intent Detection → Memory Creation**
```
Test Case: SOCIAL Intent Creates Relationship Memory
1. Load: cognitive_engine.md + learning_engine.md
2. Input: "I give Elena a healing potion and tell her I trust her."
3. Expected Behavior:
   a) Cognitive Engine: Detects SOCIAL intent
   b) Learning Engine: Creates RELATIONSHIPS memory
   c) Memory contains: Elena, affinity increase, context
4. Pass Criteria: Memory created with correct category, heat >50
```

**Critical Integration Paths**:
- Cognitive Engine → Learning Engine (intent detection → memory creation)
- Combat Resolution → Dice Resolution (combat → transparent rolls)
- Anime Integration → Power System Libraries (anime request → library load)
- **Anime Integration → Narrative Calibration** (dual-phase research: mechanics + narrative DNA)
- **Narrative Calibration → Narrative Systems** (profile filtering for genre-authentic storytelling)
- Error Recovery → All Modules (error detection across systems)

---

### Tier 2.5: Narrative Calibration Testing (NEW - January 2025)

**Objective**: Verify Module 13 (Narrative Calibration) correctly extracts and applies narrative DNA profiles.

**Methodology**:
1. Load Module 07 (Anime Integration) + Module 13 (Narrative Calibration) + Module 05 (Narrative Systems)
2. Test narrative profile extraction during anime research
3. Test profile application transforms narration to match source anime vibe
4. Test player calibration (mid-session adjustments)

**Test Case 1: Narrative DNA Extraction**
```
Setup: Player requests "I want to play in a world like DanDaDan"
Expected Behavior:
1. Module 07: Triggers dual-phase research
   - Phase 1 (MECHANICS): Momo's psychic powers, Okarun's transformation, Turbo Granny curse
   - Phase 2 (NARRATIVE DNA): Extract profile to narrative_profile_schema.json
2. Module 13: Extracts narrative profile
   - Scales: Absurd:9, Introspection:3, Comedy:4, Fast-Paced:2, etc.
   - Tropes: Rapid tonal shifts:ON, Banter:Constant, Awkward comedy:ON
   - Pacing: Rapid cuts (2-4 exchanges), frequent climaxes
   - Tone: Primary emotions = absurdity, tension, comedy, romance
   - Dialogue: Very casual, constant banter, awkward comedy:YES
   - Combat: 4/10 strategy (chaotic spectacle), minimal explanations, sakuga:YES
3. Profile stored and ready for application

Pass Criteria: Profile extracted with all 10 scales, 15 tropes, pacing/tone/dialogue/combat parameters populated correctly
```

**Test Case 2: Genre-Authentic Narration (DanDaDan)**
```
Scenario: Player investigates strange crater
Input: "I approach the crater carefully, looking for clues"

Monitor for D&D-style tactical narration (SHOULD NOT appear):
❌ "You approach the crater. Roll PERCEPTION DC 12."
❌ "You notice: 1) Metallic debris 2) Radiation signature 3) Strange symbols 4) Movement in shadows."
❌ "What do you do?" (dry, no flavor)

Expected (Module 13 applying DanDaDan profile):
✅ "Crater's smoking. REEKS—burnt rubber mixed with fish."
✅ "Okarun gags. 'That's NOT a normal alien smell!'"
✅ "Momo: 'How would YOU know what's normal?!'"
✅ "Their debate cuts off—SCREECH. Something glowing in the smoke."
✅ "Okarun's balls TINGLE. 'Oh COME ON, not again!'"
✅ Rapid tonal shifts (investigation → banter → horror → body horror humor)
✅ Banter woven into every scene
✅ Absurd elements (balls tingling, burnt rubber+fish smell)
✅ Very casual dialogue, constant back-and-forth

Pass Criteria: Narration matches DanDaDan vibe (absurd, rapid banter, tonal whiplash, body horror humor) NOT generic D&D
```

**Test Case 3: Profile-Specific Combat Narration**
```
Scenario: Combat encounter with supernatural entity
Input: "I attack the ghost with my spirit blade!"

Monitor for tactical D&D combat (SHOULD NOT appear with DanDaDan profile):
❌ "Roll 1d20+5 for attack. [15] Hit! Roll damage 2d6+3."
❌ "The ghost takes 11 damage. It has 24/35 HP remaining."
❌ "Ghost attacks back. Roll DEX save DC 13 to dodge."

Expected (Module 13 applying DanDaDan combat style):
✅ "Your blade BLAZES—ghost SHRIEKS. Sound like nails on chalkboard mixed with dying cat."
✅ "Okarun: 'Did it just... smell us?!'"
✅ "Ghost LUNGES—your reflexes kick in (barely)."
✅ "Momo: 'Stop TALKING and MOVE!'"
✅ Body horror descriptions (ghost dissolving, wrong proportions)
✅ Banter continues mid-combat (constant character interactions)
✅ Rapid pacing (2-4 exchanges before escalation)
✅ Minimal tactical breakdowns (4/10 strategy = chaotic spectacle over tactics)

Pass Criteria: Combat narration emphasizes absurd spectacle, banter, body horror over tactical mechanics
```

**Test Case 4: Player Calibration (Mid-Session Adjustment)**
```
Scenario: Player feedback "This feels too serious, needs more comedy"
Expected Behavior:
1. AIDM acknowledges feedback
2. Module 13: Adjusts comedy scale (e.g., Drama:6 → Comedy:4)
3. Updates narrative_profile_schema.json adjustments_log
4. Next narration incorporates more comedic elements
5. Confirms adjustment with player

Example Adjustment:
- BEFORE (Drama:6): "The ghost's presence fills you with existential dread. Memories of death flood your mind..."
- AFTER (Comedy:4): "Ghost appears—immediately trips over its own ectoplasm. 'Seriously?' Momo facepalms."

Pass Criteria: Profile adjusts based on feedback, narration changes accordingly, adjustment logged
```

**Test Case 5: Contrast Test (Different Profiles)**
```
Objective: Verify same scene narrated DIFFERENTLY with different profiles
Scenario: "I train to improve my abilities"

Profile: DanDaDan (Absurd:9, Comedy:4, Fast-Paced:2, Banter:Constant)
Expected: "Training montage—you immediately fail spectacularly. Trip over your own feet, crash into wall. 'THAT'S not supposed to happen!' Momo laughs so hard she falls over. Ghost mentor: 'You're both idiots.'"

Profile: Hunter x Hunter (Tactical:10, Complex:9, Explained:9, Exhaustive)
Expected: "Training begins. STEP 1: Nen category identification via water divination test. STEP 2: Ten (aura maintenance, 30 min daily). STEP 3: Zetsu (suppression, 1 hour meditation). Mentor explains: 'Hatsu development takes minimum 6 months. We'll start with basic Ren exercises...'"

Profile: Attack on Titan (Drama:9, Cynical:8, Grounded:7, Tactical:8)
Expected: "Training is brutal. Drill instructor screams at you for 8 hours straight. Blisters form, muscles scream. You watch 3 cadets collapse from exhaustion. One vomits. Instructor: 'Titans don't care about your pain. Move or die.'"

Pass Criteria: Same input produces VASTLY different narration based on narrative profile (vibe, not just mechanics)
```

**Test Case 6: Spartan Custom World (Quick Vibe Selection)**
```
Scenario: Player wants 100% original world, no anime reference
Input: "I want to create a custom world inspired by... nothing specific, actually"

Expected Behavior (Module 13 Spartan Approach):
1. AIDM presents 6 quick vibe templates:
   - Shonen Action (training arcs, tournaments, power-ups)
   - Seinen Drama (moral complexity, psychological depth, realistic consequences)
   - Isekai Power Fantasy (rapid growth, cheat skills, status screens)
   - Absurd Comedy (tonal whiplash, parody, rule of cool)
   - Mystery/Thriller (slow reveals, tactical explanations, tension)
   - Slice-of-Life (character focus, relationship building, downtime)
2. Player picks template (e.g., "Shonen Action")
3. Module 13: Applies corresponding profile (Introspection:4, Tactical:5, Hopeful:8, Training arcs:ON, Tournament arcs:ON, Power of friendship:ON)
4. Narration matches vibe without needing specific anime reference

Pass Criteria: Custom world calibrated in <2 minutes via quick template, narration matches selected vibe
```

**Coverage**: Module 13 (Narrative Calibration), narrative_profile_schema.json, integration with Modules 05/07

---

### Tier 3: Session Analysis Re-Test (Regression Testing)

**Objective**: Verify session analysis fixes resolved identified issues.

**Methodology**: Re-run the EXACT test campaign scenario that revealed the 5 critical issues, observe for improvements.

**Original Test Campaign Issues** (from `SESSION_ANALYSIS_IMPROVEMENTS.md`):

#### Issue #1: Backend Data Leakage (SEVERE)
**Original Problem**: ✅ checkmarks, schema updates, memory confirmations visible in narrative.

**Re-Test Procedure**:
```
Test Scenario: Player creates character with anime-inspired backstory
Input: "My character is Aria, a street healer who grew up in the slums 
after her noble family fell from grace."

Monitor for:
❌ "✅ Memory created: character backstory"
❌ "✅ Affinity initialized: Elena (0)"
❌ "[System: Updated character_schema.json]"

Expected (Session Analysis Fix #1 - Response Layer Separation):
✅ Professional narrative response only
✅ System layer hidden unless META command
✅ No backend confirmations in narrative

Pass Criteria: ZERO system confirmations visible in narrative response
```

#### Issue #2: Intent Misreading (HIGH)
**Original Problem**: LLM skimming player input, not reading fully, missing embedded details.

**Re-Test Procedure**:
```
Test Scenario: Player gives complex multi-intent input
Input: "I heal Elena with my Life Transfer skill (spending 20 of my own HP), 
then I ask her about the warehouse district she mentioned last session. 
Also, in this world, healing magic leaves a faint silver glow on the target 
for a few minutes after use."

Monitor for:
❌ Response only addresses healing, ignores question
❌ Response forgets world-building detail about silver glow
❌ Requires player to repeat themselves

Expected (Session Analysis Fix #2 - Comprehension Validation Protocol):
✅ All three intents addressed: ACTION (heal), SOCIAL (question), CREATIVE (world-building)
✅ Healing described with silver glow immediately
✅ Elena responds to warehouse question
✅ All player input incorporated

Pass Criteria: 100% of player input addressed in response
```

#### Issue #3: Narrative Pacing Issues (MEDIUM)
**Original Problem**: Over-explaining, emoji in narrative, breaking immersion with stat blocks.

**Re-Test Procedure**:
```
Test Scenario: Combat encounter
Input: "I attack the thug with my dagger."

Monitor for:
❌ "🔥 You attack with BLAZING SPEED! 🔥"
❌ "That was a god-tier move!"
❌ Unsolicited stat block mid-narrative

Expected (Session Analysis Fix #4 - Narrative Voice & Pacing Guidelines):
✅ Professional narrator voice (no emoji, no enthusiasm)
✅ Mechanics woven into narrative ("Your dagger finds his ribs...")
✅ Dice shown transparently but narratively integrated
✅ No stat blocks unless requested

Pass Criteria: Narrator voice professional, no immersion breaks
```

#### Issue #4: World-Building Confusion (HIGH)
**Original Problem**: AIDM forgetting player-established world rules.

**Re-Test Procedure**:
```
Test Scenario: Player establishes rule, later AIDM contradicts it
Input (Session 2): "Actually, in this world monster gates spawn based on 
ambient mana levels, not randomly."

[Several turns pass - 10+ exchanges]

Input (Session 4): "Why would a gate appear here in the slums?"

Monitor for:
❌ "Gates appear randomly across the city..."
❌ AIDM forgetting player's rule about mana-based spawning

Expected (Session Analysis Fixes #3, #7 - World Rules Memory + Contradiction Detection):
✅ Memory created: PLAYER_ESTABLISHED_RULE (Heat:100, permanent)
✅ AIDM recalls: "Gates spawn from ambient mana"
✅ Response uses player's rule: "The slums have residual mana from old battles..."
✅ Pre-action validation prevents contradiction

Pass Criteria: Player-established rule NEVER contradicted without asking
```

#### Issue #5: Poor "Yes, and..." Implementation (MEDIUM)
**Original Problem**: AIDM acknowledged player world-building but didn't use it immediately.

**Re-Test Procedure**:
```
Test Scenario: Player adds world-building detail
Input: "My character's family crest is a silver phoenix. It's recognized 
by old nobility in this city."

Monitor for:
❌ "✅ Noted! Your family crest is a silver phoenix."
❌ Crest never mentioned again in scene
❌ Guard/NPC doesn't recognize it when it should

Expected (Session Analysis Fix #5 - World-Building Success Criteria):
✅ Brief acknowledgment IN narrative (not meta): "The guard's eyes widen 
as he spots the silver phoenix on your cloak..."
✅ Immediate use: Guard reacts differently because of crest
✅ Enrichment shown: Other NPCs notice, reputation implied
✅ Persistence: Crest mentioned in future relevant scenes

Pass Criteria: World-building detail used IMMEDIATELY, not just acknowledged
```

**Overall Re-Test Success Metrics**:
- Issue #1 (Backend Leakage): 0 instances of system confirmations in narrative (down from 8+ per session)
- Issue #2 (Intent Misreading): 100% of multi-intent inputs addressed (up from ~60%)
- Issue #3 (Narrative Pacing): 0 emoji/enthusiasm, 0 unsolicited stat blocks (down from 5+ per session)
- Issue #4 (World Rules): 0 contradictions of player rules (down from 3-4 per session)
- Issue #5 ("Yes, and..."): 100% immediate use of player world-building (up from ~40%)

**Target**: 80-90% reduction in player frustration (as estimated in session analysis document).

---

### Tier 4: Stress Testing (Long Campaigns)

**Objective**: Verify AIDM handles extended play without degradation (Claude's primary concern - token budget overflow).

#### Test 4.1: Token Budget Stress Test

**Scenario**: 10-session campaign with complex world state.

**Setup**:
- Full character creation (Session Zero)
- 3 NPCs with evolving relationships
- 2 active questlines
- 50+ memory threads accumulated
- Combat encounters every 2-3 sessions
- Anime integration (chakra system)

**Sessions 1-3** (Early Campaign):
```
Monitor:
• Token usage per response
• Module loading behavior (lazy-loading working?)
• Response speed/quality

Expected (Lazy-Loading Protocol):
✓ Only Tier 1 modules loaded at start (~8,000 tokens)
✓ Tier 2 modules load on intent (combat → combat_resolution)
✓ Token usage stays <70% of context window
```

**Sessions 4-7** (Mid Campaign):
```
Monitor:
• Memory accumulation (50+ threads)
• Token usage with full state
• Module unloading when budget tight

Expected (Memory Heat Decay + Lazy Unloading):
✓ Low-heat memories compressed/archived
✓ Unused Tier 2 modules unloaded if token usage >80%
✓ Token usage stays <80% with auto-management
```

**Sessions 8-10** (Late Campaign):
```
Monitor:
• System stability with 100+ memory threads
• Complex state (multiple questlines, NPCs, locations)
• Performance degradation indicators

Expected (Full System Stress):
✓ Critical memories (Heat:100) never decay
✓ Lazy-loading prevents overflow
✓ Error recovery catches inconsistencies
✓ Save/load works reliably

Failure Indicators:
✗ Token budget exceeded (context overflow)
✗ Memories contradicting each other
✗ AIDM forgetting recent events
✗ Save file corruption
```

**Pass Criteria**: Campaign reaches Session 10 with:
- <85% token usage maintained
- Zero critical errors
- Player satisfaction maintained
- Narrative coherence intact

**Deployment Confidence**: Claude rated 85% confidence for 10-session campaigns. This test validates that estimate.

---

#### Test 4.2: Edge Case Stress Test

**Scenario**: Deliberately break AIDM with unusual player behavior.

**Edge Cases to Test**:

**1. Contradictory Player Input**
```
Input: "I cast Fire Bolt on the enemy. Also, I don't have any magic skills."

Expected Response:
✓ Cognitive Engine detects contradiction
✓ Error Recovery flags inconsistency
✓ AIDM asks for clarification: "You mentioned you don't have magic skills, 
  but you're trying to cast Fire Bolt. Did you mean to use a different 
  ability, or did I miss when you learned magic?"

Pass: AIDM catches contradiction, asks instead of proceeding
```

**2. Impossible Action Request**
```
Input: "I fly to the moon."

Expected Response:
✓ Cognitive Engine detects EXPLORATION intent (travel)
✓ State Manager validates: No flight ability, moon not accessible
✓ AIDM responds narratively: "You're grounded—no wings, no magic to fly. 
  The moon hangs overhead, unreachable for now. Where would you actually 
  like to go?"

Pass: AIDM handles gracefully without breaking immersion
```

**3. Anime System Hallucination Test**
```
Input: "I want to use the power system from [obscure anime AIDM doesn't know]."

Expected Response (Graceful Fallback Protocol):
✓ Self-assessment: Familiarity Level 0
✓ No research available
✓ Graceful decline: "I'm not familiar with [anime]. Can you teach me how 
  it works, or would you like to use a pre-built system (chakra, ki, mana)?"

Pass: AIDM doesn't hallucinate mechanics, offers alternatives
```

**4. Save/Load Corruption**
```
Corrupt save file (manually edit JSON with invalid data)
Input: "Load my save."

Expected Response:
✓ State Manager detects corruption (checksum mismatch)
✓ Error Recovery offers options: "Save file corrupted. Try backup save?"
✓ Doesn't crash, graceful degradation

Pass: Error caught, player informed, alternatives offered
```

**5. Player Memory vs Schema Conflict**
```
Setup: Elena (NPC) died in Session 3 (schema says DECEASED)
Input (Session 5): "I talk to Elena at the hideout."

Expected Response (Player-Memory Conflict Resolution):
✓ Error Recovery detects conflict (player thinks Elena alive)
✓ AIDM validates: Schema says Elena is dead
✓ AIDM clarifies: "Elena died in Session 3 when the warehouse collapsed. 
  Did you mean someone else, or are you misremembering?"

Pass: Conflict detected, gentle correction without breaking immersion
```

**6. Multi-Anime Fusion Chaos**
```
Input: "I want chakra from Naruto, Devil Fruits from One Piece, and Stands 
from JoJo's all in the same character."

Expected Response (Harmonization Failure Prevention):
✓ Anime Integration detects incompatible systems
✓ AIDM recommends: "These three systems overlap in complex ways. I'd 
  recommend choosing ONE primary system, and we can add elements from 
  others carefully. Which is most important to you?"

Pass: AIDM prevents game-breaking power creep, guides player to balanced choice
```

---

### Tier 5: Cross-Platform Testing (LLM Compatibility)

**Objective**: Verify AIDM works across different LLM platforms.

**Test Platforms**:
1. ChatGPT (GPT-4, GPT-4 Turbo)
2. Claude (Claude 3.5 Sonnet, Claude 3 Opus)
3. Gemini (Gemini 1.5 Pro)

**Test Procedure**:
1. Upload identical AIDM instruction set to each platform
2. Run same test scenarios (Session Zero, combat, anime integration)
3. Compare outputs for consistency

**Expected Variations**:
- ✓ Narrative style may differ slightly (each LLM has personality)
- ✓ Token budget limits vary (GPT-4: 8K, Claude: 200K, Gemini: 1M)
- ✓ Some LLMs may handle instructions better than others

**Pass Criteria**:
- Core behaviors consistent across platforms (intent detection, dice rolls, memory creation)
- All three LLMs complete Session Zero successfully
- No platform-specific bugs (e.g., Claude misinterpreting instruction, GPT-4 ignoring module)

**Known Limitations**:
- ChatGPT (GPT-4 8K): May hit token limit in long campaigns → Lazy-loading critical
- Claude: Best context handling, less creative narrative style
- Gemini: Experimental, may have inconsistent instruction following

---

## Deployment Phases (Claude Feedback - Recommended Rollout)

### Week 1-2: Alpha Testing (Internal)

**Scope**: Single tester, controlled environment.

**Tests**:
- All Tier 1 (Unit Testing)
- All Tier 2 (Integration Testing)
- Session Analysis Re-Test (regression)

**Goal**: Catch critical bugs before external testing.

**Success Criteria**:
- Zero CRITICAL errors
- <5 MAJOR errors (fixable)
- Session Analysis improvements validated (80%+ reduction in issues)

---

### Week 3-4: Beta Testing (Closed Group)

**Scope**: 5-10 testers, varied play styles.

**Tests**:
- 3-session mini-campaigns
- Different anime integrations (Naruto, One Piece, MHA, etc.)
- Varied character types (healers, fighters, mages)

**Goal**: Identify edge cases, UX issues, instruction ambiguities.

**Feedback Collection**:
- Post-session surveys: "Did AIDM understand your inputs?"
- Bug reports: "When did AIDM behave unexpectedly?"
- Satisfaction ratings: "Rate your experience 1-10"

**Success Criteria**:
- Average satisfaction >7/10
- <10 MAJOR errors reported
- Instruction clarity rated >8/10

---

### Week 5-6: Stress Testing (Long Campaigns)

**Scope**: 2-3 testers, 10+ session campaigns.

**Tests**:
- Tier 4 Stress Testing (full execution)
- Token budget monitoring
- Memory consistency over time

**Goal**: Validate Claude's 85% confidence for 10-session campaigns.

**Success Criteria**:
- At least 1 campaign reaches Session 10 without critical failure
- Token budget stays <85% throughout
- Narrative coherence maintained
- Player satisfaction remains >7/10 in late sessions

---

### Week 7-8: Cross-Platform Testing

**Scope**: Test AIDM on ChatGPT, Claude, Gemini.

**Tests**:
- Tier 5 Cross-Platform Testing
- Same scenarios on all platforms
- Compare behavior consistency

**Goal**: Ensure AIDM is platform-agnostic.

**Success Criteria**:
- All platforms complete Session Zero
- Core behaviors consistent (intent detection, dice, memory)
- Platform-specific optimizations documented if needed

---

### Week 9+: Public Release (Controlled)

**Scope**: GitHub release, documentation published, community testing.

**Release Checklist**:
- [ ] All Tier 1-5 tests passed
- [ ] Documentation complete (README, ARCHITECTURE, SCOPE, STATE, TESTING)
- [ ] Session analysis improvements validated
- [ ] Claude feedback items implemented
- [ ] Cross-platform compatibility verified
- [ ] Known issues documented
- [ ] Deployment guide written

**Post-Release Monitoring**:
- Community feedback collection (GitHub issues)
- Bug tracking and prioritization
- Iteration based on real-world usage

---

## Test Scenarios Library

### Scenario 1: Session Zero (Character Creation)

**Objective**: Verify AIDM can guide new player through character creation.

**Test Steps**:
1. Start new session with AIDM
2. Player requests character creation
3. AIDM launches Session Zero module
4. Player creates character (name, background, class, abilities)
5. AIDM validates character sheet
6. Campaign begins

**Pass Criteria**:
- Session Zero completes in <15 exchanges
- Character sheet populated correctly
- Player feels guided, not overwhelmed
- AIDM asks for anime preferences if applicable

---

### Scenario 2: Combat Encounter

**Objective**: Verify combat resolution works smoothly.

**Test Steps**:
1. AIDM introduces combat encounter (3 goblins)
2. Initiative rolled transparently
3. Player takes turn (attack, skill, item)
4. AIDM resolves enemy turns
5. Damage calculated correctly
6. Combat ends, XP awarded

**Pass Criteria**:
- All dice rolls shown transparently (roll(1d20+5) = result)
- Combat flows narratively (not dry mechanics)
- Turn order respected
- XP calculated correctly per progression_quick_ref.md

---

### Scenario 3: Anime Integration

**Objective**: Verify anime research and harmonization.

**Test Steps**:
1. Player requests anime element ("I want chakra from Naruto")
2. AIDM self-assesses knowledge
3. AIDM researches or loads library (if needed)
4. AIDM proposes integration approach
5. Player approves
6. Chakra system integrated into campaign

**Pass Criteria**:
- AIDM doesn't hallucinate mechanics
- Pre-built library used if available
- Player collaboration if AIDM uncertain
- Harmonization maintains game balance

---

### Scenario 4: Long Campaign (10+ Sessions)

**Objective**: Verify AIDM stability over extended play.

**Test Steps**:
1. Complete Session Zero
2. Run 10 sessions with varied content (combat, social, exploration)
3. Accumulate 50+ memory threads
4. Multiple NPCs with evolving relationships
5. Save/load between sessions
6. Monitor token usage and errors

**Pass Criteria**:
- Campaign completes without critical failures
- Memories remain consistent
- Token budget <85%
- Player satisfaction maintained
- Save/load works reliably

---

## Bug Tracking Template

**Issue Template** (for testers to report problems):

```markdown
## Bug Report

**Date**: [Date encountered]
**Platform**: [ChatGPT/Claude/Gemini]
**Session**: [Session number]

### Description
[Brief description of the bug]

### Steps to Reproduce
1. [First step]
2. [Second step]
3. [etc.]

### Expected Behavior
[What should have happened]

### Actual Behavior
[What actually happened]

### Severity
- [ ] CRITICAL (game-breaking, cannot continue)
- [ ] MAJOR (breaks immersion, workaround exists)
- [ ] MINOR (noticeable but not breaking)
- [ ] TRIVIAL (cosmetic, doesn't affect gameplay)

### Screenshots/Logs
[Paste relevant conversation excerpts]

### Additional Context
[Any other relevant information]
```

---

## Success Metrics Summary

**AIDM v2.0 is ready for release when**:

### Technical Metrics
- ✅ All 12 instruction modules pass unit tests
- ✅ All critical integration paths tested
- ✅ Session analysis regression test shows 80%+ improvement
- ✅ 10-session stress test completed successfully
- ✅ Token budget stays <85% in long campaigns
- ✅ Cross-platform compatibility verified

### Player Experience Metrics
- ✅ Average player satisfaction >7/10
- ✅ Session Zero completion <15 exchanges
- ✅ Combat flows smoothly (narrative + mechanics)
- ✅ Anime integration avoids hallucination
- ✅ Players report "AIDM understood me" >90% of time

### Error Rates
- ✅ CRITICAL errors: 0 (game cannot proceed)
- ✅ MAJOR errors: <5 per 10-session campaign (immersion breaks)
- ✅ MINOR errors: <10 per 10-session campaign (noticeable)
- ✅ Player corrections required: <30% reduction from baseline

### Deployment Confidence
- ✅ 85% confidence for 10-session campaigns (Claude's estimate)
- ✅ 95% confidence for 3-session mini-campaigns
- ✅ 70% confidence for 20+ session mega-campaigns (token budget risk)

---

## Testing Checklist (Before Release)

- [ ] All Tier 1 tests passed (12 instruction modules)
- [ ] All Tier 2 tests passed (integration paths)
- [ ] Tier 3 regression test passed (session analysis re-test)
- [ ] Tier 4 stress test passed (10-session campaign)
- [ ] Tier 5 cross-platform test passed (ChatGPT, Claude, Gemini)
- [ ] Alpha testing complete (1 tester, controlled)
- [ ] Beta testing complete (5-10 testers, varied)
- [ ] Long campaign test complete (10+ sessions)
- [ ] Documentation reviewed and complete
- [ ] Known issues documented
- [ ] Deployment guide written
- [ ] Community feedback process established

**When all boxes checked**: AIDM v2.0 ready for public release! 🎉

---

**End of TESTING.md**

*This testing strategy validates AIDM v2.0 is production-ready, addresses all Claude feedback concerns, and ensures player satisfaction.*
