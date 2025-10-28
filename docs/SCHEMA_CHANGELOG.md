# AIDM Schema Changelog

**Purpose**: Track all modifications to JSON schemas with impact assessment for migration planning

**Schema Versioning**: Semantic versioning (MAJOR.MINOR.PATCH)
- **MAJOR**: Breaking changes requiring migration scripts
- **MINOR**: Backward-compatible additions (new optional fields)
- **PATCH**: Documentation/clarification updates, no structural changes

---

## Version 2.0.0 (2025-10-27)

**Status**: Current baseline version

### All Schemas (8 total)

**Added**:
- `schema_version` field (string, pattern: `^\d+\.\d+\.\d+$`, default: "2.0.0")
  - Required field in all 8 schemas
  - Enables migration compatibility tracking
  - Separate from `export_version` in session_export_schema (schema file version vs export data version)

**Impact**: 
- ✅ Backward compatible (new field with default value)
- ✅ No migration required for existing data
- ⚠️ New exports/data MUST include schema_version field
- 📝 Update Module 00 (System Initialization) to validate schema_version on startup
- 📝 Update Module 03 (State Manager) to include schema_version in exports

**Affected Files**:
- `character_schema.json`
- `world_state_schema.json`
- `npc_schema.json`
- `memory_thread_schema.json`
- `narrative_profile_schema.json`
- `anime_world_schema.json`
- `power_system_schema.json`
- `session_export_schema.json`

**Rationale**: Phase 2.1a requirement - establish migration tracking before adding new features (quest system, faction system, economy system) that will modify schemas

---

## Schema Change Discipline

### Adding Fields

**Process**:
1. Determine if field is required or optional
2. If required: provide default value AND update all dependent modules
3. If optional: document expected behavior when field absent
4. Increment MINOR version (backward compatible)
5. Update this changelog with impact assessment
6. Test with old data to ensure graceful handling

**Example**:
```json
"new_field": {
  "type": "string",
  "description": "New feature tracking",
  "default": "none"
}
```

### Removing Fields

**Process**:
1. **Version N**: Mark field as deprecated in description
2. **Version N+1**: Make field optional with deprecation notice
3. **Version N+2**: Remove field, increment MAJOR version
4. Create migration helper to transform old data
5. Document migration in ARCHITECTURE.md

**Timeline**: Minimum 2 versions (6-12 months) between deprecation and removal

### Renaming Fields

**Process**:
1. Add new field with desired name
2. Keep old field as alias for 1 version transition
3. Update all modules to use new field name
4. Remove old field in next version
5. Increment MINOR (addition) then MAJOR (removal)

**Example Migration**:
```json
// Version 2.1.0 (transition)
"new_name": { "type": "string" },
"old_name": { 
  "type": "string",
  "description": "DEPRECATED: Use new_name instead"
}

// Version 2.2.0 (cleanup)
"new_name": { "type": "string" }
// old_name removed
```

### Breaking Changes

**Triggers** (require MAJOR version bump):
- Removing required field
- Changing field type
- Changing validation rules (stricter patterns/ranges)
- Restructuring nested objects
- Changing enum values

**Requirements**:
- Create migration script or manual migration guide
- Update Module 03 (State Manager) to handle both versions during transition
- Document in ARCHITECTURE.md
- Test extensively with old data

---

## Version 2.1.0 (2025-10-27)

**Status**: In Development (Phase 2.1b - Quest Management System)

### quest_schema.json (NEW)

**Added**:
- Complete quest schema with structured objectives, branching paths, dependencies, time limits
- Objective system: progress tracking, required/optional flags, hidden objectives, mutual exclusivity
- Branching system: choice-based paths, parent-child quest chains, unlockable quests
- Reward system: XP, items, currency, reputation, skills, quest unlocks
- Fail conditions: NPC death, time expiration, location destruction, item loss, reputation thresholds
- Quest categories: main, side, faction, personal, daily, event, tutorial
- Difficulty tiers: trivial, easy, moderate, hard, epic, legendary
- Metadata: complete lifecycle tracking with timestamps and event logs

**Impact**:
- ✅ New schema (not breaking existing data)
- 📝 Must update Module 03 (State Manager) to handle quest CRUD operations
- 📝 Must update Module 05 (Narrative Systems) for quest generation
- 📝 Must update Module 09 (Progression) for automated XP awards
- 📝 Add quest validation to Module 00 startup checks
- 📝 Include in session_export_schema.json

**Rationale**: Phase 2.1b requirement - structured quest management with branching, dependencies, and automated tracking. Replaces informal quest arrays in character schema with full quest objects stored in world state.

### character_schema.json

**Modified**:
- Changed `quests` object from embedded quest data to ID-only references
- Old: Full quest objects with objectives/rewards/status stored in character schema
- New: Arrays of quest_ids (available/active/completed/failed) referencing world_state.narrative_state.quests
- Failed quests now store failure reason and timestamp

**Impact**:
- ⚠️ BREAKING CHANGE for existing saves with active quests
- Migration required: Extract quest data from character schema → Create quest objects in world_state → Replace with IDs
- Reduces character schema bloat (quests stored once in world, referenced by all characters)
- Enables multi-character campaigns (multiple PCs can share quest state)

**Migration Path**:
1. Read character.quests.active array (old format with embedded data)
2. For each quest: Create quest object in world_state.narrative_state.quests using quest_schema.json
3. Replace character.quests.active with array of quest_ids
4. Update character schema_version to 2.1.0

### world_state_schema.json

**Modified**:
- Added `narrative_state.quests` object (master quest registry)
- Structure: `{ "quest_id": <quest_schema.json object> }`
- All quest data stored here, characters only reference IDs

