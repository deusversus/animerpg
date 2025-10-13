# AIDM Scaffolding Architecture - Implementation Plan

**Date**: October 11, 2025  
**Status**: Ready to Begin Priority 1  
**Backup**: `workspace_backup_scaffolding_integration_2025-10-11_2111.zip` (1.94 MB)

---

## System Architecture Confirmed

**AIDM is an intelligent scaffolding system** that:
1. Generates narrative profiles from ANY anime (Module 07 research → Module 13 extraction)
2. Maps narrative DNA → mechanical systems using library **templates**
3. Pre-made profiles = optional reference implementations (shortcuts for popular anime)

**NOT a prescriptive database** - AIDM thinks and generates intelligently

---

## Integration Issues Found

**7 Critical Findings** (see `MODULE_INTEGRATION_AUDIT.md` for full details):

1. 🔴 **Module 12/13 No Mapping** - Power Fantasy scale → Growth model (missing)
2. 🔴 **Module 09 No Mapping** - Fast/Slow scale → XP multiplier (missing)
3. 🟡 **Module 01 Flow Undocumented** - Genre library integration unclear
4. 🟡 **Module 02 No Memory Category** - Can't store profile adjustments
5. 🔴 **Missing Scaffolding Examples** - Pre-made profiles don't show mapping decisions
6. 🟡 **Module 13 Incomplete** - No scaffolding section
7. 🟡 **Module 03 No State** - Generated profiles can't persist (CRITICAL)

**Root Cause**: Module 13 extracts narrative DNA but doesn't map to mechanics

---

## Implementation Plan

### Priority 1: Scaffolding Rules (6-8 hours) - **START HERE**

**Task 1**: Add "Narrative DNA → Mechanical Scaffolding" to Module 13 (2-3 hours)

Location: `aidm/instructions/13_narrative_calibration.md`

Add section after "Integration with Existing Modules" (~1,500-2,000 words):

