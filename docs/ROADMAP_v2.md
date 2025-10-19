# AIDM v2 Development Roadmap

**Last Updated**: 2025-10-19  
**Current Version**: v2.0 MVP (Production Ready)  
**Next Target**: v2.1 Core Systems (Q4 2025 - Q1 2026)

---

## Current Status: v2.0 MVP ✓

**Complete**: Core narrative engine, 20 anime profiles, 15 genre trope libraries, 8 JSON schemas, 14 instruction modules, Session Zero, memory system, NPC intelligence, combat resolution, progression, anime integration, token optimization (62.3% reduction)

**Validation Status**:
- ✅ 2/8 acceptance tests passed (TEST-001 Session Zero, TEST-004 Combat)
- ⚠️ 6/8 tests incomplete (Multi-Anime Fusion, Session Persistence, Memory Coherence, Error Recovery, Genre Adaptation, Research Protocol)
- ⚠️ Long-term play (10+ sessions) untested
- ⚠️ Extreme scale (100+ NPCs/quests) theoretical

**Known Gaps**:
- No quest management system (tracked informally via memory)
- No faction reputation mechanics (NPC affinity exists, faction-level missing)
- No economy/currency system (inventory exists, no transactions)
- No death/resurrection rules (0 HP = defeat, but no dying mechanics)
- Schema migration tool missing (version tagging exists, no automation)

---

## Priority 1: Production Validation (NOW - 4 weeks)

**Goal**: Complete all 8 acceptance tests before v2.1 feature work

### Tasks

1. **Complete TEST-002: Multi-Anime Fusion** (1 week)
   - Test 3-anime blend (Naruto + MHA + Solo Leveling)
   - Verify power system harmonization works
   - Check for rule contradictions
   - Document edge cases

2. **Complete TEST-003: Session Persistence** (1 week)
   - Run 20+ turn session with save/load cycles
   - Verify all state preserved (NPCs, quests, memory)
   - Test schema validation on import
   - Check memory compression triggers

3. **Complete TEST-005: Memory Coherence** (1 week)
   - Validate heat_index decay over extended play
   - Test memory retrieval accuracy
   - Verify compression doesn't lose critical info
   - Check 100+ thread handling

4. **Complete TEST-006: Error Recovery** (3 days)
   - Test edge cases (invalid inputs, corrupted state)
   - Verify graceful degradation
   - Check fallback modes
   - Validate error messages

5. **Complete TEST-007: Genre Adaptation** (3 days)
   - Test genre switching mid-campaign
   - Verify trope library loading
   - Check narrative consistency
   - Validate profile blending

6. **Complete TEST-008: Research Protocol** (3 days)
   - Test with fake anime (must not hallucinate)
   - Verify web research protocol
   - Check player confirmation loop
   - Validate fallback behavior

### Success Criteria
- All 8 tests show PASS status
- Root cause analysis documented for failures
- Prompt adjustments implemented
- Known limitations documented

---

## Priority 2: v2.1 Core Systems (4-6 months)

**Goal**: Add essential gameplay systems deferred from v2.0

### Phase 2.1a: Critical Fixes (2 weeks)

**Schema Migration System**
- Add `schema_version` field to all schemas
- Create migration scripts for v2.0 → v2.1
- Document migration procedures
- Add backward compatibility checks

**Documentation Sync**
- Fix Module 10 loading (Tier 1 vs Session-Specific)
- Align "World State memory" vs "world_events" terminology
- Add prompt injection defense rule
- Standardize "Next:" pointers (or remove)

**Automated State Propagation**
- City destruction → auto-update locations/NPCs/factions
- NPC death → auto-update relationships/world events
- Quest completion → auto-award XP/update memory
- Faction change → auto-update affiliated NPCs

### Phase 2.1b: Quest System (3 weeks)

**quest_schema.json**
```json
{
  "quest_id": "string",
  "title": "string",
  "description": "string",
  "objectives": [
    {
      "id": "string",
      "description": "string",
      "completed": "boolean",
      "progress": "number",
      "required": "boolean"
    }
  ],
  "rewards": {
    "xp": "number",
    "items": ["string"],
    "reputation": {}
  },
  "status": "active|completed|failed",
  "branching": {
    "choices": [],
    "dependencies": []
  },
  "time_limit": "datetime|null",
  "fail_conditions": []
}
```

**Module Updates**
- Expand Module 03: Quest state tracking
- Expand Module 05: Quest generation
- Expand Module 09: Quest XP automation
- Add quest log compression (10+ quests)

### Phase 2.1c: Faction System (2 weeks)

**faction_schema.json**
```json
{
  "faction_id": "string",
  "name": "string",
  "description": "string",
  "reputation": "number",  // -100 to +100
  "reputation_tier": "hostile|unfriendly|neutral|friendly|allied",
  "relationships": {
    "faction_id": "number"
  },
  "quests": ["quest_id"],
  "benefits": {},
  "penalties": {}
}
```

**Module Updates**
- Expand Module 04: Faction-influenced NPC disposition
- Update world_state_schema: Add faction reputation tracking
- Add faction quest lines

### Phase 2.1d: Economy System (2 weeks)

