# Narrative Profile Library - Master Index

**Library Version**: 1.1 (Scale 11 Update)  
**Last Updated**: 2025-01-15  
**Total Profiles**: 12 CORE (expanded) + DanDaDan bonus  
**Profile Location**: `aidm/libraries/narrative_profiles/`

---

## Quick Reference Guide

**For Players (Session Zero)**: Browse by genre → Read 2-3 matching profiles → Discuss elements with AIDM → AIDM calibrates

**For AIDM**: Present index → Player selects 1-3 profiles → Extract DNA (copy scales/tropes/styles to `active_narrative_profile`) → Store profile ID(s) in session schema → Reference during gameplay

**Format**: Files = `{anime}_profile.md` | IDs = `narrative_{short_name}`

---

## Profile Library by Genre

### Battle Shonen (Action-Focused, Growth Arcs)

**Hunter x Hunter** (`narrative_hxh`): Tactical 10/10, exhaustive explanations, Nen conditions/costs, strategic battles | *Best for*: Earned victories through strategy  
**Jujutsu Kaisen** (`narrative_jjk`): Dark tone, permanent deaths, Domain Expansions, binding vows, horror (Mahito) | *Best for*: Consequences + beautiful tragedy  
**Demon Slayer** (`narrative_demon_slayer`): Emotional sakuga, Breathing techniques, empathy for enemies, tragic backstories | *Best for*: Visually stunning combat, kind protagonist

*Common*: Power systems with rules, training arcs, escalating threats, friendship (varies)

---

### Dark Fantasy / Military

**Attack on Titan** (`narrative_aot`): Grim military tactics, titan horror, political conspiracy, pyrrhic victories, formal tone, "no safety" | *Best for*: Mortal danger always, truth worse than mystery

*Common*: War brutality, existential threats, politics, high casualties

---

### Comedy / Parody

**Konosuba** (`narrative_konosuba`): Anti-power-fantasy, incompetent party, mundane stakes (rent>Demon King), constant banter, backfire comedy | *Best for*: Failing upward, dysfunctional family, undercut drama

*Common*: Parody tropes, slapstick, financial struggles, chaos wins

---

### Psychological Thriller / Mystery

**Death Note** (`narrative_death_note`): Cat-and-mouse, dual inner monologue, "just as planned", plans within plans, no combat | *Best for*: Detective vs mastermind, evidence>violence  
**Code Geass** (`narrative_code_geass`): Mecha politics, Geass costs, tonal whiplash (school→tragedy), strategic mastermind, checkmate moments | *Best for*: 4D chess, dual identity strain

*Common*: Strategy>strength, inner monologue, moral grey, tragic descents

---

### Isekai (Transported to Another World)

**Konosuba** (`narrative_konosuba`): Comedy isekai parody (see Comedy section)  
**Re:Zero** (`narrative_rezero`): Time loop horror, Return by Death, graphic deaths, PTSD accumulation, trial-and-error mystery | *Best for*: Suffering isekai, learning through 3-7 failed loops

*Common*: Trope awareness (Konosuba parodies, Re:Zero subverts), OP mechanics with costs

---

### Atmospheric / Contemplative

**Mushishi** (`narrative_mushishi`): Episodic wanderer, no combat (observation/treatment), mushi as nature, bittersweet endings, slow (90% contemplation), silence=content | *Best for*: Philosophy>action, acceptance>victory, quiet beauty

*Common*: Slice-of-life, existential acceptance, nature focus, melancholy

---

### Seinen (Mature, Realistic)

**Vinland Saga** (`narrative_vinland_saga`): Historical brutality, realistic ugly violence, redemption (revenge→pacifism), Viking accuracy, "I have no enemies" | *Best for*: Grounded medieval, PTSD depicted, pacifism HARD choice

*Common*: Moral complexity, violence has cost, slow transformation, historical grounding

---

### Sports / Team Drama

**Haikyuu** (`narrative_haikyuu`): Volleyball teamwork (literal cooperation), underdog wins, practice matters, chibi comedy, losses teach, "One More!" | *Best for*: Team campaign, skill training, found family

*Common*: Teamwork mechanics, training arcs, respect rivals, emotional catharsis

