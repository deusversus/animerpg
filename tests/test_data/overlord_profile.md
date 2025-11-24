# Narrative Profile: Overlord

## Mechanical Configuration

```json
{
  "economy": {
    "type": "fiat_currency",
    "parameters": {
      "currency_name": "Gold",
      "starting_amount": 1000000,
      "scarcity": "abundant",
      "inflation_rate": "none",
      "special_mechanics": ["nazarick_treasury", "yggdrasil_items", "data_crystals"]
    }
  },
  "crafting": {
    "type": "experimental",
    "parameters": {
      "craft_focus": "magic_items",
      "discovery_mode": true,
      "side_effects": true
    }
  },
  "progression": {
    "type": "static_op",
    "parameters": {
      "starting_power_tier": 8,
      "growth_focus": "technique_variety"
    }
  },
  "downtime": {
    "enabled_modes": ["faction_building", "social_links", "investigation"],
    "default_mode": "faction_building",
    "time_tracking": true,
    "faction_config": {
      "management_focus": ["military", "economy", "diplomacy", "intelligence"],
      "automation_level": "semi_automated"
    }
  }
}
```

## Anime Source

**Title**: Overlord  
**Genres**: Isekai, Dark Fantasy, Strategy  
**Power System**: Yggdrasil magic system (MMO-style with max-level protagonist)

## World Summary

A max-level player from a shutting-down MMORPG is trapped in the game world as his undead overlord character. Focus on nation-building, strategic conquest, and managing an overpowered faction rather than personal power growth.
