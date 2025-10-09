# Narrative Profile Library - Master Index

**Library Version**: 1.0  
**Last Updated**: 2025-01-15  
**Total Profiles**: 13  
**Profile Location**: `aidm/libraries/narrative_profiles/`

---

## Quick Reference Guide

### How to Use This Library

**For Players (Session Zero)**:
1. Browse profiles by genre below
2. Read 2-3 profiles that match your desired campaign tone
3. Discuss with AIDM which elements appeal to you
4. AIDM will calibrate narrative DNA using selected profile(s)

**For AIDM**:
1. During Session Zero, present this index to player
2. Player selects 1-3 profiles as tonal references
3. Extract narrative DNA from selected profiles:
   - Copy scale values to `active_narrative_profile`
   - Enable/disable tropes based on profile
   - Set dialogue_style and combat_narrative_style
4. Store profile ID(s) in session export schema
5. Reference profile during gameplay for consistency

**Profile File Naming**: `{anime_title_snake_case}_profile.md`  
**Profile ID Format**: `narrative_{short_name}`

---

## Profile Library by Genre

### Battle Shonen (Action-Focused, Growth Arcs)

| Profile | ID | Key Features | Best For |
|---------|-----|--------------|----------|
| **Hunter x Hunter** | `narrative_hxh` | Tactical combat (10/10), exhaustive power explanations, complex moral choices, strategic battles, Nen system depth | Players who want EXPLAINED tactics, every ability has conditions/costs, earn victories through strategy |
| **Jujutsu Kaisen** | `narrative_jjk` | Dark tone, permanent character deaths, horror elements (Mahito), Domain Expansions, binding vows, modern urban supernatural | Players who want consequences, beautiful combat + tragedy, cursed techniques with rules |
| **Demon Slayer** | `narrative_demon_slayer` | Emotional spectacle, Breathing techniques (sakuga), empathy for enemies, tragic backstories, hopeful despite darkness | Players who want visually stunning combat, crying after victories, kind protagonist |

**Common Themes**: Power systems with rules, training arcs, escalating threats, friendship (varies by subversion level)

---

### Dark Fantasy / Military

| Profile | ID | Key Features | Best For |
|---------|-----|--------------|----------|
| **Attack on Titan** | `narrative_aot` | Grim military tactics, titan horror, political conspiracy, "no safety" philosophy, dramatic declarations, pyrrhic victories | Players who want mortal danger always, formal military tone, truth worse than mystery, walls = false security |

**Common Themes**: War brutality, existential threats, political intrigue, high casualties

---

### Comedy / Parody

| Profile | ID | Key Features | Best For |
|---------|-----|--------------|----------|
| **Konosuba** | `narrative_konosuba` | Anti-power-fantasy, incompetent party, mundane stakes (rent > Demon King), constant banter, fanservice played for comedy, everything backfires hilariously | Players who want failing upward, dysfunctional found family, absurd situations with grounded reactions, ALWAYS undercut drama |

**Common Themes**: Parody tropes, slapstick, financial struggles, chaos wins

---

### Psychological Thriller / Mystery

| Profile | ID | Key Features | Best For |
|---------|-----|--------------|----------|
| **Death Note** | `narrative_death_note` | Cat-and-mouse mind games, dual inner monologue (protagonist + antagonist), "Just as planned", plans within plans, moral ambiguity, no physical combat | Players who want strategic detective vs mastermind, psychological horror, evidence > violence, delayed plan reveals |
| **Code Geass** | `narrative_code_geass` | Mecha political intrigue, Geass powers with costs, tonal whiplash (school comedy → tragedy), strategic mastermind protagonist, moral ambiguity, "checkmate" moments | Players who want 4D chess tactics, dual identity strain (student vs terrorist), complex betrayals, tragic hero |

**Common Themes**: Strategy over strength, inner monologue, moral grey areas, tragic descents

---

### Isekai (Transported to Another World)

