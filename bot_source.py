# bot_source.py

import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
GEN_CHANNEL = os.getenv('DISCORD_GEN_CH')

client = discord.Client()


@client.event
async def on_ready():
    # handier code that makes use of discord.py functions
    # lambda means that you can have multiple arguements, but only one expression
    # guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    # simple code
    # for guild in client.guilds:
    #   if guild.name == GUILD:
    #      break

    # or even simpler
    guild = discord.utils.get(client.guilds, name=GUILD)
    # don't need an env var
    text_ch = discord.utils.get(guild.text_channels, name='general')




    print(
        f'{client.user} has connected to Discord! \n'
        f'{client.user} has connected to the following guild: \n'
        f'{guild.name} (id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'list of guild members: \n - {members}')
    await text_ch.send('Hello, I LIVE MASTER')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the Discord Channel!'
    )


client.run(TOKEN)
