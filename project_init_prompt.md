# Project Initialization Protocol

You are helping bootstrap a new software project with explicit architecture to enable successful AI-assisted development at scale.

## Your Task
Extract project requirements from minimal user input, then generate a complete structural foundation that prevents architecture decay.

## Phase 1: Requirements Extraction (Ask Once, Ask Well)

Ask the user these questions in a single message:

1. **Project Purpose** (1-2 sentences): What does this software do?
2. **Primary User Actions** (3-5 items): What will users actually DO with this?
3. **Tech Stack Preference**: Any required languages/frameworks, or should I choose?
4. **Scope Boundaries**: What is explicitly OUT of scope? (If unsure, I'll suggest boundaries)
5. **Success Criteria**: How do you know when it's "done enough"?

## Phase 2: Architecture Generation

Based on responses, generate this complete file structure:

### `/docs/ARCHITECTURE.md`
```markdown
# System Architecture

## Core Purpose
[Distilled 1-sentence purpose]

## System Invariants
[3-5 rules that MUST remain true]
- Example: "User data never leaves the services/ layer unencrypted"
- Example: "UI components never contain business logic"
- Example: "All external API calls must be retryable"

## Module Structure
[Visual directory tree with purpose annotations]

### Module: [name]
- **Purpose**: [Single responsibility]
- **Dependencies**: [What it can import]
- **Forbidden**: [What it must NOT do]
- **Key Files**: [List with 1-line descriptions]

## Data Flow
[Describe how data moves through the system]
[Use arrows: User -> API -> Service -> Database]

## External Dependencies
[List third-party services/APIs and why they're needed]

## Deployment Model
[How does this run? Web server? Desktop app? CLI tool?]
```

### `/docs/SCOPE.md`
```markdown
# Project Scope Definition

## In Scope (MVP)
- [Feature 1 with acceptance criteria]
- [Feature 2 with acceptance criteria]
- [Feature 3 with acceptance criteria]

## Explicitly Out of Scope
- [Anti-feature 1 and why]
- [Anti-feature 2 and why]
- [Complex feature we're deferring]

## Known Limitations
[Technical constraints we're accepting]

## Future Considerations
[Features we might add later, but NOT now]
```

### `/docs/DEVELOPMENT.md`
```markdown
# Development Guidelines

## Code Organization Principles
[Language-specific rules based on chosen stack]

## Testing Strategy
- Unit tests for: [which components]
- Integration tests for: [which flows]
- No tests needed for: [what we skip and why]

## AI Collaboration Rules
When working with AI assistants on this project:

1. **Never ask AI to**: [Forbidden refactors/changes]
2. **Always provide AI with**: [Required context documents]
3. **Session boundaries**: [When to start fresh chat]
4. **Architecture changes require**: [Explicit approval for what]

## Common Pitfalls
[Based on project type, list 3-5 ways this usually fails]
```

### `/docs/STATE.md`
```markdown
# Current Project State

**Last Updated**: [Auto-generated timestamp]

## Completed
- [ ] Initial architecture documents
- [ ] [Other checkboxes based on MVP scope]

## In Progress
[Empty initially]

## Known Issues
[Empty initially]

## Next Session Goals
1. [First implementation task]
2. [Second implementation task]
3. [Third implementation task]

## File Inventory
[Auto-generated list of all files with 1-line purposes]
```

### Actual Code Structure

Generate language-appropriate boilerplate:

**For TypeScript/Node.js:**
```
/src
  /core          # Business logic, pure functions
  /services      # External integrations (DB, APIs)
  /types         # Shared type definitions
  /ui            # React/Vue components (if applicable)
  /utils         # Generic helpers
  index.ts       # Entry point
/tests
  /unit
  /integration
/docs
  [Documentation files above]
```

**For Python:**
```
/src
  /core
  /services  
  /models        # Data structures
  /api           # FastAPI/Flask routes (if applicable)
  __main__.py
/tests
  /unit
  /integration
/docs
```

**Adapt structure to chosen stack**

### `/README.md`
```markdown
# [Project Name]

[One paragraph description]

## Quick Start
[Minimal steps to run]

## Architecture
See `/docs/ARCHITECTURE.md` for system design.

## Development
See `/docs/DEVELOPMENT.md` for coding guidelines.

## Project Status
See `/docs/STATE.md` for current progress.
```

### Type Definitions (Language-Dependent)

**For TypeScript projects, generate `/src/types/index.ts`:**
```typescript
// Core domain types
export interface User {
  id: string;
  // ...based on requirements
}

export interface [OtherCoreType] {
  // Extrapolate from user requirements
}

// Service contracts
export interface UserService {
  getUser(id: string): Promise<User>;
  // ...complete interface
}
```

**For Python projects, generate `/src/models/__init__.py`:**
```python
from dataclasses import dataclass
from typing import Protocol

@dataclass
class User:
    id: str
    # ...based on requirements

class UserService(Protocol):
    def get_user(self, user_id: str) -> User:
        ...
```

## Phase 3: Validation Checklist

Present this to user:

"I've generated the following structure: [list files]. Before we start coding, verify:

1. Does the module structure match your mental model?
2. Are the scope boundaries correct?
3. Are any critical invariants missing?
4. Should any modules be split or merged?

Once you approve, we can start implementing with [specific first task]."

## Phase 4: Implementation Handoff

After approval, say:

"Architecture locked. Beginning implementation.

**Session Protocol**: 
- I'll update `/docs/STATE.md` after each significant change
- If you start a new chat, share STATE.md and ARCHITECTURE.md first
- I'll refuse changes that violate documented invariants unless you explicitly override

**First task**: [Concrete, testable implementation goal]

Ready to proceed?"

---

## Meta-Instructions for This Protocol

- **Be opinionated**: Don't ask "Do you want types?" Just generate them for appropriate languages.
- **Infer aggressively**: User says "todo app" → You know it needs users, tasks, persistence, etc.
- **Front-load decisions**: Choose sensible defaults for everything not explicitly specified.
- **Make it executable**: Generated code should run (even if minimal) immediately.
- **Fail fast on ambiguity**: If truly unclear, ask ONE pointed question, don't generate partial docs.

## Success Criteria for This Protocol

You've succeeded if:
1. A developer can understand the system in 15 minutes from docs alone
2. An AI assistant can implement features without architecture questions
3. The user can resume the project after 6 months using only the docs
4. Scope creep is immediately obvious (violates documented boundaries)
5. No file exists without a documented purpose in STATE.md

---

## Usage Instructions

Copy this entire prompt into a new Claude conversation, then respond with your 5 answers to the Phase 1 questions. Claude will generate your complete project foundation in one shot.