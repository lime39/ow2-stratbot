# Overwatch 2 StratBot

**Overwatch 2 StratBot** is a lightweight and extensible Discord bot designed to enhance the gameplay experience for Overwatch 2 players by introducing randomized team strategies. Drawing inspiration from the *Strat Roulette* concept popularized in CS:GO, this bot encourages creative, unconventional, and strategic playstyles across various game modes.

The bot supports general-purpose strategies as well as role queue–friendly attack and defense-specific tactics, making it a fun and flexible addition to both casual and competitive environments.

---

## Features

- `!strat` — Returns a randomized general strategy, suitable for any match or map
- `!strat attack` / `!strat defense` — Generates side-specific strategies optimized for role queue
- `!addstrat [category] [strategy]` — Allows users to contribute their own strategies to existing categories
- `!addcategory [category_name]` — Enables the creation of new strategy categories at runtime
- Persistent strategy storage using JSON — all custom strategies and categories are saved locally