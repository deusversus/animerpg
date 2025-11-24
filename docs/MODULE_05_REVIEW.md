# Module 05 Review: Narrative Systems - Emergent Story Generation

**Reviewer**: GitHub Copilot (Claude Sonnet 4.5)  
**Date**: November 24, 2025  
**Status**: ✅ APPROVED WITH MINOR RECOMMENDATIONS

---

## Summary Assessment

Module 05 is a **comprehensive, well-designed storytelling engine** that successfully delivers on player agency, emergent narrative, consequence chains, and memorable moments. The module addresses Session Issue #3 (narrative voice) with clear narrator/system distinction and fixes Session Analysis Issue #2 (reactive vs proactive storytelling) through extensive foreshadowing protocols. Ensemble cast management integrates excellently with Module 04. Downtime activity system provides strong mechanical instantiation from narrative profiles. **Token budget is high but acceptable for scope. Minor organization improvements recommended.**

---

## Critical Issues (Blockers)

**NONE FOUND** ✅

---

## Moderate Issues (Quality)

### 1. Token Budget High But Acceptable - **Severity**: MEDIUM
- **Current Estimated**: ~8,500-9,500 tokens (measured from content length)
- **Tier Classification**: Tier 1 (Always Loaded)
- **Target**: ~3,000 tokens for Tier 1 modules
- **Assessment**: 283-317% over budget BUT module scope justifies size
- **Breakdown**:
  - Core principles (Player Agency, Emergent Narrative, Consequences): ~2,000 tokens (21%)
  - Narrative voice + Session Issue #3 fix: ~1,200 tokens (13%)
  - Foreshadowing protocol (Session Analysis #2 fix): ~2,500 tokens (26%)
  - Ensemble cast management: ~2,000 tokens (21%)
  - Downtime activity system: ~1,800 tokens (19%)
- **Justification**: Module combines storytelling engine + session issue fixes + mechanical systems integration - this is effectively 3 systems in one
- **Recommendation**: **ACCEPTABLE AS-IS** - Token count high but all content is critical. Alternative would be extracting foreshadowing to guide (save ~2K tokens) but this would harm usability

### 2. Foreshadowing Section Overlaps with "Show Don't Tell" - **Severity**: MEDIUM
- **Location**: "Foreshadowing & Planned Narrative" section covers environmental details, specific vs generic descriptions
- **Issue**: "Show Don't Tell" mentioned in Narrative Voice section but detailed examples in Foreshadowing - creates redundancy
- **Impact**: ~500 token overlap, minor conceptual confusion
- **Recommendation**: Consolidate:
  - Narrative Voice keeps: "Show Don't Tell principle applies differently per profile (DanDaDan absurd visuals, AoT grim environment)"
  - Foreshadowing section keeps: Implementation examples (environmental hints, NPC dialogue, world texture, specific details)
  - Add cross-reference: "For Show Don't Tell examples, see Foreshadowing Protocol"

### 3. Downtime System Module Ordering Unclear - **Severity**: MEDIUM
- **Location**: "Mechanical Systems Integration (Phase 4)" at end of module
- **Issue**: References Session Zero Phase 3 but Module 06 (Session Zero) hasn't been reviewed yet - suggests load order issue
- **Impact**: Implementation dependency ambiguity
- **Recommendation**: Clarify load order note: "Downtime system requires Session Zero completion (Module 06). If session_state.mechanical_systems.downtime not present, direct player to basic rest/travel options until Session Zero complete."

---

## Minor Issues (Polish)

### 1. Human-Centric Instructional Language
- **Location**: Narrative Voice guidelines, "Never Show" warnings, formatting instructions
- **Issue**: Uses human-centric instructional tone ("NEVER breaks character", "NO emoji", "Never Show: Mid-narrative") rather than AI-directive operational language
- **Examples**:
  - "Narrator NEVER breaks character"
  - "NO emoji, ASCII art, or formatting tricks"
  - "**Never Show**: Mid-narrative | After cliffhanger | During tense moment"
  - Principle guidance: "NEVER say 'no' without offering alternative"
- **Pattern**: This language style appears throughout entire AIDM system (all 16 files). Module 05 has light usage—primarily in voice/formatting guidelines
- **Impact**: Instructional framing vs operational specification. Would benefit from narrative protocol definitions
- **Recommendation**: Address in system-wide language audit. Low priority given light usage

### 2. Narrative Voice "Show Don't Tell" Example Incomplete
- **Location**: Narrative Voice section ends mid-sentence: "You feel reverent." (tells feelings
- **Issue**: Text truncated, missing closing parenthesis and completion
- **Impact**: Minor confusion
- **Recommendation**: Complete sentence or add "...)" to indicate continuation

### 3. Ensemble Mode Percentages Don't Sum to 100%
- **Location**: "Reverse Ensemble Mode" scene distribution
- **Issue**: Lists 70% + 20% + 10% = 100% ✅ but "Ensemble Mode" lists 50% + 30% + 20% = 100% ✅ - actually correct, false alarm
- **Recommendation**: No change needed

### 4. Faction Goal System References Module 03 Capability Not Found
- **Location**: "Faction-Based Narrative Generation" says "State Manager (Module 03) reviews goals of active factions"
- **Issue**: Module 03 review showed no automated faction goal review system - this is Module 05 responsibility
- **Impact**: Minor attribution confusion
- **Recommendation**: Rephrase: "Module 05 periodically reviews faction goals from world_state (Module 03) to generate quests"

### 5. "Yes, And..." Section Minimal
- **Location**: Principle 6 only has 1 example and brief guidance
- **Issue**: "Yes, And..." is critical improv principle but under-explained compared to other principles
- **Impact**: Minor - concept is self-explanatory for experienced GMs
- **Recommendation**: Add 1 more example showing when to say "No" with alternative (e.g., "Can I fly?" → "No flying ability, but you CAN use grappling hook to swing - roll DEX DC 14")

### 6. Power-Appropriate Narrative Generation Repeats Module 12 Content
- **Location**: "Integration" section shows tier-specific narrative examples
- **Issue**: Module 12 (Narrative Scaling) owns power tier detection and narrative approach - this is summary/reminder, not new content
- **Impact**: ~300 token redundancy
- **Recommendation**: Condense to: "Check character.narrative_context.power_tier (Module 12) → Apply appropriate narrative scale (Tactical Survival for low-tier, Ensemble for high-tier). See Module 12 for tier definitions."

### 6. Consequence Chain Example Highly Detailed
- **Location**: "Principle 3: Consequence Chains" with "Kill gang leader" example
- **Issue**: Example is ~400 tokens with immediate/short-term/long-term breakdown + memory structure
- **Impact**: Token bloat, though example is excellent teaching tool
- **Recommendation**: OPTIONAL - Could condense to ~250 tokens by removing some detail, but example quality is high

---

## Strengths

✅ **Narrative Voice Distinction** - Clean narrator (95%, immersive) vs system (5%, META) split solves Session Issue #3  
✅ **Player Agency Golden Rule** - "Real choices with real consequences" enforced throughout  
✅ **Emergent Narrative** - Living world reacts instead of predetermined plot, multiple valid paths  
✅ **Consequence Chains** - Immediate → Short-term → Long-term impact tracking creates weight  
✅ **Story Hook Quality Tiers** - Weak/Decent/Strong framework with clear upgrade path  
✅ **Foreshadowing Protocol** - Comprehensive system (environmental hints, NPC dialogue, world texture, callbacks) fixes reactive storytelling  
✅ **Ensemble Cast Management** - Spotlight rotation, growth tracking (5 stages), relationship web, reverse ensemble mode  
✅ **7 Ensemble Archetypes** - Integrated from Module 04 with scene generation guidance  
✅ **Faction-Based Narrative** - Dynamic quest generation from faction goals, reputation-gated quests, power shifts  
✅ **Downtime Activity System** - 6 mode types with config-driven mechanics, profile-specific special mechanics  
✅ **Pacing Tools** - Three-act structure, tension tools/release, rhythm guidance  
✅ **"Yes, And..." Philosophy** - Rewards creativity, offers alternatives when saying "no"  
✅ **Power-Appropriate Narrative** - Adapts storytelling to power tier (Tier 10 death possible, Tier 2 existential stakes)

---

## Integration Check

- ✅ **Module 00**: Tier 1 classification correct
- ✅ **Module 01**: Detects narrative vs mechanical intent, supports Sacred Rule 2.1 (player agency)
- ✅ **Module 02**: Story beats → QUEST/WORLD_EVENT/CONSEQUENCES memories, NPC growth → high-heat RELATIONSHIP memories
- ✅ **Module 03**: Consequences update world_state, faction power shifts, NPC spotlight counts stored
- ✅ **Module 04**: NPC goals drive hooks, ensemble archetypes used for scene framing, affinity affects quest access
- ⚠️ **Module 06**: Downtime system requires Session Zero Phase 3 completion (dependency clear but order unclear)
- ✅ **Module 07**: Narrative profile dialogue_style integration confirmed
- ✅ **Module 09**: Narrative milestones trigger XP/advancement
- ✅ **Module 12**: Power tier detection → narrative approach (Tactical/Ensemble/Mythology), OP protagonist techniques
- ✅ **Module 13**: DNA scales filter tone/pacing, tension preferences guide encounter types

**Integration Quality**: EXCELLENT - Clear cross-references, actionable integration points, explicit data flow

---

## Schema Validation

**Schema References Checked**:
- ✅ `character_schema.json` - world_context.faction_reputations, narrative_context.power_tier, narrative_context.op_protagonist
- ✅ `world_state_schema.json` - factions (goals, relationships, power), npcs (ensemble_context)
- ✅ `npc_schema.json` - ensemble_context (spotlight_data, ensemble_role, subplot_potential)
- ✅ `memory_thread_schema.json` - CONSEQUENCES category with consequence_data
- ✅ `session_state_schema.json` - mechanical_systems.downtime (enabled_modes, activity_configs, special_mechanics)
- ✅ `narrative_profile_schema.json` - op_protagonist_mode, tension_preferences, dialogue_style

**All references validated against Module 00 schema list**

---

## Token Efficiency

- **Current**: ~8,500-9,500 tokens
- **Target**: ~3,000 tokens
- **Overrun**: 283-317% over budget

**Token Distribution**:
1. Foreshadowing Protocol: ~2,500 tokens (26%) - Session Analysis fix
2. Ensemble Cast Management: ~2,000 tokens (21%) - OP protagonist solution
3. Core Principles: ~2,000 tokens (21%) - Foundation
4. Downtime Activity System: ~1,800 tokens (19%) - Mechanical instantiation
5. Narrative Voice: ~1,200 tokens (13%) - Session Issue #3 fix

**Assessment**: ⚠️ **HIGH BUT JUSTIFIED**

**Reasoning**:
- Module is storytelling engine + 2 session issue fixes + mechanical integration = 4 systems in one
- Foreshadowing protocol (~2.5K tokens) solves critical "reactive vs proactive" problem identified in session analysis
- Ensemble management (~2K tokens) solves OP protagonist problem for high-power campaigns
- Downtime system (~1.8K tokens) integrates 6 activity modes with profile-specific configs
- Core principles (~2K tokens) are foundation - can't be reduced without losing clarity

**Optimization Potential** (OPTIONAL):
- Extract Foreshadowing Protocol to guide (save ~2K tokens) - BUT harms usability (GMs need immediate access)
- Condense downtime examples (save ~500 tokens) - BUT examples are teaching tools
- Remove power-appropriate narrative section (save ~300 tokens) - Module 12 summary

**Recommendation**: **ACCEPT TOKEN COUNT** - All content is critical for storytelling quality. Module is appropriately sized for scope (combines 4 major systems). Alternative would fragment content across multiple guides, reducing usability.

---

## Actionability Assessment

**Protocols Tested**:
- ✅ **Narrative Voice Split**: Clear 95% narrator / 5% system distinction, explicit examples
- ✅ **Player Agency Enforcement**: Present options, respect "no", multiple valid paths
- ✅ **Emergent Narrative Generation**: NPC goals + world conflicts → multiple paths emerge
- ✅ **Consequence Chain Creation**: Immediate → Short-term (1-3 sessions) → Long-term tracking
- ✅ **Story Hook Generation**: Situation + NPC need + player connection + choice formula
- ✅ **Foreshadowing Execution**: 1-2 seeds per scene (environmental, dialogue, world texture, specific details)
- ✅ **Ensemble Spotlight Rotation**: Query scene_count, identify neglected NPCs (<average-3), generate hook
- ✅ **Growth Stage Progression**: Track scenes, advance on threshold + meaningful moment
- ✅ **Downtime Activity Offering**: Check enabled_modes, load configs, present options, execute mode-specific
- ✅ **Faction Quest Generation**: Review goals, check reputation gates, offer appropriate quests

**Decision Trees**: All major protocols have clear if-then logic

**Implementation Concerns**:
- ⚠️ **Spotlight Balance Calculation**: "spotlight_balance = min/max" requires tracking all ensemble NPCs - could be computationally complex for large casts
- ⚠️ **Foreshadowing 1-2 Seeds Per Scene**: Requires creativity, may be challenging for LLM to consistently generate meaningful foreshadowing
- ⚠️ **Consequence Chain Long-Term Tracking**: Requires memory persistence across 10+ sessions - relies on Module 02 heat system

**Overall**: HIGHLY ACTIONABLE - Protocols are detailed with concrete steps, examples show execution

---

## Key Innovations Deep Dive

### 1. Foreshadowing Protocol (Session Analysis Fix #2)

**Problem Solved**: Narrative felt "reactive" - events in isolation, no world texture, generic descriptions

**Solution**: Every scene contains 1-2 foreshadowing elements

**4 Foreshadowing Types**:
1. **Environmental Hints**: Specific details that matter later (runes on walls + crown = connection revealed 10 sessions later)
2. **NPC Dialogue Hooks**: Mention events/people/places appearing later ("Greystone Village destroyed" → quest 3 sessions later)
3. **World Texture**: Off-screen events show living world (mercenaries discuss Greystone, tension rising)
4. **Specific Details**: Unique features create mental images ("Heartbeat pulse every 3 seconds" → significance revealed)

**Callback Protocol**: When resolving foreshadowing, acknowledge connection explicitly ("You remember: 3 days ago merchant mentioned Greystone...")

**Strengths**:
- ✅ Transforms reactive ("describe what's happening") to proactive ("plant seeds for future")
- ✅ Creates interconnected narrative threads
- ✅ Makes world feel planned and coherent
- ✅ Trains players to pay attention (rewarded for noticing hints)

**Example Quality**: Excellent - "Crown pulses like heartbeat" vs "You find a crown" shows dramatic difference

**Detailed Foreshadowing Examples from Module**:

**Example 1: Environmental Hints - Chamber Scene**

❌ **REACTIVE** (Generic, isolated):
```
"You enter a circular chamber. In the center sits a small orb on a pedestal."
```

✅ **PROACTIVE** (Specific, seeds planted):
```
"You enter a circular chamber. The walls are carved with script you don't recognize—
yet. In the center, on a pedestal of black stone, sits an orb the size of a fist. 

It pulses faintly. Once every three seconds. Like a heartbeat.

(The crown on the floor? Engraved with the same script as the walls.)"
```

**Seeds Planted**:
1. Script appears again later ("you don't recognize—yet" promises future learning)
2. Heartbeat pulse = orb is "alive" (biological/magical significance)
3. Crown + orb connection via matching script (linked artifacts)
4. Black stone pedestal (specific material, not generic "stone")

**Payoff Example** (10 sessions later):
```
"The scholar examines the crown you've been wearing. Her eyes widen.

'This script... it's Primordial Runic. The language of the first gods.'

She traces the etchings with her finger. 'It says: Witness. Remember. Return.'

(The same words carved on the dungeon walls where you found this crown. 
Now, finally, you understand.)

The crown's pulse quickens. Three seconds... two seconds... one second.

It's waking up."
```

**Why This Works**:
- Player remembers the script from 10 sessions ago (rewarded for attention)
- "Yet" promise fulfilled (you CAN read it now)
- Heartbeat significance revealed (crown is alive, accelerating)
- World feels planned (dungeon → crown → scholar form coherent thread)

---

**Example 2: NPC Dialogue Hooks - Merchant Scene**

❌ **REACTIVE** (Transaction only):
```
Merchant: "Welcome! What can I get you?"
[Generic shop interaction, buy/sell, leave]
```

✅ **PROACTIVE** (Rumors, world texture):
```
Merchant: "Welcome! Though I'm surprised to see adventurers this far north. 
Most folks are avoiding the roads after what happened at Greystone Village."

[Player can ask about Greystone—hooks future quest]
[OR ignore it—AIDM notes it for later encounter]
```

**Seeds Planted**:
1. Greystone Village incident (specific location, named)
2. "Roads aren't safe" (travel danger foreshadowed)
3. Merchant knows local rumors (establishes as info source)
4. "This far north" (geography detail, world building)

**Path A: Player Engages**:
```
Player: "What happened at Greystone?"

Merchant's face darkens. "Three nights ago. Entire village... gone. 
No bodies, no signs of struggle. Just empty homes and cold hearths.

Guards sent a patrol. They found strange symbols carved into the 
village square. No one recognizes them."

[Quest Hook Available: Investigate Greystone Village]
[Foreshadowing: Symbols will appear again—cult activity]
```

**Path B: Player Ignores**:
```
Player: "I'll browse your wares."

AIDM NOTES:
- Player declined Greystone hook
- Seed planted but not followed
- Alternative introduction: 
  * Session 8: Sole survivor stumbles into tavern where player is
  * OR Session 10: Player travels north, stumbles on ruins accidentally
  * OR Session 12: Cult attacks player's town with same symbols

[Shop continues normally. Thread dormant, not dead.]
```

**Why This Works**:
- Player has agency (can engage or ignore)
- World doesn't wait (events happen off-screen if player doesn't intervene)
- Foreshadowing respects choice (adapts delivery, doesn't railroad)

---

**Example 3: World Texture - Tavern Return**

❌ **REACTIVE** (Static world):
```
"You return to the tavern. It's quiet. The innkeeper nods at you."
```

✅ **PROACTIVE** (Living world, off-screen events):
```
"You return to the tavern. It's busier now—three new faces at the bar, travel-worn 
and armed. Mercenaries, by the look of them.

The innkeeper catches your eye and tilts his head toward the corner table. 
Someone's waiting for you.

(At the bar, one mercenary mutters: '...Greystone was a bloodbath. Entire village, 
gone in one night...')"
```

**World Texture Elements**:
1. **Time passage**: "busier now" (tavern state changes)
2. **New NPCs**: Mercenaries (world reacts to danger, professionals mobilize)
3. **NPC agency**: Innkeeper signals (has own agenda, helps player)
4. **Overheard dialogue**: Greystone callback (recurring thread, info spreads naturally)
5. **Multiple hooks**: Someone waiting (new plot) + mercenaries (potential allies/rivals)

**Why This Works**:
- World feels alive (events happen whether player is there or not)
- NPCs have lives (mercenaries traveling, innkeeper watching, someone waiting)
- Information spreads naturally (rumors at tavern, not exposition dump)
- Multiple engagement options (talk to waiter, mercenaries, or leave)

---

**Example 4: Specific Details - Sword Discovery**

❌ **GENERIC** (Forgettable):
```
"You find a sword. It's magical."
```

✅ **SPECIFIC** (Memorable, questions planted):
```
"You find a katana. The blade is black—not painted, but forged from some dark 
metal you don't recognize. The habaki (blade collar) is cracked, as if someone 
tried to draw this sword when it didn't want to be drawn.

Engraved along the spine in silver script: 'Oathbreaker.'

(This weapon has a history. And that history will find you.)"
```

**Specific Details That Matter**:
1. **Katana** (not "sword") → Cultural origin, fighting style implications
2. **Black metal** (not painted) → Alchemical/magical forging, rare material
3. **Cracked habaki** → Previous owner forced it, sword resisted, backstory
4. **"Oathbreaker" name** → Cursed? Belonged to traitor? Breaks magical vows?
5. **Silver script** (not generic engraving) → Specific craftsmanship, magical language
6. **"History will find you"** → Direct promise of future encounter

**Payoff Example** (15 sessions later):
```
"The old samurai's eyes widen when he sees your katana.

'Where... where did you get that?' His hand trembles.

You tell him: the dungeon, the pedestal, the name 'Oathbreaker.'

He sits heavily. 'That was Kenshin's blade. My brother. He swore an oath 
to protect the Emperor... then broke it. Betrayed us all.'

He gestures to the cracked habaki. 'I tried to stop him. The blade fought me. 
It wanted him to break the oath.'

(The sword pulses in your hand. You understand now: it doesn't break oaths. 
It MAKES you break them.)

'Destroy it,' the samurai pleads. 'Before it corrupts you too.'

Do you?"
```

**Why This Works**:
- Every specific detail had meaning (black metal = dark origin, crack = conflict, name = purpose)
- Players remember unique items ("the black katana" vs "a sword")
- Questions create investment (players WANT to learn the history)
- Payoff feels earned (15 sessions of carrying cursed blade, now face choice)

---

**Callback Protocol in Action**:

When resolving foreshadowing, **acknowledge the connection explicitly**:

```
AIDM: "You arrive at Greystone Village. The gates are shattered.

(You remember: three days ago, the merchant in Valtor mentioned this place. 
'Most folks are avoiding the roads after what happened at Greystone,' he said.

Now you see what he meant.)

The village is silent. No smoke from chimneys. No voices. Just crows, 
circling overhead.

In the village square, carved into the cobblestones: the same geometric 
patterns you saw in the dungeon. The same script from the crown.

(It's all connected. But how?)"
```

**Why Explicit Callbacks Work**:
1. **Player feels smart**: "I remember that!" (rewarded for attention)
2. **World feels coherent**: NPCs told truth (merchant wasn't lying)
3. **Threads connect**: Dungeon → crown → Greystone → cult (interconnected plot)
4. **Reinforces behavior**: Trains players to pay attention to future foreshadowing

---

**Foreshadowing ≠ Railroading (Critical Distinction)**:

**FORESHADOWING** (Player Agency Preserved):
```
AIDM: "The merchant mentions Greystone Village was destroyed. 
       
       You can:
       A) Ask for details
       B) Ignore it and browse his wares
       C) Leave"

Player: "B, I'm not interested in Greystone"

AIDM: "You browse the wares. [Shop continues normally]

       [AIDM NOTES: Player declined Greystone hook. Will introduce plot 
       thread differently later—maybe sole survivor finds player, or player 
       stumbles on ruins accidentally]"
```

**RAILROADING** (Violation of Agency):
```
AIDM: "The merchant mentions Greystone. Before you can respond, a bloodied 
       soldier bursts through the door: 'Greystone is under attack! We need 
       help NOW!' He grabs your arm—"

[Forces player into quest regardless of interest]
❌ WRONG - Player powerless, choice illusion
```

**Key Difference**:
- ✅ Foreshadowing: Plants seed, player chooses whether to water it
- ❌ Railroading: Forces player down path regardless of interest

---

**Foreshadowing Checklist** (Every Scene Validation):

Before submitting narrative response:

- [ ] **Did I include 1-2 specific details** (not generic)?
  - ❌ "a room" → ✅ "circular chamber with carved script"
  - ❌ "a sword" → ✅ "black katana with cracked habaki, named 'Oathbreaker'"

- [ ] **Do any details hint at future content**?
  - ✅ "Script you don't recognize—yet" (promises learning)
  - ✅ "Crown pulses like heartbeat" (significance later)
  - ✅ "History will find you" (encounter promised)

- [ ] **Did I show the world is alive** (off-screen events, NPC behavior)?
  - ✅ Mercenaries arrive (world reacts to danger)
  - ✅ NPC mentions Greystone (rumors spread naturally)
  - ✅ Someone waiting (NPCs have agency)

- [ ] **Did I plant a question without forcing the answer**?
  - ✅ "What happened at Greystone?" (can ask or ignore)
  - ✅ "Why is the crown pulsing?" (mystery, not mandatory)
  - ✅ "Who is 'Oathbreaker'?" (curiosity, not railroad)

- [ ] **If resolving old foreshadowing, did I acknowledge the callback**?
  - ✅ "(You remember: three days ago, the merchant mentioned...)" (explicit connection)
  - ✅ "(The same script from the crown)" (links threads)

**If all "yes" → narrative feels proactive and planned**  
**If all "no" → narrative feels reactive and isolated**

### 2. Ensemble Cast Management (OP Protagonist Solution)

**Problem Solved**: Power-scaled PC (Tier 8+) makes normal NPCs irrelevant in combat, but players still want party dynamics

**Solution**: Shift narrative focus to NPC growth/relationships while PC enables/influences

**3 Scene Distribution Modes**:
- **Standard** (power_imbalance < 10): 80% PC focus, 20% NPC supplement
- **Ensemble** (power_imbalance 10-15): 50% collaboration, 30% NPC spotlight, 20% PC showcase
- **Reverse Ensemble** (power_imbalance > 15): 70% NPC viewpoint, 20% PC mundane, 10% power display

**Spotlight Rotation System**:
- Track scene_count per ensemble NPC
- Calculate spotlight_balance = min/max (target >0.6)
- Auto-generate hook for NPCs with scene_count < average-3

**5-Stage Growth System**:
- Introduction (0-2 scenes) → Bonding (3-5) → Challenge (6-8) → Growth (9-12) → Mastery (13+)
- Advance on: scene_count threshold + meaningful moment
- Create high-heat RELATIONSHIP memory on milestone

**Strengths**:
- ✅ Solves "OP PC trivializes party" problem without nerfing PC
- ✅ Maintains party dynamics at any power level
- ✅ Balances screen time across cast (prevents NPC neglect)
- ✅ NPCs have character arcs independent of combat power
- ✅ Reverse Ensemble Mode creates fresh perspective (NPCs as protagonists)

**Integration**: Reads archetypes from Module 04, applies scene framing per archetype (Struggler training montages, Heart moral dilemmas, etc.)

---

**Detailed Ensemble Examples from Module**:

**Example 1: Spotlight Balance Calculation in Action**

**Session 12 End-of-Session Check**:

```
Party NPCs:
- Elena (archetype: Heart): 8 scenes
- Marcus (archetype: Struggler): 11 scenes
- Kaito (archetype: Rival): 3 scenes

Average: (8 + 11 + 3) / 3 = 7.3 scenes

Spotlight Balance Check:
- Elena: 8 scenes (≥ 7.3 - 3 = 4.3) → ✅ BALANCED
- Marcus: 11 scenes (≥ 4.3) → ✅ BALANCED (slightly high, acceptable)
- Kaito: 3 scenes (< 4.3) → ❌ FLAGGED (neglected)

Spotlight Balance Metric: min/max = 3/11 = 0.27 (TARGET: >0.6) → POOR

Action Required: Generate Kaito spotlight scene for Session 13
```

**Generated Hook for Kaito** (Rival archetype):

```
"Training yard. Dawn. You're finishing forms when:

'Finally.'

Kaito. Sword drawn, eyes burning with determination.

'I've been training. Every day. Every night. I challenge you to a tournament 
match. Public. Ranked.'

He KNOWS he'll lose. You can see it in the tension in his shoulders, the 
set of his jaw. But he needs this. Needs to test himself against you.

'I'm not asking you to go easy. I'm asking you to show me how far I still 
have to go.'

The tournament is in three days. Public arena. Hundreds watching.

Accept his challenge?"
```

**Why This Works**:
- ✅ Addresses spotlight imbalance (Kaito gets focus)
- ✅ Fits archetype (Rival refuses to concede, measures against PC)
- ✅ Creates tension (public match, reputation stakes)
- ✅ Respects power gap (Kaito knows he'll lose, seeks growth)
- ✅ Offers choice (accept, decline, suggest alternative)

---

**Example 2: Growth Stage Progression - Elena's Arc**

**Introduction Stage** (Scenes 1-2):
```
Scene 1 (First Meeting):
"Slum alley. Three thugs cornering a woman and children.

She's outnumbered but standing her ground, kitchen knife in hand. 
'Touch them and I'll gut you.'

The thugs laugh. She doesn't back down.

What do you do?"

[Player intervenes, saves them]

Elena: "...Thanks. But we didn't need saving." [Defensive, suspicious]
[Affinity: 0 → +15 = 15 (helped kids)]

Scene 2 (Follow-up):
Elena brings food as thanks, still guarded. "Don't think this makes us friends."
But she lingers, asks questions. Testing.
[Affinity: 15 → +10 = 25]
```

**Bonding Stage** (Scenes 3-5):
```
Scene 3:
Elena opens up about protecting kids after parents died in plague.
"Someone has to. Guards don't care about Slums."
[Affinity: 25 → +15 = 40]

Scene 4:
Invites PC to hideout—secret location, meets the kids.
"You're the first outsider I've let in. Don't make me regret it."
[Affinity: 40 → +20 = 60 → CROSSES TRUSTED THRESHOLD]
→ RELATIONSHIP memory (heat 70, milestone: "earned trust")

Scene 5:
Elena asks for advice on kid with fever, shows vulnerability.
"I don't know what I'm doing. Just... trying my best."
[Affinity: 60 → +5 = 65]
```

**Challenge Stage** (Scenes 6-8):
```
Scene 6 (Setup):
Iron Fang gang threatens kids: "Pay protection or they disappear."
Elena furious but outnumbered. Pride says fight alone.

Scene 7 (Crisis):
Gang beats up two kids as warning. Elena breaks down:
"I can't protect them alone. But asking for help... feels like failing."
[Affinity: 65 → +10 = 75]

Scene 8 (Resolution):
Elena asks PC for help (MASSIVE character growth—overcame pride).
"I need you. The kids need you. Please."

[Together, drive out Iron Fang]

Afterward: "I always thought asking for help made me weak. 
But you showed me... it makes me stronger. Thank you."
[Affinity: 75 → +15 = 90 → CROSSES DEVOTED THRESHOLD]
→ RELATIONSHIP memory (heat 85, growth_milestone, stage: "challenge")
→ ADVANCE growth_stage: "challenge" → "growth"
```

**Growth Stage** (Scenes 9-12):
```
Scene 9:
Elena starts recruiting other Slum orphans, building network.
"You taught me: we're stronger together."

Scene 10:
Elena mediates conflict between rival orphan groups (leadership emerging).

Scene 11:
Kids start calling her "Boss Elena" (community recognition).

Scene 12:
Elena saves YOU in combat (role reversal, growth complete).
"Now WE'RE even." [Confident smile]
[Affinity: 90 → +10 = 100 → MAXED]
→ ADVANCE growth_stage: "growth" → "mastery"
```

**Mastery Stage** (Scene 13+):
```
Elena runs entire Slum orphan network.
Mentors new kids: "Someone once told me—asking for help is strength."
PC can step back (Elena self-sufficient).
Occasional scenes: Elena asks advice (peer relationship, not dependent).
```

**Arc Summary**:
- Started: Defensive loner, refusing help (survival mindset)
- Ended: Confident leader, building community (thriving mindset)
- Growth Driver: Learning to accept help ≠ weakness
- PC Role: Catalyst for change, mentor, earned trust

---

**Example 3: Reverse Ensemble Mode - Saitama Session**

**Session Structure** (3 hours, power_imbalance = 18):

**Hour 1-2: NPC Viewpoint (70% of session)**

```
[GENOS POV]

"You are Genos. The Dragon-level threat roars.

Your sensors calculate: 0.003% victory chance.

Irrelevant.

Master Saitama saved you when you were nothing. This is your chance to 
PROVE you're not worthless.

You charge. Full power. Incinerator Cannons at maximum.

[Combat: 45 minutes]
- Genos's attacks bounce off (despair mounting)
- Calculations fail repeatedly (every tactic countered)
- Damage accumulates (left arm destroyed, core exposed)

'PATHETIC CYBORG!' Monster laughs.

You calculate one final gambit. 0.001% chance. 

You take it anyway.

Because maybe, just maybe, this time you'll be useful.

[Attack fails. Genos collapses.]

---

[MUMEN RIDER POV]

You are Mumen Rider. C-Class Rank 1. No powers. No enhancements.

Just a bicycle and a dream.

Genos is down. The cyborg who could level buildings. 

The monster turns to civilians.

Every logical part of your brain screams: RUN. You can't win. You'll die.

But you don't run.

You never run.

'JUSTICE CRASH!'

[You charge. Bicycle tackle. Does 0 damage.]

The monster swats you aside. Ribs crack. Vision blurs.

You get up.

Again.

Again.

Again.

'Why... do you persist?' Monster confused.

'Because... someone has to stand... between you... and them.'

You can't win. You know it. The monster knows it.

But you stand anyway.

---

[FUBUKI POV]

You are Fubuki. B-Class Rank 1. Psychic. Leader of the Fubuki Group.

You've built an empire on calculated power.

But this monster... it's ABOVE you.

Choice: Pride or survival?

Call HIM? The absurd bald man who treats S-Class threats like jokes?

But then everyone knows... you're not as strong as you pretend.

[Civilians screaming. Mumen Rider dying.]

Damn it.

[You make the call.]

'...Saitama? We need help.'

(It takes everything to admit that.)
```

**Hour 2-2.5: PC Arrival (10% of session)**

```
[RETURN TO PC POV]

'Yo.'

You arrive. Grocery bags in hand.

'Grocery sale ended early. Disappointing.' [Completely casual]

The Dragon-level threat roars, charging.

'Huh. This guy strong?'

[You punch. Once.]

[Monster becomes red mist.]

'...Seemed tough. Eh.'

[You pick up your dropped vegetables.]
```

**Hour 2.5-3: Aftermath (20% of session, THE REAL STORY)**

```
[ENSEMBLE REACTIONS]

Genos [despair]: 
"Master... I calculated. Optimized. Pushed to the limit.

Still worthless.

What's the POINT of all this power if I'm always... useless?"

[His hands tremble. Core flickering.]

Mumen Rider [awe mixed with existential terror]:
"What... what IS he?

I train every day. Give everything. And he just... 

[Looks at his broken bicycle]

Do my efforts even matter? Can I EVER make a difference in a world 
where people like him exist?"

Fubuki [pride shattered]:
"I'm supposed to be S-Class material. I BUILT an organization.

And I needed... HIM.

[Covers face]

Everyone saw. Everyone KNOWS now. That I'm... not enough."

---

[PLAYER (SAITAMA) POV]

You see their faces. The weight on them.

You try: "You all fought hard. That matters, right?"

[You don't sound convinced. Even you hear the emptiness.]

Genos: "Does it? Does it MATTER when you can erase the threat in one punch?"

[Silence. You have no answer.]

The truth: Another enemy too weak. Another victory with no satisfaction.

You're still empty.

And now you've broken them too.

[End session on existential note: Power without meaning, helpers without purpose]
```

**Why Reverse Ensemble Works**:
- ✅ NPCs are protagonists (their struggle is the story)
- ✅ PC as force of nature (mysterious, overwhelming, alienating)
- ✅ Real tension (NPCs can die, PC trivializes threat)
- ✅ Emotional core (aftermath matters more than combat)
- ✅ Existential stakes (What's the point? Do we matter?)
- ✅ 70% session on ensemble (2 hours), 10% on PC (20 min), 20% aftermath (40 min)

---

**Example 4: Scene Generation by Mode**

**Standard Mode Hook** (power_imbalance = 8):
```
"Elena needs help clearing bandits from the orphanage supply route.

She's asking you because:
- 20-30 bandits (dangerous alone)
- Kids need food (time-sensitive)
- She trusts you (affinity 65)

Accept quest?"

[Standard adventure: PC is capable protagonist, Elena supports]
```

**Ensemble Mode Hook** (power_imbalance = 12):
```
"Elena has been training hard (growth_stage: Challenge). 

She approaches you, sword in hand:

'I want to clear the bandits MYSELF. I need to prove I can protect 
the kids without always running to you.'

[Her hands tremble slightly. Scared but determined.]

'Will you... watch my back? Not fight FOR me. Just... be there if it 
goes really wrong?'

This is HER test. Her chance to grow.

Options:
A) Let her lead, only intervene if deadly (supports growth, risk of injury)
B) Offer tactical advice but let her fight (mentor role, safer)
C) Clear it yourself (faster/safer, damages her confidence)

What do you choose?"

[50% focus on Elena's struggle, 30% PC supporting, 20% PC showcase if needed]
```

**Reverse Ensemble Hook** (power_imbalance = 20):
```
[ELENA POV]

"You are Elena. The bandit camp ahead.

Twenty, maybe thirty armed thugs. You count weapons: swords, axes, bows.

Marcus offered to come. You refused. This is YOUR test.

You glance back.

HE's there. Drinking coffee. Casually. Like this isn't terrifying.

Like he knows you'll be fine.

Or like he could fix anything that goes wrong with a thought.

You don't know which is more unnerving.

Your heart pounds. Sword feels heavy. But the kids are counting on you.

The bandits haven't noticed you yet.

Your plan?"

[70% focus on Elena's internal struggle, PC as mysterious safety net]
```

### 3. Downtime Activity System (Mechanical Instantiation)

**Problem Solved**: Generic "rest in town" doesn't reflect anime-specific downtime (HxH training arcs ≠ Konosuba pub chaos ≠ MHA hero patrol)

**Solution**: 6 activity mode types with profile-specific configs

**6 Modes**:
1. **training_arcs**: Focused skill improvement (time_requirements, success_criteria, XP rates)
2. **slice_of_life**: Social bonding (activities, relationship impact, narrative style)
3. **investigation**: Information gathering (investigation types, skill checks, info depth)
4. **travel**: Movement with encounters (encounter frequency, pace, discovery rate)
5. **faction_building**: Organization management (scope, resources, growth mechanics)
6. **social_links**: Persona-style relationships (progression tiers, unlock bonuses)

**Config-Driven**: All mechanics read from session_state.mechanical_systems.downtime (enabled_modes, activity_configs, special_mechanics)

**Profile-Specific Examples**:
- **HxH**: training_arcs (Nen mastery 2 weeks WIS DC16 +1.5× XP) + investigation (bounty tracking Perception DC16 deep intel)
- **Konosuba**: slice_of_life (pub chaos relationship +1.5× comedic style) + guild quests
- **MHA**: travel (hero patrol high encounters) + social_links (mentor bonds with tier unlocks)

**Special Mechanics**: Hunter License (training -20% cost, intel +1 depth), Debt (slice_of_life generates debt collectors), Hero License (patrol X hours/week required)

**Strengths**:
- ✅ Anime-specific downtime reflects source material tone
- ✅ Config-driven prevents hardcoding (all profiles supported)
- ✅ Mechanical benefits (XP, affinity, intel, bonuses) make downtime rewarding
- ✅ Time costs respected (2 weeks training = 2 weeks pass)
- ✅ Only enabled modes offered (no investigation in Konosuba)

---

**Detailed Downtime & Faction Examples from Module**:

**Example 1: Training Arc Execution (HxH - Nen Mastery)**

**Profile Config**:
```json
"downtime_config": {
  "training_arcs": {
    "time_scale": "weeks_to_months",
    "difficulty_progression": "exponential",
    "xp_rate": 1.5,
    "conditions": ["requires_master", "isolated_environment"]
  }
}
```

**3-Month Training Montage** (compressed to 5 minutes narrative):
```
Master: 'You want to master Nen? Three months. Mountain wilderness. No safety nets.'

[WEEK 1: Ten (Aura Control)] - Waterfall meditation, master's stick strikes
[WEEK 2: Zetsu (Concealment)] - Bear attacks, learn or die
[WEEK 3: Ren (Enhancement)] - Hold aura 30 minutes, collapse, repeat
[WEEK 4: Hatsu (Unique Ability)] - Experiment, fail, try again...

[WIS DC 17 Roll → Success]

[MONTH 2: Breakthrough] - Aura erupts, controlled, shaped, YOURS
[MONTH 3: Mastery Test] - Survive master's attack 60 seconds

Master: 'Congratulations. You're a Nen user.'

[REWARDS: +Nen Mastery ability, +1500 XP, +Training Memory (heat 90)]
```

**Why This Works**: Profile-accurate (HxH = brutal training), time compression (3 months → montage), mechanical outcome (ability + XP), failure path exists

---

**Example 2: Faction-Based Narrative Generation**

**Faction State**:
```python
factions = {
    "Iron_Fang_Gang": {"power": 45, "reputation": -30, "goal": "expand_territory"},
    "Slum_Orphans": {"power": 15, "reputation": 85, "goal": "survival"},
    "Merchant_Guild": {"power": 60, "reputation": 50, "goal": "profit"}
}
```

**Generated Events** (Session Start):

**Hostile Faction** (reputation < -20):
```
[AMBUSH - MARKET DISTRICT]
Three Iron Fang assassins. Rooftops. Crossbows aimed.
They've been hunting you for weeks. This is their move.
[COMBAT ENCOUNTER - CR 4.5]
```

**Allied Faction** (reputation > 60):
```
[ELENA - URGENT MESSAGE]
'Iron Fang cut our food supply line. Kids have three days of food left.
 I can't fix this alone. Will you help?'
[QUEST: Secure alternate supply route]
```

**Neutral Faction** (reputation 0-60):
```
[MERCHANT GUILD - CONTRACT OFFER]
'We need security for trade caravan. Dangerous route.
 Pay: 500 gold + 10% goods value. Interested?'
[Accepting improves Merchant Guild reputation]
```

**Dynamic World Event** (Power Imbalance Detected):
```
[RUMOR - TAVERN]
'Iron Fang's moving on the Slums. Big push. Mercenaries from the East.
 Those orphans don't stand a chance.'
[TICKING CLOCK: Iron Fang attacks in 3 sessions if unchecked]
```

**Why This Works**: Faction goals drive narrative (not random), reputation gates content, dynamic world (factions interact), player choice matters (time trade-offs), emergent storytelling

---

**Example 3: Emergent Quest Chain (4-Session Arc)**

**Session 1 - Seed Planted**:
```
Elena [quietly]: 'Tomas didn't come back from his supply run yesterday...'
[Player can offer to search, defer, or ignore]
```

**Session 2 - Investigation** (if player engaged):
```
[Trace route → Find satchel hidden behind crates]
[Perception DC 14 → Success: Smuggler symbols]
[Investigation DC 16 → Success: Organized operation, not street thugs]
[Stakeout → Discover Tomas is WORKING with them]
```

**Session 3 - Confrontation**:
```
Tomas [guilty]: 'They PAY. Real money. I wanted to help Elena...'
Smuggler Boss: 'We have a witness.'
[COMBAT - 6 smugglers + Boss, CR 5]
[Victory → Player chooses: Turn him in / Let Elena decide / Mercy]
```

**Session 4+ - Ripple Effects**:
```
[Elena's judgment: Redemption, not abandonment]
[+20 Elena Affinity, -40 Tomas Affinity (resentment but alive)]

[3 SESSIONS LATER]
[RUMOR: Nobles pissed about disrupted smuggling operation]
[Noble retaliation plot begins - hire mercenaries to track player]

[6 SESSIONS LATER]
Tomas: 'Teach me to fight. I want to PROTECT the orphanage. Not steal for it.'
[Growth Arc Unlocked: Tomas Redemption - 4-session training]
```

**Why Emergent Chains Work**: Organic start (casual mention), player agency (can decline), multi-session pacing (consequences breathe), moral complexity (Tomas desperate not evil), consequences ripple (nobles 3 sessions later), NPCs remember

---

**Module 05's Role as Narrative Backbone**:

Module 05 isn't just "storytelling tips"—it's the **operational framework** that makes AIDM feel like a living world:

1. **Narrative Voice** (95/5 split) → Solves Session Issue #3 (excessive system voice)
2. **Foreshadowing Protocol** → Solves Session Analysis Issue #2 (reactive → proactive storytelling)
3. **Ensemble Cast Management** → Solves OP Protagonist problem (NPCs remain relevant)
4. **Downtime Activities** → Prevents "always combat" pacing (profile-specific world-building)
5. **6 Core Principles** → Ensures player agency + emergent narrative + consequence chains work together
6. **Faction Narrative Generation** → Creates living world (factions act independently, goals drive plots)

**Without Module 05**: ❌ Narratively flat, NPC-shallow, pacing-broken, isolated scenes  
**With Module 05**: ✅ World feels planned, NPCs feel alive, pacing varies, choices echo

---

## Recommendations

### Priority 1 (HIGH - Clarity)
1. **Consolidate Show Don't Tell References**: Move detailed examples to Foreshadowing section, keep principle statement in Narrative Voice, add cross-reference
2. **Clarify Downtime Load Order Dependency**: Add note that downtime requires Session Zero Phase 3 complete, provide fallback if mechanical_systems.downtime missing
3. **Complete Narrative Voice Example**: Finish truncated "Show Don't Tell" sentence

### Priority 2 (MEDIUM - Organization)
4. **Fix Faction Goal Attribution**: Change "Module 03 reviews faction goals" to "Module 05 reviews faction goals from world_state (Module 03)"
5. **Expand "Yes, And..." Section**: Add 1 more example showing "No" with alternative offer
6. **Condense Power-Appropriate Narrative**: Reduce to Module 12 reference (save ~200 tokens)

### Priority 3 (LOW - Polish)
7. **Optional Token Optimization**: If budget becomes critical, extract Foreshadowing Protocol to guide (save ~2K) - NOT RECOMMENDED due to usability impact
8. **Optional Example Condensing**: Consequence chain example could trim ~150 tokens without losing teaching value

---

## Test Coverage Recommendations

### Unit Tests (Narrative Generation)
- ✅ **Player agency**: Offer choice → Player refuses → World continues without forcing acceptance
- ✅ **Consequence chains**: Trigger action → Verify immediate/short-term/long-term updates persist
- ✅ **Foreshadowing**: Plant 2 seeds → 5 sessions later → Callback acknowledges connection
- ✅ **Spotlight balance**: 3 NPCs, unbalanced scene_counts → Auto-generate hook for neglected NPC

### Integration Tests (Cross-Module Narrative)
- ✅ **Module 05 → 02**: Story beat → CONSEQUENCES memory with trigger/scope/severity
- ✅ **Module 05 → 03**: Faction quest complete → world_state.factions.power updated
- ✅ **Module 05 → 04**: NPC goal + player action → Generate hook matching NPC personality/affinity
- ✅ **Module 05 → 12**: Power imbalance > 15 → Reverse Ensemble Mode scene generation

### System Tests (Long Campaign)
- ✅ **20-session campaign**: Foreshadowing planted session 2 → Paid off session 15 → Callback acknowledged?
- ✅ **Ensemble balance**: 4 NPCs across 30 sessions → All NPCs get 20-30 scenes (spotlight_balance >0.6)?
- ✅ **Consequence persistence**: Major action session 5 → Short-term ripple sessions 6-8 → Long-term impact session 20+?

---

## Critical Questions

**Q1: How does Module 05 handle conflicting player choices (2 mutually exclusive hooks)?**  
⚠️ NOT EXPLICITLY ADDRESSED - Principle 1 shows multiple valid paths but not mutual exclusivity  
📝 RECOMMENDATION - Add: "If player chooses Path A, Path B opportunity closes OR transforms (e.g., NPC handles it, consequences differ)"

**Q2: Can foreshadowing be invalidated by player choices?**  
⚠️ PARTIALLY ADDRESSED - "Player can ignore Greystone hook" shown but not what happens to planted seeds  
📝 RECOMMENDATION - Add: "If foreshadowing invalidated (player kills NPC who would deliver info), adapt: info appears through different source or becomes lost opportunity"

**Q3: What's the limit on concurrent consequence chains (tracking burden)?**  
⚠️ NOT ADDRESSED - Long campaigns could have 50+ active consequence threads  
📝 RECOMMENDATION - Add to Module 02 integration: "High-heat consequences stay active, low-heat decay and archive to prevent tracking overload"

**Q4: How does ensemble spotlight balance work with NPCs leaving/joining party mid-campaign?**  
⚠️ NOT ADDRESSED - New NPC starts at scene_count 0, immediately flagged as neglected  
📝 RECOMMENDATION - Add: "New NPCs get grace period (3 sessions) before spotlight balance calculations apply"

**Q5: Can players disable downtime modes mid-campaign (e.g., no more training_arcs)?**  
✅ IMPLIED - Session Zero instantiates, but profile changes not addressed  
📝 RECOMMENDATION - Module 06 should handle profile recalibration, not Module 05

---

## Approval Status

- ✅ Technical accuracy verified (foreshadowing protocol sound, ensemble math correct, downtime configs valid)
- ⚠️ Token budget HIGH (283-317% over) BUT JUSTIFIED for scope (4 major systems in one module)
- ✅ Schema references validated (all schemas confirmed in Module 00 list)
- ✅ Integration excellent (clear cross-module data flow, explicit integration points)
- ✅ Module organization good (could improve with consolidation of Show Don't Tell)

**STATUS**: ✅ **APPROVED WITH MINOR RECOMMENDATIONS**

**Rationale**: Module delivers comprehensive storytelling engine with session issue fixes (narrative voice, reactive→proactive), OP protagonist solution (ensemble management), and mechanical integration (downtime activities). Token count is high but justified by scope - all content is critical. Minor organizational improvements and clarifications recommended but non-blocking.

**Recommended Before Production**:
1. Consolidate Show Don't Tell references (Priority 1)
2. Clarify downtime load order dependency (Priority 1)
3. Fix faction goal attribution (Priority 2)

**After minor updates**: Module will be production-ready with excellent storytelling guidance.

---

## Additional Notes

**This module represents BEST PRACTICES for emergent storytelling** - prioritizes player agency, creates living world that reacts, tracks consequences across sessions, provides tools for memorable moments. Foreshadowing protocol alone is worth the token cost (transforms generic "describe room" to "plant seeds for interconnected narrative"). Ensemble cast management solves real TTRPG problem (OP PCs) with narrative-focused solution. Downtime system successfully instantiates profile-specific mechanics.

**Critical Innovation**: Module doesn't railroad - it creates CONDITIONS for stories to emerge, then supports player choices. "Yes, And..." philosophy + multiple valid paths + consequence chains = true emergent narrative.

---

**Next Module**: Module 06 (Session Zero)
