# AIDM v2: Anime-Integrated Dungeon Master System

**Version 2.0-beta** - Advanced AI Dungeon Master for Dynamic Anime-Inspired RPG Experiences  
**Status**: 52 files complete, token optimized, P1 research enforcement applied  
**Token Budget**: 45,542 tokens (22.8% of 200K context) - Optimized for long campaigns ✅

---

## What Is This?

AIDM v2 is a comprehensive instruction set designed for high-quality LLMs (Large Language Models) to act as sophisticated AI Dungeon Masters for text-based anime RPG experiences. Unlike traditional game systems, AIDM v2:

- **Researches and integrates** real anime settings, characters, and power systems (VS Battles Wiki priority)
- **Fuses multiple anime** into coherent, playable worlds with power harmonization
- **Maintains persistent state** across sessions through exportable save files
- **Adapts to any anime genre** (isekai, shonen, seinen, slice-of-life, mecha, etc.)
- **Learns player preferences** and evolves narratives dynamically
- **Manages complex JRPG mechanics** (HP/MP/SP, skills, leveling, combat)
- **Enforces research protocols** with automatic blocking mechanisms (no hallucination tolerance)

---

## Quick Start

### For Players

1. **Choose Your LLM**: Upload these files to ChatGPT, Claude, Gemini, or another high-quality LLM
2. **Load Core Instructions**: Start by uploading `/docs/CORE_AIDM_INSTRUCTIONS.md`
3. **Add Essential Schemas**: Upload `/schemas/character_schema.json` and `/schemas/world_state_schema.json`
4. **Start Session Zero**: Say "I want to begin Session Zero" and follow the AIDM's guided character creation
5. **Play**: Interact naturally - the AIDM handles everything else

### For Returning Players

1. **Load Your Save**: Paste your exported session state (from previous session)
2. **Resume Play**: The AIDM will reconstruct your complete game state

### For Developers/Tinkerers

1. **Read Architecture**: See `/docs/ARCHITECTURE.md` for system design
2. **Check Scope**: See `/docs/SCOPE.md` for what's included/excluded
3. **Review Guidelines**: See `/docs/DEVELOPMENT.md` for modification guidelines

---

## Project Structure

```
/docs                           # Development documentation
  ├── ARCHITECTURE.md           # Complete system design (52 files)
  ├── SCOPE.md                  # In/out of scope boundaries
  ├── DEVELOPMENT.md            # AI collaboration guidelines
  └── STATE.md                  # Current project status (comprehensive changelog)

/aidm                           # AIDM system files (upload to LLMs)
  ├── CORE_AIDM_INSTRUCTIONS.md # Master control file (2,847 words)
  ├── /instructions             # Behavioral instruction modules (13 files)
  ├── /schemas                  # JSON data structures (7 files)
  ├── /libraries                # Pre-built knowledge bases (12 files)
  │   ├── /genre_tropes         # Anime genre conventions (4 files)
  │   ├── /power_systems        # Power frameworks (5 files, universal taxonomy)
  │   └── /common_mechanics     # JRPG mechanics references (3 files)
  └── /quick_references         # Combat & progression quick refs (2 files)

/tests                          # Testing framework
  ├── /test_scripts             # 8 acceptance test procedures
  └── /results                  # Test execution logs

/backup                         # System backups
  └── aidm_pre_phase1_backup_*.zip  # Pre-optimization snapshots

/tools                          # Development utilities
  └── state_validator.py        # Game state consistency checker

/.github/instructions           # GitHub Copilot workspace instructions
TOKEN_OPTIMIZATION_AUDIT.md     # Comprehensive token budget analysis
CONTINUE_HERE.md                # Quick continuation guide for new sessions
```

---

## Key Features

### 🎭 Anime Integration
- **Automatic Research Protocol**: AIDM automatically researches anime when mentioned (blocking, non-negotiable)
- **VS Battles Wiki Priority**: Standardized power scaling via VS Battles Wiki (Tier 10-C to 2-A+)
- **Verification Loop**: Confirms findings with you to prevent hallucinations
- **Multi-Anime Fusion**: Intelligently harmonizes conflicting power systems
- **Genre Awareness**: Adapts tone and mechanics to anime genre
- **Research Enforcement**: ABORT mechanisms prevent progression without complete research

### 🧠 Advanced Intelligence
- **Intent Classification**: Distinguishes dialogue, thought, meta-commands, and narrative
- **Memory Threading**: Persistent, evolving memory across unlimited sessions
- **NPC Relationships**: Complex affinity systems with realistic social dynamics
- **Emergent Narrative**: World evolves independently based on hidden systems

### ⚔️ Complete JRPG Mechanics
- **Flexible Stats**: HP/MP/SP system adaptable to any anime power system
- **Unified Skills**: Covers physical combat, magic, psionics, unique abilities
- **Progression Systems**: Experience, leveling, skill mastery
- **Combat Resolution**: Tactical turn-based or narrative-focused combat

### 💾 Session Persistence
- **Export/Import**: Complete game state saved as JSON/YAML
- **Cross-Session Memory**: Resume exactly where you left off
- **State Validation**: Built-in consistency checking prevents errors

