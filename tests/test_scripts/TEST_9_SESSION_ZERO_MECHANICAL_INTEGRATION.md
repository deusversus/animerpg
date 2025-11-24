# TEST-9: SESSION ZERO MECHANICAL SYSTEMS INTEGRATION

**Version**: 1.0  
**Priority**: HIGH  
**Type**: Integration Test  
**Duration**: 30-45 minutes

## Purpose

Validate that Session Zero Phase 3: MECHANICAL BUILD correctly integrates the mechanical instantiation system to load economy, crafting, progression, and downtime systems from narrative profiles.

## Test Scope

**In Scope**:
- Profile loading in Session Zero Phase 0.5
- Mechanical system extraction from profile config
- MechanicalInstantiator.load_from_profile() execution
- System display to player
- Storage in session state
- Module 03 access to instantiated systems

**Out of Scope**:
- Full character creation workflow (covered in TEST-1)
- Combat mechanics (covered in TEST-4)
- Anime research protocol (covered in TEST-8)

## Prerequisites

**Required Files**:
- `aidm/instructions/06_session_zero.md` (Session Zero with Phase 3 integration)
- `aidm/instructions/00_system_initialization.md` (Module 00 with mechanical_instantiation in Tier 1)
- `aidm/lib/mechanical_instantiation.py` (instantiation system)
- `aidm/schemas/economy_meta_schema.json`
- `aidm/schemas/crafting_meta_schema.json`
- `aidm/schemas/progression_meta_schema.json`
- `aidm/schemas/downtime_meta_schema.json`
- `aidm/libraries/narrative_profiles/hunter_x_hunter.md` (test profile 1)
- `aidm/libraries/narrative_profiles/my_hero_academia.md` (test profile 2)
- `aidm/libraries/narrative_profiles/konosuba.md` (test profile 3)

**System State**: Fresh AIDM instance, no active session

## Test Cases

### TC-9.1: Mechanical System Loading (Hunter x Hunter)

**Setup**:
1. Start new AIDM session
2. Begin Session Zero
3. Select Hunter x Hunter narrative profile in Phase 0.5

**Execution**:
```
Player: "I want to start a new game in the Hunter x Hunter universe."

Expected AI Response:
- Phase 0: Research Hunter x Hunter
- Phase 0.5: Load hunter_x_hunter.md profile
- Phase 1-2: Character creation (name, concept)
- Phase 3: Display mechanical systems

Expected Phase 3 Output:
"Based on your Hunter x Hunter narrative profile, I've configured:

ECONOMY: Fiat Currency (Jenny)
• Starting amount: 200 Jenny
• Scarcity: Normal
• Transactions: Standard merchant system
• Special: Hunter License privileges

CRAFTING: Skill-Based (Nen abilities)
• Focus: Hatsu development
• Skill stat: INT (understanding Nen principles)
• Quality tiers: Novice → Master
• Special: Conditions & Restrictions system

PROGRESSION: Mastery Tiers (Nen System)
• Levels: Initiation → Practitioner → User → Master → Beyond Human
• Categories: Enhancement, Transmutation, Emission, Manipulation, Conjuration, Specialization
• Advancement: Training arcs + combat experience

DOWNTIME: Training Arcs + Investigation
• Training: Develop new Hatsu techniques, increase aura output
• Investigation: Track targets, gather intelligence
• Special: Water divination to determine Nen type

Does this match your expectations, or would you like to adjust anything?"
```

**Validation Checkpoints**:
- ✅ Profile loaded correctly in Phase 0.5
- ✅ mechanical_instantiation.py executed
- ✅ Economy system: fiat_currency (Jenny, 200 starting)
- ✅ Crafting system: skill_based (INT, Hatsu development)
- ✅ Progression system: mastery_tiers (6 categories)
- ✅ Downtime system: training_arcs + investigation
- ✅ Systems stored in session state
- ✅ Player offered customization option

**Pass Criteria**: All 4 systems displayed correctly with Hunter x Hunter specifics

---

### TC-9.2: Different System Combination (My Hero Academia)

**Setup**:
1. Start new AIDM session
2. Begin Session Zero
3. Select My Hero Academia narrative profile