---

### Supernatural Romance / Action

**DanDaDan** (`narrative_dandadan`): Occult+aliens, rapid tonal shifts (horror→romance→comedy), body-swap, psychic powers, relationship focus, Gen Z dialogue | *Best for*: Genre-blending chaos, fast multi-genre

*Common*: Romance subplot, tonal whiplash, supernatural+sci-fi---

## Cross-Reference Matrix

**If Player Wants... → Recommend**:

"Tactical combat" → HxH | JJK, Code Geass  
"Dark/brutal" → AoT, Re:Zero | Vinland, JJK  
"Comedy/fun" → Konosuba | Haikyuu, DanDaDan  
"Mind games" → Death Note | Code Geass, Re:Zero  
"Beautiful combat" → Demon Slayer | JJK  
"Time loops" → Re:Zero (unique)  
"Contemplative/slow" → Mushishi | Vinland (S2)  
"Redemption arc" → Vinland | JJK  
"Team dynamics" → Haikyuu | Konosuba  
"Mecha/politics" → Code Geass | AoT  
"Isekai parody" → Konosuba (unique)  
"Isekai serious" → Re:Zero (unique)  
"Power system rules" → HxH | JJK, Demon Slayer  
"Empathy for enemies" → Demon Slayer | Vinland  
"Tournament structure" → Haikyuu | HxH

---

## Blending Profiles (Advanced)

**AIDM can combine 2-3 profiles**:

**"Tactical Dark Fantasy"**: HxH (tactics) + AoT (grim) + JJK (horror) = Explained powers, high lethality, strategic with permanent deaths

**"Comedic Isekai with Heart"**: Konosuba (comedy) + Haikyuu (bonding) = Dysfunctional party failing upward but genuinely caring

**"Psychological Horror Isekai"**: Re:Zero (loops) + Death Note (planning) = Loop knowledge to outmaneuver intelligent opponents

**"Contemplative Redemption"**: Mushishi (slow, acceptance) + Vinland (redemption) = Quiet growth, bittersweet, violence renounced

**Guidelines**:  
1. Choose **1 primary** (dominant tone/pacing)  
2. Add **1-2 secondary** (specific elements)  
3. **Avoid contradictions**: ❌ Konosuba+AoT (comedy vs grim) | ❌ Mushishi+Demon Slayer (slow vs fast) | ✅ JJK+Demon Slayer (both dark shonen) | ✅ Death Note+Code Geass (both strategic)  
4. **Extract**: Scales=average or primary | Tropes=union of enabled | Dialogue/Combat=primary's style, adjust 1-2 from secondary

---

## Profile Structure (All Profiles Follow This Format)

1. Metadata (ID, source, confidence) | 2. Narrative Scales (11 scales 0-10/0-11) | 3. Storytelling Tropes (15 ON/OFF) | 4. Pacing Rhythm (scene/arc length, climax frequency, downtime %) | 5. Tonal Signature (emotions, violence/fanservice/horror) | 6. Dialogue Style (6 parameters) | 7. Combat Narrative (5 parameters) | 8. Example Scenes (3: combat, dialogue, exploration) | 9. Adjustment Log (session calibration history) | 10. Usage Notes (when to apply, tips, mistakes)

**NOTE**: All profiles now include **Scale 11: POV Distribution** - see dedicated section below for detailed guidance.

---

## Scale 11: POV Distribution Spectrum

**NEW ADDITION (2025-01-15)**: All CORE profiles now include **Scale 11: POV Distribution** measuring protagonist focus vs ensemble dynamics.

### Understanding the Scale

**Scale 11 Measures**: Narrative camera distribution across characters  
**Range**: 1/10 (solo protagonist) → 11/10 (full ensemble)  
**Purpose**: Calibrate spotlight management, player agency distribution, session structure

**Key Insight**: POV distribution ≠ importance. Solo protagonists can be deeply flawed (Re:Zero), ensemble casts can have clear leaders (Haikyuu). Scale measures **narrative time allocation**, not character hierarchy.

---

### POV Distribution Levels

