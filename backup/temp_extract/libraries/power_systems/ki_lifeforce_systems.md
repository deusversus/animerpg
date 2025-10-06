# Ki & Lifeforce Systems (Internal Energy)

## Purpose

This library provides AIDM with generalized frameworks for **ki, chakra, and lifeforce-based systems** commonly found in anime. These systems are characterized by **internal energy cultivation** - developing and channeling power from within the practitioner's body, life essence, or spiritual core.

**Coverage**: ~30-35% of anime power systems (Dragon Ball, Naruto, Hunter x Hunter, Bleach, One Piece, Avatar, etc.)

**Use This Library When**:
- Player wants martial arts, body enhancement, or internal cultivation
- Power source is the user's life force, spiritual energy, or physical training
- System emphasizes physical conditioning, willpower, and mental discipline
- World features martial artists, monks, cultivators, or warriors

---

## Core Characteristics

### What Defines Internal Energy Systems

**Energy Source**: Within the practitioner
- Life force energy circulating through body
- Spiritual pressure/power emanating from soul
- Physical stamina converted to supernatural power
- Willpower and mental discipline made manifest

**Mechanics**:
- **Body-Dependent**: Stronger body = more ki/chakra capacity
- **Cultivation-Based**: Training increases power over time
- **Stamina-Linked**: Depletes with physical exertion
- **Aura/Presence**: Often visible as emanation around user
- **Enhancement-Focused**: Primarily boosts physical capabilities

