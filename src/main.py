import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello! :avgcsmajor:')

client.run('MTE0NDA3MjQzNTI3NzI0MjQ1MQ.GHeipf.J6O9ZDoWJH-DeQ7wB6VfXQoJThgmnM3Ibvy81o')