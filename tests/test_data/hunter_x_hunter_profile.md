# Narrative Profile: Hunter x Hunter

## Mechanical Configuration
```json
{
  "economy": {
    "type": "fiat_currency",
    "parameters": {
      "currency_name": "Jenny",
      "starting_amount": 200,
      "scarcity": "normal",
      "inflation_rate": "none",
      "special_mechanics": ["hunter_licenses", "greed_island_currency", "bounties"]
    }
  },
  "crafting": {
    "type": "skill_based",
    "parameters": {
      "craft_focus": "greed_island_cards",
      "skill_stat": "INT",
      "quality_tiers": ["D-Rank", "C-Rank", "B-Rank", "A-Rank", "S-Rank"]
    }
  },
  "progression": {
    "type": "mastery_tiers",
    "parameters": {
      "system_name": "Nen",
      "mastery_levels": ["Novice", "Initiate", "Practitioner", "Expert", "Master"],
      "categories": [
        "Enhancement",
        "Transmutation",
        "Emission",
        "Conjuration",
        "Manipulation",
        "Specialization"
      ],
      "advancement_method": "training_arc"
    }
  },
  "downtime": {
    "enabled_modes": ["training_arcs", "social_links", "investigation"],
    "default_mode": "training_arcs",
    "time_tracking": true,
    "training_config": {
      "training_types": ["nen_mastery", "combat_techniques", "strategic_thinking"],
      "time_requirement": "weeks",
      "mentor_required": true,
      "breakthrough_chance": true
    }
  }
}
```

## Anime Source
**Title**: Hunter x Hunter  
**Genres**: Shonen, Adventure, Fantasy  
**Power System**: Nen (life energy manipulation with 6 categories)

## World Summary
A world where Hunters pursue dangerous creatures, treasure, and secrets. Characters develop Nen abilities through intense training and life-threatening battles.
