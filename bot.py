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
            json.dump({"general: []"}, f, indent=2)
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

    if message.content.lower() == '!strat':
        strat = random.choice(strats)
        await message.channel.send(f"🎲 **Strat Roulette:** {strat}")

client.run(TOKEN)
