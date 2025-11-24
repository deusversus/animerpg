# TEST-13: Leveling Mechanics Integration

**Test Type**: Mechanical Integration Validation  
**Focus**: Module 09 type-specific leveling systems  
**Duration**: 90-120 minutes  
**Profiles Used**: Hunter x Hunter (mastery_tiers), My Hero Academia (quirk_awakening + class_based hybrid), Milestone-based custom

---

## Test Objective

Validate that Module 09 (Progression Systems) correctly reads and applies progression configurations from `session_state.mechanical_systems.progression` for leveling mechanics across different progression types.

---

## Pre-Test Setup

### 1. Session Zero Phase 3 Execution

```
AIDM: Run Session Zero Phase 3 for each profile to instantiate mechanical systems.

Profile 1: Hunter x Hunter (mastery_tiers)
Profile 2: My Hero Academia (quirk_awakening with class_based hybrid)
Profile 3: Custom milestone_based profile

Expected output:
- session_state.mechanical_systems.progression loaded
- Type-specific leveling rules populated
```

### 2. Character Creation

```
Create three test characters:
1. Gon (Hunter x Hunter) - Journeyman tier, approaching Expert
2. Deku (My Hero Academia) - Level 10 Hero class, Base quirk awakening
3. Milestone Hero (custom) - Level 5, milestone-based progression
```

---

## Test Scenarios

### Scenario 1: mastery_tiers - Tier Advancement (NOT Levels)

**Context**: Progression type = "mastery_tiers", NO traditional leveling

#### Test 1.1: Tier Advancement Demonstration
```
Setup:
- Gon: Journeyman tier, 5200/5000 XP (threshold exceeded)
- Quest available: "Demonstrate Expert Mastery to Wing"

Player: "Go to Wing for Expert tier demonstration."

Expected Process:
1. Load tier_system: next_tier = "Expert"
2. Check XP: 5200/5000 (threshold met)
3. Initiate demonstration challenge
4. Execute demonstration (WIS DC 18)
5. On success: advance tier, award bonuses

Expected Output:
"Wing's dojo. He stands ready.

'Your aura has grown. Show me you're ready for Expert tier.'

[DEMONSTRATION CHALLENGE: Expert Tier]
[Requirement: Maintain Ten for 1 hour under pressure]
[WIS Check DC 18]

[Roll: 1d20 + 6 = 19 vs DC 18 - SUCCESS!]

One hour begins. Wing attacks with nen-charged strikes. You maintain Ten PERFECTLY. Not a flicker.

Wing stops. Smiles. 'You pass.'

[TIER ADVANCEMENT: Journeyman → Expert]

NEW TIER BONUSES:
- Attack: +2 → +3
- Defense: +2 → +3
- Aura Control: +3

NEW TECHNIQUES UNLOCKED:
- Gyo (focus aura in eyes to see hidden nen)
- In (conceal aura completely, stealth)
- En (expand aura sphere, detect within 50m)

[Tier XP: 5200 → 200 / 10,000 to Master tier]

Your Nen has EVOLVED. Expert-level control achieved."

Validation:
✅ Tier advancement (Journeyman → Expert), NOT level-up
✅ Demonstration required (WIS DC 18 check)
✅ Tier bonuses upgraded (+3 attack/defense)
✅ New techniques unlocked (Gyo, In, En)
✅ XP reset with overflow (5200 → 200 toward Master)
✅ NO traditional "Level X" mentioned
```

#### Test 1.2: No Traditional Levels
```
Setup:
- Check character sheet after tier advancement

Player: "Show character sheet."

Expected Output:
"GON - Hunter x Hunter

MASTERY TIER: Expert (Tier 4 of 5)
Tier XP: 200 / 10,000 to Master tier

STATS:
- STR: 16 (+3)
- DEX: 18 (+4)
- CON: 15 (+2)
- WIS: 16 (+3)
- INT: 12 (+1)
- CHA: 14 (+2)

TIER BONUSES:
- Attack: +3 (Expert tier)
- Defense: +3 (Expert tier)
- Aura Control: +3 (Expert tier)

NEN TECHNIQUES:
- Ten (learned)
- Ren (learned)
- Zetsu (learned)
- Ko (Journeyman)
- Ken (Journeyman)
- Ryu (Journeyman)
- Gyo (Expert) [NEW]
- In (Expert) [NEW]
- En (Expert) [NEW]

(No 'Level' stat - mastery_tiers uses TIERS, not levels)"

Validation:
✅ Character sheet shows TIER, not level
✅ Tier XP displayed (200/10,000)
✅ Tier bonuses clearly marked
✅ Techniques organized by tier unlock
✅ NO "Level 12" or similar traditional level display
```

