# Module 13 Integration Audit - Critical Findings

**Date**: Phase 3 Integration Analysis (Updated with Scaffolding Architecture)  
**Scope**: Module 13 (Narrative Calibration) coordination with core AIDM modules  
**Status**: 🔴 CRITICAL DISCONNECTS FOUND → ✅ SCAFFOLDING APPROACH DEFINED → ✅ **PRIORITY 1 COMPLETE**

**Implementation Status**:
- ✅ **Priority 1 COMPLETE** (October 12, 2025):
  - Task 1: Added scaffolding rules to Module 13 (~1,200 words) ✅
  - Task 2: Added scaffolding examples to 12 CORE profiles (~1,000-2,500 words each) ✅
  - Task 3: Added state tracking to Module 03 (~2,500 words) ✅
- ✅ **Priority 2 COMPLETE** (October 12, 2025):
  - Task 1: Added NARRATIVE_STYLE memory category to Module 02 (~600 words) ✅
  - Task 2: Documented narrative flow in Module 01 (~2,000 words) ✅
  - Task 3: Cross-linked genre libraries ↔ profiles (4 libraries + 3 profile examples) ✅
- ⏳ **Priority 3**: Genre libraries, testing, roadmap update (14-20 hours)

## CRITICAL ARCHITECTURAL CLARIFICATION

**AIDM is NOT a prescriptive database** - It's an intelligent scaffolding system:

- ✅ **Narrative Profile Generator**: Automatically extracts DNA from ANY anime via Module 07 research
- ✅ **Mechanical Scaffolding System**: Maps narrative DNA → appropriate game systems using library templates ✅
- ✅ **Modular Pre-Made Profiles**: Optional convenience shortcuts (DanDaDan, HxH, etc. = examples with scaffolding sections ✅, not requirements)

**Libraries = Templates, Not Rules**:
- `power_systems/` = Pattern templates AIDM references when mapping powers to mechanics
- `genre_tropes/` = Pattern libraries for profile generation (NOT complete, missing seinen/shoujo/mecha/sports/thriller/slice-of-life)
- `stat_frameworks/` = Mapping guidance ("Tactical anime 7-10 → 6-stat framework")

**Pre-Made Profiles = Reference Implementations** ✅:
- **NOW INCLUDE**: "Mechanical Scaffolding (Reference Implementation)" sections showing mapping decisions
- Show example mappings ("DanDaDan Fast-Paced 2/10 → High XP model 1K-1.5K/session, Accelerated growth")
- AIDM uses as templates when generating new profiles
- NOT prescriptive mechanics, but scaffolding examples

---

## Executive Summary

**User Concern**: "Is Module 13 respecting other systems? Is Module 12 even necessary with narrative calibration? The OP protag part feels redundant."

**Verdict**: ⚠️ **PARTIAL INTEGRATION** - Module 13 exists in isolation from critical mechanical systems, creating redundancies and missing coordination points.

**Integration Score**: 4/13 modules actively integrate with Module 13  
**Critical Gaps**: 8 modules don't reference narrative calibration (including core systems like Cognitive Engine, Learning Engine, Progression, Player Agency)

### Critical Findings

| Finding | Severity | Impact |
|---------|----------|--------|
| **Module 12 Power Level Agency** completely ignored by Module 13 | 🔴 CRITICAL | System has 2 separate OP protagonist handling systems with no coordination |
| **Module 09 Progression** not referenced in narrative calibration | 🔴 CRITICAL | Fast-paced anime get same XP as slow anime, no mechanical support for narrative pacing |
| **Module 01 Cognitive Engine** doesn't explicitly route to narrative profiles | 🟡 MEDIUM | Genre libraries → anime profiles flow exists but undocumented |
| **Module 02 Learning Engine** has no narrative profile tailoring mechanism | 🟡 MEDIUM | No memory category for genre-specific storytelling patterns |
| **Module 03 State Manager** doesn't track narrative profile state | 🟡 MEDIUM | No validation or persistence for active narrative calibration |
| **Combat stats (HP/MP/SP)** orphaned from narrative calibration | 🔴 CRITICAL | (From Phase 2) Profiles don't explain mechanical tracking |
| **Module 13 incomplete integration documentation** | 🟡 MEDIUM | Lists only 3 modules (04/05/07), ignores 4 modules that actively use it (06/08) |

### Module-by-Module Integration Status

**✅ GOOD INTEGRATION** (4 modules actively use Module 13):
1. **Module 04 (NPC Intelligence)**: ✅ Checks `dialogue_style` parameters before generating dialogue
2. **Module 05 (Narrative Systems)**: ✅ Explicitly states "Module 13 FILTERS all narrative rules"
3. **Module 06 (Session Zero)**: ✅ Has "Phase 0.5: NARRATIVE CALIBRATION" section
4. **Module 08 (Combat Resolution)**: ✅ Checks `combat_narrative_style` parameters before narration

**🟡 MENTIONED BUT NOT INTEGRATED** (1 module):
5. **Module 00 (System Initialization)**: 🟡 Lists narrative profiles library location, no workflow

**❌ ZERO INTEGRATION** (8 modules):
6. **Module 01 (Cognitive Engine)**: ❌ Doesn't mention narrative profiles in intent handling
7. **Module 02 (Learning Engine)**: ❌ No narrative style memory category
8. **Module 03 (State Manager)**: ❌ No narrative profile state tracking
9. **Module 07 (Anime Integration)**: ❌ Mentions extracting narrative DNA but doesn't reference Module 13 storage
10. **Module 09 (Progression)**: ❌ No narrative pacing coordination
11. **Module 10 (Error Recovery)**: ❌ No narrative profile error handling
12. **Module 11 (Dice Resolution)**: ❌ No narrative-influenced dice mechanics
13. **Module 12 (Player Agency)**: ❌ No coordination with Module 13 Power Fantasy scale

**Module 13 Self-Documentation**: Lists only 3 modules (04/05/07) in integration section, **missing 06/08 which actively use it**

### Bottom Line

**Module 13 extracts narrative DNA but doesn't map to mechanics**, creating **disconnected systems**:
- **Module 13 (Narrative DNA)**: DanDaDan has "Fast-Paced 2/10" scale, "Absurdity 9/10", rapid tonal shifts
- **Module 12 (Power Scaffolding)**: Has Tier 1-5 power level system with narrative pivot rules at T3-5
- **Module 09 (Progression Scaffolding)**: Has XP pacing estimates (L1-3 fast, L10+ legendary)

**Missing**: Mapping rules showing "Fast-Paced 2/10 → High XP model" or "Power Fantasy 4/10 → Accelerated growth model"  
**They don't talk to each other** = AIDM can't intelligently scaffold mechanics from narrative DNA

---

## Finding 1: Module 12 Power Level Agency Redundancy

### Current State

**Module 12 (Player Agency)** contains extensive OP protagonist handling:

**3 Growth Models** (Session Zero choice):
- **Modest**: Traditional linear (T1 → T2 over 20 sessions)
- **Accelerated**: Isekai exponential (T1 → T3 in 15 sessions)
- **Instant OP**: Saitama-style (start T5 godlike, no growth)

