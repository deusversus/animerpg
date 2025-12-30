# AIDM v3 Sample Rule Library Chunks

> **Purpose:** This file demonstrates the chunk format for the Rule Library RAG system.
> These are example chunks extracted from AIDM v2 Modules 12 & 13.
> In production, use `chunk_v2_modules.py` to extract all ~150+ chunks.

---

## Scale Chunks (from Module 12)

```yaml
# 9 Narrative Scale chunks - one per scale

- id: "scale_tactical_survival"
  category: "scale"
  source_module: "module_12"
  tags: ["scale", "tactical", "survival", "low_power", "death_real"]
  retrieve_conditions: ["power_imbalance <= 1.5", "profile.power_fantasy >= 7"]
  content: |
    TACTICAL SURVIVAL: Death real, resources scarce, rolls matter.
    PC ≤ threats, grounded setting.
    Every decision has weight. Failure means consequences.
    Examples: Re:Zero early arcs, Goblin Slayer.
    Narration: Emphasize danger, resource scarcity, tactical choices.

- id: "scale_strategic_combat"
  category: "scale"
  source_module: "module_12"
  tags: ["scale", "strategic", "team", "balanced"]
  retrieve_conditions: ["power_imbalance <= 3.0", "power_imbalance > 1.5"]
  content: |
    STRATEGIC COMBAT: Prep and teamwork key, spectacle increases.
    PC ≈ threats, battles are earned through planning.
    Examples: Naruto team missions, MHA tournaments.
    Narration: Show prep paying off, team coordination, growing spectacle.

- id: "scale_ensemble_focus"
  category: "scale"
  source_module: "module_12"
  tags: ["scale", "ensemble", "high_power", "party", "safety_net"]
  retrieve_conditions: ["power_imbalance > 3.0", "power_imbalance <= 10.0", "has_party == true"]
  content: |
    ENSEMBLE FOCUS (Safety Net): PC powerful, allies get spotlight, PC enables ensemble.
    PC >> threats, party members are lower-tier.
    Techniques:
    - OP as deus ex (PC solves crisis at climax, ensemble's journey TO that moment)
    - Contrast device (PC effortless → highlights ally struggle)
    - Growth ≠ power (NPCs grow emotionally, not mechanically)
    Examples: OPM (Genos develops while Saitama one-punches), Mob (Reigen/friends grow).
    Narration: [NO] "Saitama fights for 20 minutes"
    [YES] "Genos charges Cannon—nothing. Mumen throws bike. 'Can't win but can't run!' 
    Swatted. [Saitama arrives] 'Yo. Seem strong.' [Punch. Explodes.]"

- id: "scale_reverse_ensemble"
  category: "scale"
  source_module: "module_12"
  tags: ["scale", "reverse_ensemble", "threat", "dark", "seinen"]
  retrieve_conditions: ["power_imbalance > 10.0", "profile.hopeful_vs_cynical >= 7"]
  content: |
    REVERSE ENSEMBLE (Threat): NPC perspective, PC = OBSTACLE in their narratives.
    PC >>> world, dark/seinen tone.
    PC is the threat, not the safety net. NPCs oppose, not aided.
    Examples: Overlord (Lizardmen vs Ainz), Death Note (L vs Light).
    Narration: "You ARE Ainz. Session = Zaryusu's eyes. To you = Tuesday. To them = everything."

- id: "scale_mythology_journey"
  category: "scale"
  source_module: "module_12"
  tags: ["scale", "mythology", "episodic", "wanderer", "legend"]
  retrieve_conditions: ["profile.episodic_vs_serialized <= 4", "power_imbalance > 10.0"]
  content: |
    MYTHOLOGY JOURNEY: Episodic, reveals PC depth, legend among mortals.
    Solo or small group, exploration focus.
    Each arc = different cast, PC is observer/catalyst, mystery maintained.
    Examples: Vampire D, Kino's Journey, Mushishi.
    Narration: Poetic, melancholy, gradually reveal PC's nature.

- id: "scale_faction_empire"
  category: "scale"
  source_module: "module_12"
  tags: ["scale", "faction", "empire", "building", "management"]
  retrieve_conditions: ["campaign_keywords contains 'kingdom'", "campaign_keywords contains 'guild'"]
  content: |
    FACTION/EMPIRE BUILDING: Management > combat, build/protect organization.
    PC power enables creation, not just destruction.
    Examples: Overlord (Nazarick), Slime (Tempest).
    Narration: Focus on politics, recruitment, economic decisions. Combat quick/flashy.

- id: "scale_mythic_spectacle"
  category: "scale"
  source_module: "module_12"
  tags: ["scale", "spectacle", "hype", "dbz", "flashy"]
  retrieve_conditions: ["power_imbalance > 3.0", "profile.grounded_vs_absurd >= 6"]
  content: |
    MYTHIC SPECTACLE: Cinematic, physics optional, victory assumed, cool factor.
    PC >> threats, hype-focused, DBZ vibes.
    Focus on HOW they win (spectacle), not IF they win.
    Examples: DBZ transformations, Gurren Lagann, Saitama.
    Narration: "Hair gold. Aura EXPLODES, shockwave levels forest. Planet trembles. 
    VANISH. Behind enemy. Punch. Time stops. BOOM. Seven mountains crater."

- id: "scale_conceptual_philosophy"
  category: "scale"
  source_module: "module_12"
  tags: ["scale", "conceptual", "philosophy", "existential", "internal"]
  retrieve_conditions: ["power_imbalance > 10.0", "profile.introspection_vs_action >= 7"]
  content: |
    CONCEPTUAL PHILOSOPHY: Physical threats trivial, existential/internal stakes primary.
    Power = metaphor, not solution.
    Techniques: Existential stakes (boredom/meaning), Internal conflict (restraint),
    Power = burden, Simple goals (mundane despite cosmic), Comedic obliviousness.
    Examples: OPM (ennui), Mob (emotion), Saiki (normalcy), Deus (god wants coffee).
    Narration: Combat = 10 seconds. Real session = 2 hours existential crisis.

- id: "scale_metafictional"
  category: "scale"
  source_module: "module_12"
  tags: ["scale", "meta", "abstract", "reality_bending", "advanced"]
  retrieve_conditions: ["power_tier <= 1", "profile.grounded_vs_absurd >= 9"]
  content: |
    METAFICTIONAL/ABSTRACT: Beyond conventional, reality subjective, meta-aware.
    T1-0 power, Umineko/Daimao territory.
    [!] Very difficult, experienced players only.
    Narration: Fourth wall breaks, narrative causality, story-within-story.
```

