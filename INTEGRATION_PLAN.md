# AIDM Integration Enhancement Plan for Sonnet 3.5

## Executive Summary
Fix integration gaps between Modules 06/07/12/13, add explicit orchestration, and introduce new features to strengthen narrative generation pipeline.

---

## Phase 1: Fix Critical Integration Gaps (Priority: URGENT)
**Time: 1-2 hours**

### Task 1.0: Enhance Module 04 for Ensemble Support
```markdown
Location: Module 04, add to npc_schema requirements (Step 1)
ADD to Schema Key Fields section:

ENSEMBLE SUPPORT (for recurring NPCs):
- spotlight_data: {
    scene_count: int (tracks appearances),
    last_spotlight_session: int,
    growth_stage: string (Introduction/Bonding/Challenge/Growth/Mastery),
    current_arc: string (description of NPC's personal storyline)
  }
- ensemble_role: {
    archetype: string (Struggler/Heart/Skeptic/Dependent/Equal/Observer/Rival),
    assigned_reason: string (why this archetype fits),
    relationship_to_pc: string (Mentor/Friend/Rival/Romance/Protege)
  }
- npc_relationships: {
    [other_npc_id]: {
      affinity: -100 to +100,
      relationship_type: string,
      subplot_potential: boolean
    }
  }

USAGE:
- Module 05 reads spotlight_data to balance scene generation
- Module 05 uses ensemble_role.archetype to frame NPC scenes appropriately
- Module 04 updates spotlight_data.scene_count after each significant interaction
- NPC-to-NPC relationships create B-plot opportunities (Module 05)

EXAMPLE (Elena):
spotlight_data: {
  scene_count: 12,
  last_spotlight_session: 8,
  growth_stage: "Challenge" (struggling with trust issues),
  current_arc: "Learning to rely on others after years of self-reliance"
}
ensemble_role: {
  archetype: "Heart" (moral compass, reminds PC of humanity),
  assigned_reason: "Protective values + high affinity + grounds PC in reality",
  relationship_to_pc: "Friend/Protege"
}
npc_relationships: {
  "marcus_npc_001": { affinity: 45, relationship_type: "Respectful colleagues", subplot_potential: true },
  "tomas_npc_002": { affinity: 85, relationship_type: "Protective guardian", subplot_potential: false }
}
```

### Task 1.1: Module 06 → Module 13 Explicit Integration
```markdown
Location: Module 06, after Phase 0.5 line ~176
ADD:
- EXECUTE: Module 13.interpret_narrative_profile(selected_profile)
- RECORD: power_fantasy_rating (0-10) → world_state.narrative_calibration
- DETERMINE: growth_model (Modest/Accelerated/Instant) → character.progression_model
```

### Task 1.2: Module 06 → Module 12 Initial Scale Determination
```markdown
Location: Module 06, after Phase 0.6 line ~217
ADD:
- EXECUTE: Module 12.determine_initial_scale()
  - Input: power_tier, op_mode, starting_context
  - Output: narrative_scale (Tactical/Strategic/Ensemble/etc.)
- STORE: narrative_scale → character.narrative_context.current_scale
- CREATE: Memory(NARRATIVE_SCALE, heat=60, decay=normal)
```

### Task 1.3: Module 07 → Module 13 Profile Coordination
```markdown
Location: Module 07, Step 7 (new) after current Step 6
ADD:
Step 7: Narrative Profile Integration
- IF anime has narrative_profile: LOAD from libraries
- ELSE: GENERATE profile based on anime research
- PASS to Module 13 for DNA interpretation
- CONFIRM Power Fantasy alignment with character concept
```

### Task 1.4: Add Orchestration Map to Module 01
```markdown
Location: Module 01, after header, before Sacred Rule (~line 15)
ADD:
## Module Dependencies & Call Flow

CHARACTER CREATION:
06.Phase0.3 → [07 if anime] → 06.Phase0.4 → 06.Phase0.5 → 13 → 06.Phase0.6 → 12 → Complete

RUNTIME NARRATIVE:
01.Intent → 02.Memory → 13.DNA → 12.Scale → 05.Generate → 01.Respond

MODULE REQUIREMENTS:
- Module 13 REQUIRES: narrative_profile (from 06/07)
- Module 12 REQUIRES: power_tier, op_mode (from 06)
- Module 05 REQUIRES: constraints (from 12+13)
- Module 01 ORCHESTRATES: all runtime calls
```