**5 Power Tiers with Narrative Pivot System**:
- **T1 Street (L1-5)**: Combat challenges, tactical narration, death possible
- **T2 City (L6-10)**: Player handles most, bosses challenge, intrigue layers
- **T3 National (L11-15)**: 🔄 **PIVOT BEGINS** - Regular enemies trivial, focus shifts to RP/politics/morals
- **T4 Global (L16-20)**: 🔄 **ENSEMBLE CRITICAL** - Spotlight allies, player mentors, outcomes foregone
- **T5 Cosmic (L21+)**: 🔄 **FULL PIVOT** - Combat = storytelling device, philosophical questions, internal conflict

**Combat Narration Templates by Tier**:
- T1-2: Tactical (`"Roll dodge, take 8 damage"`)
- T3: Outcomes (`"Deflect effortlessly, army morale breaks"`)
- T4: Spectacle (`"Mountain splits, army erased"`)
- T5: Assume victory (`"Threat erased. Real question: your daughter watched you kill her father"`)

**Session Zero Questions**:
- "Growth rate preference? Modest/Accelerated/Instant OP?"
- "Comfortable with ensemble spotlight at high tiers?"
- "Power fantasy vs struggle?"
- "Tier 5 goals? (Philosophy? Godhood? Retirement?)"
- "De-powering acceptable?"

**Module 13 (Narrative Calibration)** has:

**1 Power Fantasy Scale**:
- **Power Fantasy vs Struggle**: 0 = OP hero (Overlord), 10 = underdog (Re:Zero)
- No tier system
- No level breakpoints
- No combat narration guidelines
- No Session Zero questions about power level

### Integration Analysis

**Module 13 mentions Module 12**: ❌ **ZERO TIMES**

Searched entire Module 13 for:
- "player agency" - 0 results
- "module 12" - 0 results  
- "OP protagonist" - 1 result (in Spartan Custom Worlds example: "C) Isekai Power (Overlord, Slime): OP protagonist, empire-building")
- "overpowered" - 0 results
- "tier" - 0 results
- "power level" - 0 results

**Module 12 mentions Module 13**: ❌ **ZERO TIMES**

Searched Module 12 for:
- "narrative calibration" - 0 results
- "module 13" - 0 results
- "narrative profile" - 0 results
- "storytelling" - 0 results

**Integration Notes in Module 12**:
> *"Integration: Works with Session Zero, Narrative Systems (Module 05), Combat (Module 08), Progression (Module 09), NPC Systems"*

Lists Module 05 (narrative), but NOT Module 13 (narrative calibration).

**Integration Notes in Module 13**:
> *"Integration: Pairs with Module 07 (research), Module 05 (narrative), Module 04 (NPC dialogue), all combat/exploration narration"*

Lists Module 04, 05, 07, but NOT:
- Module 08 (combat resolution) - even though Module 08 actively uses narrative profiles
- Module 12 (player agency) - zero coordination with Power Level Agency system
- Module 09 (progression) - no pacing coordination
- Module 06 (session zero) - even though Session Zero Phase 0.5 is narrative calibration

**Module 13's Integration Section** (lines 177-184):
```markdown
## Integration with Existing Modules

**Module 05 (Narrative Systems)**: Generic rules → Filtered through profile  
*Example*: "Pacing" rule = DanDaDan (Fast:8) = 2-3 exchanges max | Mushishi (Slow:9) = scenes linger

**Module 07 (Anime Integration)**: Research mechanics AND narrative DNA simultaneously  
*Process*: Research power systems → Extract narrative profile → Harmonize → Calibrate voice

**Module 04 (NPC Intelligence)**: NPC dialogue filtered through profile  
*Example*: DanDaDan (Banter:Frequent) = awkward small talk | AoT (Formal, Banter:Rare) = efficient military brevity
```

**Lists only 3 modules (04, 05, 07)** - doesn't mention:
- Module 08 (combat) which actively uses it
- Module 06 (session zero) which implements it
- Module 12 (player agency) where coordination needed
- Module 09 (progression) where pacing integration needed

### The Problem

**AIDM has 2 separate OP protagonist systems**:

**System A (Module 12 - Mechanical)**: 
- Tier-based with level breakpoints
- Narrative pivot rules (T3 begins, T5 full pivot)
- Combat narration templates
- Ensemble focus requirements
- Session Zero questions

**System B (Module 13 - Vibes)**: 
- Single 0-10 scale
- No mechanical integration
- No tier system
- No pivot rules
- Generic "power fantasy vs struggle" vibe

**Real-World Scenario**:

Player: *"I want One Punch Man vibes!"*

**Module 12 says**: Use Instant OP growth model → Start Tier 5 → Full narrative pivot from session 1 → Combat narration assumes victory, focus on internal conflict/philosophy → Ensemble spotlight critical

**Module 13 says**: Power Fantasy scale = 0 (OP hero) → No further guidance

**What actually happens?**: 
- If AIDM loads Module 12 → Gets mechanical tier system
- If AIDM loads Module 13 → Gets vibe scale
- They don't coordinate → Player gets inconsistent experience

**Example Conflict**:

Overlord anime profile (Module 13): Power Fantasy 0/10, Combat 2/10 strategy (outcomes not tactics)

Module 12 Instant OP model: Start T5, combat narration assumes victory, focus NPCs

**Are they the same thing?** YES, but expressed differently with no cross-reference.

### Recommendations

**Option A: Cross-Reference (RECOMMENDED)**
- Add to Module 13 narrative profiles: 
  - `"Power Level Integration: [Anime] typical protagonist arc = [Module 12 Growth Model]"`
  - `"Overlord = Instant OP (Tier 5 start), Naruto = Modest growth (Tier 1→3 over 50+ sessions), Konosuba = Modest BUT comedic failures maintain T1-2 tension despite level growth"`
- Add to Module 12 Power Level Agency section:
  - `"See Module 13 narrative profiles for genre-appropriate power level expectations"`
  - `"Instant OP model commonly found in: Overlord, One Punch Man, Slime isekai (check narrative profile for storytelling approach)"`
- **Effort**: ~2 hours (add notes to 12 CORE profiles + Module 12 integration section)
- **Benefit**: Systems coordinate, users get both mechanical AND vibe guidance

**Option B: Consolidate**
- Merge Module 12 Power Level Agency into Module 13
- Make narrative calibration the authoritative OP protagonist system
- Add mechanical tier breakpoints to narrative profiles
- **Effort**: ~8 hours (restructure Module 12, expand all narrative profiles)
- **Risk**: Loses Module 12's Session Zero questions and clear tier boundaries

**Option C: Keep Separate (CURRENT STATE, NOT RECOMMENDED)**
- Leave as-is
- Accept redundancy
- Hope users figure it out
- **Benefit**: No work required
- **Risk**: User confusion, inconsistent experiences, wasted development effort

---

## Finding 2: Module 09 Progression Pacing Ignored

### Current State

**Module 09 (Progression Systems)** defines:

**XP Awards**:
- Combat: Base × Challenge Modifier (Trivial ×0.1, Fair ×1.0, Deadly ×2.0, Boss ×3.0)
- Quests: Minor 100, Standard 300, Major 750, Epic 2000 (× quality)
- Roleplay: 25-100 per meaningful scene
- Discovery: 150 per major revelation
- Milestones: 50-500 for story beats

