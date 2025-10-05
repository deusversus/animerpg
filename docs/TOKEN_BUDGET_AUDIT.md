# AIDM v2.0 Token Budget Audit

**Audit Date**: October 5, 2025  
**System Version**: 2.0-beta (post-TEST-004 fixes)  
**Audit Type**: Comprehensive token usage analysis

---

## Executive Summary

**Current Status**: ✅ WITHIN BUDGET (24% of 200K context window)

**Key Findings**:
- **Base System**: 47,984 tokens (24% of 200K Claude context)
- **Gameplay Reserve**: 152,016 tokens (76% remaining)
- **Critical Issue**: Module 07 (Anime Integration) consumes 4,676 tokens (9.7% of total system)
- **Recommendation**: Implement aggressive lazy-loading for Tier 2 modules

---

## Token Usage Breakdown

### Instruction Modules (13 files)

**Total**: 32,680 tokens (68% of system budget)

| Rank | Module | Lines | Est. Tokens | % of System | Priority | Load Strategy |
|------|--------|-------|-------------|-------------|----------|---------------|
| 1 | 07_anime_integration.md | 1,336 | 4,676 | 9.7% | CRITICAL | Tier 2 - CREATIVE intent |
| 2 | 10_error_recovery.md | 944 | 3,304 | 6.9% | HIGH | Tier 1 - Always loaded |
| 3 | 06_session_zero.md | 793 | 2,776 | 5.8% | CRITICAL | Tier 2 - META intent |
| 4 | 05_narrative_systems.md | 782 | 2,737 | 5.7% | MEDIUM | Tier 2 - Story ongoing |
| 5 | 02_learning_engine.md | 768 | 2,688 | 5.6% | HIGH | Tier 1 - Always loaded |
| 6 | 01_cognitive_engine.md | 732 | 2,562 | 5.3% | HIGH | Tier 1 - Always loaded |
| 7 | 08_combat_resolution.md | 697 | 2,440 | 5.1% | HIGH | Tier 2 - COMBAT intent |
| 8 | 03_state_manager.md | 694 | 2,429 | 5.1% | CRITICAL | Tier 1 - Always loaded |
| 9 | 00_system_initialization.md | 661 | 2,314 | 4.8% | HIGH | Tier 1 - Bootstrap only |
| 10 | 04_npc_intelligence.md | 581 | 2,034 | 4.2% | HIGH | Tier 2 - SOCIAL intent |
| 11 | 09_progression_systems.md | 458 | 1,603 | 3.3% | MEDIUM | Tier 2 - XP events |
| 12 | 11_dice_resolution.md | 451 | 1,578 | 3.3% | HIGH | Tier 1 - Always loaded |
| 13 | 12_player_agency.md | 440 | 1,540 | 3.2% | CRITICAL | Tier 1 - Always loaded |

**Tier 1 Breakdown** (7 core modules - always loaded):
- 00_system_initialization.md: 2,314 tokens
- 01_cognitive_engine.md: 2,562 tokens
- 02_learning_engine.md: 2,688 tokens
- 03_state_manager.md: 2,429 tokens
- 10_error_recovery.md: 3,304 tokens
- 11_dice_resolution.md: 1,578 tokens
- 12_player_agency.md: 1,540 tokens

**Tier 1 Total**: 16,415 tokens (34% of system, 8.2% of 200K context)

**Tier 2 Breakdown** (6 modules - lazy-loaded on intent):
- 04_npc_intelligence.md: 2,034 tokens (SOCIAL)
- 05_narrative_systems.md: 2,737 tokens (ongoing story)
- 06_session_zero.md: 2,776 tokens (META - character creation)
- 07_anime_integration.md: 4,676 tokens (CREATIVE - anime research)
- 08_combat_resolution.md: 2,440 tokens (COMBAT)
- 09_progression_systems.md: 1,603 tokens (XP events)

**Tier 2 Total**: 16,266 tokens (34% of system) - loaded conditionally

---

### Schema Files (7 files)

