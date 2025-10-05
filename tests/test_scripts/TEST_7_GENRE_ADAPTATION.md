# Test 7: Genre Adaptation

**Test ID**: AIDM-TEST-007  
**Category**: Quality & Polish  
**Priority**: MEDIUM  
**Estimated Time**: 45-60 minutes

---

## Test Objective

Validate that AIDM adapts tone, pacing, and mechanical focus appropriately across different anime genres.

**Success Criteria**:
1. **Isekai**: Fast pacing, power fantasy, status screens, dungeon crawling
2. **Shonen**: Training arcs, friendship themes, dramatic battles, power-ups
3. **Slice-of-Life**: Slow pacing, relationship focus, seasonal activities, minimal combat
4. Each session feels genre-authentic
5. AIDM adapts mechanics appropriately (combat vs social stats)

---

## Pre-Test Setup

### Files to Load into LLM

**Required**:
1. `aidm/CORE_AIDM_INSTRUCTIONS.md`
2. All files in `aidm/instructions/` (12 files)
3. All files in `aidm/schemas/` (7 files)
4. **All 4 genre trope libraries**:
   - `aidm/libraries/genre_tropes/isekai_tropes.md`
   - `aidm/libraries/genre_tropes/shonen_tropes.md`
   - `aidm/libraries/genre_tropes/seinen_tropes.md`
   - `aidm/libraries/genre_tropes/slice_of_life_tropes.md`
5. Common mechanics libraries (stats, leveling, skills)

**Platform**: Claude Sonnet 4.5, ChatGPT-4, or equivalent  
**Time**: 3 separate sessions (~15-20 min each)

---

## Test Procedure

### SESSION A: Isekai Adventure (Exchanges 1-10)

**Exchange 1: Isekai Setup**
```
Player: "I want to play an isekai adventure like Solo Leveling. I'm a modern guy who gets access to a game-like 'System' after gates appear. Fast-paced power fantasy with lots of dungeon crawling and leveling."
```

**Expected AIDM Response**:
- Initiates isekai Session Zero
- Asks about cheat skills/unique abilities
- Offers gate/dungeon system
- Suggests status screen display
- Tone: Exciting, power fantasy

**Validation**:
- [ ] AIDM recognizes isekai genre
- [ ] Session Zero questions genre-appropriate
- [ ] Tone energetic and fast-paced

---

**Exchange 2-3: Character Creation (Isekai)**
```
Exchange 2: "I want a rare 'Necromancer' class with a cheat skill that lets me level faster than normal hunters."

Exchange 3: "Start me at E-Rank hunter, but with potential to become the strongest."
```

**Expected**:
- Creates character with System interface
- Displays status screen (HP/MP/Level/Stats)
- Shows skills/class abilities
- Assigns E-Rank with growth potential
- **Isekai elements**: Status screen, ranking system, unique class

**Example Character Sheet**:
```
NAME: [Player Choice]
CLASS: Necromancer (Unique)
RANK: E (Hunter Association)
LEVEL: 5

HP: 60/60
MP: 100/100
SP: 50/50

STATS:
STR: 8  | DEX: 10 | CON: 9
INT: 16 | WIS: 12 | LUK: 14

SKILLS:
- Summon Skeleton Warrior (30 MP)
- Death Bolt (20 MP, 2d8 necrotic)
- Life Drain (25 MP, heal = damage dealt)

CHEAT SKILL: Rapid Growth (Gain 2× XP from all sources)

TITLE: None (yet)
```

**Validation**:
- [ ] Status screen displayed (isekai trope)
- [ ] Ranking system present (E-Rank)
- [ ] Cheat skill included
- [ ] Mechanics game-like (levels, stats, skills)

---

**Exchange 4-7: Dungeon Crawling (Fast Pacing)**
```
Exchange 4: "I enter my first E-Rank gate."
```

