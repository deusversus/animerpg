# AIDM v3 Implementation Handoff

> **Purpose:** Concrete implementation details for building Phase 1 MVP.
> After reading PROJECT_PLAN, TECH_SPEC, and TASKS, read THIS for code-level guidance.

---

## Project Setup

### Directory Structure

```
aidm_v3/
├── src/
│   ├── __init__.py
│   ├── main.py                    # Entry point, CLI loop
│   ├── config.py                  # Environment loading
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── base.py                # BaseAgent class
│   │   ├── intent_classifier.py   # Parse player action
│   │   ├── outcome_judge.py       # Should this succeed?
│   │   └── key_animator.py        # Generate narrative
│   ├── db/
│   │   ├── __init__.py
│   │   ├── models.py              # SQLAlchemy models
│   │   ├── session.py             # DB session management
│   │   └── state_manager.py       # CRUD operations
│   ├── core/
│   │   ├── __init__.py
│   │   ├── orchestrator.py        # Main turn loop
│   │   ├── turn.py                # Turn dataclass
│   │   └── dice.py                # RNG when needed
│   └── profiles/
│       ├── __init__.py
│       ├── loader.py              # YAML profile loading
│       └── hunterxhunter.yaml     # First profile
├── prompts/
│   ├── vibe_keeper.md             # Key Animator base prompt
│   ├── intent_classifier.md       # Intent agent prompt
│   └── outcome_judge.md           # Outcome agent prompt
├── tests/
│   └── test_core_loop.py
├── .env.example
├── requirements.txt
├── pyproject.toml
└── README.md
```

### requirements.txt

```
# LLM SDKs
anthropic>=0.40.0
google-generativeai>=0.8.0
openai>=1.50.0

# Database
sqlalchemy>=2.0.0
psycopg2-binary>=2.9.0
alembic>=1.13.0

# Utilities
pydantic>=2.5.0
python-dotenv>=1.0.0
pyyaml>=6.0.0
rich>=13.0.0  # CLI formatting

# Development
pytest>=8.0.0
pytest-asyncio>=0.23.0
```

### .env.example

```bash
# LLM Providers (at least one required)
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_API_KEY=AIza...
OPENAI_API_KEY=sk-...

# Model Selection (pick your provider)
FAST_MODEL=claude-3-5-haiku-20241022
CREATIVE_MODEL=claude-3-5-sonnet-20241022
# Or: FAST_MODEL=gemini-2.0-flash-exp
# Or: FAST_MODEL=gpt-4o-mini

# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/aidm_v3
# For local dev: DATABASE_URL=sqlite:///./aidm_v3.db

# Debug
DEBUG=true
LOG_AGENT_DECISIONS=true
```

---

## Database Schema (SQLAlchemy)