```markdown
## Narrative DNA → Mechanical Scaffolding

AIDM uses narrative DNA to intelligently select game systems. These mapping rules
apply to BOTH pre-made and generated profiles.

### Power Level Mapping (Module 12 Integration)

**Power Fantasy Scale → Growth Model**:

- **0-2 (OP protagonist)**: Instant OP model
  - Start Tier 5 (cosmic power level)
  - Narrative pivot from session 1 (focus internal conflict, philosophy)
  - Combat narration assumes victory, spotlight NPCs
  - Examples: Overlord, One Punch Man, Slime isekai
  
- **3-6 (Balanced power)**: Accelerated model
  - Start Tier 1, reach Tier 3 by session 15
  - Standard power growth with faster pivot
  - Combat challenges scale with player
  - Examples: Most shonen (Naruto, Demon Slayer, MHA)
  
- **7-10 (Underdog struggle)**: Modest model
  - Start Tier 1, slow progression (Tier 2 by session 20)
  - Death possible, struggle emphasized
  - Combat remains challenging throughout
  - Examples: Re:Zero, Attack on Titan, Hunter x Hunter (early arcs)

**Application**: When generating profile, check Power Fantasy scale → Select growth model → 
Configure Module 12 accordingly

### Progression Pacing Mapping (Module 09 Integration)

**Fast vs Slow Scale → XP Multiplier**:

- **0-3 (Fast-paced)**: High XP model
  - 1,000-1,500 XP per session
  - Rapid level growth matches narrative velocity
  - L1-5 in 5-8 sessions, L10 in 15-20 sessions
  - Examples: DanDaDan, Trigger anime, tournament arcs
  
- **4-6 (Moderate pacing)**: Standard XP model
  - 600-900 XP per session
  - Balanced growth rate
  - L1-5 in 8-12 sessions, L10 in 30-40 sessions
  - Examples: Most shonen, balanced narratives
  
- **7-10 (Slow contemplative)**: Low XP or milestone-only
  - 300-500 XP per session OR milestone-based progression
  - Growth de-emphasized, focus on atmosphere/character
  - Level progression secondary to narrative
  - Examples: Mushishi, slice-of-life, philosophical seinen

**Special Case - Arc Length Consideration**:
- Episodic (2-5 session arcs) + Fast-paced → High XP (complete arc = significant growth)
- Serialized (13-25 session arcs) + Moderate → Standard XP (growth spans multiple arcs)

**Application**: Check Fast vs Slow scale + Arc Length → Select XP model → 
Configure Module 09 session XP targets

### Combat System Mapping (Module 08 Integration)

**Tactical vs Instinctive Scale → Stat Framework**:

- **0-3 (Instinctive combat)**: 3-stat framework
  - Body, Mind, Spirit (simplified)
  - Combat narration focuses on spectacle, outcomes
  - Minimal tactical depth, rule of cool emphasized
  - Examples: Pure action anime, spectacle-focused
  
- **4-6 (Balanced)**: 6-stat framework
  - STR, DEX, CON, INT, WIS, CHA (standard)
  - Moderate tactical complexity
  - Mix of strategy and spectacle
  - Examples: Most shonen, balanced approach
  
- **7-10 (Tactical mastery)**: 6-stat + custom mechanics
  - Standard stats + anime-specific systems (Nen conditions, Domain rules)
  - Exhaustive tactical explanations
  - Strategic planning emphasized
  - Examples: Hunter x Hunter, Code Geass, Death Note

**Strategy vs Spectacle → Combat Narration**:
- Spectacle (0-3): Describe chaos/visuals, outcomes not tactics, minimal mechanics
- Balanced (4-6): Explain key tactical decisions + epic moments
- Strategy (7-10): Exhaustive breakdown, explain every choice, chess-like

**Application**: Check Tactical scale → Select stat framework → 
Configure Module 08 combat_narrative_style parameters

### Power System Mapping (Libraries Integration)

**Based on anime's power type + Explained vs Mysterious scale**:

**Psychic/Telekinetic Powers**:
- Load: `power_systems/psionic_psychic_systems.md`
- MP costs based on Tactical scale (High tactical = lower costs + more control)
- Explained 0-3 → Minimal rules, mysterious limits, narrative flexibility
- Explained 7-10 → Exhaustive rules, clear costs/limits, mechanical precision
- Examples: Mob Psycho 100, DanDaDan (Momo), Saiki K

**Martial Arts/Physical Enhancement**:
- Load: `power_systems/ki_lifeforce_systems.md`
- SP costs, stamina-focused (physical exertion)
- Tactical scale determines technique complexity
- Examples: Dragon Ball, Naruto (taijutsu), most martial arts anime

**Magic/Spells**:
- Load: `power_systems/mana_magic_systems.md`
- MP costs, spell slot systems if Tactical 7+
- Explained scale determines rule depth (vancian magic vs narrative casting)
- Examples: Fairy Tail, Black Clover, Frieren

**Metaphysical/Soul Powers**:
- Load: `power_systems/soul_spirit_systems.md`
- Mixed HP/MP costs (life force + spiritual energy)
- Often involves permanent costs/consequences
- Examples: Jujutsu Kaisen (cursed energy), Bleach (spiritual pressure)

**Custom/Unique Systems** (Nen, Stands, Devil Fruits, Alchemy):
- Reference closest library template as starting point
- Create custom mechanics based on research
- Explained scale determines documentation depth
- Document in power_system_schema.json for campaign

**Application**: Identify power type from research → Load appropriate library → 
Apply Tactical + Explained scales → Generate cost formulas + limitations

### Attribute Priority Mapping

**Based on combat style + power type**:

**Physical Combat Focus** (low Tactical, martial arts):
- Prioritize: STR (damage), CON (durability), DEX (speed)
- Secondary: WIS (combat sense), CHA (presence)
- De-emphasize: INT (unless tactical elements)

**Strategic Combat Focus** (high Tactical, mind games):
- Prioritize: INT (strategy), WIS (perception), CHA (manipulation)
- Secondary: DEX (reflexes), CON (endurance)
- De-emphasize: STR (physical force less relevant)

**Balanced Combat**:
- Distribute evenly or based on protagonist archetype
- Allow player customization within archetype

**Application**: Check Tactical scale + Power type → Recommend attribute priorities → 
Guide character creation (Module 06)

---

## Integration Notes

**For Pre-Made Profiles**:
- Include "Mechanical Scaffolding (Reference Implementation)" section
- Show example mapping decisions for this specific anime
- AIDM uses as template when generating similar profiles

**For Generated Profiles**:
- Apply mapping rules automatically during Session Zero
- Store selected systems in active_narrative_profile
- Persist via Module 03 state tracking (full data, not just ID)

**Validation**:
- Profile adjustments stored in Module 02 NARRATIVE_STYLE memory
- State persistence via Module 03 export/import
- Cross-reference with Module 04 (NPC), Module 05 (Narrative), Module 08 (Combat)
```