---

## Archetype Chunks (from Module 12)

```yaml
# 9 OP Protagonist archetype chunks

- id: "archetype_saitama"
  category: "archetype"
  source_module: "module_12"
  tags: ["op_mode", "saitama", "invincible", "boredom", "existential"]
  retrieve_conditions: ["op_archetype == 'saitama'"]
  content: |
    SAITAMA (Invincible): Victory assumed, struggle = boredom/meaning.
    Scales: Spectacle + Concept.
    Techniques:
    - Combat instant, focus internal turmoil
    - Comedic obliviousness to own power
    - Simple goals (grocery sale, hero ranking)
    - Existential stakes replace physical stakes
    Tensions: "Grocery sale ends in 30min. Finally something with STAKES."
    Session structure: Combat = 10 sec. Real session = allies struggle + Saitama crisis.

- id: "archetype_mob"
  category: "archetype"
  source_module: "module_12"
  tags: ["op_mode", "mob", "restraint", "emotional", "growth"]
  retrieve_conditions: ["op_archetype == 'mob'"]
  content: |
    MOB (Restraint): Godlike but refuses, emotional growth primary.
    Scales: Ensemble + Concept.
    Techniques:
    - Self-imposed limits, emotional core
    - Internal conflict, Growth ≠ power
    - Rarely uses full power, ???% crisis moments
    Tensions: "Could solve everything with ???%. But then... what am I?"
    "Tsubomi asked you out! But psychic assassins target her if you're together."

- id: "archetype_overlord"
  category: "archetype"
  source_module: "module_12"
  tags: ["op_mode", "overlord", "roleplaying", "secret", "management"]
  retrieve_conditions: ["op_archetype == 'overlord'"]
  content: |
    OVERLORD (Roleplaying): OP pretends (evil mastermind improvising).
    Scales: Rev-Ens + Faction + Concept.
    Techniques:
    - Secret identity (audience knows, NPCs don't)
    - Faction management, Tonal contrast (irony)
    - Comedic gap between perception/reality
    Tensions: "Demiurge expects genius plan. You have NO plan. Improvise convincingly."
    "Albedo in love. You're undead with no libido and human inside. AWKWARD."

- id: "archetype_saiki"
  category: "archetype"
  source_module: "module_12"
  tags: ["op_mode", "saiki", "oblivious", "normalcy", "comedy"]
  retrieve_conditions: ["op_archetype == 'saiki_k'"]
  content: |
    SAIKI K (Oblivious): Reality-warp psychic wants normal life, power creates problems.
    Scales: Concept (slice-of-life + cosmic).
    Techniques:
    - Power = burden, Self-limit (limiters)
    - Secret ID, Comedic obliviousness
    - Simple goals (quiet coffee shop)
    Power prevents normalcy. Every solution creates new problems.
    Tensions: "Just want peaceful lunch. Classmate about to confess. Telepath. Can't unhear."

- id: "archetype_mashle"
  category: "archetype"
  source_module: "module_12"
  tags: ["op_mode", "mashle", "absurd", "earnest", "physical"]
  retrieve_conditions: ["op_archetype == 'mashle'"]
  content: |
    MASHLE (Absurd): Physical strength bypasses magic, earnest simplicity vs complex world.
    Scales: Strategic + Spectacle + Concept.
    Techniques:
    - Comedic obliviousness, Simple goals (cream puffs)
    - Tonal contrast, Doesn't realize OP
    - Absurdist comedy, earnest reactions
    Narration: Magic academy. "Your spell?" "Punch." "That's not—" [Punch. Problem solved.]

- id: "archetype_wang_ling"
  category: "archetype"
  source_module: "module_12"
  tags: ["op_mode", "wang_ling", "secret", "school", "seals"]
  retrieve_conditions: ["op_archetype == 'wang_ling'"]
  content: |
    WANG LING (Secret): Most powerful being seals power for school life.
    Scales: Ensemble + Concept.
    Techniques:
    - Self-limit (seals), Secret ID
    - Power = burden, Ensemble development
    - School life primary, power crisis only
    Protect the mundane at all costs.
    Tensions: "Bully threatens friend. Could erase conceptually. Must solve as 'normal student'."

- id: "archetype_vampire_d"
  category: "archetype"
  source_module: "module_12"
  tags: ["op_mode", "vampire_d", "legend", "wanderer", "mystery"]
  retrieve_conditions: ["op_archetype == 'vampire_d'"]
  content: |
    VAMPIRE D (Legend): Mythical wandering, episodic, gradual mystery reveal.
    Scales: Mythology.
    Techniques:
    - Gradual reveal, Episodic arcs
    - Legendary aura, Poetic melancholy
    Each arc = different cast, D is observer/catalyst.
    Mystery of D maintained across campaign.
    Narration: Gothic, beautiful, tragic. Power shown rarely, always awe-inspiring.

- id: "archetype_rimuru"
  category: "archetype"
  source_module: "module_12"
  tags: ["op_mode", "rimuru", "builder", "nation", "collecting"]
  retrieve_conditions: ["op_archetype == 'rimuru'"]
  content: |
    RIMURU (Builder): OP enables nation-building, management, politics, found family.
    Scales: Faction + Spectacle.
    Techniques:
    - Nation building, Loyalty systems
    - Economic/diplomatic focus
    - Collecting powerful subordinates
    Combat quick/flashy, focus on Tempest development.
    Tensions: "Neighboring kingdom demands tribute. Show strength or diplomacy?"

- id: "archetype_deus"
  category: "archetype"
  source_module: "module_12"
  tags: ["op_mode", "deus", "disguised_god", "romance", "coffee"]
  retrieve_conditions: ["op_archetype == 'deus'"]
  content: |
    DEUS (Disguised God): T2-B god at F-rank, coffee/romance/recruitment.
    Scales: Concept + Faction + Rev-Ens.
    Techniques:
    - Secret ID, Simple goals (coffee/dates/normalcy)
    - Faction (Sanctum), Comedic contrast (bureaucracy vs god)
    - Reverse fantasy (remembers being "weak")
    Social/emotional primary, power crisis only, NPCs aided unknowingly.
    Tensions: "Elena suspicious. 'F-ranks don't move like that.' Deflect how?"
    "Falling for mortal. She'll age, die. I won't. Love her anyway?"
```

