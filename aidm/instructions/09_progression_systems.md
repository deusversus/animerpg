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

## Integration

With: State Manager (03) - atomic updates, Combat (08) - XP awards, Narrative (05) - roleplay/quest/discovery XP, Learning (02) - PROGRESSION memories for milestones

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
