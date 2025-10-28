# Automated Cascade System Design

**Purpose**: Reduce manual update burden and prevent state inconsistencies by automatically propagating world changes across related entities

**Target**: Module 03 (State Manager) expansion for Phase 2.1a

---

## Design Principles

1. **Atomic Transactions**: All cascade updates succeed or fail together (no partial states)
2. **Explicit Triggers**: Clear, documented conditions that initiate cascades
3. **Predictable Order**: Deterministic execution sequence for debugging
4. **Graceful Degradation**: If cascade fails, system logs error but doesn't crash
5. **Audit Trail**: All cascades logged for debugging and player transparency

---

## Cascade Types

### 1. NPC Death Cascade

**Trigger**: NPC `hp_current` reaches 0 AND `can_die` = true

**Cascade Sequence**:
```
1. Update npc_schema:
   - Set status = "dead"
   - Set can_die = false (prevent re-death)
   - Add death_timestamp
   - Preserve all other fields (for memory/relationships)

2. Update character_schema.relationships:
   - Find all entries with npc_id
   - Set status = "deceased"
   - DO NOT remove (preserve for narrative)
   - Add death_note field

3. Update character_schema.quests:
   - Scan all active quests for associated_npcs containing npc_id
   - Defeat/kill quests → Mark complete, award XP
   - Protection/escort quests → Mark failed
   - Neutral quests → Add complication flag

4. Update world_state_schema.factions:
   - IF NPC has faction_role = "leader":
     - Reduce faction power by 15-25%
     - Add faction_event: "Leadership Lost"
     - Trigger succession (if defined)
   - IF NPC has faction_role = "member":
     - Reduce faction power by 1-5%
   - Update faction.members array (remove npc_id)

5. Create memory_thread:
   - category: "world_events"
   - summary: "[NPC name] died [cause]"
   - heat_index: 80-100 (based on NPC importance)
   - flags.plot_critical: true (if NPC had plot_critical flag)
   - immutable: true

6. Update world_state_schema.world_changing_events:
   - Add event log entry
   - Include ripple effects

7. Log cascade execution:
   - Record all updates made
   - Timestamp
   - Success/failure status
```

**Example**:
```json
// Trigger: Zabuza's HP reaches 0
{
  "cascade_type": "npc_death",
  "npc_id": "npc_zabuza",
  "updates": [
    {"schema": "npc", "field": "status", "old": "alive", "new": "dead"},
    {"schema": "character.quests", "quest_id": "quest_defeat_zabuza", "status": "complete", "xp_awarded": 500},
    {"schema": "world_state.factions", "faction_id": "hidden_mist", "power": -20},
    {"schema": "memory", "thread_id": "mem_world_events_zabuza_death_1", "created": true}
  ],
  "timestamp": "2025-10-27T14:32:00Z",
  "success": true
}
```

---

### 2. Location Destruction Cascade

**Trigger**: Location `status` changes to "destroyed" OR `destruction_level` ≥ 75%

**Cascade Sequence**:
```
1. Update world_state_schema.locations:
   - Set status = "destroyed"
   - Set accessible = false
   - Preserve description (for historical reference)
   - Add destruction_cause, destruction_timestamp

2. Update all NPCs with current_location = location_id:
   - Set current_location = "displaced" OR nearest safe location
   - Add displaced flag
   - Create NPC-specific memory of displacement

3. Update world_state_schema.factions:
   - IF location was faction territory:
     - Remove from faction.controlled_territories
     - Reduce faction power by 10-30% (based on strategic importance)
     - Add faction_event: "Territory Lost"
   - Update rival factions (may gain territory/power)

4. Update character_schema.quests:
   - Scan for quests with quest_location = location_id
   - Mark as failed OR add complication (location rebuilt/changed)
   - Offer alternative quest paths if available

5. Update world_state_schema.special_events:
   - Cancel events scheduled at destroyed location
   - Create refugee crisis event if civilian_population > 0

6. Create memory_thread:
   - category: "world_events"
   - summary: "[Location] destroyed by [cause]"
   - heat_index: 90-100
   - flags.plot_critical: true
   - immutable: true

7. Create ripple effect memories:
   - Economic impact (trade routes disrupted)
   - Political impact (power vacuum)
   - Social impact (refugee movement)

8. Log cascade execution
```