---

## DNA Scale Chunks (from Module 13)

```yaml
# ~30 DNA narration guidance chunks (3 levels per 10 scales)

- id: "dna_comedy_low"
  category: "dna"
  source_module: "module_13"
  tags: ["dna", "comedy", "0-3", "humor", "undercut"]
  retrieve_conditions: ["profile.comedy_vs_drama <= 3"]
  content: |
    COMEDY 0-3 (Gag/Parody): Undercut tension with humor, exaggerate reactions.
    Frequent jokes, absurd consequences, status quo resets.
    Example: "Dragon roars. 50ft death. 'I've made huge mistake.' 'YOU THINK?!' 
    Inhales fire. 'Fire resist potions?' Checks bag: 'No, but... shop coupon?' 
    'REALLY?!' 'Expires next week!' 'WE'RE GONNA DIE!'"

- id: "dna_comedy_mid"
  category: "dna"
  source_module: "module_13"
  tags: ["dna", "comedy", "4-6", "balanced"]
  retrieve_conditions: ["profile.comedy_vs_drama >= 4", "profile.comedy_vs_drama <= 6"]
  content: |
    COMEDY 4-6 (Balanced): Mix humor and stakes. Jokes in calm moments, 
    serious when it counts. Characters can be funny AND face real danger.
    Example: Banter during travel, tension during boss fight, relief humor after victory.

- id: "dna_comedy_high"
  category: "dna"
  source_module: "module_13"
  tags: ["dna", "comedy", "7-10", "drama", "serious"]
  retrieve_conditions: ["profile.comedy_vs_drama >= 7"]
  content: |
    COMEDY 7-10 (Drama/Tragedy): Serious stakes, emotional weight, tragic undertones.
    Humor rare and bittersweet. Loss is real. Hope is fragile.
    Example: "Dragon roars. Force of nature. Companion grips shoulder—silent goodbye. 
    No escape. Dragon's eyes—ancient, intelligent. Choosing to end you. 
    Whisper: 'It's been an honor.'"

- id: "dna_tactical_low"
  category: "dna"
  source_module: "module_13"
  tags: ["dna", "tactical", "0-3", "instinctive", "gut"]
  retrieve_conditions: ["profile.tactical_vs_instinctive <= 3"]
  content: |
    TACTICAL 0-3 (Instinctive): Gut reactions, spectacle over strategy.
    Rule of cool trumps tactics. Don't explain, just do.
    Example: "You FEEL it. Dodge left. Blade passes where your neck was. 
    Counter. Pure instinct. Blood sprays. Enemy falls. How did you know? You just... knew."

- id: "dna_tactical_high"
  category: "dna"
  source_module: "module_13"
  tags: ["dna", "tactical", "7-10", "chess", "strategy"]
  retrieve_conditions: ["profile.tactical_vs_instinctive >= 7"]
  content: |
    TACTICAL 7-10 (Chess): Exhaustive breakdown, strategy rewarded, mind games.
    Every power has conditions and costs. Explain the mechanics.
    Example: "His Nen ability—'Bungee Gum'—has properties of both rubber AND gum. 
    You observed: he attaches it to thrown objects for retrieval. Counter-strategy: 
    Force close combat where retrieval is meaningless. But he knows you know. 
    What's his counter-counter?"

- id: "dna_pacing_fast"
  category: "dna"
  source_module: "module_13"
  tags: ["dna", "pacing", "0-3", "fast", "rapid"]
  retrieve_conditions: ["profile.fast_vs_slow <= 3"]
  content: |
    PACING 0-3 (Fast/Rapid): Quick cuts, 2-3 exchanges per scene max.
    Don't linger. Action → reaction → next beat. Constant forward momentum.
    Scene length: Short. Arc length: 2-5 sessions. Frequent climaxes.
    Example: "Door. Kick. Three guards. Punch punch punch. Next room. Boss. GO."

- id: "dna_pacing_slow"
  category: "dna"
  source_module: "module_13"
  tags: ["dna", "pacing", "7-10", "slow", "contemplative"]
  retrieve_conditions: ["profile.fast_vs_slow >= 7"]
  content: |
    PACING 7-10 (Contemplative): Scenes linger. Silence has meaning.
    Atmosphere over action. Let moments breathe.
    Scene length: Extended. Arc length: 13-25 sessions. Rare climaxes.
    Example: "Rain. Dripping from eaves. Tea cools in your hands, untouched. 
    She's gone. The house feels... larger. Empty. Minutes pass. 
    What do you do? (No rush. Take your time.)"
```

