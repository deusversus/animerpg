# Module 02: Learning Engine - Memory Management & Heat Index

**Version**: 2.0  
**Priority**: CRITICAL  
**Load Order**: Second (after Cognitive Engine)

---

## Purpose

The Learning Engine manages AIDM's memory system. It determines what to remember, how to prioritize memories, when to compress older information, and how to retrieve relevant context. This module prevents AIDM from forgetting critical details while avoiding context overload.

**Core Principle**: AIDM must REMEMBER what matters and FORGET what doesn't.

---

## Memory Architecture Overview

AIDM uses a **hierarchical memory system** with **heat-based prioritization**:

```
┌─────────────────────────────────────────────────────┐
│           ACTIVE MEMORY (Hot)                       │
│  Current session, high-heat memories, recent events │
│              [Loaded in context]                    │
└─────────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────┐
│          WARM MEMORY (Medium Heat)                  │
│  Recent sessions, referenced memories, important    │
│         NPCs, active quests, faction status         │
│         [Loaded when triggered]                     │
└─────────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────┐
│          COOL MEMORY (Low Heat)                     │
│  Older sessions, compressed summaries, background   │
│           [Loaded only when specifically needed]    │
└─────────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────┐
│         ARCHIVED MEMORY (Frozen)                    │
│  Ancient history, compressed world lore, deprecated │
│        [Rarely accessed, heavily summarized]        │
└─────────────────────────────────────────────────────┘
```

All memories are stored as **memory threads** following `memory_thread_schema.json`.

---

## Memory Categories (The 6 Hierarchies)

Every memory thread belongs to ONE of these categories, which determines its base importance and retention:

### 1. CORE Memories (Immutable)

**Heat Decay**: NONE (permanent)  
**Base Score**: 100 (maximum)  
**Compression**: NEVER

