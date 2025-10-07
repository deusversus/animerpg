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
2. **Immediate Consequences**: Depends on tone (regression/second chance, high stakes/loot lost+time passed, permadeath/game over)
3. **Player Agency**: Always give choice after defeat (retry? retreat? different approach?)

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
