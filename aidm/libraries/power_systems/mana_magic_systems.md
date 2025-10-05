# Mana & Magic Systems (External Energy)

## Purpose

This library provides AIDM with generalized frameworks for **mana-based and magic systems** commonly found in anime. These systems are characterized by **external energy manipulation** - drawing power from the environment, arcane sources, or metaphysical forces outside the practitioner's body.

**Coverage**: ~30-35% of anime power systems (Fairy Tail, Black Clover, Overlord, Mushoku Tensei, Frieren, Konosuba, Re:Zero, etc.)

**Use This Library When**:
- Player wants spell-casting, elemental magic, or arcane powers
- World features mages, wizards, sorcerers, or magic academies
- Power source is environmental (ley lines, mana atmosphere, magical items)
- System emphasizes resource management (MP pools, spell slots)

---

## Core Characteristics

### What Defines External Energy Systems

**Energy Source**: Outside the practitioner
- Ambient mana in atmosphere
- Ley lines and magical hotspots
- Enchanted items and artifacts
- Divine/demonic pacts
- Ritual circles and magical infrastructure

**Mechanics**:
- **Resource Pool**: Mana/MP bar that depletes and regenerates
- **Knowledge-Based**: Requires learning spells, studying grimoires
- **Environmental Interaction**: Stronger in certain locations/conditions
- **Tool-Dependent**: Wands, staves, catalysts enhance performance
- **Structured**: Spell schools, tiers, affinities

**Narrative Role**:
- Scholarly pursuit (magic academies, research)
- Social stratification (those with/without magical talent)
- Environmental impact (mana pollution, magical disasters)
- Ancient knowledge (lost spells, forbidden magic)

---

## Common Anime Examples

### High-Magic Fantasy
**Fairy Tail**: Elemental magic, transformation, celestial spirits  
**Black Clover**: Grimoire-based magic, anti-magic  
**Magi**: Djinn metal vessels, magoi manipulation  
**The Irregular at Magic High School**: Structured modern magic system

### Isekai Magic
**Overlord**: D&D-style tiered spells, divine/arcane split  
**Mushoku Tensei**: Chantless casting, elemental schools  
**Konosuba**: RPG-style spell learning, MP management  
**Re:Zero**: Gate-based magic, elemental affinities

### Magitech
**Fullmetal Alchemist**: Alchemy (equivalent exchange)  
**Fate Series**: Magecraft, reality marbles, noble phantasms  
**A Certain Magical Index**: Esper powers (scientific magic)

---

## System Framework Components

### 1. Mana Pool & Regeneration

**Resource Management**:
- **MP (Mana Points)**: Numerical pool that depletes with spell use
- **Regeneration Rate**: Passive recovery (often time-based)
- **Environmental Factors**: Recover faster near ley lines, slower in mana-dead zones
- **Items**: Mana potions, ethers, magical food

**AIDM Integration**:
```markdown
**MP Pool**: Current MP / Max MP (e.g., 450/600)
**Regeneration**: +10 MP per turn (or +5% per hour narrative time)
**Environmental Modifier**: +50% regeneration near ancient shrine
```

**Example (Black Clover style)**:
- Mana Pool increases with training/leveling
- Depleted mana = physical exhaustion
- Overuse risks "mana burn" (temporary HP damage)

---

### 2. Spell Schools & Affinities

**Common Categorization**:

**A. Elemental Schools** (Most Common)
- **Fire**: Offense, destruction, passion
- **Water**: Defense, healing, adaptability
- **Earth**: Fortification, endurance, stability
- **Wind**: Speed, precision, freedom
- **Lightning**: Power, speed, aggression
- **Ice**: Control, preservation, isolation
- **Light**: Healing, purification, revelation
- **Dark**: Curses, necromancy, concealment

**B. Conceptual Schools**
- **Creation Magic**: Summon objects, creatures, barriers
- **Destruction Magic**: Pure damage, disintegration
- **Transmutation**: Change properties, alchemy
- **Enchantment**: Buff/debuff, mind control
- **Divination**: Foresight, detection, scrying
- **Necromancy**: Undead, life/death manipulation
- **Spatial Magic**: Teleportation, pocket dimensions
- **Time Magic**: Slow/haste, time stop (usually rare)

**C. Hybrid/Unique**
- Blood Magic (HP as resource)
- Rune Magic (inscribed patterns)
- Ritual Magic (preparation-heavy)
- Contract Magic (spirit/demon pacts)

**AIDM Integration**:
```markdown
**Affinity**: Fire (Primary), Wind (Secondary)
**Known Schools**: Evocation, Transmutation
**Restricted Schools**: Necromancy (forbidden), Time (innate talent required)
```

---

