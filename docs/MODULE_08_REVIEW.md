# Module 08: Combat Resolution - Comprehensive Audit

**Audit Date**: November 24, 2025  
**Module Version**: 2.0  
**Auditor**: GitHub Copilot (Claude Sonnet 4.5)  
**Status**: NEEDS REVISION (CRITICAL token overruns + architectural issues)

---

## Executive Summary

Module 08 (Combat Resolution) provides JRPG turn-based combat mechanics with **excellent validation protocols** and **comprehensive death/resurrection systems**. The 5-step pre-combat validation (Resources → Prerequisites → Calculation → State Update → Narrative) is **systematically sound** and prevents common errors. Tier-appropriate combat language successfully prevents narrative scaling mismatches.

**CRITICAL ISSUES**:
1. **Token Budget Failure**: ~11,000-12,500 tokens (267-317% OVER Tier 1 target of 3K). Mechanical Systems Integration section alone consumes 3,000 tokens duplicating Module 09 content.
2. **Human-Centric Language**: Instructional tone throughout ("BEFORE generating ANY combat narrative, ALWAYS validate:", "DO NOT proceed") assumes human user rather than agentic AI executor. Same architectural misalignment as Module 07.
3. **Massive Content Duplication**: Progression types explained exhaustively in Module 08 (3K tokens), will be explained again in Module 09. Tier language duplicates Module 12 content.

**MODERATE ISSUES**:
1. Tier-Appropriate Language section (2K tokens) duplicates Module 12 Narrative Scaling verb sets
2. Missing explicit integration with Module 11 (Dice Resolution) for roll notation

**STRENGTHS**:
- Pre-combat validation protocol is bulletproof (5 systematic steps)
- Change Log integration for atomic state updates is exemplary
- Narrative Profile combat_narrative_style integration is elegant
- Death system nuanced (downed ≠ dead, injury table, resurrection tiers)
- Boss battle and tournament frameworks complete

**APPROVAL STATUS**: ❌ **NEEDS REVISION** - Extract Mechanical Systems Integration (3K tokens) to separate guide, condense Tier Language to reference Module 12, rephrase to AI-directive language.

---

## Module Structure Analysis

### Current Organization (8 major sections)

1. **Purpose & Core Principle** (~100 tokens)
   - Clear framing: Combat = "STORY THROUGH CONFLICT, not math"
   - ✅ Well-stated

2. **Pre-Combat Validation Protocol** (~2,500 tokens)
   - 5-step validation: Resource → Prerequisite → Calculation → State → Narrative
   - Exhaustive examples with code blocks and JSON
   - ⚠️ Overly verbose with repeated warnings ("DO NOT proceed", "HALT", "ALWAYS")

3. **Combat Types & Player Actions** (~1,500 tokens)
   - Standard/Narrative/Quick resolution
   - 5 player actions (Attack/Skill/Item/Defend/Flee)
   - Enemy AI priority system
   - ✅ Complete coverage

4. **Damage, Status, Boss Battles** (~1,500 tokens)
   - Damage types, resistances (immune/resistant/vulnerable)
   - Status effects (buffs/debuffs)
   - Boss traits (phases, mechanics, narrative beats)
   - Tournament framework (structure, fatigue, bracket tracking)
   - ✅ Comprehensive

5. **Combat Narration (Narrative Profile Integration)** (~1,200 tokens)
   - Checks narrative_profile_schema.combat_narrative_style
   - Parameters: strategy_vs_spectacle (0-10), sakuga_moments (ON/OFF), named_attacks, environmental_destruction
   - Examples: DanDaDan (spectacle), HxH (strategy), Demon Slayer (sakuga)
   - ✅ Excellent integration, shows how narrative DNA affects combat voice

6. **Victory & Defeat Narration** (~400 tokens)
   - 4-element victory protocol (visceral death, environmental impact, emotional beat, transition hook)
   - 3-element defeat protocol (how defeat happens, downed/death state, player agency)
   - ✅ Strong narrative guidance

7. **Death & Resurrection System** (~1,500 tokens)
   - Downed state (≠ dead), death saves (3 success/fail)
   - Injury table (d20 roll if 2+ fails)
   - Resurrection tiers (Revivify/Raise Dead/Resurrection/True Res with costs)
   - Anime variants (senzu, Return by Death, willpower, Aqua)
   - ✅ Nuanced, prevents cheap death

8. **Combat Maneuvers & Tournament Framework** (~800 tokens)
   - Grapple, Disarm, Called Shot, Aid actions
   - Tournament structure (seeding, fatigue, bracket tracking, spectators)
   - ✅ Complete tactical options

9. **Tier-Appropriate Combat Narration** (~2,000 tokens)
   - Language by tier (T11-T1) with verb sets
   - Tier mismatch prevention examples
   - Context application (environmental modifiers, secret ID)
   - ⚠️ **Duplicates Module 12 content** - Should reference, not re-explain

10. **Mechanical Systems Integration (Phase 4)** (~3,000 tokens)
    - 5 progression types: mastery_tiers, class_based, quirk_awakening, milestone_based, static_op
    - Type-specific XP calculation for each
    - Exhaustive examples per type
    - ❌ **CRITICAL DUPLICATION** - Module 09 will explain these same types

### Structural Assessment

**Strengths**:
- Pre-combat validation is systematic and enforceable
- Narrative Profile integration shows cross-module coherence
- Death/resurrection system prevents trivial death
- Boss and tournament frameworks enable story arcs

