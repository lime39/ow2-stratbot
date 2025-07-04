import discord
import json
import random
import os
from dotenv import load_dotenv

# Load environment variables.
load_dotenv()
TOKEN = os.getenv("TOKEN")

STRAT_FILE = "strats.json"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


# Loading strategies from the JSON file.
def load_strats():
    if not os.path.exists(STRAT_FILE):
        with open(STRAT_FILE, "w") as f:
            json.dump({"general": []}, f, indent=2)
    with open(STRAT_FILE, "r") as f:
        return json.load(f)
    
# Saving straegies back to the JSON file.
def save_strats(data):
    with open(STRAT_FILE, "w") as f:
        json.dump(data, f, indent=2)

strats = load_strats()


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content
    lower_message = content.lower()

    # Logic for !strat
    if lower_message == "!strat":
        if strats["general"]:
            strat = random.choice(strats["general"])
            await message.channel.send(f"🎲 {strat}")
        else:
            await message.channel.send("No strategies available yet!")
    
    # Logic for !addstrat [strategy text]
    elif lower_message.startswith("!addstrat"):
        parts = content.split(maxsplit=1)
        if len(parts) < 2:
            await message.channel.send("❌ Usage: `!addstrat [strategy text]`")
            return
        new_strat = parts[1].strip()
        if new_strat in strats["general"]:
            await message.channel.send("That strategy already exists!")
            return
        
        strats["general"].append(new_strat)
        save_strats(strats)
        await message.channel.send(f"🗿 Strategy added by {message.author.display_name}!")

client.run(TOKEN)