**economy_schema.json**
```json
{
  "currencies": {
    "gold": "number",
    "gems": "number"
  },
  "prices": {
    "item_id": "number"
  },
  "transactions": [],
  "market_conditions": {}
}
```

**Module Updates**
- Expand Module 03: Currency transactions
- Expand Module 04: Merchant NPCs
- Add item pricing tables
- Add buying/selling mechanics

### Phase 2.1e: Combat Enhancements (3 weeks)

**Death/Resurrection**
- 0 HP = Downed (not dead)
- Death saves: 3 successes = stabilize, 3 failures = dead
- Resurrection costs (items, rituals, XP penalty)
- Injury table for lasting consequences

**Combat Maneuvers**
- Grapple: STR vs STR/DEX contest
- Disarm: Attack at disadvantage
- Called Shot: -5 to hit for targeted effect
- Aid: Give ally Advantage

**Training System**
- Downtime training grants skill XP
- 1 week training = bonus skill points
- Training montage mechanics

**Tournament Framework**
- Bracket management
- Between-match fatigue
- Seeding mechanics
- Spectator reactions

### Phase 2.1f: Validation & Polish (2 weeks)

- Re-run all 8 acceptance tests
- Document new features in SCOPE.md
- Update token counts (estimate: +15-25k)
- Cross-model testing (Claude, GPT-4, Gemini)
- Extended playtest (10+ session campaign)

---

## Priority 3: Content & Accessibility (Parallel work)

**Can be done alongside P1/P2**

### Content Verification (1 week)
- Audit Seinen tropes (95 lines - sufficient?)
- Audit Slice-of-Life tropes (179 lines - sufficient?)
- Verify Sports tropes (428 lines - looks good)
- Check profile-to-trope linkage completeness

### Optional Profile Additions (1 week each)
- Fruits Basket (shoujo romance)
- Toradora (romantic comedy)
- Your Lie in April (music/drama)

### UX Enhancements (1 week)
- Expand `/help` with examples
- Add content safety checklist to Session Zero
- Add inclusivity prompts (pronouns, accessibility)
- Add simplified narration mode toggle
- Platform setup guides (ChatGPT, Claude)

---

## Priority 4: v2.5 Advanced Features (Q1-Q2 2026)

**Deferred until v2.1 stable**

- Romance mechanics (confession system, dating sim elements)
- Timekeeping automation (auto-advance date, aging)
- Training montage system (time-skip framework)
- Mass combat rules (army-scale battles)
- Weather/environment hazards
- Vehicle/mount/companion systems
- Political intrigue mechanics

---

## Priority 5: v2.x Optional Systems (Q2+ 2026)

**Port from v1 as Tier 3 libraries**

- Crafting system (3,879 lines from v1)
- Guild system (1,327 lines from v1)
- Base building (781 lines from v1)

---

## AI Development Protocol

### Session Setup
1. Load `docs/STATE.md` first (current progress)
2. Load `docs/ARCHITECTURE.md` (system invariants)
3. Load this roadmap (what to work on)
4. Check `/tests/` for relevant acceptance tests

### Work Rules
1. **Never** skip acceptance tests for "done" features
2. **Always** update STATE.md after completing work
3. **Always** validate changes don't break existing tests
4. **Always** maintain token budget (<87k base, <30k active)
5. **Never** add features not in this roadmap without approval

### Completion Checklist
- [ ] Feature implementation done
- [ ] Relevant tests pass
- [ ] STATE.md updated
- [ ] Token count verified
- [ ] Documentation updated
- [ ] Integration points validated

### When to Ask
- Architecture changes (breaks invariants)
- Scope additions (not in roadmap)
- Major refactors (affects >3 modules)
- Test failures (can't resolve)
- Token budget exceeded (+5k over estimate)

---

## Token Budget Tracking

**Current Base**: ~87k tokens
- Modules: ~54k
- Schemas: ~33k

**Phase 2.1 Estimate**: +15-25k tokens
- quest_schema.json: ~3-5k
- faction_schema.json: ~2-3k
- economy_schema.json: ~2-3k
- Module expansions: ~8-14k

**Target**: Stay under 120k base total

**Alert Thresholds**:
- 100k = review for optimization
- 110k = mandatory consolidation
- 120k = hard limit, reject additions

---

## Version Milestones

### v2.0 (Current) ✓
Core narrative engine operational

### v2.1 (Target: Q1 2026)
- All 8 tests pass
- Quest/Faction/Economy systems
- Death/resurrection mechanics
- 10+ session validation

### v2.5 (Target: Q2 2026)
- Romance/timekeeping/training
- Extended playtest validation
- Cross-model compatibility

### v3.0 (Target: Q3+ 2026)
- Community content platform
- Multimodal enhancements
- Advanced AI features

---

## Anti-Patterns to Avoid

**❌ Don't**:
- Add features before tests pass
- Skip STATE.md updates
- Exceed token budget without review
- Break module dependencies
- Add content without schema updates
- Duplicate code across modules

**✅ Do**:
- Complete one priority at a time
- Update docs with code
- Validate tests after changes
- Keep token counts visible
- Follow established patterns
- Ask before major changes