---

## Phase 2: Add Power Tier Progression System (Priority: HIGH)
**Time: 2-3 hours**

### Task 2.1: Create Tier Progression Framework
```markdown
NEW SECTION: Module 12, after Power Imbalance
## Power Tier Progression & Scale Shifts
When character power tier changes:
1. CHECK: Current tier → New tier gap
2. IF gap ≥ 1 full tier: Mandatory scale reevaluation
3. APPLY: Scale Shift Ceremony (narrative moment acknowledging power growth)
4. UPDATE: Memory(POWER_TIER_CHANGE) + trigger Module 12 recalc

Progression Triggers:
- Level threshold (e.g., Level 20 → Tier bump)
- Story event (awakening, power-up, training complete)
- Equipment (legendary item grants tier bump)
- Temporary (transformation, buff, divine blessing)

Scale Shift Ceremony Examples:
- Tier 9→8: "Your movements blur. What once challenged now seems slow."
- Tier 8→7: "The earth cracks beneath your stance. You've transcended mortal limits."
- Tier 7→6: "Your power draws attention across nations. You are now a strategic asset."
- Tier 6→5: "Reality bends around you. Physical laws are now suggestions."
```

### Task 2.2: Add Progressive OP Mode
```markdown
ENHANCE: Module 12 OP Protagonist section
## Progressive OP Mode
For Power Fantasy 3-6 (Accelerated Growth):
- Starts normal, becomes OP gradually
- Each tier crossed: Re-evaluate if OP Mode should enable
- Threshold: When power_imbalance > 10 consistently
- Auto-suggest OP archetype based on behavior:
  - Many defensive actions → Mob (restraint)
  - Humor responses → Saitama (oblivious)
  - Building focus → Rimuru (builder)
```

---

## Phase 3: Add Narrative Conflict Generator (Priority: MEDIUM)
**Time: 2-3 hours**

### Task 3.1: Add Non-Combat Tension System to Module 12
```markdown
Location: Module 12, after Power Imbalance Detection section
ADD:
## Non-Combat Tension for High Power Imbalance

When power_imbalance > 10 (OP protagonist territory):
- REDUCE: Combat encounters 50% (PC too strong for meaningful fights)
- INCREASE: Social/existential encounters 200% (stakes shift)

TENSION CATEGORIES:

Social (Tier-Agnostic):
- Secret identity at risk | Romantic misunderstandings | Cultural faux pas
- Bureaucratic nightmares | Family/friend conflicts | Social expectations

Existential (High-Tier 6+):
- Purpose without challenge | Isolation from normal life | Weight of responsibility
- Fear of own power | Immortality ennui | Being worshipped vs. befriended

Structural (Always Valid):
- Time limits (can't be everywhere) | Information limits (power ≠ omniscience)
- Social limits (can't force friendship/love) | Moral limits (could but shouldn't)

IMPLEMENTATION:
- Module 05 generates encounters from appropriate category
- Pass tension_type to Module 13 for tone/pacing adjustment
- Create memories with TENSION category for tracking themes
```

### Task 3.2: Enhance Module 13 with Tension Preferences
```markdown
ADD to: narrative_profile_schema.json
"tension_preferences": {
  "combat": 0.0-1.0,
  "social": 0.0-1.0,
  "political": 0.0-1.0,
  "existential": 0.0-1.0,
  "mystery": 0.0-1.0,
  "resource": 0.0-1.0
}
```

---

## Phase 4: Add Ensemble Cast Manager (Priority: MEDIUM)
**Time: 3-4 hours**

