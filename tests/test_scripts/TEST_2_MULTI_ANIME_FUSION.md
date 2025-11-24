# Test 2: Multi-Anime Fusion

**Test ID**: AIDM-TEST-002  
**Category**: Advanced Functionality  
**Priority**: HIGH  
**Estimated Time**: 30-40 minutes

---

## Test Objective

Validate that AIDM can create a coherent unified power system AND mechanical systems when player requests elements from multiple incompatible anime series.

**Success Criteria**:
1. AIDM creates coherent unified power system from 3 different anime
2. **Mechanical systems fusion resolved** (economy, progression, downtime)
3. Fusion logic explained clearly (how systems interact)
4. No contradictions or conflicts in mechanics or mechanical systems
5. World is playable (character can use all power types)
6. **Session Zero Phase 3 displays coherent mechanical fusion**

---

## Pre-Test Setup

### Files to Load into LLM

**Required**:

1. `aidm/CORE_AIDM_INSTRUCTIONS.md`
2. All files in `aidm/instructions/` (**14 files** - updated from 12)
3. All files in `aidm/schemas/` (**15+ files** - updated from 7)
4. **4 meta-schemas** (critical for mechanical fusion):
   - `aidm/schemas/economy_meta_schema.json`
   - `aidm/schemas/crafting_meta_schema.json`
   - `aidm/schemas/progression_meta_schema.json`
   - `aidm/schemas/downtime_meta_schema.json`
5. **All 5 power system libraries** (critical for this test):
   - `aidm/libraries/power_systems/mana_magic_systems.md`
   - `aidm/libraries/power_systems/ki_lifeforce_systems.md`
   - `aidm/libraries/power_systems/soul_spirit_systems.md`
   - `aidm/libraries/power_systems/psionic_psychic_systems.md`
   - `aidm/libraries/power_systems/power_scaling_narrative.md`
6. **Python library**: `aidm/libraries/common_mechanics/mechanical_instantiation.py`

**Optional**:
- `aidm/libraries/genre_tropes/isekai_tropes.md` (gates = isekai trope)
- `aidm/libraries/genre_tropes/shonen_tropes.md` (all 3 are shonen)

**Platform**: Claude Sonnet 4.5, ChatGPT-4, or equivalent  
**Required Features**: Web search (for anime research)

---

## Test Scenario

**Player Request**: Combine 3 incompatible power systems
1. **Naruto**: Chakra/jutsu system (internal ki/lifeforce)
2. **Solo Leveling**: Gates/dungeons, stat screens, leveling (isekai mechanics)
3. **My Hero Academia**: Quirks (genetic superpowers)

**Challenge**: These systems have different metaphysical foundations:
- Naruto = Learned ninja skills + chakra manipulation
- Solo Leveling = MMORPG-like "System" with quantified stats
- MHA = Inborn genetic mutations (no leveling, no chakra)

---

## Test Procedure

### Exchange 1: Fusion Request

**Player Input**:
```
I want to play in a world that combines Naruto ninja powers, Solo Leveling gates and dungeons with the "System", and My Hero Academia quirks. Can you make this work?
```

**Expected AIDM Response**:
- Acknowledges complex fusion request
- May perform web research on all 3 anime
- Begins analyzing power system compatibility
- Proposes fusion approach or asks clarifying questions

**Validation Checks**:
- [ ] AIDM recognizes all 3 anime references
- [ ] AIDM acknowledges power system conflicts
- [ ] No immediate rejection (should attempt fusion)

---

### Exchange 2-3: Fusion Logic Explanation

**Expected AIDM Behavior**:
AIDM should propose a **unified metaphysical framework** that reconciles all 3 systems.

**Example Coherent Fusion** (AIDM might propose something like this):

```
In this world, humans have 3 power sources:

1. QUIRKS (MHA - Genetic Foundation):
   - All humans born with unique genetic mutation (Quirk)
   - Quirks are passive/always-on abilities or trainable active powers
   - Examples: Hardening, Fire Generation, Super Strength
   - Quirks CANNOT be learned, only inherited

2. CHAKRA (Naruto - Internal Energy):
   - All humans have chakra network (like MHA, but trainable)
   - Jutsu are learned techniques that manipulate chakra
   - Training increases chakra capacity (like leveling)
   - Examples: Shadow Clone, Fireball Jutsu, Substitution

3. THE SYSTEM (Solo Leveling - Dungeons & Leveling):
   - 20 years ago, "Gates" appeared connecting to dungeon dimensions
   - Entering Gates grants access to "The System" (status screen, quests, leveling)
   - Defeating monsters grants XP, levels increase all stats
   - System quantifies Quirk power and Chakra capacity numerically

UNIFIED MECHANICS:
- Character Sheet shows: Quirk name, Chakra capacity (MP), Level, Stats (STR/DEX/etc.)
- Quirk determines base abilities (e.g., Fire Quirk makes fire jutsu easier)
- Chakra/jutsu learned through training (Naruto style)
- Leveling (Solo Leveling style) increases both Quirk power AND chakra capacity
- Gates/dungeons exist (Solo Leveling), but also ninja villages (Naruto) and hero schools (MHA)
```

