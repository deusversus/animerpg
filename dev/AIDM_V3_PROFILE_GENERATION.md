# AIDM v3 Profile Generation

> **Purpose:** Describes how to create new Narrative Profiles from anime research.
> This is distinct from Profile USAGE (loading existing profiles during gameplay).

---

## Two Workflows: Generation vs Usage

| Aspect | Profile Generation | Profile Usage |
|--------|-------------------|---------------|
| **When** | Session Zero / Setup | Per-turn gameplay |
| **Frequency** | Once per anime | Every turn |
| **Model** | Opus/Pro (expensive, thorough) | Haiku for retrieval |
| **Input** | Anime name + optional research | profile.yaml + rule_library chunks |
| **Output** | profile.yaml + example chunks | Context for Key Animator |
| **Web Search** | Optional (if available) | Not needed |

---

## Profile Generation Flow

```
┌──────────────────────────────────────────────────────────────────┐
│                      USER REQUEST                                │
│  "Create a profile for [Anime Name]"                            │
└─────────────────────────────────────┬────────────────────────────┘
                                      ▼
┌──────────────────────────────────────────────────────────────────┐
│                    RESEARCH PHASE (optional)                     │
│                                                                  │
│  IF web search available:                                        │
│    - Query: "[Anime] tone pacing combat style analysis"          │
│    - Query: "[Anime] power system explained"                     │
│    - Query: "[Anime] vs [similar anime] comparison"              │
│                                                                  │
│  IF no web search:                                               │
│    - Rely on LLM training data knowledge                         │
│    - Request user to provide details if unfamiliar               │
└─────────────────────────────────────┬────────────────────────────┘
                                      ▼
┌──────────────────────────────────────────────────────────────────┐
│                   EXTRACTION PHASE (Opus/Pro)                    │
│                                                                  │
│  Load: __MASTER_TEMPLATE.md as structure guide                   │
│                                                                  │
│  Extract:                                                        │
│  1. Mechanical Configuration (economy, crafting, progression)   │
│  2. 11 Narrative DNA Scales (with justifications)               │
│  3. 15 Storytelling Tropes (enabled/disabled + explanations)    │
│  4. Pacing Rhythm (scene length, arc length, climax frequency)  │
│  5. Tonal Signature (emotions, violence, fanservice, optimism)  │
│  6. Dialogue Style (formality, banter, exposition method)       │
│  7. Combat Narrative Style (tactics, pacing, named attacks)     │
│  8. 3 Example Scenes (combat, dialogue, exploration)            │
│  9. Mechanical Scaffolding (power mapping, progression, combat) │
│  10. Usage Notes (when to use, calibration tips, mistakes)      │
└─────────────────────────────────────┬────────────────────────────┘
                                      ▼
┌──────────────────────────────────────────────────────────────────┐
│                    OUTPUT GENERATION                             │
│                                                                  │
│  Create:                                                         │
│  1. profiles/[anime_name].yaml                                   │
│     - Compact version of DNA scales, tropes, system mappings    │
│     - Used during gameplay for quick loading                    │
│                                                                  │
│  2. Full profile document (optional archive)                     │
│     - Complete __MASTER_TEMPLATE format with justifications     │
│     - Stored in aidm/libraries/narrative_profiles/              │
│                                                                  │
│  3. rule_library/examples/[anime_name].yaml                     │
│     - 3+ example scene chunks for RAG retrieval                 │
│     - Combat, dialogue, exploration scene examples              │
└─────────────────────────────────────┬────────────────────────────┘
                                      ▼
┌──────────────────────────────────────────────────────────────────┐
│                    USER VALIDATION                               │
│                                                                  │
│  Present extracted profile to user:                              │
│  "DanDaDan profile extracted:                                    │
│   - Absurd: 9/10, Comedy: 4/10, Tactical: 5/10                  │
│   - Tropes ON: Rapid tonal shifts, Rule of cool, Mystery box    │
│   - Combat: Fast, sakuga-heavy, minimal explanations            │
│                                                                  │
│   Adjustments needed?"                                           │
│                                                                  │
│  User can tweak values before finalizing.                       │
└──────────────────────────────────────────────────────────────────┘
```

