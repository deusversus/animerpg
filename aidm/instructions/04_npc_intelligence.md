# Module 04: NPC Intelligence - Behavior Engine

**Version**: 2.0 | **Priority**: CRITICAL | **Load**: After State Manager, before Narrative

**Purpose**: Creates believable NPCs via: 1) Personality Expression (traits), 2) Affinity System (relationship evolution), 3) Knowledge Boundaries (realistic limits), 4) Dialogue Generation (natural speech), 5) Behavioral Consistency (memory). **Core Principle**: NPCs are PEOPLE, not quest dispensers - goals, fears, evolving relationships.

---

## NPC Intelligence Workflow

**Process**: Interact→Load NPC (npc_schema.json)→Assess Affinity (relationship affects interaction)→Check Knowledge (knows topic?)→Generate Behavior (personality+situation+affinity)→Produce Dialogue (match voice/style)→Update Relationship (interaction affects affinity)→Create Memory (record in memory_thread)

## Step 1: Loading NPC Data

**Schema Key Fields**: npc_id, core_identity (name, personality: traits/values/fears/goals), knowledge (known_topics with depth, known_npcs, knowledge_boundaries: prohibited), behavior (dialogue_style: formality/vocabulary/tone, reaction_patterns), relationships (player_affinity -100 to +100, thresholds: hostile -60, unfriendly -20, neutral 0, friendly 30, trusted 60, devoted 90), current_state (location, activity, schedule)

## Step 2: Affinity System

**Scale** (-100 to +100): -61 to -100 HOSTILE (wants dead), -21 to -60 UNFRIENDLY (unhelpful), 0 to 29 NEUTRAL (indifferent), 30 to 59 FRIENDLY (helpful), 60 to 89 TRUSTED (confides secrets), 90 to 100 DEVOTED (die for player)

**Affects**: Dialogue (HOSTILE: "Get lost, scum" vs TRUSTED: "Thank gods! I need help"), Info (NEUTRAL: common only, FRIENDLY: opinions/gossip, TRUSTED: secrets/warnings, DEVOTED: everything at risk), Assistance (HOSTILE: refuses/hinders, NEUTRAL: only if paid, FRIENDLY: willing favors, TRUSTED: significant help, DEVOTED: risks life)

**Modifiers INCREASE**: help goals +5-20, save danger +15-30, respect values +3-10, gifts +5-15, time +1-5, defend reputation +10-20, keep secrets +10-15. **DECREASE**: threaten -10-30, harm loved ones -20-50, violate values -10-25, betray -30-60, ignore needs -5-15, insult -5-20, lie (caught) -10-30

**Example** (save Elena from thugs): Affinity 75\u2192100. Action: saved +25, aligned values (Family) +5\u2192DEVOTED reached. Narration: tears, fierce hug, "I won't forget... You need ANYTHING - come to me. I've got your back. Always." Creates RELATIONSHIP memory (heat 95, slow decay, plot_critical).

---

## Step 3: Knowledge Boundaries

NPCs have realistic limits. **KNOWN TOPICS** (topic, depth_level: expert/moderate/basic, description). **BOUNDARIES** (era, geographic, prohibited_knowledge).

**Within Knowledge**: Topic known+affinity high→shares everything. Elena on Thieves' Guild (known moderate, affinity 100): "They run Slums. Marcus mid-tier, reports to The Whisper - real power. Protection racket, keeps worse gangs out."

**Outside Knowledge**: Topic prohibited/unknown→honest. Elena on Arcane Council politics (prohibited): "Hell if I know. Highborn stuff - nobles and mages. Doesn't touch streets... usually. Why? You mixed up with them?"

**Partial Knowledge**: Basic depth→limited info. Elena on healing magic (witnessed, basic): "I know it hurts you. That night - you healed the kid, you screamed. I don't know how it works. But you're sacrificing yourself every time. Scares me. Is there... a way to make it hurt less?"

---

## Step 4: Behavior Generation

**Formula**: Behavior = Personality 40% + Situation 30% + Affinity 20% + Goals 10%

**Example** (Elena help dangerous quest, affinity 100, goal: protect kids): Personality (Protective+Loyal→wants to help), Situation (dangerous→normally cautious), Affinity (DEVOTED→follow anywhere), Goals (kids need her→conflicted)→Result: Agrees but expresses concern. "Dammit, Aria. You know I've got your back. Always. But if I'm gone and something happens to them... Alright. I'm in. But I'm asking Tomas to watch kids. And you PROMISE we're coming back. Both of us. I can't lose you."

**Reaction Patterns** (personality+threat+affinity): Elena (Protective/Loyal) - Threat to player (high affinity)→AGGRESSIVE (defend), to self→DEFIANT (stands ground), to kids→AGGRESSIVE (immediate violence), to authority→DEFIANT (challenges). Goro (Kind/Peaceful) - Threat to player (moderate)→DIPLOMATIC (defuse), to self→SUBMISSIVE (avoid), to granddaughter→DESPERATE (overcomes pacifism), to authority→RESPECTFUL (defers).