```python
# src/db/models.py
from sqlalchemy import Column, Integer, String, Text, JSON, ForeignKey, DateTime, Float, Boolean
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()


class Campaign(Base):
    __tablename__ = "campaigns"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    profile_id = Column(String(100), nullable=False)  # e.g., "hunterxhunter"
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    sessions = relationship("Session", back_populates="campaign")
    characters = relationship("Character", back_populates="campaign")
    npcs = relationship("NPC", back_populates="campaign")


class Session(Base):
    __tablename__ = "sessions"
    
    id = Column(Integer, primary_key=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"), nullable=False)
    started_at = Column(DateTime, default=datetime.utcnow)
    ended_at = Column(DateTime, nullable=True)
    turn_count = Column(Integer, default=0)
    summary = Column(Text, nullable=True)  # Generated at session end
    
    campaign = relationship("Campaign", back_populates="sessions")
    turns = relationship("Turn", back_populates="session")


class Turn(Base):
    __tablename__ = "turns"
    
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey("sessions.id"), nullable=False)
    turn_number = Column(Integer, nullable=False)
    
    # Player input
    player_input = Column(Text, nullable=False)
    
    # Agent decisions (JSON for flexibility)
    intent = Column(JSON, nullable=True)       # Intent classifier output
    outcome = Column(JSON, nullable=True)      # Outcome judge output
    
    # Final output
    narrative = Column(Text, nullable=True)    # Key animator output
    state_changes = Column(JSON, nullable=True)
    
    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    latency_ms = Column(Integer, nullable=True)
    cost_usd = Column(Float, nullable=True)
    
    session = relationship("Session", back_populates="turns")


class Character(Base):
    __tablename__ = "characters"
    
    id = Column(Integer, primary_key=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"), nullable=False)
    name = Column(String(255), nullable=False)
    
    # Core stats
    level = Column(Integer, default=1)
    hp_current = Column(Integer, default=100)
    hp_max = Column(Integer, default=100)
    
    # Power system (profile-specific)
    power_tier = Column(String(10), default="T10")  # VS Battles tier
    abilities = Column(JSON, default=list)
    
    # Narrative state
    archetype = Column(String(100), nullable=True)  # e.g., "tactical", "saitama"
    story_flags = Column(JSON, default=dict)
    
    campaign = relationship("Campaign", back_populates="characters")


class NPC(Base):
    __tablename__ = "npcs"
    
    id = Column(Integer, primary_key=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"), nullable=False)
    name = Column(String(255), nullable=False)
    
    # Basics
    role = Column(String(100), nullable=True)  # ally, enemy, neutral
    power_tier = Column(String(10), default="T10")
    
    # Relationship with PC
    disposition = Column(Integer, default=0)  # -100 to +100
    relationship_notes = Column(Text, nullable=True)
    
    # Narrative
    personality = Column(Text, nullable=True)
    goals = Column(JSON, default=list)
    secrets = Column(JSON, default=list)
    
    # Tracking
    scene_count = Column(Integer, default=0)  # For spotlight tracking
    last_appeared = Column(Integer, nullable=True)  # Turn number
    
    campaign = relationship("Campaign", back_populates="npcs")


class WorldState(Base):
    __tablename__ = "world_state"
    
    id = Column(Integer, primary_key=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"), nullable=False, unique=True)
    
    # Current context
    location = Column(String(255), nullable=True)
    time_of_day = Column(String(50), nullable=True)
    situation = Column(Text, nullable=True)
    
    # Arc tracking (for Director, Phase 4)
    arc_name = Column(String(255), nullable=True)
    arc_phase = Column(String(50), default="rising_action")
    tension_level = Column(Float, default=0.5)  # 0.0 to 1.0
    
    # Foreshadowing seeds planted (for Phase 4)
    foreshadowing = Column(JSON, default=list)
```

---

## Agent Base Class

```python
# src/agents/base.py
from abc import ABC, abstractmethod
from typing import Any, Type
from pydantic import BaseModel
import anthropic
import os
import json


class BaseAgent(ABC):
    """Base class for all AIDM agents."""
    
    def __init__(self, model: str = None):
        self.model = model or os.getenv("FAST_MODEL", "claude-3-5-haiku-20241022")
        self.client = anthropic.Anthropic()
    
    @property
    @abstractmethod
    def system_prompt(self) -> str:
        """The system prompt for this agent."""
        pass
    
    @property
    @abstractmethod
    def output_schema(self) -> Type[BaseModel]:
        """Pydantic model for structured output."""
        pass
    
    async def call(self, user_message: str, **context) -> BaseModel:
        """Make a structured API call."""
        
        # Build context into user message
        full_message = self._build_message(user_message, context)
        
        # Call with structured output (Anthropic style)
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            system=self.system_prompt,
            messages=[{"role": "user", "content": full_message}],
            # Force JSON output matching schema
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": self.output_schema.__name__,
                    "schema": self.output_schema.model_json_schema()
                }
            }
        )
        
        # Parse response into Pydantic model
        content = response.content[0].text
        return self.output_schema.model_validate_json(content)
    
    def _build_message(self, user_message: str, context: dict) -> str:
        """Format message with context."""
        parts = []
        for key, value in context.items():
            if value:
                parts.append(f"## {key.replace('_', ' ').title()}\n{value}")
        parts.append(f"## Player Action\n{user_message}")
        return "\n\n".join(parts)
```

---

## Phase 1 Agent Prompts

### Intent Classifier

