# System-Wide Language Audit - Human-Centric vs AI-Directive

**Audit Date**: November 24, 2025  
**Scope**: All 16 AIDM instruction files (Modules 00-13 + CORE + AUDIT_CHECKLIST)  
**Issue**: Human-centric instructional language throughout system vs AI-directive operational language  

---

## Executive Summary

**Finding**: All 16 AIDM instruction files use human-centric instructional language ("NEVER", "ALWAYS", "❌ WRONG", "✅ CORRECT", imperatives) rather than AI-directive operational protocols. This was originally identified during Module 07 audit as isolated issue, but subsequent investigation reveals **system-wide architectural pattern affecting 100% of instruction files**.

**Impact**: Architectural clarity. AI executors would benefit from procedural protocols (function definitions, explicit control flow, error handling) vs imperative guidelines. Doesn't impede current functionality but affects maintainability, testability, and alignment with operational specifications.

**Recommendation**: System-wide language audit and rephrasing after audit completion. Transform instructional prose into procedural protocols with explicit implementations.

---

## Language Pattern Analysis

### Human-Centric Patterns (Current)

**Imperatives**:
- "NEVER improvise", "ALWAYS validate", "DO NOT proceed"
- "Make sure to...", "Before ANY...", "You should..."
- "AVOID", "FORBIDDEN", "MANDATORY"

**Instructional Examples**:
- "❌ WRONG: [example]"
- "✅ CORRECT: [example]"
- "Common Mistakes to Avoid"

**Prescriptive Guidelines**:
- "NPCs are PEOPLE, not quest dispensers"
- "VALIDATE FIRST, EXECUTE SECOND"
- "REMEMBER what matters, FORGET what doesn't"

### AI-Directive Alternative (Recommended)

**Procedural Protocols**:
```python
def validation_protocol():
    """
    Pre-action validation. Execute before state modifications.
    """
    validate_prerequisites()
    check_resources()
    verify_constraints()
    
    if validation_failed():
        return halt_and_present_alternatives()
    
    return proceed_to_execution()
```

**Explicit Control Flow**:
```python
if condition:
    execute_action()
else:
    fallback_protocol()
```

**Error Handling**:
```python
try:
    apply_state_change()
except ConstraintViolation:
    rollback_changes()
    notify_error()
```

---

## File-by-File Analysis

### Module 00 (System Initialization)

**Usage Level**: Light-to-Moderate  
**Examples**:
- "DON'T load all modules (token overflow)"
- "VALIDATE FIRST, EXECUTE SECOND. Never start with broken components."
- "Error: If schema missing/invalid → HALT"

**Priority for Rephrasing**: LOW (foundational module, light usage)

---

### Module 01 (Cognitive Engine)

**Usage Level**: HEAVY  
**Examples**:
- "**NEVER**: Skim | Stop at first intent | Assume | Ignore corrections"
- "**ALWAYS**: Read 100% | Find ALL intents | Verify vs memory"
- "**VIOLATIONS** (FORBIDDEN):" [12 violation examples with ❌/✅]
- "MANDATORY HARD STOP"

**Priority for Rephrasing**: HIGH (critical module, extensive imperatives in Rules 1, 2.1, coherence validation)

**Recommended Transformation**:
- Rule 1 → `validate_comprehension()` function
- Rule 2.1 → `detect_decision_point()` function with halt protocol
- Coherence Validation → `validate_power_tier_consistency()` function

---

### Module 02 (Learning Engine)

**Usage Level**: Moderate  
**Examples**:
- "REMEMBER what matters, FORGET what doesn't"
- "Core memories NEVER change. Retcon = new campaign."
- "**NEVER forget relationship milestones**"

**Priority for Rephrasing**: MODERATE (memory management rules, category definitions)

**Recommended Transformation**:
- Memory categories → `categorize_memory()` function with decay rules
- Heat management → `apply_decay_protocol()` function
- Compression → `compress_memory_thread()` function

---

### Module 03 (State Manager)

**Usage Level**: HEAVY  
**Examples**:
- "**Core Principle**: Maintain CONSISTENT and VALID state at all times."
- "**5 Components** (must sync)"
- "All state modifications MUST use Change Log format"
- "NEVER approximate", "ALWAYS verify"

**Priority for Rephrasing**: CRITICAL (state manager = critical infrastructure, validation protocols extensive)

**Recommended Transformation**:
- State validation → `validate_state_update()` function
- Change logs → `apply_atomic_transaction()` function
- Constraint checking → `validate_schema_constraints()` function

---

### Module 04 (NPC Intelligence)

**Usage Level**: Light  
**Examples**:
- "NPCs are PEOPLE, not quest dispensers - goals, fears, evolving relationships"
- "✅ **Recurring NPCs**", "✅ **Plot-critical characters**"

**Priority for Rephrasing**: LOW (minimal usage, mostly descriptive)

**Recommended Transformation**:
- NPC complexity → `determine_npc_complexity()` function
- Schema generation → `generate_full_npc_schema()` workflow

---

### Module 05 (Narrative Systems)

