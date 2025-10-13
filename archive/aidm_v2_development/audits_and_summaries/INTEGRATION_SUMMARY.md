# AIDM Integration Summary - Quick Reference

**Date**: 2025-10-11  
**Status**: ANALYSIS COMPLETE - Awaiting User Decisions  
**Full Analysis**: See `INTEGRATION_ANALYSIS.md`

---

## TL;DR - The Problem

**Narrative Calibration (Module 13 + CORE Profiles) is EXCELLENT at storytelling** but **disconnected from mechanical systems**:

❌ **Profiles don't explain HP/MP tracking** (DanDaDan: How much MP does Momo's psychic slam cost?)  
❌ **Profiles don't link to power_systems** (Hunter x Hunter: Which library defines Nen mechanics?)  
❌ **Profiles don't reference stat_frameworks** (Attack on Titan: Use 6-stat or 3-stat? Linear or exponential leveling?)  
✅ **Genre tropes ARE comprehensive** but not cross-linked with profiles

**Result**: AIDM might narrate beautifully (DanDaDan chaos, Vinland brutality) but **improvise mechanics instead of referencing libraries**.

---

## The Fix - Three Sections Per Profile

Add ~1,900 words to each of 12 CORE profiles:

### 1. Mechanical Implementation (~500 words)
**What**: HP/MP/SP formulas for iconic characters, resource costs for signature abilities, depletion narration examples

**Example (DanDaDan)**:
```
Momo: Psychic Power Pool = (INT 16 + WIS 12) × 10 = 280 MP
Costs: Psychic Slam 30 MP, Barrier 20 MP sustained, Levitation 10 MP/turn
Depletion Narrative: Below 50% MP → "Momo's grip WEAKENS—alien breaks free!"
```

### 2. Power System Integration (~800 words)
**What**: Which power_systems libraries apply, specific costs/scaling, limitations, tier progression

**Example (Hunter x Hunter)**:
```
Primary System: Nen (custom system, reference ki_lifeforce for base structure)
Gon's Jajanken: Rock (Enhancement) = 80 Nen, Paper (Emission) = 50 Nen, Scissors (Transmutation) = 60 Nen
Nen Pool: (INT + WIS + CON) × 15 = ~450 Nen at Lv10
Conditions: Verbal declaration required (+20% power), charge time (Rock 5 sec charge)
```

### 3. Character Creation Guidelines (~600 words)
**What**: Recommended stat framework (6-stat/3-stat/anime-specific), leveling curve, skill priorities

**Example (Attack on Titan)**:
```
Stat Framework: 6-Stat Classic (STR/DEX/CON/INT/WIS/CHA)
Leveling: Linear Slow (realistic military progression, +1 stat every 4 levels)
Build Priorities: Survey Corps = DEX 16+ (ODM gear), CON 14+ (survive), INT 12+ (tactics)
```

---

## Effort Estimate

- **Phase 1** (Audit): 1-2 hours ✅ DONE (genre tropes comprehensive, power_systems exist, stat_frameworks ready)
- **Phase 2** (Expand Profiles): 8-12 hours (1,900 words × 12 profiles = ~23K words)
- **Phase 3** (Cross-Reference): 2-4 hours (update libraries with profile examples)
- **Phase 4** (Integration Guide): 1-2 hours (create NARRATIVE_MECHANICS_INTEGRATION.md)

**Total**: 12-20 hours (~2-3 full work sessions)

---

## User Decisions Needed

### 1. Genre Tropes Priority
**Status**: Tropes ARE comprehensive (shonen/isekai verified complete)  
**Question**: Just add cross-links or full bidirectional integration?

**Option A** (Quick): Add 200-word "Genre Trope Integration" to each profile's Usage Notes  
**Option B** (Thorough): Add profile examples to each trope file + profile cross-references (bidirectional)

**Recommendation**: Option B (thorough) - ~2 hours extra for permanent value

---

### 2. Mechanical Detail Level

**Minimal** (~300 words): Just HP/MP formulas + 2-3 power cost examples  
**Standard** (~500 words, RECOMMENDED): Formulas + costs + depletion narration + recovery  
**Comprehensive** (~800 words): All above + edge cases + multi-character examples

**Recommendation**: Standard (500 words) - balances depth with token cost

---

### 3. Power System Libraries

**Question**: Verify existing power_systems files before linking, or expand as we discover gaps?

**Option A** (Verify First): Read mana_magic, ki_lifeforce, psionic_psychic to confirm depth (2 hours)  
**Option B** (Expand As Needed): Link profiles now, expand libraries when gaps found (iterative)

**Recommendation**: Option A - verify foundation before building on it

---

### 4. Timeline

**Option A** (Sequential): Complete mechanical integration for all 12 profiles → Phase 2 new profiles  
**Option B** (Interleaved): Expand 2-3 profiles mechanically → Add 1 new skeletal profile → Repeat

**Recommendation**: Option A (sequential) - establish pattern with existing profiles before scaling

---

## Immediate Next Steps (If User Approves)

1. **Prototype 1 Profile** (DanDaDan or Hunter x Hunter): Add all 3 sections, validate approach (2-3 hours)
2. **User Review**: Check prototype quality, adjust section lengths/depth
3. **Expand to Remaining 11 Profiles**: Apply pattern (8-10 hours)
4. **Cross-Reference Libraries**: Add profile examples to stat_frameworks, power_systems, genre_tropes (2-3 hours)
5. **Create Integration Guide**: NARRATIVE_MECHANICS_INTEGRATION.md workflow document (1-2 hours)

---

## What Gets FIXED

### Before Integration
```
Player: "I want DanDaDan campaign!"
AIDM: *Loads dandadan_profile.md*
      "Psychic chaos, rapid tonal shifts, absurd energy!"
      *Narrates beautifully*
Player: "I use psychic slam!"
AIDM: *Improvises* "Roll 1d20+INT... uh, costs... 20 MP?"
      ❌ No guidance from profile, guessing mechanics
```

### After Integration
```
Player: "I want DanDaDan campaign!"
AIDM: *Loads dandadan_profile.md*
      *Reads Mechanical Implementation section*
      "Momo's Psychic Power Pool: 280 MP, Slam costs 30 MP"
      *Reads Power System Integration*
      "Using psionic_psychic_systems.md framework"
      *Reads Character Creation Guidelines*
      "3-stat framework, MIND 8/10 for Momo"
Player: "I use psychic slam!"
AIDM: "30 MP cost. Roll 1d20+MIND. [Success] Alien SLAMS into wall!"
      "Momo's MP: 280 → 250. Psychic grip still strong!"
      ✅ Mechanics from profile + narration from Combat Narrative Style
```

---

## Questions for User

1. **Approve mechanical integration approach?** (Add 3 sections to each CORE profile)
2. **Detail level preference?** (Minimal 300w / Standard 500w / Comprehensive 800w per section)
3. **Genre tropes integration depth?** (Quick cross-links / Full bidirectional)
4. **Power systems verification?** (Verify first / Expand as needed)
5. **Which profile to prototype first?** (DanDaDan / Hunter x Hunter / Attack on Titan / User choice)

**Respond with decisions and I'll begin immediately!**

---

**End of Summary**  
**Full analysis**: `INTEGRATION_ANALYSIS.md` (10,000+ words with examples, integration maps, phase breakdowns)