#### 1/10: Solo Protagonist (Isolated Hero)
**Definition**: 80-95% POV from single character, minimal ensemble  
**Examples**: Death Note (Light 90%), Mushishi (Ginko 95%), Re:Zero (Subaru 85%)  
**Characteristics**: Inner monologue dominant, other characters NPC-like, isolated decision-making  
**AIDM Application**: Single-player TTRPG or clear main PC in party (others support), deep psychological focus  
**Session Structure**: Every scene = protagonist present, other PCs episodic appearances  
**Player Expectations**: One player/PC heavily featured, others accept support roles  
**Pitfalls**: Unintended spotlight hogging, supporting players feel sidelined

**When to Use**: Solo campaigns, psychological horror (isolation = feature), mystery protagonist needs constant access to clues

---

#### 2/10: Solo-Leaning (Sidekick Structure)
**Definition**: 70-85% primary protagonist, 15-30% supporting cast  
**Examples**: Code Geass (Lelouch 80% + Suzaku/C.C. 20%), Vinland Saga S2 (Thorfinn 85% + Einar 10%)  
**Characteristics**: Clear main character, recurring sidekick/deuteragonist, supporting cast rotates  
**AIDM Application**: Traditional "main PC + party" where one PC clearly leads, others crucial but secondary  
**Session Structure**: Most scenes = main PC, 1-2 scenes per session spotlight sidekick  
**Player Expectations**: One player drives plot, others contribute meaningfully but not equally  
**Pitfalls**: Sidekick players want more agency, main player burns out from constant spotlight

**When to Use**: Traditional hero's journey with companions, redemption arcs (Vinland S2), solo mastermind with allies (Code Geass)

---

#### 3/10: Duo/Primary Focus (Dynamic Duo + Supporting)
**Definition**: 50-60% primary protagonist, 20-40% deuteragonist, 10-30% ensemble  
**Examples**: Attack on Titan S1 (Eren 50% + Mikasa/Armin 15% each), Hunter x Hunter (Gon 50% + Killua 40%)  
**Characteristics**: Two protagonists (unequal), primary drives plot, secondary equal in competence/importance  
**AIDM Application**: Two-player campaigns or party with clear leader + lieutenant structure  
**Session Structure**: Alternate scenes between primary/secondary, ensemble rotates supporting scenes  
**Player Expectations**: Two players share spotlight unequally but meaningfully, others specialized roles  
**Pitfalls**: Secondary protagonist feels like sidekick not co-lead, ensemble players underutilized

**When to Use**: Mentor/student dynamics (Gon+Killua), leader/lieutenant (Eren+Armin), unequal duo with clear primary

---

#### 4/10: Primary with Distributed Support
**Definition**: 40-50% primary protagonist, 50-60% distributed across supporting cast  
**Examples**: Jujutsu Kaisen (Yuji 50% + Megumi/Nobara/Gojo/etc 50% distributed)  
**Characteristics**: Clear main character, supporting cast individually significant (10-15% each)  
**AIDM Application**: Traditional party structure with protagonist PC + 3-4 equal supporting PCs  
**Session Structure**: Primary appears most scenes, each support gets spotlight arc every 3-5 sessions  
**Player Expectations**: One player slightly featured, others rotate episodes/arcs, ensemble recognized  
**Pitfalls**: Primary player dominates unintentionally, support players feel undervalued

**When to Use**: Shonen protagonist with recurring team (Yuji+school), hero with specialized allies

---

#### 5/10: Balanced Quartet/Small Ensemble
**Definition**: 20-30% each across 4-5 core characters, equal distribution  
**Examples**: Konosuba (Kazuma/Aqua/Megumin/Darkness ~25% each)  
**Characteristics**: No primary protagonist, ensemble operates as unit, equal narrative weight  
**AIDM Application**: Balanced party campaigns, each PC gets equal spotlight, decisions collective  
**Session Structure**: Rotate scenes evenly, every session = each PC featured, collective climaxes  
**Player Expectations**: All players expect equal time, "party = protagonist", shared victories  
**Pitfalls**: One player accidentally dominates, scenes feel fragmented without clear POV

**When to Use**: Classic D&D parties (4-5 PCs equal), sitcom ensembles, dysfunctional teams (Konosuba)

---

