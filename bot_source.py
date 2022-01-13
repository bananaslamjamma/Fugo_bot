# bot_source.py

import os
import re
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

def isAnime_exp(str):
    matched = re.match('{{2}.{1,}\}{2}', str)
    return bool(matched)

def isManga_exp(str):
    matched = re.match('<{2}.{1,}>{2}', str)
    return bool(matched)

def mal_embed(str, str2):
        name = str.strip(" < > { }")   
        info = get_mal_object(name, str2)
        #response = info
        embedVar = discord.Embed(title=info[0], description = info[1], color = 0x00ff00, url = "https://myanimelist.net/anime/{}".format(info[2]))
        embedVar.add_field(name = "Start Date: ", value= info[4])
        embedVar.add_field(name = "End Date: ", value= info[5])
        embedVar.add_field(name = "Popularity: ", value= info[6])
        embedVar.add_field(name = "Rank: ", value= info[7])
        if str2 == "anime":
            embedVar.add_field(name = "Number of Episodes: ", value= info[9])
        if str2 == "manga":
            embedVar.add_field(name = "Number of Chapters: ", value= info[9])
        embedVar.add_field(name = "Status: ", value= info[8])    
        embedVar.set_image(url = info[3])
        embedVar.set_footer(text = "{{anime}} <<manga>>")
        return embedVar
        
    

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
    if isAnime_exp(str):
        embedObject = mal_embed(str, "anime")
    elif isManga_exp(str):
        embedObject = mal_embed(str, "manga")
    await message.channel.send(embed=embedObject)
        


# exception handling
# elif message.content == 'raise-exception':
# raise discord.DiscordException


client.run(TOKEN)