### 3. Spell Tier System

**Progressive Power Scaling**:

**Tier 1 (Novice)**: 5-20 MP
- Cantrips, basic utility
- Examples: Fireball, Water Splash, Light, Detect Magic
- Cooldown: None (spammable)

**Tier 2 (Apprentice)**: 20-50 MP
- Combat-viable, minor effects
- Examples: Ice Lance, Lightning Bolt, Shield, Minor Heal
- Cooldown: 1-3 turns

**Tier 3 (Adept)**: 50-100 MP
- Battlefield control, significant damage
- Examples: Meteor Strike, Blizzard, Summon Elemental, Major Heal
- Cooldown: 3-5 turns

**Tier 4 (Master)**: 100-200 MP
- Game-changing, area effects
- Examples: Flame Storm, Gravity Well, Teleportation Circle, Resurrection
- Cooldown: Once per encounter

**Tier 5 (Archmage)**: 200-500+ MP
- Strategic, cataclysmic
- Examples: Meteor Swarm, Time Stop, Mass Resurrection, Wish
- Cooldown: Once per day/session

**Tier 6+ (Legend/God)**: 500+ MP
- World-altering, plot-significant
- Examples: Continent-shattering magic, reality rewriting, divine intervention
- Cooldown: Once per arc

**AIDM Notes**:
- Lower tiers scale with INT or magical stat
- Higher tiers may require specific conditions (ritual preparation, rare components)
- Boss enemies may have access to higher tiers than level suggests

---

### 4. Casting Mechanics

**A. Chanting vs. Chantless**

**Chanted Casting** (Traditional):
- Requires verbal component (full incantation)
- Longer cast time = higher power/accuracy
- Interrupted if silenced or disrupted
- Examples: Fairy Tail, most classic fantasy

**Chantless Casting** (Advanced):
- Silent, instant activation
- Requires mastery (reduced power initially)
- Cannot be disrupted by silence
- Examples: Mushoku Tensei, skilled mages

**AIDM Integration**:
```markdown
**Chanted**: 1 turn charge, full power
**Shortened Chant**: Instant, 75% power
**Chantless**: Instant, 50% power (or mastery-dependent)
```

**B. Catalysts & Foci**

**Staff/Wand**: +20% spell power, reduces MP cost by 10%  
**Grimoire**: Unlocks access to stored spells  
**Orb/Crystal**: Enhances specific element (+30% fire damage)  
**Runestone**: Enables ritual magic  
**No Catalyst**: Full MP cost, -20% power (untrained)

**C. Environmental Factors**

- **Ley Line Nexus**: +50% power, -30% MP cost
- **Mana-Dead Zone**: -50% power, +50% MP cost
- **Elemental Terrain**: +30% matching element (fire in volcano)
- **Weather**: Storm enhances lightning, rain weakens fire
- **Time of Day**: Lunar magic stronger at night, solar at noon

---

### 5. Magic System Variations

**A. Grimoire-Based** (Black Clover)
- Personal grimoire unlocks at maturity
- Grimoire pages unlock with experience/emotion
- Number of clovers = magical potential
- Lost grimoire = severe power reduction

**B. Tiered Spell Slots** (Overlord, D&D-style)
- Fixed slots per tier (e.g., 4x Tier 1, 3x Tier 2, 2x Tier 3)
- Slots regenerate after rest
- Metamagic options (quicken, empower, extend)

**C. Elemental Awakening** (Avatar-style)
- Start with one element, unlock others through training
- Master level = sub-elements (ice from water, lightning from fire)
- Avatar/Legend = access to all elements

**D. Magitech Integration** (Fate, Index)
- Magic formulas as scientific equations
- Programmable spells (magic circuits, code)
- Technology enhances/replaces traditional casting

**E. Contract Magic** (Various)
- Summon spirits/demons via pact
- Spirit bears MP cost and provides power
- Breaking contract = severe consequences

---

## Integration Guidelines

### Harmonizing with Other Power Systems

**Mana + Ki (Internal Energy)**:
- **Compatible**: Mages can learn body enhancement (ki) for defense
- **Separate Pools**: MP and Ki are distinct resources
- **Hybrid Builds**: Spellblade (magic + martial), Monk-Mage (rare)
- **Example**: Rimuru (Slime) uses magic + physical skills

**Mana + Soul/Spirit**:
- **Overlap**: Necromancy, spirit summoning blur the line
- **Clarification**: Mana fuels the spell, soul/spirit is the target/source
- **Example**: Bleach (spiritual pressure + kido spells)

**Mana + Psionic**:
- **Rare Overlap**: Telepathy can be magic spell or psionic talent
- **Distinguish**: Magic = learned, external. Psionic = innate, mental.
- **Example**: Index (magic vs. esper powers are incompatible)

