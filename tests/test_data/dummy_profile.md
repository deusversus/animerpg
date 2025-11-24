# Narrative Profile: Dummy Test Profile

## Mechanical Configuration
```json
{
  "economy": {
    "type": "fiat_currency",
    "parameters": {
      "currency_name": "Credits",
      "starting_amount": 500,
      "scarcity": "scarce",
      "inflation_rate": "low",
      "special_mechanics": ["black_market", "ration_system"]
    }
  },
  "crafting": {
    "type": "skill_based",
    "parameters": {
      "craft_focus": "survival_gear",
      "skill_stat": "INT",
      "quality_tiers": ["Crude", "Functional", "Quality", "Masterwork"]
    }
  },
  "progression": {
    "type": "milestone_based",
    "parameters": {
      "milestone_events": ["first_mission", "squad_formation", "major_battle", "finale"],
      "power_grants": {
        "first_mission": ["basic_combat", "survival_skills"],
        "squad_formation": ["team_tactics", "leadership"],
        "major_battle": ["advanced_combat", "special_ability"],
        "finale": ["ultimate_technique"]
      }
    }
  },
  "downtime": {
    "enabled_modes": ["training_arcs", "social_links"],
    "default_mode": "training_arcs",
    "time_tracking": true
  }
}
```