#### Test 1.3: Tier 5 (Master) Advancement
```
Setup:
- Gon reaches Master tier threshold (10,000/10,000)

Player: "Demonstrate Master tier mastery."

Expected Output:
"You've reached the pinnacle. Master tier.

Wing: 'There's nothing more I can teach you. You must forge your own path now.'

[DEMONSTRATION CHALLENGE: Master Tier - ULTIMATE TEST]
[Requirement: Create your own unique Nen ability]
[Multiple checks: WIS DC 20, INT DC 18, Creativity demonstration]

[This is the FINAL tier. No tiers beyond Master.]

(Demonstration would be extensive quest, not instant check)

Master tier = PEAK of mastery_tiers progression. You've achieved the highest level of Nen mastery possible."

Validation:
✅ Master tier = final tier (no tiers beyond)
✅ Master demonstration extremely challenging (unique ability creation)
✅ Represents peak mastery, not infinite progression
```

---

### Scenario 2: quirk_awakening + class_based Hybrid - Dual Progression

**Context**: Two progression tracks: general levels (class_based) + quirk awakenings (event-based)

#### Test 2.1: Standard Level-Up (No Quirk Evolution)
```
Setup:
- Deku: Level 10 Hero class, 18,500/20,000 XP
- Gain 2,500 XP from quest

Player: "Complete hero patrol quest (+2500 XP)."

Expected Process:
1. Add XP: 18,500 + 2,500 = 21,000
2. Check threshold: 21,000 >= 20,000 (YES)
3. Level up: 10 → 11
4. Award standard rewards (HP/MP/SP, attribute points)
5. Check class abilities: Level 11 Hero unlock?
6. Quirk awakening stage: UNCHANGED (no awakening event)

Expected Output:
"Hero patrol complete. Experience solidifies.

[+2500 XP]
[XP: 18,500 → 21,000 / 20,000]

[LEVEL UP! Hero Class 10 → 11]

HP: 195 → 205
MP: 160 → 170
SP: 125 → 130

+2 Attribute Points (allocate now)
+1 Skill Point

[Level 11 Hero Ability: NO CLASS ABILITY THIS LEVEL]
(Hero class abilities unlock at specific levels: 1, 3, 5, 7, 10, 13, 15, 17, 20)

[Quirk Awakening Stage: Base (unchanged)]
(Awakenings are EVENT-based, not level-based)

[XP: 1,000 / 26,000 to Level 12]

You're more experienced. Stronger overall. But your quirk hasn't evolved—that requires a dramatic breakthrough.

Allocate attribute points?"

Validation:
✅ Standard level-up (10 → 11)
✅ HP/MP/SP gains (+10/+10/+5)
✅ Attribute and skill points awarded (+2, +1)
✅ Class ability check (none at L11)
✅ Quirk awakening UNCHANGED (no event)
✅ Dual tracks clearly separated
```

#### Test 2.2: Class Ability Unlock (Level-Based)
```
Setup:
- Deku levels from 12 → 13 (Hero class ability level)

Player: "Level up to 13."

Expected Process:
1. Standard level-up sequence
2. Check class_abilities: Level 13 Hero = new ability
3. Unlock and announce class ability

Expected Output:
"[LEVEL UP! Hero Class 12 → 13]

HP: 215 → 225
MP: 180 → 190
SP: 135 → 140

+2 Attribute Points
+1 Skill Point

[NEW CLASS ABILITY: One For All - Full Cowl 15%]
You can now sustain 15% of One For All's power continuously (was 10%).
- +3 STR, +3 DEX while active
- 20 MP/minute to sustain
- Combat mobility greatly enhanced

'Plus Ultra!' This is what All Might trained you for.

[Quirk Awakening Stage: Base (still unchanged)]

Your control has improved through training and experience. This is CLASS progression.

Quirk AWAKENING would require a dramatic event—near-death, emotional breakthrough, or limit break."

Validation:
✅ Class ability unlocked at specific level (13)
✅ Ability described clearly (Full Cowl 15%)
✅ Mechanical benefits stated (+3 STR/DEX)
✅ Cost/duration specified (20 MP/min)
✅ Quirk awakening still separate track
```