**Total**: 15,304 tokens (32% of system budget)

| Rank | Schema | Lines | Est. Tokens | % of System | Load Timing |
|------|--------|-------|-------------|-------------|-------------|
| 1 | npc_schema.json | 806 | 3,224 | 6.7% | With Module 04 (SOCIAL) |
| 2 | anime_world_schema.json | 704 | 2,816 | 5.9% | With Module 07 (CREATIVE) |
| 3 | power_system_schema.json | 618 | 2,472 | 5.2% | With Module 07 (CREATIVE) |
| 4 | memory_thread_schema.json | 570 | 2,280 | 4.8% | With Module 02 (always) |
| 5 | character_schema.json | 403 | 1,612 | 3.4% | With Module 03 (always) |
| 6 | world_state_schema.json | 399 | 1,596 | 3.3% | With Module 03 (always) |
| 7 | session_export_schema.json | 326 | 1,304 | 2.7% | With Module 03 (save/load) |

**Always-Loaded Schemas** (4 files):
- character_schema.json: 1,612 tokens
- world_state_schema.json: 1,596 tokens
- session_export_schema.json: 1,304 tokens
- memory_thread_schema.json: 2,280 tokens

**Always-Loaded Schema Total**: 6,792 tokens (14% of system, 3.4% of context)

**Lazy-Loaded Schemas** (3 files):
- npc_schema.json: 3,224 tokens (with SOCIAL intent)
- anime_world_schema.json: 2,816 tokens (with CREATIVE intent)
- power_system_schema.json: 2,472 tokens (with CREATIVE intent)

**Lazy-Loaded Schema Total**: 8,512 tokens (18% of system) - loaded conditionally

---

## Token Budget Scenarios

### Scenario 1: Session Start (Minimal Load)

**Loaded**:
- Tier 1 instructions: 16,415 tokens
- Always-loaded schemas: 6,792 tokens

**Total**: 23,207 tokens (11.6% of 200K context)  
**Remaining**: 176,793 tokens (88.4% for gameplay)

**Verdict**: ✅ EXCELLENT - Maximum gameplay space

---

### Scenario 2: Combat Session (Combat + NPCs)

**Loaded**:
- Tier 1 instructions: 16,415 tokens
- Tier 2 (Combat): 2,440 tokens
- Tier 2 (NPCs): 2,034 tokens
- Always-loaded schemas: 6,792 tokens
- NPC schema: 3,224 tokens

**Total**: 30,905 tokens (15.5% of 200K context)  
**Remaining**: 169,095 tokens (84.5% for gameplay)

**Verdict**: ✅ GOOD - Plenty of gameplay space

---

### Scenario 3: Character Creation (Session Zero)

**Loaded**:
- Tier 1 instructions: 16,415 tokens
- Tier 2 (Session Zero): 2,776 tokens
- Tier 2 (Anime Integration): 4,676 tokens
- Always-loaded schemas: 6,792 tokens
- Anime schemas: 5,288 tokens (anime_world + power_system)

**Total**: 35,947 tokens (18% of 200K context)  
**Remaining**: 164,053 tokens (82% for gameplay)

**Verdict**: ✅ GOOD - Adequate space for interactive character creation

---

### Scenario 4: ALL Modules Loaded (Worst Case)

**Loaded**:
- All Tier 1 instructions: 16,415 tokens
- All Tier 2 instructions: 16,266 tokens
- All schemas: 15,304 tokens

**Total**: 47,984 tokens (24% of 200K context)  
**Remaining**: 152,016 tokens (76% for gameplay)

**Verdict**: ⚠️ ACCEPTABLE - Still 76% remaining, but wasteful

**Risk**: If all modules stay loaded, conversation history will fill faster
- At 100 exchanges (~150 tokens/exchange avg): 15,000 tokens
- **Total usage**: 62,984 tokens (31.5% of context)
- Still safe, but inefficient

---

## Critical Findings

### 🔴 Issue 1: Module 07 (Anime Integration) Is Oversized

