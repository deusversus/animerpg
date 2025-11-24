# TEST-11: Downtime Integration

**Test Type**: Mechanical Integration Validation  
**Focus**: Module 05 downtime system integration with narrative profiles  
**Duration**: 60-90 minutes  
**Profiles Used**: Hunter x Hunter, Konosuba, My Hero Academia

---

## Test Objective

Validate that Module 05 (Narrative Systems) correctly reads and applies downtime configurations from `session_state.mechanical_systems.downtime` for different enabled_modes:
1. **training_arcs + investigation** (Hunter x Hunter)
2. **slice_of_life + training_arcs** (Konosuba)
3. **training_arcs + social_links** (My Hero Academia)

---

## Pre-Test Setup

### 1. Session Zero Phase 3 Execution

```
AIDM: Run Session Zero Phase 3 for each profile to instantiate mechanical systems.

Profile 1: Hunter x Hunter
Profile 2: Konosuba
Profile 3: My Hero Academia

Expected output:
- session_state.mechanical_systems.downtime loaded
- enabled_modes array populated
- activity_configs for each mode loaded
```

### 2. Character Creation

```
Create three test characters:
1. Gon (Hunter x Hunter) - Nen user, bounty hunter
2. Kazuma (Konosuba) - Adventurer, party leader
3. Deku (My Hero Academia) - Hero student, provisional license
```

---

## Test Scenarios

### Scenario 1: Hunter x Hunter - Training + Investigation

**Context**: Enabled modes: `["training_arcs", "investigation"]`

#### Test 1.1: Downtime Activity Offering
```
Player: "What can I do during downtime?"

Expected Process:
1. Load enabled_modes: ["training_arcs", "investigation"]
2. Load activity_configs for both modes
3. Present only enabled activities

Expected Output:
"Yorknew City. Quest complete. Downtime available.

ACTIVITIES:

1. TRAINING (training_arcs):
   - Nen mastery with Wing (2 weeks, WIS DC 16, +1.5× skill XP)
   - Solo aura control (1 week, WIS DC 14, +1.0× skill XP)

2. INVESTIGATION (investigation):
   - Track Phantom Troupe rumors (3 days, Perception DC 16, deep intel)
   - Research auction security (1 day, Investigation DC 12, moderate intel)

Choose activity?"

Validation:
✅ Only enabled modes offered (training_arcs, investigation)
✅ NO slice_of_life offered (not in enabled_modes)
✅ Activity configs show time requirements, DCs, benefits
```

#### Test 1.2: Training Arc Execution
```
Player: "Train Nen mastery with Wing (2 weeks)."

Expected Process:
1. Load training_arcs config:
   - time_requirements: "2 weeks intensive"
   - success_criteria: "WIS DC 16"
   - skill_progression_rate: 1.5
   - special_conditions: "Nen master required"
2. Execute WIS check
3. Calculate skill XP: base (200) × rate (1.5) = 300 XP
4. Award XP, narrate training

Expected Output:
"Wing's dojo. Two weeks intensive training.

[WIS Check: 1d20 + 6 = 18 vs DC 16 - SUCCESS!]

Day 1: Wing demonstrates Ken. 'Maintain aura across entire body. FOCUS.'

Week 1: Struggling. Aura keeps concentrating in hands. Frustrating.

Week 2: CLICKS. Whole body glowing. Wing nods. 'You've got it.'

[+300 Nen XP (base 200 × 1.5 master bonus)]
[Nen: 450/700 XP to next level]

[2 weeks pass]"

Validation:
✅ Time requirement enforced (2 weeks)
✅ WIS DC 16 check executed
✅ Skill progression rate (1.5×) applied
✅ Narrative matches training_arcs style (progression beats)
✅ Special condition met (Nen master = Wing)
```