### Task 4.1: Add Ensemble Cast Manager to Module 05
```markdown
Location: Module 05, new section after Faction-Based Narrative Generation
ADD:
## Ensemble Cast Management

PURPOSE: When narrative_scale = Ensemble/Reverse Ensemble (Module 12), shift story focus to NPC party members while PC enables/influences.

### Core Systems

**1. Spotlight Rotation**
- Track scene_count per NPC in world_state.npcs[].spotlight_data
- Each session: Ensure at least 1 spotlight scene per recurring NPC
- FLAG: When NPC neglected > 3 scenes → Auto-generate hook involving them
- METRIC: spotlight_balance = min(scene_counts) / max(scene_counts) [Target: >0.6]

**2. Growth Tracking** (Simplified Character Arcs)
- NPCs have growth_stage: [Introduction → Bonding → Challenge → Growth → Mastery]
- Track emotional_arc and power_arc separately
- MILESTONE: Each stage completion → Create MEMORY + unlock new capability/depth
- Example: Genos starts "Seeking strength" → "Understanding limits" → "Finding purpose beyond power"

**3. Relationship Web**
- PC↔NPC: Track relationship_type [Mentor/Friend/Rival/Romance/Dependent]
- NPC↔NPC: Generate subplots (2 NPCs bonding/conflicting creates B-plot)
- Faction↔Party: Track party reputation separately from PC reputation
- CASCADES: PC actions affect NPC relationships ("You saved my rival, now I respect you more")

**4. Reverse Ensemble Mode** (High Power Imbalance)
When op_protagonist_mode = TRUE and power_imbalance > 10:
- NPCs become viewpoint characters for scenes
- PC narrated as force of nature / mysterious benefactor / overwhelming presence
- Generate NPC internal monologues about PC's actions
- Example: "Genos watches Saitama walk away. 'How is he so strong? What training did he do?'"

**5. Ensemble Archetypes** (Auto-Assign to Party NPCs)
When PC power_tier >> party power_tier:
- The Struggler (Genos): Tries to keep up, measures self against PC
- The Heart (Mumen Rider): Moral compass, reminds PC of humanity
- The Skeptic: Questions PC methods, provides tension
- The Dependent: Needs PC protection, creates stakes
- The Equal: Different power type (social/political/knowledge), PC can't solve everything
- The Observer: Documents PC legend, provides narration
- The Rival: Refuses to accept gap, drives own growth

AUTO-ASSIGNMENT:
- Check NPC personality + goals → Suggest archetype
- Allow overlap (1 NPC can be Struggler + Rival)
- Track archetype in npc_schema.relationship_context

### Integration with Narrative Generation

**Standard Mode** (power_imbalance < 10):
- Generate quests as normal
- NPCs provide support/commentary
- PC is protagonist

**Ensemble Mode** (power_imbalance 10-15):
- 50% scenes: PC + NPCs collaborate (balanced)
- 30% scenes: NPC spotlight (PC enables/supports)
- 20% scenes: PC spotlight (showcase power gap)

**Reverse Ensemble Mode** (power_imbalance > 15):
- 70% scenes: NPC viewpoint (PC as mysterious/overwhelming force)
- 20% scenes: PC mundane activities (contrast power with normalcy)
- 10% scenes: PC power display (reminder of capability)

### Example Scene Generation

Standard Quest:
"Elena asks for help clearing bandits. You accept."

Ensemble Mode:
"Elena has been training. She wants to clear the bandits herself. She asks if you'll watch her back—not do it for her. This is her test. Do you:
A) Let her lead, only intervene if deadly
B) Offer tactical advice but let her fight
C) Clear it yourself (faster, but damages her confidence)"

Reverse Ensemble:
"[ELENA POV] You grip your sword. The bandit camp ahead. Marcus offered to come, but this is your fight. You glance back. He's... drinking coffee. Casually. Like this isn't dangerous. Like he knows you'll be fine. Or like he could fix anything that goes wrong with a thought. You don't know which is more terrifying."

### Spotlight Balance Protocol

END OF EACH SESSION:
1. CALCULATE: spotlight_balance for all recurring NPCs
2. IF any NPC < 0.4 balance → FLAG for next session hook
3. GENERATE: Hook involving neglected NPC (personal quest, relationship scene, crisis)
4. UPDATE: NPC.spotlight_data.scene_count

TRACKING:
world_state.npcs[].spotlight_data: {
  scene_count: int,
  last_spotlight: session_number,
  growth_stage: string,
  current_arc: string
}
```

---

## Phase 5: Add Combat Narration Enhancer (Priority: LOW)
**Time: 2 hours**

