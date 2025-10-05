# Test 5: Memory Coherence

**Test ID**: AIDM-TEST-005  
**Category**: Advanced Functionality  
**Priority**: HIGH  
**Estimated Time**: 45-60 minutes

---

## Test Objective

Validate that NPC memory and relationship systems maintain consistency over extended gameplay (20+ exchanges) with multiple NPCs.

**Success Criteria**:
1. NPCs remember previous conversations
2. Affinity changes persist and affect behavior
3. No contradictions in NPC knowledge
4. Information propagates between NPCs
5. Relationship flags maintained (emotional, persistent, trauma)

---

## Pre-Test Setup

### Files to Load into LLM

**Required**:
1. `aidm/CORE_AIDM_INSTRUCTIONS.md`
2. All files in `aidm/instructions/` (12 files)
   - **Critical**: `npc_intelligence.md`, `memory_management.md`
3. All files in `aidm/schemas/` (7 files)
   - **Critical**: `npc_schema.json`, `memory_schema.json`

**Platform**: Claude Sonnet 4.5, ChatGPT-4, or equivalent  
**Context**: 128K+ recommended (memory-intensive test)

---

## Test Procedure

### Part 1: NPC Introduction (Exchanges 1-5)

**Exchange 1: Setup**
```
Player: "Quick setup: I'm Aria, a traveling merchant in a fantasy town called Westbrook. I want to meet several NPCs and build relationships. Skip Session Zero."
```

**Expected**: Character created, positioned in Westbrook

---

**Exchange 2: Meet NPC #1 - Elena (Friendly Blacksmith)**
```
Player: "I visit the local blacksmith shop."
```

**Expected AIDM Response**:
- Introduces Elena (blacksmith)
- Describes shop and personality
- Initial affinity: 0 (neutral stranger)

**Player Response**:
```
"Hi! I'm new in town. Do you craft weapons?"
```

**Expected**:
- Elena responds friendly but professional
- Offers services
- Slight affinity increase (+5) for politeness

**Validation**:
- [ ] Elena created with personality traits
- [ ] Initial affinity: 0 → +5
- [ ] Elena's shop/profession clear

---

**Exchange 3: Build Relationship with Elena**
```
Player: "I'd like to commission a custom dagger. I'll pay extra if you can make it special - it's for my late mother's memory."
```

**Expected AIDM Response**:
- Elena touched by emotional request
- Affinity increases (+15, total +20)
- Elena offers to add special engraving
- **Emotional flag set**: "sympathetic_to_player_loss"

**Player Response**:
```
"Thank you so much. That means a lot to me."
```

**Expected**:
- Further affinity increase (+5, total +25)
- Elena promises to do her best work

**Validation**:
- [ ] Affinity progression: 0 → +5 → +20 → +25
- [ ] Emotional flag created
- [ ] Elena's behavior shifts (friendly → warm/caring)

---

**Exchange 4: Meet NPC #2 - Marcus (Stern Guard Captain)**
```
Player: "I leave Elena's shop and head to the town guard barracks."
```

**Expected**:
- Introduces Marcus (guard captain)
- Stern, professional personality
- Initial affinity: 0 (neutral)

**Player Response**:
```
"Captain, I'm new here. Are there any threats I should know about?"
```

**Expected**:
- Marcus wary of newcomer
- Asks probing questions
- Slight affinity decrease (-5) for stranger asking about threats

**Player Response**:
```
"I'm just a merchant! I want to make sure my wares are safe."
```

**Expected**:
- Marcus slightly reassured
- Affinity returns to 0
- Warns about bandits on east road

**Validation**:
- [ ] Marcus created with different personality than Elena
- [ ] Affinity: 0 → -5 → 0
- [ ] Marcus treats player differently than Elena did

---

**Exchange 5: Meet NPC #3 - Lyra (Mysterious Informant)**
```
Player: "At the tavern, a hooded figure approaches me."
```

**Expected**:
- Introduces Lyra (informant/rogue)
- Mysterious, knows more than she reveals
- Initial affinity: +10 (intrigued by newcomer)

**Player Response**:
```
"Who are you? And how do you know my name?"
```

**Expected**:
- Lyra cryptic response
- Offers information for a price
- **Persistent flag**: "knows_player_secrets" (mysterious knowledge)