#### Test 1.3: Investigation Execution (Success)
```
Player: "Investigate Phantom Troupe rumors (3 days)."

Expected Process:
1. Load investigation config:
   - investigation_types: ["physical_clues", "witness_interviews"]
   - skill_checks: "Perception DC 16"
   - information_depth: "deep"
2. Execute Perception check
3. Reveal intel based on success

Expected Output:
"Three days. Slum informants. Auction rumors.

[Perception Check: 1d20 + 5 = 19 vs DC 16 - SUCCESS!]

Day 1: Street contacts mention 'Spiders coming.'
Day 2: Witness saw member near auction house. Tall, spider tattoo on back.
Day 3: Pattern emerges: September 1st. Underground Auction. ALL members.

[INTEL GAINED - DEEP]:
- Phantom Troupe targeting Sept 1st Underground Auction
- Full member attendance expected
- Auction items: Rare artifacts, cursed objects
- Security: Mafia + hired Nen users

[New Quest Hook: Stop Phantom Troupe Heist]

[3 days pass]"

Validation:
✅ Investigation type used (physical_clues, witness_interviews)
✅ Perception DC 16 check executed
✅ Information depth "deep" (full intel revealed)
✅ Intel actionable (quest hook unlocked)
```

#### Test 1.4: Investigation Execution (Failure)
```
Player: "Investigate different target (Perception DC 18)."

Expected Process:
1. Execute Perception check (fail)
2. Reveal superficial intel only

Expected Output:
"Two days. Following leads. Dead ends.

[Perception Check: 1d20 + 5 = 11 vs DC 18 - FAIL]

Informants scared. Won't talk. You're asking the wrong questions.

[INTEL GAINED - SUPERFICIAL]:
- Target was seen in East District (vague)
- No specifics on timing or plans

Need better sources or more time.

[2 days pass, minimal progress]"

Validation:
✅ Failed check = superficial intel only
✅ Narrative acknowledges failure
✅ Time still passes (cost paid)
```

---

### Scenario 2: Konosuba - Slice of Life + Training

**Context**: Enabled modes: `["slice_of_life", "training_arcs"]`

#### Test 2.1: Slice of Life Activity
```
Player: "Hang out at guild pub."

Expected Process:
1. Load slice_of_life config:
   - available_activities: ["guild_quests", "pub_drinking", "shopping", "festivals"]
   - relationship_impact: 1.5
   - narrative_style: "comedic"
2. Execute activity with comedic beats
3. Award affinity with multiplier

Expected Output:
"Axel Guild. Evening. Aqua SLAMS mug on table.

'ANOTHER ROUND!' [Already drunk]

Kazuma sighs. 'We're BROKE because of you...'

Darkness: 'The ale here is EXQUISITE suffering!' [Blushing at 'insults' from patron]

Megumin: 'I shall drink... water. (We're poor.)'

[Hours blur. Aqua crying about debt. Kazuma calculating. Darkness enjoying being ignored. Megumin asleep on table.]

Bartender: 'That'll be 50 Eris. On credit. AGAIN.'

[Affinity +15 (base 10 × 1.5 comedic multiplier): Aqua, Darkness, Megumin]
[Comedy beats: 4 | Relationship development: Strong]
[Currency: -50 Eris (more debt...)]

[4 hours pass]"

Validation:
✅ Slice_of_life mode enabled
✅ Narrative style "comedic" (chaos, party interactions)
✅ Relationship impact 1.5× multiplier applied (10 → 15 affinity)
✅ Multiple party members affected
✅ Comedic beats throughout
```

#### Test 2.2: Training Arc (Grinding)
```
Player: "Train magic with Megumin (1 week)."

Expected Process:
1. Load training_arcs config:
   - time_requirements: "1 week grinding"
   - success_criteria: "INT DC 14"
   - skill_progression_rate: 1.0 (standard)
   - special_conditions: "none (self-motivated)"
2. Execute INT check
3. Award XP with comedic narrative

Expected Output:
"Training grounds. Megumin: 'I shall teach you the glory of EXPLOSION!'

Kazuma: 'Can you teach something USEFUL? Like basic fire magic?'

Megumin: 'NO. EXPLOSION IS SUPREME.'

[INT Check: 1d20 + 4 = 16 vs DC 14 - SUCCESS!]

Week of practice. You learn explosion magic. It's INCREDIBLY powerful.

It also costs ALL your MP. You can cast it ONCE per day. Then collapse.

Megumin: 'Perfect! You understand!'

Kazuma: 'This is TERRIBLE design!'

[+200 Explosion Magic XP]
[NEW SKILL: Explosion (1/day, massive AOE damage, costs all MP, user incapacitated)]

[1 week pass]"

Validation:
✅ Training_arcs mode enabled
✅ Time requirement (1 week) enforced
✅ Success criteria (INT DC 14) checked
✅ Skill progression standard (1.0×)
✅ Narrative maintains comedic tone (Konosuba style)
```

