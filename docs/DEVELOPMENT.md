# AIDM v2 Development Guidelines

## Working With AI Assistants on This Project

This document provides critical guidelines for collaborating with AI assistants (like GitHub Copilot, ChatGPT, Claude, etc.) when developing or modifying AIDM v2.

**What is AIDM v2?** See `README.md` for complete system overview.

---

## Core Principles

### 1. **Architecture Over Implementation**
The AIDM v2 system is INSTRUCTION-BASED, not code-based. Changes should focus on improving instructions, not building software.

### 2. **Modularity is Sacred**
Each instruction module must function independently. Never create dependencies that require all files to be loaded simultaneously.

### 3. **Player Agency First**
Any change that could diminish player control must be rejected. The AI assists; it doesn't decide.

### 3.5. **Genre-Authentic Storytelling** (NEW - January 2025)
AIDM must learn HOW anime tells stories (narrative DNA), not just mechanics. Module 13 (Narrative Calibration) extracts storytelling vibe via 10 scales (0-10), 15 trope switches (ON/OFF), and pacing/tone/dialogue/combat parameters. This prevents "D&D in anime skin" - same mechanics, different FEEL per source anime.

### 4. **Context Budget Management** (Critical)
Token efficiency is a first-class design constraint. AIDM operates in 200K context windows:
- **Current base system**: ~97,816 tokens (48.9% of budget) - 13 modules + 8 schemas + narrative DNA
- **Pre-optimization**: 142,192 tokens (instruction modules alone)
- **Actual reduction**: 62% base + narrative DNA system (~13,626 tokens for genre-authentic storytelling)
- **Alert threshold**: >100,000 tokens (50% of budget)

**Why this matters**: Every token saved in instruction files = more tokens available for gameplay (NPC memories, conversation history, world state, narrative depth).