**AIDM Rule**: If player mixes systems, establish clear boundaries early (Session 0) to prevent confusion.

---

### Creating Original Magic Systems

**Template for Custom Systems**:

1. **Define Energy Source**: Where does mana come from?
   - Ambient atmosphere? Ley lines? Gods? User's lifespan?

2. **Resource Mechanics**: Pool, slots, or cooldown-based?
   - Traditional MP bar, spell slots, or unlimited with cooldowns?

3. **Acquisition Method**: How do users learn magic?
   - Study grimoires? Inherit bloodline? Divine blessing? Contract?

4. **Power Scaling**: Tiers, levels, or freeform?
   - Structured tiers (1-10), level-based, or narrative power?

5. **Unique Restriction**: What makes it interesting?
   - Elemental affinities? Chanting requirements? Physical cost?

6. **Failure State**: What happens if misused?
   - Mana burn? Explosion? Cursed? Demonic corruption?

**Example Custom System** (Player creates "Fate-weaving Magic"):
- **Source**: Threads of destiny in metaphysical plane
- **Mechanics**: 3 spell slots per "fate tier", regenerate at story milestones
- **Acquisition**: Born with "Weaver's Eye" (rare genetic trait)
- **Scaling**: 5 tiers (Thread → Rope → Chain → Tapestry → Loom of Fate)
- **Restriction**: Cannot alter own fate directly
- **Failure**: Severed threads cause paradox damage (HP loss)

---

## Common Tropes & Story Hooks

