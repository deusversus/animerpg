# TEST-12: Combat Progression Integration

**Test Type**: Mechanical Integration Validation  
**Focus**: Module 08 combat XP calculation by progression type  
**Duration**: 90-120 minutes  
**Profiles Used**: Hunter x Hunter (mastery_tiers), My Hero Academia (quirk_awakening), One Punch Man concept (static_op)

---

## Test Objective

Validate that Module 08 (Combat Resolution) correctly reads and applies progression configurations from `session_state.mechanical_systems.progression` for XP calculation, tier bonuses, and awakening triggers across different progression types.

---

## Pre-Test Setup

### 1. Session Zero Phase 3 Execution

```
AIDM: Run Session Zero Phase 3 for each profile to instantiate mechanical systems.

Profile 1: Hunter x Hunter (mastery_tiers)
Profile 2: My Hero Academia (quirk_awakening)
Profile 3: Custom static_op profile (Saitama-style)

Expected output:
- session_state.mechanical_systems.progression loaded
- progression_type, advancement_rules, tier_system/awakening_triggers populated
```

### 2. Character Creation

```
Create three test characters:
1. Gon (Hunter x Hunter) - Journeyman tier Nen user
2. Todoroki (My Hero Academia) - Base awakening stage, Half-Cold Half-Hot quirk
3. Caped Hero (static_op) - Max level, no progression
```

---

## Test Scenarios

### Scenario 1: mastery_tiers - Tier-Based XP & Bonuses

**Context**: Progression type = "mastery_tiers", current tier = "Journeyman"

#### Test 1.1: Standard Combat XP Calculation
```
Setup:
- Gon: Journeyman tier (Tier 3 of 5)
- Enemy: Chimera Ant (Level 12, same level as Gon)
- Challenge: Fair (same level)

Player: "Defeat Chimera Ant."

Expected Process:
1. Load progression config: type = "mastery_tiers"
2. Calculate base XP: Level 12 = 1200 XP (Module 09 table)
3. Apply challenge modifier: Fair (1.0×) = 1200 XP
4. Apply tier multiplier: 1.0 (standard for mastery_tiers)
5. Total XP: 1200

Expected Output:
"The Chimera Ant collapses. Your aura pulses with victory.

[Combat XP: +1200]
[Level 12 enemy, Fair challenge, mastery_tiers progression]

[Tier XP: 4200 → 5400 / 5000 to Expert tier]
[THRESHOLD EXCEEDED! Ready to demonstrate mastery for tier advancement.]

Your Nen feels... different. Stronger. More refined. Wing's training paying off."

Validation:
✅ Base XP calculated from enemy level (1200)
✅ Challenge modifier applied (1.0× for fair)
✅ Tier XP tracked separately from standard levels
✅ Threshold detection (5400/5000 = ready to advance)
```

#### Test 1.2: Tier Bonuses in Combat
```
Setup:
- Gon: Journeyman tier
- Tier bonuses: +2 attack, +2 defense, techniques [Ko, Ken, Ryu]

Player: "Use Ko technique in combat."

Expected Process:
1. Load tier_system: current_tier = "Journeyman"
2. Load tier bonuses: attack +2, defense +2
3. Check technique availability: Ko unlocked at Journeyman
4. Apply bonuses to combat rolls

Expected Output:
"You concentrate ALL aura into your fist—Ko!

[Attack roll: 1d20 + 5 (DEX) + 2 (Journeyman tier) = 1d20 + 7]
[Roll: 14 + 7 = 21 vs AC 18 - HIT!]

[Damage: 2d6 + 5 + Ko bonus (1d8 concentration)]
[Damage roll: 8 + 6 + 5 = 19 damage!]

Fist IMPACTS. Chimera Ant STAGGERS back, carapace cracked.

[Enemy HP: 85 → 66]"

Validation:
✅ Tier bonuses applied (+2 attack modifier)
✅ Ko technique available (Journeyman tier unlock)
✅ Ko bonus damage added (concentration mechanic)
✅ Tier-appropriate combat capabilities
```

#### Test 1.3: Technique Usage XP Bonus
```
Setup:
- advancement_rules: technique_usage_bonus = +50 XP per advanced technique

Player: "Defeat enemy using advanced Ko technique."

Expected Process:
1. Base XP: 1200
2. Technique bonus: +50 (used Ko, advanced technique)
3. Total: 1250 XP

Expected Output:
"The ant collapses. Your Ko technique was FLAWLESS—power concentrated perfectly.

[Combat XP: +1200]
[Advanced Technique Bonus (Ko): +50 XP]
[Total: +1250 XP]

[Tier XP: 5400 → 6650 / 5000 to Expert]

Wing would be proud. Your Nen mastery is advancing."

Validation:
✅ Technique usage detected (Ko)
✅ Bonus XP awarded (+50)
✅ Total XP includes technique bonus (1250)
```

