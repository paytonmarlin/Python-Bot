# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import random

msg = None
tennis = "\N{TABLE TENNIS PADDLE AND BALL}"

#New update in Discord needs permissions to be accessable by bot, can activiate in the developer window!
intents = discord.Intents.all()
intents.members = True

#Now we will load the .env file we created with information for bot to use
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') #Global variables so the scope is the whole project
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=intents) #Gets the Client class with the intent permissions to DM users

#One event to handle if the bot comes online in the Discord Server
@client.event
async def on_ready(): #provides validation for bot if connected to discord/server
        
        channel = client.get_channel('755859489302773882')
           
        for guild in client.guilds: #prints out the guild that the bot is in
            if guild.name == GUILD:
                break

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        
        )

    #Print out each member in the member list by using 'guild.fetch_members' to fetch all members
        print("\nMember list:")
        async for member in guild.fetch_members(limit=150):
            print("\t-" + member.name)


#Another event to handle if a new member joins the server
@client.event
async def on_member_join(member):
    #Will DM a member when they join
    await member.create_dm()
    await member.dm_channel.send(
        f'''Hi {member.name}, welcome to my Discord server, please enjoy the stay!

        This server is for INFOTC 2620, Simulations Design and Modeling. Payton is the PLA for this course, so please message him over discord
        shall you have any questions. Additionally, you can email pjmddc@mail.missouri.edu if would rather email. Have fun designing!
        '''
    )


#Another event to handle response to messages containing a keyword
@client.event
async def on_message(message):
    if message.author == client.user: #This is necessary to allow bot not to message itself, which makes a infinite loop of messages
        return
#A list of funky quotes from my favorite TV Show
    AoS_Quotes = [
        '''\nJust because we don't understand something yet, doesn't mean we have to regress back to the dark ages
            -Jemma Simmons''',
        '''\nI really wish I hadn't eaten that hot-pocket earlier
            -Agent Coulson''',
        '''\nUsually, one person doesn't have the solution but... 100 people with 1% of the solution? That'll get it done.
            -Skye''',
        '''\nNick Fury gave me this badge. When he did, I swore an oath. We all did. To serve when everything else fails.
        To be humanity's last line of defense.
        To be the shield.
            -Coulson''']

    mandoQuote = [
        '''This is the way
        -The Mando''',
        '''I can bring you in warm, or I can bring you in cold
        -The Mando''',
        '''I'm a Mandalorian. Weapons are part of my religion
        -The Mando''']
    
    if 'shield' in message.content.lower(): #If the keyword 'shield' is in a channel, it will send random quote
        response = random.choice(AoS_Quotes)
        await message.channel.send(response)

    if 'yoda' in message.content.lower():
        response_2=random.choice(mandoQuote)
        await message.channel.send(response_2)
        await message.channel.send("\nThe power of Grogu, I summon")
        await message.channel.send(file=discord.File('grogu.jpeg'))


#Another event to handle reactions to messages
##@client.event
##async def on_reaction_add(reaction, user):
##        #Channel = client.get_channel('755859489302773882')
##        
##        if reaction.user == client.user:
##                return
##        
##        if reaction.message == msg and reaction.emoji ==tennis:
##                verified = discord.utils.get(user.server.roles, name="verified")
##                await client.add_roles(user, verified)


client.run(TOKEN)
