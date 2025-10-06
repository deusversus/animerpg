# Skill Taxonomies

Skill systems (active/passive/ultimate abilities) for anime power frameworks. **Coverage**: Categories, mastery, trees, combos, SP, cooldowns. **Use**: Session Zero abilities, skill progression, balancing actives/passives, combo design.

**Skills = Character Identity + Tactical Variety + Progression**: Named techniques (RASENGAN!), signature moves, strategic choices. Make skills **flavorful**, **distinct**, **interesting**.

---

## Categories

**Active** (cost resources): **Attack** (Single: Power Strike 2×dmg+STR 15SP; AoE: Fireball 3d6 20MP; DoT: Poison 1d4/turn 10SP) · **Utility** (Move: Dash 2×speed 10SP, Teleport 20MP; Stealth: Invisibility 3turns 25MP; Info: Appraisal 10MP) · **Buff/Debuff** (Buff: Bless +2 rolls 15MP, Haste +5DEX 20MP; Debuff: Curse -2 rolls 15MP, Slow -5DEX 20MP) · **Healing** (Cure 2d8+WIS 15MP; Cleanse status 10MP; Barrier 20tempHP 15MP)

---

**Passive** (always-on): **Stats** (+2 STR/INT/WIS; +10% melee/spell dmg; +10% dodge) · **Resist** (50% elem dmg; poison/mind immunity) · **Efficiency** (-10% MP/SP cost; +5HP/turn regen) · **Enhance** (Improved [Skill] +dmg/radius; Crit 19-20 not 20; 3×crit not 2×)

---

**Ultimate** (signature, limited): High cost (50+MP/SP, long CD, once/combat), high impact, iconic. **Examples**: Rasengan (5d10 1turn charge 40MP), Kamehameha (6d12 line 2turn charge 50SP), Domain Expansion (trap 30ft guarantee-hit 80MP once/combat), Gear Fourth (+10STR/DEX/+50HP 5turn, drawback -5stats after, once/day). **Types**: Offensive (Meteor 8d10 AoE 60MP, Limit all-crits 50SP), Defensive (Perfect Guard 2turn 40SP, Mass Heal full 80MP), Utility (Time Stop 1turn 70MP, Summon ally 60MP).

---

## Acquisition

**1. Level-Up** (class-based, predictable): Fire Mage L1 Flame Bolt → L3 Fire Resist → L5 Fireball → L10 Fire Shield → L15 Meteor. *Pro: Balanced. Con: No choice.*

**2. Skill Points** (flexible): +1SP/level, +1SP/5levels, +1SP quest. Costs: T1 Basic 1SP, T2 Improved 2SP, T3 Advanced 3SP, T4 Expert 5SP, T5 Ultimate 10SP (prereqs required). *Pro: Customization. Con: Balance complexity.*

**3. Training/Discovery** (earned): **Mentor** (train 3 sessions → trial → unlock) · **Scrolls** (loot → study INT check → learn) · **Mimicry** (witness → DEX check → copy at half-power, master via use). *Pro: Narrative. Con: GM-dependent.*

**4. Skill Trees** (branching): Core → Branch A/B/C specialization. Ex: Weapon Mastery → Power (Strike/Cleave/Limit) | Speed (Rapid/Flash/Thousand Cuts) | Defense (Parry/Counter/Perfect). *Pro: Deep builds. Con: Design complexity.*

---

## Mastery (improve via use)

**Ranks**: Novice 0-10 (base) → Apprentice 11-25 (+10%dmg -5%cost) → Adept 26-50 (+20%dmg -10%cost -1CD) → Expert 51-100 (+30%dmg -15%cost -2CD +effect) → Master 101+ (+50%dmg -20%cost -3CD major-effects). **Track**: Fireball Apprentice 18/25 (3d6→3.3d6, 20→19MP, 7 to Adept). *Pro: Rewards favorites. Con: Bookkeeping.*

---

## Resources

**MP/SP** (classic pools): MP=INT×10, SP=(STR+DEX+CON)×3. Regen: Short rest +25%, Long rest +100%, Potions +50. *Strategy: Spam weak OR save big?*