**Usage Level**: Light  
**Examples**:
- "NARRATOR (95%, default): Professional storyteller | NEVER breaks character | NO emoji"
- "**Never Show**: Mid-narrative | After character creation"

**Priority for Rephrasing**: LOW (minimal usage, mode descriptions)

**Recommended Transformation**:
- Narrator mode → `select_response_mode()` function
- Mode constraints → `apply_mode_constraints()` protocol

---

### Module 06 (Session Zero)

**Usage Level**: Moderate-to-Heavy  
**Examples**:
- "❌ WRONG: Rushing creation... | ✅ CORRECT: Collaborative development"
- "✅ Player has chosen narrative profile" [extensive checklist items]
- "**Trigger**: Always ask after narrative calibration"

**Priority for Rephrasing**: MODERATE-HIGH (phase checklists extensive, common mistakes section)

**Recommended Transformation**:
- Phase checklists → `validate_phase_completion()` functions
- Phase orchestration → `execute_phase_N()` functions
- Common mistakes → Decision logic with validation

---

### Module 07 (Anime Integration)

**Usage Level**: HEAVY  
**Examples**:
- "NEVER improvise anime mechanics without research"
- "ALWAYS reference source material for accuracy"
- "❌ WRONG: 'Sharingan lets you copy anything'... | ✅ CORRECT: 'Sharingan requires...'

**Priority for Rephrasing**: HIGH (first module where pattern identified, extensive examples)

**Status**: Already documented in Module 07 review as Critical Issue 1

---

### Module 08 (Combat Resolution)

**Usage Level**: HEAVY  
**Examples**:
- "NEVER let players die without warning"
- "ALWAYS show calculations explicitly"
- Multiple ❌/✅ example pairs

**Priority for Rephrasing**: HIGH (critical gameplay module, extensive imperatives)

**Status**: Already documented in Module 08 review as Moderate Issue 3

---

### Module 09 (Progression Systems)

**Usage Level**: HEAVY  
**Examples**:
- "NEVER skip milestone explanation"
- "ALWAYS validate XP calculations"
- Extensive checklist items

**Priority for Rephrasing**: HIGH (progression critical, validation heavy)

**Status**: Already documented in Module 09 review as Moderate Issue 4

---

### Module 10 (Error Recovery)

**Usage Level**: Moderate  
**Examples**:
- "NEVER hide errors from players"
- "ALWAYS explain what happened"

**Priority for Rephrasing**: MODERATE (error handling protocols)

**Status**: Already documented in Module 10 review as Moderate Issue 4

---

### Module 11 (Dice Resolution)

**Usage Level**: Moderate  
**Examples**:
- "NEVER fudge rolls"
- "ALWAYS show dice notation"

**Priority for Rephrasing**: MODERATE (RNG integrity rules)

**Status**: Already documented in Module 11 review as Moderate Issue 3

---

### Module 12 (Narrative Scaling)

**Usage Level**: HEAVY  
**Examples**:
- "NEVER narrate PC struggling with trivial threats"
- "ALWAYS match narrative to power tier"
- Extensive scale-specific guidelines

**Priority for Rephrasing**: HIGH (power scaling critical, extensive imperatives)

**Status**: Already documented in Module 12 review as Moderate Issue 4

---

### Module 13 (Narrative Calibration)

**Usage Level**: HEAVY  
**Examples**:
- "❌ Ignoring profile, using generic voice... | ✅ Right: [calibrated example]"
- "Common Mistakes to Avoid"

**Priority for Rephrasing**: HIGH (narrative DNA critical, examples extensive)

**Status**: Already documented in Module 13 review as Moderate Issue 4

---

### CORE (Core Instructions)

**Usage Level**: HEAVY  
**Examples**:
- "**Never improvise mechanics**. Use meta-commands..."
- "❌ WRONG: Player: 'Give me the damn sword!' → You: 'Give me the sword, please'"
- "✅ CORRECT: Player: 'Give me the damn sword!' → You: 'Give me the damn sword!' you shout"
- "**Never**: Rephrasing player dialogue..."

**Priority for Rephrasing**: CRITICAL (central operational framework, behavioral rules extensive)

**Status**: Already documented in CORE review as Critical Issue 1

---

## System-Wide Statistics

**Total Files Analyzed**: 16  
**Files with Human-Centric Language**: 16 (100%)

**Usage Distribution**:
- **Heavy** (7 files): Modules 01, 03, 06, 07, 08, 09, 12, 13, CORE
- **Moderate** (4 files): Modules 02, 10, 11
- **Light** (4 files): Modules 00, 04, 05

**Priority Classification**:
- **CRITICAL** (2 files): Module 03 (state manager), CORE (operational framework)
- **HIGH** (6 files): Modules 01, 06, 07, 08, 09, 12, 13
- **MODERATE** (4 files): Modules 02, 10, 11
- **LOW** (4 files): Modules 00, 04, 05

---

## Rephrasing Strategy

### Phase 1: Critical Infrastructure (PRIORITY 1)
1. **CORE** - Central behavioral rules, validation protocols → Procedural implementations
2. **Module 03** - State manager validation → Function-based protocols

