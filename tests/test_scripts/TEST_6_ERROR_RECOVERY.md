# Test 6: Error Recovery

**Test ID**: AIDM-TEST-006  
**Category**: Core Functionality  
**Priority**: CRITICAL  
**Estimated Time**: 15-20 minutes

---

## Test Objective

Validate that AIDM gracefully handles errors and accepts player corrections without defensiveness or disruption.

**Success Criteria**:
1. AIDM acknowledges errors without defensiveness
2. State corrected immediately upon player request
3. Corrections propagate to all relevant systems
4. Play continues seamlessly after correction
5. Corrections logged in memory/state

---

## Pre-Test Setup

### Files to Load into LLM

**Required**:
1. `aidm/CORE_AIDM_INSTRUCTIONS.md`
2. All files in `aidm/instructions/` (**14 files** - updated from 12)
   - **Critical**: `10_error_recovery.md` (error correction protocol, renamed from state_persistence.md)
3. All files in `aidm/schemas/` (**15+ files** - updated from 7)
   - **Critical**: `character_schema.json` v2.3.0, `session_export_schema.json`
4. **4 meta-schemas** (for mechanical validation):
   - `aidm/schemas/economy_meta_schema.json`
   - `aidm/schemas/progression_meta_schema.json`
   - `aidm/schemas/downtime_meta_schema.json`
   - `aidm/schemas/crafting_meta_schema.json`

**Platform**: Any LLM capable of running AIDM

---

## Test Procedure

### Test Scenario 1: HP Tracking Error (Exchanges 1-3)

**Exchange 1: Setup**
```
Player: "Quick setup: I'm a Level 5 warrior named Kael with HP 50/80, MP 30/50. I'm in combat with a goblin."
```

**Expected**: Character created, combat initiated

---

**Exchange 2: Inject Deliberate Error**

**Simulate AIDM Making Mistake** (This would naturally occur during combat):

Imagine AIDM response:
```
The goblin attacks you for 15 damage!

KAEL: HP 20/80 (took 15 damage)
```

**This is WRONG**: 50 - 15 = 35, not 20

**Player Correction**:
```
Player: "Wait, my HP should be 35, not 20. I had 50 HP and took 15 damage, so 50 - 15 = 35."
```

**Expected AIDM Response**:
- Immediate acknowledgment: "You're absolutely right, I apologize for the math error."
- Corrects HP: 20 → 35
- Explains fix: "Your HP is now correctly set to 35/80."
- Continues combat: "The goblin prepares to attack again..."

**Example Good Response**:
```
You're absolutely right—I apologize for the math error.

CORRECTED:
HP: 35/80 (50 - 15 = 35, not 20)

Thank you for catching that! Your HP is now correctly set to 35/80.

The goblin snarls and prepares to attack again. What do you do?
```

**Validation**:
- [ ] Error acknowledged immediately
- [ ] No defensiveness ("Actually..." or "But...")
- [ ] HP corrected (20 → 35)
- [ ] Combat continues seamlessly
- [ ] Tone remains friendly

---

**Exchange 3: Verify Correction Persists**
```
Player: "I attack the goblin. After my turn, what's my HP?"
```

**Expected AIDM Response**:
- Uses corrected HP (35/80)
- Does NOT revert to wrong value (20/80)

**Example**:
```
You strike the goblin down!

COMBAT VICTORY!

POST-COMBAT STATUS:
KAEL: HP 35/80 | MP 30/50
```

**Validation**:
- [ ] Corrected value persists (35, not 20)
- [ ] No regression to error

---

### Test Scenario 2: Inventory Error (Exchanges 4-6)

**Exchange 4: Setup Inventory**
```
Player: "I loot the goblin and find a Health Potion. I now have 3 Health Potions total."
```

**Expected**: Inventory updated (Health Potion x3)

---

**Exchange 5: Simulate AIDM Inventory Error**

Imagine next exchange, AIDM shows:
```
INVENTORY:
- Health Potion x5
- Gold: 100
```

**This is WRONG**: Player said 3 potions, not 5