#### Test 2.3: Quirk Awakening (Event-Based, Independent of Level)
```
Setup:
- Deku: Level 13
- Combat vs overwhelming villain
- HP drops to 8% (near-death trigger)
- Emotional stakes: Mentor watching, must prove self

Player: "Push past limits to save mentor!"

Expected Process:
1. Detect awakening trigger: near-death (HP < 10%)
2. Check emotional context: high stakes (mentor danger)
3. Initiate awakening event
4. Complete awakening: Base → Awakened
5. Award new abilities (quirk evolution)
6. Award awakening bonus XP (+2000)
7. Level stays 13 (awakening ≠ level-up)

Expected Output:
"Villain's fist CONNECTS. Ribs SHATTER. [HP: 35 → 18 / 225 = 8%]

All Might watching. Bleeding. 'Young Midoriya... run...'

NO. You're his SUCCESSOR. You HAVE to save him.

10% Full Cowl isn't enough. 15%... still not enough.

'Only one option. GO BEYOND!'

[AWAKENING TRIGGER: Near-Death (8% HP) + Emotional Breakthrough (All Might danger)]

20%! Aura EXPLODES. But... different. Not just more power. REFINED power. CONTROLLED power.

[QUIRK AWAKENING: One For All → One For All: Mastered Output]

NEW ABILITIES:
- Full Cowl 20% (sustained, minimal strain)
- Air Pressure Attacks (Detroit Smash shockwaves)
- Blackwhip (tendrils of power, restraint/mobility)

[Awakening Bonus: +2000 XP]
[Character Level: STILL 13 (awakening ≠ level)]

This isn't about gaining experience. This is TRANSFORMATION. Your quirk has EVOLVED.

[Quirk Awakening Stage: Base → Awakened]"

Validation:
✅ Awakening triggered by EVENT, not level
✅ Level stays 13 (awakening independent)
✅ New abilities granted (quirk-specific)
✅ Awakening bonus XP awarded (+2000)
✅ Quirk stage updated (Base → Awakened)
✅ Dual tracks work independently
```

---

### Scenario 3: milestone_based - Story-Driven Leveling

**Context**: Progression type = "milestone_based", minimal combat XP, massive story milestone XP

#### Test 3.1: Minimal Combat XP
```
Setup:
- Milestone Hero: Level 5, 3000/5500 XP
- Combat: Defeat 5 bandits (would be 500 XP standard)

Player: "Defeat bandit group."

Expected Process:
1. Load progression config: type = "milestone_based"
2. Calculate base XP: 500 (5 bandits × 100)
3. Apply milestone reduction: 500 × 0.1 = 50 XP
4. Award minimal XP

Expected Output:
"Bandits scatter. Too easy.

[Combat XP: +50 (base 500 × 0.1 milestone reduction)]

You're not getting stronger from this. These fights are beneath you.

[XP: 3000 → 3050 / 5500 to Level 6]

Real growth comes from CHALLENGES. From TRIALS. From facing the impossible.

Grinding weak enemies won't make you stronger in this world."

Validation:
✅ Combat XP reduced drastically (500 → 50)
✅ milestone_based multiplier applied (0.1×)
✅ Narrative discourages grinding
✅ Emphasizes story-driven growth
```

#### Test 3.2: Major Story Milestone (Direct Level Grant)
```
Setup:
- Milestone Hero: Level 5
- Complete major arc: "Defeat Warlord, Save Village"

Player: "Complete Defeat Warlord arc."

Expected Process:
1. Detect milestone completion: major arc
2. Load milestone rewards: direct_level_grant = 2 levels
3. Award levels directly (no XP calculation)
4. Execute level-up sequence twice

Expected Output:
"The warlord falls. Village saved. Hundreds of lives preserved.

You feel... TRANSFORMATION. Not gradual growth. LEAP.

The ordeal FORGED you. Tested your limits. Broke through barriers.

[MAJOR MILESTONE COMPLETE: Warlord Defeated, Village Saved]

[LEVEL JUMP: 5 → 6 → 7 (Double level-up from milestone!)]

Level 5 → 6:
- HP: 145 → 155
- MP: 120 → 130
- SP: 100 → 105
- +2 Attribute Points

Level 6 → 7:
- HP: 155 → 165
- MP: 130 → 140
- SP: 105 → 110
- +2 Attribute Points

Total gains:
- HP: 145 → 165 (+20)
- MP: 120 → 140 (+20)
- SP: 100 → 110 (+10)
- +4 Attribute Points total
- +2 Skill Points total

[XP: 3050 → 0 / 15,000 to Level 8]
(Milestone bypassed XP thresholds entirely)

THIS is how you grow. Not grinding. STORY. Facing impossible odds and WINNING."

Validation:
✅ Direct level grant (2 levels)
✅ No XP calculation (milestone bypasses)
✅ Multiple level-ups executed (5 → 6 → 7)
✅ All rewards awarded for both levels
✅ XP reset to 0 (milestone doesn't add XP)
✅ Narrative celebrates achievement
```