**Mandatory approach**:
- Create content in optimized format from the start (don't write verbose then compress)
- Apply token optimization techniques during initial drafting
- Multi-pass refinement required (3+ iterations for all files)
- Validate 100% information parity before considering file complete

**Reference**: See `docs/TOKEN_OPTIMIZATION_METHODOLOGY.md` for complete guide and `OPTIMIZATION_CHECKLIST.md` for quick reference.

### 5. **Test Before You Ship**
All changes must pass the 8 acceptance tests in `/docs/SCOPE.md` before being considered complete.

---

## When Working With AI Assistants

### Session Boundaries

**Start of New Session**:
1. Provide context: "I'm working on AIDM v2, an instruction-set for LLMs to act as anime RPG dungeon masters"
2. Share relevant files: At minimum `README.md`, `ARCHITECTURE.md`, `SCOPE.md`
3. Explain your goal: "I need to [specific task]"
4. Reference constraints: "This must stay under 2000 words" or "This must work without external dependencies"

**During Session**:
- Keep AI focused on ONE module at a time
- Request explanations: "Why did you structure it this way?"
- Challenge assumptions: "Does this violate the modularity principle?"
- Test incrementally: "Let's validate this works before moving on"

**End of Session**:
- Document what was completed in `/docs/STATE.md`
- Note any breaking changes or dependencies introduced
- Create TODO items for incomplete work

### Always Provide AI With

When asking AI to modify or create AIDM files:

1. **Context**: What system/module you're working on
2. **Constraints**: Word limits, dependencies, scope boundaries
3. **References**: Point to `ARCHITECTURE.md` or `SCOPE.md` sections
4. **Success Criteria**: How you'll know it's correct
5. **Integration Points**: What other modules interact with this

### Never Ask AI To

1. **Build standalone applications** - AIDM is instruction files, not software
2. **Create dependencies on external services** - Everything must work within an LLM
3. **Implement features outside scope** - Check `/docs/SCOPE.md` first
4. **Break modularity** - Modules must work independently
5. **Compromise player agency** - AI assists, doesn't control

---

## Architecture Changes Require Approval

**Major Changes (Discuss Before Implementing)**:
- Adding new core systems (beyond 10 instruction modules)
- Changing module dependencies
- Modifying core schemas (character, world, NPC, memory)
- Adding external tool requirements
- Changing fundamental game mechanics

**Minor Changes (Implement Freely)**:
- Adding trope libraries
- Creating new templates
- Expanding documentation
- Bug fixes in existing modules
- Clarifying instructions

---

## File Modification Guidelines

### Instruction Files (`/instructions/*.md`)

**Structure Requirements**:
```markdown
# [Module Name]

## Purpose
[Single sentence describing what this module does]

## Core Responsibilities
[3-5 bullet points]

## Processing Flow
[Step-by-step description or diagram]

## Integration Points
[What other modules does this interact with?]

## Key Concepts
[Detailed explanations]

## Examples
[Concrete usage examples]

## Error Handling
[What to do when things go wrong]
```

**Word Limits**:
- Core instructions: <3500 words
- Major modules: <5000 words each
- Supporting modules: <3000 words each

**Tone**: Direct, technical, imperative ("Do X", not "You should consider doing X")

### Schema Files (`/schemas/*.json`)

**Requirements**:
- Valid JSON (test with parser)
- Comprehensive field documentation
- Example values in comments
- Type specifications
- Required vs. optional fields clearly marked

**Structure**:
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "[Schema Name]",
  "description": "[What this schema represents]",
  "type": "object",
  "required": ["field1", "field2"],
  "properties": {
    "field1": {
      "type": "string",
      "description": "[What this field means]",
      "example": "[Example value]"
    }
  }
}
```

### Library Files (`/libraries/**/*.md`)

**Purpose**: Pre-built knowledge to reduce research load

**Requirements**:
- Factual and well-researched
- Genre/power-system agnostic (no anime-specific lore)
- Examples from multiple anime
- Clear categorization
- Easy to scan/reference

### Template Files (`/templates/*.md`)

**Purpose**: Examples for players and AIDM to reference

**Requirements**:
- Complete, working examples
- Well-commented
- Multiple variations when appropriate
- Clear structure

---

## Common Pitfalls

### Pitfall 1: "Let's Build an App!"
**Wrong**: "We should create a web interface for AIDM"  
**Right**: "We should improve the session export format to make state management easier"

**Why**: AIDM is an instruction set for LLMs, not standalone software

### Pitfall 2: "This Needs Perfect Balance"
**Wrong**: "We need to mathematically balance all skills for competitive play"  
**Right**: "Skills should feel narratively appropriate and roughly balanced"

**Why**: AIDM prioritizes story over competitive mechanics

### Pitfall 3: "Let's Pre-Build Everything"
**Wrong**: "We should create complete worlds for 100 popular anime"  
**Right**: "We should create frameworks and research protocols so AIDM can build any anime world on demand"

**Why**: Research-on-demand scales better than pre-built content

### Pitfall 4: "More Features = Better"
**Wrong**: "Let's add 20 new mechanics to make it more interesting"  
**Right**: "Let's ensure the 6 core systems work flawlessly"

**Why**: Simple, robust systems beat complex, fragile ones

### Pitfall 5: "The AI Should Decide"
**Wrong**: "AIDM should automatically adjust difficulty without telling the player"  
**Right**: "AIDM should ask the player their difficulty preference and remember it"

**Why**: Player agency is sacred

### Pitfall 6: "Verbose Documentation is Better" (NEW - Critical)
**Wrong**: "Let's add 6 detailed paragraphs explaining this 3-line concept"  
**Right**: "Let's compress this to structured data: Category(attribute) | Category(attribute)"

**Why**: Token efficiency enables better gameplay. See Context Budget Management principle.

**Example of anti-pattern**:
```markdown
❌ VERBOSE (50 tokens):
The familiarity scale ranges from 0, which means completely unknown and the 
player has never heard of the concept, all the way to 4, which represents 
expert mastery where the player has deep understanding.

✅ OPTIMIZED (18 tokens):
Familiarity: 0=UNKNOWN(never heard)→Full research | 1=HEARD→Quick research | 
2=KNOW→Verify | 3=FLUENT→Apply | 4=EXPERT→Innovate
```
**Impact**: 32 tokens saved (64% reduction), 100% information preserved

**When creating new files**:
- Use ultra-compact markdown from the start
- Follow patterns in existing optimized files
- Apply multi-pass refinement (3+ iterations)
- Validate information parity = 100%

**See**: `OPTIMIZATION_CHECKLIST.md` for quick reference, `docs/TOKEN_OPTIMIZATION_METHODOLOGY.md` for complete guide

---

## Testing Protocol

### Before Submitting Changes

1. **Self-Review**:
   - Does this violate any invariants in `ARCHITECTURE.md`?
   - Is this within scope per `SCOPE.md`?
   - Does this preserve player agency?
   - Is it modular (works without requiring other new files)?
   - **NEW**: Does it meet token optimization targets? (See checklist below)

2. **Token Optimization Validation** (NEW - Mandatory):
   - [ ] Applied multi-pass optimization (3+ iterations)
   - [ ] Meets reduction target for file type (60-75% for instructions, 55-65% for libraries)
   - [ ] 3+ dry tests performed (grep searches for critical content) - 100% PASS required
   - [ ] Information parity = 100% vs unoptimized version
   - [ ] Word count documented (use 0.75 conversion for token estimate)
   - [ ] Reference: `OPTIMIZATION_CHECKLIST.md` for process

3. **Documentation**:
   - Updated `STATE.md` with changes
   - Updated `TOKEN_OPTIMIZATION_AUDIT.md` if file was optimized
   - Added examples if needed
   - Clarified integration points
   - Noted any breaking changes

4. **Validation**:
   - JSON schemas validated with parser
   - Word counts within limits AND optimized
   - No external dependencies introduced
   - Clear, technical writing (machine-interpreter oriented)

### Acceptance Testing

Run the 8 tests from `/docs/SCOPE.md`:
1. Cold Start Test
2. Multi-Anime Fusion Test
3. Session Persistence Test
4. Combat Mechanics Test
5. Memory Coherence Test
6. Error Recovery Test
7. Genre Adaptation Test
8. Research Validation Test

**All must pass** before considering changes complete.

---

## AI Collaboration Best Practices

### For Code-Related Tasks

**Good Request**:
```
I need to create the character_schema.json file. It should include:
- HP/MP/SP with current and max values
- Skills array with name, type, cost, cooldown
- Inventory with weight limits
- Experience and level tracking

It must be valid JSON and under 200 lines. Reference the 
JRPG mechanics in SCOPE.md for what stats to include.
```

**Poor Request**:
```
Make me a character system.
```

### For Writing/Instruction Tasks

**Good Request**:
```
Write the Session Zero instruction file (06_session_zero.md). It should:
- Guide players through 5-phase character creation
- Stay under 3000 words
- Reference anime_integration.md for research protocol
- Include examples of each phase
- Tone should be direct and technical

Here's the architecture context: [paste relevant section]
```

**Poor Request**:
```
Write session zero stuff.
```

### For Refinement Tasks

**Good Request**:
```
The cognitive_engine.md file needs better examples of intent 
classification. Add 5 examples covering edge cases:
- Sarcastic dialogue
- Implicit actions
- Ambiguous commands
- Multi-intent inputs
- Jailbreak attempts

Keep under 500 words total for examples section.
```

**Poor Request**:
```
Improve the cognitive engine file.
```

---

## File Organization Rules

### Directory Structure (MUST FOLLOW)

```
/docs                    # Core project documentation
/instructions            # AIDM behavioral instructions
/schemas                 # JSON structure definitions
/libraries               # Pre-built knowledge bases
  /genre_tropes          # Anime genre tropes
  /power_systems         # Power frameworks
  /common_mechanics      # JRPG mechanics
/templates               # Example files
/tools                   # Validation scripts
/isekairpg_old           # Archived v1.0 (reference only)
```

**Never**:
- Create new top-level directories without approval
- Mix file types (don't put schemas in /instructions)
- Store temporary/test files in the project
- Include generated output (save exports, etc.)

---

## Contribution Workflow

### For New Features

1. **Proposal**: Describe feature, why it's needed, how it fits scope
2. **Design**: Create architecture sketch, identify affected modules
3. **Review**: Check against invariants and scope
4. **Implement**: Create/modify files following guidelines
5. **Test**: Run acceptance tests
6. **Document**: Update STATE.md, add examples
7. **Submit**: Mark as complete in todo list

### For Bug Fixes

1. **Reproduce**: Confirm the bug with specific example
2. **Locate**: Identify which module(s) are affected
3. **Fix**: Make minimal change to resolve issue
4. **Validate**: Ensure fix doesn't break other tests
5. **Document**: Note fix in STATE.md

### For Documentation

1. **Identify Gap**: What's unclear or missing?
2. **Research**: Check if it's covered elsewhere
3. **Write**: Create clear, concise explanation
4. **Cross-Reference**: Link to related docs
5. **Review**: Have AI check for clarity

---

## Emergency Protocols

### If AI Goes Off-Track

**Symptoms**:
- Suggesting standalone app development
- Adding external dependencies
- Violating modularity
- Removing player agency
- Scope creep

**Recovery**:
1. Stop current work
2. Re-share `README.md`, `ARCHITECTURE.md`, `SCOPE.md`
3. Explicitly state: "We're building instruction files for LLMs, not standalone software"
4. Point to specific violated principle
5. Ask AI to restart with constraints in mind

### If Stuck on Complex Problem

**Strategies**:
1. **Simplify**: Can this be broken into smaller pieces?
2. **Reference Old System**: How did v1.0 handle this? (see `/isekairpg_old`)
3. **Check Improvement Proposal**: Does AIDM_Improvement_Proposal_2025.md address this?
4. **Ask for Alternatives**: "Give me 3 different approaches to solve this"
5. **Sleep On It**: Complex problems often clarify overnight

### If Tests Fail

**Debug Process**:
1. Identify which test failed and why
2. Check if recent changes introduced the bug
3. Review module integration points
4. Validate schemas and data flow
5. Test with simplified scenario
6. If persistent, revert changes and rethink approach

---

## Quality Standards

### Writing Quality

- **Clear**: No jargon without explanation
- **Concise**: Respect word limits strictly
- **Complete**: Provide examples, not just theory
- **Consistent**: Match tone and style of existing docs

### Technical Quality

- **Valid**: JSON schemas parse correctly
- **Tested**: Examples actually work when executed
- **Robust**: Handle edge cases and errors gracefully
- **Efficient**: Respect LLM token/context limits

### User Experience

- **Intuitive**: Players can understand without reading everything
- **Forgiving**: Errors are caught and corrected
- **Respectful**: Player agency always preserved
- **Engaging**: System enhances fun, doesn't obstruct it

---

## Version Control

### When to Increment Version

- **Patch (2.0.x)**: Bug fixes, documentation clarifications
- **Minor (2.x.0)**: New trope libraries, additional examples, non-breaking features
- **Major (x.0.0)**: Architecture changes, breaking changes to schemas, new core systems

### Changelog Maintenance

Update `/docs/STATE.md` after every significant change:
- What changed
- Why it changed
- Impact on existing files
- Migration notes if breaking

---

## Success Indicators

You're doing it right if:

✅ Files stay within word/size limits  
✅ Modules remain independent  
✅ All 8 acceptance tests pass  
✅ Player agency is preserved  
✅ No external dependencies introduced  
✅ Documentation stays current  
✅ AI can understand and work with the system  

You're doing it wrong if:

❌ Building standalone applications  
❌ Creating tightly coupled modules  
❌ Tests breaking after changes  
❌ AI making player decisions  
❌ Requiring databases or servers  
❌ Documentation out of sync  
❌ AI confused about what to do  

---

## Final Reminder

**AIDM v2 is an instruction set, not a program.**

Every file you create should be something an LLM can read and follow as behavioral guidance. If you find yourself thinking "we need to deploy this" or "users need to install this," you've strayed from the core concept.

Stay focused on making the instructions clear, comprehensive, and modular. The LLM does the hard work of executing them.

---

**For questions, check `/docs/ARCHITECTURE.md`. For scope questions, check `/docs/SCOPE.md`. For progress, check `/docs/STATE.md`.**