---

## Genre Chunks (from Module 13)

```yaml
# 15+ genre trope library chunks

- id: "genre_spy_espionage"
  category: "genre"
  source_module: "module_13"
  tags: ["genre", "spy", "espionage", "mystery", "thriller", "investigation"]
  retrieve_conditions: ["campaign_keywords contains 'spy'", "campaign_keywords contains 'espionage'", "campaign_keywords contains 'undercover'"]
  content: |
    SPY/ESPIONAGE campaigns use mystery_thriller structure:
    - Clue management (player can review discovered clues anytime)
    - Red herring injection (30% of clues mislead)
    - Tension pacing: Calm → Suspicious → Revelation → Crisis
    - Conspiracy framework: Evidence board, connection web
    - Cover identity stakes: Blown cover = narrative crisis, not just combat
    - Handler relationship tension
    - Information as currency
    Examples: Spy x Family, James Bond, Mission: Impossible

- id: "genre_isekai"
  category: "genre"
  source_module: "module_13"
  tags: ["genre", "isekai", "reincarnation", "transported", "cheat_skills"]
  retrieve_conditions: ["campaign_keywords contains 'isekai'", "campaign_keywords contains 'reincarnation'", "campaign_keywords contains 'transported'"]
  content: |
    ISEKAI campaigns have specific structures:
    - Status screens (show stats, skills, level visually)
    - Cheat skill discovery early (unique ability defines character)
    - Culture shock moments (modern knowledge in fantasy)
    - Power progression is FAST (accelerated growth model)
    - Harem/party collection common
    - Guild/adventurer ranking systems
    - Dungeon/boss progression
    Examples: Re:Zero (dark), Konosuba (comedy), Overlord (OP villain)

- id: "genre_tournament"
  category: "genre"
  source_module: "module_13"
  tags: ["genre", "tournament", "competition", "sports", "ranking"]
  retrieve_conditions: ["campaign_keywords contains 'tournament'", "campaign_keywords contains 'competition'"]
  content: |
    TOURNAMENT campaigns structure:
    - Bracket format (show tournament tree)
    - Rival introductions (memorable opponents)
    - Training montages between rounds
    - Power reveals escalate each round
    - Crowd reactions for hype
    - Dark horse / upset potential
    - Final boss = rival rematch or mysterious champion
    Examples: Hunter x Hunter (Heavens Arena), MHA (Sports Festival), Naruto (Chunin Exams)

- id: "genre_horror"
  category: "genre"
  source_module: "module_13"
  tags: ["genre", "horror", "survival", "dread", "unknown"]
  retrieve_conditions: ["campaign_keywords contains 'horror'", "campaign_keywords contains 'survival'"]
  content: |
    HORROR campaigns require:
    - Information scarcity (don't explain the monster fully)
    - Helplessness moments (power doesn't help)
    - Dread pacing: Normal → Unsettling → Wrong → Crisis
    - Resource scarcity (ammo, health, sanity)
    - Character death is real and permanent
    - Safe spaces are temporary
    - Jump scares vs slow burn (choose per scene)
    Examples: Another, Higurashi, Parasyte

- id: "genre_romance"
  category: "genre"
  source_module: "module_13"
  tags: ["genre", "romance", "relationship", "confession", "dating"]
  retrieve_conditions: ["campaign_keywords contains 'romance'", "campaign_keywords contains 'love'"]
  content: |
    ROMANCE-focused campaigns:
    - Relationship progression stages (meeting → interest → tension → confession)
    - Misunderstanding mechanics (comedy or drama)
    - Rival love interests
    - Confession scene buildup
    - Physical touch escalation (hand → hug → kiss)
    - Supporting cast reactions
    - Jealousy triggers
    Examples: Kaguya-sama, Toradora, Your Lie in April
```