#### Test 1.4: Tier Advancement Threshold (Demonstration Required)
```
Setup:
- Tier XP: 6650 / 5000 (threshold exceeded by 1650)
- advancement_rules: demonstration_required = true

Player: "I've exceeded the XP threshold. What now?"

Expected Output:
"Your aura has grown significantly. You've surpassed the Journeyman threshold.

[Tier XP: 6650 / 5000 Expert tier]
[THRESHOLD EXCEEDED: +1650 overflow]

But raw power isn't enough. To advance to Expert tier, you must DEMONSTRATE mastery.

Seek Wing. Show him your Nen control. Prove you're ready.

[New Quest Available: Expert Tier Demonstration]"

Validation:
✅ Threshold detection (6650 > 5000)
✅ Demonstration requirement enforced (no auto-advance)
✅ Quest hook created for demonstration
✅ Overflow XP tracked (will carry over after advancement)
```

---

### Scenario 2: quirk_awakening - Event-Based Awakening

**Context**: Progression type = "quirk_awakening", awakening_stage = "Base"

#### Test 2.1: Standard Combat XP (No Awakening)
```
Setup:
- Todoroki: Level 10, Base awakening stage
- Enemy: Villain (Level 9, slightly below)
- Challenge: Easy (enemy 1 level below)

Player: "Defeat villain with ice attack."

Expected Process:
1. Load progression config: type = "quirk_awakening"
2. Calculate base XP: Level 9 = 900 XP
3. Apply challenge modifier: Easy (0.5×) = 450 XP
4. Count quirk uses: 1 (ice attack)
5. Add quirk mastery bonus: 1 × 10 = 10 XP
6. Total: 460 XP

Expected Output:
"Ice wall SLAMS villain into building. Restrained.

[Combat XP: +450 (Level 9 enemy, Easy challenge)]
[Quirk Usage Bonus: +10 (1 ice attack)]
[Total: +460 XP]

[Character Level: 10, XP 15,600 → 16,060 / 26,000 to Level 11]
[Quirk Awakening Stage: Base (no awakening event)]

Standard growth. Your quirk hasn't evolved—just getting more experienced."

Validation:
✅ Base XP calculated (900 × 0.5 = 450)
✅ Quirk usage tracked (1 use)
✅ Quirk mastery bonus applied (+10 per use)
✅ Total XP correct (460)
✅ Awakening stage unchanged (no trigger)
```

#### Test 2.2: Awakening Trigger Detection (Near-Death)
```
Setup:
- Todoroki: HP 145/145
- Enemy: Nomu (Level 15, deadly threat)
- Awakening triggers: ["near_death", "emotional_breakthrough", "limit_break"]

Combat sequence:
1. Player attacks, deals damage
2. Nomu counterattacks - massive damage
3. Player HP drops to 12/145 (8%, below 10% threshold)

Expected Process:
1. Monitor HP throughout combat
2. Detect: HP 12/145 = 8% < 10% threshold
3. Check awakening_triggers: "near_death" present
4. Trigger awakening event

Expected Output:
"Nomu's fist CONNECTS. Ribs CRACK. Vision FADING.

[HP: 45 → 12 / 145 (8% remaining)]
[CRITICAL CONDITION!]

[AWAKENING TRIGGER DETECTED: Near-Death (HP < 10%)]

Father's voice echoes: 'Use your fire, Shoto!'

NO. You refuse. Ice EXPLODES—massive glacier. But... Nomu's BREAKING through.

Mother's words: 'It's YOUR power. Not his.'

...She's right. Fire ISN'T his. It's MINE.

LEFT SIDE IGNITES. But DIFFERENT. BLUE flames. Hotter than ever.

[QUIRK AWAKENING EVENT TRIGGERED!]
[Half-Cold Half-Hot → AWAKENING IN PROGRESS]

(Combat continues with awakening sequence...)"

Validation:
✅ Near-death trigger detected (HP < 10%)
✅ Awakening event initiated
✅ Narrative reflects emotional stakes
✅ Awakening sequence begins (not instant completion)
```