**Problem**: 4,676 tokens (9.7% of total system, 14.3% of all instructions)

**Why It's Large**:
- Anime Integration includes:
  - 5 familiarity levels (detailed decision trees)
  - Research protocol (web search, player collaboration, fallback methods)
  - Harmonization workflows (power balance, lore conflicts)
  - Regression mechanics (4,000 words added in TEST-004 fixes)
  - Pre-built library references
  - Integration examples from multiple anime

**Impact**:
- When CREATIVE intent detected → 4,676 tokens loaded
- Combined with anime schemas (5,288 tokens) = 9,964 tokens just for anime features
- **27% of total system budget** for one feature

**Recommendations**:
1. **Split Module 07 into two files** (HIGH PRIORITY):
   - `07a_anime_integration_core.md` (~2,000 tokens): Research protocol, familiarity levels
   - `07b_anime_regression_mechanics.md` (~2,500 tokens): Time-loop rules, temporal logic
   - Load `07b` only when regression protagonist detected

2. **Move examples to external library**:
   - Create `libraries/anime_examples/integration_examples.md`
   - Reference library instead of embedding examples
   - Saves ~800 tokens

3. **Compress decision trees**:
   - Current: Verbose flowcharts with full descriptions
   - Target: Compact bullet lists with cross-references
   - Potential savings: 500-700 tokens

**Estimated Savings**: 1,500-2,000 tokens (3-4% of system budget)

---

### ⚠️ Issue 2: Tier 1 (Always-Loaded) Is Heavy

**Problem**: 16,415 tokens (34% of system) loaded on EVERY session

**Breakdown**:
- Module 10 (Error Recovery): 3,304 tokens - heaviest Tier 1 module
- Module 02 (Learning Engine): 2,688 tokens
- Module 01 (Cognitive Engine): 2,562 tokens

**Impact**:
- Every session starts with 8.2% of 200K context consumed
- Long campaigns (50+ exchanges) may approach 40-50% context usage
- Less critical in 200K windows, but problematic for 128K LLMs

**Recommendations**:

1. **Compress Module 10 (Error Recovery)** (MEDIUM PRIORITY):
   - Current: 3,304 tokens (extensive error examples, recovery protocols)
   - Target: 2,000-2,500 tokens
   - How: Remove redundant examples, consolidate error categories
   - Savings: 800-1,300 tokens

2. **Move Module 00 (System Initialization) to one-time load** (LOW PRIORITY):
   - Current: 2,314 tokens loaded always
   - Reality: Only needed during bootstrap (first response)
   - Solution: Unload after successful initialization
   - Savings: 2,314 tokens (reduces Tier 1 to 14,101 tokens)

3. **Consider splitting Module 02 (Learning Engine)** (LOW PRIORITY):
   - Core memory operations: ~1,500 tokens (always needed)
   - Advanced compression/heat index: ~1,200 tokens (load when memory >50% full)
   - Savings during early sessions: ~1,200 tokens

**Estimated Savings**: 2,500-4,800 tokens (5-10% of system budget)

---

### ✅ Success 1: Tier 2 Modules Are Well-Sized

**Finding**: All Tier 2 modules are 1,600-2,800 tokens (except Module 07)

**Well-Designed Modules**:
- 09_progression_systems.md: 1,603 tokens - compact, focused
- 04_npc_intelligence.md: 2,034 tokens - efficient for complex system
- 08_combat_resolution.md: 2,440 tokens - comprehensive without bloat

**Why This Works**:
- Lazy-loading means these only load when needed
- Even if 3-4 Tier 2 modules load simultaneously, total <10K tokens
- Leaves 80%+ of context for gameplay

**No Action Needed**: Tier 2 modules are optimally sized

---

### ✅ Success 2: Schemas Are Appropriate Size

**Finding**: 15,304 total tokens (32% of system) is reasonable for 7 comprehensive data structures

