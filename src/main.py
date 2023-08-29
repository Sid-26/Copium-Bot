import discord
from db import findCourses
from dotenv import load_dotenv
import commands
import os
load_dotenv()
key = os.getenv('BOT_KEY')


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    commands.__init__(client)
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello! :avgcsmajor:')

    

client.run(key)