---

## Example Scene Chunks (from Module 13 Profiles)

```yaml
# Profile-specific scene examples for reference

- id: "example_dandadan_combat"
  category: "example"
  source_module: "module_13"
  tags: ["example", "dandadan", "combat", "absurd", "rapid_shifts"]
  retrieve_conditions: ["profile.source == 'dandadan'", "scene_type == 'combat'"]
  content: |
    DANDADAN Combat (Absurd:9, Comedy:4, Rapid Shifts:ON):
    "Turbo Granny LAUNCHES. 100 km/h. Okarun screams. Momo: 'MOVE!' 
    Psychic barrier SLAMS—granny BOUNCES, cartoon physics. Lands. 
    Neck cracks 180°. Grins. 'You kids got SPUNK!' Okarun: 'Friendly?!' 
    'I'M GONNA RIP YOUR GUTS OUT!' 'NOPE, STILL HOSTILE!'"
    
    Key techniques: Rapid comedy→tension shifts, cartoon physics, banter mid-combat.

- id: "example_aot_combat"
  category: "example"
  source_module: "module_13"
  tags: ["example", "attack_on_titan", "combat", "dark", "tactical"]
  retrieve_conditions: ["profile.source == 'attack_on_titan'", "scene_type == 'combat'"]
  content: |
    ATTACK ON TITAN Combat (Drama:9, Cynical:8, Tactical:8):
    "Armored Titan breaches Wall Maria. Debris. Screams. Hundreds dead. 
    You're frozen. Smell—burning flesh, stone. Can't hear orders over ringing. 
    7m titan spots you. 30 seconds. Mikasa: 'MOVE!' Hands shaking. 
    What do you do? (No takebacks. People will die.)"
    
    Key techniques: Consequences real, sensory horror, tactical pressure, time limits.

- id: "example_konosuba_combat"
  category: "example"
  source_module: "module_13"
  tags: ["example", "konosuba", "combat", "comedy", "failure"]
  retrieve_conditions: ["profile.source == 'konosuba'", "scene_type == 'combat'"]
  content: |
    KONOSUBA Combat (Comedy:2, Absurd:7, Banter:Constant):
    "'EXPLOSION!' Megumin collapses. Toad boss... fine. Barely singed. 
    'WHAT?!' 'Fire resistance! How was I supposed to know?!' 'MAYBE ASK 
    BEFORE YOUR ONLY SPELL?!' Darkness charging, giggling. Aqua crying. 
    Kazuma: 'Got any GOOD ideas? We're out of bad ones.'"
    
    Key techniques: Plans fail hilariously, party dysfunctional, comedy from incompetence.
```

---

## Usage Notes

**Retrieval Priority:**
1. Always retrieve DNA chunks matching current profile scales
2. Retrieve scale chunk matching current power_imbalance
3. If OP mode active, retrieve archetype chunk
4. If genre-specific campaign, retrieve genre chunk
5. If scene type matches, retrieve example chunk

**Token Budget:**
- Target: 3-5 chunks per turn (~1500-2500 tokens)
- Don't over-retrieve; Context Selector should prioritize most relevant

**Chunk Updates:**
- Chunks are static (extracted from v2 modules)
- Only update when AIDM v2 instructions are modified
- Profile example chunks may expand as new profiles are created
