# AIDM v3 Implementation Tasks

> **Philosophy:** Prove core loop first, add complexity only when needed.
> Each phase should produce a playable (if limited) system.

---

## Phase 1: Core Loop MVP

**Goal:** Does Intent → Outcome → Key Animator → State feel like anime?

**Skip for now:** Sakuga, Memory, Director, multiple profiles

- [ ] **Database Setup**
  - [ ] Create PostgreSQL schema for characters, NPCs, world_state
  - [ ] Implement basic CRUD operations
  - [ ] Session/campaign management

- [ ] **Single Profile**
  - [ ] Define YAML schema for narrative profiles
  - [ ] Create HunterXHunter profile (tactical, well-defined)
  - [ ] Implement profile loader

- [ ] **Core Agents**
  - [ ] Intent Classifier (Haiku) - parse player action
  - [ ] Outcome Judge (Haiku) - should this succeed? how dramatically?
  - [ ] Key Animator (Sonnet) - generate narrative

- [ ] **Code Layer (Minimal)**
  - [ ] State read/write
  - [ ] Dice engine (when randomness desired)
  - [ ] Turn commit

- [ ] **Interface**
  - [ ] CLI chat loop
  - [ ] Debug output (show agent decisions)

- [ ] **Vibe Test**
  - [ ] 5 manual test turns
  - [ ] Does it feel like HxH? Adjust prompts if not

---

## Phase 2: Context Layer

**Goal:** Does it remember past events and adapt to profile style?

**Add:** Memory Store, Rule Library, Context Selector

- [ ] **Memory Store**
  - [ ] ChromaDB/Pinecone setup
  - [ ] Heat decay system
  - [ ] Vector search retrieval

- [ ] **Rule Library (RAG)**
  - [ ] Create chunk extraction script (`chunk_v2_modules.py`)
  - [ ] Extract chunks from Module 12 (scales, archetypes, ceremonies)
  - [ ] Extract chunks from Module 13 (DNA, genres, examples)
  - [ ] Implement `rule_library.py` (loader + vector indexing)

- [ ] **Memory Ranker Agent**
  - [ ] Relevance scoring (semantic + heat)
  - [ ] Top-K retrieval

- [ ] **Context Selector Agent**
  - [ ] Pull from Rule Library (relevant chunks)
  - [ ] Assemble prompt under token budget
  - [ ] Inject profile DNA

- [ ] **Vibe Test**
  - [ ] Same 5 turns as Phase 1
  - [ ] Does retrieved context improve feel?
  - [ ] Create 5+ golden set entries

---

## Phase 3: Full Agent Layer

**Goal:** Does it make good decisions across all situations?

**Add:** Sakuga, Validation, judgment agents, more profiles

> **Philosophy (Dec 2025):** Fast models with 100% schema compliance. 
> Use structured LLM calls for all judgment, not Python plugins.

- [ ] **Sakuga Interceptor**
  - [ ] "Is this moment epic?" detection
  - [ ] Override flag for auto-success

- [ ] **Validation Agent**
  - [ ] Resource checks, target existence, cooldowns
  - [ ] Provide alternatives when invalid

- [ ] **Scale Selector Agent**
  - [ ] Which narrative scale applies? (tactical, ensemble, spectacle...)
  - [ ] Replaces hardcoded tier thresholds

- [ ] **NPC Reaction Agent**
  - [ ] Disposition change, dialogue hint
  - [ ] Replaces affinity math

- [ ] **Additional Profiles**
  - [ ] AttackOnTitan (dark, tactical)
  - [ ] GurrenLagann (hype, spirit)
  - [ ] OnePunchMan (comedy, OP)
  - [ ] Konosuba (comedy, failure)

- [ ] **Golden Set Testing**
  - [ ] 20+ entries per profile
  - [ ] LLM-as-judge scoring
  - [ ] Target: 7+ average

---

## Phase 4: The Showrunner (Director Layer)

**Goal:** Does it plan long-term and manage campaign arcs?

**Note:** Could ship v3.0 without this. Only needed for multi-session campaigns.

- [ ] **Director Agent**
  - [ ] System prompt (swappable per profile)
  - [ ] Session-end review trigger
  - [ ] Every-5-turn check-in

- [ ] **Campaign Bible**
  - [ ] Arc tracking (phase, triggers)
  - [ ] Plot thread management

- [ ] **Foreshadowing Ledger**
  - [ ] Seed planting
  - [ ] Callback detection
  - [ ] Overdue alerts

- [ ] **Spotlight Tracker**
  - [ ] Scene count per NPC
  - [ ] Spotlight debt → recommendations

- [ ] **Player Calibration**
  - [ ] Feedback signal collection
  - [ ] DNA adjustment recommendations

---

## Phase 5: Polish & Production

**Goal:** Production-ready for external users.

- [ ] **Web UI**
  - [ ] Chat interface
  - [ ] Debug HUD (state, decisions, costs)
  - [ ] Profile selector + campaign management

- [ ] **Session Management**
  - [ ] Save/load campaigns
  - [ ] Session summaries
  - [ ] "Previously on..." generation

- [ ] **Error Recovery**
  - [ ] Agent fallback hierarchy
  - [ ] State rollback on failure
  - [ ] Rate limit handling

- [ ] **Optimization**
  - [ ] Prompt caching (30-50% savings)
  - [ ] Parallel agent execution
  - [ ] Token/cost monitoring

- [ ] **Human Testing**
  - [ ] 5 testers × 5 profiles × 1 session
  - [ ] Post-session survey
  - [ ] Iterate on failures

---

## Reference Links
- [AIDM v3 Project Plan](./AIDM_V3_PROJECT_PLAN.md)
- [AIDM v3 Tech Spec](./AIDM_V3_TECH_SPEC.md)
- [AIDM v2 Instructions Summary](../docs/aidm_instructions_summary.md)
- [Original v2 Instructions](../aidm/instructions/)