**Session XP Estimates**:
- Low roleplay: 300-500 XP
- Standard mix: 600-900 XP
- High multi-combat: 1,000-1,500 XP
- Epic boss sessions: 2,000+ XP

**Progression Pacing**:
- L1-3: Fast (2-3 sessions per level)
- L4-6: Moderate (4-5 sessions per level)
- L7-9: Slow (6-8 sessions per level)
- L10+: Legendary (10+ sessions per level)

**Module 13 (Narrative Calibration)** defines:

**Pacing Scale**:
- **Fast vs Slow**: 0 = rapid (Trigger anime), 10 = contemplative (Mushishi)
- **Arc Length**: 2-5 sessions / 6-12 sessions / 13-25 sessions
- **Climax Frequency**: Frequent / Moderate / Rare
- **Downtime %**: Low / Medium / High

**Example Profiles**:
- **DanDaDan**: Fast-Paced 2/10, arc length 6-12 sessions, frequent climaxes
- **Mushishi**: Slow-Paced 9/10, arc length 2-5 sessions (episodic), rare climaxes, high downtime
- **Attack on Titan**: Fast-Paced 4/10, arc length 13-25 sessions (serialized), frequent climaxes

### Integration Analysis

**Module 13 mentions Module 09**: ❌ **ZERO TIMES**

Searched Module 13 for:
- "progression" - 0 results
- "leveling" - 0 results
- "XP" - 0 results
- "module 09" - 0 results
- "experience points" - 0 results

**Module 09 mentions Module 13**: ❌ **ZERO TIMES**

Searched Module 09 for:
- "narrative calibration" - 0 results
- "module 13" - 0 results
- "pacing" - 2 results (both internal progression pacing, not narrative pacing)
- "fast-paced" - 0 results
- "slow-paced" - 0 results

**Integration Notes in Module 09**:
> *"Integration: Works with State Manager (tracks XP), Combat (awards XP), Narrative (milestone XP), Learning Engine (remembers progression), Player Agency"*

Lists "Narrative" (Module 05) but not Module 13.

**Integration Notes in Module 13**:
> *"Integration: Pairs with Module 07 (research), Module 05 (narrative), Module 04 (NPC dialogue), all combat/exploration narration"*

Does NOT list Module 09.

### The Problem

**Narrative pacing and mechanical pacing are disconnected**:

**DanDaDan profile says**: Fast-Paced 2/10 (rapid cuts, frequent climaxes, 6-12 session arcs)

**Module 09 says**: Standard XP = 600-900/session → L1-3 in 2-3 sessions, L10 in ~40+ sessions

**What SHOULD happen**: DanDaDan's fast narrative pacing = accelerated XP gains (1,000-1,500/session) to match story velocity

**What ACTUALLY happens**: AIDM uses standard XP regardless of narrative pacing → Fast anime feel slow mechanically

**Example Conflict**:

**Mushishi Campaign** (Slow-Paced 9/10, episodic 2-5 session arcs, contemplative):
- Player expects: Slow power growth, focus on atmosphere and philosophy
- Module 09 gives: Standard 600-900 XP/session → L1-3 in 2-3 sessions (same as DanDaDan)
- **Mechanical pace contradicts narrative pace**

**Attack on Titan Campaign** (Fast-Paced 4/10, serialized 13-25 session arcs):
- Player expects: Rapid escalation, high stakes, frequent power-ups
- Module 09 gives: Standard 600-900 XP/session → L10 in ~40 sessions
- **Could reach L10 before finishing single 25-session arc** → Wrong feel

### Recommendations

**Option A: Add Mechanical Pacing Guidance to Profiles (RECOMMENDED)**

Add to each narrative profile's **Character Creation Guidelines** section:

```markdown
### Progression Pacing Integration (Module 09)

**[Anime] Recommended XP Model**:
- **Session XP**: [Low 300-500 / Standard 600-900 / High 1K-1.5K / Epic 2K+]
- **Rationale**: [Anime] [Fast/Slow]-Paced [X/10] scale means [narrative feels rushed/glacial] with standard XP
- **Level Expectations**: 
  - **Early game (L1-5)**: [X] sessions ([faster/slower] than Module 09 standard)
  - **Mid game (L6-10)**: [X] sessions
  - **Late game (L11-15)**: [X] sessions
- **Arc-Level Alignment**: 
  - Typical [Anime] arc = [X] sessions → Expect [Y] levels gained per arc
  - Major climax = L[X] milestone (time with major story beat)

**Example**: 
- DanDaDan 6-12 session arc (frequent climaxes) → Recommend High XP (1K-1.5K/session) → L1-5 in first arc, L6-10 in second arc
- Mushishi 2-5 session episodes (contemplative) → Recommend Low XP (300-500/session) → L1-3 over 3-4 episodes, emphasize atmospheric growth not power scaling
```

**Add to Module 09**:

```markdown
### Narrative Pacing Integration (Module 13)

**Adjust XP rates based on narrative profile pacing**:

- **Fast-Paced Anime (0-3 scale)**: High XP model (1K-1.5K/session) to match rapid story velocity
  - Examples: DanDaDan, Trigger anime, battle shonen tournament arcs
  - Players expect: Frequent power-ups, rapid escalation
  
- **Moderate Pacing (4-6 scale)**: Standard XP model (600-900/session)
  - Examples: Hunter x Hunter, Attack on Titan, most battle shonen
  - Players expect: Steady growth balanced with story

- **Slow-Paced Anime (7-10 scale)**: Low XP model (300-500/session) OR narrative milestones only
  - Examples: Mushishi, slice-of-life, contemplative seinen
  - Players expect: Growth de-emphasized, focus on character/atmosphere

**See Module 13 narrative profiles for specific anime recommendations.**
```

**Effort**: ~3-4 hours (add section to 12 CORE profiles + Module 09 integration)  
**Benefit**: Mechanical pacing matches narrative pacing, consistent experience

**Option B: Dynamic XP Scaling**

Add rule to Module 09:
- If narrative profile Fast-Paced ≤3 → XP × 1.5
- If narrative profile Slow-Paced ≥7 → XP × 0.6
- **Effort**: ~30 minutes (add rule to Module 09)
- **Risk**: Oversimplified, doesn't account for arc structure or genre expectations

**Option C: Ignore (CURRENT STATE, NOT RECOMMENDED)**
- Accept that all anime get same XP pacing
- DanDaDan takes 40 sessions to L10 just like Mushishi
- **Risk**: Breaks immersion, mechanical pace contradicts narrative tone

---

## Finding 3: Cognitive Engine Flow Undocumented

### Current State

**Module 01 (Cognitive Engine)** workflow:

```
BEFORE EVERY RESPONSE:
1. Deep Read: Consume 100% of player input
2. Memory Check: Load last 5 conversation turns
3. State Validation: Verify HP/MP/SP/inventory/location
4. Response Planning: Classify intent → Determine response layers
```

**Intent Classification** (7 categories):
- NARRATIVE, MECHANICAL, SOCIAL, META, CREATIVE, EXPLORATION, COMBAT

**Multi-Intent Priority**:
- META > COMBAT > SOCIAL > MECHANICAL > NARRATIVE > EXPLORATION > CREATIVE