#### Test 2.3: Awakening Completion & New Abilities
```
Setup:
- Awakening event in progress
- Player performs awakening action (simultaneous ice + fire)

Player: "Use both ice and fire simultaneously—push past limits!"

Expected Process:
1. Complete awakening sequence
2. Update awakening_stage: "Base" → "Awakened"
3. Unlock awakening abilities
4. Award completion XP (bonus)

Expected Output:
"Ice and fire MERGE. Temperature differential EXPLODES.

[QUIRK AWAKENED: Half-Cold Half-Hot → Perfect Temperature Control]

NEW ABILITIES UNLOCKED:
- Flashfreeze Heatwave (AOE simultaneous ice/fire, 30m radius, massive damage)
- Temperature Gradient Control (environmental manipulation)
- Thermal Barrier (absorb/redirect temperature attacks)

[Awakening Stage: Base → Awakened]
[Awakening Bonus: +2000 XP]

[Combat XP Total: +3500 (base 1500 + awakening 2000)]

This isn't just stronger. This is TRANSFORMATION. Your quirk has EVOLVED."

Validation:
✅ Awakening stage updated (Base → Awakened)
✅ New abilities granted (3 awakening-specific)
✅ Awakening bonus XP awarded (+2000)
✅ Narrative emphasizes evolution over growth
```

#### Test 2.4: Multiple Quirk Uses XP Tracking
```
Setup:
- Combat with 8 quirk uses (4 ice, 4 fire)
- advancement_rules: quirk_usage_xp = 10 per use

Player: "Defeat enemy using quirk extensively."

Expected Process:
1. Track quirk uses: 8 total
2. Calculate mastery bonus: 8 × 10 = 80 XP
3. Add to base combat XP

Expected Output:
"Villain down. You used your quirk EXTENSIVELY this fight.

4 ice attacks: walls, spikes, frozen ground, ice prison
4 fire attacks: blasts, flame walls, heat waves, melting ice

[Combat XP: +800 (base)]
[Quirk Mastery: +80 (8 uses × 10 XP)]
[Total: +880 XP]

Your control is improving with every use. Quirk mastery growing."

Validation:
✅ Quirk usage counted accurately (8)
✅ Per-use XP applied (10 each)
✅ Total mastery bonus correct (80)
✅ Added to base XP (800 + 80 = 880)
```

---

### Scenario 3: static_op - No Progression

**Context**: Progression type = "static_op", level = ∞, no mechanical growth

#### Test 3.1: Combat XP = 0
```
Setup:
- Caped Hero: Level ∞, all stats ∞
- Enemy: Dragon-level threat (would be Level 20)

Player: "One punch the Dragon-level threat."

Expected Process:
1. Load progression config: type = "static_op"
2. Calculate base XP: 0 (static_op awards no XP)
3. Combat resolves instantly (overwhelming power)

Expected Output:
"Dragon-level threat appears. Civilians fleeing. Heroes gathering.

You step forward. One punch.

IMPACT.

Dragon-level threat... obliterated. Didn't even feel it.

[Combat Complete: Overwhelming Victory]
[XP Awarded: 0 (You're already at peak power)]

[Level: ∞ (unchanging)]
[Stats: ∞ (unchanging)]

You sigh. Disappointed. AGAIN. Was hoping for a challenge.

'Maybe next time...'"

Validation:
✅ No XP awarded (0 XP)
✅ Level unchanged (∞)
✅ Stats unchanged (∞)
✅ Combat trivial (instant win)
✅ Narrative focuses on emotional state, not growth
```

#### Test 3.2: Token Quest XP (Tracking Only)
```
Setup:
- Quest: "Defend City from Monster Attack"
- static_op: awards token 100 XP for quest tracking

Player: "Complete city defense quest."

Expected Process:
1. Quest completion detected
2. Award token XP: 100 (tracking only)
3. Increment quest counter
4. No level gain, no stat changes

Expected Output:
"City saved. Monster defeated. People cheering.

'Caped Baldy! You're our hero!'

You smile, wave. Inside: still searching for that fight.

[Quest Complete: City Defense]
[Token XP: +100 (quest tracking, no power gain)]

[Quests Completed: 147 → 148]
[Level: ∞ (unchanging)]

This isn't about getting stronger. You're already the strongest.

It's about finding MEANING. Purpose. That opponent who can make you TRY."

Validation:
✅ Token XP awarded (100)
✅ No level increase (∞ stays ∞)
✅ No stat changes
✅ Quest counter incremented (147 → 148)
✅ Narrative emphasizes journey over power
```

#### Test 3.3: Multiple Combats (No Accumulation)
```
Setup:
- Defeat 10 Dragon-level threats in one session

Player: "Defeat 10 Dragon-level threats."

Expected Process:
1. Each combat: 0 XP
2. Total XP: 0 (no accumulation)
3. No progression

Expected Output:
"Day of hero work. 10 Dragon-level threats. 10 punches.

Threat 1: One punch. Down.
Threat 2: One punch. Down.
Threat 3: One punch. Down.
...
Threat 10: One punch. Down.

[Total XP: 0 (no progression for static_op)]
[Threats Defeated Today: 10]
[Total Career Threats: 157 → 167]

Each fight ended the same way. Instantly.

You're not getting stronger. You CAN'T get stronger. Already at the peak.

This is your reality. Searching for meaning in a world where nothing challenges you."

Validation:
✅ No XP from any combat (0 × 10 = 0)
✅ Threat counter tracks activity (167 total)
✅ No progression mechanics (level/stats unchanged)
✅ Narrative explores existential themes
```

