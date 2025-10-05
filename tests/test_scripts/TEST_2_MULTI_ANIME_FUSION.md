# Test 2: Multi-Anime Fusion

**Test ID**: AIDM-TEST-002  
**Category**: Advanced Functionality  
**Priority**: HIGH  
**Estimated Time**: 30-40 minutes

---

## Test Objective

Validate that AIDM can create a coherent unified power system when player requests elements from multiple incompatible anime series.

**Success Criteria**:
1. AIDM creates coherent unified power system from 3 different anime
2. Fusion logic explained clearly (how systems interact)
3. No contradictions or conflicts in mechanics
4. World is playable (character can use all power types)

---

## Pre-Test Setup

### Files to Load into LLM

**Required**:
1. `aidm/CORE_AIDM_INSTRUCTIONS.md`
2. All files in `aidm/instructions/` (12 files)
3. All files in `aidm/schemas/` (7 files)
4. **All 5 power system libraries** (critical for this test):
   - `aidm/libraries/power_systems/mana_magic_systems.md`
   - `aidm/libraries/power_systems/ki_lifeforce_systems.md`
   - `aidm/libraries/power_systems/soul_spirit_systems.md`
   - `aidm/libraries/power_systems/psionic_psychic_systems.md`
   - `aidm/libraries/power_systems/power_scaling_narrative.md`

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

**Example Character Sheet**:
```
NAME: [Player Choice]
LEVEL: 8 (C-Rank Hunter)
QUIRK: Lightning Generation (can generate electricity, enhances Raiton jutsu)

STATS:
HP: 120/120
CHAKRA: 80/80 (MP equivalent)
STAMINA: 100/100

STR: 12  |  DEX: 15  |  CON: 11
INT: 13  |  WIS: 10  |  CHA: 9

JUTSU (Chakra Techniques):
- Lightning Style: Chidori (40 Chakra, 3d10 lightning damage)
- Lightning Style: False Darkness (20 Chakra, 2d6 lightning damage, ranged)
- Body Flicker Technique (15 Chakra, teleport short distance)

QUIRK ABILITIES:
- Passive: Lightning Generation (can create electricity without chakra, 1d6 damage)
- Active: Overcharge (boost Quirk power, risks damage to self, once per day)

SYSTEM SKILLS:
- Dash (5 Stamina, double movement speed for 1 turn)
- Analyze (10 Stamina, reveal enemy stats)

INVENTORY:
- Hunter License (C-Rank)
- Kunai x10
- Healing Potion x3
```

**Validation Checks**:
- [ ] Character has Quirk (MHA element)
- [ ] Character has jutsu (Naruto element)
- [ ] Character has stats/level/System skills (Solo Leveling element)
- [ ] All 3 systems integrated on one character sheet
- [ ] No contradictions (e.g., jutsu don't conflict with Quirk)

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
   
2. **Clear Explanation**:
   - AIDM explains how systems interact
   - Metaphysical foundation established
   - Rules for edge cases defined
   
3. **Playable World**:
   - Character can use all power types
   - Combat works with all 3 systems
   - World contains elements from all 3 anime
   
4. **No Conflicts**:
   - Systems complement each other (not fight for dominance)
   - Stat tracking works across all systems
   - Narrative doesn't favor one anime over others

### FAIL Criteria (Any triggers failure)

1. ❌ AIDM refuses fusion attempt
2. ❌ Major contradictions (e.g., "Quirks use chakra" when MHA has no chakra)
3. ❌ One system dominates/replaces others (e.g., everything becomes Solo Leveling, Naruto ignored)
4. ❌ Fusion is incoherent (player confused about how powers work)
5. ❌ Systems conflict mechanically (can't use jutsu and Quirk together)

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

**Coherence**:
- [ ] Fusion logic explained clearly
- [ ] No fundamental contradictions
- [ ] Edge cases handled reasonably
- **Coherence Rating**: ___/10

**Playability**:
- [ ] Character can use all 3 power types
- [ ] Combat works
- [ ] World contains all 3 anime elements
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
