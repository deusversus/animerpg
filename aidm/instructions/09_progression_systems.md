# Module 09: Progression Systems - Leveling & Advancement

**Version**: 2.0 | **Priority**: HIGH | **Load**: After Combat Resolution

**Purpose**: Character growth through experience. Fair XP awards (matches challenge), meaningful leveling (rewarding), skill advancement (use+training), build diversity (multiple paths), progression pacing (balanced). **Core Principle**: GROWTH IS EARNED, NOT GIVEN. Every level tells a story.

## Progression Workflow

**Process**: Complete Challenge (combat/quest/discovery/roleplay)→Award XP (difficulty-based)→Check Level-Up (threshold?)→Level-Up Sequence (if reached)→Distribute Rewards (attributes/skills/abilities)→Update State (atomic)→Narrative Moment (celebrate)

## XP Award System

**COMBAT**: XP = Base XP × Challenge Mod. Base: L1=50, L2=100, L3=200, L4=350, L5=550, L6+=(Level×100). Modifier: Trivial (3+ below)×0.1, Easy (1-2 below)×0.5, Fair (same)×1.0, Hard (1-2 above)×1.5, Deadly (3+ above)×2.0, Boss×3.0. Example: L5 defeats L4 goblin: 350×0.5=175 XP

**QUESTS**: XP = Difficulty × Quality. Difficulty: Minor 100, Standard 300, Major 750, Epic 2000. Quality: Partial×0.5, Complete×1.0, Exceptional×1.5. Example: Minor quest exceptional: 100×1.5=150 XP

**ROLEPLAY/DISCOVERY**: Roleplay 25-100, Discovery 150, Puzzle 50-200, Negotiation 100, Creative 75-150

**MILESTONES**: First skill use 50, Relationship tier 100, Faction milestone 150, Story beat 200-500

---

## Level-Up System

**XP Requirements**: L1→2: 1K, L2→3: 2K, L3→4: 3.5K, L4→5: 5.5K, L5→6: 8K, L6→7: 11K, L7→8: 15K, L8→9: 20K, L9→10: 26K, L10+: (Level×3000). Rationale: Early fast, mid slower, late commitment.

**Rewards (Every Level)**: +10 HP, +10 MP, +5 SP, +2 Attribute Points, +1 Skill Point

**Milestone (L5/10/15/20)**: Standard rewards + 1 BONUS Skill Point (2 total), unlock new ability tier, narrative moment

**Level-Up Example** (Aria L5→L6, defeats boss +1500 XP, 7850→9350 over threshold): "Power surges... LEVEL UP! L5→L6. HP 145→155, MP 220→230, SP 130→135. +2 Attribute pts, +1 Skill pt. How grow?" Player chooses WIS+1, CON+1 →"WIS 16→17, CON 14→15 (HP 155→160)." Then skill: Life Transfer L2→L3 →"NEW MASTERY: Cost 0.75:1 (was 1:1), Range 2m (was touch). [Complete! L6, HP 160/160, MP 230/230, SP 135/135, XP 1350/11K]"

## Skill Advancement

**ACTIVE**: Spend 1 skill point per level (immediate, player-controlled)

**PASSIVE**: Use-based XP. Per use: Trivial +5, Standard +15, Challenging +30, Critical +50. XP to next: L1→2: 200, L2→3: 400, L3→4: 700, L4→5: 1100, L5+: (Level×250). Example: Stealth L2 (150/400)→challenging use +30→180/400... [Many sessions]→420/400 →"SKILL MASTERY! Stealth L3. NEW: Shadow Blend (+5 in dark), Silent Movement (no penalty fast)"

**Mastery Bonuses** (L3/5/7/10): Life Transfer: L1 basic (1:1, touch), L3 efficient (0.75:1, 2m), L5 advanced (0.5:1, 5m, cure poison), L7 expert (0.25:1, 10m, status), L10 ULTIMATE (Resurrection 1min). Stealth: L1 basic, L3 shadow blend (+5 dark, silent), L5 expert (hide plain sight, +10 dark), L7 master (invisibility 1 turn, 1/day), L10 ULTIMATE (Shadowstep 10m to shadow, 3/day)