**Expected AIDM Response**:
- Quick dungeon entry (no 10-minute prep)
- Describes gate/dungeon visually
- Presents monsters immediately
- **Pacing: FAST** (action within 1-2 exchanges)

```
Exchange 5: "I fight the skeleton monsters."
```

**Expected**:
- Combat resolved quickly (1-3 exchanges, not 10+ turns)
- Multiple enemies defeated per exchange
- XP/loot displayed immediately
- Status screen updates shown

**Example**:
```
You summon two Skeleton Warriors and send them into battle!

COMBAT (quick resolution):
- Your skeletons defeat 5 Skeleton Mobs (20 XP each = 100 XP)
- You cast Death Bolt on the Skeleton Knight (killed, 80 XP)

TOTAL XP GAINED: 180 × 2 (Rapid Growth) = 360 XP!

LEVEL UP! 5 → 6
+10 HP, +15 MP, +1 INT, +1 WIS

LOOT: Skeleton Bone x8, Mana Crystal x2, 150 gold

STATUS:
HP: 70/70 | MP: 65/115 | LEVEL: 6 | XP: 210/900
```

**Validation**:
- [ ] Combat fast (not turn-by-turn tactical)
- [ ] Multiple enemies defeated quickly
- [ ] XP/leveling prominent (power progression)
- [ ] Loot immediate and satisfying
- [ ] Status screen updates shown

---

```
Exchange 6: "I clear the dungeon."

Exchange 7: "I return and immediately enter a D-Rank gate."
```

**Expected AIDM Response**:
- Dungeon cleared quickly (no long epilogue)
- **Fast pacing**: Can immediately enter next gate
- Power progression evident (E-Rank → D-Rank)
- No forced downtime

**Validation**:
- [ ] Pacing: FAST (action → action → action)
- [ ] Power fantasy (player progressing rapidly)
- [ ] No forced slice-of-life interruptions

---

**Exchange 8-10: Isekai Tropes**
```
Exchange 8: "Do I get a title or achievement?"
```

**Expected**: System awards title (e.g., "Dungeon Crawler I")

```
Exchange 9: "Can I see my full status screen?"
```

**Expected**: Displays detailed status (isekai staple)

```
Exchange 10: "Do other hunters react to my rapid progress?"
```

**Expected**: NPCs notice player's unusual growth (isekai jealousy/rivalry trope)

**Validation**:
- [ ] Isekai tropes present (titles, status screens, envy)
- [ ] Genre feels authentic (Solo Leveling vibes)
- [ ] Mechanics appropriate (game-like, quantified)

---

### SESSION B: Shonen Battle (Exchanges 1-10)

**NEW SESSION** (clear AIDM context or mark clear genre shift)

**Exchange 1: Shonen Setup**
```
Player: "I want to play a shonen battle campaign like My Hero Academia or Naruto. Focus on training arcs, friendship, dramatic battles, and getting stronger through hard work and bonds."
```

**Expected AIDM Response**:
- Recognizes shonen genre
- Asks about power system (quirks, jutsu, etc.)
- Suggests training arc, rivals, mentor
- Tone: Inspirational, friendship-focused

**Validation**:
- [ ] AIDM recognizes shonen genre
- [ ] Session Zero questions different from isekai
- [ ] Tone shifts (inspirational vs power fantasy)

---

**Exchange 2-3: Character Creation (Shonen)**
```
Exchange 2: "I'm a young ninja at the academy, aiming to become the strongest. I have a lightning affinity but struggle with chakra control."

Exchange 3: "I want a mentor and a rival my age."
```

**Expected**:
- Creates character with flaws (struggles with chakra)
- Introduces mentor NPC (experienced jonin)
- Introduces rival (friendly or antagonistic)
- **Shonen elements**: Growth mindset, relationships matter

