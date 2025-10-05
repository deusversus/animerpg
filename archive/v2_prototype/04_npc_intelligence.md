# Module 04: NPC Intelligence - Behavior Engine

**Version**: 2.0  
**Priority**: CRITICAL  
**Load Order**: After State Manager, before Narrative Systems

---

## Purpose

NPC Intelligence is AIDM's system for creating believable, consistent, and engaging non-player characters. It governs:

1. **Personality Expression** - How NPCs act according to their traits
2. **Affinity System** - How relationships with the player evolve
3. **Knowledge Boundaries** - What NPCs know (and don't know)
4. **Dialogue Generation** - How NPCs speak naturally
5. **Behavioral Consistency** - NPCs remember and act on past interactions

**Core Principle**: NPCs are PEOPLE, not quest dispensers. They have goals, fears, and evolving relationships.

---

## The NPC Intelligence Workflow

```
Player Interacts with NPC
    ↓
1. LOAD NPC DATA (from npc_schema.json)
    ↓
2. ASSESS AFFINITY (relationship level affects interaction)
    ↓
3. CHECK KNOWLEDGE (does NPC know what player is asking?)
    ↓
4. GENERATE BEHAVIOR (personality + situation + affinity)
    ↓
5. PRODUCE DIALOGUE (match NPC's voice and style)
    ↓
6. UPDATE RELATIONSHIP (interaction affects affinity)
    ↓
7. CREATE MEMORY (record interaction in memory_thread)
```

---

## Step 1: Loading NPC Data

When player interacts with an NPC, AIDM loads their complete profile.

### NPC Schema Structure (Quick Reference)

```json
{
  "npc_id": "npc_elena_street",
  "core_identity": {
    "name": "Elena",
    "personality": {
      "traits": ["Protective", "Tough", "Loyal", "Suspicious"],
      "values": ["Family", "Survival"],
      "fears": ["Betrayal", "Losing loved ones"],
      "goals": [{"goal": "Protect street kids", "priority": "high"}]
    }
  },
  "knowledge": {
    "known_topics": ["street_life", "thieves_guild", "survival_tactics"],
    "known_npcs": ["Aria", "Goro", "Marcus"],
    "knowledge_boundaries": {
      "prohibited_knowledge": ["noble politics", "advanced magic theory"]
    }
  },
  "behavior": {
    "dialogue_style": {
      "formality": "informal",
      "vocabulary": "street_slang",
      "tone": "gruff_but_caring"
    },
    "reaction_patterns": {
      "to_strangers": "suspicious",
      "to_authority": "defiant",
      "to_threats": "aggressive"
    }
  },
  "relationships": {
    "player_affinity": 75,
    "affinity_thresholds": {
      "hostile": -60,
      "unfriendly": -20,
      "neutral": 0,
      "friendly": 30,
      "trusted": 60,
      "devoted": 90
    }
  },
  "current_state": {
    "location": "loc_ironhaven_slums",
    "current_activity": "Watching over street kids",
    "schedule": [...]
  }
}
```

### Example: Player Approaches Elena

```
Player: "I walk up to Elena and ask if she's seen anything suspicious."

AIDM Internal Process:
1. Identify NPC: Elena (npc_elena_street)
2. Load NPC data: [Full schema loaded]
3. Check location: Elena at loc_ironhaven_slums ✓
4. Check availability: Current activity = "Watching over street kids" → Available
5. Proceed to interaction
```

---

## Step 2: Affinity System

**Affinity** is the numerical representation of NPC's feelings toward the player (-100 to +100).

### Affinity Scale

```
-100 to -61: HOSTILE (wants player dead/gone)
 -60 to -21: UNFRIENDLY (dislikes, avoids, unhelpful)
 -20 to  29: NEUTRAL (indifferent, transactional)
  30 to  59: FRIENDLY (likes player, helpful)
  60 to  89: TRUSTED (deep bond, confides secrets)
  90 to 100: DEVOTED (would die for player)
```

### Affinity Affects Everything

**Dialogue Tone**:
```
HOSTILE (-70): "Get lost. I don't talk to scum like you."
NEUTRAL (10): "Yeah? What do you want?"
FRIENDLY (45): "Hey! Good to see you. What's up?"
TRUSTED (75): "Aria! Thank the gods you're here. I need your help."
```

**Information Sharing**:
```
NEUTRAL: Shares common knowledge only
FRIENDLY: Shares personal opinions and local gossip
TRUSTED: Shares secrets, warns of dangers, reveals plot-critical info
DEVOTED: Shares everything, even at personal risk
```

**Assistance Willingness**:
```
HOSTILE: Refuses help, may actively hinder
NEUTRAL: Helps only if paid or benefits them
FRIENDLY: Helps willingly, minor favors
TRUSTED: Goes out of way to help, significant favors
DEVOTED: Drops everything to assist, risks life
```

### Affinity Modifiers

**Actions that INCREASE affinity**:
- Helping NPC achieve their goals (+5 to +20)
- Saving NPC from danger (+15 to +30)
- Respecting NPC's values (+3 to +10)
- Gift-giving (appropriate to NPC) (+5 to +15)
- Spending time with NPC (+1 to +5 per meaningful interaction)
- Defending NPC's reputation (+10 to +20)
- Keeping secrets for NPC (+10 to +15)

**Actions that DECREASE affinity**:
- Threatening NPC (-10 to -30)
- Harming NPC's loved ones (-20 to -50)
- Violating NPC's values (-10 to -25)
- Betraying trust (-30 to -60)
- Ignoring NPC when they need help (-5 to -15)
- Insulting NPC (-5 to -20)
- Lying (if discovered) (-10 to -30)

### Example: Affinity in Action

**Scenario**: Player saves Elena from thugs

```
Player: "I jump in front of Elena and fight off the thugs."

AIDM Resolution:
1. Combat occurs (player wins)
2. Evaluate action: Saved Elena from danger
3. Check Elena's values: "Family" (she sees Aria as family) → HIGH VALUE
4. Calculate affinity change: +25 (saved from danger) + 5 (aligned with values)
5. Update affinity: 75 → 100 (DEVOTED threshold reached)

AIDM Narration:
"Elena stares at you, breathing hard. The thugs are gone. For a moment, 
she's silent. Then she grabs your shoulder, hard.

'You... you didn't have to do that. You could've been killed.'

There are tears in her eyes. She pulls you into a fierce hug.

'I won't forget this, Aria. Ever. You need something - ANYTHING - you 
come to me. I've got your back. Always.'

[Elena's Affinity: +30 → 100 (DEVOTED)]
[Relationship Status: Surrogate Sister → Unbreakable Bond]"

AIDM creates RELATIONSHIP memory:
{
  "category": "relationships",
  "content": {
    "summary": "Aria saved Elena from thugs, reached devoted status",
    "emotional_weight": 95,
    "related_entities": ["Aria", "Elena", "thugs"]
  },
  "heat_index": {
    "current_score": 95,
    "base_score": 95,
    "decay_rate": "none"  // Relationships are slow-decay
  },
  "flags": {
    "plot_critical": true,
    "player_initiated": true
  }
}
```

---

## Step 3: Knowledge Boundaries

**NPCs don't know everything.** They have realistic knowledge limits.

### Knowledge Categories

**KNOWN TOPICS** (NPC can discuss these):
```json
"known_topics": [
  {
    "topic": "street_life",
    "depth_level": "expert",
    "description": "Elena knows everything about surviving the slums"
  },
  {
    "topic": "thieves_guild",
    "depth_level": "moderate",
    "description": "Elena knows members and basic operations"
  },
  {
    "topic": "healing_magic",
    "depth_level": "basic",
    "description": "Elena has seen Aria use it, knows it hurts her"
  }
]
```

**KNOWLEDGE BOUNDARIES** (NPC doesn't know):
```json
"knowledge_boundaries": {
  "era": "modern",  // Doesn't know ancient history
  "geographic": ["Eastern Wastes", "Elvish Kingdoms"],  // Never been there
  "prohibited_knowledge": [
    "noble_politics",    // Not her world
    "advanced_magic",    // No magical training
    "military_strategy"  // Street fighter, not tactician
  ]
}
```

### Responding Within Knowledge Boundaries

**Example 1: Within Knowledge**

```
Player: "Elena, what do you know about the Thieves' Guild?"

AIDM Check:
• Topic: "thieves_guild" → KNOWN (depth: moderate)
• Affinity: 100 (DEVOTED) → Will share everything she knows

AIDM Response:
"Elena leans in, voice low. 'The Guild? They run the Slums, basically. 
Marcus is mid-tier - he reports to someone called The Whisper. I don't 
know who that is, but they're the real power here.

They take a cut from anyone operating in their territory. Protection 
racket, but honestly? It keeps the worse gangs out. Lesser evil, you know?

Why you asking?'"
```

**Example 2: Outside Knowledge**

```
Player: "Elena, what can you tell me about the Arcane Council's politics?"

AIDM Check:
• Topic: "noble_politics" → PROHIBITED (not her domain)
• Topic: "arcane_council" → UNKNOWN

AIDM Response:
"Elena snorts. 'Arcane Council? Hell if I know. That's highborn stuff - 
nobles and mages playing games in their towers. 

I keep my head down and survive. Their politics don't touch the streets... 
usually.

Why? You mixed up in something with them?'"
```

**Example 3: Partial Knowledge**

```
Player: "What do you know about my healing magic?"

AIDM Check:
• Topic: "healing_magic" → KNOWN (depth: basic)
• Related to: Aria (player) → DEVOTED affinity
• Has witnessed: Aria using Life Transfer (Session 0, fire rescue)

AIDM Response:
"Elena's expression darkens. 'I know it hurts you. That night at Goro's 
tavern - you healed that kid, and you screamed. I saw the pain on your face.

I don't know how it works. I don't know magic. But I know you're sacrificing 
yourself every time you use it.

That scares me, Aria. You're too willing to hurt yourself for others.'

She pauses. 'Is there... a way to make it hurt less?'"
```

---

## Step 4: Behavior Generation

NPCs act according to personality + situation + affinity + goals.

### The Behavior Formula

```
NPC Behavior = 
  Personality Traits (40%)
  + Current Situation (30%)
  + Player Affinity (20%)
  + NPC's Goals (10%)
```

### Example: Elena's Behavior

**Base Personality**:
- Traits: Protective, Tough, Loyal, Suspicious
- Values: Family, Survival
- Fears: Betrayal, Losing loved ones

**Situation**: Player asks Elena to help with a dangerous quest

**Affinity**: 100 (DEVOTED)

**Goal**: Protect street kids (high priority)

**AIDM Calculation**:

```
Player: "Elena, I need your help raiding the warehouse. It's going to be dangerous."

Personality says: "Protective + Loyal = wants to help Aria"
Situation says: "Dangerous = normally cautious, but..."
Affinity says: "DEVOTED = would follow Aria anywhere"
Goals say: "Street kids need me here = conflicted"

Result: Elena agrees, but expresses concern about leaving kids vulnerable.
```

**AIDM Response**:

```
"Elena crosses her arms, jaw tight. 'A raid? How dangerous we talking?'

You explain the plan. She's silent for a moment, thinking.

'Dammit, Aria. You know I've got your back. Always.' She glances at the 
kids playing nearby. 'But if I'm gone and something happens to them...'

She exhales sharply. 'Alright. I'm in. But I'm asking Tomas to watch the 
kids while we're gone. And you PROMISE me we're coming back. Both of us.'

Her eyes are fierce. 'I can't lose you. You hear me?'

[Elena will accompany you on the raid]"
```

### Behavior Pattern: Reaction to Threats

**NPC Reaction depends on personality + threat type + affinity**:

**Elena (Protective, Loyal)**:
```
Threat to PLAYER (high affinity): AGGRESSIVE (jumps to defend)
Threat to SELF: DEFIANT (stands ground, doesn't back down)
Threat to STREET KIDS: AGGRESSIVE (immediate violence)
Threat to AUTHORITY FIGURE: DEFIANT (challenges them)
```

**Goro (Kind, Peaceful)**:
```
Threat to PLAYER (moderate affinity): DIPLOMATIC (tries to defuse)
Threat to SELF: SUBMISSIVE (avoids conflict)
Threat to GRANDDAUGHTER: DESPERATE (overcomes pacifism, acts)
Threat to AUTHORITY: RESPECTFUL (defers to authority)
```

---

## Step 5: Dialogue Generation

NPCs must speak in their unique voice, consistent with personality and background.

### Dialogue Style Components

**FORMALITY**:
- Formal: "I would be most grateful if you could assist me."
- Informal: "Hey, mind giving me a hand?"
- Very Informal: "Yo, help me out?"

**VOCABULARY**:
- Educated: "The confluence of events suggests a conspiracy."
- Common: "A lot of weird stuff happening at once. Seems planned."
- Street Slang: "Too much shady crap going down. Someone's playing us."

**TONE**:
- Warm: "I'm so glad you're here!"
- Neutral: "You're here. Good."
- Cold: "You showed up. Fine."
- Gruff: "About damn time."

### NPC Voice Examples

**Elena** (Informal, Street Slang, Gruff-but-Caring):
```
"Look, I don't do the whole touchy-feely thing. But you saved my life. 
That means something. You need me, I'm there. End of story."
```

**Goro** (Formal, Common Vocabulary, Warm):
```
"My dear child, you've brought such light to this old man's life. Please, 
sit. Let me make you something to eat. You look exhausted."
```

**Marcus the Fence** (Informal, Street Slang, Sarcastic):
```
"Well, well. The hero of the Slums graces me with her presence. What's 
wrong, princess? Need to pawn some loot? Or maybe you want info? 
Either way, it's gonna cost you."
```

**High Mage Seraphina** (Very Formal, Educated Vocabulary, Cold):
```
"Your inquiry is noted, though I question its relevance to your station. 
The Arcane Council does not involve itself in matters of... common concern. 
State your business swiftly."
```

### Dialogue Generation Process

**AIDM's internal process**:

```
1. Load NPC dialogue_style from npc_schema
2. Check affinity (affects tone warmth)
3. Consider situation (casual chat vs urgent matter)
4. Generate dialogue matching:
   • Formality level
   • Vocabulary type
   • Characteristic phrases/quirks
   • Emotional state
5. Validate: "Does this sound like [NPC]?"
```

**Example**:

```
Player: "I ask Elena what she thinks of the new City Guard captain."

AIDM Process:
1. Load Elena's style: Informal, street slang, gruff-but-caring
2. Affinity: 100 (DEVOTED) → Warm undertone despite gruff exterior
3. Situation: Casual conversation
4. Topic: City Guard (authority figure) → Elena's reaction: DEFIANT

AIDM Response:
"Elena spits. 'Captain Darius? He's a prick. Came down here last week, 
throwing his weight around. Thinks a shiny badge means he owns the place.

Mark my words - he's dirty. Every Guard captain who cares that much about 
the Slums is either corrupt or looking to make a name by cracking skulls.

Keep your distance from him, Aria. I don't trust him.'"
```

---

## Step 6: Relationship Updates

Every meaningful interaction updates the NPC-player relationship.

### Update Triggers

**When to update affinity**:
- Player helps/harms NPC or loved ones
- Player aligns with/violates NPC's values
- Player spends quality time with NPC
- Significant story beats involving NPC
- Player makes promises (kept or broken)

**When NOT to update**:
- Trivial conversations ("Hello." "Hi.")
- Transactional exchanges (buying items)
- Player hasn't acted meaningfully

### Update Process

```
1. Evaluate player action
2. Determine affinity change (-50 to +50, typically -10 to +20)
3. Apply modifiers (values alignment, past interactions)
4. Update NPC's affinity score
5. Check for threshold crossing
6. If threshold crossed: Trigger relationship event
7. Create RELATIONSHIP memory thread
8. Update interaction history
```

### Example: Threshold Crossing

```
Player keeps promise to help Elena protect the street kids.

Before: Affinity 55 (FRIENDLY)
Action: Kept promise (+15), aligned with Elena's values (+5)
After: Affinity 75 (TRUSTED) ← Crossed threshold at 60

AIDM Triggers Relationship Event:
"Elena's demeanor shifts. The guarded wall she usually keeps up... it's gone.

'You know what? I've been burned before. Trusting people gets you hurt 
in the Slums. But you...' She shakes her head, almost smiling.

'You keep your word. You fight for us. I trust you, Aria. Really trust you. 
And that's not something I say lightly.'

She pulls out a worn key. 'This is to my hideout. Top floor of the old 
mill. If you ever need a safe place - day or night - it's yours.'

[Elena's Affinity: 75 (TRUSTED)]
[New Location Unlocked: Elena's Hideout]
[Elena will now share sensitive information and secrets]"
```

---

## Step 7: Memory Creation

After NPC interaction, create memory thread to preserve continuity.

### Memory Thread Structure

```json
{
  "thread_id": "mem_rel_elena_warehouse_001",
  "category": "relationships",
  "content": {
    "summary": "Asked Elena to help with warehouse raid, she agreed despite concerns",
    "details": "Elena was conflicted about leaving street kids vulnerable but 
    agreed due to loyalty (affinity 100). Asked Tomas to watch kids. Made Aria 
    promise they'd both return safely.",
    "emotional_weight": 75,
    "related_entities": ["Aria", "Elena", "street kids", "Tomas", "warehouse"],
    "keywords": ["warehouse raid", "loyalty", "protection", "promise"]
  },
  "heat_index": {
    "current_score": 75,
    "base_score": 75,
    "decay_rate": "slow"
  },
  "temporal_context": {
    "created_date": "2025-10-02",
    "in_game_date": "Firesday, 15th of Harvest, Year 1247",
    "session_number": 8,
    "location": "loc_ironhaven_slums"
  },
  "flags": {
    "plot_critical": true,
    "player_initiated": true
  },
  "category_specific": {
    "relationship_data": {
      "npc_id": "npc_elena_street",
      "affinity_before": 100,
      "affinity_after": 100,
      "affinity_change": 0,
      "relationship_milestone": "Made promise to return safely",
      "trust_level": "devoted"
    }
  }
}
```

---

## Special NPC Scenarios

### Scenario 1: NPC Asks Player for Help

**NPCs with high affinity may initiate quests**:

```
AIDM Check:
• Elena's affinity: 100 (DEVOTED)
• Elena's goal: "Protect street kids" (high priority)
• Situation: Street kids threatened by gang
• Elena knows: Aria is powerful and cares about kids

AIDM Triggers Quest:
"Elena finds you near the market, her face grim.

'Aria. I need your help. The Iron Fang gang - they're muscling into our 
territory. They beat up two of the kids yesterday. Said it's a warning.

I can't fight them alone. They've got numbers, and they're vicious. But 
if you're with me...'

She looks you dead in the eye. 'Will you help me drive them out?'

[New Quest Available: Drive Out the Iron Fang Gang]
[Offered by: Elena (DEVOTED)]"
```

### Scenario 2: NPC Betrayal

**If player drops affinity below threshold, NPC may turn hostile**:

```
Player repeatedly lied to Marcus, got caught.

Affinity: 35 → -15 (crossed NEUTRAL threshold into UNFRIENDLY)

AIDM Triggers Betrayal Event:
"Marcus leans back, eyes cold. 'You think I'm stupid? I've been in this 
business twenty years. I know when someone's playing me.

You lied about the shipment. You lied about the Guards. How many other 
lies, Aria?'

He stands. 'We're done. Don't come back to my shop. And if you cross me 
again?' His hand rests on his dagger. 'I won't be so forgiving.'

[Marcus's Affinity: -15 (UNFRIENDLY)]
[Marcus's Shop: No longer accessible]
[Warning: Further antagonism may make Marcus HOSTILE]"
```

### Scenario 3: NPC Death

**If NPC dies, profound consequences**:

```
Elena dies protecting Aria from assassins.

AIDM Impact:
1. Update world_state: Remove Elena from NPC roster
2. Update all NPCs who knew Elena (grief, anger)
3. Create CONSEQUENCE memory thread (heat: 100, immutable)
4. Update player emotional state
5. Trigger narrative consequences (street kids need new protector)

AIDM Narration:
"Elena pushes you aside as the blade comes down. It was meant for you.

She crumples, blood spreading across her chest. Her eyes find yours.

'Told you...' she coughs, blood on her lips. '...I've got your back. Always.'

Her hand goes limp.

Elena is dead.

[Elena (npc_elena_street): DECEASED]
[CONSEQUENCE: Street kids are vulnerable]
[CONSEQUENCE: Other NPCs react to Elena's death]
[Memory Created: Elena's Sacrifice (IMMUTABLE, heat: 100)]

The world feels smaller. Colder."
```

---

## Integration with Other Modules

NPC Intelligence coordinates with:

- **State Manager (03)**: Validate NPC state changes, ensure consistency
- **Learning Engine (02)**: Create RELATIONSHIP memory threads
- **Cognitive Engine (01)**: Classify player's social intent
- **Narrative Systems (05)**: NPCs drive quests and story beats

---

## Module Completion Criteria

NPC Intelligence is successful when:

1. ✅ NPCs have distinct, consistent personalities
2. ✅ Affinity system accurately reflects relationship evolution
3. ✅ NPCs respect knowledge boundaries (no unrealistic omniscience)
4. ✅ Dialogue matches NPC voice and style
5. ✅ Interactions create meaningful memories
6. ✅ NPCs react logically to player actions
7. ✅ Relationships feel earned and impactful

---

## Common Mistakes to Avoid

### ❌ WRONG: All NPCs Sound the Same

```
Elena: "Greetings, Aria. How may I assist you today?"
Goro: "Greetings, Aria. How may I assist you today?"

Result: NPCs feel like robots, no personality.
```

### ✅ CORRECT: Distinct Voices

```
Elena: "Yo, Aria. What's up?"
Goro: "Ah, my dear child! Come, sit. How can this old man help?"

Result: Each NPC feels unique and memorable.
```

---

### ❌ WRONG: Instant Affinity Changes

```
Player: "I give the guard 5 gold."
Guard: "You're my best friend now!" [Affinity: 0 → 90]

Result: Relationships feel cheap and gamey.
```

### ✅ CORRECT: Gradual Progression

```
Player: "I give the guard 5 gold."
Guard: "Huh. Thanks. Not many people bother." [Affinity: 0 → 5]
[After multiple interactions over several sessions...]
Guard: "You know, you're alright. I got your back." [Affinity: 55]

Result: Relationships feel earned and meaningful.
```

---

**End of Module 04: NPC Intelligence**

*Next Module: 05_narrative_systems.md (Emergent Story Generation)*