**Execution**:
```
Player: "Let's do a My Hero Academia campaign."

Expected Phase 3 Output:
"Based on your My Hero Academia narrative profile, I've configured:

ECONOMY: Fiat Currency (Yen)
• Starting amount: 50,000 yen
• Scarcity: Normal
• Transactions: UA budget + hero salary
• Special: Hero ranking affects income

CRAFTING: Experimental (Support Items)
• Focus: Quirk-enhancing gear
• Resources: Tech components, rare materials
• Success: Roll-based with complications
• Special: UA Support Course access

PROGRESSION: Quirk Awakening
• Levels: Discovery → Basic Control → Plus Ultra → Awakening
• Quirk Types: Emitter, Transformation, Mutant
• Advancement: Combat experience + training
• Special: Quirk evolution events

DOWNTIME: Training Arcs + Slice of Life
• Training: Quirk mastery, physical conditioning
• Slice of Life: School events, hero internships
• Special: UA class dynamics

Does this match your expectations, or would you like to adjust anything?"
```

**Validation Checkpoints**:
- ✅ Profile loaded: my_hero_academia.md
- ✅ Economy: fiat_currency (yen, 50000 starting)
- ✅ Crafting: experimental (support items)
- ✅ Progression: quirk_awakening
- ✅ Downtime: training_arcs + slice_of_life
- ✅ Different systems from TC-9.1 (validates profile-specific loading)

**Pass Criteria**: All 4 systems match MHA profile configuration

---

### TC-9.3: Minimal Systems (Konosuba)

**Setup**:
1. Start new AIDM session
2. Begin Session Zero
3. Select Konosuba narrative profile

**Execution**:
```
Player: "I want a comedic Konosuba-style adventure."

Expected Phase 3 Output:
"Based on your Konosuba narrative profile, I've configured:

ECONOMY: Fiat Currency (Eris)
• Starting amount: 0 eris (you're broke!)
• Scarcity: High (debt is a constant threat)
• Transactions: Quest rewards, gambling
• Special: Debt accumulation mechanic

CRAFTING: None
• Equipment: Purchase from merchants or quest rewards
• Special: No crafting (you're too incompetent)

PROGRESSION: Class-Based (Adventurer Card)
• Classes: Crusader, Arch Wizard, Thief, etc.
• Levels: 1-99 (grinding required)
• Advancement: XP from quests + monster kills
• Special: Skill points for learning class abilities

DOWNTIME: Slice of Life + Training Arcs
• Slice of Life: Guild quests, pub drinking, gambling
• Training: Level grinding (often interrupted by chaos)
• Special: Random comedy encounters

Does this match your expectations, or would you like to adjust anything?"
```

**Validation Checkpoints**:
- ✅ Profile loaded: konosuba.md
- ✅ Economy: fiat_currency (eris, 0 starting, high scarcity)
- ✅ Crafting: none (validated as valid system type)
- ✅ Progression: class_based (adventurer card)
- ✅ Downtime: slice_of_life + training_arcs
- ✅ Profile-specific flavors (debt, incompetence, comedy)

**Pass Criteria**: Systems match Konosuba profile including "none" crafting

---

### TC-9.4: Player Customization

**Setup**:
1. Complete TC-9.1 (Hunter x Hunter profile loaded)
2. Player wants to modify systems

**Execution**:
```
Player: "Actually, I don't want the investigation downtime mode. Can we do faction building instead?"

Expected AI Response:
"Of course! I'll update your downtime modes:

DOWNTIME: Training Arcs + Faction Building
• Training: Develop new Hatsu techniques, increase aura output
• Faction Building: Build Hunter organization, recruit members
• Special: Hunter License network connections

Updated configuration saved. Continue to starting skills?"
```

**Validation Checkpoints**:
- ✅ AI recognizes customization request
- ✅ Downtime system updated (investigation → faction_building)
- ✅ New configuration validated with meta-schema
- ✅ Other systems unchanged (economy, crafting, progression)
- ✅ Session state updated with modified systems

**Pass Criteria**: Customization works, validation passes, systems updated

---

### TC-9.5: No Profile Baseline Systems

**Setup**:
1. Start new AIDM session
2. Begin Session Zero
3. Skip anime profile selection (use baseline)

**Execution**:
```
Player: "I want an original fantasy setting, no anime."

Expected Phase 3 Output:
"Since you're not using a narrative profile, I've configured baseline systems:

ECONOMY: Fiat Currency (Gold)
• Starting amount: 200 gold
• Scarcity: Normal
• Transactions: Standard merchants
• Special: None

CRAFTING: None
• Equipment: Purchase from merchants
• Special: No crafting available

PROGRESSION: Class-Based
• Classes: Warrior, Mage, Rogue
• Levels: 1-20
• Advancement: XP from combat/quests
• Special: None

DOWNTIME: Training Arcs + Social Links
• Training: Improve skills, learn abilities
• Social Links: Build NPC relationships
• Special: None

Does this work, or would you like to customize?"
```