**Example**:
```json
// Trigger: Konoha destroyed
{
  "cascade_type": "location_destruction",
  "location_id": "konoha",
  "updates": [
    {"schema": "world_state.locations", "field": "status", "old": "thriving", "new": "destroyed"},
    {"schema": "npc", "count": 47, "field": "current_location", "old": "konoha", "new": "displaced"},
    {"schema": "world_state.factions", "faction_id": "leaf_village", "power": -50, "territories": -1},
    {"schema": "character.quests", "failed": 3, "complicated": 5},
    {"schema": "world_state.special_events", "canceled": 2},
    {"schema": "memory", "threads_created": 4}
  ],
  "timestamp": "2025-10-27T15:00:00Z",
  "success": true,
  "ripple_effects": ["economic_collapse", "refugee_crisis", "power_vacuum"]
}
```

---

### 3. Quest Completion Cascade

**Trigger**: Quest `status` changes to "complete"

**Cascade Sequence**:
```
1. Update character_schema.quests:
   - Move from active_quests to completed_quests array
   - Set completion_timestamp
   - Preserve all quest data

2. Award XP automatically:
   - Read quest.rewards.xp
   - Add to character_schema.progression.current_xp
   - Trigger level up check (cascade into level up if threshold met)
   - Log XP gain in progression.xp_log

3. Update NPCs with associated_quests containing quest_id:
   - Mark quest as resolved in NPC's quest_involvement
   - Adjust affinity based on quest outcome (+20 for success, -10 for betrayal)

4. Check quest dependencies:
   - Scan quest_tree for child quests
   - Unlock child quests if prerequisites met
   - Add to character_schema.quests.available_quests

5. Update world_state if quest has world_impact flag:
   - Faction power adjustments
   - Location status changes
   - Political landscape shifts

6. Create memory_thread:
   - category: "quests"
   - summary: "Completed [quest name]"
   - heat_index: Based on quest significance (40-80)
   - flags.player_initiated: true

7. Distribute rewards automatically:
   - Items → character_schema.inventory
   - Currency → character_schema.wallet
   - Skills → character_schema.skills.available_skills
   - Reputation → faction_reputation updates

8. Log cascade execution
```

**Example**:
```json
// Trigger: Quest "Defeat the Nine-Tails" completed
{
  "cascade_type": "quest_completion",
  "quest_id": "quest_nine_tails",
  "updates": [
    {"schema": "character.quests", "moved": "active → completed"},
    {"schema": "character.progression", "xp_awarded": 1000, "level_up": false},
    {"schema": "npc", "npc_id": "npc_hiruzen", "affinity": +30},
    {"schema": "character.quests.available", "unlocked": ["quest_hokage_ceremony"]},
    {"schema": "world_state.factions", "faction_id": "leaf_village", "power": +10},
    {"schema": "character.inventory", "items_added": ["hero_medal"]},
    {"schema": "memory", "thread_id": "mem_quests_nine_tails_1", "created": true}
  ],
  "timestamp": "2025-10-27T16:00:00Z",
  "success": true
}
```

---

### 4. Faction Power Shift Cascade

**Trigger**: Faction `power_score` changes by ≥15 points OR `territory` array modified

**Cascade Sequence**:
```
1. Update world_state_schema.factions:
   - Recalculate power_score
   - Update faction_standing (dominant/major/minor/failing)
   - Adjust controlled_territories if applicable

2. Update affiliated NPCs:
   - Scan all NPCs with faction_affiliation = faction_id
   - Adjust behavior based on faction strength:
     - Dominant faction → NPCs more confident/aggressive
     - Failing faction → NPCs desperate/defensive
   - Update NPC dialogue_tone based on faction morale

3. Update rival factions:
   - If faction gains power → rivals lose influence
   - Update faction.relationships (standings between factions)
   - Trigger political events (alliances/conflicts)

4. Update player faction_reputation:
   - IF player involved in faction power shift:
     - Adjust character_schema.faction_reputation
     - May trigger faction quests (recruitment, betrayal, alliance)

5. Create memory_thread:
   - category: "world_events"
   - summary: "[Faction] power shifted [direction] due to [cause]"
   - heat_index: 60-90
   - flags: Include political_impact flag

6. Update world_state.political_landscape:
   - Recalculate faction dominance rankings
   - Trigger special events if power balance tips
   - Update trade routes, safe zones based on faction control

7. Log cascade execution
```