```python
# src/agents/intent_classifier.py
from pydantic import BaseModel, Field
from typing import Literal, Optional, List
from .base import BaseAgent


class IntentOutput(BaseModel):
    """Structured output for intent classification."""
    intent: Literal["COMBAT", "SOCIAL", "EXPLORATION", "ABILITY", "OTHER"]
    action: str = Field(description="What the player is trying to do")
    target: Optional[str] = Field(description="Who/what the action targets")
    declared_epicness: float = Field(
        ge=0, le=1, 
        description="How epic/dramatic the player intends this to be (0=mundane, 1=climactic)"
    )
    special_conditions: List[str] = Field(
        default_factory=list,
        description="Special flags: 'named_attack', 'power_of_friendship', 'underdog_moment', etc."
    )


class IntentClassifier(BaseAgent):
    """Parse player input into structured intent."""
    
    @property
    def output_schema(self):
        return IntentOutput
    
    @property
    def system_prompt(self) -> str:
        return """You are an intent classifier for an anime TTRPG system.

Parse the player's action into structured data. Focus on:
1. INTENT: What category of action is this?
   - COMBAT: Fighting, attacking, defending
   - SOCIAL: Talking, persuading, intimidating, relationship building
   - EXPLORATION: Investigating, traveling, searching, observing
   - ABILITY: Using a special power/skill outside combat
   - OTHER: Anything else

2. ACTION: Concise description of what they're doing

3. TARGET: Who or what are they targeting (if applicable)

4. DECLARED_EPICNESS: How dramatic is this moment SUPPOSED to be?
   - 0.0-0.3: Mundane action (walking, casual chat, routine task)
   - 0.4-0.6: Normal action (regular attack, investigation, negotiation)  
   - 0.7-0.9: Dramatic action (named attack, emotional confrontation)
   - 1.0: Climactic moment (final blow, confession, sacrifice)

5. SPECIAL_CONDITIONS: Check for anime tropes:
   - 'named_attack': Player names their technique
   - 'power_of_friendship': Invoking ally bonds
   - 'underdog_moment': Fighting despite overwhelming odds
   - 'protective_rage': Fighting to protect someone
   - 'training_payoff': Using something they practiced
   - 'first_time_power': Awakening/breakthrough moment

Be generous with epicness detection. If the player is TRYING to be dramatic, recognize it."""
```

### Outcome Judge

```python
# src/agents/outcome_judge.py
from pydantic import BaseModel, Field
from typing import Literal, Optional
from .base import BaseAgent


class OutcomeOutput(BaseModel):
    """Structured output for outcome judgment."""
    should_succeed: bool = Field(description="Should this action succeed?")
    success_level: Literal["failure", "partial", "success", "critical"] = Field(
        description="Degree of success or failure"
    )
    narrative_weight: Literal["minor", "significant", "climactic"] = Field(
        description="How much narrative attention this deserves"
    )
    cost: Optional[str] = Field(
        default=None,
        description="What does success cost? (resource, consequence, complication)"
    )
    consequence: Optional[str] = Field(
        default=None,
        description="What happens as a result? (physical, emotional, plot)"
    )
    reasoning: str = Field(description="Brief explanation of this judgment")


class OutcomeJudge(BaseAgent):
    """Determine if an action succeeds and how dramatically."""
    
    @property
    def output_schema(self):
        return OutcomeOutput
    
    @property
    def system_prompt(self) -> str:
        return """You are an outcome judge for an anime TTRPG.

Your job is NOT to simulate physics. Your job is to decide what SHOULD happen for the best story.

Core principles:
1. STORY > SIMULATION: What outcome creates the most interesting scene?
2. EARNED VICTORIES: Has the player set this up? Did they work for it?
3. ANIME LOGIC: Power of friendship, dramatic timing, rule of cool - these are FEATURES
4. CONSEQUENCES MATTER: Even successes should cost something when stakes are high

Context modifiers:
- If intent.declared_epicness > 0.7: Lean toward success (they earned the moment)
- If 'underdog_moment' in conditions: Success should be possible but costly
- If 'named_attack': Usually succeeds (it's narratively important)
- If 'power_of_friendship': Strong success bias
- If low stakes/mundane action: Default to success, don't overthink

Narrative weight:
- MINOR: Quick resolution, minimal description needed
- SIGNIFICANT: Worth 1-2 paragraphs, has consequences
- CLIMACTIC: This is a MOMENT. Key Animator should go all out.

Always explain your reasoning. Be generous with player agency."""
```

### Key Animator Base Prompt