### Character Archetypes
- **Prodigy**: Natural talent, progresses rapidly (Asta's rival Yuno)
- **Late Bloomer**: Weak initially, explosive growth (Asta with anti-magic)
- **Specialist**: Master of one school, weak in others (fire-only mage)
- **Archmage**: Already powerful, mentor role (Ainz, Frieren)
- **Forbidden User**: Dark/illegal magic, hunted (necromancer, blood mage)

### Story Hooks
- **Magic Academy Arc**: Learn magic, school politics, tournaments
- **Forbidden Spell**: Powerful magic with terrible cost
- **Mana Crisis**: World's mana depleting, magic dying
- **Ancient Grimoire**: Lost knowledge, dangerous if misused
- **Magic vs. Technology**: Clash between traditional magic and modern science
- **Elemental Imbalance**: One element dominates, seeking balance

### Social Dynamics
- **Caste System**: Magical talent = nobility (Black Clover)
- **Magic Guilds**: Organizations control magic usage (Fairy Tail)
- **Outlawed Schools**: Certain magic types banned (necromancy)
- **Magical Items**: Rare artifacts create power imbalance

---

## AIDM Implementation Examples

### Example 1: Traditional Fantasy Mage

**Player Request**: "I want to be a fire mage like Natsu"

**AIDM Response**:
```markdown
**Power System: Elemental Magic (Fire Affinity)**

**Mana Pool**: 200 MP (INT-based, scales with level)
**Regeneration**: +10 MP/turn, +15 MP/turn near fire sources
**Affinity**: Fire (Primary), Lightning (Potential Secondary)

**Starting Spells**:
- [Tier 1] **Flame Burst**: 15 MP, 2d6 fire damage, ranged
- [Tier 1] **Warm Touch**: 10 MP, minor heal (fire regenerates)
- [Tier 2] **Fire Fist**: 30 MP, 4d6 fire damage, melee enhancement
- [Tier 2] **Flame Shield**: 25 MP, +3 AC, burns attackers (1d4)

**Growth Path**: Unlock Tier 3 spells at level 5, Tier 4 at level 10
**Unique Trait**: "Dragon Slayer Magic" variant (consume fire to regenerate MP)
```

### Example 2: Grimoire-Based System

**Player Request**: "I want a magic book like Black Clover"

**AIDM Response**:
```markdown
**Power System: Grimoire Magic**

**Grimoire**: Three-Leaf Clover (average magical talent)
**Pages Unlocked**: 12/100 (unlocks via experience + emotional growth)
**Mana Pool**: 300 MP

**Current Pages**:
- **Page 1**: [Basic Elements] - Fire/Water/Earth/Wind cantrips
- **Page 5**: [Shield of Faith] - Defensive barrier (40 MP)
- **Page 8**: [Lightning Strike] - Single-target damage (50 MP)
- **Page 12**: [Healing Light] - Restore 3d8 HP (60 MP)

**Locked Pages**: Revealed during story moments (rage, despair, joy, triumph)
**Special Mechanic**: Grimoire damaged = power reduced 50%
```

### Example 3: Magitech Hybrid

**Player Request**: "Can I combine magic with technology?"

**AIDM Response**:
```markdown
**Power System: Magitech Engineering**

**Mana Circuits**: 5/10 installed (each circuit +50 MP max)
**Current MP**: 250/250
**Equipment**: Arcane Rifle (converts MP to energy blasts)

**Spell Programs**:
- [Program 1] **Arcane Shot**: 20 MP, 3d6 force damage, ranged
- [Program 2] **Energy Shield**: 30 MP, absorb 20 damage
- [Program 3] **Overclock**: 50 MP, +2 to all actions for 3 turns

**Unique Mechanic**: Can "compile" new spell programs by studying defeated enemies' magic
**Risk**: Circuit overload if exceed 100% MP capacity (take 2d6 damage)
```

---

## Balancing Guidelines for AIDM

### Power Budget

**Low-Level (1-5)**:
- MP Pool: 100-300
- Tier 1-2 spells only
- 2-4 spells known
- Single element/school

**Mid-Level (6-10)**:
- MP Pool: 300-600
- Tier 3 spells unlocked
- 6-10 spells known
- Secondary element available

**High-Level (11-15)**:
- MP Pool: 600-1000
- Tier 4 spells unlocked
- 12-20 spells known
- Multi-element combos

**Epic-Level (16-20)**:
- MP Pool: 1000-2000
- Tier 5 spells unlocked
- 20-30 spells known
- Reality-bending magic

**Godlike (21+)**:
- MP Pool: 2000+
- Tier 6+ (narrative magic)
- See `power_scaling_narrative.md` for guidance

### Combat Balance

**Action Economy**:
- Most spells = 1 action
- Tier 4+ may require 2 actions (charge turn)
- Cantrips can be bonus actions

**Damage Scaling**:
- Tier 1: 1d6-2d6 per 10-15 MP
- Tier 2: 3d6-5d6 per 20-40 MP
- Tier 3: 6d6-10d6 per 50-100 MP
- Tier 4+: Narrative effects, avoid pure damage spam

**Defensive Options**:
- Shield spells absorb ~2x MP cost in damage
- Counterspell = negate enemy spell (match their MP cost)

---

## Customization Hooks

These elements can be modified per campaign:

**MP Regeneration Rate**: Slow (gritty), medium (balanced), fast (high-magic)  
**Spell Schools Available**: All, restricted (no necromancy), custom schools  
**Casting Time**: Instant, chanted, ritual-required  
**Mana Scarcity**: Abundant (mana everywhere), scarce (ley line dependent)  
**Social Status**: Mages as elite, mages as outcasts, mages as common  
**Multiclassing**: Allowed (spellblade), restricted (pure mage only), encouraged (hybrid)

**AIDM Directive**: Confirm these settings during Session 0, record in world_state_schema.

---

## Error Prevention

### Common Pitfalls

**❌ Unlimited Mana**: Always enforce MP costs and regeneration limits  
**❌ Spell Spam**: Use cooldowns on powerful spells  
**❌ Undefined Power**: Clarify what each spell *cannot* do  
**❌ No Consequences**: Overuse = exhaustion, mana burn, corruption  
**❌ Ignoring Environment**: Fire weaker in rain, stronger in volcano

### Validation Checks

Before allowing spell usage:
1. **MP Cost**: Does player have enough MP?
2. **Requirements**: Catalyst available? Chant possible (not silenced)?
3. **Environment**: Any modifiers (ley line, mana-dead zone)?
4. **Cooldown**: Has cooldown expired?
5. **Restrictions**: Spell school available? Not forbidden?

---

## Cross-Reference

**Related Systems**:
- `ki_lifeforce_systems.md` - Internal energy (may hybrid with mana)
- `soul_spirit_systems.md` - Metaphysical powers (overlaps with necromancy)
- `psionic_psychic_systems.md` - Mental powers (distinguish from magic)
- `power_scaling_narrative.md` - High-level magic guidance

**Schema References**:
- `power_system_schema.json` - Structure for defining magic systems
- `character_schema.json` - MP pool, spells known, affinities
- `world_state_schema.json` - Ley lines, mana density, magic laws

**Instruction Modules**:
- `07_anime_integration.md` - How to research and integrate magic from anime
- `08_combat_resolution.md` - Spell usage in combat
- `09_progression_systems.md` - Learning new spells, MP growth

---

**This library covers ~30-35% of anime power systems. For internal energy (ki/chakra), see `ki_lifeforce_systems.md`. For metaphysical/death powers, see `soul_spirit_systems.md`. For mental powers, see `psionic_psychic_systems.md`.**

**AIDM: Use this as reference when player requests mana-based magic. Adapt specifics to fit campaign world. Confirm customization choices during Session 0.**