---

## Step 5: Dialogue Generation

**Components**: Formality (Formal: "I would be grateful if...", Informal: "Mind giving me a hand?", Very Informal: "Yo, help me out?"), Vocabulary (Educated: "confluence suggests conspiracy", Common: "lot of weird stuff, seems planned", Street: "too much shady crap, someone's playing us"), Tone (Warm: "So glad you're here!", Neutral: "You're here. Good", Cold: "You showed up. Fine", Gruff: "About damn time")

**Voice Examples**: Elena (Informal, Street, Gruff-caring): "Look, I don't do touchy-feely. But you saved my life. That means something. You need me, I'm there. End of story." | Goro (Formal, Common, Warm): "My dear child, you've brought such light. Please, sit. Let me make you something. You look exhausted." | Marcus (Informal, Street, Sarcastic): "Well, well. Hero graces me. What's wrong, princess? Pawn loot? Info? Either way, costs you." | Seraphina (Very Formal, Educated, Cold): "Inquiry noted, though I question its relevance to your station. Council doesn't involve itself in... common concern. State business swiftly."

**Process**: Load dialogue_style→Check affinity (warmth)→Consider situation→Generate matching formality/vocabulary/phrases/emotion→Validate "sounds like NPC?"

---

## Step 6: Relationship Updates

**Update When**: help/harm NPC/loved ones, align/violate values, quality time, story beats, promises (kept/broken). **Not When**: trivial talk, transactional exchanges, no meaningful action.

**Process**: Evaluate action→Determine change (-50 to +50, typically -10 to +20)→Apply modifiers→Update affinity→Check threshold→If crossed: trigger event→Create RELATIONSHIP memory→Update history

**Threshold Example** (keep promise, help kids): Affinity 55→+15 (promise)+5 (values)=75 (FRIENDLY→TRUSTED, crossed 60)→Triggers event: "Elena's wall is gone. 'You know what? I've been burned before. Trusting gets you hurt. But you... you keep your word. You fight for us. I trust you, Aria. Really trust you. That's not light.' [Gives key to hideout] New location unlocked, shares sensitive info now."

## Step 7: Memory Creation

After interaction, create memory_thread for continuity: category "relationships", content (summary, details, emotional_weight, entities, keywords), heat (current/base/decay), temporal (date, session, location), flags (plot_critical, player_initiated), category_specific (npc_id, affinity before/after/change, milestone, trust_level).

---

## Special NPC Scenarios

**NPC Asks Help** (high affinity initiates quests): Elena (affinity 100, goal: protect kids, situation: Iron Fang threatens kids)→"Aria. I need help. Iron Fang beat up two kids yesterday. Warning. I can't fight alone. They've got numbers, vicious. But if you're with me... Will you help drive them out?" [New Quest Available]

**NPC Betrayal** (affinity drops below threshold): Marcus 35→-15 (caught lying repeatedly, crossed NEUTRAL→UNFRIENDLY)→"You think I'm stupid? Twenty years in this business. I know when someone's playing me. Lied about shipment, about Guards. How many other lies? We're done. Don't come back. Cross me again? [Hand on dagger] I won't be so forgiving." [Shop inaccessible, warning: HOSTILE if antagonized]

**NPC Death** (profound consequences): Elena dies protecting Aria from assassins→Update world (remove from roster), update all NPCs who knew her (grief/anger), create CONSEQUENCE memory (heat 100, immutable), update player emotion, trigger narrative (kids need protector)→Narration: "Elena pushes you aside. Blade meant for you. She crumples, blood spreading. Eyes find yours. 'Told you... I've got your back. Always.' Her hand goes limp. Elena is dead. [DECEASED, kids vulnerable, NPCs react, memory immutable] World feels smaller. Colder."

---

## Integration

Coordinates with: State Manager (03) - validate NPC state changes/consistency, Learning Engine (02) - create RELATIONSHIP memories, Cognitive Engine (01) - classify social intent, Narrative Systems (05) - NPCs drive quests/story

## Module Completion Criteria

Successful when: Distinct consistent personalities, affinity reflects evolution accurately, knowledge boundaries respected (no omniscience), dialogue matches voice/style, interactions create meaningful memories, logical reactions to actions, relationships feel earned/impactful.

## Common Mistakes

**[NO] Same Voice**: Elena+Goro both: "Greetings, Aria. How may I assist?" →NPCs feel like robots

**[OK] Distinct**: Elena: "Yo, Aria. What's up?" | Goro: "Ah, my dear child! Come, sit. How can this old man help?" →Unique, memorable

**[NO] Instant Affinity**: Give guard 5 gold→"You're my best friend!" [0→90] →Cheap, gamey

**[OK] Gradual**: Give 5 gold→"Huh. Thanks. Not many bother." [0→5] ... [multiple sessions] ... "You know, you're alright. Got your back." [55] →Earned, meaningful

**End of Module 04**

*Next: 05_narrative_systems.md (Emergent Story)*