### 🎮 Player-Calibrated Experience
- **Content Preferences**: Tragedy, romance, violence, explicitness levels
- **Gameplay Balance**: Combat complexity, puzzle difficulty, social depth
- **Difficulty Scaling**: Power fantasy to brutal challenge
- **Narrative Pacing**: Episodic adventures vs. long story arcs

---

## Example Usage

### Creating a Naruto-Inspired Character
```
Player: "I want to play in a world like Naruto, but with gate awakeening like Solo Leveling."

AIDM: [Researches both anime, confirms findings]
"I've researched Naruto's chakra-based ninja system and Solo Leveling's gate/hunter mechanics. 
I'll create a world where ancient ninja clans discovered 'Gates' - dimensional portals that 
awakened chakra potential. Your character will use both systems. Shall we begin character creation?"
```

### Mid-Combat Action
```
Player: "I channel chakra into my legs and leap onto the rooftop, then activate Shadow Clone Jutsu!"

AIDM: [Tracks MP consumption, validates skill prerequisites, updates position]
"You surge chakra through your legs (−15 MP), launching yourself three stories up in a blur. 
Landing smoothly on the tiled roof, you form the cross-seal: 'Shadow Clone Jutsu!' (−30 MP). 
Five perfect copies materialize around you in puffs of smoke. The bandit below freezes, 
eyes widening. [Current: HP 145/145, MP 75/120, SP 95/100]"
```

### Exporting Your Game
```
Player: "META: Export state"

AIDM: [Generates complete JSON export]
"Your game state has been exported. Copy the JSON below and save it locally..."
```

---

## System Requirements

### Minimum LLM Capabilities
- **Context Window**: 32K+ tokens recommended (128K+ ideal)
- **Web Search**: Ability to research anime/manga (ChatGPT with browsing, Perplexity, etc.)
- **JSON Processing**: Can parse and generate structured data
- **File Upload**: Can accept uploaded instruction files

### Recommended LLMs (as of October 2025)
- **OpenAI GPT-4** (with web browsing enabled)
- **Anthropic Claude 3.5 Sonnet** or **Claude 3 Opus**
- **Google Gemini 1.5 Pro** (with extended context)
- **Perplexity** (excellent for anime research)

---

## Architecture Overview

AIDM v2 is built on a modular architecture with 6 core systems:

1. **Cognitive Engine**: Processes player input and classifies intent
2. **Learning Engine**: Manages memory and adapts to player preferences
3. **State Manager**: Tracks game mechanics, world state, and persistence
4. **NPC Intelligence**: Realistic relationship dynamics and social networks
5. **Narrative Systems**: Emergent storytelling, drift, and consistency
6. **Anime Integration**: Research, fusion, and genre adaptation

See `/docs/ARCHITECTURE.md` for detailed system design.

---

## Project Philosophy

AIDM v2 is designed around three core principles:

### 1. **Player Agency First**
The AI enhances your story, never replaces your choices. The "Verbatim Echo Rule" ensures your words are always honored.

### 2. **Failure Creates Story**
Bad rolls and setbacks aren't dead ends—they're narrative opportunities that make victories more meaningful.

### 3. **Emergent Complexity**
Simple, well-designed systems interact to create unpredictable, engaging experiences that surprise even the AI.

---

## Project Status

**Current Version**: 2.0 (October 2025)  
**Status**: Production-ready MVP  
**Last Updated**: See `/docs/STATE.md`

### Completed Features
✅ Complete AIDM architecture from v1  
✅ Anime research and integration system  
✅ Multi-anime fusion framework  
✅ JRPG mechanics implementation  
✅ Session persistence (export/import)  
✅ Genre-specific trope libraries  
✅ Power system harmonization  
✅ Player calibration system  

### Planned Enhancements
🔄 Advanced emotional intelligence (AIDM Improvement Proposal features)  
🔄 Multimodal integration (images, audio)  
🔄 Federated learning network  
🔄 Constitutional AI ethics framework  

---

## Contributing

This project is designed to be extended and customized:

- **Add Genre Libraries**: Create new trope files for underserved anime genres
- **Expand Power Systems**: Document additional power frameworks
- **Create Templates**: Build example characters, worlds, or scenarios
- **Improve Instructions**: Refine AIDM behavior based on play experience

See `/docs/DEVELOPMENT.md` for contribution guidelines.

---

## Credits

**AIDM v2** builds upon:
- **Original Isekai RPG System** (20 instruction files, archived in `/isekairpg_old`)
- **AIDM System Architecture** (comprehensive AI DM framework)
- **AIDM Improvement Proposal 2025** (cutting-edge AI research integration)

**Created by**: [Your Name]  
**License**: [Your License Choice]  
**Version**: 2.0  
**Date**: October 2025

---

## Support & Community

- **Bug Reports**: Create an issue describing the problem
- **Feature Requests**: Suggest improvements in discussions
- **Questions**: Check `/docs/DEVELOPMENT.md` for common answers

---

## Quick Links

- [System Architecture](docs/ARCHITECTURE.md)
- [Project Scope](docs/SCOPE.md)
- [Development Guide](docs/DEVELOPMENT.md)
- [Project Status](docs/STATE.md)
- [Core AIDM Instructions](docs/CORE_AIDM_INSTRUCTIONS.md)

---

**Ready to begin your anime RPG adventure? Load the core instructions and say "Start Session Zero"!**