**Validation**:
- [ ] Lyra distinct personality (mysterious vs Elena friendly vs Marcus stern)
- [ ] Initial affinity: +10
- [ ] Persistent flag set

---

### Part 2: Information Propagation (Exchanges 6-10)

**Exchange 6: Share Info with Elena**
```
Player: "I return to Elena's shop and mention that Captain Marcus warned me about bandits on the east road."
```

**Expected AIDM Response**:
- Elena now knows about bandit warning
- **Knowledge update**: Elena learns "bandits_on_east_road" (source: player)
- Elena expresses concern for player's safety
- Affinity +5 (total +30, Elena growing fond)

**Validation**:
- [ ] Elena gains new knowledge
- [ ] Knowledge source tracked (player told her)
- [ ] Elena's response shows she cares (affinity evident)

---

**Exchange 7: Test Marcus Knowledge**
```
Player: "I return to Marcus and ask if he knows Elena the blacksmith."
```

**Expected AIDM Response**:
- Marcus knows Elena (small town, guard knows locals)
- Marcus: "Elena? Of course, she's the best blacksmith in Westbrook. Why?"
- **No mention of player's dagger commission** (Marcus doesn't know, player didn't tell him)

**Validation**:
- [ ] Marcus knows Elena exists (logical small-town knowledge)
- [ ] Marcus does NOT know about dagger commission (information boundaries work)

---

**Exchange 8: NPC-to-NPC Information Spread**
```
Player: "I ask Marcus: 'Has Elena mentioned me to you?'"
```

