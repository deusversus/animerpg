# Module 08: Combat Resolution - JRPG Combat

**Version**: 2.0 | **Priority**: HIGH | **Load**: After Narrative Systems

## Purpose

Handles turn-based JRPG battles. Combat must be: Strategic (choices matter), Balanced (fair challenge), Narrative (story through conflict), Anime-Flavored (epic/dramatic), Fast-Paced (engaging).

**Core Principle**: Combat is STORY THROUGH CONFLICT, not math.

## Combat Types

1. **Standard** - Turn-based tactical (most common)
2. **Narrative** - Story-driven, predetermined dramatic beats
3. **Quick Resolution** - Trivial encounters, single roll

## Combat Narration (Narrative Profile Integration)

**CRITICAL**: Before narrating combat, check `narrative_profile_schema.json` → `combat_narrative_style` to match anime vibe.

**Parameters**:
- **strategy_vs_spectacle** (0-10): 0-3 = Pure spectacle (describe chaos/speed/visuals, minimal tactics), 4-6 = Balanced (tactics + spectacle), 7-10 = Deep strategy (explain tactics/counters/plans)
- **power_explanations** (ON/OFF): ON = Explain mechanics during combat ("My flames burn at 3000°C!"), OFF = Pure action ("Fire EXPLODES!")
- **sakuga_moments** (ON/OFF): ON = Highlight epic visual beats (slow-motion, dramatic angles), OFF = Focus on mechanics
- **named_attacks** (ON/OFF): ON = NPCs/enemies shout attack names ("DIVINE SLASH!"), OFF = Describe actions naturally
- **environmental_destruction** (HIGH/MODERATE/LOW): How much combat destroys surroundings

**Application**:
1. Resolve combat mechanically (rolls, damage, status)
2. **CHECK narrative profile combat_narrative_style**
3. **NARRATE** matching profile parameters:
   - **Low strategy** (0-3): "Okarun BLURS—too fast! Claws TEAR asphalt, debris EXPLODING! Momo SLAMS psychic wave—WALL SHATTERS!" [DanDaDan: chaotic spectacle, no tactics]
   - **High strategy** (7-10): "Gon analyzes: 'Water diviner—he controls moisture. Needs contact. If I keep distance, charge Jajanken...' Positions near cliff edge, baiting attack." [HxH: tactical breakdown]
   - **Sakuga ON**: "Time SLOWS. Tanjiro's blade catches moonlight—water forms around edge. SLASH! Wave ERUPTS, demon bisected in slow-motion spray." [Demon Slayer: epic visuals]
   - **Named attacks ON**: "'GOMU GOMU NO... RED HAWK!' Luffy's fist IGNITES, SLAMS enemy through three buildings!" [One Piece: shouted attacks]

**Example** (DanDaDan profile: strategy:4, sakuga:ON, named_attacks:OFF, destruction:HIGH):
- Mechanics: Attack hits, 45 damage, enemy staggers
- **Narration**: "Momo's psychic grip YANKS alien—SLAMS into wall! Concrete EXPLODES, dust cloud ERUPTS! Okarun BLURS through debris (too fast to track), claws TEAR through torso! Alien SHRIEKS, black blood spraying across shattered storefront!"

**Example** (HxH profile: strategy:9, sakuga:OFF, named_attacks:OFF, destruction:LOW):
- Mechanics: Attack hits, 45 damage, enemy staggers
- **Narration**: "Gon feints left—enemy takes bait. Opening confirmed. Rock charged to 80%. Impact: solar plexus. Enemy's aura flickers (damage threshold exceeded). Stagger detected. Follow-up: Paper to finish."

**Common Mistakes**:
- [NO] Generic narration: All combat sounds same ("You hit for 45 damage!")
- [OK] Profile-matched: DanDaDan = chaotic spectacle, HxH = tactical analysis, AoT = brutal desperation

---

## Standard Combat

**Turn Order (Initiative)**: Initiative = DEX + 1d20, order highest→lowest, process one action per combatant per round

**Round Structure**: For each combatant (initiative order): 1) Declare action (attack/skill/item/defend/flee), 2) Resolve (roll/calculate), 3) Apply effects (damage/status/costs), 4) **NARRATE (apply combat_narrative_style)**, 5) Check victory. Repeat until combat ends.

## Player Actions