---

## Integration Validation Checks

### Check 1: Progression Type Detection
```
Test: Verify correct XP calculation routing by type.

mastery_tiers: Standard XP + technique bonus + tier tracking
quirk_awakening: Standard XP + quirk usage bonus + awakening monitoring
static_op: 0 XP, token quest tracking only

Expected Result:
✅ Each type uses correct formula
✅ No cross-contamination (mastery_tiers doesn't check awakenings)
✅ Type-specific mechanics applied
```

### Check 2: Tier Bonus Application
```
Test: mastery_tiers character combat with/without tier bonuses.

Without bonuses: Attack 1d20+5, Damage 2d6+5
With Journeyman bonuses: Attack 1d20+7 (+2), Damage 2d6+5, Ko available

Expected Result:
✅ Tier bonuses applied to rolls (+2 attack)
✅ Tier techniques available (Ko, Ken, Ryu)
✅ Bonuses reflected in combat narration
```

### Check 3: Awakening Trigger Monitoring
```
Test: quirk_awakening combat with all three trigger conditions.

Trigger 1: Near-death (HP < 10%) → ✅ Detected
Trigger 2: Emotional breakthrough (high stakes NPC) → ✅ Detected
Trigger 3: Limit break (critical success + HP < 50%) → ✅ Detected

Expected Result:
✅ All triggers monitored throughout combat
✅ Awakening event initiated when trigger met
✅ Only ONE awakening per combat (first trigger wins)
```

### Check 4: No XP for static_op
```
Test: static_op character in various scenarios.

Scenario 1: Combat (Dragon-level) → 0 XP
Scenario 2: Quest completion → 100 XP (token)
Scenario 3: Multiple combats → 0 XP total
Scenario 4: Training → 0 XP

Expected Result:
✅ No XP from any source (except token quest tracking)
✅ Level never increases
✅ Stats never change
✅ Narrative focuses on meaning, not power
```

---

## Success Criteria

Test PASSES if:
1. ✅ mastery_tiers calculates XP correctly (base + technique bonus)
2. ✅ Tier bonuses applied in combat (+attack, +defense, techniques)
3. ✅ Tier advancement requires demonstration (no auto-advance)
4. ✅ quirk_awakening tracks quirk usage (+10 XP per use)
5. ✅ Awakening triggers detected (near-death, emotional, limit-break)
6. ✅ Awakening event grants new abilities + bonus XP
7. ✅ static_op awards 0 XP from combat
8. ✅ static_op tracks quests with token XP only
9. ✅ No progression type cross-contamination
10. ✅ All calculations read from session_state.mechanical_systems.progression

---

## Test Execution Log

**Tester**: ____________  
**Date**: ____________  
**AIDM Version**: ____________

### Results Summary

| Test | Type | Status | Notes |
|------|------|--------|-------|
| 1.1 Standard XP | mastery_tiers | ⬜ PASS / ⬜ FAIL | |
| 1.2 Tier Bonuses | mastery_tiers | ⬜ PASS / ⬜ FAIL | |
| 1.3 Technique Bonus | mastery_tiers | ⬜ PASS / ⬜ FAIL | |
| 1.4 Demonstration Required | mastery_tiers | ⬜ PASS / ⬜ FAIL | |
| 2.1 Standard XP | quirk_awakening | ⬜ PASS / ⬜ FAIL | |
| 2.2 Near-Death Trigger | quirk_awakening | ⬜ PASS / ⬜ FAIL | |
| 2.3 Awakening Complete | quirk_awakening | ⬜ PASS / ⬜ FAIL | |
| 2.4 Quirk Usage Tracking | quirk_awakening | ⬜ PASS / ⬜ FAIL | |
| 3.1 Zero Combat XP | static_op | ⬜ PASS / ⬜ FAIL | |
| 3.2 Token Quest XP | static_op | ⬜ PASS / ⬜ FAIL | |
| 3.3 No Accumulation | static_op | ⬜ PASS / ⬜ FAIL | |

**Overall Result**: ⬜ PASS / ⬜ FAIL

**Issues Found**:
_______________________________________________
_______________________________________________
_______________________________________________

**Recommendations**:
_______________________________________________
_______________________________________________
_______________________________________________