**Largest Schema Analysis**:
- `npc_schema.json`: 3,224 tokens
  - Includes: Personality, knowledge, affinity, schedules, dialogue history, relationships
  - Justified: NPCs are complex entities requiring detailed state tracking

- `anime_world_schema.json`: 2,816 tokens
  - Includes: Power systems, world rules, fusion tracking, verification data
  - Justified: Anime integration requires extensive metadata

**Recommendation**: No compression needed. Schemas define data structure, not loaded into every response.

---

## Optimization Recommendations

### Priority 1: CRITICAL (Immediate Action)

**1. Split Module 07 (Anime Integration)**

**Action**:
```
Current: 07_anime_integration.md (4,676 tokens)

Split into:
- 07a_anime_integration_core.md (~2,000 tokens)
  - Research protocol, familiarity levels, harmonization
- 07b_anime_regression_mechanics.md (~2,500 tokens)
  - Time-loop rules, temporal logic, butterfly effect models
```

**Impact**: 
- Saves 2,500 tokens when regression mechanics not needed (most sessions)
- Reduces CREATIVE intent load: 4,676 → 2,000 tokens (57% reduction)
- Better modularity (regression is specialized feature)

**Implementation Time**: 30 minutes (reorganize content, update load triggers)

---

**2. Implement Aggressive Module Unloading**

**Current State**: Module 00 says "unload at >80% token usage"

**Problem**: 80% of 200K = 160,000 tokens. By that point, only 40K tokens remain.

**New Protocol**:
```markdown
## Aggressive Token Management

**Unload Tier 2 modules when**:
1. Token usage >60% (120,000 / 200K) - unload LEAST recently used module
2. Token usage >70% (140,000 / 200K) - unload ALL unused Tier 2 modules
3. Token usage >80% (160,000 / 200K) - compress memory threads (emergency)

**Track Module Activity**:
- Last used turn: {module_name: turn_number}
- If module unused for 10+ turns → candidate for unloading
- If module unused for 20+ turns → automatic unload

**Reload on Demand**:
- Module unloaded mid-session? Reload when intent detected again
- Example: Combat module unloaded after fight → reload when next combat starts
```

**Impact**:
- Extends viable session length: 50 turns → 100+ turns
- Maintains 70%+ gameplay space throughout campaign
- Prevents emergency compressions (reactive → proactive)

**Implementation Time**: 45 minutes (update Module 00, add tracking protocol)

---

### Priority 2: HIGH (This Week)

**3. Compress Module 10 (Error Recovery)**

**Current**: 3,304 tokens (extensive error examples)

**Target**: 2,200 tokens (consolidated examples, reference-based error categories)

**How**:
- Remove redundant error examples (keep 1-2 per category, not 5)
- Convert verbose recovery protocols to compact checklists
- Move detailed error explanations to comments (LLM reads, but lower token weight)

**Savings**: ~1,100 tokens (2.3% of system budget)

**Implementation Time**: 1 hour (rewrite module, validate coverage)

---

**4. One-Time Load for Module 00 (System Initialization)**

**Current**: 2,314 tokens, always loaded

**New Strategy**:
```
Load Module 00 → Bootstrap system → Unload Module 00 after success

Module 00 is only needed for:
1. Schema validation (once per session)
2. Module loading (once per session)
3. Session detection (once per session)

After initialization complete, Module 00 never referenced again.
```

**Impact**:
- Tier 1 reduction: 16,415 → 14,101 tokens (14% smaller)
- Session start: 23,207 → 20,893 tokens (10.4% of 200K instead of 11.6%)
- Permanent savings for entire session duration

**Implementation Time**: 15 minutes (add unload trigger after bootstrap)

---

### Priority 3: MEDIUM (This Month)

**5. Split Module 02 (Learning Engine) for Progressive Loading**

**Current**: 2,688 tokens, always loaded

**Proposed**:
```
02a_learning_engine_core.md (~1,500 tokens) - Tier 1
- Basic memory storage/retrieval
- Memory thread creation
- Heat index calculation

02b_learning_engine_advanced.md (~1,200 tokens) - Tier 2
- Aggressive compression protocols
- Memory archival
- Cross-thread analysis
- Load when: Memory >50% capacity OR explicit META: COMPRESS command
```

