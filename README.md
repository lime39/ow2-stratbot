# Overwatch 2 StratBot

**Overwatch 2 StratBot** is a lightweight and extensible Discord bot designed to enhance the gameplay experience for Overwatch 2 players by introducing randomized team strategies. Drawing inspiration from the *Strat Roulette* concept popularized in CS:GO, this bot encourages creative, unconventional, and strategic playstyles across various game modes.

The bot supports general-purpose strategies to be used in role queue, making it a fun and flexible addition to both casual and competitive environments.

---

## Features

- `!strat` — Returns a randomized general strategy, suitable for any match or map
- `!addstrat [strategy]` — Allows users to contribute their own strategies to existing categories
- Persistent strategy storage using JSON — all custom strategies and categories are saved locally

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/stratbot.git
cd stratbot
```

### 2. Install Dependencies
This project uses `discord.py` and `python-dotenv`:

```bash
pip install -r requirements.txt
```
If you don't have a `requirements.txt`, create one:

```bash
discord.py
python-dotenv
```

### 3. Create a `.env` File
Inside the project folder, create a file named `.env`:

```bash env
TOKEN=your_discord_bot_token_here
```
## Usage
Run the bot with:
```bash
python bot.py
```

Then in Discord:
- `!strat` - Randomly selects and sends a strategy from the general pool
- `!addstrat [strategy]` - Adds a new strategy if it doesn't already exist

Example:
```bash
!addstrat Go Lucio and ride walls only
```