#### 6/10: Ensemble-Leaning (Primary + Robust Cast)
**Definition**: 30-40% primary, 60-70% distributed across 5-8 recurring characters  
**Examples**: Demon Slayer (Tanjiro 40% + Hashira squad 60%), Vinland Saga S1 (Thorfinn 50% + Askeladd 40% + others 10%)  
**Characteristics**: Identified protagonist, large supporting cast with individual arcs, dual-narrative lanes  
**AIDM Application**: Large parties (6-8 PCs) with designated leader, NPCs get spotlight arcs  
**Session Structure**: Primary present most scenes, each support gets 1-2 dedicated episodes per arc  
**Player Expectations**: Leader recognized, everyone gets "their episode", ensemble celebrated  
**Pitfalls**: Too many characters = diluted focus, some PCs forgotten

**When to Use**: Military squads (AoT), guild campaigns (Demon Slayer Hashira), dual protagonists (Vinland S1 Thorfinn+Askeladd)

---

#### 7/10: Dual Protagonists (True Co-Leads)
**Definition**: 40-50% each for TWO protagonists, 10-20% supporting  
**Examples**: DanDaDan (Momo 45% + Okarun 45% + supporting 10%)  
**Characteristics**: TRUE CO-LEADS (equal narrative weight), interdependent mechanics, alternating spotlight, romance/rivalry core  
**AIDM Application**: Two-player campaigns with equal agency, buddy cop dynamics, romantic pairs  
**Session Structure**: Strict alternation (Momo episodes → Okarun episodes), joint climaxes, separation = tension  
**Player Expectations**: Both players equally featured, decisions collaborative, duo = single unit  
**Pitfalls**: One player accidentally dominates, forced equal time feels artificial

**When to Use**: Buddy campaigns (DanDaDan Momo+Okarun), romantic pairs, rival dynamics needing equal time

---

#### 8-10/10: Large Ensemble (Multiple Protagonists)
**Definition**: 15-25% each across 6-10+ core characters  
**Examples**: [Not yet profiled - potential: My Hero Academia class, Durarara!!, Baccano!]  
**Characteristics**: Multiple protagonists with individual arcs, rotates focus, interconnected plots  
**AIDM Application**: West Marches campaigns, large party rotations, anthology arcs  
**Session Structure**: Each session = 2-3 PCs featured, arcs dedicated to character subsets  
**Player Expectations**: Players accept rotation, "your arc coming up", ensemble victories  
**Pitfalls**: Fragmentation, players feel ignored during others' arcs

**When to Use**: Large casts (6-10+ PCs), anthology structures, interconnected character webs

---

#### 11/10: PEAK Ensemble (Full Rotation)
**Definition**: 5-10% each across 15-20+ characters, constantly rotating spotlight  
**Examples**: Haikyuu (20+ volleyball team members, spotlight rotates match-by-match)  
**Characteristics**: NO primary protagonist, every character gets arcs, collective narrative, "team = hero"  
**AIDM Application**: Sports teams, military platoons, guild-wide campaigns, West Marches  
**Session Structure**: Rotating spotlight (3-4 PCs per session), team climaxes (everyone contributes), character episodes scheduled  
**Player Expectations**: Everyone gets spotlight eventually, patience required, ensemble victories > individual glory  
**Pitfalls**: Players feel lost without clear POV, new players overwhelmed by cast size

**When to Use**: Sports campaigns (Haikyuu volleyball), large guilds, West Marches rotations, "team of specialists" dynamics

---

### Scale 11 Cross-Reference Table