**Validation Checkpoints**:
- ✅ No profile loaded (active_narrative_profile = None)
- ✅ Baseline systems loaded instead
- ✅ Economy: simple fiat_currency (gold, 200)
- ✅ Crafting: none
- ✅ Progression: class_based (warrior/mage/rogue)
- ✅ Downtime: training_arcs + social_links
- ✅ Player offered customization

**Pass Criteria**: Baseline systems work without profile, customization offered

---

### TC-9.6: Gameplay Integration Preview (Module 03 Economy)

**Setup**:
1. Complete TC-9.1 (Hunter x Hunter with Jenny currency)
2. Finish Session Zero character creation
3. Enter gameplay (Session 1)

**Execution**:
```
Player: "I go to the market to buy a sword."

Expected AI Response:
"You arrive at the Yorknew City marketplace. A merchant displays various weapons.

AVAILABLE WEAPONS:
- Iron Sword (1d8 damage) - 40 Jenny
- Steel Longsword (1d10 damage) - 80 Jenny
- Hunter's Blade (1d8+2, lightweight) - 120 Jenny

You have 200 Jenny. What do you buy?"

[Player buys Iron Sword for 40 Jenny]

Expected AI Response:
"Transaction complete. You pay 40 Jenny and receive the Iron Sword.

UPDATED INVENTORY:
- Iron Sword (1d8 damage)

CURRENT MONEY: 160 Jenny remaining"
```

**Validation Checkpoints**:
- ✅ Module 03 State Manager loaded
- ✅ Module 03 accesses instantiated economy system
- ✅ Currency displayed: Jenny (from Hunter x Hunter profile)
- ✅ Transaction uses correct currency
- ✅ Starting amount correct (200 Jenny)
- ✅ Deduction correct (200 - 40 = 160)
- ✅ No errors or fallback to generic "gold"

**Pass Criteria**: Module 03 uses instantiated currency throughout transaction

**NOTE**: TC-9.6 is a PREVIEW of gameplay integration. For comprehensive validation of Modules 03/05/08/09 using instantiated systems throughout gameplay, see **PART 2: GAMEPLAY VALIDATION** below.

---

## Integration Points

**Module 00 → mechanical_instantiation.py**:
- Tier 1 loading: mechanical_instantiation in always-loaded modules
- Schema validation: 4 meta-schemas (economy, crafting, progression, downtime)
- Health check: mechanical instantiation marked as critical

**Module 06 → mechanical_instantiation.py**:
- Phase 0.5: Narrative profile loaded (existing)
- Phase 3: Extract mechanical config from active_narrative_profile
- Phase 3: Execute MechanicalInstantiator.load_from_profile()
- Phase 3: Display systems to player
- Phase 3: Store in session state

**Module 06 → Module 03**:
- Session state stores instantiated systems
- Module 03 reads economy system for transactions
- Module 03 reads crafting system for item creation
- Module 03 reads progression system for XP/level-up
- Module 03 reads downtime system for available activities

## Success Criteria

**All tests pass when**:
1. ✅ TC-9.1: Hunter x Hunter systems load correctly (4/4 systems)
2. ✅ TC-9.2: My Hero Academia systems load (validates profile variance)
3. ✅ TC-9.3: Konosuba systems load (validates "none" type handling)
4. ✅ TC-9.4: Player customization works (validate + update)
5. ✅ TC-9.5: Baseline systems work without profile
6. ✅ TC-9.6: Module 03 uses instantiated systems in gameplay

**Failure Conditions**:
- Systems don't load from profile
- Wrong system types displayed
- Module 03 doesn't access instantiated systems
- Currency reverts to generic "gold" instead of profile currency
- Player customization fails validation
- Baseline systems don't work

## Error Recovery

**Schema validation failure**:
- Check meta-schema files exist
- Validate JSON syntax
- Check required fields present

**Profile loading failure**:
- Verify profile exists in `aidm/libraries/narrative_profiles/`
- Check mechanical_configuration section present
- Validate nested structure (not flat parameters)

**Instantiation failure**:
- Check MechanicalInstantiator.validate_config() passes
- Verify system types exist in meta-schemas
- Check for missing required parameters