### Task 5.1: Add Tier-Specific Combat Language to Module 08
```markdown
Location: Module 08, after Cinematic Resolution section
ADD:
## Tier-Appropriate Combat Narration

Combat language MUST match power_tier to maintain narrative consistency.

Tier 11-9 (Human-Superhuman):
- Verbs: strikes, dodges, bleeds, staggers, grunts, parries
- Scale: personal space, immediate area, room-sized
- Consequences: injuries, exhaustion, broken bones, death
- Example: "Blade bites shoulder. Blood. Stagger. -15 HP."

Tier 8-7 (Urban-Nuclear):
- Verbs: demolishes, obliterates, craters, vaporizes, shatters
- Scale: buildings, city blocks, mountains
- Consequences: collateral damage, evacuations, landscape scarring
- Example: "Punch connects. Shockwave flattens three buildings. Civilians scatter."

Tier 6-5 (Tectonic-Substellar):
- Verbs: sunders, atomizes, warps, transcends, rends
- Scale: continents, moons, planets
- Consequences: geographic reformation, extinction events, atmospheric disruption
- Example: "Clash splits continent. Tectonic plates shift. New ocean forming."

Tier 4-3 (Stellar-Cosmic):
- Verbs: unravels, conceptualizes, manifests, erases, rewrites
- Scale: solar systems, galaxies, dimensional boundaries
- Consequences: reality distortion, temporal paradoxes, causality breaks
- Example: "Stars blink out. Galaxy dims. Time stutters backward three seconds."

Tier 2-1 (Multiversal-Higher):
- Verbs: authors, negates, subsumes, transcends, encompasses
- Scale: infinite universes, conceptual frameworks, narrative layers
- Consequences: narrative causality, meta-effects, ontological shifts
- Example: "You erase the concept of 'enemy's victory' from all timelines simultaneously."

IMPLEMENTATION:
1. CHECK: character.power_tier before narrating combat
2. SELECT: Appropriate verb set + scale + consequences
3. NARRATE: Using tier-matched language
4. AVOID: Tier mismatch (Tier 9 character "shattering mountains" or Tier 5 character "struggling with street thugs")
```

---

## Phase 6: Add Narrative Coherence Validator (Priority: LOW)
**Time: 1-2 hours**

### Task 6.1: Create Consistency Checker
```markdown
ADD to: Module 01, after Sacred Rule
## Narrative Coherence Check
Before responding, validate:
1. Power tier consistency (character shouldn't struggle with lower tier)
2. Scale consistency (Tier 6 shouldn't have street-level problems)
3. Archetype consistency (Saitama-type shouldn't show fear)
4. Growth consistency (check progression_model alignment)

IF inconsistency detected:
- LOG: "Coherence warning: [specific issue]"
- ADJUST: Reframe scene to match established parameters
- CONTINUE: With adjusted narrative
```

---

## Phase 7: Documentation & Testing (Priority: CRITICAL)
**Time: 2 hours**

### Task 7.0: Update Schemas for Ensemble Support
```markdown
FILE: /aidm/schemas/npc_schema.json
VERSION: 2.2.0 → 2.3.0

ADD to properties (after "narrative_role"):
"ensemble_context": {
  "type": "object",
  "description": "Support for ensemble cast management (Module 05)",
  "properties": {
    "spotlight_data": {
      "type": "object",
      "properties": {
        "scene_count": {
          "type": "integer",
          "minimum": 0,
          "default": 0,
          "description": "Number of significant scenes this NPC has appeared in"
        },
        "last_spotlight_session": {
          "type": "integer",
          "description": "Session number of last significant appearance"
        },
        "growth_stage": {
          "type": "string",
          "enum": ["introduction", "bonding", "challenge", "growth", "mastery"],
          "description": "NPC character arc progression"
        },
        "current_arc": {
          "type": "string",
          "description": "Description of NPC's personal storyline"
        }
      }
    },
    "ensemble_role": {
      "type": "object",
      "properties": {
        "archetype": {
          "type": "string",
          "enum": ["struggler", "heart", "skeptic", "dependent", "equal", "observer", "rival", "none"],
          "description": "Role in ensemble when PC is OP: struggler (Genos), heart (Mumen Rider), skeptic, dependent, equal (different power type), observer (documents legend), rival"
        },
        "assigned_reason": {
          "type": "string",
          "description": "Why this archetype fits (based on personality + PC relationship)"
        },
        "relationship_to_pc": {
          "type": "string",
          "enum": ["mentor", "friend", "rival", "romance", "protege", "peer", "other"],
          "description": "Primary relationship dynamic"
        }
      }
    },
    "subplot_potential": {
      "type": "boolean",
      "default": false,
      "description": "True if NPC's relationships create B-plot opportunities"
    }
  }
}

RATIONALE: 
- spotlight_data enables Module 05 to balance screen time
- ensemble_role allows archetype-based scene generation
- Complements existing npc_relationships for subplot tracking
```