**Player Response** (if AIDM asks for feedback):
```
Exchange 2: "That makes sense! So everyone has a Quirk, can learn jutsu, and levels up through the System. Let's go with that."
```

**Validation Checks**:
- [ ] Fusion logic is coherent (no contradictions)
- [ ] All 3 power systems integrated (not just cherry-picked)
- [ ] Explanation is clear and understandable
- [ ] Metaphysical foundation established

---

### Exchange 3.5: MECHANICAL SYSTEMS FUSION (Phase 4 Integration - NEW)

**Purpose**: Validate AIDM resolves mechanical conflicts during Session Zero Phase 3

**Expected AIDM Behavior**:
After power system fusion explanation, AIDM should proceed to **Session Zero Phase 3: MECHANICAL BUILD**, where mechanical conflicts must be resolved:

**Mechanical Conflicts to Resolve**:

1. **Currency Conflict**:
   - Naruto profile: **Ryo** (fiat currency)
   - Solo Leveling profile: **Gold** (fiat currency)
   - My Hero Academia profile: **Yen** (fiat currency)
   - **Conflict**: 3 different currencies, which one to use?

2. **Progression Conflict**:
   - Naruto profile: **mastery_tiers** (ninja ranks: Genin → Chunin → Jonin)
   - Solo Leveling profile: **class_based** (E-Rank → S-Rank Hunters with levels)
   - My Hero Academia profile: **quirk_awakening** (dual tracks: hero levels + quirk evolution)
   - **Conflict**: 3 fundamentally different progression systems

3. **Downtime Overlap** (easier to resolve):
   - Naruto: **training_arcs** + **investigation**
   - Solo Leveling: **training_arcs** + **travel** + **faction_building** (Hunter Guild)
   - My Hero Academia: **training_arcs** + **slice_of_life** (school)
   - **Conflict**: Overlapping modes, which to enable?

**Expected AIDM Phase 3 Display**:

```
=== MECHANICAL SYSTEMS FUSION ===

I've detected conflicts between the mechanical systems from these 3 anime:

CURRENCY:
• Naruto uses Ryo
• Solo Leveling uses Gold  
• My Hero Academia uses Yen

PROGRESSION:
• Naruto uses mastery_tiers (ninja ranks, demonstration-based)
• Solo Leveling uses class_based (Hunter ranks with standard leveling)
• My Hero Academia uses quirk_awakening (dual tracks)

DOWNTIME:
• All 3 have training_arcs (compatible!)
• Solo Leveling adds travel, faction_building
• My Hero Academia adds slice_of_life

PROPOSED RESOLUTION:

ECONOMY: Unified Currency System
• Primary currency: **Yen** (MHA modern economy makes sense for Gates/dungeons world)
• Exchange rates: 1 Yen = 1 Gold (Solo Leveling) = 0.1 Ryo (Naruto)
• Quest rewards use Yen
• Loot drops from Gates use Yen

PROGRESSION: Hybrid System
• Base: **class_based** leveling (Solo Leveling E→S Ranks)
• Ninja techniques: Require **rank demonstrations** (Naruto mastery_tiers rules)
  - Example: To learn Jonin-level jutsu, must demonstrate skill (WIS DC 18)
• Quirk evolution: **awakening_stage** tracked separately (MHA rules)
  - Near-death triggers awaken Quirk to next stage
• Character advances via: XP for levels (Solo Leveling) + demonstrations for jutsu (Naruto) + awakenings for Quirk (MHA)

DOWNTIME: Fusion of All Modes
• Enabled modes: training_arcs, investigation, travel, faction_building, slice_of_life
• All 3 anime activity types available

Would you like to customize any of these mechanical systems?
```

**Player Response**:
```
That works! Let's use that fusion setup.
```