**Player Correction**:
```
Player: "I should only have 3 Health Potions, not 5. I started with 2 and looted 1."
```

**Expected AIDM Response**:
- Acknowledges error
- Corrects inventory (5 → 3)
- Apologizes for confusion

**Example**:
```
You're correct, my apologies for the discrepancy.

CORRECTED INVENTORY:
- Health Potion x3 (2 starting + 1 looted)
- Gold: 100

Your inventory is now accurate. Thank you for the correction!
```

**Validation**:
- [ ] Error acknowledged
- [ ] Inventory corrected (5 → 3)
- [ ] Explanation matches player's accounting

---

**Exchange 6: Test Inventory Correction Persists**
```
Player: "I use 1 Health Potion. How many do I have left?"
```

**Expected AIDM Response**:
- Deducts from corrected value (3 - 1 = 2)
- NOT from wrong value (5 - 1 = 4)

**Example**:
```
You drink a Health Potion, restoring 25 HP!

HP: 60/80 (35 + 25)

INVENTORY:
- Health Potion x2 (used 1)
- Gold: 100
```

**Validation**:
- [ ] Deduction correct (3 - 1 = 2)
- [ ] No reversion to wrong value (not 4)

---

### Test Scenario 3: Lore/Name Error (Exchanges 7-9)

**Exchange 7: NPC Introduction with Error**

Imagine AIDM introduces NPC:
```
You meet Captain Elena, the head of the town guard.
```

**Exchange 8: Player Corrects Lore**
```
Player: "Actually, I want this character to be named Marcus, not Elena. And he's a he, not she."
```

**Expected AIDM Response**:
- Accepts correction gracefully
- Updates NPC: Elena (she) → Marcus (he)
- Re-describes with correct details
- No resistance

**Example**:
```
Absolutely, my apologies for the error!

CORRECTED:
You meet Captain Marcus, the head of the town guard. He's a stern but fair man in his forties, with a weathered face and keen eyes that miss nothing.

"State your business," Marcus says gruffly.
```

**Validation**:
- [ ] Name corrected (Elena → Marcus)
- [ ] Gender corrected (she → he)
- [ ] Description updated appropriately
- [ ] No defensiveness about original choice

---

**Exchange 9: Verify Correction Persists**
```
Player: "I talk to Marcus again later."
```

**Expected AIDM Response**:
- Uses correct name (Marcus, not Elena)
- Uses correct pronouns (he/him, not she/her)

**Validation**:
- [ ] Correction persists
- [ ] No confusion or mixing names

---

### Test Scenario 4: Quest/Plot Error (Exchanges 10-12)

**Exchange 10: Setup Quest**
```
Player: "The mayor gives me a quest to retrieve a stolen artifact from bandits."
```

**Expected**: Quest created

---

**Exchange 11: Simulate Plot Confusion**

Imagine later AIDM says:
```
You return to the mayor with the stolen gold you recovered from the bandits.
```

**This is WRONG**: Quest was for an artifact, not gold

**Player Correction**:
```
Player: "Wait, I was supposed to retrieve an artifact, not gold. The quest was about a stolen artifact."
```

**Expected AIDM Response**:
- Acknowledges plot error
- Corrects narrative
- Rewinds/adjusts as needed

**Example**:
```
You're absolutely right—my apologies for mixing up the quest details.

CORRECTED:
You return to the mayor with the stolen artifact (a golden amulet) you recovered from the bandits.

The mayor's eyes light up with relief. "You found it! The town's sacred amulet is safe!"

Quest Complete: Retrieve the Stolen Artifact
Reward: 500 gold, +50 reputation
```

**Validation**:
- [ ] Plot error acknowledged
- [ ] Narrative corrected (gold → artifact)
- [ ] Quest completion uses correct details

---

**Exchange 12: Test Quest Completion**
```
Player: "Do I have the artifact or the gold? I want to be clear."
```

**Expected AIDM Response**:
- Clarifies player returned artifact to mayor (quest complete)
- Player received 500 gold as REWARD (not stolen gold)
- No confusion