**Module 03 integration failure**:
- Verify session state stores instantiated systems
- Check Module 03 reads from session state (not hardcoded)
- Validate currency name matches profile (not defaulting to "gold")

## Documentation

**On Test Completion**:
- Update `dev/TESTING.md` with TEST-9 results
- Create `dev/PHASE_3_COMPLETION_REPORT.md`
- Update `dev/STATE.md` with Phase 3 completion status
- Update `dev/ARCHITECTURE.md` with mechanical integration flow

## Notes

**Design Philosophy**: Session Zero should automatically configure mechanical systems from narrative profiles while allowing player customization. The instantiation system bridges narrative flavor (Jenny, Eris, Yen) with mechanical function (all are fiat_currency types).

**Token Efficiency**: Mechanical instantiation happens once during Session Zero, then stored in session state. Modules read from session state (not re-instantiating every time).

---

# PART 2: GAMEPLAY VALIDATION (Phase 4 Extension)

**Purpose**: Validate that Modules 03, 05, 08, 09 correctly read from `session_state.mechanical_systems` throughout gameplay.

**Duration**: 30-45 minutes  
**Prerequisites**: Complete TC-9.1 (Hunter x Hunter Session Zero)

## TC-9.7: Module 03 Economy Integration (Extended)

**Setup**: Character with 160 Jenny (after TC-9.6 sword purchase)

### Test 9.7.1: Loot Generation
```
Player: "I defeat a bandit and loot his corpse."

Expected Module 03 Response:
Economy type: fiat_currency
Loot mode: currency_drops
Generate: 35 Jenny + Knife (1d4)

"You search the bandit's body and find 35 Jenny and a rusty knife.

UPDATED INVENTORY:
- Iron Sword (1d8 damage)
- Rusty Knife (1d4 damage)

CURRENT MONEY: 195 Jenny"
```

**Validation**:
- [ ] Loot uses Jenny (NOT "gold")
- [ ] economy.mechanics.loot_generation mode applied
- [ ] Currency_name dynamically inserted

### Test 9.7.2: Quest Rewards
```
Player: "I complete a quest to clear out a monster nest. What's my reward?"

Expected Module 03 Response:
Economy type: fiat_currency
Reward mode: currency_based
Generate: 150 Jenny

"The villagers thank you and pay 150 Jenny for clearing the nest.

CURRENT MONEY: 345 Jenny"
```

**Validation**:
- [ ] Quest reward uses Jenny (NOT "gold")
- [ ] economy.mechanics.quest_rewards mode applied

**Pass Criteria**: Module 03 uses Jenny consistently throughout all economy operations

---

## TC-9.8: Module 05 Downtime Integration

**Setup**: Complete TC-9.7, character has downtime

### Test 9.8.1: Activity Offering
```
Player: "I have some downtime before my next mission. What can I do?"

Expected Module 05 Response:
Reads downtime.enabled_modes: ["training_arcs", "investigation"]

"You have some free time. What would you like to do?

AVAILABLE DOWNTIME ACTIVITIES:
1. TRAINING ARCS: Seek out Wing to train your Nen abilities
2. INVESTIGATION: Gather intelligence on the Phantom Troupe

What interests you?"
```

**Validation**:
- [ ] Only enabled_modes offered (training_arcs, investigation)
- [ ] NOT offered: slice_of_life, travel, faction_building, social_links
- [ ] Module 05 reads from session_state.mechanical_systems.downtime

### Test 9.8.2: Training Arc Execution
```
Player: "I'll train my Nen with Wing."

Expected Module 05 Response:
Reads activity_configs.training_arcs:
- time_requirement: "2 weeks"
- success_criteria: "WIS DC 16"
- xp_rate: 1.5
- unlock_bonuses: ["Ko", "Ken", "Ryu"]

"You spend 2 weeks training with Wing, focusing on advanced Nen techniques.

TRAINING CHECK: Roll WIS DC 16
[Rolls 18 - Success!]

You successfully master the fundamentals of Ko (concentrated aura)!

TRAINING RESULTS:
- Time passed: 2 weeks
- XP gained: 600 (base 400 × 1.5 training multiplier)
- NEW TECHNIQUE: Ko (Journeyman Nen technique)

Your Nen control has improved significantly!"
```

**Validation**:
- [ ] Time requirement enforced (2 weeks)
- [ ] Success criteria applied (WIS DC 16)
- [ ] XP rate multiplier applied (× 1.5)
- [ ] Unlock bonus granted (Ko technique)
- [ ] Module 05 reads activity_configs