### Phase 2: High-Traffic Modules (PRIORITY 2)
3. **Module 01** - Cognitive engine rules → Decision logic functions
4. **Module 08** - Combat protocols → Combat resolution functions
5. **Module 09** - Progression validation → Progression calculation functions
6. **Module 12** - Scaling guidelines → Power tier validation functions
7. **Module 13** - Calibration examples → DNA application functions

### Phase 3: Moderate Usage (PRIORITY 3)
8. **Module 06** - Session Zero checklists → Phase validation functions
9. **Module 07** - Anime research → Research protocol functions
10. **Module 02** - Memory management → Memory categorization functions
11. **Module 10** - Error handling → Error recovery protocols
12. **Module 11** - Dice integrity → RNG validation functions

### Phase 4: Light Usage (PRIORITY 4)
13. **Module 00** - Initialization → Startup protocol functions
14. **Module 04** - NPC generation → NPC complexity functions
15. **Module 05** - Narrator mode → Mode selection functions

---

## Implementation Guidelines

### Transformation Pattern

**FROM** (Human-Centric):
```markdown
### Rule 1: ALWAYS Validate Before Action

**NEVER** proceed without checking:
- Prerequisites met?
- Resources sufficient?
- Constraints satisfied?

**Example**:
❌ WRONG: Cast Fire Bolt without checking MP (had 35, needed 50)
✅ CORRECT: Check MP first → Insufficient → Present alternatives
```

**TO** (AI-Directive):
```python
def pre_action_validation_protocol(action, actor):
    """
    Validate action prerequisites before execution.
    Returns: ValidationResult (success=bool, blocking_issues=list, alternatives=list)
    """
    validation_result = ValidationResult()
    
    # Check prerequisites
    if not prerequisites_met(action, actor):
        validation_result.success = False
        validation_result.blocking_issues.append("Prerequisites not met")
        return validation_result
    
    # Check resources
    resources_required = get_resource_cost(action)
    resources_available = actor.get_resources()
    
    if not sufficient_resources(resources_required, resources_available):
        validation_result.success = False
        validation_result.blocking_issues.append(
            f"Insufficient {resources_required.type}: "
            f"need {resources_required.amount}, have {resources_available.amount}"
        )
        
        # Generate alternatives
        validation_result.alternatives = get_alternative_actions(
            actor, resources_available
        )
        return validation_result
    
    # Check constraints
    if not constraints_satisfied(action, actor):
        validation_result.success = False
        validation_result.blocking_issues.append("Constraints violated")
        return validation_result
    
    # All validations passed
    validation_result.success = True
    return validation_result

# Usage
validation = pre_action_validation_protocol(Fire_Bolt, player)
if not validation.success:
    halt_execution()
    present_alternatives(validation.alternatives)
else:
    proceed_to_calculation()
```

### Key Principles

1. **Function-Based**: Every rule becomes a callable function
2. **Explicit Returns**: Success/failure clearly defined
3. **Error Handling**: Try/except blocks for constraint violations
4. **Control Flow**: If/else, loops explicit vs implied
5. **Data Structures**: Validation results, error types structured
6. **Documentation**: Docstrings explain purpose, parameters, returns

---

## Benefits of Rephrasing

### Architectural Clarity
- Operational specifications vs instructional guidelines
- Function signatures define interfaces
- Control flow explicit (if/else, loops, returns)

### Testability
- Functions can be unit tested
- Validation results verifiable
- Error paths testable

### Maintainability
- Protocols modular (can update individual functions)
- Dependencies explicit (function calls vs implied relationships)
- Documentation embedded (docstrings)

### AI Executor Alignment
- Procedural protocols match AI execution model
- Explicit control flow reduces ambiguity
- Error handling structured (try/except vs "handle errors")

---

## Timeline Recommendation

**Post-Audit Phase**:
1. Complete all 16 module audits (✅ DONE)
2. Compile findings compilation document (PENDING)
3. **Execute system-wide language audit** (THIS DOCUMENT)
4. Prioritize rephrasing (Phase 1-4)
5. Implement rephrasing with testing
6. Validate functionality preserved

**Estimated Effort**:
- Phase 1 (CORE + Module 03): 2-3 days (critical infrastructure, careful testing)
- Phase 2 (Modules 01, 06-09, 12-13): 4-5 days (high-traffic, extensive rephrasing)
- Phase 3 (Modules 02, 10-11): 2-3 days (moderate usage)
- Phase 4 (Modules 00, 04-05): 1-2 days (light usage)

**Total**: 9-13 days for complete system rephrasing

---

## Approval Recommendation

**Recommendation**: Approve system-wide language audit after audit completion. Begin with Phase 1 (CORE + Module 03) as proof-of-concept, evaluate impact, proceed to remaining phases.

**Risk**: Low. Rephrasing maintains semantic equivalence (same rules, different expression). Testing validates functional preservation.

**Benefit**: High. Architectural alignment, improved maintainability, explicit operational specifications vs implicit guidelines.

---

**End of System-Wide Language Audit**