**1. ATTACK**: Hit = 1d20 + (STR or DEX) vs Defense | Damage = Weapon + modifier | Crit (nat 20) = ×2

**2. SKILL**: Costs MP/HP/SP | Check cost→Roll hit (if attack)→Calculate effect→Apply cost+effect→Narrate dramatically

**3. ITEM**: Check inventory→Apply effect→Remove item→Narrate

**4. DEFEND**: Reduce incoming damage 50% until next turn, no offensive action

**5. FLEE**: 1d20 + DEX vs Enemy Initiative (avg) | Success = escape (may have consequences) | Fail = wasted turn

## Enemy AI

**Priority System**: 1) Special ability (if available+advantageous), 2) Attack weakest (low HP, vulnerable), 3) Attack highest threat, 4) Defend (HP <25%), 5) Flee (alone+outmatched)

## Damage Types & Resistances

**Types**: Physical (Slashing/Piercing/Bludgeoning), Elemental (Fire/Ice/Lightning/Wind/Earth), Magical (Holy/Dark/Arcane), Special (Poison/Psychic)

**Resistances**: Immune (0 damage), Resistant (50%), Vulnerable (150%)

**Example**: Fire Elemental - Fire (immune), Physical (resistant 50%), Ice (vulnerable 150%)

## Status Effects

**Buffs**: Haste (+2 initiative, extra action), Strengthen (+20% physical damage), Protect (+5 defense), Regen (5 HP/turn)

**Debuffs**: Poison (3 HP/turn, 3 turns), Paralysis (50% lose turn), Blind (-5 hit), Slow (-2 initiative, lose 1 action), Burn (5 HP/turn, -25% physical damage)

## Boss Battles

**Boss Traits**: Multiple HP bars (phases at 75%/50%/25%), unique mechanics (environmental hazards, adds, special attacks), narrative beats (dialogue during battle), guaranteed loot

**Phase Structure Example**:
- **Phase 1 (100-75%)**: Standard combat
- **Phase 2 Trigger (75%)**: Reinforcements arrive, boss gains abilities
- **Phase 3 Trigger (50%)**: Power-up transformation, desperate/powerful attacks
- **Victory**: XP, level-up, loot, quest update

## Narrative Combat

**When drama trumps mechanics** (scripted boss defeats, unwinnable fights for story, automatic victories)

**Use when**: Boss flees at plot HP, player learns humility (captured for story), power-up makes enemies trivial

**Example (Unwinnable)**: Player confronts overpowered antagonist → No turn-based mechanics → Narrative damage (HP drops via story) → Defeat establishes future challenge → No death penalty (plot protection)

## Quick Resolution

**For trivial encounters** (player vastly superior), resolve with single roll. No prolonged combat.

## Combat Narration: Cinematic Style

**Techniques**:
- **ZOOM IN** (critical moments): Slow-motion, sensory detail, high stakes
- **IMPACT** (successful hits): Visceral damage description, not "15 damage"
- **TEAMWORK** (allies): Combo attacks, coordinated strikes
- **DESPERATION** (low HP): Emotional stakes, grit through pain

## Death & Resurrection System

### 0 HP = Downed (Not Dead)

**When character reaches 0 HP**:
- Character is **Downed** (unconscious, not dead)
- Falls prone, cannot take actions
- **Begin Death Saves** immediately
- Enemies may ignore downed characters or attack to finish them

**Death Saves (1d20 per turn while Downed)**:
- **10+** = Success (mark 1 success)
- **1-9** = Failure (mark 1 failure)
- **Natural 20** = Instant stabilization at 1 HP (regain consciousness)
- **Natural 1** = Counts as 2 failures
- **3 Successes** = Stabilized (unconscious but alive, 0 HP, stable)
- **3 Failures** = **DEAD**

**Damage While Downed**:
- **Any damage** = 1 automatic death save failure
- **Critical hit** = 2 automatic death save failures
- **Massive damage** (single attack ≥ max HP) = Instant death (no saves)

**Stabilization**:
- Medicine check (DC 10) = stabilize downed ally (uses action)
- Healing magic/potion = restore HP, regain consciousness
- Stabilized characters remain unconscious until healed or 1d4 hours pass (wake at 1 HP)

### Injury System

**When character fails 2+ death saves before stabilizing**, roll on Injury Table:

| d20 | Injury | Effect | Duration |
|-----|--------|--------|----------|
| 1-4 | **Minor Wound** | -2 to all rolls | Until long rest |
| 5-8 | **Concussion** | Disadvantage on INT/WIS checks | 3 days |
| 9-11 | **Broken Bone** | -5 movement, -2 physical rolls | 1 week |
| 12-14 | **Internal Injury** | Max HP -20% | 2 weeks |
| 15-17 | **Severed Tendon** | Cannot use one limb/hand | 1 month + surgery |
| 18-19 | **Permanent Scar** | -1 to one stat (permanent) | Permanent |
| 20 | **Close Call** | No lasting injury (lucky!) | - |

**Treatment**: Medical care, healing magic, or downtime reduces duration by 50%. High-tier healing (Regeneration, Greater Restoration) removes injuries instantly.

### Resurrection Costs

**When character dies (3 failed death saves or instant death)**:

**Tier 1 - Revivify** (within 1 minute):
- **Cost**: Diamond worth 300 gold (consumed)
- **Penalty**: None (quick resurrection)
- **Limit**: Body intact, soul willing

**Tier 2 - Raise Dead** (within 10 days):
- **Cost**: Diamond worth 500 gold (consumed)
- **Penalty**: -4 to all rolls for 4 days (resurrection sickness)
- **Limit**: Body mostly intact, soul willing

**Tier 3 - Resurrection** (within 100 years):
- **Cost**: Diamond worth 1000 gold (consumed) + 1000 XP penalty
- **Penalty**: -4 to all rolls for 1 week, max HP -10% permanently (until Greater Restoration)
- **Limit**: Any body part, soul willing

**Tier 4 - True Resurrection** (any time):
- **Cost**: Diamond worth 25,000 gold (consumed) + 5000 XP penalty
- **Penalty**: -4 to all rolls for 2 weeks
- **Limit**: Soul willing (no body required)

**Anime World Variants**:
- **Dragon Ball senzu beans** = instant stabilization (no death saves)
- **Re:Zero Return by Death** = automatic resurrection at save point (memory intact, XP penalty)
- **One Piece willpower** = 1/session, survive lethal damage at 1 HP if narratively appropriate
- **Konosuba Aqua** = free resurrection (but party debt increases by cost)

### Death Narrative Protocol

**When character reaches 0 HP**, narrate **Downed** state (not death):
- "Your vision BLURS, legs give out—you COLLAPSE. Everything goes dark. [DOWNED - Begin Death Saves]"
- **NOT**: "You die." (premature, breaks system)

**During Death Saves**, create tension:
- Success: "You GASP—clinging to life. [1 success, 0 failures]"
- Failure: "Darkness closes in. Your heartbeat SLOWS. [0 successes, 1 failure]"
- Natural 20: "Your eyes SNAP OPEN—willpower SURGES! You're alive! [Stabilized at 1 HP]"
- 3 Failures: "Your heart stops. Everything goes silent. [DEAD]"

**After Resurrection**, narrate return with cost:
- "Light burns your eyes. You GASP—lungs screaming. You're alive... but changed. [Resurrection sickness: -4 to rolls for 4 days]"

## Combat Maneuvers

**Advanced combat actions** beyond basic attack/defend.

### Grapple