## Build Diversity

**Example Builds**: Combat Healer (WIS/CON, Life Transfer/First Aid), Glass Cannon (INT/WIS, Elemental Magic), Tank (STR/CON, Shield/Taunt), Rogue (DEX/CHA, Stealth/Lockpick), Hybrid (balanced all)

---

## Progression Pacing

**Session XP** (2hr): Low (roleplay) 300-500, Standard (mix) 600-900, High (multi-combat/quest) 1K-1.5K, Epic (boss/climax) 2K+

**Level Estimate**: L1-3: 2-3 sessions/level (fast), L4-6: 4-5 sessions (moderate), L7-9: 6-8 sessions (slow), L10+: 10+ sessions (legendary)

## Achievements & Milestones

**Categories**: COMBAT (First Blood +50, Boss Slayer +200, Untouchable +150, Combo Master +100), SOCIAL (Trusted +100, Devoted +250, Silver Tongue +150), EXPLORATION (Discoverer +100, Treasure Hunter +200, Lorekeeper +150), PROGRESSION (Adept L5 +250, Expert L10 +500, Master Skill +300), NARRATIVE (Hero's Sacrifice +200, Villain's Bane +500, World Changer +1K)

**Announcement**: "Peace negotiated. ACHIEVEMENT: Silver Tongue +150 XP. Reputation as peacemaker grows."

## Multi-Classing (L10+)

At L10, choose secondary class (Warrior/Mage/Rogue/Paladin/Monk). Starts L1, levels alongside primary. Benefits: new skill trees, hybrid abilities, uniqueness. Example: Aria L10 Healer→chooses Paladin→"[Secondary: Paladin L1] New skills: Holy Strike/Divine Shield/Righteous Fury. HYBRID: Healing Strike (attack heals 50% dmg dealt)"

## Stat Caps

Soft Cap 20 (mortal max), Hard Cap 25 (requires legendary). Diminishing Returns after 18: 18→19 costs 2 pts, 19→20 costs 3 pts, 20→21+ costs 4 pts + special quest/item

## Downtime Training System

**Purpose**: Allow characters to advance skills during downtime (travel, rest, off-screen periods) without relying solely on active use.

### Training Basics

**Training Session**: 1 week (in-game time) of dedicated practice
- **Requirements**: Downtime period (no active quests/combat/travel), trainer (NPC expert or self-study), cost (gold for trainer or resources)
- **Outcome**: Skill XP based on training quality

**Training Quality**:
- **Self-Study** (no trainer): +50 skill XP/week (slow but free)
- **Competent Trainer** (skill level ≥ target skill + 2): +100 skill XP/week (50 gold/week)
- **Expert Trainer** (skill level ≥ target skill + 5): +200 skill XP/week (200 gold/week)
- **Master Trainer** (skill level 10): +300 skill XP/week (500 gold/week + quest hook)

**Skill Point Conversion** (alternative to XP grinding):
- Spend **1 skill point** = Instant skill level-up (no XP required)
- Spend **downtime training** = Accumulate skill XP (slower but free/cheap)

**Training Limits**:
- **Cannot train skills above trainer's level** (need better trainer to advance further)
- **Maximum 4 weeks training per skill** before diminishing returns (-50% XP after week 4)
- **Cannot train during active adventures** (downtime only)

### Training Montage Mechanics

**Narrative Shortcut** for training arcs (anime-style):

**Setup**: Player declares training goal + duration
- "I spend 3 weeks training Swordsmanship with the retired master."
- "During the month-long voyage, I practice Elemental Magic every day."

**Resolution**:
1. **Calculate Total XP**: Training quality × weeks (e.g., 100 XP/week × 3 weeks = 300 XP)
2. **Apply to Skill**: Add XP to skill, check for level-up
3. **Narrate Montage**: Describe training progression (struggles → breakthroughs → mastery)
4. **Cost**: Deduct gold (trainer fees) or resources (materials consumed)