**Deliverable**: ~1,500-2,000 words of mapping guidance in Module 13

---

**Task 2**: Add scaffolding examples to 12 CORE profiles (2-3 hours)

For EACH profile (DanDaDan, HxH, JJK, Demon Slayer, AoT, Konosuba, Death Note, Re:Zero, Mushishi, Vinland Saga, Code Geass, Haikyuu):

Add section after example scenes (~500-700 words):

```markdown
## Mechanical Scaffolding (Reference Implementation)

This section shows how AIDM maps [Anime]'s narrative DNA to game mechanics.
Use as template for similar profiles ([genre] with [key traits]).

### Power Level (Module 12)
- Power Fantasy: X/10 ([description])
- **Maps to**: [Growth model] - [reasoning]
- [Specific implementation notes]

### Progression (Module 09)
- Fast-Paced: X/10 ([description])
- **Maps to**: [XP model] - [reasoning]
- [Session/level expectations]

### Combat System (Module 08)
- Tactical: X/10 ([description])
- Strategy vs Spectacle: X/10
- **Maps to**: [Stat framework] - [reasoning]
- [Combat narration approach]

### Power System
- [Power type] ([protagonist ability])
- **Libraries**: [specific .md files]
- **Costs**: [MP/SP/HP formulas based on scales]
- **Explained**: X/10 → [rule depth approach]

### Attribute Priorities
- **Primary**: [attributes] ([reasoning])
- **Secondary**: [attributes]
- **De-emphasize**: [attributes] ([reasoning])

### Character Creation Notes
- [Recommended starting approach]
- [Common archetypes for this anime]
- [Pitfalls to avoid]
```

**Example (DanDaDan)**:

```markdown
## Mechanical Scaffolding (Reference Implementation)

This section shows how AIDM maps DanDaDan's narrative DNA to game mechanics.
Use as template for similar profiles (absurd supernatural action with rapid tonal shifts).

### Power Level (Module 12)
- Power Fantasy: 4/10 (protagonists struggle but grow, threats scale rapidly)
- **Maps to**: Accelerated growth model
  - Start Tier 1 (street level), reach Tier 3 (national threats) by session 15
  - Combat remains challenging due to absurd threat escalation
  - Narrative pivot begins at Tier 3 (focus on relationship dynamics + existential questions)
- **Reasoning**: Protagonists aren't OP but grow quickly to match escalating chaos

### Progression (Module 09)
- Fast-Paced: 2/10 (rapid narrative velocity, frequent climaxes)
- **Maps to**: High XP model (1,000-1,500 XP per session)
  - L1-5 in 5-8 sessions (first major arc)
  - L6-10 in next 8-12 sessions (second arc)
  - Rapid level growth supports constant escalation
- **Reasoning**: Fast pacing = rapid power-ups to match threat escalation

### Combat System (Module 08)
- Tactical: 5/10 (some strategy but spectacle emphasized)
- Strategy vs Spectacle: 4/10 (lean spectacle)
- **Maps to**: 6-stat framework (balanced, not oversimplified)
  - Prioritize: DEX (speed), CON (durability), INT (Momo's psychic control)
  - Combat narration: Chaotic spectacle + key tactical moments
  - Sakuga ON, named attacks OFF, destruction scale HIGH
- **Reasoning**: Needs tactical depth for Momo's abilities but spectacle dominates

### Power System
- Psychic (Momo: telekinesis, barriers, channeling) + Spirit possession (Okarun: speed, strength)
- **Libraries**: psionic_psychic_systems.md + soul_spirit_systems.md
- **Costs**: 
  - Momo psychic: MP-intensive (Tactical 5 = moderate costs), formula: [Power level × 3 MP]
  - Okarun transformation: SP-based (physical), cost: 10 SP activation + 5 SP/round
- **Explained**: 4/10 (some rules, mostly mysterious) → Loose costs, narrative flexibility
  - Don't over-systematize, preserve chaos vibe

### Attribute Priorities
- **Momo**: INT (psychic power), WIS (spirit sense), CON (durability)
- **Okarun**: DEX (transformation speed), CON (physical combat), WIS (ghost sense)
- **De-emphasize**: CHA (romance subplot but not social focus), STR (speed over strength)

### Character Creation Notes
- Expect dual protagonists or ensemble (Module 12 ensemble focus at Tier 3+)
- Psychic characters: High INT, moderate MP pool
- Possessed/transformed: High DEX/CON, SP-based abilities
- Avoid: Pure martial builds (doesn't fit supernatural focus), overly tactical (chaos > strategy)
```

**Deliverable**: ~500-700 words per profile × 12 = ~6,000-8,400 words total

---

**Task 3**: Add narrative profile state tracking to Module 03 (2-3 hours)

Location: `aidm/instructions/03_state_manager.md`

Add section after existing state components:

```markdown
### Narrative Profile State

**Purpose**: Track active narrative calibration (CRITICAL for generated profiles)

**Tracked Data**:
- `active_profile_id`: String (e.g., "narrative_hxh", "generated_chainsaw_man", "custom_blend_001")
- `profile_sources`: Array of profile IDs if blended (e.g., ["narrative_hxh", "narrative_aot"])
- `profile_type`: Enum ("pre_made", "generated", "custom", "blended")
- `profile_scales`: Object with 10 scale values (0-10 each)
  - introspection_vs_action, comedy_vs_drama, simple_vs_complex, power_fantasy_vs_struggle,
    explained_vs_mysterious, fast_vs_slow, episodic_vs_serialized, grounded_vs_absurd,
    tactical_vs_instinctive, hopeful_vs_cynical
- `profile_tropes`: Object with 15 trope switches (boolean ON/OFF)
  - fourth_wall, inner_monologue, visual_metaphor, rapid_tonal_shifts, tournament_arcs,
    power_of_friendship, tragic_backstories, escalating_threats, slice_of_life, mystery_box,
    unreliable_narrator, existential_philosophy, rule_of_cool, mundane_to_epic, tragic_hero
- `profile_pacing`: Object (scene_length, arc_length, climax_frequency, downtime_percent)
- `profile_tone`: Object (primary_emotions array, violence_level, fanservice, horror, optimism)
- `profile_dialogue`: Object (formality, exposition_method, banter_frequency, declarations, philosophy_combat, awkward_comedy)
- `profile_combat`: Object (strategy_vs_spectacle, power_explanations, sakuga, named_attacks, destruction_scale)
- `adjustments_log`: Array of adjustment objects
  - {session: number, adjustment: string, reason: string, timestamp: ISO8601}
- `last_calibration_session`: Integer (session number of last adjustment)
- `mechanical_scaffolding`: Object (selected systems based on mapping rules)
  - growth_model: string ("instant_op", "accelerated", "modest")
  - xp_model: string ("high", "standard", "low", "milestone_only")
  - stat_framework: string ("3_stat", "6_stat", "6_stat_custom")
  - power_systems: array of library references (["psionic_psychic_systems", "soul_spirit_systems"])
  - attribute_priorities: object ({primary: [], secondary: [], deemphasize: []})

**Storage Differentiation**:

**Pre-Made Profiles** (e.g., "narrative_hxh"):
- Store: `active_profile_id`, `profile_type: "pre_made"`, `adjustments_log`, `mechanical_scaffolding`
- Scales/tropes/styles: Reference library file (don't duplicate)
- Size: ~500-800 bytes

**Generated Profiles** (e.g., "generated_chainsaw_man"):
- Store: Full profile data (all scales, tropes, pacing, tone, dialogue, combat)
- CRITICAL: Can't reference file (doesn't exist), must persist complete data
- Size: ~3,000-5,000 bytes
- Include research_sources for validation

**Custom/Blended Profiles**:
- Store: Full data + `profile_sources` array
- Document which scales from which source

**Validation Rules**:
- Verify `active_profile_id` format (alphanumeric + underscores only)
- If `profile_type: "pre_made"`, verify file exists in narrative_profiles library
- Validate scale values (0-10 integer range)
- Validate trope switches (boolean only)
- Check `adjustments_log` chronological order (session numbers ascending)
- Verify `mechanical_scaffolding` references valid Module 09/12 options

**Export/Import**:
- Include complete narrative_profile object in session export
- On import validation:
  - If pre-made profile, verify file exists (warn if missing, offer recalibration)
  - If generated profile, restore full data
  - Validate adjustments_log integrity
  - Restore mechanical_scaffolding selections

**State Persistence**:
- Save narrative_profile with every state update
- Load on session restart (preserve calibration)
- Preserve across error recovery (Module 10)
- Include in session export for campaign transfers

**Integration**:
- Module 13 (Narrative Calibration): Populates this state during Session Zero
- Module 02 (Learning Engine): NARRATIVE_STYLE memory references this for adjustments
- Module 06 (Session Zero): Creates initial state
- Module 07 (Anime Integration): Generates profile data for new anime
```

**Deliverable**: ~800-1,000 words of state tracking specification

---

### Priority 2: Storage & Flow (4-6 hours) - After Priority 1

**Tasks**:
1. Add NARRATIVE_STYLE memory category to Module 02 (2 hours)
2. Document cognitive engine flow in Module 01 (1-2 hours)
3. Cross-link genre libraries ↔ profiles (1-2 hours)

---

### Priority 3: Genre Libraries + More Examples (14-20 hours) - After Priority 2

**Tasks**:
1. Create 6 missing genre tropes libraries (8-12 hours)
   - seinen_tropes.md, shoujo_tropes.md, mecha_tropes.md
   - sports_tropes.md, thriller_tropes.md, slice_of_life_tropes.md
2. Add more scaffolding examples to profiles (6-8 hours)

---

## Next Steps

1. **Read this plan completely** ✓
2. **Begin Task 1**: Open `aidm/instructions/13_narrative_calibration.md`
3. **Add scaffolding section** after line ~185 (after "Integration with Existing Modules")
4. **Continue to Task 2**: Update all 12 profiles
5. **Complete Task 3**: Update Module 03

**Estimated Time**: 6-8 hours for Priority 1 complete

---

## Success Criteria

**Priority 1 Complete When**:
- ✅ Module 13 has "Narrative DNA → Mechanical Scaffolding" section (~1,500-2,000 words)
- ✅ All 12 CORE profiles have scaffolding examples (~500-700 words each)
- ✅ Module 03 tracks narrative profile state (generated profiles can persist)
- ✅ Can test intelligent profile generation for anime NOT in library

**Ready to Begin!** 🚀