| Profile | ID | Key Features | Best For |
|---------|-----|--------------|----------|
| **Konosuba** | `narrative_konosuba` | Comedy isekai parody (see Comedy section) | Light-hearted isekai mockery |
| **Re:Zero** | `narrative_rezero` | Time loop horror, Return by Death (resets on death), graphic deaths, PTSD accumulation, mystery solving through iteration, isolation from meta-knowledge | Players who want suffering isekai, trial-and-error gameplay, learning through failure, psychological trauma, earned victories after 3-7 failed loops |

**Common Themes**: Isekai trope awareness (Konosuba parodies, Re:Zero subverts), overpowered mechanics with costs

---

### Atmospheric / Contemplative

| Profile | ID | Key Features | Best For |
|---------|-----|--------------|----------|
| **Mushishi** | `narrative_mushishi` | Episodic wanderer, no combat (observation/treatment), mushi as natural phenomena, bittersweet endings, slow pacing (90% contemplation), nature descriptions, silence is content | Players who want philosophy over action, acceptance over victory, quiet beauty, Ginko helps then leaves, environmental storytelling |

**Common Themes**: Slice-of-life, existential acceptance, nature focus, melancholy beauty

---

### Seinen (Mature, Realistic)

| Profile | ID | Key Features | Best For |
|---------|-----|--------------|----------|
| **Vinland Saga** | `narrative_vinland_saga` | Historical brutality, realistic violence (ugly not stylish), redemption arc (S1 revenge → S2 pacifism), slow burn character growth, Viking Age accuracy, "I have no enemies" philosophy | Players who want grounded medieval combat, PTSD depicted, pacifism as HARD choice, slavery/war consequences, found family through trauma |

**Common Themes**: Moral complexity, violence has cost, slow character transformation, historical grounding

---

### Sports / Team Drama

| Profile | ID | Key Features | Best For |
|---------|-----|--------------|----------|
| **Haikyuu** | `narrative_haikyuu` | Volleyball teamwork (literal cooperation required), underdog victories, practice matters, chibi comedy breaks, hopeful tone, losses teach, respect rivals, "One More!" mentality | Players who want team-based campaign, skill development through training, found family, tournament structure, inspirational growth |

**Common Themes**: Teamwork mechanics, training arcs, rivalries with respect, emotional catharsis

---

### Supernatural Romance / Action

| Profile | ID | Key Features | Best For |
|---------|-----|--------------|----------|
| **DanDaDan** | `narrative_dandadan` | Occult + aliens, rapid tonal shifts (horror → romance → comedy), body-swap mechanics, psychic powers, relationship focus, "believe to perceive" theme, Gen Z dialogue | Players who want genre-blending chaos, relationship development through weird situations, fast-paced multi-genre |

**Common Themes**: Romance subplot, tonal whiplash, supernatural meets sci-fi

---

## Cross-Reference Matrix

### If Player Wants... → Recommend These Profiles