**Pass Criteria**: Module 05 uses instantiated downtime configs correctly

---

## TC-9.9: Module 08 Combat Progression Integration

**Setup**: Character with mastery_tiers progression (from HxH profile)

### Test 9.9.1: Combat XP Calculation
```
Player: "I fight another Chimera Ant Soldier (fair challenge)."

Expected Module 08 Response:
Reads progression.type: "mastery_tiers"
Applies mastery_tiers XP formula:
base_xp × 1.0 + technique_bonus

"You defeat the Chimera Ant Soldier!

XP CALCULATION (Mastery Tiers):
- Base XP: 800
- Challenge multiplier: 1.0 (fair fight)
- Technique bonus: +50 (used Ko advanced technique)
- TOTAL XP: 850

Tier XP: 5350 + 850 = 6200/5000

TIER ADVANCEMENT THRESHOLD EXCEEDED!
You've accumulated enough experience to advance from Journeyman to Expert tier.
Seek out Wing to demonstrate your mastery and attempt the tier advancement."
```

**Validation**:
- [ ] XP formula uses mastery_tiers (base × 1.0 + technique_bonus)
- [ ] Technique usage adds +50 XP
- [ ] tier_xp tracked (NOT character_xp)
- [ ] Tier threshold detection works
- [ ] Module 08 reads progression.type

### Test 9.9.2: Tier Bonuses in Combat
```
Player: "During combat, do my Journeyman tier bonuses apply?"

Expected Module 08 Response:
Reads progression.tier_system.tier_bonuses:
Journeyman: +2 attack, +2 defense, +2 aura control

"Yes! Your Journeyman tier grants:
- +2 to attack rolls
- +2 to defense/AC
- +2 to aura control checks

These bonuses are active in all combat."
```

**Validation**:
- [ ] Tier bonuses read from progression config
- [ ] Bonuses applied in combat

**Pass Criteria**: Module 08 uses mastery_tiers progression correctly

---

## TC-9.10: Module 09 Leveling Integration

**Setup**: Character with 6200 tier_xp (threshold exceeded in TC-9.9.1)

### Test 9.10.1: Tier Advancement (No Auto-Level)
```
Player: "I seek out Wing to attempt my tier advancement."

Expected Module 09 Response:
Reads progression.type: "mastery_tiers"
Reads advancement_rules: "demonstration_required"

"Wing greets you at the training dojo.

'I can sense your aura has grown significantly. You've accumulated the experience needed for Expert tier... but experience alone isn't enough. You must DEMONSTRATE your mastery.'

Wing presents a challenge: 'Show me your control over Ko, Ken, and Ryu. Prove you understand the principles of advanced Nen.'

TIER ADVANCEMENT CHALLENGE:
- Difficulty: WIS DC 18
- Requirements: Demonstrate Ko, Ken, Ryu
- On Success: Advance to Expert tier
- On Failure: Retain Journeyman tier, can retry after more training

What do you do?"
```

**Validation**:
- [ ] NO auto-level (demonstration required)
- [ ] Module 09 reads progression.type: "mastery_tiers"
- [ ] Module 09 reads advancement_rules: "demonstration_required"
- [ ] Tier advancement is a narrative event (NOT automatic XP threshold)

### Test 9.10.2: Tier Advancement Success
```
Player: "I demonstrate my Nen techniques to Wing."

[Rolls WIS DC 18 - Success with 19!]

Expected Module 09 Response:
Progression type: mastery_tiers
Tier advancement: Journeyman → Expert

"You focus your aura and demonstrate each technique flawlessly.

Wing nods approvingly. 'Excellent control. You understand the principles deeply. You've earned this advancement.'

TIER ADVANCEMENT: JOURNEYMAN → EXPERT

NEW TIER BONUSES:
- Attack: +2 → +3
- Defense: +2 → +3
- Aura Control: +2 → +3

NEW TECHNIQUES UNLOCKED:
- Gyo (focus aura in eyes to see hidden aura)
- In (conceal aura completely, stealth)
- En (extend aura to sense surroundings, detection)

TIER XP RESET:
- Previous: 6200/5000 (Journeyman)
- New: 1200/10,000 (Expert) [200 overflow + 1000 advancement bonus]

You feel fundamentally stronger. Your mastery of Nen has reached a new level!"
```