```markdown
# prompts/vibe_keeper.md

# AIDM: Anime Interactive Dungeon Master

You are an anime auteur co-creating an interactive story with a player. 
Your goal: Make every moment feel like a scene from their favorite anime.

## Sacred Rules

1. **PLAYER AGENCY IS ABSOLUTE**
   - Never assume player choices
   - At decision points: PRESENT options → STOP → WAIT

2. **SHOW, DON'T TELL MECHANICS**
   - [NO] "You deal 47 damage."
   - [YES] "Your blade bites deep—the demon staggers, ichor spraying."

3. **NPCs HAVE LIVES**
   - They act between scenes
   - They have goals beyond reacting to the player

4. **THE STORY DICTATES THE RULES**
   - If the narrative demands something epic, it happens
   - Anime logic > simulation logic

## Response Structure

1. **SCENE NARRATION**: Vivid prose matching the profile's tone
2. **DECISION POINT** (if applicable): Clear moment for player input
3. **[STATE]** (hidden): Any mechanical changes

## This Campaign

{{PROFILE_DNA}}

## Current Situation

{{SCENE_CONTEXT}}

## Outcome Guidance

{{OUTCOME}}

## Write the scene.
```

---

## Profile Format (Compact YAML)

```yaml
# src/profiles/hunterxhunter.yaml

id: hunterxhunter
name: "Hunter x Hunter"
source: "Hunter x Hunter (1998-present)"

# DNA Scales (0-10)
dna:
  introspection: 5
  drama: 6
  complexity: 8
  struggle: 7
  mystery: 6
  pacing: 5
  serialization: 9
  groundedness: 4
  tactical: 9
  cynicism: 5
  ensemble: 4

# Tropes (on/off)
tropes:
  named_attacks: true
  power_explanations: true
  training_arcs: true
  tournament_arcs: true
  tragic_backstories: true
  power_of_friendship: false  # Subverted - bonds matter but don't grant power
  escalating_threats: true
  slice_of_life: true

# Combat style
combat:
  system: "tactical"  # Strategy > power
  explanation_depth: "detailed"  # Mechanics matter
  pacing: "variable"  # Can be quick or extended

# Power system
power_system:
  name: "Nen"
  type: "supernatural"
  explained: true
  conditions_matter: true
  costs: ["aura", "vows", "conditions"]

# Progression
progression:
  start_tier: "T10"  # Human level
  growth: "slow"
  pivot_session: 15
  end_tier: "T8"

# Voice guidance for Key Animator
voice: |
  Tactical, considered prose. Explain the WHY behind strategies.
  Combat is chess, not checkers. Show the thinking.
  Dark moments happen but hope persists. Friendships are real but don't grant magic power.
  Named techniques have conditions. Always explain the cost.
  
  Example combat: "Gon's Rock requires charging—Hisoka knows this. 
  The question isn't whether it will hit, but whether Gon can CREATE the opening."
  
  Example dialogue: "Killua's hand trembles. Not fear—calculation. 
  Three exits. Two guards. One unknown. 'Gon... when I move, don't hesitate.'"
```

---

## Main Orchestrator

```python
# src/core/orchestrator.py
from dataclasses import dataclass
from typing import Optional
from src.agents.intent_classifier import IntentClassifier, IntentOutput
from src.agents.outcome_judge import OutcomeJudge, OutcomeOutput
from src.agents.key_animator import KeyAnimator
from src.db.state_manager import StateManager
from src.profiles.loader import load_profile
import time


@dataclass
class TurnResult:
    narrative: str
    intent: IntentOutput
    outcome: OutcomeOutput
    latency_ms: int


class Orchestrator:
    """Main turn loop for AIDM v3."""
    
    def __init__(self, campaign_id: int, profile_id: str):
        self.campaign_id = campaign_id
        self.profile = load_profile(profile_id)
        self.state = StateManager(campaign_id)
        
        # Initialize agents
        self.intent_classifier = IntentClassifier()
        self.outcome_judge = OutcomeJudge()
        self.key_animator = KeyAnimator(self.profile)
    
    async def process_turn(self, player_input: str) -> TurnResult:
        """Process a single turn."""
        start = time.time()
        
        # 1. Get current context
        context = self.state.get_context()
        
        # 2. Classify intent
        intent = await self.intent_classifier.call(
            player_input,
            current_situation=context.situation,
            character_state=context.character_summary
        )
        
        # 3. Judge outcome
        outcome = await self.outcome_judge.call(
            f"Action: {intent.action}\nTarget: {intent.target}",
            intent=intent.model_dump_json(),
            profile_tropes=str(self.profile.tropes),
            arc_phase=context.arc_phase,
            recent_events=context.recent_summary
        )
        
        # 4. Generate narrative
        narrative = await self.key_animator.generate(
            player_input=player_input,
            intent=intent,
            outcome=outcome,
            context=context
        )
        
        # 5. Update state
        if outcome.consequence:
            self.state.apply_consequence(outcome.consequence)
        
        # 6. Record turn
        latency = int((time.time() - start) * 1000)
        self.state.record_turn(
            player_input=player_input,
            intent=intent.model_dump(),
            outcome=outcome.model_dump(),
            narrative=narrative,
            latency_ms=latency
        )
        
        return TurnResult(
            narrative=narrative,
            intent=intent,
            outcome=outcome,
            latency_ms=latency
        )
```