| Scale | Example Series | Primary POV | Secondary POV | Ensemble % | Best For |
|-------|----------------|-------------|---------------|------------|----------|
| **1/10** | Death Note, Mushishi, Re:Zero | 80-95% | 0-10% | 5-10% | Solo campaigns, psychological horror |
| **2/10** | Code Geass, Vinland S2 | 70-85% | 10-20% | 5-10% | Hero + sidekick, redemption arcs |
| **3/10** | Attack on Titan S1, Hunter x Hunter | 50-60% | 20-40% | 10-30% | Dynamic duo + team, mentor/student |
| **4/10** | Jujutsu Kaisen | 40-50% | 50-60% (distributed) | - | Protagonist + supporting cast |
| **5/10** | Konosuba | 20-30% each (4-5 chars) | - | - | Balanced parties, sitcom ensembles |
| **6/10** | Demon Slayer, Vinland S1 | 30-40% | 60-70% (5-8 chars) | - | Large parties, squad campaigns |
| **7/10** | DanDaDan | 40-50% each (2 chars) | 10-20% | - | True co-leads, buddy cops, romance pairs |
| **8-10/10** | [Future profiles] | 15-25% each (6-10 chars) | - | - | Large ensembles, anthology arcs |
| **11/10** | Haikyuu | 5-10% each (15-20+ chars) | - | - | Sports teams, guild campaigns, West Marches |

---

### Progression Models (Scale 11 Can Change)

**Vinland Saga**: 6/10 (S1 War Arc: Thorfinn 50% + Askeladd 40%) → 2/10 (S2 Farmland Saga: Thorfinn 85% + Einar 10%)  
**Reason**: S1 = dual-narrative political+revenge, S2 = solo redemption arc, structural shift from war ensemble to intimate character study

**Attack on Titan**: 3/10 (S1: Eren 50% + Mikasa/Armin 15% each) → 6/10 (S3-4: Distributed across Survey Corps)  
**Reason**: Early seasons = trio-focused, later seasons = military ensemble with political factions

**AIDM Application**: POV can shift mid-campaign based on narrative needs:
- **Character death** (ensemble loses member → remaining PCs get larger shares)
- **Arc transitions** (war arc = ensemble → redemption arc = solo focus)
- **Player availability** (player leaves → redistribute POV to remaining PCs)
- **Story needs** (mystery requires solo POV for clue access, war requires ensemble for tactics)

**How to Transition**:  
1. **Gradual** (3 sessions): Session N = announce shift, N+1 = 70% old/30% new distribution, N+2 = 30% old/70% new, N+3 = full new distribution  
2. **Narrative justification**: Character leaves party (Vinland Askeladd dies → Thorfinn solo), new member joins (duo → trio), story structure changes (war → peace)  
3. **Update `adjustment_log`**: Document old Scale 11 → new Scale 11, reason for shift, session number  
4. **Player communication**: Session Zero warning ("this will become solo-focused redemption arc"), mid-campaign check-in ("how do you feel about ensemble increasing?")

---

### Session Zero Questions for Scale 11 Calibration

**Ask Players**:

1. **"Do you prefer one clear protagonist or shared spotlight?"**  
   Solo preference → 1-3/10 | Balanced preference → 4-6/10 | Ensemble preference → 7-11/10

2. **"How do you feel about scenes without your character?"**  
   Uncomfortable → 1-3/10 (everyone in every scene) | Fine occasionally → 4-6/10 | Love ensemble storytelling → 7-11/10

3. **"Reference example: Think [Death Note solo] vs [Haikyuu full team]. Where between?"**  
   Death Note vibes → 1-2/10 | Middle ground → 4-6/10 | Haikyuu vibes → 9-11/10

4. **"If one player can't attend, how should we handle their PC?"**  
   Abort session (need everyone) → 5-11/10 ensemble | NPC them (solo can continue) → 1-4/10 solo-leaning

5. **"Do you want individual character arcs or collective party goals?"**  
   Individual → 1-3/10 solo campaigns | Mix → 4-7/10 balanced | Collective → 8-11/10 ensemble

**Calibration Formula**:  
- **Majority solo preference + uncomfortable without PC** = 1-2/10  
- **Mix of preferences + fine with occasional absence** = 4-6/10  
- **Ensemble preference + love rotating spotlight** = 8-11/10  
- **Two-player campaign wanting equal time** = 7/10 (true duo)

---

### Common Mistakes & Solutions

**Mistake 1: Unintended Solo Dominance in Ensemble Campaign**  
**Symptom**: Set Scale 11 = 6/10 (ensemble), but one PC gets 70% spotlight  
**Cause**: Player personality (extroverted), character design (leader role), AIDM defaults to them  
**Solution**: Explicitly rotate scenes ("Next scene focuses on [quiet PC]"), track POV % per session, address in Session Zero ("everyone gets spotlight")

