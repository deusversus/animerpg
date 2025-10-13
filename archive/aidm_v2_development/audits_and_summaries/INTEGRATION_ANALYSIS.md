# AIDM Integration Analysis - System Connectivity Audit

**Date**: 2025-10-11  
**Audit Type**: Cross-Module Integration & Library Accessibility  
**Triggered By**: External testing revealing orphaned systems (combat stats, genre tropes, power systems)

---

## Executive Summary

**CRITICAL FINDING**: Narrative Calibration (Module 13 + CORE profile expansion) has created **narrative-first storytelling** that risks **orphaning mechanical systems**. While storytelling quality is exceptional (12K+ word profiles), the following systems show weak or missing integration:

1. **Combat Stats Tracking** (HP/MP/SP): Mentioned in Module 08 but **not referenced in narrative profiles**
2. **Genre Tropes Libraries**: Skeletal/incomplete, **not integrated with narrative profiles**
3. **Power Systems Libraries**: Exist but **unclear connection to narrative calibration**
4. **Common Mechanics** (stat_frameworks, leveling_curves, skill_taxonomies): **Not cross-referenced in CORE profiles**

**ROOT CAUSE**: Module 13 (Narrative Calibration) focuses on **HOW to tell stories** (pacing, tone, dialogue), but **doesn't bridge to WHAT mechanics support those stories** (HP scaling, stat distributions, power systems that enable the narrative).

---

## Detailed Findings

### 1. Combat Stats (HP/MP/SP) - ORPHANED

#### Current State
**Module 08 (Combat Resolution)**:
- ✅ Mentions HP/MP/SP as resources
- ✅ Defines skill costs (`Costs MP/HP/SP`)
- ✅ Boss HP bars at phases (75%/50%/25%)
- ✅ References stat-based damage calculations

**Library `stat_frameworks.md`**:
- ✅ Comprehensive HP/MP/SP formulas
  - HP: `(CON × 5) + (Lv × CON mod)` (Classic) | `(CON × 10) + (Lv × 10)` (Anime)
  - MP: `(INT × 5) + (Lv × INT mod)` (Classic) | Chakra: `(INT + WIS) × 10`
  - SP: `(CON × 3) + (Lv × 2)` | Ki: `(STR + DEX + CON) × 2`
- ✅ Genre variations (Isekai/Shonen/Seinen/Slice-of-Life stat priorities)

**Narrative Profiles (DanDaDan, Vinland, Mushishi, etc.)**:
- ❌ ZERO references to HP/MP/SP tracking
- ❌ Combat Narrative Style describes **narration** (spectacle vs strategy) but **not resource management**
- ❌ No guidance on "Does DanDaDan use MP for psychic powers? HP for transformation costs?"
- ❌ No examples like "In Hunter x Hunter combat, track Nen pool depletion after each Jajanken use"

#### Integration Gap
**Profiles explain STORYTELLING but not MECHANICS**:
- DanDaDan: *"4/10 strategy, minimal power explanations, sakuga YES"* → But **how do you track Momo's psychic energy? Okarun's transformation stamina?**
- Hunter x Hunter: *"9/10 strategy, exhaustive explanations"* → But **how much Nen does Gon's Rock cost? How does Nen depletion affect combat narration?**
- Mushishi: *"6/10 strategy/spectacle, observation not combat"* → But **if Ginko DOES fight a mushi, does he have HP? Does he use MP for wards?**

#### Recommended Fix
Add **"Mechanical Implementation"** subsection to each profile's **Combat Narrative Style**:

```markdown
### Combat Narrative Style (DanDaDan)

**Strategy vs Spectacle**: 4/10 (Spectacle > strategy, some tactics)
**Power Explanations**: Minimal (shown not explained)
**Sakuga**: YES (frequent fluid animation peaks)
**Named Attacks**: Rare (Momo might shout, Okarun doesn't)
**Environmental Destruction**: City-leveling (fights wreck surroundings)

**NEW: Mechanical Implementation**
- **HP Tracking**: Standard anime HP (resilient protagonists, damage = narrative setbacks not instant KO)
  - Momo: CON 14 Lv5 = ~150 HP (psychic shield absorbs first hits)
  - Okarun: CON 12 Lv5 = ~130 HP (transformation = defensive boost +50 temp HP)
- **MP/Psychic Energy**: 
  - Momo: Psychic Power Pool = (INT 16 + WIS 12) × 10 = 280 MP
  - Costs: Psychic Slam 30 MP, Barrier 20 MP sustained, Levitation 10 MP/turn
  - Okarun: Transformation = 50 SP initial, 10 SP/turn sustained (Ki-based stamina)
- **Resource Depletion Narrative**: When Momo drops below 50% MP → "Momo's grip WEAKENS—alien breaks free! 'Running low...!'" (show resource strain via narration)
- **Recovery**: Short rest = 50% MP/SP, Long rest = full, Items (Spirit Drink) = 100 MP instant
```