**Example**:
```
NAME: [Player Choice]
AGE: 13 (Academy Student)
AFFINITY: Lightning (Raiton)

STATS:
Chakra: 50/50 (low for your age)
Stamina: 60/60
Chakra Control: 3/10 (weakness - room for growth!)

JUTSU:
- Basic Clone (5 Chakra)
- Substitution (10 Chakra)
- Lightning Spark (15 Chakra, weak attack)

MENTOR: Jonin Takeshi (stern but fair, sees your potential)
RIVAL: Kenji (natural talent, challenges you constantly)

GOAL: Become the strongest ninja and prove hard work beats talent!
```

**Validation**:
- [ ] Character has flaws (chakra control weak)
- [ ] Relationships central (mentor, rival)
- [ ] Growth mindset (hard work theme)
- [ ] Different from isekai (not instant power)

---

**Exchange 4-7: Training Arc (Slow Build)**
```
Exchange 4: "I ask Sensei Takeshi to train me in chakra control."
```

**Expected AIDM Response**:
- Describes training regimen
- **Pacing: SLOW** (training takes time, not instant)
- Mentor gives wisdom/encouragement
- Tone: Inspirational struggle

**Example**:
```
Sensei Takeshi nods. "Chakra control is fundamental. We'll start with tree-walking."

He demonstrates, walking up a tree trunk vertically using chakra on his feet.

"Focus your chakra to your soles. Too little, you fall. Too much, the tree explodes. Balance is key."

You attempt it. (Roll Chakra Control check: 1d20+3 = 9... failure)

You manage two steps before slipping and falling.

Takeshi: "Again. A ninja doesn't give up after one try."

What do you do?
```

