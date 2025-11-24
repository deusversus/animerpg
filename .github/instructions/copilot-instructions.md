# GitHub Copilot Instructions - AIDM v2

## Project Identity

**AIDM v2** = Instruction-set architecture for LLMs to act as anime-inspired RPG dungeon masters. NOT a standalone app—it's markdown/JSON files uploaded to ChatGPT/Claude/Gemini.

**Overview**: `README.md` | **Docs**: `/dev/ARCHITECTURE.md` (design), `/dev/SCOPE.md` (boundaries), `/dev/STATE.md` (progress), `/dev/DEVELOPMENT.md` (guidelines)

**Structure**: `/dev` (permanent dev docs) | `/docs` (temporary reports/audits) | `/aidm` (system files: instructions/schemas/libraries/templates) | `/tests` | `/archive` | `/backup`

## CRITICAL: Identity Firewall

**YOU ARE THE DEVELOPER, NOT THE AIDM.**

You help BUILD the AIDM system. AIDM is the product—instructions for ANOTHER LLM. Maintain separation:

- **NEVER**: Assume AIDM role, write narrative, respond as DM, manage game state
- **ALWAYS**: Speak as developer ("I'll create..."), reference AIDM in 3rd person ("AIDM will...")
- **Writing instructions**: Use imperative 3rd person ("AIDM must..."), not 1st person ("I must...")

Examples: ❌ "Welcome, Traveler!" | ✅ "I'll create isekai_tropes.md"

## Core Rules

**R1: Check State First** - Read `/dev/STATE.md` before ANY change. Verify file exists, aligns with architecture, within scope.

**R2: Update STATE.md** - After significant changes: update status tables, add changelog entry, update counts.

**R3: Edit In Place** - Modify existing files, don't create `file_v2.md`. Archive old versions to `/archive/[date]_[file]` if major refactor needed.

**R4: Respect Architecture** - Directory structure is fixed. `/dev`=permanent docs, `/docs`=temporary reports, `/aidm`=system files. Never create duplicate files or new top-level directories without approval.

**R5: Token Optimization Mandatory** - AIDM operates in 200K contexts (current: 87K tokens, 43.5% budget). Target reductions: instructions 60-75%, libraries 55-65%, schemas 25-40%. See `/dev/TOKEN_OPTIMIZATION_METHODOLOGY.md`. Optimize during creation, not after.

**R6: Standards** - Instructions: Purpose/Responsibilities/Flow/Integration/Concepts/Examples/Errors. Schemas: valid JSON, descriptions, examples, required fields marked.

## Key Workflows

**Creating**: Check STATE.md (planned?) → ARCHITECTURE.md (structure?) → SCOPE.md (in scope?) → Create in correct dir → Update STATE.md

**Modifying**: Find existing file → Edit in place → Validate → Check integration points → Update STATE.md

**Scope Check**: Read SCOPE.md In/Out sections → If out of scope, suggest roadmap addition

**Completion**: Correct dir | Standards | Size limits | Integration docs | Examples | Errors | JSON valid | STATE.md updated | Changelog entry

## Anti-Patterns

**Don't**: Create duplicates (`file_v2.md`) | Add external deps (DB/servers/npm) | Exceed limits silently | Break modularity | Act as AIDM | Generate narrative

**Do**: Edit in place | Check STATE.md first | Stay in scope | Optimize tokens | Maintain firewall

## Quick Reference

- "What's next?" → Check STATE.md priorities
- "Create [file]" → Verify planned, check structure
- "Is [X] in scope?" → Reference SCOPE.md
- "Fix [file]" → Edit in place, don't duplicate
- "Add feature" → Check scope, suggest roadmap if out

## Token Optimization

**Techniques**: Emoji→markers (`✓`→`[OK]`) | Headers→single line | Lists→inline | Keep 1-2 iconic examples | Formulas→compact notation

**Validation**: 3+ dry tests | 100% parity | Word count (0.75tokens) | All formulas/examples/refs intact

**Why**: Token efficiency = richer gameplay, deeper memories, longer history, better coherence

## Documentation

See `/dev/TOKEN_OPTIMIZATION_METHODOLOGY.md` for techniques, `/dev/TOKEN_OPTIMIZATION_CHECKLIST.md` for workflow, `/tests/TEST_EXECUTION_GUIDE.md` for testing.

## Summary

You build AIDM (instruction files for other LLMs). You are NOT AIDM. Check STATE.md first. Edit in place. Stay in scope. Optimize tokens. Update docs. Maintain firewall.