**Mistake 2: Forced Equal Time Feels Artificial**  
**Symptom**: Strict 25% each in 5/10 quartet, but some PCs lack narrative hooks  
**Cause**: Not all characters need equal time in every arc, some PCs support-role naturally  
**Solution**: Allow organic variation (20-30% range OK), give support PCs dedicated episodes occasionally, don't force equality in every session

**Mistake 3: Ensemble Fragmentation (Players Feel Lost)**  
**Symptom**: 11/10 Haikyuu-style ensemble, but players forget who's who  
**Cause**: Too many PCs, no clear POV anchor, spotlight rotates too fast  
**Solution**: Establish 2-3 "anchor PCs" (players can rely on them for POV), rotate spotlight slower (full episode/session blocks), use visual aids (character relationship maps)

**Mistake 4: Duo Accidentally Becomes Solo**  
**Symptom**: Set 7/10 true duo (DanDaDan style), but one PC gets 70% time  
**Cause**: One player more proactive, one character mechanically stronger, AIDM defaults  
**Solution**: Strict alternation rules (Episode A = PC1 focus, Episode B = PC2 focus), interdependent mechanics (PC1 can't succeed without PC2), romance/rivalry requires both present

**Mistake 5: Mid-Campaign POV Shift Feels Jarring**  
**Symptom**: Shifted from 3/10 duo to 6/10 ensemble suddenly, players confused  
**Cause**: No narrative justification, instant shift (no gradual transition)  
**Solution**: Gradual 3-session transition (see Progression Models above), narrative reason (party grows, war begins, mentor dies), Session Zero warning ("this arc = ensemble focus")

---

### AIDM Guidance for Scale 11 Integration

**During Session Zero**:
1. Present Scale 11 spectrum (show examples: Death Note solo vs Haikyuu ensemble)  
2. Ask calibration questions (see above)  
3. Set initial Scale 11 value based on player preferences  
4. Document in `active_narrative_profile` and session schema  
5. Explain how it affects session structure ("scenes without your PC OK?")

**During Gameplay**:
1. **Track POV distribution** (mental note: "Protagonist PC appeared 8/10 scenes this session")  
2. **Reference Scale 11 when narrating** (1-3/10 = always include solo PC, 7-11/10 = rotate freely)  
3. **Adjust spotlight proactively** (notice PC underutilized → create scene for them)  
4. **Use Scale 11 for NPC behavior** (1/10 solo = NPCs orbit protagonist, 11/10 ensemble = NPCs have independent agency)

**When Calibrating Mid-Campaign**:
1. After 3-5 sessions, ask "Is spotlight distribution feeling right?"  
2. If issues → reference Scale 11 table, suggest adjustment ("We're playing 3/10 duo but maybe 5/10 quartet fits better?")  
3. Gradual transition (3 sessions) with narrative justification  
4. Update `adjustment_log`: `"Session 12: Scale 11 shifted 3/10 → 5/10 (party grew, player feedback wanted more ensemble)"`

**Blending Profiles with Different Scale 11 Values**:
- **Use primary profile's Scale 11** (e.g., HxH 3/10 duo + AoT 6/10 ensemble → choose 3/10 if tactical duo core, or 6/10 if military ensemble core)  
- **Average if equal weight** (JJK 4/10 + Demon Slayer 6/10 → 5/10 balanced quartet)  
- **Document in session schema**: `"Scale 11: 5/10 (averaged from JJK 4/10 + Demon Slayer 6/10)"`

---

## Quick Start Workflows

**1. Player Knows Anime**: "I want Hunter x Hunter!" → Open `hunter_x_hunter_profile.md` → Copy scales/tropes/styles to `active_narrative_profile` → Set `profile_sources=["narrative_hxh"]` → Reference "Usage Notes" during gameplay

**2. Player Knows Genre**: "Dark fantasy + strategy" → Consult matrix (Tactical→HxH, Dark→AoT) → Show both example scenes → Player chooses blend (HxH tactics + AoT tone) → Extract HxH (Tactical:10, Explained:3, exhaustive dialogue) + AoT (Drama:9, Cynical:8, military formality) → Merge → Set `profile_sources=["narrative_hxh","narrative_aot"]`

**3. Player Wants Custom**: "Fun campaign, no references" → Use Module 13 baseline → Session Zero calibration questions (comedy vs drama? tactical vs instinctive?) → Leave `profile_sources=[]` → After 3-5 sessions, suggest closest library match → Player adopts or continues custom

**4. Mid-Campaign Tone Shift**: Konosuba(comedy) → serious → "Which serious? Dark/Tactical/Redemption?" → Player: "Vinland redemption" → Gradual transition: Session N (comedy but serious consequence), N+1 (50% comedy, introduce guilt), N+2 (shift to Vinland: slow burn, PTSD, pacifism) → Update `profile_sources=["narrative_konosuba","narrative_vinland_saga"]` → Mark in `adjustment_log`

---

## Profile Maintenance & Updates

**Adding New Profile**: Follow structure → Add to index under genre → Update cross-reference matrix → Add blending suggestions → Increment count → Update date

**Suggested Future Profiles**: Fullmetal Alchemist (adventure, equivalent exchange) | Steins;Gate (time travel thriller) | One Punch Man (parody, OP boredom) | Mob Psycho 100 (coming-of-age psychic) | Made in Abyss (exploration horror, cute+dark) | Monogatari (dialogue-heavy wordplay) | Cowboy Bebop (episodic space western jazz) | Fate/Zero (battle royale, tragic heroes)

---

## Integration with Module 13

**Relationship**: Module 13 defines schema (scales, tropes, styles) | Library provides pre-calibrated examples | Library=examples, Module 13=system

**File References**: Schema=`13_narrative_calibration.md` | Session data=`session_export_schema.json` (`active_narrative_profile`) | Module 00 (Init)=references during Session Zero | Module 04 (NPCs)=uses `dialogue_style` | Module 05 (Great Sage)=uses scales for tone | Module 08 (Combat)=uses `combat_narrative_style`

---

## Appendix: All Profile Files

```
aidm/libraries/narrative_profiles/
├── attack_on_titan_profile.md       (narrative_aot)          [CORE: ~12K words, Scale 11: 3/10 duo]
├── code_geass_profile.md            (narrative_code_geass)   [CORE: ~13K words, Scale 11: 2/10 solo-leaning]
├── dandadan_profile.md              (narrative_dandadan)     [CORE: ~11.5K words, Scale 11: 7/10 dual protagonists]
├── death_note_profile.md            (narrative_death_note)   [CORE: ~10K words, Scale 11: 1/10 solo]
├── demon_slayer_profile.md          (narrative_demon_slayer) [CORE: ~12K words, Scale 11: 6/10 ensemble-leaning]
├── haikyuu_profile.md               (narrative_haikyuu)      [CORE: ~15K words, Scale 11: 11/10 PEAK ensemble]
├── hunter_x_hunter_profile.md       (narrative_hxh)          [CORE: ~14K words, Scale 11: 3/10 duo]
├── jujutsu_kaisen_profile.md        (narrative_jjk)          [CORE: ~13K words, Scale 11: 4/10 primary]
├── konosuba_profile.md              (narrative_konosuba)     [CORE: ~11K words, Scale 11: 5/10 quartet]
├── mushishi_profile.md              (narrative_mushishi)     [CORE: ~12.7K words, Scale 11: 1/10 solo]
├── rezero_profile.md                (narrative_rezero)       [CORE: ~12.6K words, Scale 11: 1/10 solo]
└── vinland_saga_profile.md          (narrative_vinland_saga) [CORE: ~12K words, Scale 11: 6/10→2/10 PROGRESSION]
```

**Total**: 12 CORE profiles (8-15K words each) + DanDaDan bonus (11.5K words)  
**Estimated Tokens**: ~120,000 tokens (entire CORE library)  
**Per-Profile Average**: ~10,000 tokens (CORE format)  
**Scale 11 Coverage**: 1/10 (solo) to 11/10 (PEAK ensemble) - full spectrum represented

---

**End of Master Index**  
**For profile content, open individual `.md` files in `aidm/libraries/narrative_profiles/` directory**