**Impact**:
- ✅ Backward compatible (new optional field)
- Centralizes quest data for easier management
- Enables quest sharing across multiple characters
- Supports DM-controlled quest progression (change state, all PCs see update)

**Rationale**: Single source of truth for quest state. Character schema tracks "which quests this PC has" while world schema defines "what those quests are".

---

## Planned Changes (Phase 2.1 Continued)

### Version 2.1.0 (Target: Q4 2025)

#### character_schema.json

**Additions** (MINOR - already partially implemented above):
- ~~`quests` object enhancement~~ ✅ DONE (ID-based references)
- `faction_reputation` object:
  - Add faction_id → reputation_score mapping
  - Add faction_standing enum (enemy/neutral/ally/champion)
- Economy integration:
  - Expand `currency` object with multi-currency support
  - Add `transaction_history` array (optional, for tracking)

**Impact**: Faction and economy additions are optional. Quest changes already applied (breaking change handled via migration).

#### world_state_schema.json

**Additions** (MINOR - partially implemented above):
- ~~`narrative_state.quests`~~ ✅ DONE (master quest registry)
- `factions` enhancement:
  - Add `territory` array of controlled locations
  - Add `power_score` calculation
  - Add `relationships` object (faction-to-faction standings)
- `economy` enhancement:
  - Add `markets` array with dynamic pricing
  - Add `merchant_npcs` references

**Impact**: Optional enhancements. Existing faction tracking via world_events continues working.

---

## Version 2.0.0 (2025-10-27)

#### npc_schema.json

**Additions** (MINOR):
- `relationships` enhancement:
  - Add `faction_affiliation` with loyalty score
  - Add `auto_update_triggers` for cascade system
- `behavior` enhancement:
  - Add `merchant_data` object for economy NPCs
  - Add `death_conditions` for cascade triggers

**Impact**: All optional. Existing NPC affinity system remains functional.

### Version 2.0.1 (Target: November 2025)

**Documentation Updates** (PATCH):
- Clarify `heat_index` decay rate meanings in memory_thread_schema
- Add examples to power_system_schema for fusion scenarios
- Expand narrative_profile_schema trope toggle descriptions

**Impact**: None - documentation only

---

## Migration Planning

### Automatic vs Manual Migration

**Automatic** (handled by Module 03):
- Adding optional fields with defaults
- Version validation and compatibility checks
- Field renaming with aliases

**Manual** (requires user action):
- Breaking changes requiring data transformation
- Complex restructuring (nested object changes)
- Version jumps > 1 MAJOR version

### Migration Tools Roadmap

**Phase 2.1a** (Current):
- [x] Add schema_version to all schemas
- [ ] Create schema_validator.py for version checking
- [ ] Update Module 00 to validate schema versions on startup
- [ ] Update Module 03 to include schema_version in exports

**Phase 2.1f** (Validation):
- [ ] Create migration_helper.py for automated transformations
- [ ] Test migration from v2.0.0 → v2.1.0 with sample data
- [ ] Document manual migration procedures in ARCHITECTURE.md

**Phase 2.2+** (Future):
- [ ] Backward compatibility layer (support N-1 versions)
- [ ] Automated schema evolution detection
- [ ] Migration testing suite

---

## Validation Procedures

### Pre-Release Checklist

Before incrementing any schema version:
- [ ] Update this changelog with changes and impact
- [ ] Test with old data to verify compatibility
- [ ] Update dependent modules (check Integration sections)
- [ ] Run schema_validator.py if available
- [ ] Update ARCHITECTURE.md if breaking changes
- [ ] Increment version in schema file
- [ ] Tag release in git with schema version

### Testing Requirements

**MINOR version** (additions):
- Load v2.0.0 data with v2.1.0 schema → Should work with defaults
- Create new data with v2.1.0 schema → Should validate
- Verify all new fields have documented defaults

**MAJOR version** (breaking):
- Load v2.0.0 data with v3.0.0 schema → Should fail gracefully with migration prompt
- Run migration tool v2.0.0 → v3.0.0 → Should produce valid v3.0.0 data
- Test edge cases (missing fields, malformed data, partial migrations)

---

## Current Schema Versions

| Schema | Version | Last Updated | Status |
|--------|---------|--------------|--------|
| character_schema.json | 2.1.0 | 2025-10-27 | Modified (quest references) |
| world_state_schema.json | 2.1.0 | 2025-10-27 | Modified (quest registry) |
| quest_schema.json | 2.1.0 | 2025-10-27 | NEW |
| npc_schema.json | 2.0.0 | 2025-10-27 | Stable |
| memory_thread_schema.json | 2.0.0 | 2025-10-27 | Stable |
| narrative_profile_schema.json | 2.0.0 | 2025-10-27 | Stable |
| anime_world_schema.json | 2.0.0 | 2025-10-27 | Stable |
| power_system_schema.json | 2.0.0 | 2025-10-27 | Stable |
| session_export_schema.json | 2.0.0 | 2025-10-27 | Stable |

---

## Notes for AI Developers

**Always check this file before modifying schemas**. Schema changes have cascading effects across:
- Instruction modules (01-13)
- State Manager (Module 03 export/import logic)
- System Initialization (Module 00 validation)
- Player-facing documentation

**When proposing schema changes**:
1. Read existing schema thoroughly
2. Check if change is truly necessary (can feature work with existing fields?)
3. Prefer optional additions over breaking changes
4. Document rationale and impact assessment
5. Update this changelog BEFORE committing schema modification

**Schema philosophy**: Schemas define data contracts. Changes should be rare, well-justified, and carefully planned. Favor composition (adding optional objects) over mutation (changing existing fields).