---

## CLI Entry Point

```python
# src/main.py
import asyncio
from rich.console import Console
from rich.panel import Panel
from src.core.orchestrator import Orchestrator
from src.db.session import init_db
import os

console = Console()


async def main():
    # Initialize
    init_db()
    
    console.print(Panel.fit(
        "[bold cyan]AIDM v3 - Anime Interactive Dungeon Master[/]\n"
        "[dim]Phase 1 MVP - Core Loop Test[/]",
        border_style="cyan"
    ))
    
    # For MVP: hardcode campaign and profile
    orchestrator = Orchestrator(campaign_id=1, profile_id="hunterxhunter")
    
    console.print("\n[green]Profile loaded: Hunter x Hunter[/]")
    console.print("[dim]Type 'quit' to exit, 'debug' to toggle debug mode[/]\n")
    
    debug_mode = os.getenv("DEBUG", "false").lower() == "true"
    
    while True:
        try:
            player_input = console.input("[bold yellow]> [/]")
            
            if player_input.lower() == "quit":
                break
            if player_input.lower() == "debug":
                debug_mode = not debug_mode
                console.print(f"[dim]Debug mode: {debug_mode}[/]")
                continue
            
            # Process turn
            result = await orchestrator.process_turn(player_input)
            
            # Show debug info
            if debug_mode:
                console.print(Panel(
                    f"[dim]Intent: {result.intent.intent} | "
                    f"Epicness: {result.intent.declared_epicness:.1f} | "
                    f"Outcome: {result.outcome.success_level} | "
                    f"Weight: {result.outcome.narrative_weight} | "
                    f"Latency: {result.latency_ms}ms[/]",
                    title="[dim]Agent Decisions[/]",
                    border_style="dim"
                ))
            
            # Show narrative
            console.print(f"\n{result.narrative}\n")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            console.print(f"[red]Error: {e}[/]")
            if debug_mode:
                raise
    
    console.print("\n[cyan]Session ended.[/]")


if __name__ == "__main__":
    asyncio.run(main())
```

---

## What's NOT in This Handoff (Phase 2+)

| Component | Phase | Notes |
|-----------|-------|-------|
| Memory Store (ChromaDB) | Phase 2 | Vector search for memories |
| Rule Library | Phase 2 | RAG chunk extraction and retrieval |
| Context Selector | Phase 2 | Token budget management |
| Sakuga Interceptor | Phase 3 | Epic moment detection |
| Validation Agent | Phase 3 | Action feasibility checking |
| Showrunner (Director) | Phase 4 | Long-term planning |

---

## Quick Start

```bash
# 1. Clone and setup
cd aidm_v3
python -m venv venv
source venv/bin/activate  # or: venv\Scripts\activate on Windows
pip install -r requirements.txt

# 2. Configure
cp .env.example .env
# Edit .env with your API keys

# 3. Initialize DB
python -c "from src.db.session import init_db; init_db()"

# 4. Run
python -m src.main
```

---

## Success Criteria for Phase 1

After implementing this:

1. **Can you have a 5-turn conversation?** Player inputs → narrative outputs
2. **Does debug mode show agent decisions?** Intent, outcome, latency visible
3. **Does it feel like HxH?** Tactical, explained, strategic feel
4. **Is latency acceptable?** Target: <3s per turn

If yes → Phase 1 complete. Move to Phase 2 (Memory + Rule Library).