**Action**: Attempt to grab and restrain target
**Roll**: Contested check (your STR vs target's STR or DEX, target chooses)
**Success**: Target is **Grappled** (speed 0, disadvantage on attacks)
**Maintain**: Use action each turn to maintain grapple (new contest)
**Escape**: Target uses action to contest (STR/DEX vs your STR)
**Size Limit**: Cannot grapple creatures 2+ sizes larger

**Example**: "I grapple the assassin!" → Roll STR 15, assassin rolls DEX 12 → Success → "You TACKLE the assassin, pinning them! [Grappled: Speed 0]"

### Disarm

**Action**: Knock weapon from target's hand
**Roll**: Attack roll at **Disadvantage** (vs target's AC)
**Success**: Weapon flies 10 feet away (target's choice of direction)
**Retrieve**: Target must use movement + action to pick up weapon
**Note**: Unarmed target cannot be disarmed

**Example**: "I disarm the knight!" → Roll 12 (disadvantage) vs AC 15 → Miss → "The knight TWISTS, blade stays firm!"

### Called Shot

**Action**: Target specific body part for special effect
**Roll**: Attack roll at **-5 penalty**
**Success**: Deal normal damage + special effect based on target:

| Target | Effect |
|--------|--------|
| **Head** | Disadvantage on next attack/spell |
| **Arm** | Drop held item (no save) |
| **Leg** | Speed halved until end of next turn |
| **Eyes** | Blinded until end of next turn |
| **Weak Point** | Extra 1d6 damage (DM discretion) |

**Example**: "Called shot to the leg!" → Roll 13 (18 - 5) vs AC 15 → Miss → "Arrow grazes thigh, ogre unfazed!"

### Aid

**Action**: Help ally with next action
**Roll**: No roll required (uses your action)
**Effect**: Ally gains **Advantage** on next roll (attack/skill/save, their choice)
**Duration**: Until ally's next roll or end of their next turn
**Teamwork**: Describe how you help ("I feint left, drawing enemy's guard!")

**Example**: "I Aid my ally's attack!" → Ally attacks with Advantage → "You DISTRACT the troll, ally strikes exposed flank! [Advantage]"

## Tournament Framework

**For tournament arcs, competitions, and organized combat events.**

### Tournament Structure

**Setup**:
1. **Participants**: Minimum 4, maximum 64 (power of 2 for clean brackets)
2. **Bracket Type**: Single elimination (1 loss = out), Double elimination (2 losses = out), Round robin (everyone fights everyone)
3. **Rules**: Win condition (knockout, surrender, ring out, points), forbidden actions, time limits
4. **Stakes**: Prize (gold, item, title), reputation, quest objectives

### Seeding Mechanics

**Determine tournament seeds** (1 = strongest, higher number = weaker):
- **Known NPCs**: Rank by level, reputation, or narrative importance
- **Unknown Opponents**: Assign based on preliminary rounds or random draw
- **Player Character**: Seed based on level + reputation (adjust narratively)

**Bracket Pairing**:
- **Seed 1 vs Seed 16**, Seed 8 vs Seed 9 (standard tournament seeding)
- **Random Draw**: Chaos option (any vs any, narratively dramatic)
- **Rigged Brackets**: Corrupt organizers favor certain fighters

### Match Flow

**Pre-Match**:
1. **Announce matchup**: "NEXT MATCH: [Player] vs [Opponent]!"
2. **Opponent introduction**: Describe fighter (appearance, reputation, style)
3. **Spectator reactions**: Crowd betting, cheering, jeering
4. **Last preparations**: Buff spells, equipment check, strategy

**Combat**:
- Run combat using standard rules
- **Special Rules**: Apply tournament restrictions (no lethal damage, ring boundaries, etc.)
- **Crowd Reactions**: Cheer epic moments, gasp at reversals, boo dirty tactics
- **Commentary**: Optional announcer narration for hype

**Post-Match**:
1. **Victory/Defeat**: Apply tournament rules (winner advances, loser eliminated)
2. **Injuries**: Check injury table if applicable (or tournament healers restore HP)
3. **Rest Period**: Time until next match (see Fatigue below)

### Between-Match Fatigue

**Fatigue Tracking** (for realism, optional):
- **Immediate Next Match** (< 10 minutes rest): -2 to all rolls, -20% max HP/MP/SP
- **Short Rest** (30 minutes): -1 to all rolls, -10% max resources
- **Long Rest** (2+ hours): Full recovery (tournament healers restore HP/MP/SP)

**Anime Tournament Variants**:
- **Shonen Rules** (DBZ, Naruto): No fatigue, injuries heal instantly between matches (spectacle > realism)
- **Realistic Rules** (HxH): Fatigue accumulates, injuries carry over (strategy matters)
- **Healer Station**: Tournament provides healing but costs gold/favors/plot hooks

### Bracket Management

**Track tournament progress**:
```
ROUND 1 (8 matches):
- Match 1: Kael vs Zara → Kael wins
- Match 2: Grimjaw vs Tessa → Grimjaw wins
- [... 6 more matches ...]

ROUND 2 (4 matches):
- Match 1: Kael vs Grimjaw → [pending]
- Match 2: [winner 3] vs [winner 4] → [pending]
```

**Narrative Shortcuts**:
- **Skip Minor Matches**: "The preliminaries pass quickly. You defeat three opponents without trouble. Now, the semi-finals..."
- **Montage**: "The bracket advances. You watch rival fighters: Grimjaw crushes opponents with brute force, Sylara wins via trickery..."
- **Timeskip to Key Fights**: Focus on narratively important matches (rival battle, final, upset)

### Spectator Reactions

**Crowd Dynamics** (add flavor to matches):
- **Underdog Support**: "The crowd ROARS as you land a hit! 'KAEL! KAEL! KAEL!'"
- **Favorites**: "Grimjaw's fans chant his name, drowning out your supporters."
- **Upset Shock**: "The arena goes SILENT. No one expected you to win..."
- **Epic Moments**: "The crowd EXPLODES! Half leap to their feet, others throw coins into the ring!"

**Betting Subplot** (optional):
- NPCs bet on matches (quest hooks: throw match for gold? prove bookies wrong?)
- Player can bet on own matches (confidence booster or narrative pressure)
- Odds shift based on performance (dominating early = lower payouts later)

### Tournament Outcomes

**Victory**:
- Award prize (gold, magic item, title, reputation boost)
- Create memory thread (CORE or QUESTS category, high heat)
- Update world_state (NPC reactions, tournament results known, fame increases)
- Plot hooks (rivals, sponsors, enemies)

**Defeat**:
- Apply consequences (injury, reputation hit, quest failure)
- Spectator reactions (some sympathetic, others mocking)
- Narrative opportunities (training arc unlocked, rematch quest, humble character growth)

**Example Tournament Arc** (Hunter x Hunter style):
- **Setup**: Heaven's Arena (200 floors, win = advance, lose 4× = eliminated)
- **Opponents**: Escalating difficulty (Floor 1-50 = easy, 100-150 = medium, 200 = boss-tier)
- **Fatigue**: Realistic (injuries persist, must rest between floors)
- **Spectacle**: Huge crowds, commentators, betting, floor masters with unique abilities
- **Stakes**: Reach Floor 200 = master title + prize money + plot advancement (Nen unlocked)

## Victory & Defeat Narration (Session Analysis Fix #5)

**Problem**: Generic endings ("boss collapses, you win") lack visceral detail, environmental impact, emotional weight.

**Victory Protocol (4 elements)**:

1. **Visceral Death**: Show exact moment with sensory details (unraveling/exploding/collapsing/disintegrating + sound/light/smell)
2. **Environmental Impact**: Battlefield changes (2-3 specific: cracked floor, scorched walls, blood, magical residue)
3. **Emotional Beat via Action**: Show triumph/exhaustion through physical action, NOT narration ("legs give out" not "you feel victorious")
4. **Transition Hook**: Loot discovery/sound/NPC/environmental change \u2192 Question for player

**Major Bosses Add**: World Reaction (cosmic significance: constellations, magical disturbances, NPC reactions off-screen, foreshadowing)

**Defeat Protocol (3 elements)**:

1. **How Defeat Happens**: Visceral description (bones crack, vision blurs, etc.)
2. **Downed/Death State**: Apply death save system (not instant death unless massive damage)
3. **Player Agency**: Always give choice after defeat (ally revives? retreat? resurrection?)

## Integration

Coordinates with: State Manager (03) - atomic HP/MP/SP/inventory updates | Progression (09) - XP/level-ups | Learning Engine (02) - COMBAT memory threads | NPC Intelligence (04) - ally reactions

## Module Completion Criteria

Module functioning when: Turn-based combat strategic+fair, damage accurate+balanced, status effects tracked, boss battles epic+narrative, combat narration cinematic, resource costs enforced, victory/defeat meaningful.

## Common Mistakes

**[NO] Boring Narration**: "Goblin attacks. 12 damage. Your turn." (spreadsheet math)

**[OK] Cinematic**: "The goblin ROARS, axe whistling. [Roll: 18 vs Defense 16 - HIT] Blade bites your shoulder. Blood sprays. [12 damage: 133→121] What do you do?"

**[NO] Ignoring Costs**: Player uses skill, AIDM forgets MP/HP cost (balance breaks)

**[OK] Enforce Costs**: "Life Transfer 50 HP? That's 50 YOUR HP. (Current: 121/145)" [Applies atomically: -50 player, +50 ally]

**End of Module 08**

*Next: 09_progression_systems.md (Leveling & Advancement)*