**Weaknesses**:
- Mechanical Systems Integration should be separate guide or heavy reference to Module 09
- Tier Language should reference Module 12, not duplicate verb sets
- Verbose warnings throughout ("ALWAYS", "NEVER", "DO NOT") inflate token count

---

## Critical Issues

### Issue 1: Token Budget Catastrophic Failure (CRITICAL)

**Problem**: Module 08 consumes ~11,000-12,500 tokens, **267-317% OVER** Tier 1 budget (3K target).

**Breakdown**:
- Pre-Combat Validation: 2,500 tokens (acceptable, core functionality)
- Combat Types/Actions: 1,500 tokens (acceptable)
- Narrative Profile Integration: 1,200 tokens (acceptable, unique to Module 08)
- **Tier-Appropriate Language: 2,000 tokens** (DUPLICATE of Module 12)
- Death/Resurrection: 1,500 tokens (acceptable, unique system)
- **Mechanical Systems Integration: 3,000 tokens** (MASSIVE DUPLICATE of Module 09)
- Other sections: 800 tokens (acceptable)

**Token Violators**:
1. **Mechanical Systems Integration (3,000 tokens)**: Explains 5 progression types with exhaustive examples. Module 09 will explain the same types. Should be condensed to: "XP calculation varies by progression type (mastery_tiers, class_based, quirk_awakening, milestone_based, static_op). See Module 09 for type-specific rules. Apply advancement_rules from session_state.mechanical_systems.progression."

2. **Tier-Appropriate Language (2,000 tokens)**: Repeats Module 12's power tier verb sets. 11 tiers × examples = bloat. Should be: "Combat narration MUST match power_tier. T11-9 = personal-scale verbs (strikes, dodges), T8-7 = building-scale (demolishes, craters), T6-5 = continental (sunders, warps), T4-3 = cosmic (unravels, erases), T2-1 = conceptual (authors, negates). See Module 12 for complete tier language framework and context modifiers."

3. **Pre-Combat Validation (2,500 tokens)**: Overly verbose with repeated warnings. Can condense by 30% (~750 tokens saved) by removing instructional framing.

**Recommended Fixes**:
1. **Extract Mechanical Systems Integration** to `/aidm/guides/combat_progression_integration.md` (Tier 3). Leave 200-token summary in Module 08: "Combat XP calculation reads session_state.mechanical_systems.progression. Five types exist (mastery_tiers, class_based, quirk_awakening, milestone_based, static_op), each with unique XP formulas and advancement triggers. See Combat Progression Integration Guide for implementation details."

2. **Condense Tier Language** from 2,000 → 500 tokens: "Combat narration matches power_tier to prevent scaling mismatches. Use tier-appropriate verbs (T11-9: strikes/dodges, T8-7: demolishes/craters, T6-5: sunders/warps, T4-3: unravels/erases, T2-1: authors/negates). Apply context modifiers (environmental ×0.1-0.5, secret ID ×0.1-0.3). See Module 12 for complete tier framework."

3. **Streamline Pre-Combat Validation** from 2,500 → 1,750 tokens by removing instructional repetition ("BEFORE generating ANY", "ALWAYS validate", "DO NOT proceed" appears 8 times).

**Post-Optimization Estimate**: 11,500 → 6,500 tokens (still 117% over, but acceptable given combat complexity)

**Severity**: ❌ **CRITICAL** - 267-317% overrun blocks lazy loading, makes Module 08 unloadable in Tier 1.

---

### Issue 2: Human-Centric Instructional Language (MODERATE - Architectural)

**Problem**: Module 08 uses human-centric instructional tone ("BEFORE generating ANY combat narrative, ALWAYS validate:", "DO NOT proceed to calculation", "CHECK character_schema.resources") rather than AI-directive operational language. Same architectural misalignment identified in Module 07.

**System Reality**: AIDM v2 executor is **high-end agentic AI** (Claude Sonnet 4.5, GPT-4) with tool access:
- File operations (create_file, replace_string_in_file)
- Code execution (run_in_terminal)
- Web search (fetch_webpage)
- Schema validation (programmatic)

Instructions should be **operational protocols** for AI execution, not educational guidance for human users.

**Examples of Human-Centric Language**:

**Example 1: Pre-Combat Validation Header**
```markdown
❌ CURRENT (Human-centric):
"BEFORE generating ANY combat narrative, ALWAYS validate:"

✅ AI-DIRECTIVE:
"Pre-combat validation protocol (mandatory): Execute steps 1-5 sequentially. Block narrative generation until all validations pass."
```

**Example 2: Resource Validation**
```markdown
❌ CURRENT (Human-centric):
"CHECK character_schema.resources:
- MP available ≥ skill MP cost?
- SP available ≥ skill SP cost?
- HP > 0? (cannot act if incapacitated)
- Item exists in inventory? (if using item)

IF insufficient resources:
  - HALT combat action
  - Notify player: 'Insufficient [resource]: need X, have Y'
  - Suggest alternatives (lower-cost skill, basic attack, item use)
  - DO NOT proceed to calculation or narrative"

✅ AI-DIRECTIVE:
"Resource validation:
```python
resources = character_schema.resources
action_cost = skill.cost

validation = {
    'mp_sufficient': resources.mp.current >= action_cost.mp,
    'sp_sufficient': resources.sp.current >= action_cost.sp,
    'hp_positive': resources.hp.current > 0,
    'item_available': action.item_id in inventory.items if action.type == 'item' else True
}