**Example**:
```json
// Trigger: Akatsuki gains +25 power from capturing Tailed Beast
{
  "cascade_type": "faction_power_shift",
  "faction_id": "akatsuki",
  "power_change": +25,
  "updates": [
    {"schema": "world_state.factions", "field": "power_score", "old": 60, "new": 85},
    {"schema": "world_state.factions", "field": "standing", "old": "major", "new": "dominant"},
    {"schema": "npc", "count": 12, "faction_id": "akatsuki", "behavior": "aggressive"},
    {"schema": "world_state.factions", "faction_id": "leaf_village", "influence": -10},
    {"schema": "world_state.political_landscape", "updated": true},
    {"schema": "character.faction_reputation", "faction_id": "akatsuki", "reputation": -50},
    {"schema": "memory", "thread_id": "mem_world_events_akatsuki_rise_1", "created": true}
  ],
  "timestamp": "2025-10-27T17:00:00Z",
  "success": true,
  "triggered_events": ["faction_conflict_alert", "safe_zone_update"]
}
```

---

## Implementation Architecture

### Module 03 Expansion

**New Section**: Cascade Management System

```markdown
## Cascade Management System

### Purpose
Automatically propagate state changes across related entities to maintain consistency and reduce manual update burden.

### Cascade Registry

**Defined Cascades**:
1. npc_death → [NPC schema, Character relationships, Quests, Factions, Memory]
2. location_destruction → [Locations, NPCs, Factions, Quests, Events, Memory]
3. quest_completion → [Quests, Progression, NPCs, Dependencies, Rewards, Memory]
4. faction_power_shift → [Factions, NPCs, Reputation, Politics, Memory]

### Trigger Detection

**When to check for cascades**:
- After ANY schema update (State Manager validates then checks triggers)
- During SAVE operation (ensure consistent state)
- During LOAD operation (repair inconsistencies if detected)

**Trigger evaluation**:
- Read affected schema field
- Check against cascade registry
- If match found → Execute cascade

### Execution Flow

1. **Pre-validation**: Verify current state is valid before cascade
2. **Cascade planning**: Build execution plan with all required updates
3. **Atomic execution**: Apply all updates in transaction
4. **Post-validation**: Verify new state is valid
5. **Rollback**: If validation fails, revert all changes
6. **Logging**: Record cascade execution regardless of success/failure

### Error Handling

**If cascade fails**:
- Log error with full context (which trigger, what failed, why)
- Revert ALL changes from this cascade (atomic rollback)
- Alert AIDM to notify player: "State update encountered an issue, please report"
- Continue gameplay (degraded mode - manual updates required)

**If cascade partially succeeds**:
- Should never happen (atomic execution)
- If detected → Treat as total failure, rollback

### Performance Considerations

**Cascade throttling**:
- Maximum 5 cascades per turn (prevent infinite loops)
- Cascade depth limit: 3 levels (prevent chaining)
- If exceeded → Log warning, halt cascades, alert AIDM

**Cascade chaining**:
- Allowed: Quest completion → Level up → Skill unlock
- Forbidden: Faction shift → NPC death → Faction shift (circular)

### Player Transparency

**Cascade notifications**:
- Always show cascade effects to player
- Example: "Zabuza's death caused: Leaf Village power +10, Quest 'Defeat Zabuza' complete (+500 XP), 3 relationships updated"
- Format: "[Event] → [Consequence 1], [Consequence 2], [Consequence 3]"

**Cascade opt-out**:
- Advanced players can disable auto-cascades via meta-command
- Manual mode: AIDM asks "This would trigger cascades: [list]. Proceed? (yes/no)"
```

### Cascade Execution Code Template