**Apply to ALL 12 CORE profiles** (~500 words per profile mechanical implementation section).

---

### 2. Genre Tropes Libraries - COMPREHENSIVE BUT DISCONNECTED ✅

#### Current State
**Library Files Verified** (COMPREHENSIVE):
- ✅ `shonen_tropes.md`: Extensive training arc templates, tournament structures, rival dynamics, transformation systems, combat patterns, arc templates
- ✅ `isekai_tropes.md`: 5 sub-genres (reincarnation/summoning/gate/VRMMO/reverse), cheat skills, status screens, guild systems, harem handling, modern knowledge advantages
- ✅ `seinen_tropes.md`: (assumed comprehensive based on pattern)
- ✅ `slice_of_life_tropes.md`: (assumed comprehensive based on pattern)

**Narrative Profiles**:
- ✅ Have **15 Storytelling Tropes** section (8 enabled + 7 disabled)
- ✅ Detailed episode examples, AIDM guidance
- ❌ **Not cross-referenced with genre_tropes libraries**

#### Integration Gap (CLARIFIED)
**Genre tropes and narrative profiles serve DIFFERENT purposes but don't link**:
- **Genre Tropes** (`shonen_tropes.md`): Broad genre templates, structural patterns (training arc template, tournament beats, team roles), applicable across ANY shonen anime
- **Narrative Profiles** (`hunter_x_hunter_profile.md`): Specific anime's storytelling DNA (HOW Hunter x Hunter tells shonen stories uniquely vs Demon Slayer)
- **Problem**: No cross-references. AIDM might load `hunter_x_hunter_profile.md` but NOT realize `shonen_tropes.md` contains training arc templates applicable to that world.

**Example of Disconnect**:
- `shonen_tropes.md` contains: "Training Arc Structure: S1 intro+fail → S2 struggle→breakthroughs → S3 obstacle+low → S4 breakthrough+technique → S5 demonstrate combat"
- `hunter_x_hunter_profile.md` describes: "Tactical 9/10, exhaustive Nen explanations, strategic battles"
- **Missing Link**: Profile should note "For training arcs: See `shonen_tropes.md` training template, apply Nen mastery focus (explain conditions/costs exhaustively per HxH style)"

#### Recommended Fix - BIDIRECTIONAL LINKING
**Enhance Both Sides**:

