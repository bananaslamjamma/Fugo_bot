# bot_source.py

import os
from mal_api import *

import discord
from vardata import *
import random
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
GEN_CHANNEL = os.getenv('DISCORD_GEN_CH')

print("Value of ENV: ", TOKEN )
print("Value of ENV: ", GUILD )

client = discord.Client()


@client.event
async def on_ready():
    # handier code that makes use of discord.py functions
    # lambda means that you can have multiple arguments, but only one expression
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

    greetings = [
        (
            'Hello again, whaddya want boss?'
        ),
        (
            'Yeah, yeah, I\'m up.'
        ),
        (
            'Wow, you\'re reeaaallly working hard there aren\'t ya?.'
        ),
        (
            'I\'M ALIVE!'
        ),
        (
            'I\'M ALIVE!.... again.'
        ),
        (
            'Did you kiss your homies?'
        ),
        (
            ''
        )
    ]

    response = random.choice(greetings)
    await text_ch.send(response)


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the Discord Channel!'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return



    str = message.content
    print(str)
    if 'pog' in message.content.lower():
        response = random.choice(no_pog_warning)
        await message.channel.send(response)
    if '$help' == message.content.lower():
        response =random.choice(help_messages)
        await message.channel.send(response)
    if '$mal' == message.content.lower():
        text = get_mal()
        print(text)
        response = text
        await message.channel.send(response)


# exception handling
# elif message.content == 'raise-exception':
# raise discord.DiscordException


client.run(TOKEN)