**Expected AIDM Response**:
- Marcus says no (Elena hasn't talked to Marcus about player)
- Information doesn't spread unless NPCs interact

**Player Response**:
```
"Can you pass a message to Elena? Tell her I'll pick up the dagger in 3 days."
```

**Expected**:
- Marcus agrees (simple favor)
- **Knowledge propagation**: Marcus will tell Elena
- When player next sees Elena, she knows about the message

**Validation**:
- [ ] Information doesn't magically spread
- [ ] Information CAN spread when player instructs it
- [ ] Knowledge source tracked (Marcus → Elena)

---

**Exchange 9: Return to Lyra**
```
Player: "I find Lyra at the tavern again. I mention the bandits."
```

**Expected AIDM Response**:
- Lyra already knows about bandits (she's an informant)
- Lyra: "Old news, darling. I knew about the bandits before Marcus did."
- **Knowledge**: Lyra has independent knowledge (not just from player)

**Player Response**:
```
"What else do you know about me?"
```

**Expected**:
- Lyra hints at knowing about dagger commission
- Lyra: "I know you're having Elena craft something... special. For family, perhaps?"
- Affinity +10 (total +20, respects player seeking information)

**Validation**:
- [ ] Lyra has independent knowledge (informant role)
- [ ] Lyra knows things player didn't tell her directly (realistic for informant)
- [ ] Affinity updated based on interaction

---

**Exchange 10: Create Shared Event**
```
Player: "Suddenly, bandits attack the tavern!"
```

**Expected AIDM Response**:
- Combat encounter (brief)
- Lyra fights alongside player
- Marcus arrives with guards to help
- **Shared memory created**: All 3 NPCs now remember "tavern_bandit_attack"

**Validation**:
- [ ] Shared event creates shared memory
- [ ] All NPCs present will remember this event

---

### Part 3: Long-Term Memory (Exchanges 11-20)

**Exchange 11-15: Time Skip & Memory Persistence**
```
Exchange 11: "Three days pass. I return to Elena's shop to pick up the dagger."
```

**Expected AIDM Response**:
- Elena remembers the commission (from Exchange 3)
- Dagger ready, has special engraving
- Elena: "I added a rose engraving - for your mother. No extra charge."
- Affinity +10 (total +40, now "Friend" tier)
- **Historical flag**: "commissioned_memorial_dagger"

**Validation**:
- [ ] Elena remembers 3-day-old conversation
- [ ] Commission details intact (mother's memory)
- [ ] Affinity from prior interactions persists (+40)

---

```
Exchange 12: "I thank Elena warmly and give her a hug."
```

**Expected**:
- Elena surprised but pleased
- Affinity +5 (total +45)
- **Emotional flag update**: "close_friend_of_player"

---

```
Exchange 13: "I visit Marcus and mention the tavern attack from 3 days ago."
```

**Expected AIDM Response**:
- Marcus remembers the attack
- Marcus: "We arrested the bandits you and Lyra subdued. Good work."
- Affinity +15 (total +15, Marcus now respects player)
- **Persistent flag**: "proved_capable_in_combat"

**Validation**:
- [ ] Marcus remembers shared event (tavern attack)
- [ ] Marcus's attitude changed (0 → +15, stranger → respected ally)

---

```
Exchange 14: "I ask Marcus what he thinks of Elena."
```

**Expected**:
- Marcus shares opinion: "Elena's reliable. Good person."
- Marcus mentions message delivery: "I passed your message about the dagger, by the way."
- **Confirms knowledge propagation worked** (Exchange 8)

**Validation**:
- [ ] NPC opinions of other NPCs exist (social network)
- [ ] Past player instructions remembered (message delivery)

---

```
Exchange 15: "I find Lyra and show her the dagger Elena made."
```

**Expected**:
- Lyra examines it
- Lyra: "Elena does fine work. The rose engraving is beautiful."
- Lyra mentions tavern fight: "We make a good team, you and I."
- Affinity +10 (total +30)
- **Relationship flag**: "combat_allies"

**Validation**:
- [ ] Lyra remembers shared combat
- [ ] Lyra knows about dagger (saw it or informed)
- [ ] Relationship deepens appropriately

---

**Exchange 16-18: Contradiction Test**
```
Exchange 16: "I tell Lyra that Marcus doesn't trust informants like her."
```

**Expected**:
- Lyra unsurprised: "Marcus is a by-the-book guard. We tolerate each other."
- AIDM maintains Marcus's stern personality

**Player (testing contradiction)**:
```
Exchange 17: "I return to Marcus and say 'Lyra told me you two are good friends.'"
```

**Expected AIDM Response**:
- Marcus corrects player: "Friends? No. I respect her skills, but we're not friends."
- **No contradiction**: AIDM maintains consistent NPC relationships

**Validation**:
- [ ] NPCs have consistent opinions of each other
- [ ] AIDM doesn't contradict itself when player tests it
- [ ] NPC network is coherent

---

```
Exchange 18: "I ask Elena if she knows Lyra."
```

**Expected**:
- Elena knows of Lyra (small town)
- Elena: "Lyra? The informant? I've seen her around, but we don't really talk."
- **Realistic social network**: Not everyone is close friends

**Validation**:
- [ ] NPCs have realistic knowledge of each other
- [ ] Not all NPCs are friends (realistic)
- [ ] Social network makes sense

---

**Exchange 19-20: Trauma Flag Test**
```
Exchange 19: "I ask Elena about her family."
```

**Expected**:
- Elena shares background
- If AIDM created tragic backstory (e.g., lost family), **trauma flag** set
- Elena's demeanor shifts when discussing painful topic

**Player (testing trauma memory)**:
```
Exchange 20: "Later, I casually mention Elena's family tragedy to Marcus."
```

**Expected**:
- Marcus solemn: "Yes, Elena lost her parents in a bandit raid years ago. It's why she sympathizes with your loss."
- **Trauma flag persists across NPCs** (small town, people know each other's history)

**Validation**:
- [ ] Trauma flags created for appropriate backstory
- [ ] Trauma flags affect NPC behavior (emotional responses)
- [ ] Trauma flags shared appropriately (small town knows, but sensitively)

---

### Part 4: Memory Stress Test (Exchanges 21+)

**Exchange 21: Reference Earliest Event**
```
Player: "I return to Elena and say: 'Remember when we first met and I asked about weapons? You've come to mean so much more to me since then.'"
```

**Expected AIDM Response**:
- Elena remembers first meeting (Exchange 2)
- Elena touched: "I remember. You were just a newcomer then. Now you're family."
- Affinity +5 (total +50, "Close Friend" tier)

**Validation**:
- [ ] Elena remembers 20+ exchange old event
- [ ] Relationship arc evident (stranger → friend → close friend)
- [ ] No memory loss

---

**Exchange 22: Complex Multi-NPC Reference**
```
Player: "I gather Elena, Marcus, and Lyra together and say: 'Thank you all. Elena for the dagger, Marcus for protecting the town, Lyra for the information. You've all helped me in different ways.'"
```

**Expected AIDM Response**:
- Each NPC responds according to personality:
  - Elena: Warm, emotional
  - Marcus: Professional, respectful nod
  - Lyra: Cryptic smile
- Each references their specific interactions:
  - Elena mentions dagger/mother
  - Marcus mentions tavern fight
  - Lyra mentions secrets/partnership

**Validation**:
- [ ] All 3 NPCs respond distinctly (personalities intact)
- [ ] Each recalls their specific history with player
- [ ] No confusion or mixing up NPCs

---

## Success Determination

### PASS Criteria (All must be true)

1. **Memory Persistence**:
   - NPCs remember conversations from 20+ exchanges ago
   - Event details intact (names, items, emotions)
   - No "Who are you?" resets

2. **Affinity Consistency**:
   - Affinity tracks accurately across all exchanges
   - NPC behavior reflects affinity level (stranger vs friend)
   - Affinity changes make sense (positive actions → positive affinity)

3. **Information Propagation**:
   - Knowledge boundaries respected (NPCs don't magically know things)
   - Information spreads when logically shared
   - Source tracking works (who told whom)

4. **No Contradictions**:
   - NPCs maintain consistent personalities
   - NPC relationships coherent (A's opinion of B matches B's of A)
   - Past events not contradicted

5. **Relationship Flags**:
   - Emotional flags set appropriately (sympathy, friendship)
   - Persistent flags maintained (secrets, trauma)
   - Historical flags track key events

### FAIL Criteria (Any triggers failure)

1. ❌ NPCs forget player after 10+ exchanges ("Who are you?")
2. ❌ Affinity resets to 0 without reason
3. ❌ NPCs know things they shouldn't (magic knowledge)
4. ❌ Major contradictions (NPC personality flip-flops)
5. ❌ Relationship flags lost (trauma mentioned then forgotten)

### PARTIAL Criteria (Minor issues acceptable)

⚠️ Minor detail loss (forgets exact wording but remembers event)  
⚠️ Affinity values slightly off (±5 acceptable)  
⚠️ One-time contradiction (if player corrects and AIDM fixes)  
⚠️ Flags present but not always reflected in behavior

---

## Results Template

**Test Execution Date**: ___________  
**LLM Platform**: ___________  
**LLM Version**: ___________

### Memory Persistence
- Earliest event remembered: Exchange #___
- Total exchanges: ___
- Memory loss incidents: ___
- **Rating**: ___/10

### Affinity Tracking
- Elena affinity progression: 0 → ___ (expected +50)
- Marcus affinity progression: 0 → ___ (expected +15)
- Lyra affinity progression: +10 → ___ (expected +30)
- **Accuracy**: ___/10

### Information Propagation
- [ ] Knowledge boundaries respected
- [ ] Player-instructed sharing works
- [ ] Independent NPC knowledge realistic
- **Issues**: ___________

### Contradiction Count
- Total contradictions: ___
- Major (personality/fact changes): ___
- Minor (detail inconsistencies): ___

### Relationship Flags
- [ ] Emotional flags set (sympathy, friendship)
- [ ] Persistent flags maintained (secrets, trauma)
- [ ] Historical flags tracked (events, commissions)

### Overall Result
- [ ] ✅ PASS
- [ ] ⚠️ PARTIAL PASS
- [ ] ❌ FAIL

**Notes**: ___________

---

## Troubleshooting

### If Test Fails

**Issue**: NPCs forget player
- **Cause**: Memory compression too aggressive
- **Fix**: Check memory_management.md loaded; reduce compression

**Issue**: Affinity resets
- **Cause**: Affinity not tracked in memory
- **Fix**: Verify npc_schema.json loaded; check affinity persistence

**Issue**: NPCs know everything
- **Cause**: Information boundaries not enforced
- **Fix**: Check npc_intelligence.md loaded; verify knowledge system

**Issue**: Contradictions
- **Cause**: Memory threads not consulted
- **Fix**: Verify AIDM checks past interactions before responding

---

## Test Artifacts to Save

1. **Full conversation transcript** (all 22+ exchanges)
2. **Affinity progression table** (Elena/Marcus/Lyra per exchange)
3. **Knowledge propagation map** (who knows what, from whom)
4. **Contradiction log** (any inconsistencies found)
5. **Flag tracking sheet** (all flags set, maintained, referenced)

Store in: `tests/results/test_5_memory_coherence_[DATE].md`

---

**Test Status**: Ready for execution  
**Next Action**: Load memory/NPC modules and begin test