if not all(validation.values()):
    halt_action()
    output_message(f"Insufficient {failed_resource}: need {required}, have {current}")
    generate_alternatives([lower_cost_skills, basic_attack, available_items])
    return VALIDATION_FAILED
```

Proceed to calculation only if return code = VALIDATION_PASSED."
```

**Example 3: Prerequisite Validation**
```markdown
❌ CURRENT (Human-centric):
"CHECK action prerequisites:
- Skill unlocked? (in character_schema.skills.learned)
- Cooldown expired? (check skill.last_used + cooldown < current_time)
- Target valid? (alive, in range, targetable)
- Status effects blocking? (paralyzed, stunned, silenced)
- Action economy available? (hasn't used action this turn)

IF prerequisites fail:
  - HALT combat action
  - Notify player of blocking condition
  - DO NOT proceed to calculation"

✅ AI-DIRECTIVE:
"Prerequisite validation protocol:
```python
prerequisites = {
    'skill_unlocked': skill.id in character_schema.skills.learned,
    'cooldown_ready': (current_time - skill.last_used) >= skill.cooldown,
    'target_valid': target.hp.current > 0 and distance(character, target) <= skill.range,
    'not_blocked': not any(effect.blocks_action for effect in character.status_effects),
    'action_available': character.combat_state.actions_remaining > 0
}

failed_checks = [k for k, v in prerequisites.items() if not v]

if failed_checks:
    halt_action()
    output_blocking_condition(failed_checks[0])
    return PREREQUISITE_FAILED
```

Proceed to calculation only if return code = PREREQUISITE_PASSED."
```

**Example 4: State Update Protocol**
```markdown
❌ CURRENT (Human-centric):
"UPDATE schemas using Change Log format:

1. Create Change Log entry for each modification:
   - operation: Type of change (subtract, add, set, append, etc.)
   - before: Current value (for validation)
   - after: New value (post-operation)
   - delta: Change amount (for numeric ops)
   - reason: Why changed (audit trail)
   - validated: Pre-commit hooks passed"

✅ AI-DIRECTIVE:
"State update protocol (Change Log format):
```python
def update_combat_state(changes):
    change_log = []
    
    for change in changes:
        entry = {
            'schema': change.target_schema,
            'path': change.field_path,
            'operation': change.op_type,  # subtract, add, set, append
            'before': get_current_value(change.target_schema, change.field_path),
            'after': calculate_new_value(change.before, change.delta, change.op_type),
            'delta': change.delta,
            'reason': change.audit_reason,
            'validated': run_precommit_hooks(change)
        }
        change_log.append(entry)
    
    if all(entry['validated'] for entry in change_log):
        apply_changes_atomic(change_log)
        return SUCCESS
    else:
        rollback_all(change_log)
        return VALIDATION_FAILED
```

Execute atomically: all changes succeed together OR rollback together."
```

**Impact**:
- **Architectural Clarity**: Removes ambiguity about AIDM's target executor (AI agent, not human)
- **Actionability**: Procedural code > instructional prose = easier programmatic interpretation
- **Token Efficiency**: Code blocks are denser than verbose warnings
- **Consistency**: Matches operational tone needed for agentic AI with tools

**Severity**: **MODERATE** (same as Module 07) - Affects system architecture clarity, but doesn't break functionality. Rephrasing is token-neutral or slightly beneficial.

**System-Wide Note**: This issue affects **ALL instruction modules** (identified in Modules 07 and 08 so far). Entire AIDM system should be audited for human-centric vs. AI-directive language after completing module reviews.

---

### Issue 3: Massive Content Duplication with Module 09 (CRITICAL)

**Problem**: Mechanical Systems Integration section (3,000 tokens) exhaustively explains 5 progression types that Module 09 (Progression Systems) will also explain.

**Duplication Analysis**:

**Module 08 Content**:
- mastery_tiers: Concept, XP calculation, tier advancement, tier bonuses, example (Hunter x Hunter)
- class_based: Concept, XP calculation, class advancement, example (My Hero Academia)
- quirk_awakening: Concept, XP calculation, awakening triggers, example (Todoroki awakening)
- milestone_based: Concept, XP calculation, story-driven power, example (milestone-based system)
- static_op: Concept, no XP, example (Saitama)

**Module 09 Content** (anticipated):
- Same 5 progression types
- Same XP formulas
- Same advancement rules
- Same examples

**Why This Is Critical**:
1. **Token Waste**: 3,000 tokens × 2 modules = 6,000 tokens explaining same concepts
2. **Maintenance Burden**: Changes to progression types require updating TWO modules
3. **Inconsistency Risk**: If Module 08 and Module 09 diverge, which is authoritative?
4. **Lazy Loading Failure**: Tier 1 budget violation forces combat module into Tier 2/3

**Correct Architecture**:
- **Module 09** (Progression Systems): Authoritative source for all 5 progression types, advancement rules, XP formulas, examples
- **Module 08** (Combat Resolution): Applies progression rules during combat, references Module 09 for type-specific logic

**Recommended Fix**:
Extract Mechanical Systems Integration (3,000 tokens) to:
1. `/aidm/guides/combat_progression_integration.md` (Tier 3 reference guide)
2. OR condense to 200-token summary in Module 08 referencing Module 09