### Task 7.1: Add Tension Preferences to Narrative Profile Schema
```markdown
FILE: /aidm/schemas/narrative_profile_schema.json
VERSION: 2.0.0 → 2.1.0

ADD to properties (after "combat_narrative_style"):
"tension_preferences": {
  "type": "object",
  "description": "What creates stakes/conflict in this narrative style",
  "properties": {
    "combat": {
      "type": "number",
      "minimum": 0.0,
      "maximum": 1.0,
      "default": 0.5,
      "description": "Weight for physical combat tension (0.0-1.0)"
    },
    "social": {
      "type": "number",
      "minimum": 0.0,
      "maximum": 1.0,
      "default": 0.3,
      "description": "Weight for social/relationship tension"
    },
    "political": {
      "type": "number",
      "minimum": 0.0,
      "maximum": 1.0,
      "default": 0.2,
      "description": "Weight for political/factional maneuvering"
    },
    "existential": {
      "type": "number",
      "minimum": 0.0,
      "maximum": 1.0,
      "default": 0.1,
      "description": "Weight for existential/philosophical stakes"
    },
    "mystery": {
      "type": "number",
      "minimum": 0.0,
      "maximum": 1.0,
      "default": 0.3,
      "description": "Weight for investigation/mystery-solving"
    },
    "resource": {
      "type": "number",
      "minimum": 0.0,
      "maximum": 1.0,
      "default": 0.4,
      "description": "Weight for survival/resource management"
    }
  },
  "description_note": "Values don't need to sum to 1.0 - they're independent weights. High combat (0.8) + high social (0.7) = action series with strong character dynamics (MHA, Demon Slayer)"
}

EXAMPLES:
- Attack on Titan: {combat: 0.9, social: 0.6, political: 0.5, existential: 0.8, mystery: 0.7, resource: 0.8}
- One Punch Man: {combat: 0.3, social: 0.7, political: 0.1, existential: 0.6, mystery: 0.2, resource: 0.1}
- Death Note: {combat: 0.1, social: 0.8, political: 0.9, existential: 0.7, mystery: 1.0, resource: 0.2}
- Konosuba: {combat: 0.4, social: 0.9, political: 0.2, existential: 0.1, mystery: 0.3, resource: 0.6}

RATIONALE:
- Module 12 uses this when power_imbalance > 10 to shift from combat to appropriate tension type
- Module 13 already calibrates tone/pacing, this extends to encounter generation
```

### Task 7.2: Add Progression Model to Character Schema
```markdown
FILE: /aidm/schemas/character_schema.json
VERSION: 2.3.0 → 2.4.0

ENHANCE "narrative_context" property:
Add under "narrative_context.properties":
"progression_model": {
  "type": "string",
  "enum": ["modest", "accelerated", "instant", "static"],
  "description": "Growth speed: modest (slow grind), accelerated (power fantasy 3-6), instant (OP from start), static (already max power)",
  "default": "accelerated"
},
"current_scale": {
  "type": "string",
  "enum": [
    "tactical_survival",
    "strategic_combat",
    "ensemble_focus",
    "reverse_ensemble",
    "mythology_journey",
    "faction_building",
    "mythic_spectacle",
    "conceptual_philosophy",
    "metafictional"
  ],
  "description": "Active narrative scale (from Module 12)"
},
"scale_shift_history": {
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "from_scale": {"type": "string"},
      "to_scale": {"type": "string"},
      "trigger": {"type": "string", "description": "What caused shift (tier change, story event, etc.)"},
      "session_number": {"type": "integer"},
      "power_tier_at_shift": {"type": "string"}
    }
  },
  "description": "Track narrative scale transitions for character arc"
}

RATIONALE:
- progression_model determined in Module 06 Phase 0.5, stored here
- current_scale set by Module 12, used by Module 05 for scene generation
- scale_shift_history creates narrative moments when power tier crosses thresholds
```

