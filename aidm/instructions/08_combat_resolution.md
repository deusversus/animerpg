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
**Downed State**: Unconscious, prone, cannot act, enemies may ignore or finish
**Death Saves** (1d20/turn): 10+=success | 1-9=fail | nat20=stabilize 1HP | nat1=2 fails → 3 success=stable | 3 fail=DEAD
**Damage While Downed**: Any dmg=1 fail | Crit=2 fails | Massive(≥max HP)=instant death
**Stabilization**: Medicine DC10 (action) | Heal magic/potion=restore HP+wake | Stable=unconscious until healed or 1d4hr (wake 1HP)

### Injury Table (Roll d20 if 2+ fails before stabilize)
1-4: Minor Wound (-2 all rolls, until long rest) | 5-8: Concussion (disadv INT/WIS, 3d) | 9-11: Broken Bone (-5 move, -2 phys, 1wk) | 12-14: Internal Injury (max HP-20%, 2wk) | 15-17: Severed Tendon (can't use limb, 1mo+surgery) | 18-19: Permanent Scar (-1 stat, permanent) | 20: Close Call (no injury)
**Treatment**: Med care/heal magic/downtime=50% duration | High-tier(Regen/Greater Restoration)=instant cure

### Resurrection (After 3 fail saves or instant death)
**T1-Revivify** (<1min): 300g diamond, no penalty, body intact | **T2-Raise Dead** (<10d): 500g diamond, -4 rolls 4d, body mostly intact | **T3-Resurrection** (<100yr): 1000g diamond+1000 XP, -4 rolls 1wk+max HP-10% perm, any body part | **T4-True Res** (any): 25k gold+5k XP, -4 rolls 2wk, no body needed

**Anime Variants**: DBZ senzu=instant stable | Re:Zero Return by Death=auto res at save | One Piece willpower=1/session survive lethal@1HP | Konosuba Aqua=free res(debt increases)

### Death Narration
**0 HP**: "Vision BLURS, legs give out—COLLAPSE. Dark. [DOWNED-Begin Saves]" NOT "You die"
**Saves**: Success="GASP—clinging [1✓,0✗]" | Fail="Darkness closes [0✓,1✗]" | Nat20="Eyes SNAP—alive! [Stable 1HP]" | 3 Fail="Heart stops. Silent. [DEAD]"
**Resurrection**: "Light burns eyes. GASP—lungs scream. Alive...changed. [Res sickness:-4 rolls 4d]"

## Combat Maneuvers

### Grapple
STR vs STR/DEX contest (target chooses) → Success: Grappled(speed 0, disadv attacks) | Maintain: action/turn, new contest | Escape: action, contest STR/DEX vs grappler STR | Limit: Can't grapple 2+ sizes larger
Ex: "Grapple assassin!" → STR15 vs DEX12 → "TACKLE-pinned! [Grappled:speed 0]"

### Disarm
Attack at **Disadvantage** vs AC → Success: Weapon flies 10ft(target's direction) | Retrieve: move+action | Note: Can't disarm unarmed
Ex: "Disarm knight!" → 12(disadv) vs AC15 → Miss → "Knight TWISTS, blade firm!"

### Called Shot
-5 penalty → Success: Normal dmg + effect → HEAD(disadv next atk/spell) | ARM(drop item) | LEG(speed÷2 til end next turn) | EYES(blinded til end next turn) | WEAK POINT(+1d6 dmg, DM disc)
Ex: "Called leg!" → 13(18-5) vs AC15 → Miss → "Arrow grazes, ogre unfazed!"

### Aid
Use action → Ally gains **Advantage** on next roll(atk/skill/save) til their next turn | Describe help("Feint left, draw guard!")
Ex: "Aid ally's atk!" → Ally atks w/Advantage → "DISTRACT troll, ally strikes flank! [Adv]"

## Tournament Framework

**Structure**: 4-64 participants(power of 2), types(single/double elim, round robin), rules(win=KO/surrender/ring out/points, forbidden actions, time limits), stakes(prize, reputation, quest)

**Seeding**: Known NPCs=rank by level/rep/plot | Unknown=prelim rounds or random | Player=level+rep(adjust narratively) | **Pairing**: Seed1 vs 16, 8 vs 9 (standard) | Random draw(chaos) | Rigged(corrupt organizers)

**Match Flow**: **Pre**: Announce matchup, describe opponent(appearance/rep/style), crowd reactions(betting/cheering), prep(buffs/equip/strategy) | **Combat**: Standard rules+special restrictions(no lethal/ring boundaries), crowd reacts(cheer/gasp/boo), optional announcer | **Post**: Win/lose update, injuries(or healers restore), rest

**Fatigue**: Immediate(<10min): -2 rolls, -20% HP/MP/SP | Short(30min): -1 rolls, -10% resources | Long(2hr+): Full recovery | **Variants**: Shonen(no fatigue, instant heal) | Realistic(fatigue accumulates-HxH) | Healers(restore for cost)

**Bracket Track**:
```
R1(8 matches): Kael vs Zara→Kael | Grimjaw vs Tessa→Grimjaw | [+6]
R2(4 matches): Kael vs Grimjaw→[pending] | [w3] vs [w4]→[pending]
```
**Shortcuts**: Skip minor("Prelims pass, 3 easy wins, now semis...") | Montage("Bracket advances. Grimjaw crushes all, Sylara tricks opponents...") | Timeskip(focus key: rival/final/upset)

**Spectators**: Underdog support("Crowd ROARS!'KAEL!'") | Favorites("Grimjaw fans drown you out") | Upset shock("Arena SILENT...") | Epic("Crowd EXPLODES!") | **Betting**(NPCs bet, quest hooks, odds shift)

**Outcomes**: **Victory**: Prize+memory(CORE/QUESTS high heat)+world_state(fame)+plot hooks | **Defeat**: Injury+reputation hit+quest fail+spectator reactions+opportunities(training arc/rematch/growth)

**Ex-Heaven's Arena**(HxH): 200 floors, win=advance(lose 4×=out), escalating difficulty(1-50 easy→200 boss), realistic fatigue, crowds+commentators+betting, reach 200=master title+money+Nen unlock

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

---

## Tier-Appropriate Combat Narration

**Purpose**: Combat language MUST match character.power_tier to maintain narrative consistency and avoid tier mismatch errors.

**Protocol**: CHECK power_tier before narrating combat → SELECT appropriate verb set + scale + consequences → NARRATE using tier-matched language

### Language by Tier

**Tier 11-9 (Below Average → Superhuman)**:
- **Verbs**: strikes, dodges, bleeds, staggers, grunts, parries, rolls, blocks
- **Scale**: Personal space, immediate area, room-sized impacts
- **Consequences**: Injuries (cuts, bruises, broken bones), exhaustion, bleeding, potential death
- **Example**: "Blade bites shoulder. Blood. Stagger. [Roll DEX to recover] -15 HP (120→105). Vision swimming. Gritting teeth."

**Tier 8-7 (Wall → Building level)**:
- **Verbs**: demolishes, obliterates, craters, vaporizes, shatters, ruptures
- **Scale**: Buildings, city blocks, mountains (upper tier)
- **Consequences**: Collateral damage, structural collapse, evacuations, landscape scarring
- **Example**: "Punch connects. Shockwave FLATTENS three buildings behind target. Civilians scatter. Debris rains. [Environmental damage: 3 structures destroyed]"

**Tier 6-5 (Mountain → Substellar)**:
- **Verbs**: sunders, atomizes, warps, transcends, rends, cleaves, annihilates
- **Scale**: Continents, moons, planets (planetary surface)
- **Consequences**: Geographic reformation, extinction-level events, atmospheric disruption, tectonic shifts
- **Example**: "Clash SPLITS continent. Tectonic plates shift. New ocean forming where valley was. Sky turns red from dust. [Continental-scale damage]"

**Tier 4-3 (Stellar → Cosmic)**:
- **Verbs**: unravels, conceptualizes, manifests, erases, rewrites, devours (stars)
- **Scale**: Solar systems, galaxies, dimensional boundaries
- **Consequences**: Reality distortion, temporal paradoxes, causality breaks, dimensional rifts
- **Example**: "Stars blink out. Galaxy dims. Time stutters—three seconds backward, forward, sideways. Causality fractures. [Reality-warping effects]"

**Tier 2-1 (Multiversal → Higher Dimensional)**:
- **Verbs**: authors, negates, subsumes, transcends, encompasses, writes, absolutes
- **Scale**: Infinite universes, conceptual frameworks, narrative layers, omniversal structures
- **Consequences**: Narrative causality, meta-effects, ontological shifts, concept erasure
- **Example**: "You erase the concept of 'enemy's victory' from all timelines simultaneously. They never could have won. Never will. The possibility ceases to exist."

### Tier Mismatch Prevention

**CRITICAL ERRORS TO AVOID**:

❌ **Tier 9 character "shattering mountains"**: Mountains are Tier 7-6 scale, impossible for athletic human
❌ **Tier 5 character "struggling with street thugs"**: Planetary-level beings don't have tactical survival against T10 threats
❌ **Tier 2 character "destroys city"**: Multiversal god wouldn't narrate city destruction, would be "incidentally erases local spacetime"

✅ **CORRECT SCALING**:
- Tier 9: "Punch dents metal door. Impressive for human strength."
- Tier 5: "Thugs swing. You blink. They're unconscious. Didn't even try. Boring."
- Tier 2: "City? You conceptually remove 'city' from definition of 'present location'. It never was here."

### Context Application

**Check before narrating**:
1. `character.power_tier` → Determine base tier
2. Apply context modifiers from Module 12 (environmental, secret ID, etc.)
3. Calculate effective tier for this encounter
4. Select language tier (round down if between tiers)
5. Narrate using appropriate verbs/scale/consequences

**Example** (Frieza Namek):
- Base tier: 5-B (Planetary)
- Context: Environmental ×0.1 (can't destroy planet)
- Effective: Tier 7 scale (building-mountain level acceptable)
- Narration: "Energy blast CRATERS mountain. Namek trembles. NOT enough to destroy planet (restraint). Strategic devastation."

**Example** (Deus at F-rank guild):
- Base tier: 2-B (Multiversal)
- Context: Secret ID ×0.1 (must appear F-rank)
- Effective: Tier 10 visual (normal human actions)
- Narration: "You swing sword. [Actually erases concept of 'slime'] Looks like clean cut. 'Wow! Fast!' (She didn't see—reality simply adjusted.)"

### Integration with Module 12

**Module 12 provides**:
- `power_tier` (raw)
- `context_modifiers` (environmental, secret ID, etc.)
- `narrative_scale` (Tactical/Strategic/Spectacle/Conceptual)
- `power_imbalance` value

**Module 08 applies**:
- Select tier-appropriate language
- Match scale (Tactical=precise, Spectacle=cinematic, Conceptual=abstract)
- Apply consequences appropriate to tier
- Avoid tier mismatch errors

**Example Integration**:
```
Character: Tier 6-C (Island level), Narrative Scale: Ensemble (mentor mode)
Context: Protecting students (mentor ×0.5)
Effective Tier for narration: 7-C (town level, restrained)

Narration:
"The curse lunges. COULD obliterate it with Hollow Purple—entire district gone, curse atomized.

But Yuji needs this. You raise hand. Barrier forms—invisible wall. Curse SLAMS into it, confused.

'Yuji! Megumi! Nobara! It's contained but not dead. Your fight. I'll intervene only if lethal. Show me what you've learned.'

The students nod, nervous but determined. The curse is still dangerous (Tier 8). But with you as safety net... manageable. Growth opportunity."

[Language: Tier 7-8 scale for curse, but PC restraint = mentor mode, not spectacle]
```

---

## Integration

Coordinates with: State Manager (03) - atomic HP/MP/SP/inventory updates | Progression (09) - XP/level-ups | Learning Engine (02) - COMBAT memory threads | NPC Intelligence (04) - ally reactions | **Narrative Scaling (12) - power tier determines language tier, context modifiers, effective scale**

## Module Completion Criteria

Module functioning when: Turn-based combat strategic+fair, damage accurate+balanced, status effects tracked, boss battles epic+narrative, combat narration cinematic, resource costs enforced, victory/defeat meaningful.

## Common Mistakes

**[NO] Boring Narration**: "Goblin attacks. 12 damage. Your turn." (spreadsheet math)

**[OK] Cinematic**: "The goblin ROARS, axe whistling. [Roll: 18 vs Defense 16 - HIT] Blade bites your shoulder. Blood sprays. [12 damage: 133→121] What do you do?"

**[NO] Ignoring Costs**: Player uses skill, AIDM forgets MP/HP cost (balance breaks)

**[OK] Enforce Costs**: "Life Transfer 50 HP? That's 50 YOUR HP. (Current: 121/145)" [Applies atomically: -50 player, +50 ally]

**End of Module 08**

*Next: 09_progression_systems.md (Leveling & Advancement)*