**Validation Checks** (Phase 3 Mechanical Fusion):
- [ ] AIDM detects currency conflict (Ryo vs Gold vs Yen)
- [ ] AIDM proposes coherent currency resolution (pick one or unified system)
- [ ] AIDM detects progression conflict (mastery_tiers vs class_based vs quirk_awakening)
- [ ] AIDM proposes coherent progression resolution (pick one or hybrid)
- [ ] AIDM detects downtime overlap
- [ ] AIDM proposes downtime fusion (enable all or subset)
- [ ] Resolution is internally consistent (no contradictions)
- [ ] Player offered customization (can override proposal)
- [ ] Mechanical systems stored in session_state.mechanical_systems

**Critical Validation**:
- **Economy**: ONE primary currency chosen (Yen in example), not "Ryo for ninja stuff, Gold for Gates, Yen for MHA"
- **Progression**: Coherent advancement rules defined (not "sometimes levels, sometimes demonstrations, randomly")
- **Downtime**: Clear list of enabled modes

**Acceptable Fusion Approaches**:
1. **Pick Dominant Anime**: Use Solo Leveling mechanics (Gold, class_based, travel), ignore Naruto/MHA mechanical systems
2. **True Hybrid**: Unified currency (Yen), hybrid progression (levels + demonstrations + awakenings), all downtime modes
3. **Player Choice**: AIDM asks "Which anime's economy do you prefer?" and applies player selection

**Unacceptable Approaches**:
- ❌ No resolution proposed (ignores conflicts)
- ❌ Incoherent resolution (use Ryo for ninja villages, Gold in Gates, Yen in cities → player confused what currency to use where)
- ❌ Over-complex resolution (4-page explanation of multi-currency exchange rates)

---

### Exchange 4-5: Character Creation with Fusion

**Player Input**:
```
Exchange 3: "I want to create a character. My Quirk is 'Lightning Generation', I've trained in Lightning Style jutsu (Naruto), and I'm a C-Rank Hunter (Solo Leveling)."
```

**Expected AIDM Response**:
- Creates character integrating all 3 elements
- Shows stats screen (Solo Leveling style)
- Lists Quirk, jutsu, and System skills
- Assigns appropriate level/stats for C-Rank

**Example Character Sheet** (Hybrid Mechanical Systems):
```
NAME: [Player Choice]
LEVEL: 8 (C-Rank Hunter) | XP: 6200/7000 to Level 9
QUIRK: Lightning Generation (Base Stage) | awakening_stage: 0/3
NINJA RANK: Chunin (demonstration-based, not tied to Level)

STATS:
HP: 120/120
CHAKRA: 80/80 (MP equivalent)
STAMINA: 100/100

STR: 12  |  DEX: 15  |  CON: 11
INT: 13  |  WIS: 10  |  CHA: 9

JUTSU (Chakra Techniques - Require Rank Demonstrations):
- Lightning Style: Chidori (40 Chakra, 3d10 lightning damage) [Jonin-level technique, requires demonstration]
- Lightning Style: False Darkness (20 Chakra, 2d6 lightning damage, ranged) [Chunin-level]
- Body Flicker Technique (15 Chakra, teleport short distance) [Genin-level]

QUIRK ABILITIES (Awakening Stage 0):
- Passive: Lightning Generation (can create electricity without chakra, 1d6 damage)
- Active: Overcharge (boost Quirk power, risks damage to self, once per day)
- [LOCKED] Stage 1: Lightning Aura (requires near-death awakening trigger)

SYSTEM SKILLS (Solo Leveling):
- Dash (5 Stamina, double movement speed for 1 turn)
- Analyze (10 Stamina, reveal enemy stats)

INVENTORY:
- Hunter License (C-Rank)
- Kunai x10
- Healing Potion x3
- **Currency: 5,000 Yen** (unified currency)

PROGRESSION TRACKS:
• Hunter Levels: Standard XP (defeat enemies, complete quests)
• Ninja Rank: Demonstration-based (prove skill to sensei, WIS/DEX checks)
• Quirk Awakening: Event-based (near-death triggers, emotional breakthroughs)
```