**Impact**:
- Tier 1 reduction: 14,101 → 12,901 tokens (during early/mid sessions)
- Advanced features load only when memory management critical
- No functionality loss (progressive enhancement)

**Savings**: 1,200 tokens (early sessions), 0 tokens (late sessions when needed)

**Implementation Time**: 1.5 hours (split module, update triggers)

---

**6. Reference-Based Examples (Move to Libraries)**

**Current**: Many modules embed 5-10 examples inline

**Target**: 
```
Module: Include 1-2 core examples inline
Library: Create examples/[module]_examples.md with 10+ detailed examples

LLM loads examples library only when:
- Player explicitly requests examples: "META: Show combat examples"
- AIDM confused/uncertain: Auto-load relevant example library
- Testing/validation: Load to verify understanding
```

**Modules to Optimize**:
- Module 07 (Anime Integration): ~800 tokens of examples
- Module 05 (Narrative Systems): ~400 tokens of examples
- Module 08 (Combat Resolution): ~300 tokens of examples

**Total Savings**: ~1,500 tokens (3% of system)

**Implementation Time**: 2 hours (extract examples, create library structure, update references)

---

## Long-Term Projections

### Scenario A: No Optimizations (Current State)

**Session Start**: 23,207 tokens (11.6%)  
**After 50 exchanges** (~7,500 tokens conversation): 30,707 tokens (15.4%)  
**After 100 exchanges** (~15,000 tokens conversation): 38,207 tokens (19.1%)  
**After 200 exchanges** (~30,000 tokens conversation): 53,207 tokens (26.6%)

**Verdict**: ✅ SAFE for 200K context windows, ⚠️ RISKY for 128K windows

---

### Scenario B: Priority 1 Optimizations Implemented

**Changes**:
- Module 07 split (saves 2,500 tokens when regression not used)
- Aggressive unloading at 60% threshold

**Session Start**: 20,707 tokens (10.4%)  
**After 50 exchanges**: 28,207 tokens (14.1%)  
**After 100 exchanges**: 35,707 tokens (17.9%)  
**After 200 exchanges**: 48,207 tokens (24.1%) + unloading kicks in at 120K

**Verdict**: ✅ GOOD for 200K, ✅ SAFE for 128K (with unloading)

---

### Scenario C: All Optimizations Implemented

**Changes**:
- Module 07 split: -2,500 tokens (conditional)
- Module 00 unload after init: -2,314 tokens
- Module 10 compression: -1,100 tokens
- Module 02 split: -1,200 tokens (early sessions)
- Example libraries: -1,500 tokens

**Total Savings**: 8,614 tokens (18% reduction)

**Session Start**: 14,593 tokens (7.3%)  
**After 50 exchanges**: 22,093 tokens (11%)  
**After 100 exchanges**: 29,593 tokens (14.8%)  
**After 200 exchanges**: 44,593 tokens (22.3%)

**Verdict**: ✅ EXCELLENT for 200K, ✅ EXCELLENT for 128K

---

## Platform-Specific Recommendations

### Claude Sonnet 4.5 (200K context)

**Current Status**: ✅ NO URGENCY

**Recommendations**:
- Priority 1 optimizations: OPTIONAL (nice-to-have)
- Priority 2 optimizations: SKIP (200K is plenty)
- Priority 3 optimizations: SKIP (diminishing returns)

**Reasoning**: 76% of 200K context (152K tokens) for gameplay is more than sufficient for 99% of sessions.

---

### ChatGPT-4 (128K context)

**Current Status**: ⚠️ MODERATE URGENCY

**Recommendations**:
- Priority 1 optimizations: IMPLEMENT (critical for 100+ exchange sessions)
- Priority 2 optimizations: IMPLEMENT (safety margin)
- Priority 3 optimizations: CONSIDER (if extensive campaigns planned)

