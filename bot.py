import discord
import json
import random
import os
import dotenv

TOKEN = 'TOKEN'

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Example strat pool
strats = [
    "Strat 1"
    "Strat 2"
    "Strat 3"
]

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