**Condensed Version** (200 tokens):
```markdown
## Mechanical Systems Integration (Phase 4)

**Purpose**: Apply progression system from Session Zero Phase 3 to combat XP calculation.

**Protocol**: 
1. Read `session_state.mechanical_systems.progression` to determine type
2. Apply type-specific XP formula:
   - **mastery_tiers**: Standard XP + technique bonus, check tier threshold
   - **class_based**: Standard XP + class feature bonus, check level threshold
   - **quirk_awakening**: Standard XP + quirk usage bonus, monitor awakening triggers
   - **milestone_based**: Reduced XP (10% multiplier), major XP from story milestones
   - **static_op**: Zero XP (no mechanical progression)

**See Module 09 (Progression Systems) for complete type definitions, advancement rules, and examples.**

**Integration Validation**: Check session_state.mechanical_systems exists at combat start. Error if missing (Session Zero Phase 3 incomplete).
```

**Token Savings**: 3,000 → 200 = **2,800 tokens saved**

**Severity**: ❌ **CRITICAL** - Duplication wastes 3K tokens, creates maintenance burden, violates DRY principle.

---

## Moderate Issues

### Issue 4: Tier Language Duplication with Module 12 (MODERATE)

**Problem**: Tier-Appropriate Combat Narration section (2,000 tokens) duplicates Module 12 (Narrative Scaling) content. Module 12 already defines power tier verb sets, scale descriptions, and context modifiers.

**Current Module 08 Content**:
- 11 power tiers (T11-T1) with verb sets
- Scale descriptions (personal → continental → cosmic → conceptual)
- Consequences by tier (injuries → extinction events → reality warping → concept erasure)
- Tier mismatch prevention examples
- Context application (environmental, secret ID modifiers)

**Module 12 Content** (from earlier review):
- Same 11 power tiers
- Same verb sets and scale descriptions
- Context modifiers framework
- Power imbalance detection

**Why Module 08 Needs Tier Language**:
Combat narration must match power tier to prevent scaling errors ("Tier 9 shattering mountains" is impossible). Module 08 needs to apply tier rules, but doesn't need to re-teach them.

**Recommended Fix**:
Condense from 2,000 → 500 tokens by referencing Module 12:

```markdown
## Tier-Appropriate Combat Narration

**Purpose**: Combat language MUST match character.power_tier to maintain narrative consistency.

**Protocol**: 
1. Query character.power_tier and context_modifiers from Module 12
2. Calculate effective tier for combat (base tier × context modifiers)
3. Select verb set and scale appropriate to effective tier
4. Generate combat narration using tier-matched language

**Tier Language Quick Reference**:
- **T11-9** (Below Average → Superhuman): Personal-scale verbs (strikes, dodges, bleeds), injuries/exhaustion
- **T8-7** (Wall → Building): Structural-scale verbs (demolishes, craters), collateral damage
- **T6-5** (Mountain → Substellar): Geographic-scale verbs (sunders, warps), continental impacts
- **T4-3** (Stellar → Cosmic): Reality-scale verbs (unravels, erases), causality breaks
- **T2-1** (Multiversal → Higher Dimensional): Conceptual-scale verbs (authors, negates), ontological shifts

**Tier Mismatch Prevention**:
- ❌ T9 character "shattering mountains" (mountains = T7-6 scale)
- ❌ T5 character "struggling with thugs" (planetary being vs T10 threats)
- ❌ T2 character "destroys city" (multiversal god = "conceptually removes city from existence")

**See Module 12 (Narrative Scaling) for complete tier framework, verb sets, scale definitions, and context modifier calculations.**
```

**Token Savings**: 2,000 → 500 = **1,500 tokens saved**

**Severity**: ⚠️ **MODERATE** - Duplication wastes tokens but doesn't break functionality. Quick reference useful for combat-specific context.

---

### Issue 5: Missing Explicit Dice Resolution Integration (MINOR)

**Problem**: Module 08 uses dice notation throughout ("1d20 = 15", "1d8 = 6") but never explicitly references Module 11 (Dice Resolution) for notation standards.

**Current State**:
- Module 08 shows examples: "1d20 + 5 (STR) = 20 vs AC 18"
- No mention of Module 11's explicit dice protocol
- Assumes standard dice notation without defining it

**Potential Issues**:
- If Module 11 specifies notation format (e.g., "ALWAYS show roll separately: [1d20 = 15] + 5 = 20"), Module 08 examples might conflict
- No cross-reference for advantage/disadvantage, critical rules

**Recommended Fix**:
Add integration note in Combat Narration section:

```markdown
**Dice Notation**: All combat rolls follow Module 11 (Dice Resolution) explicit dice protocol:
- Show roll result explicitly: "[1d20 = 15]"
- Apply modifiers with source: "+5 (STR 20 → +5 mod)"
- Show final calculation: "15 + 5 = 20 vs AC 18 (HIT)"
- Critical hits (nat 20) and failures (nat 1) apply Module 11 critical rules
- Advantage/Disadvantage: Roll twice, take higher/lower per Module 11
```

**Token Cost**: +100 tokens (acceptable, improves consistency)

**Severity**: ⚠️ **MINOR** - Low impact, but cross-module reference improves system coherence.

---

## Strengths

### Strength 1: Bulletproof Pre-Combat Validation Protocol ⭐⭐⭐

**Why Excellent**:
The 5-step validation (Resource → Prerequisite → Calculation → State → Narrative) is **systematic and enforceable**. Each step has clear pass/fail conditions, and failure halts progression.