**Reasoning**: 
- Current: 47,984 tokens = 37.5% of 128K context
- After 100 exchanges: ~63K tokens = 49% of 128K
- Optimization target: Keep <40% even at 100 exchanges

---

### Gemini 1.5 Pro (1M context)

**Current Status**: ✅ NO URGENCY

**Recommendations**:
- All optimizations: SKIP (massive overkill)

**Reasoning**: 47,984 tokens = 4.8% of 1M context. Even 500-exchange sessions would only use ~15% total.

---

## Immediate Action Items

### This Week (Priority 1)

- [ ] **Split Module 07**: Create `07a_anime_integration_core.md` and `07b_anime_regression_mechanics.md`
- [ ] **Update Module 00**: Implement aggressive unloading at 60%/70%/80% thresholds
- [ ] **Update load triggers**: Only load `07b` when regression protagonist detected
- [ ] **Test token savings**: Validate split reduces CREATIVE intent load by 50%+

**Expected Impact**: 2,500-3,000 token savings (5-6% of system budget)

---

### This Month (Priority 2)

- [ ] **Compress Module 10**: Reduce from 3,304 → 2,200 tokens
- [ ] **One-time load Module 00**: Unload after initialization complete
- [ ] **Create unload tracking**: Monitor module usage, auto-unload after 10+ unused turns
- [ ] **Update STATE.md**: Document optimizations in changelog

**Expected Impact**: 3,400-4,500 additional tokens saved (7-9% of system budget)

---

### Future (Priority 3 - Optional)

- [ ] **Split Module 02**: Progressive loading for advanced memory features
- [ ] **Extract examples**: Move detailed examples to library files
- [ ] **Benchmark testing**: TEST-005 (Memory Coherence) with token monitoring

**Expected Impact**: 2,700-3,000 additional tokens saved (5-6% of system budget)

---

## Token Budget Health Metrics

### Current Health: ✅ GOOD (24% base system usage)

**Grading Scale**:
- **EXCELLENT** (0-20%): Abundant gameplay space, low risk
- **GOOD** (20-35%): Adequate space, minor optimizations beneficial
- **FAIR** (35-50%): Functional but tight, optimizations recommended
- **POOR** (50-65%): High risk, optimizations critical
- **CRITICAL** (65%+): Imminent context overflow, immediate action required

**Current Position**: GOOD (24%)  
**After Priority 1 fixes**: EXCELLENT (18%)  
**After All fixes**: EXCELLENT (14%)

---

## Conclusion

### Summary

**Current State**:
- Base system: 47,984 tokens (24% of 200K context)
- Tier 1 (always loaded): 16,415 tokens (8.2% of context)
- Tier 2 (conditional): 16,266 tokens (loaded on demand)
- Schemas: 15,304 tokens (32% of system, but not all loaded)

**Health Assessment**: ✅ GOOD - System is within acceptable limits

**Critical Issues**:
1. Module 07 (Anime Integration) oversized at 4,676 tokens (9.7% of system)
2. Tier 1 modules could be more aggressive about unloading

**Recommended Actions**:
- **CRITICAL**: Split Module 07 into core + regression mechanics (Priority 1)
- **HIGH**: Implement aggressive unloading at 60% threshold (Priority 1)
- **MEDIUM**: Compress Module 10, one-time load Module 00 (Priority 2)

**Expected Outcome**:
- With Priority 1 fixes: 20,707 token base (10.4% of context) - ✅ EXCELLENT
- With all fixes: 14,593 token base (7.3% of context) - ✅ EXCELLENT

**Platform Compatibility**:
- Claude Sonnet 4.5 (200K): ✅ Current state is fine, optimizations optional
- ChatGPT-4 (128K): ⚠️ Priority 1 optimizations recommended
- Gemini 1.5 Pro (1M): ✅ No action needed

---

**Next Steps**: Implement Priority 1 optimizations this week, monitor token usage during TEST-005 (Memory Coherence), validate savings.