**Example Montage** (Swordsmanship L2→L3, needs 400 XP, has 150/400):
- **Declare**: "I train with Master Takeshi for 3 weeks." (Expert trainer: 200 XP/week, 200 gold/week)
- **Calculate**: 200 XP × 3 weeks = 600 XP, 200 gold × 3 weeks = 600 gold
- **Apply**: 150 + 600 = 750 XP → Level up! (used 250 XP for L2→L3, 500 XP remaining)
- **Continue?**: "500 XP toward L3→L4 (need 700). Train 2 more weeks?" OR "Stop here, save gold."
- **Narrate**: "Day 1: Takeshi DISARMS you instantly. 'Grip too loose!' Week 1: Blocking improves. Week 2: First clean strike. Takeshi GRINS. Week 3: Sparring match—you HOLD YOUR OWN. [Swordsmanship L3! NEW: Riposte (counterattack on parry)]"

**Montage Narrative Beats** (use 2-3):
1. **Initial Struggle**: "You can barely keep up. Every muscle SCREAMS."
2. **Repetition**: "Days blur into nights. Same drills, over and over."
3. **Breakthrough Moment**: "Something CLICKS. Your form feels... natural."
4. **Final Test**: "Takeshi attacks full force. You PARRY—perfect form. He nods."
5. **Mastery Moment**: "The blade feels like an extension of your arm now."

### Training Costs by Skill Type

**Physical Skills** (Swordsmanship, Athletics, Stealth):
- **Cost**: 50-200 gold/week (trainer fees, equipment wear)
- **Time**: 1-4 weeks per level (physical muscle memory)

**Magic Skills** (Elemental Magic, Necromancy, Enchanting):
- **Cost**: 100-500 gold/week (reagents, spell components, arcane texts)
- **Time**: 2-6 weeks per level (complex theory + practice)

**Social Skills** (Persuasion, Deception, Performance):
- **Cost**: 25-100 gold/week (etiquette lessons, practice venues)
- **Time**: 1-3 weeks per level (practical application)

**Knowledge Skills** (History, Medicine, Arcana):
- **Cost**: 50-300 gold/week (books, tutors, research materials)
- **Time**: 2-8 weeks per level (dense study material)

### Anime-Style Training Arcs

**Common Tropes** (integrate narratively):

**Hell Week** (Naruto):
- 1 week of extreme training = 2 weeks normal training XP (×2 multiplier)
- **Consequence**: Exhaustion debuff for 3 days after (-2 to physical rolls)
- **Narration**: "You push beyond limits. Collapse. Wake. Push again. Every fiber burns..."

**Death Training** (Dragon Ball):
- Train in extreme environment (gravity chamber, deadly terrain, against superior opponent)
- 1 week extreme = 3 weeks normal XP (×3 multiplier)
- **Consequence**: Injury risk (roll CON save DC 15 or gain Minor Wound), exhaustion for 1 week
- **Narration**: "100× gravity CRUSHES you. Every step is agony. But you REFUSE to quit..."

**Timeskip Montage** (Generic):
- Compress months/years of training into narrative moment
- Award multiple skill levels at once (1 level per month of downtime)
- **Use When**: Story requires time passage (e.g., "3 years later...")
- **Narration**: "MONTAGE: Seasons change. You grow stronger. Years of sweat, blood, failure... then mastery."

**Hidden Master** (Kung Fu Panda):
- Train with legendary NPC (skill level 10, unique teaching method)
- 1 week = 500 skill XP (×5 normal)
- **Cost**: Complete quest for master (no gold, but difficult trial)
- **Narration**: "The master's methods seem insane. Carry water. Chop wood. Meditate. But slowly... you understand."

### Integration with Progression System

**Skill Point vs Training**:
- **Skill Point**: Instant level-up (reward for character level, no time/gold cost)
- **Training**: Gradual XP gain (time + gold cost, but unlimited if you have resources)