---

## Template Reference

All generated profiles MUST conform to the Master Template structure:

**Location:** `aidm/libraries/narrative_profiles/__MASTER_TEMPLATE.md`

**Key Sections:**
1. Mechanical Configuration (JSON block)
2. 11 Narrative Scales (0-10 with justifications)
3. 15 Storytelling Tropes (ON/OFF with explanations)
4. Pacing Rhythm
5. Tonal Signature
6. Dialogue Style
7. Combat Narrative Style
8. 3 Example Scenes (minimum 20-30 lines each)
9. Mechanical Scaffolding (Module 12 integration)
10. Usage Notes & Calibration Tips

---

## Compact Profile Format (for v3 runtime)

The full template (~24KB) is too large for per-turn loading. Generate a compact YAML:

```yaml
# profiles/dandadan.yaml
# Generated from: aidm/libraries/narrative_profiles/dandadan_profile.md

name: "DanDaDan"
source_anime: "DanDaDan (2024-)"
confidence: 85

# 11 DNA Scales (0-10)
dna_scales:
  introspection_vs_action: 3
  comedy_vs_drama: 4
  simple_vs_complex: 5
  power_fantasy_vs_struggle: 6
  explained_vs_mysterious: 7
  fast_vs_slow: 2
  episodic_vs_serialized: 6
  grounded_vs_absurd: 9
  tactical_vs_instinctive: 5
  hopeful_vs_cynical: 3
  ensemble_vs_solo: 4

# 15 Tropes (ON/OFF)
tropes:
  fourth_wall_breaks: false
  inner_monologue: true
  visual_metaphor: true
  rapid_tonal_shifts: true
  tournament_arcs: false
  power_of_friendship: true
  tragic_backstories: true
  escalating_threats: true
  slice_of_life: true
  mystery_box: true
  unreliable_narrator: false
  existential_philosophy: false
  rule_of_cool: true
  mundane_made_epic: true
  tragic_hero: false

# System Mappings
combat_system: "spectacle"  # tactical, spirit, comedy, spectacle, narrative
progression_type: "accelerated"
growth_model: "accelerated"
power_tier_range: "T9-T7"

# Director Personality
director_personality: |
  You are a chaotic storyteller who loves absurdist comedy crashing into genuine horror.
  Romantic tension builds through bickering. Ghosts are scary AND funny.
  Switch tones mid-scene. Make it weird. Make it heartfelt. Make it loud.

# Pacing
scene_length: "rapid"
arc_length_sessions: 4-6

# Reference to full profile (for deep lookup)
full_profile_path: "aidm/libraries/narrative_profiles/dandadan_profile.md"
```

---

## Example Chunk Generation

From each profile, extract 3+ example scenes as Rule Library chunks:

```yaml
# rule_library/examples/dandadan.yaml

- id: "example_dandadan_combat"
  category: "example"
  source_module: "module_13"
  profile: "dandadan"
  scene_type: "combat"
  tags: ["example", "dandadan", "combat", "absurd", "rapid_shifts", "comedy_horror"]
  retrieve_conditions: ["profile.source == 'dandadan'", "scene_type == 'combat'"]
  content: |
    DANDADAN Combat (Absurd:9, Rapid Shifts:ON):
    Turbo Granny LAUNCHES. 100 km/h. Okarun screams. Momo: 'MOVE!' 
    Psychic barrier SLAMS—granny BOUNCES, cartoon physics. Lands. 
    Neck cracks 180°. Grins. 'You kids got SPUNK!' Okarun: 'Friendly?!' 
    'I'M GONNA RIP YOUR GUTS OUT!' 'NOPE, STILL HOSTILE!'
    
    Key: Rapid comedy→tension shifts, cartoon physics, banter mid-combat, 
    gross-out humor, genuine stakes underneath absurdity.

- id: "example_dandadan_dialogue"
  category: "example"
  source_module: "module_13"
  profile: "dandadan"
  scene_type: "dialogue"
  tags: ["example", "dandadan", "dialogue", "romance", "bickering", "awkward"]
  retrieve_conditions: ["profile.source == 'dandadan'", "scene_type == 'dialogue'"]
  content: |
    DANDADAN Dialogue (Awkward Romance, Bickering):
    Okarun: "Y-you're not hurt, right? That ghost was—"
    Momo: "Of course I'm not hurt! Unlike SOME people who screamed the whole time!"
    Okarun: "I didn't—! My transformation was cooldown—!"
    Momo: "Excuses!" [secretly checking him for injuries]
    Okarun: [notices] "...You're worried."
    Momo: [RED] "I AM NOT!" [shoves him]
    
    Key: Tsundere dynamic, care shown through denial, physical comedy, 
    genuine affection under hostility, both equally embarrassed.

- id: "example_dandadan_exploration"
  category: "example"
  source_module: "module_13"
  profile: "dandadan"
  scene_type: "exploration"
  tags: ["example", "dandadan", "exploration", "investigation", "creepy", "humor"]
  retrieve_conditions: ["profile.source == 'dandadan'", "scene_type == 'exploration'"]
  content: |
    DANDADAN Exploration (Creepy + Curious):
    Abandoned hospital. Momo's phone light flickers. "Classic."
    Okarun: "Maybe we should—" 
    CRASH. Something upstairs. They freeze.
    Momo: "...After you."
    Okarun: "Why me?!"
    Momo: "You have TURBO GRANNY."
    Okarun: "She's DORMANT!"
    Slow creak. Door opening on its own. Cold air.
    Both: [long stare at each other, then door]
    Okarun: "...Together?"
    Momo: "...Fine."
    [tentatively approach, Momo slightly behind but pretending not to be]
    
    Key: Horror setup undercut by bickering, reluctant teamwork, 
    genuine creepy atmosphere, characters are scared but keep going.
```

---

## Tasks: Profile Generation System

Add to Phase 2 or create separate Phase:

- [ ] **Profile Generator Tool**
  - [ ] Create `scripts/generate_profile.py`
  - [ ] Load __MASTER_TEMPLATE.md as extraction guide
  - [ ] Implement Opus/Pro prompt for DNA extraction
  - [ ] Generate compact YAML from full extraction
  - [ ] Generate example scene chunks

- [ ] **Research Integration (Optional)**
  - [ ] Add web search capability (if available)
  - [ ] Query for anime analysis, comparisons, power systems
  - [ ] Fall back to training data if no search

- [ ] **Validation Flow**
  - [ ] Present extracted profile to user
  - [ ] Accept adjustments before finalizing
  - [ ] Save to profiles/ and rule_library/examples/

- [ ] **Pre-made Library**
  - [ ] Generate profiles for 10+ common anime
  - [ ] Ship with v3 as starter library
  - [ ] HxH, AoT, DanDaDan, Konosuba, OPM, Demon Slayer, etc.

---

## Integration with Main Orchestration

Profile Generation is a **separate tool**, not part of the per-turn game loop.

```
SESSION ZERO:
  1. User: "I want to play in a DanDaDan-style world"
  2. System: Check if profiles/dandadan.yaml exists
     - IF exists: Load it, proceed
     - IF not: Trigger Profile Generator
  3. Profile Generator: Extract DNA, create YAML, create chunks
  4. User validates/adjusts
  5. Profile saved, proceed to character creation

GAMEPLAY (per-turn):
  - Load profiles/dandadan.yaml (compact, fast)
  - Query rule_library/examples/dandadan.yaml for scene examples
  - No generation, just retrieval
```

---

## Reference

- **Master Template:** `aidm/libraries/narrative_profiles/__MASTER_TEMPLATE.md`
- **Existing Profiles:** `aidm/libraries/narrative_profiles/`
- **Module 07 (v2):** Original anime research protocol
- **Module 13 (v2):** Narrative calibration and DNA scales