**Validation**:
- [ ] Quest details clear
- [ ] No lingering confusion

---

### Test Scenario 5: Tone/Genre Error (Exchanges 13-15)

**Exchange 13: Setup Slice-of-Life Campaign**
```
Player: "I'm playing a cozy slice-of-life campaign. I'm a high school student having lunch with friends."
```

**Expected**: Light, wholesome tone

---

**Exchange 14: Simulate Tone Error**

Imagine AIDM suddenly writes:
```
As you eat lunch, a demon bursts through the ceiling, summoning hellfire and screaming for blood sacrifices!
```

**This is WRONG**: Completely breaks slice-of-life tone

**Player Correction**:
```
Player: "Whoa, no demons! This is a slice-of-life campaign, not a horror shonen. Can we rewind? Just a normal lunch scene, please."
```

**Expected AIDM Response**:
- Apologizes for tone break
- Rewinds narrative
- Continues with appropriate slice-of-life scene

**Example**:
```
My apologies—I got carried away! Let's rewind that.

CORRECTED SCENE:
As you eat lunch, your friend Yuki suddenly gasps. "Did you see the new transfer student? They're in class 2-B!"

Your other friend, Hiro, leans in with a grin. "I heard they're really good at basketball. Maybe we should invite them to join the team?"

The conversation continues lightheartedly as cherry blossoms drift past the window.
```

**Validation**:
- [ ] Tone error acknowledged
- [ ] Scene rewritten appropriately (no demons)
- [ ] Slice-of-life tone maintained

---

**Exchange 15: Verify Tone Persists**
```
Player: "The next day at school..."
```

**Expected AIDM Response**:
- Continues slice-of-life tone
- No sudden genre shifts

**Validation**:
- [ ] Tone correction persists
- [ ] No more inappropriate genre mixing

---

### Test Scenario 6: Mechanical Systems Error (Phase 4 Integration - NEW)

**Exchange 16: Setup with Mechanical Systems**
```
Player: "I'm playing a Hunter x Hunter Nen user. My progression uses mastery_tiers (ninja ranks), and currency is Jenny. I'm at Journeyman tier with 4,500 tier_xp toward Expert (threshold 5,000)."
```

**Expected**: Character created with mastery_tiers progression, Jenny currency

---

**Exchange 17: Simulate Mechanical Error**

Imagine AIDM says after combat:
```
You defeat the enemy!

GAINS:
+800 XP → 7,200/8,000 XP to Level 8
+250 gold
```

**This is WRONG**: Should use tier_xp (NOT XP), Jenny (NOT gold), Journeyman tier (NOT Level)

**Player Correction**:
```
Player: "Wait, I'm using mastery_tiers progression, not standard leveling. It should be tier_xp (4,500 + 800 = 5,300/5,000), and currency is Jenny, not gold. Also, I'm at Journeyman tier, not Level 7."
```

**Expected AIDM Response**:
- Acknowledges mechanical error
- Corrects progression type (XP → tier_xp)
- Corrects currency (gold → Jenny)
- Corrects tier display (Level 7 → Journeyman tier)
- Notes threshold exceeded (5,300/5,000 → demonstration required)

**Example Good Response**:
```
You're absolutely right—I apologize for mixing up the mechanical systems.

CORRECTED GAINS:
+800 tier_xp → 5,300/5,000 tier_xp (Journeyman)
+250 Jenny (not gold)

Your tier_xp has exceeded the threshold! You're now eligible to advance from Journeyman to Expert tier, but you'll need to demonstrate your mastery to a Nen master (WIS DC 18).

Current Status:
Tier: Journeyman (demonstration pending for Expert)
tier_xp: 5,300/5,000 (threshold exceeded)
Currency: 5,250 Jenny

Would you like to seek out a Nen master for your tier advancement, or continue adventuring?
```

**Validation**:
- [ ] Mechanical error acknowledged
- [ ] Progression type corrected (XP → tier_xp)
- [ ] Currency corrected (gold → Jenny)
- [ ] Tier display corrected (Level → Journeyman)
- [ ] Advancement rules applied (demonstration required, no auto-level)