**Combined Approach** (recommended):
- Use skill points for **immediate power-ups** (combat skills needed NOW)
- Use training for **long-term development** (non-urgent skills, downtime periods)

**Example** (Aria L6, has 2 skill points, wants to improve Healing + Persuasion):
- **Immediate Need**: Spends 1 skill point → Life Transfer L2→L3 (needed for next dungeon)
- **Downtime**: Trains Persuasion during 2-week travel (self-study: 50 XP/week × 2 = 100 XP)
- **Future Plan**: Saves 1 skill point for emergency, continues Persuasion training when safe

## Integration

With: State Manager (03) - atomic updates + **automated quest XP via quest_completion cascade**, Combat (08) - XP awards, Narrative (05) - roleplay/quest/discovery XP, Learning (02) - PROGRESSION memories for milestones

**Cascade System**:
- **Quest Completion XP** (Module 03 cascade): When quest status→"completed", automatically reads quest.rewards.xp, adds to character.progression.current_xp, checks level-up threshold, triggers level-up if met, logs XP gain. **No manual tracking required.**

## Module Completion Criteria

Successful when: Fair XP (matches difficulty), rewarding level-ups, skill advancement reflects usage, multiple builds viable, balanced pacing, achievements recognized, milestones memorable.

## Common Mistakes

**[NO] Arbitrary XP**: "Defeated goblin. +1M XP" [L1→L50 instantly] →No achievement, broken

**[OK] Scaled**: "Defeated goblin. +50 XP" [gradual progress] →Meaningful, earned

**[NO] Auto Level-Up**: "Leveled! I auto-increased stats" →No agency

**[OK] Player-Driven**: "Leveled! 2 attribute pts, 1 skill pt. How grow?" →Player shapes character

### Faction Reputation Milestones

**Purpose**: To reward players for achieving significant reputation tiers with factions, providing a tangible sense of progression and unlocking new narrative and mechanical opportunities.

**XP Awards for Reaching Tiers**:
- **Liked**: +200 XP. The character is now a recognized friend of the faction.
- **Honored**: +500 XP. The character has become a trusted and respected champion of the faction's interests.
- **Hated**: +100 XP. While negative, achieving a strong reputation (even a bad one) is a significant narrative milestone.
- **Devoted/Exalted (if applicable)**: +1000 XP. For reaching the pinnacle of a faction's relationship track.

**Rank-Up XP Awards**:
- Achieving a new rank within a faction (as defined in `faction_schema.json`) also provides an XP reward.
- **Low-tier Rank (e.g., 'Initiate', 'Member')**: +150 XP.
- **Mid-tier Rank (e.g., 'Veteran', 'Captain')**: +300 XP.
- **High-tier Rank (e.g., 'Champion', 'Inner Circle')**: +600 XP.

**Implementation**:
- The State Manager (Module 03) will monitor changes to a character's faction reputation.
- When a `modify_reputation` call results in crossing a tier or rank threshold, the State Manager will trigger a call to the Progression System (Module 09).
- Module 09 will then award the appropriate XP and create a "PROGRESSION" memory thread to log the achievement.

**Example**:
Aria completes a major quest for the Crimson Vanguard. Her reputation increases from 650 to 800.
1. **State Manager**: Detects reputation change.
2. **State Manager**: Calls `get_reputation_tier` before and after. Result: "Liked" -> "Honored".
3. **State Manager**: Calls `get_character_rank` before and after. Result: "Vanguard" -> "Vanguard Captain".
4. **State Manager**: Triggers two events for Module 09: `reputation_tier_reached` and `rank_achieved`.
5. **Module 09**:
    - Awards +500 XP for reaching "Honored".
    - Awards +300 XP for achieving the rank of "Vanguard Captain".
    - Total XP awarded: 800.
6. **Narrative System (Module 05)**: Generates a narrative moment: "Your deeds for the Crimson Vanguard have not gone unnoticed. You are now considered an Honored member and have been granted the rank of Captain. [ACHIEVEMENT UNLOCKED: Vanguard Captain. +800 XP]"