#### Test 2.3: Disabled Mode Check
```
Player: "Investigate the demon king's movements."

Expected Process:
1. Check enabled_modes: ["slice_of_life", "training_arcs"]
2. Investigation NOT enabled
3. Refuse or redirect

Expected Output:
"Investigation? That's... not really this party's strength.

Aqua: 'We don't DO detective work! We blow things up!'

Megumin: 'EXPLOSION!'

Darkness: 'Or get captured and interrogated...' [Excited]

Maybe stick to guild quests and training? (Investigation not available in this world's style.)"

Validation:
✅ Disabled mode (investigation) NOT offered
✅ AIDM redirects to enabled modes
✅ Narrative acknowledges party's approach
```

---

### Scenario 3: My Hero Academia - Training + Social Links

**Context**: Enabled modes: `["training_arcs", "social_links"]`

#### Test 3.1: Training Arc (Quirk Mastery)
```
Player: "Train quirk at UA gym (1 week)."

Expected Process:
1. Load training_arcs config:
   - time_requirements: "1 week intensive"
   - success_criteria: "CON DC 15"
   - skill_progression_rate: 1.25 (UA facility bonus)
   - special_conditions: "UA gym access"
2. Execute CON check
3. Apply facility bonus

Expected Output:
"UA Training Gym. State-of-art equipment. All Might poster watching.

[CON Check: 1d20 + 5 = 17 vs DC 15 - SUCCESS!]

Week of intensive quirk training:
- Day 1-3: Full Cowl stability exercises. Maintaining 8% consistently.
- Day 4-5: Power output drills. Breaking concrete dummies.
- Day 6-7: Combat scenarios with training bots.

Aizawa observes. 'Control improving. Keep it up.'

[+250 Quirk Mastery XP (base 200 × 1.25 UA facility bonus)]
[One For All control: 8% → 10% sustained]

[1 week pass]"

Validation:
✅ Training_arcs mode enabled
✅ UA facility bonus applied (1.25×)
✅ Special condition met (UA gym access)
✅ Narrative matches MHA style (heroic, training montage)
```

#### Test 3.2: Social Link Progression
```
Player: "Hang out with Todoroki (social link activity)."

Expected Process:
1. Load social_links config:
   - link_progression: "tiers"
   - activity_types: ["training_together", "conversations"]
   - unlock_bonuses: "+5% skill XP at Tier 3"
2. Load Todoroki current link: Tier 2, 60/100
3. Execute activity (conversation)
4. Award progress

Expected Output:
"School rooftop. Lunch break. Todoroki stares at horizon.

You: 'How's your father?'

Long silence. 'I hate him. But... I'm becoming like him. Cold. Obsessed.'

Voice cracks. 'Is that... inevitable?'

[Insight Check: 1d20 + 4 = 15 vs DC 12 - SUCCESS!]

You see it: not hatred. Fear. Fear of losing himself.

You: 'You're not him. You CHOOSE warmth. Every day, you choose differently.'

He looks at you. Nods slowly. 'Thanks. I needed to hear that.'

[Social Link: Todoroki - Tier 2, 85/100 (+25 progress)]
[Relationship: Close Friend]

[Activity complete]"

Validation:
✅ Social_links mode enabled
✅ Tier progression tracked (60 → 85/100)
✅ Activity type "conversation" used
✅ Insight check for understanding
✅ Progress toward Tier 3 unlock bonus
```

#### Test 3.3: Social Link Tier-Up
```
Player: "Continue social link activities until Tier 3."

Expected Process:
1. Complete activity: 85 + 20 = 105/100
2. Tier up: 2 → 3
3. Unlock bonus: +5% skill XP when training together

Expected Output:
"Training session with Todoroki. Quirk sparring.

Both pushing limits. Ice vs One For All. You're matching his output now.

Todoroki: 'You've gotten stronger. Let's push each other further.'

[Social Link: Todoroki - TIER UP! 2 → 3]
[NEW BOND: Close Friend → Trusted Rival]

[BONUS UNLOCKED: Training Together (+5% skill XP when training with Todoroki)]

Your rivalry pushes both of you to improve."

Validation:
✅ Tier progression system works (2 → 3)
✅ Unlock bonus granted (+5% skill XP)
✅ Narrative celebrates tier-up
✅ Mechanical benefit clearly stated
```