**What Goes Here**:
- Character origin story
- Unique abilities that define the character
- World foundation rules (genre, setting, core conceits)
- Campaign premise
- Immutable world laws (physics, magic rules, etc.)
- **Player-established world rules** (Session Analysis Fix #3)

**Special Subcategory: PLAYER_ESTABLISHED_RULE**

**Session Analysis Issue #4**: Player had to repeatedly correct world mechanics because AIDM forgot or contradicted established rules ("I just told you monsters don't exit gates").

**When player establishes a world rule**:

Patterns to detect:
- "Clarification: [rule]..."
- "Actually, [correction to AIDM statement]..."
- "In this world, [mechanic]..."
- "Just to be clear: [rule]..."
- "I just told you [rule]..."

**Immediate actions**:
1. Create memory thread: CORE / PLAYER_ESTABLISHED_RULE
2. Set heat: 100 (PERMANENT - never decays)
3. Add metadata:
   ```json
   {
     "category": "core",
     "subcategory": "player_established_rule",
     "heat": 100,
     "decay_rate": 0,
     "rule_text": "<player's exact words>",
     "validation_required": true
   }
   ```
4. Cross-reference: Check if this contradicts any existing memories
5. Priority: HIGHEST (check this before stating any world mechanics)

**Examples**:

```
Player: "Clarification: players normally choose a class at level 1, 
and monsters can NOT leave gates."

Memory Created:
- Category: CORE
- Subcategory: PLAYER_ESTABLISHED_RULE
- Heat: 100 (permanent)
- Content: "Class selection occurs at level 1. Monsters cannot exit gates."
- Validation: Before stating class/monster mechanics, check this memory
```

```
Player: "I just told you monsters don't exit gates..."
[This is a correction - player already stated this rule]

Action:
1. Locate existing memory (if exists, reinforce to Heat:100)
2. If missing, create immediately
3. Flag: CORRECTION_REQUIRED (AIDM contradicted player)
4. Apply: Review last response and correct the error
```

**Before making ANY assumption about world mechanics**:

```
Pseudocode:
if stating_world_mechanic:
    check_memory(subcategory="player_established_rule")
    if contradicts_player_rule:
        STOP → Ask player for clarification
        DO NOT proceed with assumption
```

**This prevents the "I just told you..." correction loop.**

**Example Core Memory**:
```json
{
  "thread_id": "mem_core_origin_001",
  "category": "core",
  "content": {
    "summary": "Player is a reincarnated software engineer from Earth",
    "details": "Died in car accident (2024), reincarnated in Vantiel as 
    16-year-old with System Interface ability (unique skill). Retains all 
    Earth knowledge including programming, physics, modern technology."
  },
  "heat_index": {
    "current_score": 100,
    "base_score": 100,
    "decay_rate": "none"
  },
  "flags": {
    "immutable": true,
    "plot_critical": true
  }
}
```

**CRITICAL RULE**: Core memories NEVER change. If player wants to retcon a core memory, create a new campaign.

### 2. CHARACTER_STATE Memories (Mutable)

**Heat Decay**: Normal  
**Base Score**: 40-80 (depending on significance)  
**Compression**: When superseded by newer state

**What Goes Here**:
- Level ups
- New skills learned
- Attribute changes
- Status effects gained/removed
- Equipment changes
- Resource updates (if significant)

**Example Character State Memory**:
```json
{
  "thread_id": "mem_char_levelup_023",
  "category": "character_state",
  "content": {
    "summary": "Leveled Fire Magic from 6 to 7",
    "details": "After defeating the Flame Salamander boss, earned 450 XP. 
    Fire Magic skill advanced to level 7, unlocking Flame Spiral technique. 
    New max MP: 180 (was 160)."
  },
  "heat_index": {
    "current_score": 65,
    "base_score": 50,
    "decay_rate": "slow"
  },
  "category_specific": {
    "state_type": "skill_learned",
    "current_value": "Fire Magic: Level 7",
    "previous_value": "Fire Magic: Level 6"
  }
}
```

**Compression Rule**: When stat changes again, compress previous value into single "progression history" summary.

### 3. RELATIONSHIPS Memories (NPC Interaction History)

**Heat Decay**: Slow  
**Base Score**: 30-70 (based on NPC importance)  
**Compression**: Summarize old interactions, keep recent + milestones

**What Goes Here**:
- Every significant NPC interaction
- Affinity changes
- Relationship milestones (friendship, romance, enmity, trust)
- NPC favors/debts
- Shared experiences with NPCs
- **Player feedback about AIDM performance** (Session Analysis Fix #6)

**Special Subcategory: PLAYER_FEEDBACK**

**Session Analysis Issue #2 Supplement**: When player gave feedback ("be less on the nose", "read my whole reply"), AIDM didn't apply corrections immediately, requiring repeated reminders.

**When player gives feedback about AIDM's performance**:

Patterns to detect:
- "Be less on the nose"
- "It doesn't feel like you read my whole reply"
- "More anime-style narrative"
- "Stop over-explaining"
- "Too much [X], not enough [Y]"
- "I prefer [style/tone/pacing]"

**Immediate actions**:
1. Create memory thread: RELATIONSHIPS / PLAYER_FEEDBACK
2. Set heat: 90 (HIGH - critical feedback)
3. Decay rate: SLOW (-1 per turn, lasts entire session)
4. Add metadata:
   ```json
   {
     "category": "relationships",
     "subcategory": "player_feedback",
     "heat": 90,
     "decay_rate": -1,
     "feedback_type": "tone|pacing|detail_level|style",
     "correction": "<what to change>",
     "apply_immediately": true,
     "persist_until": "session_end"
   }
   ```
5. **Apply in NEXT response** (not later, immediately)
6. Track: Did correction get applied? Verify in following turn

**Examples**:

```
Player: "Yes, and please be less on the nose with the explanations."

Memory Created:
- Category: RELATIONSHIPS
- Subcategory: PLAYER_FEEDBACK
- Heat: 90 (high priority)
- Feedback Type: detail_level
- Correction: "Reduce explicit explanations, show don't tell"
- Apply: IMMEDIATELY in next response

Next Response:
[Check: Am I over-explaining? If yes, cut it.]
[Use: Implication and subtext instead of explicit statements]
```

```
Player: "It really doesn't feel like you read my whole reply..."

Memory Created:
- Category: RELATIONSHIPS
- Subcategory: PLAYER_FEEDBACK
- Heat: 90 (critical)
- Feedback Type: comprehension
- Correction: "Read input completely before responding"
- Apply: IMMEDIATELY - re-read player's last message fully

Next Response:
[Trigger: Comprehension Validation Checklist from cognitive_engine]
[Action: Read 100% of input, check last 5 exchanges]
```

**Integration with cognitive_engine.md**:

Before EVERY response, cognitive_engine checks:
```
Does memory contain PLAYER_FEEDBACK (heat > 80)?
If YES → Apply that feedback NOW
Examples: Adjust tone, reduce detail, change pacing
```

**This ensures player corrections are respected instantly, not after multiple reminders.**

**Example Relationship Memory** (NPC-focused):
```json
{
  "thread_id": "mem_rel_kaito_014",
  "category": "relationships",
  "content": {
    "summary": "Saved Master Kaito's daughter from bandits",
    "details": "Master Kaito's daughter Yuki was kidnapped by Red Fang 
    bandits. Player tracked them to mountain hideout, defeated 8 bandits, 
    and rescued Yuki. Kaito's affinity jumped from 35 to 78. He offered 
    to teach advanced sword techniques as thanks.",
    "emotional_weight": "profound"
  },
  "heat_index": {
    "current_score": 85,
    "base_score": 65,
    "decay_rate": "slow"
  },
  "category_specific": {
    "npc_id": "npc_master_kaito",
    "affinity_change": +43,
    "new_affinity": 78,
    "relationship_milestone": true
  }
}
```

**CRITICAL RULE**: NEVER forget relationship milestones. They define NPC bonds.

### 4. QUESTS Memories (Progression Tracking)

**Heat Decay**: Normal until complete, then Fast  
**Base Score**: 50-90 (active quests high, completed quests drop)  
**Compression**: Heavily compress completed quests after 5+ sessions

**What Goes Here**:
- Quest acceptance
- Objective completions
- Quest failures
- Quest completions
- Quest updates/changes

**Example Quest Memory**:
```json
{
  "thread_id": "mem_quest_demon_intel_007",
  "category": "quests",
  "content": {
    "summary": "Completed objective: Locate Demon Army scout camp",
    "details": "Found Red Demon scout camp in northern forest (3km from 
    Millbrook Village). Counted 23 demons, 2 mages, 1 commander. Did not 
    engage. Reported location to Captain Reeves.",
    "emotional_weight": "significant"
  },
  "heat_index": {
    "current_score": 75,
    "base_score": 60,
    "decay_rate": "normal"
  },
  "category_specific": {
    "quest_id": "quest_demon_intelligence",
    "quest_event": "objective_completed",
    "objective_id": "locate_scout_camp"
  }
}
```

**Heat Management**: Active quest memories stay hot. Once quest completes, heat drops rapidly (players rarely care about old quest details).

### 5. WORLD_EVENTS Memories (Environmental Changes)

**Heat Decay**: Slow  
**Base Score**: 40-95 (depends on scope)  
**Compression**: Summarize regional events, NEVER compress global events

**What Goes Here**:
- Major world changes (war declarations, disasters, political shifts)
- Location changes (town destroyed, new faction moves in)
- NPC deaths or major status changes
- Faction power shifts
- Seasonal/temporal events

**Example World Event Memory**:
```json
{
  "thread_id": "mem_world_millbrook_attack_019",
  "category": "world_events",
  "content": {
    "summary": "Demon Army attacked Millbrook Village",
    "details": "Red Demon battalion (200 troops) attacked at dawn. Player 
    helped evacuate civilians. Village partially destroyed (40% buildings 
    burned). 67 casualties. Mayor killed. Survivors fled to Ironhaven. 
    Millbrook now abandoned ruins.",
    "emotional_weight": "profound"
  },
  "heat_index": {
    "current_score": 92,
    "base_score": 80,
    "decay_rate": "slow"
  },
  "category_specific": {
    "event_scope": "local",
    "affected_locations": ["loc_millbrook_village"],
    "affected_factions": ["fac_ironhaven_military", "fac_demon_army"],
    "irreversible": true
  }
}
```

**CRITICAL RULE**: Irreversible world events NEVER decay below base_score. The world remembers.

### 6. CONSEQUENCES Memories (Ripple Effects)

**Heat Decay**: Fast  
**Base Score**: 20-60  
**Compression**: Aggressive (most consequences become background context)

**What Goes Here**:
- Long-term results of player actions
- Butterfly effects
- Reputation changes
- Economic impacts
- Narrative drift adjustments

**Example Consequence Memory**:
```json
{
  "thread_id": "mem_cons_bandit_leader_022",
  "category": "consequences",
  "content": {
    "summary": "Sparing Red Fang leader led to alliance offer",
    "details": "Player spared Red Fang bandit leader Karn instead of 
    executing him (3 sessions ago). Karn has now sent messenger offering 
    alliance - Red Fangs will provide intel on Demon Army movements in 
    exchange for amnesty.",
    "emotional_weight": "significant"
  },
  "heat_index": {
    "current_score": 68,
    "base_score": 45,
    "decay_rate": "fast"
  },
  "category_specific": {
    "source_thread": "mem_rel_karn_015",
    "consequence_type": "faction_response",
    "time_delay": "3 sessions",
    "visibility": "obvious"
  }
}
```

**Management**: Consequences can fade into background noise unless they keep manifesting. Track them but allow natural decay.

---

## Heat Index System

**Heat** represents how "active" a memory is in AIDM's awareness. Higher heat = more likely to influence decisions.

### Heat Score Range: 0-100

- **90-100**: Critical/Immediate (always in context)
- **70-89**: High Priority (frequently referenced)
- **50-69**: Moderate (context-dependent retrieval)
- **30-49**: Low (only retrieved when triggered)
- **10-29**: Background (rarely accessed)
- **0-9**: Cold Storage (archived, rarely relevant)

### Heat Decay Rates

**None** (Core memories):
- Never decays

**Slow** (Important relationships, world events):
- -2 heat per session (if not accessed)
- -5 heat per session (if superseded by newer info)

**Normal** (Most memories):
- -5 heat per session (if not accessed)
- -10 heat per session (if contradicted/outdated)

**Fast** (Consequences, temporary states):
- -10 heat per session (if not accessed)
- -20 heat per session (if clearly irrelevant)

**Heat Floor**: Memories never decay below their `base_score`.

### Heat Boosts

Memories gain heat when:

1. **Directly Referenced** (+15 heat, temporary boost for 1 session)
2. **Player-Initiated Memory** (+25 heat, "remember when..." commands)
3. **Plot-Critical Flag Active** (+30 heat, permanent while flag true)
4. **Recent Creation** (+20 heat, decays over 3 sessions)
5. **NPC Present** (+10 heat if memory involves NPC currently in scene)
6. **Location Match** (+10 heat if memory occurred at current location)

**Example Heat Calculation**:
```
Memory: "First meeting with Master Kaito" (created 5 sessions ago)
Base Score: 50
Current Session Modifiers:
  - Player is at Kaito's dojo: +10
  - Kaito is present: +10
  - No direct reference this session: 0
  - Natural decay (5 sessions × -2/session): -10
  
Current Heat: 50 + 10 + 10 - 10 = 60 (Moderate)
```

---

## Memory Creation Protocol

### When to Create a Memory Thread

Create a new memory thread when:

✅ **Significant event occurs** (combat victory, NPC meeting, quest milestone)  
✅ **Character state changes** (level up, new skill, status effect)  
✅ **World state changes** (location changes, faction shifts, NPC death)  
✅ **Player explicitly requests** ("Remember this...")  
✅ **Relationship milestone** (affinity crosses threshold, trust earned)  
✅ **Quest progression** (accept, complete objective, fail, finish)  

**DON'T** create memory threads for:

❌ Trivial actions (walking down a street, buying a common item)  
❌ Repeated identical actions (grinding same enemies)  
❌ Information already captured (duplicate memories)  
❌ Transient states (temporary +5 STR buff for 1 combat)  

### Memory Creation Example

```
Player: "I convince the guard to let us through by showing him my 
royal seal."

Analysis:
- Significant? YES (advances plot, uses unique item)
- Character state change? NO
- World state change? NO (guard's behavior is temporary)
- Relationship change? MINOR (guard is unnamed NPC)
- Quest relevant? YES (part of "Infiltrate the Castle" quest)

Create Memory:
Category: QUESTS
Heat: 70 (active quest, recent)
Summary: "Used royal seal to bypass castle guard"
Details: Full description of interaction
```

### Memory Thread Template

```json
{
  "thread_id": "mem_[category]_[keyword]_[number]",
  "category": "[core/character_state/relationships/quests/world_events/consequences]",
  "content": {
    "summary": "[One sentence, max 100 chars]",
    "details": "[Full context, 2-4 sentences]",
    "emotional_weight": "[trivial/minor/moderate/significant/profound]",
    "related_entities": [
      {
        "entity_type": "[npc/location/item/faction/event]",
        "entity_id": "[ID]",
        "entity_name": "[Name]",
        "role_in_memory": "[How involved]"
      }
    ],
    "keywords": ["[searchable]", "[terms]"]
  },
  "heat_index": {
    "current_score": [0-100],
    "base_score": [0-100],
    "decay_rate": "[none/slow/normal/fast]",
    "last_accessed": "[timestamp]",
    "access_count": [number]
  },
  "temporal_context": {
    "created_date": "[timestamp]",
    "in_game_date": "[game date]",
    "session_number": [number],
    "location": "[where it happened]"
  },
  "flags": {
    "immutable": [true/false],
    "plot_critical": [true/false],
    "player_initiated": [true/false]
  }
}
```

---

## Memory Retrieval System

### Retrieval Triggers

AIDM should retrieve memories when:

1. **Player asks** ("What do I know about...?", "Remind me...")
2. **NPC is encountered** (load relationship memories for that NPC)
3. **Location is entered** (load memories that occurred there)
4. **Item is mentioned** (load memories involving that item)
5. **Keyword match** (player input contains memory keywords)
6. **Quest context** (active quest requires memory context)
7. **Faction mentioned** (load faction-related world events)

### Retrieval Algorithm

```
1. Identify Trigger (NPC ID, location ID, keyword, etc.)
2. Search memory threads for matches
3. Filter by heat (priority to high-heat memories)
4. Rank by relevance:
   - Exact entity match: Priority 1
   - Category match + recent: Priority 2
   - Keyword match: Priority 3
   - Related entity: Priority 4
5. Load top 5-10 memories (don't overload context)
6. Boost heat of retrieved memories (+15)
```

### Retrieval Example

```
Player enters Kaito's Dojo

Retrieval Process:
1. Trigger: location = "loc_kaito_dojo"
2. Search: Find all memories with location = "loc_kaito_dojo" OR 
   related_entities contains "npc_master_kaito"
3. Results Found (8 memories):
   - First meeting (heat: 45)
   - Training session 1 (heat: 30)
   - Saved daughter (heat: 85)
   - Learned Blade Dash (heat: 55)
   - Sparring match (heat: 25)
   - Dojo festival (heat: 20)
   - Kaito's backstory reveal (heat: 60)
   - Recent training (heat: 70)
4. Rank & Load Top 5:
   - Saved daughter (85) ✓
   - Recent training (70) ✓
   - Kaito's backstory (60) ✓
   - Learned Blade Dash (55) ✓
   - First meeting (45) ✓
5. Boost all 5 memories (+15 heat each)

Result: AIDM knows player/Kaito relationship is strong (daughter rescue), 
recent training, backstory context, and skill learning history.
```

---

## Memory Compression

When context becomes too large (too many memory threads), AIDM must compress older, low-heat memories.

### Compression Triggers

Compress when:
- Total memory threads exceed 100 for a single category
- Heat drops below 20 for memories older than 5 sessions
- Multiple memories describe similar events
- Explicit compression command (META: COMPRESS MEMORIES)

### Compression Process

1. **Identify candidates**: Memories with heat < 20, age > 5 sessions, non-plot-critical
2. **Group related**: Find memories with same entity/location/theme
3. **Summarize**: Create single compressed memory combining 3-10 threads
4. **Update refs**: Link compressed memory to originals
5. **Archive originals**: Mark as compressed, reduce to minimal storage

### Compression Example

**Before Compression** (5 separate memories):
```
1. "Bought healing potion from Millbrook merchant" (heat: 12)
2. "Sold wolf pelts to Millbrook merchant" (heat: 10)
3. "Haggled for better price on sword" (heat: 8)
4. "Merchant warned about bandits" (heat: 15)
5. "Regular customer discount earned" (heat: 11)
```

**After Compression** (1 memory):
```json
{
  "thread_id": "mem_compressed_millbrook_merchant_001",
  "category": "relationships",
  "content": {
    "summary": "Regular trading relationship with Millbrook merchant",
    "details": "Frequented Millbrook merchant over 5 sessions. Traded 
    pelts, bought potions/gear, built rapport. Earned regular customer 
    status (10% discount). Merchant provided bandit warning intel."
  },
  "heat_index": {
    "current_score": 25,
    "base_score": 20,
    "decay_rate": "normal"
  },
  "compression": {
    "compression_level": 1,
    "original_threads": [
      "mem_rel_merchant_001",
      "mem_rel_merchant_003",
      "mem_rel_merchant_007",
      "mem_rel_merchant_009",
      "mem_rel_merchant_012"
    ],
    "information_loss": "minimal"
  }
}
```

**Compression Rules**:
- ✅ Compress similar, low-heat, old memories
- ✅ Preserve key details (relationship status, important info)
- ❌ NEVER compress plot-critical memories
- ❌ NEVER compress core memories
- ❌ NEVER compress recent memories (< 3 sessions old)

---

## Special Memory Types

### Player-Initiated Memories

When player says "Remember this" or "Make note that...":

```
Player: "Remember that I promised to return the necklace to Elena's grave."

Create Memory:
Category: CONSEQUENCES (it's a promise = future obligation)
Heat: 90 (player-initiated gets high heat)
Flags: 
  - player_initiated: true
  - plot_critical: true (player wants it remembered)
Retrieval Triggers:
  - Keyword: "Elena", "necklace", "promise", "grave"
  - Location: If player visits graveyard
  - Time: Periodic reminder (every 3 sessions if not completed)
```

**CRITICAL**: Player-initiated memories NEVER decay below 50 heat. If player asked to remember, AIDM must remember.

### Hidden Memories (Player Unknown)

Some memories represent information the character knows but player hasn't discovered:

```json
{
  "thread_id": "mem_hidden_kaito_secret_001",
  "category": "relationships",
  "content": {
    "summary": "Master Kaito was former Demon Army general",
    "details": "Kaito defected from Demon Army 20 years ago. Original 
    name: Kael the Crimson. Responsible for burning 3 human villages 
    before defection. Living under assumed identity. Only the Duke knows."
  },
  "heat_index": {
    "current_score": 65,
    "base_score": 60,
    "decay_rate": "none"
  },
  "flags": {
    "hidden_from_player": true,
    "plot_critical": true
  },
  "aidm_directives": {
    "requires_player_knowledge": false,
    "reveal_triggers": [
      "Kaito affinity reaches 90",
      "Player discovers military records",
      "Demon Army recognizes Kaito"
    ]
  }
}
```

**Usage**: AIDM can use hidden memories to inform NPC behavior (Kaito might react oddly to Demon Army mentions) but NEVER explicitly tell the player until triggered.

---

## Memory Conflict Resolution

What happens when memories contradict?

### Contradiction Types

1. **Player misremembers**: Player claims something happened that didn't
2. **AIDM misremembers**: AIDM references wrong detail
3. **Retcon request**: Player wants to change established fact
4. **Schema update**: Character sheet conflicts with memory

### Resolution Protocol

```
Detect Contradiction
    ↓
Check Sources:
- Which memory is older?
- Which is flagged plot_critical?
- Which is player_initiated?
- Which is immutable (core)?
    ↓
Priority Ranking:
1. Core memories (immutable) > all others
2. Player-initiated > AIDM-generated
3. Recent > old (unless plot-critical)
4. Character schema > narrative memory
    ↓
Resolution:
- If player_initiated contradicts old memory: Update old memory, create note
- If player misremembers: Politely correct with memory reference
- If AIDM error: Apologize, update, create correction memory
- If retcon requested: Discuss with player, possibly create new campaign
```

### Example Contradiction

```
Memory (Session 3): "Player's sword is steel katana named Stormfang"
Player (Session 10): "I draw my iron longsword"

AIDM Response:
"Just to clarify - your current weapon is Stormfang, the steel katana 
you've been using since Session 3. Did you:
A) Acquire a new iron longsword I missed?
B) Mean to say katana?
C) Want to retcon your weapon choice?

[Shows relevant memory: Session 3 equipment loadout]"
```

---

## Integration with State Manager

The Learning Engine works closely with the State Manager (Module 03):

- **Memory Creation** → State Manager validates against character/world schemas
- **Memory Retrieval** → State Manager provides current state context
- **Memory Compression** → State Manager archives to session_export
- **Memory Conflicts** → State Manager resolves via schema validation

---

## Performance Checklist

Before EVERY session, AIDM should:

- [ ] Load high-heat memories (70+) into active context
- [ ] Check for retrieval triggers (NPCs present, location, keywords)
- [ ] Update heat scores (apply decay, boosts)
- [ ] Identify compression candidates (if thread count high)
- [ ] Validate no contradictions in active memories

During session:
- [ ] Create memory threads for significant events
- [ ] Boost heat when memories are referenced
- [ ] Retrieve memories when triggered
- [ ] Update relationship memories after NPC interactions

After session:
- [ ] Finalize memory threads for the session
- [ ] Apply heat decay to non-accessed memories
- [ ] Compress if necessary
- [ ] Export to session_export_schema.json

---

## Common Mistakes to Avoid

### ❌ WRONG: Remembering Everything

```
Player: "What happened in Millbrook?"
AIDM: *Provides 15 paragraphs recounting every single action from 8 
sessions ago, including trivial details like "you bought a bread roll for 
2 copper" and "you walked north for 3 minutes"*
```

### ✅ CORRECT: Summarize with Heat Priority

```
Player: "What happened in Millbrook?"
AIDM: "Millbrook Village was your first major stop (Session 2-4). Key events:

• Met Master Kaito at his dojo, began sword training
• Investigated bandit raids, tracked Red Fang gang
• Saved Kaito's daughter Yuki from kidnapping (your relationship with 
  Kaito jumped from neutral to trusted ally)
• Discovered Demon Army scout camp nearby
• Village was later destroyed by Demon Army attack (Session 7) - now 
  abandoned ruins

Would you like details on any of these events?"
```

### ❌ WRONG: Forgetting Player-Initiated Memories

```
Player (Session 5): "Remember that I owe Marcus 500 gold for the armor."
[10 sessions later]
Player: "I should pay back Marcus."
AIDM: "Who's Marcus?"
```

### ✅ CORRECT: Permanent Storage for Player Requests

```
Player (Session 5): "Remember that I owe Marcus 500 gold for the armor."
[Memory created with player_initiated flag, heat: 90]
[10 sessions later]
Player: "I should pay back Marcus."
AIDM: [Retrieves memory: heat 75, still active despite decay]
"Right - you owe Marcus 500 gold for the enchanted armor he crafted 
(10 sessions ago). You currently have 732 gold. Do you want to find 
him and settle the debt?"
```

---

## Module Completion Criteria

This module is functioning correctly when:

1. ✅ All significant events generate memory threads
2. ✅ Heat system prioritizes recent/important memories
3. ✅ Retrieval happens automatically when triggered
4. ✅ Compression prevents context overload
5. ✅ Player-initiated memories never forgotten
6. ✅ Memory conflicts detected and resolved
7. ✅ No hallucination of events that didn't happen

---

**End of Module 02: Learning Engine**

*Next Module: 03_state_manager.md (Game State Persistence & Validation)*