### Task 7.3: Update SCHEMA_CHANGELOG
```markdown
FILE: /aidm/schemas/SCHEMA_CHANGELOG.md

ADD:
## Version 2.3.0 - NPC Schema (2025-10-29)
**Changes**:
- Added `ensemble_context` for ensemble cast management
- Added `spotlight_data` (scene_count, last_spotlight_session, growth_stage, current_arc)
- Added `ensemble_role` (archetype, assigned_reason, relationship_to_pc)
- Added `subplot_potential` flag

**Migration**: Existing NPCs default to `ensemble_role.archetype: "none"`, `spotlight_data.scene_count: 0`

## Version 2.1.0 - Narrative Profile Schema (2025-10-29)
**Changes**:
- Added `tension_preferences` with 6 categories (combat, social, political, existential, mystery, resource)
- Values range 0.0-1.0, independent weights (don't need to sum to 1.0)

**Migration**: Existing profiles default all tensions to 0.5 (balanced)

## Version 2.4.0 - Character Schema (2025-10-29)
**Changes**:
- Added `narrative_context.progression_model` (modest/accelerated/instant/static)
- Added `narrative_context.current_scale` (active narrative scale)
- Added `narrative_context.scale_shift_history` (track scale transitions)

**Migration**: Existing characters default `progression_model: "accelerated"`, `current_scale: "tactical_survival"`
```

### Task 7.1: Update Architecture Documentation
```markdown
UPDATE: /docs/ARCHITECTURE.md
- Add Module 14 (Ensemble Manager) to module list
- Add NARRATIVE_ORCHESTRATION.md to documentation
- Update integration flow diagram
- Note new libraries added
```

### Task 7.2: Create Integration Tests
```markdown
NEW FILE: /tests/integration/narrative_pipeline_test.md
Test Cases:
1. Session Zero → Anime character → OP detection → Scale selection
2. Power tier progression → Scale shift → Memory update
3. Ensemble mode → NPC spotlight → Relationship tracking
4. High tier combat → Appropriate language → Consequence scaling
5. Narrative coherence → Archetype consistency → Power consistency
```

### Task 7.3: Update ROADMAP
```markdown
UPDATE: /docs/ROADMAP.md
Phase 2.1f - Narrative Integration Enhancement ✓
- Module integration fixes ✓
- Power progression system ✓
- Ensemble manager ✓
- Combat narration enhancement ✓
- Coherence validation ✓
```

---

## Implementation Order & Priority

### Week 1 (Critical Path)
1. **Day 1-2**: Phase 1 - Integration Gaps (URGENT)
2. **Day 3-4**: Phase 7 - Documentation (CRITICAL)
3. **Day 5**: Test integration fixes

### Week 2 (Core Features)
4. **Day 1-2**: Phase 2 - Power Progression (HIGH)
5. **Day 3-4**: Phase 3 - Tension System (MEDIUM)
6. **Day 5**: Test new systems

### Week 3 (Enhancement)
7. **Day 1-3**: Phase 4 - Ensemble Manager (MEDIUM)
8. **Day 4-5**: Phase 5 & 6 - Combat Language & Validator (LOW)

---

## Success Metrics

**Integration Health**:
- [ ] All modules explicitly reference their dependencies
- [ ] NARRATIVE_ORCHESTRATION.md shows clear flow
- [ ] No implicit handoffs remain

**Feature Completeness**:
- [ ] Power progression creates narrative moments
- [ ] Non-combat tension system reduces OP monotony
- [ ] Ensemble manager balances spotlight time
- [ ] Combat language matches power tier

**System Coherence**:
- [ ] 100% of test cases pass
- [ ] No narrative consistency breaks
- [ ] Documentation reflects actual behavior

---

## Risk Mitigation

**Risk**: Over-engineering ensemble system
**Mitigation**: Start with simple spotlight tracking, enhance iteratively

**Risk**: Breaking existing integration
**Mitigation**: Create integration tests FIRST, then modify

**Risk**: Token count explosion
**Mitigation**: Apply TOKEN_OPTIMIZATION to each new module/library

---

## Expected Outcomes

After implementation:
1. **Clear Orchestration**: Every module knows when it's called and what it provides
2. **Progressive Power**: Natural tier progression with narrative weight
3. **Tension Without Combat**: OP characters have meaningful conflicts
4. **Living World**: Ensemble cast grows independently
5. **Narrative Polish**: Combat language scales with tier appropriately
6. **System Confidence**: Coherence validation prevents narrative breaks

**Total Estimated Time**: 35-45 hours over 3 weeks
**Token Impact**: +~15% (before optimization), +~5% (after optimization)
**System Improvement**: 7/10 → 9.5/10 integration score