| Player Request | Primary Profile(s) | Secondary Profile(s) |
|----------------|-------------------|---------------------|
| "Tactical combat with explanations" | Hunter x Hunter | Jujutsu Kaisen, Code Geass |
| "Dark and brutal" | Attack on Titan, Re:Zero | Vinland Saga, Jujutsu Kaisen |
| "Comedy and fun" | Konosuba | Haikyuu (team comedy), DanDaDan (tonal chaos) |
| "Psychological mind games" | Death Note | Code Geass, Re:Zero (loop mystery) |
| "Beautiful combat spectacle" | Demon Slayer | Jujutsu Kaisen (Domain Expansions) |
| "Time loops / trial and error" | Re:Zero | (unique - no alternatives) |
| "Contemplative and slow" | Mushishi | Vinland Saga (S2 farm arc) |
| "Redemption arc" | Vinland Saga | Jujutsu Kaisen (Yuji's guilt) |
| "Team dynamics" | Haikyuu | Konosuba (dysfunctional team) |
| "Mecha and politics" | Code Geass | Attack on Titan (military politics) |
| "Isekai parody" | Konosuba | (unique - no alternatives) |
| "Isekai serious" | Re:Zero | (unique - no alternatives) |
| "Power system with rules" | Hunter x Hunter | Jujutsu Kaisen, Demon Slayer |
| "Empathy for enemies" | Demon Slayer | Vinland Saga (Thorfinn's pacifism) |
| "Tournament structure" | Haikyuu | Hunter x Hunter (Heavens Arena) |

---

## Blending Profiles (Advanced)

**AIDM can combine 2-3 profiles for hybrid campaigns**:

### Example Blends

**"Tactical Dark Fantasy"**:
- Hunter x Hunter (tactics) + Attack on Titan (grim tone) + Jujutsu Kaisen (horror)
- Result: Explained power system, high lethality, strategic battles with permanent deaths

**"Comedic Isekai with Heart"**:
- Konosuba (comedy) + Haikyuu (team bonding) 
- Result: Dysfunctional party failing upward but genuinely caring for each other

**"Psychological Horror Isekai"**:
- Re:Zero (time loops) + Death Note (strategic planning)
- Result: Using loop knowledge to outmaneuver intelligent opponents

**"Contemplative Redemption"**:
- Mushishi (slow pacing, acceptance) + Vinland Saga (redemption arc)
- Result: Quiet character growth, bittersweet endings, violence renounced

### Blending Guidelines

1. **Choose 1 Primary Profile** (dominant tone/pacing)
2. **Add 1-2 Secondary Profiles** (specific elements only)
3. **Avoid Contradictions**:
   - ❌ Konosuba + Attack on Titan (comedy vs grim incompatible)
   - ❌ Mushishi + Demon Slayer (slow vs fast pacing clash)
   - ✅ Jujutsu Kaisen + Demon Slayer (both dark shonen, different emphasis)
   - ✅ Death Note + Code Geass (both strategic thriller, different settings)

4. **Extract Carefully**:
   - Narrative scales: Average primary + secondary (or choose primary's values)
   - Tropes: Enable union of both profiles' enabled tropes
   - Dialogue/Combat styles: Choose primary's style, adjust 1-2 parameters from secondary

---

## Profile Structure (All Profiles Follow This Format)

Each profile contains:

1. **Metadata**: Profile ID, source anime, confidence level
2. **Narrative Scales**: 10 scales (0-10 values) matching Module 13 schema
3. **Storytelling Tropes**: 15 tropes (ON/OFF) matching Module 13 schema
4. **Pacing Rhythm**: Scene/arc length, climax frequency, downtime ratio
5. **Tonal Signature**: Primary emotions, violence/fanservice/horror levels
6. **Dialogue Style**: 6 parameters matching Module 13 dialogue_style
7. **Combat Narrative Style**: 5 parameters matching Module 13 combat_narrative_style
8. **Example Scenes**: 3 examples (combat, dialogue, exploration) showing profile in action
9. **Adjustment Log**: Session-by-session calibration history
10. **Usage Notes**: When to apply, calibration tips, common mistakes to avoid

---

## Quick Start Workflows

### Workflow 1: Player Knows Exactly What They Want

**Player**: "I want a campaign like Hunter x Hunter!"

**AIDM Steps**:
1. Open `aidm/libraries/narrative_profiles/hunter_x_hunter_profile.md`
2. Copy all 10 narrative scale values → `active_narrative_profile.scales`
3. Enable tropes from profile → `active_narrative_profile.tropes`
4. Copy dialogue_style parameters → `active_narrative_profile.dialogue_style`
5. Copy combat_narrative_style parameters → `active_narrative_profile.combat_narrative_style`
6. Set `active_narrative_profile.profile_sources = ["narrative_hxh"]`
7. Save to session export schema
8. During gameplay, reference profile's "Usage Notes" for calibration tips

---

### Workflow 2: Player Knows Genre, Not Specific Anime

**Player**: "I want dark fantasy with lots of strategy."

**AIDM Steps**:
1. Consult Cross-Reference Matrix: "Tactical combat" → Hunter x Hunter, "Dark and brutal" → Attack on Titan
2. Present both profiles to player (show example scenes)
3. Player chooses blend: HxH (tactics) + AoT (tone)
4. Extract from HxH: Tactical scale (10), Explained scale (3), dialogue_style (exhaustive explanations)
5. Extract from AoT: Drama scale (9), Cynical scale (8), combat_narrative_style (military formality)
6. Merge into `active_narrative_profile`
7. Set `profile_sources = ["narrative_hxh", "narrative_aot"]`
8. Reference both profiles during gameplay

---

### Workflow 3: Player Wants Custom, No Reference

**Player**: "I just want a fun campaign, not sure about anime references."

**AIDM Steps**:
1. Use default narrative DNA (Module 13 baseline)
2. During Session Zero, ask calibration questions:
   - "Do you want comedy or drama?" → Adjust comedy_vs_drama scale
   - "Tactical or instinctive combat?" → Adjust tactical_vs_instinctive scale
   - Etc. (use Module 13 questionnaire)
3. Leave `profile_sources = []` (custom profile)
4. After 3-5 sessions, analyze gameplay and suggest closest matching profile from library
5. Player can adopt profile or continue custom

---

### Workflow 4: Mid-Campaign Tone Shift

**Scenario**: Campaign started Konosuba-style (comedy), player wants shift to serious.

**AIDM Steps**:
1. Discuss with player: "Which serious tone? Dark (AoT), Tactical (HxH), Redemption (Vinland)?"
2. Player chooses: "I want redemption arc like Vinland Saga"
3. Gradual transition (don't shock player):
   - Session N: Konosuba comedy but introduce serious consequence (party member dies)
   - Session N+1: Comedy reduced 50%, drama increased (funeral, guilt)
   - Session N+2: Shift to Vinland Saga profile (slow burn, PTSD, pacifism themes)
4. Update `active_narrative_profile.profile_sources = ["narrative_konosuba", "narrative_vinland_saga"]` (shows evolution)
5. Mark transition in `active_narrative_profile.adjustment_log`

---

## Profile Maintenance & Updates

### Adding New Profiles

**When creating new profile**:
1. Follow standardized structure (see "Profile Structure" above)
2. Add entry to this index under appropriate genre
3. Update Cross-Reference Matrix with new profile's strengths
4. Add blending suggestions if profile has unique mechanics
5. Increment "Total Profiles" count at top of document
6. Update "Last Updated" date

**Suggested Profiles for Future Addition**:
- Fullmetal Alchemist (adventure, equivalent exchange philosophy)
- Steins;Gate (time travel thriller, sacrifice)
- One Punch Man (parody, OP protagonist boredom)
- Mob Psycho 100 (coming-of-age, psychic powers, emotional growth)
- Made in Abyss (exploration horror, cute art style + dark content)
- Monogatari Series (dialogue-heavy, wordplay, supernatural mystery)
- Cowboy Bebop (episodic space western, jazz, melancholy)
- Fate/Zero (dark battle royale, tragic heroes, moral complexity)

---

## Integration with Module 13

**This library is companion resource to Module 13 (Narrative Calibration)**:

- **Module 13 defines**: Narrative DNA schema (scales, tropes, styles)
- **This library provides**: Pre-calibrated DNA profiles extracted from popular anime
- **Relationship**: Library = examples, Module 13 = system

**File References**:
- Narrative DNA schema: `aidm/instructions/13_narrative_calibration.md`
- Session export schema: `aidm/schemas/session_export_schema.json` (stores `active_narrative_profile`)
- Module 00 (Session Init): References this library during Session Zero
- Module 04 (NPCs): Uses `dialogue_style` from active profile
- Module 05 (Great Sage): Uses narrative scales for tone consistency
- Module 08 (Combat): Uses `combat_narrative_style` from active profile

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