#### Test 3.3: Mixed XP Sources (Combat vs Milestone)
```
Setup:
- Session with combat and story milestone

Session activities:
1. Combat throughout session: 1000 XP base
2. Milestone at end: Major story beat

Player: "Complete session."

Expected Output:
"Session Summary:

COMBAT XP:
- Defeated various enemies: 1000 base XP
- Milestone reduction (×0.1): 100 XP awarded

MILESTONE XP:
- Completed Major Story Beat (Saved Kingdom): +5000 XP

[Total XP Gained: 5100]
[XP: 0 → 5100 / 15,000 to Level 8]

The combat barely mattered. Weak enemies, easy fights.

But SAVING THE KINGDOM? That changed you. That's real growth.

In this world, power comes from MEANING, not grinding."

Validation:
✅ Combat XP minimal (1000 → 100)
✅ Milestone XP massive (5000)
✅ Clear contrast emphasized
✅ Total correctly calculated (100 + 5000)
✅ Narrative reinforces milestone philosophy
```

---

## Integration Validation Checks

### Check 1: Progression Type Routing
```
Test: Verify correct leveling system by type.

mastery_tiers: Tier advancement, NO traditional levels
class_based: Standard levels + class abilities
quirk_awakening: Levels + event-based awakenings (dual track)
milestone_based: Levels via story milestones, minimal combat XP
static_op: NO leveling ever

Expected Result:
✅ Each type uses correct leveling mechanics
✅ No cross-contamination (mastery_tiers doesn't show "Level X")
✅ Type-specific rewards applied
```

### Check 2: Demonstration Requirements
```
Test: mastery_tiers tier advancement with/without demonstration.

With demonstration_required = true:
- Reach XP threshold → Quest to demonstrate → Tier advance

Without (demonstration_required = false):
- Reach XP threshold → Instant tier advance

Expected Result:
✅ Demonstration requirement enforced when true
✅ Auto-advance when false (rare)
✅ Demonstration quests appropriate difficulty
```

### Check 3: Dual Track Independence
```
Test: quirk_awakening level-up and awakening independence.

Scenario 1: Level 10 → 11, no awakening → Level changes, quirk stage UNCHANGED
Scenario 2: Awakening event at L13 → Quirk stage changes, level UNCHANGED
Scenario 3: Level-up AND awakening (same session) → Both tracks advance independently

Expected Result:
✅ Levels and awakenings tracked separately
✅ Level-up doesn't trigger awakening
✅ Awakening doesn't grant levels (except bonus XP)
✅ Both can occur in same session independently
```

### Check 4: Milestone XP vs Combat XP
```
Test: milestone_based XP sources comparison.

Combat XP: 1000 base × 0.1 = 100 XP
Milestone XP: Major arc = 5000 XP (50× more)

Expected Result:
✅ Combat XP drastically reduced (0.1× multiplier)
✅ Milestone XP massive (5000+)
✅ Clear incentive for story progression over grinding
✅ Narrative emphasizes difference
```

---

## Success Criteria

Test PASSES if:
1. ✅ mastery_tiers advances TIERS (not levels), demonstration required
2. ✅ mastery_tiers character sheet shows tier, NOT level
3. ✅ class_based unlocks class abilities at specific levels
4. ✅ quirk_awakening has dual tracks (levels + awakenings) working independently
5. ✅ Awakenings triggered by EVENTS, not levels
6. ✅ milestone_based awards minimal combat XP (0.1×)
7. ✅ milestone_based grants direct levels from story milestones
8. ✅ static_op NEVER levels up (would be tested if profile available)
9. ✅ All leveling reads from session_state.mechanical_systems.progression
10. ✅ No progression type cross-contamination

---

## Test Execution Log

**Tester**: ____________  
**Date**: ____________  
**AIDM Version**: ____________

### Results Summary

| Test | Type | Status | Notes |
|------|------|--------|-------|
| 1.1 Tier Demonstration | mastery_tiers | ⬜ PASS / ⬜ FAIL | |
| 1.2 No Traditional Levels | mastery_tiers | ⬜ PASS / ⬜ FAIL | |
| 1.3 Master Tier | mastery_tiers | ⬜ PASS / ⬜ FAIL | |
| 2.1 Standard Level-Up | quirk_awakening | ⬜ PASS / ⬜ FAIL | |
| 2.2 Class Ability Unlock | quirk_awakening | ⬜ PASS / ⬜ FAIL | |
| 2.3 Event Awakening | quirk_awakening | ⬜ PASS / ⬜ FAIL | |
| 3.1 Minimal Combat XP | milestone_based | ⬜ PASS / ⬜ FAIL | |
| 3.2 Milestone Level Grant | milestone_based | ⬜ PASS / ⬜ FAIL | |
| 3.3 Mixed XP Sources | milestone_based | ⬜ PASS / ⬜ FAIL | |

**Overall Result**: ⬜ PASS / ⬜ FAIL

**Issues Found**:
_______________________________________________
_______________________________________________
_______________________________________________

**Recommendations**:
_______________________________________________
_______________________________________________
_______________________________________________