**Validation**:
- [ ] Training arc mechanics (checks, failures, persistence)
- [ ] Pacing: SLOW (growth takes multiple exchanges)
- [ ] Mentor relationship (encouragement, wisdom)
- [ ] Tone: Inspirational (don't give up!)

---

```
Exchange 5: "I train for a week, practicing every day."

Exchange 6: "I finally master tree-walking!"
```

**Expected**:
- **Time skip allowed** (week of training)
- Success after persistence
- Chakra Control stat improves (3 → 5)
- Mentor pride / rival reaction

**Validation**:
- [ ] Training arc structure (struggle → persistence → breakthrough)
- [ ] Stats improve through training (not just leveling)
- [ ] Different from isekai (no instant power-up)

---

```
Exchange 7: "Kenji challenges me to a sparring match."
```

**Expected AIDM Response**:
- Rival battle with dramatic stakes
- **Pacing: MODERATE** (not fast like isekai, not slow like training)
- Friendship/rivalry themes (Kenji pushes you to improve)
- Tone: Dramatic but supportive

**Validation**:
- [ ] Rival dynamics (challenge → growth)
- [ ] Combat more dramatic than tactical
- [ ] Friendship themes (rivalry helps both grow)

---

**Exchange 8-10: Shonen Tropes**
```
Exchange 8: "I use my new jutsu and win through determination!"
```

**Expected**: Power of friendship/hard work victory (shonen staple)

```
Exchange 9: "After the match, Kenji and I become closer friends."
```

**Expected**: Rival → friend arc (shonen trope)

```
Exchange 10: "Sensei Takeshi says I'm ready for the Chunin Exams."
```

**Expected**: Exam/tournament arc hook (shonen structure)

**Validation**:
- [ ] Shonen tropes present (hard work wins, rivals → friends, exams)
- [ ] Genre feels authentic (Naruto/MHA vibes)
- [ ] Mechanics appropriate (training, growth, relationships)

---

### SESSION C: Slice-of-Life Romance (Exchanges 1-10)

**NEW SESSION** (clear context again)

**Exchange 1: Slice-of-Life Setup**
```
Player: "I want a cozy slice-of-life high school romance like Horimiya or Kaguya-sama. No combat, just everyday school life, relationships, and seasonal events."
```

**Expected AIDM Response**:
- Recognizes slice-of-life genre
- Asks about school setting, romance interests
- Suggests club activities, school events
- Tone: Warm, wholesome, relaxed

**Validation**:
- [ ] AIDM recognizes slice-of-life genre
- [ ] Session Zero completely different (no combat talk)
- [ ] Tone shifts (warm/cozy vs action/drama)

---

**Exchange 2-3: Character Creation (Slice-of-Life)**
```
Exchange 2: "I'm a shy second-year student who joined the Literature Club. I have a crush on the club president."

Exchange 3: "No stats for combat - just social stats like Charm, Empathy, and Creativity."
```

**Expected**:
- Creates character with personality traits (shy)
- **Social stats instead of combat stats**
- Introduces love interest (club president)
- Describes school/club setting

**Example**:
```
NAME: [Player Choice]
YEAR: Second-Year (Class 2-A)
CLUB: Literature Club

SOCIAL STATS:
Charm: 4/10 (shy, but genuine)
Empathy: 7/10 (good listener)
Creativity: 6/10 (decent writer)

RELATIONSHIPS:
- Yuki (Club President): 10/100 (barely know each other)
- Hiro (Best Friend): 60/100 (close since middle school)

PERSONALITY: Shy, thoughtful, loves reading

CURRENT SEASON: Spring (cherry blossoms blooming)
```

**Validation**:
- [ ] Social stats (not HP/MP/SP)
- [ ] Relationship meters (affinity/intimacy)
- [ ] No combat mechanics
- [ ] Seasonal context (spring)

---

**Exchange 4-7: School Life (Very Slow Pacing)**
```
Exchange 4: "It's lunchtime. I eat lunch with Hiro on the rooftop."
```

**Expected AIDM Response**:
- Describes peaceful lunch scene
- **Pacing: VERY SLOW** (entire exchange for one meal)
- Character interaction (Hiro talks about Yuki)
- Tone: Warm, slice-of-life atmosphere

**Example**:
```
You and Hiro sit on the rooftop, the spring breeze carrying cherry blossom petals past you.

Hiro unwraps his lunch. "So... I saw you staring at Yuki during club yesterday."

He grins teasingly. "You've got it bad, huh?"

Your face flushes. "I-I wasn't staring..."

Hiro laughs. "Relax! Yuki's nice. You should talk to her more. Maybe ask about her favorite books?"

The lunch bell rings in the distance. You have a free period next.

What do you do?
```

**Validation**:
- [ ] Pacing: VERY SLOW (one scene = one exchange)
- [ ] No action (just conversation)
- [ ] Tone: Cozy, wholesome
- [ ] Romance hints (blushing, teasing)

---

```
Exchange 5: "After school, I go to Literature Club."

Exchange 6: "I nervously try to talk to Yuki about books."
```

**Expected**:
- **Social interaction mechanics** (Charm check?)
- Yuki responds based on approach
- Relationship meter increases slightly (10 → 15)
- Tone: Sweet, awkward, relatable

```
Exchange 7: "The club decides to attend the Spring Festival together."
```

**Expected**: Seasonal event hook (slice-of-life staple)

**Validation**:
- [ ] Social mechanics (not combat)
- [ ] Relationship progression slow and realistic
- [ ] Seasonal activities (festival)
- [ ] No pressure or combat stakes

---

**Exchange 8-10: Slice-of-Life Tropes**
```
Exchange 8: "At the festival, Yuki and I get separated from the group."
```

**Expected**: Classic "alone together" romantic moment

```
Exchange 9: "We share cotton candy and watch the fireworks."
```

**Expected**: Romantic moment (intimacy increase, maybe hand-holding)

```
Exchange 10: "On the walk home, it starts raining. We share an umbrella."
```

**Expected**: Shared umbrella trope (slice-of-life classic!)

**Validation**:
- [ ] Slice-of-life tropes (festivals, fireworks, shared umbrella)
- [ ] Genre feels authentic (Horimiya/Kaguya-sama vibes)
- [ ] Mechanics appropriate (social stats, relationship meters)
- [ ] **NO COMBAT EVER** (genre maintained)

---

## Success Determination

### PASS Criteria (All must be true)

1. **Isekai Session**:
   - Fast pacing (action every 1-2 exchanges)
   - Power fantasy (rapid leveling, OP abilities)
   - Status screens displayed
   - Dungeon crawling focus
   - Isekai tropes present

2. **Shonen Session**:
   - Training arcs (slow build, persistence)
   - Friendship/rivalry themes
   - Dramatic battles (not tactical)
   - Power-ups through hard work
   - Shonen tropes present

3. **Slice-of-Life Session**:
   - Slow pacing (one scene per exchange)
   - Relationship focus (social stats)
   - Seasonal activities
   - **No combat** (completely different)
   - Slice-of-life tropes present

4. **Genre Adaptation**:
   - Each session feels distinct
   - Tone shifts appropriately
   - Mechanics adapt (combat → social)
   - AIDM references genre trope libraries

### FAIL Criteria (Any triggers failure)

1. ❌ All sessions feel the same (no genre differentiation)
2. ❌ Combat in slice-of-life session (genre break)
3. ❌ Isekai too slow (breaks power fantasy)
4. ❌ Shonen lacks friendship/training themes
5. ❌ Mechanics don't adapt (same stats for all genres)

### PARTIAL Criteria (Minor issues acceptable)

⚠️ Genre mostly correct but occasional tone slips  
⚠️ Some tropes missing but overall feel authentic  
⚠️ Mechanics partially adapted (social stats present but underused)  
⚠️ One session weak but other two strong

---

## Results Template

**Test Execution Date**: ___________  
**LLM Platform**: ___________  
**LLM Version**: ___________

### Isekai Session Quality
- Pacing: ___ (Fast/Moderate/Slow)
- Power fantasy feel: ___/10
- Status screens used: Yes/No
- Isekai tropes count: ___
- **Rating**: ___/10

### Shonen Session Quality
- Training arc structure: ___/10
- Friendship themes: ___/10
- Dramatic combat: Yes/No
- Shonen tropes count: ___
- **Rating**: ___/10

### Slice-of-Life Session Quality
- Pacing: ___ (Fast/Moderate/Slow)
- Romance quality: ___/10
- Combat present: Yes/No (should be NO)
- Slice-of-life tropes count: ___
- **Rating**: ___/10

### Genre Differentiation
- Sessions feel distinct: Yes/No
- Tone adaptation: ___/10
- Mechanic adaptation: ___/10

### Overall Result
- [ ] ✅ PASS
- [ ] ⚠️ PARTIAL PASS
- [ ] ❌ FAIL

**Notes**: ___________

---

## Troubleshooting

### If Test Fails

**Issue**: All sessions same tone
- **Cause**: Genre trope libraries not loaded or not applied
- **Fix**: Verify all 4 genre libraries loaded; emphasize genre in prompts

**Issue**: Combat in slice-of-life
- **Cause**: AIDM defaults to combat
- **Fix**: Explicitly state "no combat ever" in Session Zero

**Issue**: Isekai too slow
- **Cause**: AIDM over-roleplaying
- **Fix**: Emphasize "fast pacing, power fantasy" in setup

**Issue**: Shonen lacks themes
- **Cause**: shonen_tropes.md not loaded
- **Fix**: Load library; emphasize friendship/training in setup

---

## Test Artifacts to Save

1. **All 3 session transcripts** (full conversations)
2. **Genre comparison table** (pacing, tone, mechanics)
3. **Trope checklist** (which tropes appeared per genre)
4. **Mechanic comparison** (combat stats vs social stats)
5. **Tone analysis** (quotes showing tone differences)

Store in: `tests/results/test_7_genre_adaptation_[DATE].md`

---

**Test Status**: Ready for execution  
**Next Action**: Run 3 separate sessions (isekai, shonen, slice-of-life)