**Narrative Role**:
- Training arcs (pushing limits, mastering techniques)
- Willpower moments (breaking limits through determination)
- Master-student relationships (inheritance of techniques)
- Power level escalation (sensing opponent's strength)

---

## Common Anime Examples

### Martial Arts Ki
**Dragon Ball**: Ki blasts, Super Saiyan transformations, instant transmission  
**Hunter x Hunter**: Nen (conditions, restrictions, specialist abilities)  
**Fist of the North Star**: Pressure points, internal destruction  
**Kenichi**: Traditional martial arts + ki enhancement

### Ninja Chakra
**Naruto**: Chakra natures, jutsu techniques, sage mode  
**Avatar (The Last Airbender)**: Bending as chi manipulation  
**Ninja Scroll**: Supernatural ninja techniques

### Spiritual Pressure
**Bleach**: Reiatsu/reiryoku, Zanpakuto manifestation, Kidō spells  
**Yu Yu Hakusho**: Spirit energy, spirit gun, transformations  
**Noragami**: Divine power, regalia manifestation

### Unique Lifeforce
**One Piece**: Haki (observation, armament, conqueror's)  
**Jojo's Bizarre Adventure**: Hamon (ripple energy)  
**Demon Slayer**: Breathing techniques, demon slayer marks

---

## System Framework Components

### 1. Ki/Chakra Pool & Stamina

**Resource Management**:
- **Ki Points (KP) / Chakra Points (CP)**: Numerical pool representing internal energy
- **Tied to Constitution/Stamina**: Physical condition affects capacity
- **Regeneration**: Recovers with rest, meditation, or natural healing
- **Depletion Consequences**: Exhaustion, unconsciousness, or death (if fully drained)

**AIDM Integration**:
```markdown
**Ki Pool**: Current KP / Max KP (e.g., 350/500)
**Regeneration**: +20 KP per short rest, full recovery after long rest
**Physical State**: Injured = reduced max KP (75% at half HP)
**Meditation**: 10-minute focus = +50 KP (once per hour)
```

**Example (Dragon Ball style)**:
- Ki Pool scales with Power Level
- Charging increases available ki (+10% per turn, max 300%)
- Overcharging risks injury (2d6 damage per turn beyond 200%)

---

### 2. Enhancement Techniques

**Physical Augmentation** (Most Common Use):

**A. Body Enhancement**
- **Strength**: +1d6 damage to physical attacks (20 KP/turn)
- **Speed**: +2 AC, double movement (30 KP/turn)
- **Durability**: +2 AC, damage reduction 3 (25 KP/turn)
- **Healing Factor**: Regenerate 1d8 HP/turn (40 KP/turn)

**B. Sensory Enhancement**
- **Ki Sensing**: Detect living beings within 100ft (10 KP)
- **Danger Sense**: +4 to initiative, can't be surprised (passive, 15 KP/encounter)
- **Aura Reading**: Determine power level, emotional state (15 KP)

**C. Movement Techniques**
- **Flash Step** (Bleach): Instant teleport 30ft (25 KP)
- **Sky Walking**: Move through air as solid ground (20 KP/turn)
- **Instant Transmission** (DBZ): Teleport to sensed ki signature (100 KP, long range)

**AIDM Integration**:
```markdown
**Active Enhancements**:
- [Body] +1d6 unarmed damage (20 KP/turn)
- [Durability] +2 AC, DR 3 (25 KP/turn)
**Total Cost**: 45 KP/turn (sustainable for 7 turns at current capacity)
```

---

### 3. Chakra Nature & Elemental Affinities

**Nature Transformation** (Naruto-style):

**Basic Natures** (Choose 1-2 at character creation):
- **Fire**: Offense, explosion, burning
- **Water**: Versatility, healing, adaptation
- **Earth**: Defense, fortification, endurance
- **Wind**: Cutting, precision, speed
- **Lightning**: Piercing, paralysis, speed

**Advanced Natures** (Combine 2 basic, rare):
- **Ice** (Water + Wind): Freeze, immobilize
- **Wood** (Earth + Water): Life, binding, constructs
- **Lava** (Fire + Earth): Molten destruction
- **Storm** (Water + Lightning): Weather control
- **Explosion** (Earth + Lightning): Demolition

**Unique Natures** (Bloodline/Rare):
- **Yin**: Illusions, mental manipulation
- **Yang**: Life force, physical manifestation
- **Yin-Yang**: Reality creation (extremely rare)

**AIDM Integration**:
```markdown
**Chakra Nature**: Lightning (Primary), Wind (Secondary)
**Available Jutsu**:
- [Lightning] Chidori: 80 CP, 6d8 piercing damage, paralysis chance
- [Wind] Gale Palm: 40 CP, 3d6 slashing, pushback 15ft
- [Storm - Combined] Thunderstorm: 120 CP, area attack, 5d10 lightning
```

---

### 4. Nen System (Conditions & Restrictions)

**Hunter x Hunter Framework** (Most Complex):

**Nen Categories** (Choose 1 specialization):
1. **Enhancer**: Amplify natural abilities (body enhancement master)
2. **Emitter**: Project ki externally (ranged ki blasts)
3. **Transmuter**: Change ki properties (electricity, rubber, etc.)
4. **Conjurer**: Materialize objects from ki (weapons, tools)
5. **Manipulator**: Control objects or beings (puppetry, mind control)
6. **Specialist**: Unique abilities (steal powers, prophecy, etc.)

**Efficiency Chart**:
- Specialization: 100% efficiency
- Adjacent categories: 80% efficiency
- Opposite category: 40% efficiency

**Conditions & Restrictions** (Power Multiplier):
- **Vow**: "I will only use this in life-or-death situations" = 3x power
- **Cost**: "Sacrifice 10% max HP to activate" = 2x power
- **Condition**: "Only works if enemy attacks first" = 2.5x power
- **Time Limit**: "Must defeat enemy in 3 minutes or I die" = 5x power

**AIDM Integration**:
```markdown
**Nen Type**: Conjurer (Specialization: 100%)
**Hatsu Ability**: "Chain Jail"
- **Effect**: Conjure binding chains, seal target's ki
- **Condition**: Only works on specific enemy type (e.g., villains)
- **Power Multiplier**: 3x (restrictive condition)
- **Cost**: 150 KP to activate, 20 KP/turn to maintain
- **Violation Penalty**: If used on non-villain, user loses all nen forever
```

---

### 5. Haki System (Willpower Manifestation)

**One Piece Framework** (Three Types):

**A. Observation Haki** (Kenbunshoku)
- **Basic**: Sense intent, predict attacks (+2 AC)
- **Advanced**: See seconds into future (30 KP/turn)
- **Mastery**: Extended range, emotional reading (passive)

**B. Armament Haki** (Busoshoku)
- **Basic**: Harden body parts (+3 AC, +1d6 damage, 25 KP/turn)
- **Advanced**: Internal destruction (bypass armor, 50 KP/attack)
- **Mastery**: Full-body coating, permanent hardening (passive)

**C. Conqueror's Haki** (Haoshoku) - **Rare, 1 in 1 million**
- **Basic**: Knock out weak-willed enemies (AOE, 100 KP)
- **Advanced**: Infuse attacks with conqueror's will (+2d10 damage, 80 KP)
- **Mastery**: Clash with other conquerors, split the sky (narrative power)

**AIDM Integration**:
```markdown
**Haki Abilities**:
- [Observation] Future Sight: +4 AC, can't be surprised (30 KP/turn)
- [Armament] Advanced: Bypass enemy armor, internal damage (50 KP/attack)
- [Conqueror] Infusion: +2d10 to attacks (80 KP, 3 uses/day)

**Haki Bloom**: Unlocks during life-threatening situations (narrative trigger)
```

---

### 6. Breathing Techniques (Demon Slayer)

**Breath Styles** (Technique-Based):

**Core Breaths** (Elemental):
- **Water Breathing**: Fluid, adaptive (10 forms)
- **Flame Breathing**: Aggressive, powerful (9 forms)
- **Thunder Breathing**: Speed, single-strike (6 forms)
- **Stone Breathing**: Endurance, defense (5 forms)
- **Wind Breathing**: Cutting, precision (9 forms)

**Derived Breaths**:
- **Mist** (from Water): Disorientation, illusions
- **Love** (from Flame): Whip-like, flexibility
- **Serpent** (from Water): Unpredictable, winding
- **Beast** (self-taught): Feral, instinct-based
- **Sound** (self-taught): Explosive, flashy

**Sun Breathing** (Original, Most Powerful):
- 13 forms, all other breaths derived from it
- Burns user's body if untrained (Mark of the Sun)
- Legendary, passed down through Kamado family

**AIDM Integration**:
```markdown
**Breath Style**: Water Breathing (Master: 10/10 forms)
**Active Form**: Second Form - Water Wheel
- **Cost**: 40 KP
- **Effect**: 5d6 slashing damage, 360° defense
- **Cooldown**: 2 turns

**Total Concentration Breathing**:
- **Constant**: +20% max KP, passive HP regen (requires training)
- **Active**: +50 KP burst, heightened senses (60 seconds)
```

---

## Integration Guidelines

### Harmonizing with Other Power Systems

**Ki + Mana (External Energy)**:
- **Compatible**: Warriors can learn basic magic for utility
- **Separate Pools**: KP and MP are distinct (or unified "Energy" pool)
- **Hybrid Builds**: Spellblade common (ki enhancement + weapon enchantments)
- **Example**: Goblin Slayer (martial skills + scrolls/potions)

**Ki + Soul/Spirit**:
- **High Overlap**: Reiatsu (Bleach) is both ki and spiritual pressure
- **Clarification**: Ki = life energy, Soul = metaphysical essence
- **Example**: Bleach (physical + spiritual), Yu Yu Hakusho (spirit energy)

**Ki + Psionic**:
- **Rare Overlap**: Nen (HxH) blurs line between willpower and psychic
- **Distinguish**: Ki = physical manifestation, Psionic = mental projection
- **Example**: Hunter x Hunter (Nen is ki system, but feels psychic)

**AIDM Rule**: If ki system has "aura" or "pressure," it overlaps with soul/spirit. Clarify during Session 0.

---

### Creating Original Ki Systems

**Template for Custom Systems**:

1. **Define Energy Source**: What is being cultivated?
   - Life force? Spiritual pressure? Willpower? Physical stamina?

2. **Resource Mechanics**: Pool, stamina, or cooldown-based?
   - Traditional KP bar, tied to HP, or unlimited with fatigue?

3. **Acquisition Method**: How do users develop ki?
   - Training? Enlightenment? Bloodline? Life-threatening situations?

4. **Power Scaling**: Linear growth or breakthrough-based?
   - Gradual increase or "realm" system (Foundation → Core → Nascent)?

5. **Unique Mechanic**: What makes it interesting?
   - Elemental natures? Conditions? Transformations? Awakening?

6. **Physical Cost**: What's the risk?
   - Exhaustion? Lifespan reduction? Body deterioration? Death?

**Example Custom System** (Player creates "Resonance Ki"):
- **Source**: Synchronizing heartbeat with universe's rhythm
- **Mechanics**: KP pool + "Resonance Level" (1-10, increases in combat)
- **Acquisition**: Meditation + combat experience (danger breeds growth)
- **Scaling**: Breakthrough realms at level 5, 10, 15, 20 (each = new techniques)
- **Unique**: Higher resonance = time perception slows (pseudo-bullet time)
- **Cost**: High resonance damages heart (HP cost per turn at Resonance 8+)

---

## Common Tropes & Story Hooks

### Character Archetypes
- **Hard Worker**: No talent, trains relentlessly (Rock Lee, Deku)
- **Prodigy**: Natural genius, learns instantly (Goku, Naruto's Sasuke)
- **Late Bloomer**: Weak initially, explosive potential (Asta, Tanjiro)
- **Master**: Already powerful, teaches others (Master Roshi, Jiraiya)
- **Forbidden User**: Dark ki, corrupted power (Ichigo's Hollow, Dark Side)

### Story Hooks
- **Training Arc**: Master teaches secret technique, montage time
- **Power Level Escalation**: Enemies keep getting stronger
- **Transformation**: Unlock new form (Super Saiyan, Bankai, Gear 5)
- **Breaking Limits**: Surpass physical limits through willpower
- **Forbidden Technique**: Powerful but costs lifespan/sanity
- **Ki Awakening**: Unlock dormant power in crisis

### Social Dynamics
- **Dojo/School Rivalry**: Competing martial arts schools
- **Power Level Hierarchy**: Respect based on strength
- **Master-Student Bonds**: Inheritance of techniques, legacy
- **Transformations as Status**: Super Saiyan = elite warrior

---

## AIDM Implementation Examples

### Example 1: Dragon Ball Ki System

**Player Request**: "I want to power up like a Saiyan"

**AIDM Response**:
```markdown
**Power System: Saiyan Ki**

**Ki Pool**: 400 KP (scales with Power Level)
**Power Level**: 5,000 (increases via training/combat)
**Regeneration**: Full recovery after 8-hour rest

**Techniques**:
- [Basic] **Ki Blast**: 30 KP, 3d8 force damage, ranged
- [Signature] **Kamehameha**: 80 KP, 8d10 force damage, beam attack
- [Enhancement] **Kaio-Ken**: 50 KP/turn, x2 stats (damage if prolonged)
- [Ultimate] **Super Saiyan**: 150 KP to activate, +50% all stats, burns 30 KP/turn

**Transformation Path**: Base → Kaio-Ken → Super Saiyan (unlocks at near-death)
**Zenkai Boost**: Recover from near-death = permanent +10% Power Level
```

### Example 2: Naruto Chakra System

**Player Request**: "I want to be a ninja with jutsu"

**AIDM Response**:
```markdown
**Power System: Shinobi Chakra**

**Chakra Pool**: 300 CP
**Chakra Nature**: Fire (Primary), Wind (Learning)
**Regeneration**: +15 CP/turn (passive), full after long rest

**Known Jutsu**:
- [E-Rank] **Clone Technique**: 10 CP, create illusionary clone
- [C-Rank] **Fireball Jutsu**: 40 CP, 4d6 fire damage, AOE
- [B-Rank] **Phoenix Flower**: 60 CP, multiple small fireballs (3d6 each)
- [A-Rank] **Great Fireball**: 100 CP, 10d8 fire damage, massive AOE

**Special**: Learning Wind nature enables **Scorch Release** (Fire + Wind hybrid)
**Growth**: Unlock new jutsu via scrolls, training, or copying (Sharingan)
```

### Example 3: Hunter x Hunter Nen

**Player Request**: "I want a unique ability with conditions like HxH"

**AIDM Response**:
```markdown
**Power System: Nen (Conjurer Type)**

**Nen Pool**: 250 NP (Nen Points)
**Type**: Conjurer (100% efficiency), Emitter (60% efficiency)
**Regeneration**: +20 NP/turn, full after meditation

**Hatsu: "Shadow Armory"**
- **Ability**: Conjure weapons from killed enemies' shadows
- **Condition**: Must defeat enemy in 1v1 combat to "claim" weapon
- **Power Multiplier**: 2.5x (restrictive condition)
- **Cost**: 100 NP to summon weapon, 20 NP/turn to maintain
- **Arsenal**: Currently contains 3 weapons (longsword, spear, daggers)

**Consequence**: If weapon is broken, it's lost forever from armory
**Growth**: Defeat stronger enemies = access to legendary weapons
```

### Example 4: One Piece Haki

**Player Request**: "I want Haki like Luffy"

**AIDM Response**:
```markdown
**Power System: Haki (Three Colors)**

**Haki Pool**: 300 HP (Haki Points, separate from HP)
**Regeneration**: +25 HP/turn, full after long rest

**Observation Haki** (Basic):
- **Effect**: +2 AC, sense emotions within 50ft
- **Cost**: 15 HP/turn
- **Unlock**: Future Sight (see 3 seconds ahead) at level 10

**Armament Haki** (Advanced):
- **Effect**: +3 AC, +1d8 damage, can hit intangible enemies
- **Cost**: 25 HP/turn
- **Advanced**: Internal Destruction (ignore armor) = 50 HP/attack

**Conqueror's Haki** (Dormant):
- **Status**: Unlocks during desperate battle (DM trigger)
- **Effect**: Knock out weak enemies, +2d10 damage when infused
- **Note**: Rare, only 1 in a million have this

**Haki Bloom**: During life-or-death moments, Haki power surges (narrative)
```

---

## Balancing Guidelines for AIDM

### Power Budget

**Low-Level (1-5)**:
- KP Pool: 100-300
- Basic enhancements only (strength, speed, durability)
- 2-4 techniques known
- Single element/style

**Mid-Level (6-10)**:
- KP Pool: 300-600
- Advanced techniques (flash step, energy blasts)
- 6-10 techniques known
- Secondary element/style available

**High-Level (11-15)**:
- KP Pool: 600-1000
- Transformations unlocked (Super Saiyan, Bankai)
- 12-20 techniques known
- Mastery of primary style

**Epic-Level (16-20)**:
- KP Pool: 1000-2000
- Ultimate techniques (Kamehameha x10, True Bankai)
- 20-30 techniques known
- Multi-style mastery

**Godlike (21+)**:
- KP Pool: 2000+
- Reality-bending techniques (Ultra Instinct, Soul King)
- See `power_scaling_narrative.md` for guidance

### Combat Balance

**Enhancement Costs** (Per Turn):
- +1d6 damage: 20 KP
- +2 AC: 25 KP
- +10ft movement: 15 KP
- Damage reduction 3: 30 KP

**Technique Damage**:
- Tier 1 (Basic): 2d6-3d8 for 30-50 KP
- Tier 2 (Advanced): 4d8-6d10 for 60-100 KP
- Tier 3 (Ultimate): 8d10-12d12 for 120-200 KP
- Tier 4+ (Legendary): Narrative effects, not pure damage

**Transformation Costs**:
- Activation: 100-200 KP (one-time)
- Maintenance: 30-50 KP/turn
- Risk: HP damage if maintained too long (2d6/turn after time limit)

---

## Customization Hooks

These elements can be modified per campaign:

**KP Regeneration**: Slow (gritty), medium (balanced), fast (shonen)  
**Element/Nature Availability**: All, restricted (fire-only world), custom  
**Transformation Difficulty**: Easy (everyone), medium (training), rare (1%)  
**Power Level Visible**: Yes (scouters), no (hidden strength)  
**Training Time**: Fast (montage), realistic (months/years), instant (crisis unlock)  
**Physical Cost**: High (lifespan), medium (exhaustion), low (minor fatigue)

**AIDM Directive**: Confirm these settings during Session 0, record in world_state_schema.

---

## Error Prevention

### Common Pitfalls

**❌ Infinite KP**: Always enforce costs and regeneration limits  
**❌ Stat Stacking**: Cap enhancement bonuses (+6 AC max, +3d6 damage max)  
**❌ Undefined Power Levels**: Clarify what "Power Level 10,000" means mechanically  
**❌ No Exhaustion**: Overuse = fatigue, unconsciousness, or death  
**❌ Ignoring Conditions**: If Nen has restriction, ENFORCE it or consequences apply

### Validation Checks

Before allowing ki technique usage:
1. **KP Cost**: Does player have enough KP?
2. **Physical State**: Injured/exhausted = reduced capacity?
3. **Conditions Met**: Nen restrictions satisfied?
4. **Cooldown**: Has technique cooldown expired?
5. **Transformation Active**: Is maintenance cost being paid?

---

## Cross-Reference

**Related Systems**:
- `mana_magic_systems.md` - External energy (may hybrid with ki)
- `soul_spirit_systems.md` - Spiritual pressure (overlaps with Bleach reiatsu)
- `psionic_psychic_systems.md` - Mental powers (Nen blurs the line)
- `power_scaling_narrative.md` - High-level ki mastery guidance

**Schema References**:
- `power_system_schema.json` - Structure for defining ki systems
- `character_schema.json` - KP pool, techniques known, transformations
- `world_state_schema.json` - Ki density, training grounds, power level culture

**Instruction Modules**:
- `07_anime_integration.md` - How to research and integrate ki from anime
- `08_combat_resolution.md` - Ki technique usage in combat
- `09_progression_systems.md` - Learning new techniques, KP growth

---

**This library covers ~30-35% of anime power systems. For external energy (mana/magic), see `mana_magic_systems.md`. For metaphysical/death powers, see `soul_spirit_systems.md`. For mental powers, see `psionic_psychic_systems.md`.**

**AIDM: Use this as reference when player requests ki/chakra/haki-based powers. Adapt specifics to fit campaign world. Confirm customization choices during Session 0.**