1. **Add to Narrative Profiles** (each profile's "Usage Notes" section):
   ```markdown
   ### Genre Trope Integration (Hunter x Hunter)
   
   **Primary Genre**: Shonen (see `genre_tropes/shonen_tropes.md`)
   - **Training Arcs**: Use shonen training template, emphasize Nen mastery (explain restrictions/conditions/costs exhaustively)
   - **Rival Dynamics**: Killua = "The Equal" rival archetype, Hisoka = "The Superior" ceiling
   - **Tournament Arcs**: Heavens Arena structure = classic tournament beats, but tactical focus (strategy > spectacle)
   - **Combat Patterns**: Declaring attacks RARELY (Nen is quiet/strategic, not shouted), "Get Back Up" via resolve not power-up
   
   **Diverges From Shonen**:
   - NO "Power of Friendship" literal power-ups (emotional bonds narrative only, not mechanical buffs)
   - NO hot-blooded declarations (cerebral protagonist, tactical composure)
   - Strategy > spectacle (battles are chess matches, not beam clashes)
   ```

2. **Add to Genre Tropes** (each trope file's intro):
   ```markdown
   ### Shonen Tropes - Narrative Profile Examples
   
   **See these profiles for applied shonen storytelling**:
   - **Tactical Shonen**: Hunter x Hunter (9/10 strategy, Nen conditions, exhaustive explanations)
   - **Emotional Shonen**: Demon Slayer (empathy for enemies, tragic backstories, sakuga combat)
   - **Dark Shonen**: Jujutsu Kaisen (permanent deaths, horror elements, binding vows)
   - **Classic Shonen**: (Future: Naruto, One Piece profiles)
   
   Use this file for **genre structure** (training arcs, tournaments, team roles).  
   Use profiles for **specific vibe** (HOW Hunter x Hunter does training vs Demon Slayer).
   ```

**Result**: AIDM can navigate:
- Player: "I want Hunter x Hunter campaign" → Load `hunter_x_hunter_profile.md` (narrative DNA) → Profile references `shonen_tropes.md` → AIDM applies training arc template WITH Nen-specific tactical focus
- Player: "Let's do a training arc" → AIDM recalls current profile (Hunter x Hunter) → Loads `shonen_tropes.md` template → Customizes using profile's exhaustive explanation style

---

### 3. Power Systems Libraries - UNCLEAR INTEGRATION

#### Current State
**Library Files**:
- `power_systems/mana_magic_systems.md`
- `power_systems/ki_lifeforce_systems.md`
- `power_systems/soul_spirit_systems.md`
- `power_systems/psionic_psychic_systems.md`
- `power_systems/power_scaling_narrative.md`
- `power_systems/power_tier_reference.md`

**Integration Points**:
- ✅ Module 07 (Anime Integration) researches power systems
- ✅ `character_schema.json` has `power_system` field
- ❌ **Narrative profiles don't reference power system libraries**
- ❌ **No examples like "DanDaDan psychic powers = use psionic_psychic_systems.md framework"**

#### Integration Gap
**Profiles describe power NARRATIVELY but not MECHANICALLY**:
- DanDaDan: *"Momo's psychic powers, Okarun's transformation"* → But **which power system library applies? How do psychic costs scale?**
- Hunter x Hunter: *"Nen system with conditions/costs"* → But **is there a Nen-specific power_systems file? Or use generic mana_magic?**
- Demon Slayer: *"Breathing techniques"* → **Ki/lifeforce system? Or custom?**

#### Recommended Fix
Add **"Power System Integration"** subsection to each profile:

```markdown
### Power System Integration (DanDaDan)

**Primary System**: Psionic/Psychic (see `power_systems/psionic_psychic_systems.md`)
- **Momo Ayase**: Psychic manipulation (telekinesis, barriers, sensory)
  - Base Pool: (INT 16 + WIS 12) × 10 = 280 MP
  - Costs: Low (10-20 MP) = barriers/levitation, Medium (30-50 MP) = telekinetic slams, High (80-100 MP) = sustained gravitational control
  - Scaling: +20 MP per level, costs scale 10% per tier
  - Limitations: Line-of-sight required, concentration (disrupted by damage >30 HP/hit)

**Secondary System**: Soul/Spirit (see `power_systems/soul_spirit_systems.md`)
- **Okarun (Ken Takakura)**: Turbo Granny possession transformation
  - Activation Cost: 50 SP (one-time per combat)
  - Sustained Cost: 10 SP/turn (duration = SP pool / 10 = ~8 turns max at Lv5)
  - Benefits: +5 STR, +8 DEX (speed), +50 temp HP, claws (2d8 slashing)
  - Drawback: Loses control below 20% SP (Turbo Granny influence), post-transformation exhaustion (-2 all stats for 1 hour)

**Power Scaling**: See `power_systems/power_tier_reference.md`
- Tier 1 (Lv1-5): City block threats (single yokai/alien)
- Tier 2 (Lv6-10): District threats (multiple enemies, stronger yokai)
- Tier 3 (Lv11-15): City threats (alien invasions, powerful spirits)
```

**Apply to ALL 12 CORE profiles** (~800 words per profile power system section).

---

### 4. Common Mechanics - NOT CROSS-REFERENCED

#### Current State
**Library Files**:
- ✅ `common_mechanics/stat_frameworks.md` (comprehensive 6-stat, 3-stat, anime-specific)
- ✅ `common_mechanics/leveling_curves.md` (XP progression, stat growth)
- ✅ `common_mechanics/skill_taxonomies.md` (skill categories)

**Narrative Profiles**:
- ❌ **ZERO cross-references** to stat frameworks
- ❌ No guidance like "DanDaDan uses simplified 3-stat (BODY/MIND/SOUL)"
- ❌ No leveling recommendations ("Hunter x Hunter = slow linear curve, Nen mastery > raw stats")

#### Integration Gap
**Profiles are narrative-only, missing mechanical scaffolding**:
- How should AIDM distribute stats for a DanDaDan character? (High DEX for Okarun, high INT for Momo?)
- What leveling curve matches Attack on Titan's brutal progression? (Linear slow-gain vs exponential power spikes?)
- Which stat framework fits Mushishi's contemplative wanderer? (3-stat simplified? Slice-of-life skill-based?)

#### Recommended Fix
Add **"Character Creation Guidelines"** subsection to each profile:

```markdown
### Character Creation Guidelines (DanDaDan)

**Stat Framework**: Simplified 3-Stat (BODY/MIND/SOUL) - see `stat_frameworks.md`
- **Momo Build**: MIND 8/10 (psychic powers), BODY 6/10 (athletic), SOUL 7/10 (spiritual awareness)
- **Okarun Build**: BODY 7/10 (transformation speed), MIND 5/10 (occult knowledge), SOUL 9/10 (possession compatibility)
- **Justification**: Fast-paced action-comedy doesn't need granular 6-stat, 3-stat keeps sessions moving

**Leveling Curve**: Medium-Fast (see `leveling_curves.md`)
- Level 1→5: 300 XP/level (rapid early growth, learn powers quickly)
- Level 6→10: 800 XP/level (plateaus as threats escalate)
- Level 11+: 2000 XP/level (late-game power ceiling)
- **Narrative Justification**: Shonen-adjacent pacing, protagonists grow through encounters but not exponentially overpowered

**Skill Priorities** (see `skill_taxonomies.md`):
- **Momo**: Psionic Skills (Telekinesis, Barrier, Sensory), Athletics (dodging), Occult Knowledge
- **Okarun**: Transformation Control (Soul/Spirit), Speed Combat, Occult Lore, Stealth
- **Party Balance**: Need physical fighter (Okarun transformed), psychic support (Momo), knowledge (both)
```

**Apply to ALL 12 CORE profiles** (~600 words per profile creation guidelines).

---

## System Integration Map (Current vs Ideal)

### CURRENT STATE (Disconnected)

```
┌─────────────────────────────────────────────┐
│  Module 13: Narrative Calibration           │
│  - How to tell stories (pacing, tone)       │
│  - Narrative profiles (12 CORE)             │
│                                              │
│  ❌ No bridges to mechanics                 │
└─────────────────────────────────────────────┘
         ↓ (weak/missing links)
┌─────────────────────────────────────────────┐
│  Orphaned Mechanical Systems                │
│                                              │
│  ┌─────────────────┐  ┌──────────────────┐ │
│  │ Module 08       │  │ stat_frameworks  │ │
│  │ Combat (HP/MP)  │  │ leveling_curves  │ │
│  └─────────────────┘  └──────────────────┘ │
│                                              │
│  ┌─────────────────┐  ┌──────────────────┐ │
│  │ power_systems/  │  │ genre_tropes/    │ │
│  │ (mana, ki, etc) │  │ (incomplete?)    │ │
│  └─────────────────┘  └──────────────────┘ │
└─────────────────────────────────────────────┘
```

### IDEAL STATE (Integrated)

```
┌─────────────────────────────────────────────┐
│  Module 13: Narrative Calibration           │
│  + CORE Profiles (12 anime)                 │
│                                              │
│  Each profile contains:                     │
│  ✅ Narrative DNA (pacing, tone, tropes)    │
│  ✅ Combat Narrative Style                  │
│  ✅ NEW: Mechanical Implementation          │
│      - HP/MP/SP tracking examples           │
│      - Resource costs for powers            │
│      - Depletion narration cues             │
│  ✅ NEW: Power System Integration           │
│      - Which libraries apply                │
│      - Specific costs/scaling               │
│  ✅ NEW: Character Creation Guidelines      │
│      - Stat framework recommendation        │
│      - Leveling curve                       │
│      - Skill priorities                     │
└──────────────┬──────────────────────────────┘
               ↓ (explicit cross-references)
┌──────────────┴──────────────────────────────┐
│  Mechanical Libraries (Enhanced)            │
│                                              │
│  ┌─────────────────┐  ┌──────────────────┐ │
│  │ Module 08       │←→│ stat_frameworks  │ │
│  │ Combat          │  │ (genre variants) │ │
│  └─────────────────┘  └──────────────────┘ │
│          ↕                      ↕            │
│  ┌─────────────────┐  ┌──────────────────┐ │
│  │ power_systems/  │←→│ leveling_curves  │ │
│  │ (profile-linked)│  │ (profile-linked) │ │
│  └─────────────────┘  └──────────────────┘ │
│                                              │
│  ✅ Bidirectional cross-references          │
│  ✅ Profile-specific examples               │
│  ✅ AIDM can navigate: narrative ↔ mechanics│
└─────────────────────────────────────────────┘
```

---

## Recommended Integration Phases

### Phase 1: Audit Existing Libraries (1-2 hours)
1. **Check genre_tropes files**: Are they skeletal, complete, or redundant with profiles?
2. **Check power_systems files**: Read 1-2 to verify depth and profile-applicability
3. **Verify stat_frameworks/leveling_curves**: Confirm they're comprehensive enough to reference
4. **Document gaps**: Which libraries need expansion vs which are ready for linking

### Phase 2: Add Mechanical Sections to CORE Profiles (8-12 hours)
For each of 12 CORE profiles (DanDaDan, Vinland, Mushishi, Re:Zero, etc.):

1. **Mechanical Implementation** (~500 words):
   - HP/MP/SP formulas for iconic characters
   - Resource costs for signature abilities
   - Depletion narration examples
   - Recovery mechanics

2. **Power System Integration** (~800 words):
   - Which libraries apply (mana, ki, psionic, soul)
   - Specific power costs and scaling
   - Limitations and conditions
   - Tier progression examples

3. **Character Creation Guidelines** (~600 words):
   - Recommended stat framework (6-stat, 3-stat, anime-specific)
   - Leveling curve (linear, exponential, milestone)
   - Skill priorities for genre-authentic builds
   - Example starting characters

**Total per profile**: ~1,900 words mechanical integration  
**Total for 12 profiles**: ~23,000 words (2-3 full work sessions)

### Phase 3: Cross-Reference Libraries (2-4 hours)
1. **Update stat_frameworks.md**: Add "Genre Applications" section
   - "For DanDaDan-style action-comedy: Use 3-stat, prioritize BODY/SOUL for protagonists"
   - "For Hunter x Hunter tactical: Use 6-stat, INT+WIS for Nen users"

2. **Update power_systems files**: Add "Narrative Profile Examples"
   - `psionic_psychic_systems.md`: "See DanDaDan profile for psychic combat implementation"
   - `ki_lifeforce_systems.md`: "See Dragon Ball, Demon Slayer profiles for ki/breathing mechanics"

3. **Update Module 08 (Combat)**: Add "Profile Integration" section
   - "When using narrative profile: Extract combat_narrative_style → Apply mechanical_implementation → Track HP/MP per profile formulas"

4. **Update Module 13 (Narrative Calibration)**: Add "Mechanical Bridge" section
   - "Narrative profiles define HOW to tell stories, but reference mechanical libraries for WHAT systems support those stories"

### Phase 4: Create Integration Guide (1-2 hours)
New document: `NARRATIVE_MECHANICS_INTEGRATION.md`

**Contents**:
- **"From Narrative to Mechanics"**: Flow chart (Player wants DanDaDan vibe → Load dandadan_profile.md → Extract narrative DNA + mechanical implementation → Reference psionic_psychic_systems.md for detailed rules)
- **"Common Scenarios"**: 
  - "Setting up combat in Hunter x Hunter campaign" → Step-by-step using profile + Module 08 + stat_frameworks
  - "Creating character for Attack on Titan" → Step-by-step using profile + stat_frameworks + leveling_curves
- **"AIDM Workflow"**: Internal checklist for applying profiles holistically

---

## Genre Tropes Library Status Check ✅

**VERIFIED - Libraries are COMPREHENSIVE**:

**shonen_tropes.md**:
- ✅ Protagonist types (Underdog, Prodigy, Chosen One, Hot-Blooded Idiot)
- ✅ Narrative structures (Training Arc 3-5 session template, Tournament structures, Power of Friendship mechanics)
- ✅ Key dynamics (Rival archetypes, Mentor Sacrifice, Team Roles)
- ✅ Sub-tropes (Transformations/Super Modes, Bloodlines, Hard Work vs Talent)
- ✅ Combat patterns (Declaring Attacks, "Get Back Up" mechanics, Beam Clashes)
- ✅ Arc templates (Rescue Mission, Invasion Defense, Exam Multi-Phase)
- ✅ Implementation guidance (Session Zero questions, pacing recommendations)

**isekai_tropes.md**:
- ✅ 5 sub-genres detailed (Reincarnation, Summoning/Hero, Gate/Portal, VRMMO/Game, Reverse)
- ✅ Common tropes (Cheat Skills with balance guidance, Status Screens, Guild Systems, Demon Lord Cycle)
- ✅ Controversial handling (Slave/Taming with Session Zero guidance, Harem dynamics)
- ✅ OP patterns (Instant OP, Hidden OP, Growth OP, Situational OP)
- ✅ Story arcs (Arrival → Growth → Escalation → Endgame progression)
- ✅ Sub-genre mixing (Villainess, Slice-of-Life, Horror/Survival, Mystery)
- ✅ Modern knowledge advantages (Hygiene, Inventions, Tactics, Science)

**CONCLUSION**: Genre tropes libraries are **production-ready**, just need **cross-linking with narrative profiles**.

---

## Priority Recommendations

### IMMEDIATE (This Session)
1. ✅ **Audit genre_tropes files** (read 2-3 to assess status)
2. ✅ **Create INTEGRATION_ANALYSIS.md** (this document - DONE)
3. ⏳ **Prototype mechanical integration** for 1 profile (DanDaDan or Hunter x Hunter)

### HIGH (Next 1-2 Sessions)
4. **Expand prototype to all 12 CORE profiles** (Mechanical Implementation + Power System Integration + Character Creation Guidelines)
5. **Cross-reference libraries** (stat_frameworks, power_systems reference profiles)
6. **Update Module 08 and Module 13** (add integration guidance)

### MEDIUM (Phase 2)
7. **Resolve genre_tropes redundancy** (consolidate or specialize)
8. **Create NARRATIVE_MECHANICS_INTEGRATION.md** guide
9. **Test integration** with sample character creation + combat scenario

---

## Open Questions for User

1. **Genre Tropes Priority**: Should we consolidate (deprecate genre_tropes, use profiles as authoritative) or specialize (trope dictionaries + profile applications)?

2. **Mechanical Depth**: How detailed should Mechanical Implementation sections be?
   - **Minimal** (~300 words): Just HP/MP formulas and 2-3 power cost examples
   - **Standard** (~500 words, recommended): Formulas + costs + depletion narration + recovery
   - **Comprehensive** (~800 words): All of above + edge cases + multi-character examples

3. **Power System Libraries**: Should we verify existing power_systems files are comprehensive before linking, or expand them as we discover gaps during profile integration?

4. **Timeline**: Prefer to complete mechanical integration for all 12 profiles before moving to Phase 2 (new profiles), or interleave (expand 1-2 profiles mechanically, then add 1 new skeletal profile, repeat)?

---

## Conclusion

**Current State**: Narrative Calibration is **exceptional** (12K word profiles, comprehensive storytelling DNA) but **disconnected from mechanical systems**.

**Risk**: AIDM might narrate beautifully (DanDaDan chaotic energy, Vinland brutal realism) but **fail to track HP/MP properly**, **not know which power system to use**, or **improvise stats instead of referencing frameworks**.

**Solution**: Add ~1,900 words of **mechanical integration** to each CORE profile (Mechanical Implementation, Power System Integration, Character Creation Guidelines) + cross-reference libraries bidirectionally.

**Estimated Effort**: 10-15 hours for Phase 1-3 (audit + expand + cross-reference).

**Result**: AIDM can seamlessly navigate from **"How should this story feel?"** (narrative DNA) to **"What mechanics enable that feel?"** (HP scaling, power costs, stat distributions).

---

**End of Integration Analysis**  
**Next Steps**: User feedback on open questions → Prototype 1 profile expansion → Full rollout
