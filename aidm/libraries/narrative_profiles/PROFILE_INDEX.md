# Narrative Profile Library - Master Index

**Library Version**: 1.0  
**Last Updated**: 2025-01-15  
**Total Profiles**: 13  
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

1. Metadata (ID, source, confidence) | 2. Narrative Scales (10 scales 0-10) | 3. Storytelling Tropes (15 ON/OFF) | 4. Pacing Rhythm (scene/arc length, climax frequency, downtime %) | 5. Tonal Signature (emotions, violence/fanservice/horror) | 6. Dialogue Style (6 parameters) | 7. Combat Narrative (5 parameters) | 8. Example Scenes (3: combat, dialogue, exploration) | 9. Adjustment Log (session calibration history) | 10. Usage Notes (when to apply, tips, mistakes)

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
├── attack_on_titan_profile.md       (narrative_aot)
├── code_geass_profile.md            (narrative_code_geass)
├── dandadan_profile.md              (narrative_dandadan)
├── death_note_profile.md            (narrative_death_note)
├── demon_slayer_profile.md          (narrative_demon_slayer)
├── haikyuu_profile.md               (narrative_haikyuu)
├── hunter_x_hunter_profile.md       (narrative_hxh)
├── jujutsu_kaisen_profile.md        (narrative_jjk)
├── konosuba_profile.md              (narrative_konosuba)
├── mushishi_profile.md              (narrative_mushishi)
├── rezero_profile.md                (narrative_rezero)
└── vinland_saga_profile.md          (narrative_vinland_saga)
```

**Total**: 13 profiles  
**Estimated Tokens**: ~40,000 tokens (entire library)  
**Per-Profile Average**: ~3,000 tokens

---

**End of Master Index**  
**For profile content, open individual `.md` files in `aidm/libraries/narrative_profiles/` directory**