**Example Excellence**:
```python
# Step 1: Resource Validation
CHECK character_schema.resources:
- MP available ≥ skill MP cost?
- SP available ≥ skill SP cost?
- HP > 0?

IF insufficient: HALT, notify player, suggest alternatives

# Step 2: Prerequisite Validation
CHECK action prerequisites:
- Skill unlocked?
- Cooldown expired?
- Target valid?
- Status effects blocking?

IF fail: HALT, notify blocking condition

# Steps 3-5 only execute after 1-2 pass
```

**Impact**:
- Prevents common GM errors (forgetting MP costs, ignoring cooldowns)
- Ensures fair combat (player can't exploit forgotten rules)
- Atomic state updates (all changes succeed together or rollback)

**Comparison**: Most TTRPG systems leave validation to GM memory. Module 08 makes it systematic.

---

### Strength 2: Narrative Profile Combat Integration ⭐⭐⭐

**Why Excellent**:
Module 08 correctly integrates `narrative_profile_schema.combat_narrative_style` to match anime vibe. Combat narration adapts to source material DNA.

**Example Excellence**:
```markdown
**DanDaDan Profile** (strategy:4, sakuga:ON, destruction:HIGH):
"Momo's psychic grip YANKS alien—SLAMS into wall! Concrete EXPLODES, dust cloud ERUPTS! 
Okarun BLURS through debris (too fast to track), claws TEAR through torso! 
Alien SHRIEKS, black blood spraying across shattered storefront!"

**Hunter x Hunter Profile** (strategy:9, sakuga:OFF, destruction:LOW):
"Gon feints left—enemy takes bait. Opening confirmed. Rock charged to 80%. 
Impact: solar plexus. Enemy's aura flickers (damage threshold exceeded). 
Stagger detected. Follow-up: Paper to finish."
```

**Parameters Applied**:
- strategy_vs_spectacle (0-10): Controls tactical depth vs visual chaos
- sakuga_moments (ON/OFF): Slow-motion epic beats vs mechanical focus
- named_attacks (ON/OFF): Shouted attack names vs natural descriptions
- environmental_destruction (HIGH/MODERATE/LOW): Collateral damage scale

**Impact**:
- Same mechanical outcome (45 damage, enemy staggers), drastically different narration
- Maintains source material feel across combat encounters
- Players experience combat matching their anime expectations

---

### Strength 3: Nuanced Death & Resurrection System ⭐⭐⭐

**Why Excellent**:
Downed ≠ Dead distinction prevents cheap death while maintaining stakes. Death saves create tension. Injury table adds long-term consequences. Resurrection tiers have meaningful costs.

**System Breakdown**:
1. **0 HP = Downed** (unconscious, not dead, enemies may ignore or finish)
2. **Death Saves** (1d20/turn): 3 success = stabilize, 3 fail = dead
3. **Injury Table** (if 2+ fails before stabilize): Temporary to permanent injuries
4. **Resurrection Tiers**: 
   - T1 Revivify (<1min): 300g, no penalty
   - T2 Raise Dead (<10d): 500g, -4 rolls for 4d
   - T3 Resurrection (<100yr): 1000g+1000XP, -4 rolls 1wk, max HP -10% permanent
   - T4 True Resurrection (any): 25k gold+5k XP, -4 rolls 2wk

**Example Excellence**:
```markdown
**0 HP**: "Vision BLURS, legs give out—COLLAPSE. Dark. [DOWNED - Begin Saves]"
  NOT "You die"

**Death Save Success**: "GASP—clinging [1✓, 0✗]"
**Death Save Fail**: "Darkness closes [0✓, 1✗]"
**Nat 20**: "Eyes SNAP—alive! [Stable 1HP]"
**3 Fails**: "Heart stops. Silent. [DEAD]"

**Resurrection**: "Light burns eyes. GASP—lungs scream. Alive... changed. 
  [Res sickness: -4 rolls 4d]"
```

**Impact**:
- Death has weight (resurrection costs resources + penalties)
- Tension maintained (death saves create uncertainty)
- Injuries add stakes (broken bones, permanent scars)
- Prevents trivial death-as-inconvenience

**Anime Variants**: Senzu beans (instant stable), Return by Death (auto-res), willpower (survive lethal @ 1HP 1/session), Aqua's resurrection (free but debt increases)

---

### Strength 4: Boss Battle & Tournament Frameworks ⭐⭐

**Why Good**:
Boss battles have phased structure (75%/50%/25% HP thresholds trigger new mechanics). Tournament framework supports arena arc narratives with seeding, fatigue, bracket tracking, and spectator reactions.

**Boss Phase Example**:
```markdown
Phase 1 (100-75%): Standard combat
Phase 2 Trigger (75%): Reinforcements arrive, boss gains abilities
Phase 3 Trigger (50%): Power-up transformation, desperate attacks
Victory: XP, loot, quest update
```

**Tournament Framework**:
- Structure: 4-64 participants (power of 2), single/double elim, rules
- Seeding: Known NPCs ranked, unknown via prelims, player by level+rep
- Fatigue: Immediate (<10min) = -2 rolls/-20% resources, Short (30min) = -1/-10%, Long (2hr+) = full recovery
- Bracket tracking: Track winners, skip minor matches, montage advancement
- Spectators: Crowd reactions (underdog support, upset shock), betting, quest hooks

**Impact**:
- Boss fights feel epic (phases create dramatic structure)
- Tournament arcs supported (Heaven's Arena from HxH possible)
- Fatigue adds strategy (rush vs rest between matches)

---

### Strength 5: Combat Maneuvers Complete ⭐

**Why Good**:
Grapple, Disarm, Called Shot, and Aid actions provide tactical variety beyond basic attacks.

**Maneuver Coverage**:
- **Grapple**: STR vs STR/DEX contest, success = grappled (speed 0, disadv attacks)
- **Disarm**: Attack at disadvantage vs AC, success = weapon flies 10ft
- **Called Shot**: -5 penalty, success = normal damage + effect (head/arm/leg/eyes/weak point)
- **Aid**: Use action, ally gains advantage on next roll

**Impact**:
- Tactical depth beyond "I attack"
- Enables strategy (grapple spellcaster to prevent casting, disarm weapon user, called shot weak point)

---

## Integration with Other Modules

### Strong Integrations ✅

**Module 03 (State Manager)**:
- Change Log format correctly applied for atomic HP/MP/SP/inventory updates
- Pre-commit validation ensures state consistency
- Rollback on failed validation

**Module 02 (Learning Engine)**:
- Combat generates COMBAT memory threads (referenced)
- High-stakes battles = high heat (prioritized recall)

**Module 05 (Narrative Systems)**:
- Victory/defeat narration matches narrative voice (95% narrator, 5% meta)
- Combat integrates into emergent storytelling

**Module 04 (NPC Intelligence)**:
- Enemy AI priority system uses disposition/affinity (indirectly)
- Ally reactions in combat reference NPC module

**Module 13 (Narrative Calibration)**:
- Narrative Profile combat_narrative_style parameters correctly applied
- Strategy vs spectacle, sakuga moments, named attacks all parameterized

### Weak Integrations ⚠️

**Module 09 (Progression Systems)**:
- ❌ Mechanical Systems Integration duplicates Module 09 content (3,000 tokens)
- Should reference Module 09, not re-explain progression types

**Module 12 (Narrative Scaling)**:
- ⚠️ Tier-Appropriate Language duplicates Module 12 verb sets (2,000 tokens)
- Should condense to reference, not re-teach

**Module 11 (Dice Resolution)**:
- ⚠️ No explicit reference to dice notation standards
- Should cross-reference Module 11 for notation format, advantage/disadvantage, criticals

### Missing Integrations ⚠️

**Module 10 (Error Recovery)**:
- No mention of error recovery during combat validation failures
- What if character_schema is corrupted during combat?
- Should reference Module 10 for graceful failure protocols

**Module 06 (Session Zero)**:
- No mention of combat tutorials during Session Zero Phase 4 (first session)
- Should reference Session Zero for introducing combat to new players

---

## Schema Validation

### Schemas Referenced ✅

**character_schema.json**:
- `.resources.mp.current` (MP cost validation)
- `.resources.sp.current` (SP cost validation)
- `.resources.hp.current` (HP damage tracking)
- `.skills.learned` (skill unlock validation)
- `.status_effects` (status tracking)
- `.combat_state.actions_remaining` (action economy)
- `.power_tier` (tier-appropriate narration)
- `.progression.mastery_tier` (for mastery_tiers type)
- `.progression.current_xp` (XP tracking)

**narrative_profile_schema.json**:
- `.combat_narrative_style.strategy_vs_spectacle` (0-10)
- `.combat_narrative_style.power_explanations` (ON/OFF)
- `.combat_narrative_style.sakuga_moments` (ON/OFF)
- `.combat_narrative_style.named_attacks` (ON/OFF)
- `.combat_narrative_style.environmental_destruction` (HIGH/MODERATE/LOW)

**npc_schema.json**:
- `.resources.hp.current` (enemy HP tracking)
- `.combat_ai.priority` (enemy AI decisions)

**session_state.json** (implied):
- `.mechanical_systems.progression` (progression type, advancement rules)
- `.combat_state.turn_order` (initiative tracking)
- `.combat_state.active_effects` (status effects)

**world_state.json** (implied):
- `.current_combat.participants` (combatants)
- `.current_combat.round_number` (turn tracking)

### Schema Issues ⚠️

**Missing Explicit Schema References**:
- `skill.cost` structure not defined (MP/SP/HP costs)
- `skill.cooldown` structure not defined (last_used timestamp)
- `status_effects` array structure not defined (effect type, duration, magnitude)
- `combat_state` structure not explicitly referenced

**Recommendation**: Define combat-specific schema structures or reference existing schema documentation.

---

## Token Efficiency Analysis

### Current Token Budget: ~11,000-12,500 tokens

**Target**: 3,000 tokens (Tier 1 always-loaded)  
**Actual**: 11,000-12,500 tokens  
**Overage**: **267-317% OVER** ❌

### Token Breakdown by Section

| Section | Tokens | Assessment | Optimization Potential |
|---------|--------|------------|------------------------|
| Purpose & Core Principle | 100 | ✅ Efficient | None |
| Pre-Combat Validation | 2,500 | ⚠️ Verbose | -750 tokens (30% reduction via instructional removal) |
| Combat Types & Actions | 1,500 | ✅ Acceptable | -200 tokens (10% condensation) |
| Damage/Status/Bosses | 1,500 | ✅ Acceptable | None |
| Narrative Profile Integration | 1,200 | ✅ Unique to M08 | None |
| Victory/Defeat Narration | 400 | ✅ Efficient | None |
| Death & Resurrection | 1,500 | ✅ Acceptable | None |
| Combat Maneuvers/Tournament | 800 | ✅ Acceptable | None |
| **Tier-Appropriate Language** | **2,000** | ❌ **DUPLICATE M12** | **-1,500 tokens (reference M12)** |
| **Mechanical Systems Integration** | **3,000** | ❌ **DUPLICATE M09** | **-2,800 tokens (extract to guide)** |

### Optimization Recommendations

**Priority 1 (CRITICAL)**: Extract Mechanical Systems Integration
- Current: 3,000 tokens (5 progression types × exhaustive examples)
- Target: 200 tokens (summary + reference to Module 09)
- Savings: **-2,800 tokens**
- Action: Create `/aidm/guides/combat_progression_integration.md` (Tier 3)

**Priority 2 (HIGH)**: Condense Tier-Appropriate Language
- Current: 2,000 tokens (11 tiers × examples)
- Target: 500 tokens (quick reference + Module 12 reference)
- Savings: **-1,500 tokens**
- Action: Replace exhaustive tier explanations with quick reference table

**Priority 3 (MODERATE)**: Streamline Pre-Combat Validation
- Current: 2,500 tokens (overly verbose with repeated warnings)
- Target: 1,750 tokens (remove instructional framing)
- Savings: **-750 tokens**
- Action: Replace human-centric warnings with AI-directive protocols

**Total Potential Savings**: -5,050 tokens  
**Post-Optimization Estimate**: 11,500 → 6,450 tokens (115% over target, but acceptable for core combat module)

### Tier Classification Recommendation

**Current Tier**: Tier 1 (always-loaded)  
**Recommended Tier**: **Tier 1** (keep as core, but optimize to ~6,500 tokens)

**Justification**: Combat is core JRPG functionality, needs immediate access. However, must optimize to prevent context overflow. Extracting progression integration and condensing tier language brings module within acceptable range for complex combat system.

---

## Actionability Assessment

### Protocols: Highly Actionable ✅

**5-Step Pre-Combat Validation**: Clear pass/fail conditions, explicit halt points, systematic execution order. AI can implement programmatically.

**Change Log State Updates**: Precise format (operation, before, after, delta, reason, validated). Atomic execution defined. AI can generate Change Log entries directly.

**Narrative Profile Integration**: Explicit parameters (strategy_vs_spectacle 0-10, sakuga ON/OFF). AI can query schema and match narration style.

**Death Saves**: Unambiguous rules (1d20, 10+ success, 1-9 fail, nat 20/1 special). AI can execute mechanically.

### Ambiguities: Minor ⚠️

**Enemy AI Priority System**:
- "Attack weakest (low HP, vulnerable)" - What if multiple enemies equally weak?
- "Attack highest threat" - How is threat quantified? (Damage output? Healing? Control?)
- "Defend (HP <25%)" - Does this override all other priorities?

**Recommendation**: Define tie-breaking rules and threat calculation formula.

**Narrative Combat**:
- "When drama trumps mechanics" - When exactly? Who decides?
- "Use when: Boss flees at plot HP" - What's plot HP? Arbitrary DM decision?

**Recommendation**: Provide guidelines for when to use narrative combat vs standard combat.

### Examples: Excellent ✅

Every major concept includes concrete examples:
- Pre-Combat Validation: Complete JSON flow example
- Narrative Profile: DanDaDan vs Hunter x Hunter narration
- Death Saves: Exact narration for success/fail/nat20/nat1
- Boss Phases: 3-phase structure with triggers
- Tournament: Heaven's Arena example (HxH)

---

## Test Coverage Recommendations

### Critical Tests Needed

**Test 1: Pre-Combat Validation Enforcement**
- **Scenario**: Player attempts skill with insufficient MP
- **Expected**: Action halted, insufficient resource notification, alternatives suggested
- **Validates**: Resource validation step 1, halt protocol

**Test 2: Atomic State Updates**
- **Scenario**: Combat action requires 3 state changes (MP deduction, HP damage, status effect), 3rd change fails validation
- **Expected**: All 3 changes rollback, state returns to pre-action
- **Validates**: Change Log atomic execution

**Test 3: Narrative Profile Combat Narration**
- **Scenario**: Same mechanical combat (attack hits for 45 damage) with 3 different profiles (DanDaDan high spectacle, HxH high strategy, AoT moderate)
- **Expected**: 3 drastically different narrations matching profile parameters
- **Validates**: Narrative Profile integration, combat_narrative_style application

**Test 4: Death Save System**
- **Scenario**: Character at 0 HP, rolls death saves (success, fail, nat 20, nat 1)
- **Expected**: Correct tracking (3 success = stable, 3 fail = dead, nat 20 = instant stable, nat 1 = 2 fails)
- **Validates**: Death save mechanics, injury table (if 2+ fails)

**Test 5: Tier-Appropriate Language Enforcement**
- **Scenario**: T9 character (superhuman) attempts to "shatter mountain"
- **Expected**: Tier mismatch error, narration constrained to T9 scale (personal/room-scale)
- **Validates**: Tier language protocol, mismatch prevention

**Test 6: Progression Type XP Calculation**
- **Scenario**: Combat victory with 5 different progression types (mastery_tiers, class_based, quirk_awakening, milestone_based, static_op)
- **Expected**: 5 different XP awards (standard, standard+class bonus, standard+quirk bonus, 10% of standard, 0)
- **Validates**: Mechanical Systems Integration, type-specific XP formulas

### Edge Cases

**Edge Case 1**: Character downed by massive damage (≥ max HP in single hit) → Should be instant death, not death saves

**Edge Case 2**: Resurrection with missing body parts (arm severed) → Raise Dead requires "mostly intact", should fail or restore arm?

**Edge Case 3**: Status effect expires mid-turn (paralysis duration = 1 turn, character acts on turn 2) → When exactly does effect expire?

**Edge Case 4**: Simultaneous death (both combatants drop to 0 HP from same attack, e.g., Fire Shield damage reflection) → Who dies first? Draw?

---

## Final Assessment

### Issues Summary

**Critical Issues** (Must Fix):
1. **Token Budget Catastrophic Failure** (11K-12.5K tokens, 267-317% over) - Extract Mechanical Systems Integration (3K), condense Tier Language (1.5K), streamline Pre-Combat Validation (750)
2. **Massive Content Duplication with Module 09** (3K tokens) - Extract to guide or reference Module 09
3. **Human-Centric Language Throughout** (architectural misalignment) - Rephrase to AI-directive operational protocols

**Moderate Issues** (Should Fix):
1. **Tier Language Duplication with Module 12** (2K tokens) - Condense to reference Module 12
2. **Missing Dice Resolution Integration** - Add explicit Module 11 reference

**Minor Issues** (Nice to Fix):
1. Enemy AI priority tie-breaking rules undefined
2. Narrative combat trigger conditions vague

### Strengths Summary

1. ⭐⭐⭐ Pre-Combat Validation Protocol (5 systematic steps, bulletproof)
2. ⭐⭐⭐ Narrative Profile Combat Integration (matches anime DNA perfectly)
3. ⭐⭐⭐ Death & Resurrection System (nuanced, prevents cheap death)
4. ⭐⭐ Boss Battle & Tournament Frameworks (supports story arcs)
5. ⭐ Combat Maneuvers (tactical depth)

### Recommendations

**Priority 1 (CRITICAL - Token Optimization)**:
1. **Extract Mechanical Systems Integration** to `/aidm/guides/combat_progression_integration.md` (Tier 3 reference). Replace with 200-token summary referencing Module 09. **Saves 2,800 tokens.**
2. **Condense Tier-Appropriate Language** from 2,000 → 500 tokens. Create quick reference table, reference Module 12 for complete framework. **Saves 1,500 tokens.**
3. **Streamline Pre-Combat Validation** from 2,500 → 1,750 tokens. Remove instructional repetition ("BEFORE generating ANY", "ALWAYS", "DO NOT" appears 8 times). **Saves 750 tokens.**

**Post-Optimization Target**: 6,450 tokens (115% over, acceptable for combat complexity)

**Priority 1 (CRITICAL - Architecture Alignment)**:
4. **Rephrase Human-Centric Language to AI-Directive Format**. Replace instructional warnings ("ALWAYS validate", "DO NOT proceed") with operational protocols (validation_protocol(), halt_action(), return VALIDATION_FAILED). Provide procedural code blocks instead of prose warnings. **Token-neutral or slight savings, major architectural clarity improvement.**

**System-Wide Note**: The human-centric language issue affects **ALL instruction modules** (identified in Modules 07 and 08 so far). After completing remaining module audits (09-13 + CORE), perform system-wide audit for language rephrasing.

**Priority 2 (HIGH - Integration)**:
5. Add explicit Module 11 (Dice Resolution) reference for notation standards, advantage/disadvantage, critical rules. **+100 tokens, improves consistency.**
6. Add Module 10 (Error Recovery) reference for combat validation failure handling. **+50 tokens, improves robustness.**

**Priority 3 (LOW - Clarification)**:
7. Define Enemy AI priority tie-breaking rules (if multiple enemies equally weak, target closest/most damaged/random)
8. Clarify Narrative Combat trigger conditions (when to use vs standard combat)

### Approval Conditions

Module 08 approved for use AFTER:
1. ✅ Mechanical Systems Integration extracted to guide OR condensed to 200-token summary (Priority 1, Recommendation 1)
2. ✅ Tier-Appropriate Language condensed to 500-token quick reference (Priority 1, Recommendation 2)
3. ✅ Pre-Combat Validation streamlined to 1,750 tokens (Priority 1, Recommendation 3)
4. ✅ Human-centric language rephrased to AI-directive format (Priority 1, Recommendation 4)

**Post-revision token estimate**: ~6,450 tokens (115% over, acceptable)

**APPROVAL STATUS**: ❌ **NEEDS REVISION** (CRITICAL token overruns + architectural issues require fixes before deployment)

---

## Audit Metadata

**Audit Completed**: November 24, 2025  
**Module Version Audited**: 2.0  
**Audit Framework**: AUDIT_CHECKLIST.md (7 general categories + Module 08 specific targets)  
**Review Template**: Standard (Executive Summary, Structure, Issues, Strengths, Integration, Schema, Token Efficiency, Actionability, Tests, Recommendations, Approval)  
**Previous Module**: Module 07 (Anime Integration) - APPROVED WITH MODERATE RECOMMENDATIONS  
**Next Module**: Module 09 (Progression Systems)  
**Audit Progress**: 8 of 15 modules complete (53.3%)

---

**End of Module 08 Review**