---

## Integration Validation Checks

### Check 1: Enabled Modes Only
```
Test: Attempt to use disabled mode in each profile.

Profile 1 (HxH): Try slice_of_life (NOT enabled)
Profile 2 (Konosuba): Try investigation (NOT enabled)
Profile 3 (MHA): Try investigation (NOT enabled)

Expected Result:
✅ AIDM refuses or redirects
✅ Only enabled_modes offered
✅ No hardcoded "you can do X" for disabled modes
```

### Check 2: Activity Config Application
```
Test: Same activity (training) in different profiles with different configs.

HxH training: 2 weeks, WIS DC 16, 1.5× XP (master bonus)
Konosuba training: 1 week, INT DC 14, 1.0× XP (standard)
MHA training: 1 week, CON DC 15, 1.25× XP (facility bonus)

Expected Result:
✅ Different time requirements enforced
✅ Different DCs checked
✅ Different XP multipliers applied
✅ Configs read from session_state, not hardcoded
```

### Check 3: Special Mechanics
```
Test: Profile-specific special mechanics applied.

HxH: Hunter License → investigation intel +1 depth (moderate → deep)
Konosuba: Party chaos → slice_of_life 50% comedic disaster chance
MHA: Hero license requirements → patrol downtime mandatory

Expected Result:
✅ Special mechanics applied during activities
✅ Profile-specific rules enforced
✅ Mechanical benefits/consequences function
```

### Check 4: Time Passage
```
Test: Verify time costs enforced.

Activity 1: 2 weeks training → 2 weeks pass in-game
Activity 2: 3 days investigation → 3 days pass
Activity 3: 4 hours slice_of_life → 4 hours pass

Expected Result:
✅ Time passage narrated
✅ World state updated (time-sensitive events may progress)
✅ No "instant" downtime (costs matter)
```

---

## Success Criteria

Test PASSES if:
1. ✅ Only enabled_modes offered to player (no disabled modes)
2. ✅ Activity configs correctly applied (time, DCs, XP rates)
3. ✅ Profile-specific narratives match style:
   - HxH: serious training, tactical investigation
   - Konosuba: comedic chaos, party bonding
   - MHA: heroic training, deep relationships
4. ✅ Special mechanics function (Hunter License, party chaos, facility bonuses)
5. ✅ Social links track progression (tiers, unlock bonuses)
6. ✅ Time costs enforced (activities take time)
7. ✅ Session start validation catches missing config
8. ✅ Failed checks have consequences (superficial intel, partial XP)

---

## Test Execution Log

**Tester**: ____________  
**Date**: ____________  
**AIDM Version**: ____________

### Results Summary

| Test | Profile | Status | Notes |
|------|---------|--------|-------|
| 1.1 Activity Offering | HxH | ⬜ PASS / ⬜ FAIL | |
| 1.2 Training Arc | HxH | ⬜ PASS / ⬜ FAIL | |
| 1.3 Investigation Success | HxH | ⬜ PASS / ⬜ FAIL | |
| 1.4 Investigation Fail | HxH | ⬜ PASS / ⬜ FAIL | |
| 2.1 Slice of Life | Konosuba | ⬜ PASS / ⬜ FAIL | |
| 2.2 Training | Konosuba | ⬜ PASS / ⬜ FAIL | |
| 2.3 Disabled Mode | Konosuba | ⬜ PASS / ⬜ FAIL | |
| 3.1 Quirk Training | MHA | ⬜ PASS / ⬜ FAIL | |
| 3.2 Social Link | MHA | ⬜ PASS / ⬜ FAIL | |
| 3.3 Social Tier-Up | MHA | ⬜ PASS / ⬜ FAIL | |

**Overall Result**: ⬜ PASS / ⬜ FAIL

**Issues Found**:
_______________________________________________
_______________________________________________
_______________________________________________

**Recommendations**:
_______________________________________________
_______________________________________________
_______________________________________________