**Validation Checks**:
- [ ] Character has Quirk (MHA element)
- [ ] Character has jutsu (Naruto element)
- [ ] Character has stats/level/System skills (Solo Leveling element)
- [ ] All 3 systems integrated on one character sheet
- [ ] No contradictions (e.g., jutsu don't conflict with Quirk)
- [ ] **Currency: Unified currency (Yen), NOT multiple currencies**
- [ ] **Progression: Hybrid tracks clearly defined (XP + demonstrations + awakenings)**
- [ ] **awakening_stage field present (0/3 or similar)**
- [ ] **Ninja rank displayed (Chunin), separate from Hunter level (8)**

---

### Exchange 6-7: World Playability Test

**Player Input**:
```
Exchange 5: "Great! Let's start the game. I want to enter a Gate (dungeon) to hunt monsters and level up."
```

**Expected AIDM Response**:
- Opens with Gate dungeon scenario
- Shows monsters with stats
- Player can use Quirk, jutsu, AND System skills in combat
- XP/leveling mechanics present

**Player Input** (combat test):
```
Exchange 6: "I use my Quirk to generate lightning in my hand, then channel it into Chidori (jutsu) for a combo attack against the first monster!"
```

**Expected AIDM Response**:
- Allows Quirk + jutsu combo (synergy between systems)
- Calculates damage appropriately
- Deducts chakra cost
- Narrates result
- Tracks HP/MP/Stamina

**Validation Checks**:
- [ ] Gates/dungeons exist (Solo Leveling element)
- [ ] Jutsu work in combat (Naruto element)
- [ ] Quirk works in combat (MHA element)
- [ ] System tracks all resources (HP/Chakra/Stamina)
- [ ] Systems interact synergistically (combos possible)

---

### Exchange 8-10: Fusion Stress Test

**Player Inputs** (test edge cases):
```
Exchange 7: "After the dungeon, I return to my ninja village and train a new jutsu with my sensei."

Exchange 8: "Can I level up my Quirk by defeating Gate monsters, or is Quirk power genetic only?"

Exchange 9: "Do ninja villages send people into Gates, or is that a separate Hunter organization like Solo Leveling?"
```

**Expected AIDM Responses**:
- **Ex 7**: Allows training (Naruto element) while in Solo Leveling-style world
- **Ex 8**: Clarifies fusion rules (e.g., "Leveling increases Quirk effectiveness, but doesn't change Quirk type")
- **Ex 9**: Explains organizational structure (e.g., "Ninja villages AND Hunter Association exist, sometimes collaborate")

**Validation Checks**:
- [ ] All 3 systems coexist in world (not just player's powers)
- [ ] AIDM has coherent rules for edge cases
- [ ] No contradictions introduced
- [ ] World is logically consistent

---

## Success Determination

### PASS Criteria (All must be true)

1. **Coherent Power System**:
   - All 3 anime elements integrated (Quirks, jutsu, System)
   - No fundamental contradictions
   - Fusion logic is internally consistent
   
2. **Mechanical Systems Fusion** (Phase 4 Integration):
   - Currency conflict resolved (Ryo vs Gold vs Yen → ONE primary currency chosen)
   - Progression conflict resolved (mastery_tiers vs class_based vs quirk_awakening → coherent hybrid or dominant system)
   - Downtime overlap resolved (clear list of enabled modes)
   - Resolution is internally consistent (not "use Ryo in ninja villages, Gold in Gates, Yen in cities")
   - Mechanical fusion displayed in Session Zero Phase 3
   
3. **Clear Explanation**:
   - AIDM explains how power systems interact
   - AIDM explains how mechanical systems resolve
   - Metaphysical foundation established
   - Rules for edge cases defined
   
4. **Playable World**:
   - Character can use all power types
   - Combat works with all 3 systems
   - World contains elements from all 3 anime
   - **Character sheet uses unified currency (Yen), not multiple currencies**
   - **Progression tracks clearly defined (XP + demonstrations + awakenings)**
   
5. **No Conflicts**:
   - Systems complement each other (not fight for dominance)
   - Stat tracking works across all systems
   - Narrative doesn't favor one anime over others
   - **Mechanical systems don't contradict** (not "loot in Ryo, quest rewards in Gold")

### FAIL Criteria (Any triggers failure)

1. ❌ AIDM refuses fusion attempt
2. ❌ Major contradictions (e.g., "Quirks use chakra" when MHA has no chakra)
3. ❌ One system dominates/replaces others (e.g., everything becomes Solo Leveling, Naruto ignored)
4. ❌ Fusion is incoherent (player confused about how powers work)
5. ❌ Systems conflict mechanically (can't use jutsu and Quirk together)
6. ❌ **Mechanical conflicts ignored** (currency conflict not resolved, character has "5000 Ryo" and "3000 Gold" simultaneously)
7. ❌ **Incoherent mechanical fusion** (use Ryo in ninja villages, Gold in Gates, Yen in cities → player confused)
8. ❌ **No Session Zero Phase 3** (mechanical systems not displayed/validated)

### PARTIAL Criteria (Minor issues acceptable)

⚠️ Minor inconsistencies in lore (not mechanics)  
⚠️ Fusion slightly favors one anime (but all 3 present)  
⚠️ Edge cases not fully defined (but core fusion works)

---

## Results Template

**Test Execution Date**: ___________  
**LLM Platform**: ___________  
**LLM Version**: ___________

### Fusion Quality Assessment

**Power System Integration**:
- [ ] Quirks integrated (MHA)
- [ ] Jutsu/chakra integrated (Naruto)
- [ ] System/Gates/leveling integrated (Solo Leveling)
- **Integration Rating**: ___/10

**Mechanical Systems Fusion** (Phase 4 Integration):
- [ ] Currency conflict detected (Ryo vs Gold vs Yen)
- [ ] Currency resolution coherent (ONE primary currency chosen: _______)
- [ ] Progression conflict detected (mastery_tiers vs class_based vs quirk_awakening)
- [ ] Progression resolution coherent (system chosen: _______)
- [ ] Downtime overlap resolved (enabled_modes: _______)
- [ ] Session Zero Phase 3 displayed mechanical fusion
- [ ] Character sheet uses unified currency (not "5000 Ryo + 3000 Gold")
- [ ] Progression tracks clearly defined (XP / demonstration / awakening rules)
- **Mechanical Fusion Rating**: ___/10

**Coherence**:
- [ ] Fusion logic explained clearly
- [ ] No fundamental contradictions (power systems)
- [ ] No mechanical contradictions (currency, progression, downtime)
- [ ] Edge cases handled reasonably
- **Coherence Rating**: ___/10

**Playability**:
- [ ] Character can use all 3 power types
- [ ] Combat works
- [ ] World contains all 3 anime elements
- [ ] Unified currency works (loot, rewards, purchases all use same currency)
- [ ] Progression tracks work (XP gain, tier advancement, awakenings all functional)
- **Playability Rating**: ___/10

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

**Issue**: AIDM refuses to fuse systems
- **Cause**: Over-cautious about contradictions
- **Fix**: Check power_scaling_narrative.md loaded; emphasize "creative fusion"

**Issue**: Only one system dominates
- **Cause**: AIDM defaults to simplest framework
- **Fix**: Explicitly request all 3 in character sheet

**Issue**: Contradictions in mechanics
- **Cause**: Power system libraries not loaded or not referenced
- **Fix**: Verify all 5 power libraries loaded; check AIDM references them

**Issue**: Unclear fusion logic
- **Cause**: Session Zero skipped or rushed
- **Fix**: Ask AIDM to explicitly explain metaphysical framework

**Issue**: Mechanical conflicts not resolved (Phase 4)
- **Cause**: Meta-schemas not loaded or Module 00 skipped Session Zero Phase 3
- **Fix**: Verify 4 meta-schemas loaded (economy, progression, downtime, crafting), check mechanical_instantiation.py loaded

**Issue**: Character has multiple currencies (5000 Ryo + 3000 Gold)
- **Cause**: AIDM didn't resolve currency conflict
- **Fix**: Explicitly ask "What currency does this world use?" during Session Zero Phase 3

**Issue**: Progression unclear (levels AND ninja ranks, but not defined how they interact)
- **Cause**: AIDM didn't resolve progression conflict
- **Fix**: Ask "How does leveling work in this fusion?" and validate response includes ALL 3 anime progression elements

**Issue**: Character sheet missing hybrid fields (no awakening_stage, no ninja rank)
- **Cause**: Character schema v2.3.0 not loaded, or fusion didn't apply hybrid progression
- **Fix**: Verify character_schema.json v2.3.0 loaded with awakening_stage and tier_xp fields

---

## Test Artifacts to Save

1. **Full conversation transcript**
2. **Fusion framework explanation** (AIDM's exact text)
3. **Character sheet** (showing all 3 systems integrated)
4. **Combat example** (showing all systems in action)
5. **Any contradiction notes**

Store in: `tests/results/test_2_multi_anime_fusion_[DATE].md`

---

**Test Status**: Ready for execution  
**Next Action**: Load all power system libraries and begin test