**Intent Handling Examples**:
- CREATIVE intent detected → Load "Yes, and..." collaborative world-building
- Anime mentioned → **ANIME RESEARCH GATE** → Load Module 07 → External research → Extract profile

**Integration Notes**:
> *"Integration: Works with Module 05 (narrative), Module 07 (anime integration), Session State, Memory (Module 02)"*

**Mentions Module 07 (anime integration) but NOT Module 13 (narrative profiles)**

### Additional Module Integration Findings

After checking **ALL** instruction modules, found:

**✅ GOOD INTEGRATION** (4 modules actively reference Module 13):
1. **Module 04 (NPC Intelligence)**: Explicitly checks `narrative_profile_schema.json` → `dialogue_style` parameters before generating NPC dialogue
2. **Module 05 (Narrative Systems)**: States "Module 13 FILTERS all narrative rules" with examples (DanDaDan vs AoT vs Konosuba)
3. **Module 06 (Session Zero)**: Has entire "Phase 0.5: NARRATIVE CALIBRATION" section, loads profiles from library
4. **Module 08 (Combat Resolution)**: Checks `combat_narrative_style` parameters (strategy/spectacle, power explanations, sakuga, named attacks, destruction)

**❌ NO INTEGRATION** (7 modules don't mention Module 13):
1. **Module 00 (System Initialization)**: Mentions narrative profiles library location but not integration workflow
2. **Module 01 (Cognitive Engine)**: ❌ Doesn't mention narrative profiles (THIS FINDING)
3. **Module 02 (Learning Engine)**: ❌ No narrative style memory category (Finding 4)
4. **Module 03 (State Manager)**: ❌ No narrative profile state tracking
5. **Module 09 (Progression)**: ❌ No narrative pacing coordination (Finding 2)
6. **Module 10 (Error Recovery)**: ❌ No narrative profile error handling
7. **Module 11 (Dice Resolution)**: ❌ No narrative-influenced dice mechanics
8. **Module 12 (Player Agency)**: ❌ No narrative profile coordination (Finding 1)

### User Question

> "Are stories using the cognitive engine > genre library -> anime profile?"

### Analysis

**Expected Flow**:
1. Player says: *"I want Hunter x Hunter vibes!"*
2. Cognitive Engine classifies: NARRATIVE intent (campaign setup)
3. Loads: `genre_tropes/shonen_tropes.md` (genre library)
4. Loads: `narrative_profiles/hunter_x_hunter_profile.md` (anime profile)
5. Applies: Tactical combat 10/10, exhaustive explanations, strategic narration

**Actual Flow** (from Module 01):
1. Player says: *"I want Hunter x Hunter vibes!"*
2. Cognitive Engine classifies: NARRATIVE intent
3. **ANIME RESEARCH GATE** triggered → Load Module 07
4. Module 07: Research anime → Extract profile → **HANDOFF TO MODULE 13**
5. Module 13: Load `hunter_x_hunter_profile.md` → Apply scales/tropes

**Genre Libraries (`genre_tropes/shonen_tropes.md`) Role**: ❓ **UNCLEAR**

Module 01 doesn't mention:
- `genre_tropes/` directory
- Loading genre libraries before anime profiles
- Flow from genre → specific anime

**Genre libraries exist and are comprehensive** (verified Phase 2):
- `shonen_tropes.md` (protagonist types, training arcs, tournament structures, power systems)
- `isekai_tropes.md` (summoning, cheat skills, harem, guild systems)

**But when are they loaded?** Not documented in Module 01.

### Integration Analysis

**Module 13 Quick Access Workflow 1**:

```
Player: "I want Hunter x Hunter vibes!"

AIDM:
1. Open `aidm/libraries/narrative_profiles/hunter_x_hunter_profile.md`
2. Copy all scales/tropes/styles → active_narrative_profile
3. Set profile_sources = ["narrative_hxh"]
4. Reference profile's example scenes during gameplay
```

**No mention of genre libraries in this workflow.**

**Module 13 Quick Access Workflow 2**:

```
Player: "I want dark fantasy with strategy."

AIDM:
1. Open `PROFILE_INDEX.md` cross-reference matrix
2. Find: "Tactical combat" → HxH, "Dark and brutal" → AoT
3. Present both profiles to player (show example scenes)
4. Blend profiles based on player preference
```

**Uses PROFILE_INDEX cross-reference, not genre libraries.**

### The Problem

**Genre libraries are orphaned**:

1. **Module 01 (Cognitive Engine)** doesn't mention loading genre libraries
2. **Module 13 (Narrative Calibration)** workflows bypass genre libraries entirely (direct to anime profiles)
3. **Genre libraries exist** (`shonen_tropes.md`, `isekai_tropes.md`) but have no documented integration point

**Expected**:
- Player wants "shonen vibes but not specific anime" → Load `shonen_tropes.md` → Use base shonen profile
- Player wants "Hunter x Hunter" → Load `shonen_tropes.md` (context) → Load `hunter_x_hunter_profile.md` (specific)

**Actual** (undocumented):
- Player wants "Hunter x Hunter" → Jump directly to `hunter_x_hunter_profile.md`
- Genre libraries = reference material for AIDM developers? Not runtime system component?

### Recommendations

**Option A: Document Genre Library Integration (RECOMMENDED)**

Add to **Module 01 (Cognitive Engine)** intent handling:

```markdown
### NARRATIVE Intent + Genre Request

**Player requests genre without specific anime**:

Flow: NARRATIVE intent → Load genre library → Apply base profile

Example:
Player: "I want shonen vibes!"
1. Classify: NARRATIVE intent (campaign setup)
2. Load: `genre_tropes/shonen_tropes.md`
3. Present: "Shonen (Naruto, MHA style): Optimistic, friendship, tournaments? 
            OR more specific anime?"
4. If player confirms → Use shonen base profile (Module 13)
5. If player names anime → ANIME RESEARCH GATE (Module 07 → Module 13)
```

Add to **Module 13 (Narrative Calibration)** workflows:

```markdown
### Workflow 0: Player Requests Genre Only

Player: "I want shonen vibes but not a specific anime."

AIDM:
1. Load `genre_tropes/shonen_tropes.md` (reference material)
2. Use shonen base profile:
   - Power Fantasy: 4/10 (underdog with growth)
   - Comedy: 5/10 (balanced with drama)
   - Tactical: 6/10 (strategy matters but not overwhelming)
   - Hopeful: 2/10 (optimistic)
   - Tropes ON: Power of friendship, Training arcs, Tournament arcs, Escalating threats
3. Ask 2-3 tweaks: "More tactical (HxH style)? More comedy (Gintama)? Darker (JJK)?"
4. Document in profile_sources = ["genre_shonen"]
```

**Effort**: ~1 hour (add workflow to Module 01 + Module 13)  
**Benefit**: Genre libraries have clear purpose, players can request genre without anime

**Option B: Eliminate Genre Libraries**

- Remove `genre_tropes/` directory
- All genre requests redirect to anime profiles
- "I want shonen" → "Which shonen? Naruto? HxH? MHA?"
- **Effort**: None (just document current state)
- **Waste**: Phase 2 verified genre libraries are comprehensive and production-ready

**Option C: Cross-Link Profiles ↔ Genre Libraries**

Add to each anime profile:

```markdown
### Genre Library References

**[Anime] uses these shonen tropes**:
- See `genre_tropes/shonen_tropes.md` Section 2.3 (Underdog Protagonist)
- See `genre_tropes/shonen_tropes.md` Section 4.1 (Training Arc: Mentor-Student)
- See `genre_tropes/shonen_tropes.md` Section 5.2 (Tournament Arc: Bracketed)
```

Add to genre libraries:

```markdown
### Anime Examples

**Underdog Protagonist** examples:
- Naruto (`naruto_profile.md` - Power Fantasy 6/10, optimistic)
- Hunter x Hunter (`hunter_x_hunter_profile.md` - Power Fantasy 7/10, strategic)
- My Hero Academia (`mha_profile.md` - Power Fantasy 5/10, hopeful)
```

**Effort**: ~4-6 hours (bidirectional cross-linking 12 profiles + 2 genre libraries)  
**Benefit**: Genre libraries become navigation aid, profiles show trope usage

---

## Finding 4: Learning Engine Narrative Tailoring Unclear

### Current State

**Module 02 (Learning Engine)** memory architecture:

**6 Memory Categories**:
1. **CORE**: Immutable origin/rules, heat 100 permanent, never decays
2. **CHARACTER_STATE**: Stats/skills/equipment, normal decay
3. **RELATIONSHIPS**: NPC bonds, slow decay
4. **QUESTS**: Active hot, completed fast decay
5. **WORLD_EVENTS**: Major changes, slow decay
6. **CONSEQUENCES**: Ripple effects, fast decay

**Special Subcategories**:
- **PLAYER_ESTABLISHED_RULE** (CORE memory, heat 100): Player says "In this world, magic requires blood sacrifice" → Permanent rule, check before contradicting
- **PLAYER_FEEDBACK** (RELATIONSHIPS memory, heat 90): Player says "Too serious, needs more chaos" → Apply immediately in next response, persist until session end

**Heat Index 0-100**:
- 90-100: Critical (always in context)
- 70-89: High priority
- 50-69: Moderate
- 30-49: Low
- 10-29: Background
- 0-9: Cold storage

**Decay Rates**:
- None: CORE memories
- Slow (-2/session): RELATIONSHIPS, WORLD_EVENTS
- Normal (-5/session): CHARACTER_STATE, most memories
- Fast (-10/session): QUESTS (completed), CONSEQUENCES

### User Question

> "Is the learning engine being used appropriately to tailor genre and anime specific stories?"

### Analysis

**Expected**: Learning engine stores narrative profile preferences and applies genre-specific patterns

**Example**:
- Player in DanDaDan campaign
- Memory stores: "Rapid tonal shifts Comedy→Tension" (genre pattern)
- AIDM detects quiet moment → Injects absurd chaos (tailored to DanDaDan vibe)

**Actual** (from Module 02): ❓ **NO EXPLICIT NARRATIVE TAILORING MECHANISM**

**Closest mechanisms**:
1. **PLAYER_FEEDBACK subcategory**: Player says "Too serious" → Adjust immediately
2. **CORE memories**: Campaign setup includes anime choice → Permanent context

But no **NARRATIVE_STYLE** or **GENRE_PATTERN** memory category.

**Module 02 Integration Notes**:
> *"Integration: Works with all modules (provides memory), especially State Manager, Narrative Systems, NPC Systems"*

Mentions "Narrative Systems" (Module 05) but NOT Module 13.

**Module 13 Profile Adjustments**:

```json
"adjustments_log": [
  {"session": 3, "adjustment": "Drama 7→4, Absurdity 5→8", 
   "reason": "Player: 'too serious, needs chaos'"},
  {"session": 5, "adjustment": "Enabled Fourth Wall Breaks", 
   "reason": "Player enjoyed meta-humor"}
]
```

**Stored WHERE?** Module 13 describes tracking adjustments, but doesn't specify memory category.

### The Problem

**Narrative profile adjustments have no clear storage mechanism**:

1. **Module 13 says**: Track profile adjustments in JSON, apply to future narration
2. **Module 02 says**: Store memories in 6 categories (none for narrative style)
3. **Integration unclear**: Where are "Drama 7→4" adjustments stored? CORE? PLAYER_FEEDBACK? Custom category?

**Scenario**:

Session 3: Player says *"Too serious, needs more chaos"*

**Module 13 workflow**:
1. Adjust profile: Drama 7→4, Absurdity 5→8
2. Log adjustment: `{"session": 3, "adjustment": "Drama 7→4, Absurdity 5→8", "reason": "Player: too serious"}`
3. Apply immediately to narration

**Module 02 workflow**:
1. Classify feedback: PLAYER_FEEDBACK subcategory (RELATIONSHIPS memory)
2. Set heat: 90 (apply immediately)
3. Decay: Slow (-2/session)
4. But PLAYER_FEEDBACK is for **NPC relationship preferences**, not narrative style

**Mismatch**: Module 13 adjustments should be **CORE** (permanent like narrative profile choice), but PLAYER_FEEDBACK is **RELATIONSHIPS** (slow decay).

### Recommendations

**Option A: Add NARRATIVE_STYLE Memory Category (RECOMMENDED)**

Add to **Module 02 (Learning Engine)**:

```markdown
### 7. NARRATIVE_STYLE

**Purpose**: Stores genre-specific patterns and narrative profile adjustments

**Examples**:
- "DanDaDan campaign: Rapid tonal shifts Comedy→Tension"
- "Player prefers absurd chaos over serious drama (Drama 7→4, Absurdity 5→8)"
- "Hunter x Hunter campaign: Exhaustive power explanations expected"
- "Konosuba campaign: Failures should be comedic not tragic"

**Heat Management**:
- **Profile Choice** (anime selected): Heat 100, never decays (CORE-equivalent)
- **Profile Adjustments** (player feedback): Heat 90, slow decay (-2/session)
  - If reinforced (player says again): Heat → 100 (permanent)
- **Genre Patterns** (observed preferences): Heat 70-80, normal decay

**Storage**:
{
  "category": "NARRATIVE_STYLE",
  "subcategory": "PROFILE_ADJUSTMENT",
  "content": "Drama scale 7→4, Absurdity 5→8",
  "reason": "Player: 'too serious, needs chaos'",
  "session_created": 3,
  "heat": 90,
  "decay_rate": -2
}

**Integration**: Works with Module 13 (narrative calibration), Module 05 (narrative systems)
```

Add to **Module 13 (Narrative Calibration)**:

```markdown
### Profile Adjustments Storage (Module 02)

**All profile adjustments stored in NARRATIVE_STYLE memory category**:

Player feedback: "Too serious, needs chaos"

AIDM Internal:
1. Adjust profile: Drama 7→4, Absurdity 5→8
2. Create memory:
   - Category: NARRATIVE_STYLE
   - Subcategory: PROFILE_ADJUSTMENT
   - Heat: 90 (apply immediately, persist)
   - Decay: Slow (-2/session, but reinforcement → 100 permanent)
3. Reference in narration: Check NARRATIVE_STYLE memories before every response
```

**Effort**: ~2 hours (add category to Module 02, update Module 13 storage workflow)  
**Benefit**: Clear storage mechanism, narrative adjustments persist appropriately

**Option B: Use Existing PLAYER_FEEDBACK (Current Implicit State)**

- Document that PLAYER_FEEDBACK already handles narrative style adjustments
- Profile adjustments = relationship preference (player's relationship with story tone)
- **Effort**: ~30 minutes (clarify in Module 02 + Module 13)
- **Risk**: Confusing category name (RELATIONSHIPS for narrative style?)

**Option C: Store in CORE with Profile**

- Narrative profile = CORE memory (heat 100, never decays)
- All adjustments modify CORE memory directly
- **Effort**: ~30 minutes (document in Module 13)
- **Risk**: CORE intended for immutable rules, but profiles adjust over time

---

## Finding 5: Combat Stats Integration (Phase 2 Finding)

*(Consolidated from INTEGRATION_ANALYSIS.md)*

### Current State

**Module 08 (Combat Systems)** defines:
- HP (Health Points): Damage tracking, 0 HP = unconscious/death
- MP (Mana Points): Spell/ability resource costs
- SP (Stamina Points): Physical ability resource costs

**Narrative Profiles** define:
- Combat style (strategy vs spectacle)
- Power explanations (never/minimal/exhaustive)
- Sakuga moments, named attacks, destruction scale

**Gap**: Profiles don't explain how HP/MP/SP work in their anime

**Example**: DanDaDan profile doesn't answer:
- How much MP does Momo's psychic slam cost?
- How much HP does Okarun have at Level 5?
- Does DanDaDan use 6-stat (STR/DEX/CON/INT/WIS/CHA) or 3-stat (Body/Mind/Spirit)?

### Recommendation

*(Same as INTEGRATION_ANALYSIS.md - add 3 sections to each profile)*

Add to each narrative profile:

**1. Mechanical Implementation (~500 words)**:
- HP/MP/SP tracking for this anime's power system
- Stat framework (6-stat, 3-stat, custom)
- Resource costs for iconic abilities
- Example character sheet (Level 1 and Level 10)

**2. Power System Integration (~800 words)**:
- Links to `power_systems/` library (psychic, martial arts, magic, etc.)
- How anime's power system maps to AIDM mechanics
- Custom mechanics if needed (DanDaDan spirit energy, HxH Nen conditions)

**3. Character Creation Guidelines (~600 words)**:
- Session Zero questions for this anime
- Recommended starting stats
- Class/archetype suggestions
- Progression pacing (see Finding 2)

**Effort**: ~10-15 hours for 12 CORE profiles  
**Benefit**: Full mechanical integration, no more improvised tracking

---

## Finding 6: Module 13 Incomplete Integration Documentation

### Current State

**Module 13 Integration Section** (lines 177-184):

```markdown
## Integration with Existing Modules

**Module 05 (Narrative Systems)**: Generic rules → Filtered through profile  
**Module 07 (Anime Integration)**: Research mechanics AND narrative DNA simultaneously  
**Module 04 (NPC Intelligence)**: NPC dialogue filtered through profile
```

**End of Module 13**:
> *"Integration: Pairs with Module 07 (research), Module 05 (narrative), Module 04 (NPC dialogue), all combat/exploration narration"*

**Lists only 3 modules**: 04 (NPC), 05 (Narrative), 07 (Anime Integration)

### The Problem

**Module 13 doesn't acknowledge modules that actively use it**:

**Missing from Module 13's integration section**:
1. **Module 06 (Session Zero)**: Has entire "Phase 0.5: NARRATIVE CALIBRATION" section that loads profiles
2. **Module 08 (Combat Resolution)**: Checks `combat_narrative_style` parameters before every combat narration

**Module 13 says**: "Pairs with Module 04 (NPC dialogue)"  
**Module 13 doesn't say**: "Pairs with Module 08 (combat narration)" - even though Module 08 explicitly checks narrative profile

**Result**: Incomplete documentation makes it unclear which modules integrate with narrative calibration

### Integration Analysis

**Modules that USE Module 13 (checked their code)**:
- ✅ Module 04 (NPC) - **Documented in Module 13** ✓
- ✅ Module 05 (Narrative) - **Documented in Module 13** ✓
- ✅ Module 06 (Session Zero) - **NOT documented in Module 13** ✗
- ✅ Module 08 (Combat) - **NOT documented in Module 13** ✗

**Modules Module 13 claims integration with**:
- ✅ Module 04 (NPC) - Confirmed ✓
- ✅ Module 05 (Narrative) - Confirmed ✓
- ✅ Module 07 (Anime Integration) - Confirmed ✓
- ❌ "all combat/exploration narration" - Vague, should explicitly list Module 08

**Asymmetric documentation**:
- Module 08 → Module 13: ✅ "Check narrative profile before combat narration"
- Module 13 → Module 08: ❌ Not mentioned (only "all combat narration")

### Recommendations

**Option A: Complete Module 13 Integration Section (RECOMMENDED)**

Update Module 13 integration section to:

```markdown
## Integration with Existing Modules

**Module 04 (NPC Intelligence)**: NPC dialogue filtered through profile dialogue_style parameters
*Example*: DanDaDan (Banter:Frequent) = awkward small talk | AoT (Formal, Banter:Rare) = efficient military brevity

**Module 05 (Narrative Systems)**: Generic narrative rules filtered through profile scales
*Example*: "Pacing" rule = DanDaDan (Fast:8) = 2-3 exchanges max | Mushishi (Slow:9) = scenes linger

**Module 06 (Session Zero)**: Phase 0.5 loads narrative profile from library before character creation
*Process*: Player names anime → Load profile → Calibrate tone → Integrate with character concept

**Module 07 (Anime Integration)**: Research extracts mechanics AND narrative DNA simultaneously
*Process*: Research power systems → Extract narrative profile → Harmonize → Calibrate voice

**Module 08 (Combat Resolution)**: Combat narration filtered through profile combat_narrative_style parameters
*Example*: DanDaDan (Strategy:4, Sakuga:ON) = chaotic spectacle | HxH (Strategy:9) = tactical analysis

**Module 12 (Player Agency)**: Power Level Agency tier system coordinates with Power Fantasy scale
*See Finding 1 in MODULE_INTEGRATION_AUDIT.md for coordination guidelines*

**Module 09 (Progression Systems)**: Narrative pacing influences XP award rates
*See Finding 2 in MODULE_INTEGRATION_AUDIT.md for pacing integration*
```

**Effort**: ~1 hour (rewrite integration section, add cross-references)  
**Benefit**: Complete documentation, clear module relationships

**Option B: Add Integration Checklist**

Add to Module 13 end:

```markdown
### Modules Using Narrative Calibration

**ALWAYS check these modules coordinate with active narrative profile**:
- [x] Module 04: NPC dialogue style
- [x] Module 05: Narrative pacing/tone
- [x] Module 06: Session Zero calibration
- [x] Module 08: Combat narration
- [ ] Module 09: Progression pacing (see Finding 2)
- [ ] Module 12: Power Level Agency (see Finding 1)
```

**Effort**: ~15 minutes  
**Benefit**: Quick reference, identifies gaps

---

## Finding 7: Module 03 State Manager Doesn't Track Narrative Profile

### Current State

**Module 03 (State Manager)** tracks:
- Character stats (HP/MP/SP, attributes, skills)
- Inventory (items, equipment, currency)
- Location (current, visited)
- Quest log (active, completed)
- Time (session, in-game)
- Relationships (NPC affinities)

**Module 03 does NOT track**:
- ❌ Active narrative profile (which anime/custom profile loaded)
- ❌ Narrative profile adjustments (Drama 7→4, Absurdity 5→8)
- ❌ Profile sources (["narrative_hxh"] or blended)

### The Problem

**Narrative calibration has no state persistence**:

Session 5: Player says *"Too serious, needs chaos"*  
→ Module 13 adjusts: Drama 7→4, Absurdity 5→8  
→ Where is this stored?

**Module 13 says**: Store in `narrative_profile_schema.json` with adjustments log

**Module 03 (State Manager)** doesn't mention narrative profile in:
- Current state schema
- Export schema
- Validation checks
- State persistence

**Result**: Unclear if narrative profile survives:
- Session restarts (AIDM reloaded)
- Export/import (campaign transferred)
- State rollbacks (error recovery)

### Integration Analysis

**Module 13 adjustment tracking** (lines 200-209):

```json
"adjustments_log": [
  {"session": 3, "adjustment": "Drama 7→4, Absurdity 5→8", 
   "reason": "Player: 'too serious, needs chaos'"},
  {"session": 5, "adjustment": "Enabled Fourth Wall Breaks", 
   "reason": "Player enjoyed meta-humor"}
]
```

**Module 03 export schema** (needs verification):
- Character data: ✅ Exported
- Inventory: ✅ Exported
- Quest log: ✅ Exported
- Narrative profile: ❓ Not documented

**If narrative profile NOT in state export** → Campaign loses calibration on transfer

### Recommendations

**Option A: Add Narrative Profile to State Manager (RECOMMENDED)**

Add to Module 03:

```markdown
### Narrative Profile State

**Tracked Data**:
- `active_profile_id`: String ("narrative_hxh", "custom", "default")
- `profile_sources`: Array of profile IDs if blended (["narrative_hxh", "narrative_aot"])
- `profile_scales`: Current scale values (0-10 for each of 10 scales)
- `profile_tropes`: Current trope switches (ON/OFF for each of 15 tropes)
- `profile_adjustments_log`: Array of adjustments with session/reason
- `last_calibration_session`: Integer (session number of last adjustment)

**Validation**:
- Verify profile_id exists in narrative_profiles library
- Validate scale values 0-10
- Validate trope switches boolean
- Check adjustments_log format

**Export/Import**:
- Include narrative_profile in session export
- Validate on import (profile exists in destination AIDM)
- Warn if profile not found (offer default or recalibration)

**State Persistence**:
- Save narrative profile with every state update
- Load on session restart
- Preserve across error recovery
```

**Effort**: ~2-3 hours (add to Module 03, update export schema, test persistence)  
**Benefit**: Narrative calibration survives session restarts, campaign transfers

**Option B: Document Current Implicit State**

- Clarify that narrative profile = CORE memory (Module 02)
- Profile stored in memory system, not state manager
- **Effort**: ~30 minutes
- **Risk**: Memory system may decay/compress (not intended for active state)

---

## Consolidated Recommendations

### Priority 1: Critical Coordination (Next Session) - 8-10 hours

1. **Module 12 ↔ Module 13 Cross-Reference** (2 hours)
   - Add power level integration section to all 12 CORE narrative profiles
   - Add narrative profile references to Module 12 Power Level Agency
   - Resolve redundancy with explicit coordination
   - **Finding 1 fix**

2. **Module 09 ↔ Module 13 Pacing Guidance** (3-4 hours)
   - Add progression pacing section to all 12 CORE narrative profiles
   - Add narrative pacing integration to Module 09
   - Align mechanical XP with narrative velocity
   - **Finding 2 fix**

3. **Update Module 13 Integration Documentation** (1 hour)
   - Add Module 06 (Session Zero) and Module 08 (Combat) to integration section
   - Add Module 12 and Module 09 cross-references
   - Complete integration checklist
   - **Finding 6 fix**

4. **Add Narrative Profile to State Manager** (2-3 hours)
   - Extend Module 03 with narrative profile state tracking
   - Update export/import schema
   - Add validation for profile persistence
   - **Finding 7 fix**

### Priority 2: Storage & Flow Documentation (Next 1-2 Sessions) - 4-6 hours

5. **Add NARRATIVE_STYLE Memory Category** (2 hours)
   - Extend Module 02 with 7th category
   - Update Module 13 adjustment storage workflow
   - Clear persistence mechanism for profile adjustments
   - **Finding 4 fix**

6. **Document Cognitive Engine Flow** (1-2 hours)
   - Add genre library workflow to Module 01
   - Add genre-only request workflow to Module 13
   - Clarify when genre libraries are loaded vs anime profiles
   - **Finding 3 fix (partial - documentation only)**

7. **Cross-Link Genre Libraries ↔ Profiles** (1-2 hours)
   - Bidirectional references between profiles and genre_tropes
   - Navigation aid for users browsing library
   - **Finding 3 fix (complete)**

### Priority 3: Scaffolding Examples + Genre Libraries - 14-20 hours

8. **Add Scaffolding Examples to Pre-Made Profiles** (6-8 hours)
   - Add "Mechanical Scaffolding (Reference Implementation)" section to 12 CORE profiles
   - Show example mapping decisions (~500-700 words per profile)
   - NOT prescriptive mechanics, but templates for generated profiles
   - **Finding 5 fix (reframed from Phase 2)**

9. **Complete Genre Tropes Libraries** (8-12 hours)
   - Create missing pattern libraries: seinen, shoujo, mecha, sports, thriller, slice-of-life
   - Templates for profile generation when player requests genre without specific anime
   - **Finding 3 fix (complete)**

### Total Effort Estimate

- **Priority 1**: 6-8 hours (scaffolding rules + coordination)
- **Priority 2**: 4-6 hours (storage & documentation)
- **Priority 3**: 14-20 hours (scaffolding examples + genre libraries)
- **TOTAL**: 24-34 hours (3-4 work sessions)

---

## User Decisions Needed

### Decision 1: Module 12/13 Scaffolding Rules

**Question**: Add mapping rules from Power Fantasy scale → Growth model in Module 13?

**Options**:
- **A. Add Scaffolding Mapping Rules** (2-3 hours) [RECOMMENDED - SCAFFOLDING APPROACH]
  - Add to Module 13: "Narrative DNA → Mechanical Scaffolding" section
  - **Mapping**: Power Fantasy 0-2 → Instant OP (T5), 3-6 → Accelerated (T3 by session 15), 7-10 → Modest (slow tier progression)
  - Pre-made profiles show examples: "Overlord Power Fantasy 0/10 → Instant OP model"
  - **Benefit**: AIDM can intelligently scaffold ANY anime, pre-made profiles = templates
  - **Effort**: ~2-3 hours (add mapping section + examples to 12 profiles)
  
- **B. Consolidate Systems** (8+ hours) - Merge Module 12 into Module 13
  - **Risk**: Loses Module 12's mechanical clarity
  - **Not recommended**: Scaffolding approach better preserves both
  
- **C. Keep Disconnected** (0 hours) - No mapping rules
  - **Risk**: AIDM can't generate mechanics from narrative DNA

**Your Choice**: A (Scaffolding approach confirmed by user)

### Decision 2: Progression Pacing Scaffolding

**Question**: Add mapping rules from Fast/Slow scale → XP multiplier in Module 13?

**Options**:
- **A. Add Scaffolding Mapping Rules** (2-3 hours) [RECOMMENDED - SCAFFOLDING APPROACH]
  - Add to Module 13: Pacing scaffolding section
  - **Mapping**: Fast 0-3 → High XP (1K-1.5K/session), Moderate 4-6 → Standard (600-900), Slow 7-10 → Low (300-500) or milestone-only
  - Pre-made profiles show examples: "DanDaDan Fast-Paced 2/10 → High XP model"
  - **Benefit**: AIDM intelligently scaffolds XP for generated profiles
  - **Effort**: ~2-3 hours (add mapping section + examples)
  
- **B. Dynamic Formula Only** (30 min) - Simple multiplier
  - **Risk**: Oversimplified, no nuance
  
- **C. No Mapping** (0 hours) - All anime same XP
  - **Risk**: Breaks immersion

**Your Choice**: A (Scaffolding approach confirmed)

### Decision 3: Module 13 Scaffolding Documentation

**Question**: Add "Narrative DNA → Mechanical Scaffolding" section to Module 13?

**Options**:
- **A. Complete Scaffolding Section** (2-3 hours) [RECOMMENDED - SCAFFOLDING APPROACH]
  - Add comprehensive mapping rules for all integrations
  - Power Level, Progression, Combat, Power System mappings
  - Examples from pre-made profiles as templates
  - **Benefit**: AIDM can scaffold ANY anime mechanics from narrative DNA
  
- **B. Integration Checklist Only** (15 min) - Quick reference
  - **Risk**: No mapping guidance for generation
  
- **C. No Update** (0 hours)
  - **Risk**: AIDM can't generate profiles intelligently

**Your Choice**: A (Scaffolding approach confirmed)

### Decision 4: State Tracking for Generated Profiles

**Question**: Should Module 03 track narrative profiles (critical for on-the-fly generation)?

**Options**:
- **A. Add to State Manager** (2-3 hours) [RECOMMENDED - CRITICAL FOR GENERATION]
  - Track: active_profile_id, profile_sources, scales, tropes, adjustments
  - **Generated profiles**: Full data must persist (not just reference ID)
  - **Pre-made profiles**: Can store reference ID only
  - Include in export/import, validate on session restart
  - **Benefit**: Generated profiles survive session restarts, campaign transfers
  
- **B. Document Memory Storage** (30 min) - Use CORE memory
  - **Risk**: Memory may compress, unsuitable for active state
  
- **C. No Tracking** (0 hours) - Regenerate every session
  - **Risk**: Lose generated profiles + adjustments on restart
  - **CRITICAL FAILURE**: Can't support on-the-fly generation

**Your Choice**: A (Critical for scaffolding approach)

### Decision 5: Narrative Style Memory Category

**Question**: How should narrative profile adjustments be stored in Module 02?

**Options**:
- **A. New Category** (2 hours) - Add NARRATIVE_STYLE to Module 02 [RECOMMENDED]
  - Explicit category for genre patterns and profile adjustments
  - Heat 90-100, slow decay (reinforcement → permanent)
  - **Benefit**: Clear storage mechanism, appropriate persistence
  
- **B. Use PLAYER_FEEDBACK** (30 min) - Document existing subcategory usage
  - Profile adjustments = player feedback
  - **Risk**: Confusing category name (RELATIONSHIPS for narrative style?)
  
- **C. Store in CORE** (30 min) - Adjustments modify CORE memory directly
  - **Risk**: CORE intended for immutable rules, but profiles adjust over time

**Your Choice**: ___________

### Decision 6: Cognitive Engine Flow Documentation

**Question**: Should Module 01 explicitly document genre library → anime profile flow?

**Options**:
- **A. Document Flow** (1 hour) - Add workflows to Module 01 + Module 13 [RECOMMENDED]
  - Explicit steps: "Genre request → Load genre_tropes → Load anime profile"
  - Workflow for genre-only requests
  - **Benefit**: Clear integration point, genre libraries have documented purpose
  
- **B. Eliminate Genre Libraries** (0 hours) - All requests redirect to anime profiles
  - "I want shonen" → "Which shonen? Naruto? HxH?"
  - **Waste**: Genre libraries are comprehensive and production-ready
  
- **C. Cross-Link Only** (1-2 hours) - Bidirectional references, no flow documentation
  - Profiles ↔ genre_tropes references
  - **Risk**: Integration point still unclear

**Your Choice**: ___________

### Decision 7: Timeline

**Question**: When to implement scaffolding fixes?

**Options**:
- **A. Immediate Priority 1** (This session) - Start scaffolding rules (6-8 hours)
  - Add Narrative DNA → Mechanical Scaffolding section to Module 13
  - Add mapping examples to pre-made profiles
  - Add state tracking for generated profiles
  - Critical for intelligent profile generation
  
- **B. Review First** (Next session) - User reviews scaffolding approach
  - Validate architectural understanding
  - Prototype one profile with scaffolding examples
  
- **C. Phased** (Gradual) - Priority 1 now, Priority 2-3 later
  - Scaffolding rules + coordination now (6-8 hours)
  - Storage/documentation next (4-6 hours)
  - Genre libraries + examples later (14-20 hours)

**Your Choice**: A (Begin scaffolding implementation confirmed)

---

## Summary of All Findings

**7 Integration Issues Found**:

1. **🔴 Module 12/13 Redundancy** - No mapping rules: Power Fantasy scale → Growth model
2. **🔴 Module 09 Pacing Ignored** - No mapping rules: Fast/Slow scale → XP multiplier
3. **🟡 Module 01 Flow Undocumented** - Genre libraries integration unclear
4. **🟡 Module 02 No Narrative Memory** - No category for profile adjustments (generated or pre-made)
5. **🔴 Missing Scaffolding Examples** - Pre-made profiles don't show mapping decisions (Phase 2 reframed)
6. **🟡 Module 13 Incomplete Docs** - Doesn't acknowledge Module 06/08 integration, no scaffolding section
7. **🟡 Module 03 No State Tracking** - Generated profiles can't persist (critical for on-the-fly generation)

**Integration Score**: 4/13 modules actively use Module 13 (04/05/06/08)  
**Missing**: Scaffolding rules mapping narrative DNA → mechanics  
**Total Fix Effort**: 24-34 hours across 3 priorities (includes genre libraries completion)

---

## Next Steps (After User Decisions)

**If A1 (Cross-Reference) + A2 (Full Integration) + A3 (Document Flow) + A4 (New Category) + Immediate**:

1. Add Module 12/13 coordination notes (30 min per profile = 6 hours)
2. Add Module 09/13 pacing guidance (30 min per profile = 6 hours)
3. Document cognitive engine flow (1 hour)
4. Add NARRATIVE_STYLE category (2 hours)
5. **Total: ~15 hours** (1-2 work sessions)

**Then Priority 2**: Mechanical integration sections (~10-15 hours, separate session)

**Then Priority 3**: Cross-linking libraries (~4-6 hours, separate session)

---

**Awaiting your decisions before proceeding with fixes!**