**Cooldowns** (free, wait periods): Short 1-2turn, Medium 3-5turn, Long 10+turn, Once/combat, Once/day. Track: T1 Fireball used [3CD] → T2 [2] → T3 [1] → T4 available. *Pro: Simple. Con: Less resource depth.*

**Conditions** (triggers): HP-based (Desperate Strike <25%HP 5×dmg) · Combo (Thunder Clap after 2×Lightning) · Charge (Super Move 1/turn, costs 5 charges). *Track: HP 45/200 22% → Desperate AVAILABLE*

---

## Combos/Synergies

**Sequential**: Fire+Wind=Inferno (Fireball 3d6 + Wind 2d6 = 10d6 combined vs 5d6 separate) · Ice+Lightning=Frozen Shock (normal dmg + 50% paralyze) · Stun→Execute (Shield Bash stun → Execute insta-kill <30%HP). *Encourages teamwork.*

**Stacking**: Fire Mastery +10% × Elemental +15% × Spell Power +10% = +38.5% fire spell dmg (multiplicative). Sword +2ATK + Specialization +3ATK + Duelist +2ATK = +7ATK (additive). *Optimize builds via synergies.*

---

## Genre Systems

**Isekai** (game-like status screens): 8/12 active slots (Appraisal L5, Fireball L3, Heal L2, Dash L4), 5 passives (Fire Resist, Fast Learner +20%XP, Lucky Drop, Mana Efficiency, HP Regen), Unique cheat skill (Predator absorb skills). *Display on request, announce unlocks.*

**Shonen** (named techniques): Basic (Rasengan 5d10, Shadow Clone, Substitution) → Advanced (Rasenshuriken 8d12, Sage Mode 2×stats) → Ultimate (Tailed Beast 10×power, exhaustion). *Unlock: mentor/scroll → master+training → emotional breakthrough. Narrate dramatically.*

**Seinen** (realistic, limited): 4 skills only (Silent Step passive, Vital Strike 3×unaware once/combat, Poison 1d6/turn, Escape bonds once/day). *Mastery > quantity. Situational power.*

**Slice-of-Life** (social/mundane): Cooking L7/10, Music Piano L5/10, Tutoring L6/10, Fashion L4/10, Empathy L8/10. *Practice increases level. No combat. Relationship building.*

---

## Implementation

**Creation**: 1) Category (active/passive/ultimate) 2) Effect (dmg/heal/buff) 3) Cost (MP/SP/CD) 4) Flavor (name/visual) 5) Balance (vs similar) 6) Grant (level/training/loot).

**Combat**: Player declares → Check resource → Deduct cost → Resolve effect (roll dmg) → Narrate dramatically → Apply CD. Ex: "Fireball!" → 45MP-20=25MP → 3d6=12dmg → "Blazing sphere engulfs goblins!" → [3CD].

**Balance**: Dmg (Single 2-3×wpn; AoE 1.5×wpn; DoT 1×wpn/turn 3-5turn) · Cost (Weak 10-15, Medium 20-30, Strong 40-60, Ultimate 80-100) · CD (Spam none, Regular 2-3, Strong 5-10, Ultimate once/combat/day).

---

## Cross-Refs

**Libraries**: stat_frameworks.md (INT/STR governs skill power), leveling_curves.md (skills via levels), power_tier_reference.md (tier mapping), power systems (skill frameworks). **Schemas**: character_schema (skill storage/mastery), session_state_schema (CD tracking/use counts), power_system_schema (skill integration). **Modules**: 08_combat (skill resolution), 09_progression (acquisition/advancement), 06_session_zero (starting skills), 12_player_agency (power level handling).

---

**AIDM**: Create **diverse**, **flavorful** skill systems. Skills = character identity (signature moves), tactical variety (specific abilities vs "attack"), progression depth (learn techniques). Balance power with flavor. Skills turn "I attack" into "RASENGAN!" — make them **cool**, **meaningful choices** (which skill for this situation?), **strategic** (combos, resource management), **satisfying** (mastery, ultimates). Not spreadsheet entries.