**Pseudocode** (for implementation in Module 03):
```python
def execute_cascade(trigger_type, context):
    """
    Execute cascade based on trigger type
    
    Args:
        trigger_type: One of [npc_death, location_destruction, quest_completion, faction_power_shift]
        context: Dict with trigger-specific data (npc_id, location_id, quest_id, faction_id, etc.)
    
    Returns:
        CascadeResult with success/failure and update log
    """
    # 1. Pre-validation
    if not validate_current_state():
        return CascadeResult(success=False, error="Invalid state before cascade")
    
    # 2. Build execution plan
    plan = build_cascade_plan(trigger_type, context)
    
    # 3. Atomic execution
    try:
        begin_transaction()
        
        for update in plan.updates:
            apply_update(update)
        
        # 4. Post-validation
        if not validate_new_state():
            rollback_transaction()
            return CascadeResult(success=False, error="Invalid state after cascade")
        
        commit_transaction()
        
        # 5. Logging
        log_cascade(trigger_type, context, plan, success=True)
        
        return CascadeResult(success=True, updates=plan.updates)
        
    except Exception as e:
        rollback_transaction()
        log_cascade(trigger_type, context, plan, success=False, error=str(e))
        return CascadeResult(success=False, error=str(e))


def build_cascade_plan(trigger_type, context):
    """Build list of all updates required for this cascade"""
    plan = CascadePlan()
    
    if trigger_type == "npc_death":
        plan.add_update(schema="npc", field="status", value="dead")
        plan.add_update(schema="character.relationships", updates=find_npc_relationships(context.npc_id))
        plan.add_update(schema="character.quests", updates=find_affected_quests(context.npc_id))
        plan.add_update(schema="world_state.factions", updates=calculate_faction_impact(context.npc_id))
        plan.add_update(schema="memory", new_thread=create_death_memory(context))
    
    # Similar for other cascade types...
    
    return plan
```

---

## Testing Requirements

### Unit Tests (Per Cascade Type)

**NPC Death**:
- Leader death reduces faction power correctly
- Quest dependencies resolve properly
- Memory threads created with correct heat_index
- No orphaned references remain

**Location Destruction**:
- All resident NPCs displaced
- Faction territories updated
- Events canceled appropriately
- Ripple effects logged

**Quest Completion**:
- XP awarded correctly
- Dependencies unlocked
- Rewards distributed
- Child quests available

**Faction Power Shift**:
- Rival factions react appropriately
- NPC behavior updates
- Political landscape recalculated
- Player reputation adjusted

### Integration Tests

**Cascade Chaining**:
- Quest completion → Level up → Skill unlock (allowed, depth 3)
- NPC death → Faction collapse → Territory destruction (validate limits)

**Rollback Testing**:
- Corrupt one update → Entire cascade reverts
- State identical to pre-cascade after rollback

**Performance Testing**:
- 5 cascades in single turn execute within acceptable time
- Cascade depth limit enforced
- No infinite loops possible

---

## Rollout Plan

### Phase 1: Foundation (Week 1)
- [ ] Design cascade registry in Module 03
- [ ] Implement trigger detection system
- [ ] Create atomic transaction framework
- [ ] Build logging infrastructure

### Phase 2: Core Cascades (Week 2)
- [ ] Implement NPC death cascade
- [ ] Implement quest completion cascade
- [ ] Test both cascades extensively
- [ ] Document player-facing behavior

### Phase 3: Advanced Cascades (Week 3)
- [ ] Implement location destruction cascade
- [ ] Implement faction power shift cascade
- [ ] Test cascade chaining
- [ ] Add player transparency notifications

### Phase 4: Polish & Validation (Week 4)
- [ ] Optimize performance
- [ ] Add cascade opt-out for advanced players
- [ ] Complete integration testing
- [ ] Update ARCHITECTURE.md with cascade documentation

---

## Future Enhancements (Phase 2.2+)

**Additional Cascade Types**:
- Skill mastery → Training opportunities unlock
- Relationship milestone → Special quests available
- Economic crisis → Market price fluctuations
- Weather catastrophe → Location accessibility changes

**Smart Cascades**:
- ML-based cascade prediction ("This action will likely cause X")
- Player-defined cascade rules (custom automation)
- Cascade preview mode (show effects before applying)

**Cascade Analytics**:
- Track most common cascades
- Identify performance bottlenecks
- Player satisfaction metrics (are cascades helpful or annoying?)

---

## Notes for AI Developers

**Cascades are powerful but dangerous**. They can create emergent gameplay BUT also:
- Overwhelm players with too many side effects
- Create unexpected state corruption
- Impact performance if not optimized
- Cause circular dependencies if poorly designed

**Design philosophy**: 
- Cascades should feel natural and expected ("of course killing the faction leader weakens them")
- Players should see cascades as helpful automation, not mysterious black box
- When in doubt, add transparency (show what happened and why)

**Always test cascades with edge cases**:
- What if NPC is already dead?
- What if location was already destroyed?
- What if quest was already completed?
- What if faction power is already at 0 or 100?

**Idempotency**: Cascades should be safe to run multiple times with same input (no duplicate effects).