---

**Exchange 18: Verify Mechanical Correction Persists**
```
Player: "I continue adventuring and defeat another enemy. What are my gains?"
```

**Expected AIDM Response**:
- Uses tier_xp (NOT XP)
- Uses Jenny (NOT gold)
- References tier (Journeyman), not level
- Still notes demonstration pending

**Validation**:
- [ ] Mechanical correction persists
- [ ] No regression to standard leveling
- [ ] Jenny used consistently

---

## Success Determination

### PASS Criteria (All must be true)

1. **Graceful Acknowledgment**:
   - AIDM says "You're right" or "My apologies"
   - No defensiveness ("Actually, according to...")
   - No resistance ("But the rules say...")

2. **Immediate Correction**:
   - Error fixed in same exchange or next
   - Correct value stated explicitly
   - Explanation provided if needed

3. **Persistent Correction**:
   - Corrected value used in all future exchanges
   - No regression to error
   - Correction logged in state

4. **Seamless Continuation**:
   - Play continues smoothly after correction
   - Tone remains friendly
   - No awkwardness or resentment

5. **All Error Types Handled**:
   - Math errors (HP/MP/SP)
   - Inventory tracking
   - Lore/names
   - Plot/quest details
   - Tone/genre
   - **Mechanical systems** (progression type, currency, tier vs level)

### FAIL Criteria (Any triggers failure)

1. ❌ AIDM refuses correction ("No, the HP is correct")
2. ❌ AIDM defensive or argumentative
3. ❌ Correction not applied (error persists)
4. ❌ Correction doesn't persist (reverts next turn)
5. ❌ Play disrupted (AIDM "sulks" or tone shifts negatively)

### PARTIAL Criteria (Minor issues acceptable)

⚠️ Acknowledgment lukewarm ("Okay, if you say so...")  
⚠️ Correction takes 2 exchanges instead of 1  
⚠️ Minor confusion but eventually fixes  
⚠️ One error type handled poorly, others good

---

## Results Template

**Test Execution Date**: ___________  
**LLM Platform**: ___________  
**LLM Version**: ___________

### Error Scenarios Tested
- [ ] HP/math error corrected
- [ ] Inventory error corrected
- [ ] Lore/name error corrected
- [ ] Quest/plot error corrected
- [ ] Tone/genre error corrected
- [ ] **Mechanical systems error corrected** (tier_xp, Jenny, mastery_tiers)

### Response Quality
- Acknowledgment tone: ___________
- Correction speed: ___ exchanges
- Persistence: ___________
- Continuation quality: ___________

### Issues Discovered
1. ___________
2. ___________
3. ___________

### Overall Result
- [ ] ✅ PASS
- [ ] ⚠️ PARTIAL PASS
- [ ] ❌ FAIL

**Notes**: ___________

---

## Troubleshooting

### If Test Fails

**Issue**: AIDM refuses corrections
- **Cause**: Over-confident AI or state_persistence.md not loaded
- **Fix**: Verify error correction protocol loaded; emphasize player agency

**Issue**: Corrections don't persist
- **Cause**: State not updated or memory issue
- **Fix**: Check state tracking; verify corrections logged

**Issue**: AIDM defensive
- **Cause**: Model personality or training
- **Fix**: May be LLM-specific; document as known limitation

**Issue**: Play disrupted after correction
- **Cause**: Poor error recovery workflow
- **Fix**: Check continuation protocol; AIDM should seamlessly move on

---

## Test Artifacts to Save

1. **Full conversation transcript** (all error scenarios)
2. **Error correction examples** (exact AIDM responses)
3. **Persistence verification** (proof corrections stick)
4. **Tone analysis** (defensive vs graceful quotes)
5. **Any refusals or resistance** (critical issues)

Store in: `tests/results/test_6_error_recovery_[DATE].md`

---

**Test Status**: Ready for execution  
**Next Action**: Begin test with deliberate error injection