**Validation**:
- [ ] Tier advancement works (Journeyman → Expert)
- [ ] Tier bonuses upgraded (+2 → +3)
- [ ] New techniques unlocked (Gyo, In, En)
- [ ] tier_xp reset with overflow (6200 - 5000 + advancement bonus = 1200/10,000)
- [ ] Character sheet shows "Tier: Expert" (NOT "Level 8" or similar)
- [ ] Module 09 applies mastery_tiers leveling mechanics

**Pass Criteria**: Module 09 uses mastery_tiers tier advancement (NOT standard leveling)

---

## Part 2 Success Criteria

**All gameplay validation passes when**:
1. ✅ TC-9.7: Module 03 uses Jenny throughout all economy operations (loot, rewards, transactions)
2. ✅ TC-9.8: Module 05 offers only enabled_modes, applies activity_configs correctly
3. ✅ TC-9.9: Module 08 uses mastery_tiers XP formula, applies tier bonuses
4. ✅ TC-9.10: Module 09 uses tier advancement (demonstration required, NO auto-level)

**Failure Conditions**:
- Module 03 reverts to "gold" instead of Jenny
- Module 05 offers all downtime modes (ignores enabled_modes)
- Module 08 uses generic XP formula (ignores progression.type)
- Module 09 auto-levels at XP threshold (ignores demonstration requirement)

---

## TC-9.11: Multi-Anime Fusion Mechanical Resolution

**Purpose**: Validate how AIDM resolves conflicting mechanical configs when player requests multi-anime fusion.

**Setup**: Start new session, request Naruto + My Hero Academia fusion

```
Player: "I want a world that fuses Naruto and My Hero Academia. How do the mechanical systems work?"

Expected AIDM Challenge:
- Naruto profile: Jenny (Ryo) currency, mastery_tiers progression
- MHA profile: Yen currency, quirk_awakening progression

Expected Resolution (AIDM should propose coherent fusion):
"I'll create a fusion world with these systems:

ECONOMY: Fiat Currency (Yen)
• Starting: 50,000 yen (using MHA as modern setting base)
• Note: Naruto-style missions still exist, pay in yen
• Scarcity: Normal

PROGRESSION: Hybrid System (Quirk + Chakra)
• Primary: Quirk Awakening (MHA-style quirk evolution)
• Secondary: Chakra Control Tiers (Naruto-style jutsu mastery)
• Dual progression tracks:
  - Track 1: General levels + quirk awakenings (combat-driven)
  - Track 2: Chakra tiers (training-driven)
• Advancement: Combat XP for quirks, training arcs for chakra

DOWNTIME: Training Arcs + Hero Internships
• Training: Master jutsu OR quirk control
• Internships: Work with pro heroes (MHA-style)

Does this fusion make sense?"
```

**Validation**:
- [ ] AIDM detects mechanical conflicts (currency, progression)
- [ ] AIDM proposes coherent resolution (picks one or hybridizes)
- [ ] Resolution is internally consistent
- [ ] Player offered customization
- [ ] Fusion logic explained clearly

**Pass Criteria**: AIDM handles multi-anime mechanical fusion gracefully

---

## TC-9.12: Custom Mechanical Configuration

**Purpose**: Validate player can override profile mechanical configs.

**Setup**: Start Hunter x Hunter session, customize during Phase 3

```
Player: "I like the Hunter x Hunter world, but I want standard D&D-style leveling instead of mastery tiers. Can we change that?"

Expected AIDM Response:
"Of course! I'll update the progression system:

PROGRESSION: Class-Based (D&D-style)
• Classes: Hunter, Conjurer, Enhancer, Manipulator, Emitter, Transmuter
• Levels: 1-20
• Advancement: Standard XP thresholds
• Nen abilities: Learned as class features at specific levels

Other systems stay Hunter x Hunter:
• Economy: Jenny currency
• Downtime: Training arcs + Investigation

Does this work better?"
```

**Validation**:
- [ ] Custom config accepted
- [ ] Progression system changed (mastery_tiers → class_based)
- [ ] Other systems preserved (economy stays Jenny)
- [ ] Validation passes (class_based is valid type)
- [ ] Session state updated

**Pass Criteria**: Player can customize mechanical systems, overrides are validated and applied

---

## Part 2 Overall Success

**PASS Criteria**: All TC-9.7 through TC-9.12 pass  
**PARTIAL**: 4-5 test cases pass  
**FAIL**: <4 test cases pass

---

**End of TEST-9: Session Zero Mechanical Systems Integration (Parts 1 & 2)**
