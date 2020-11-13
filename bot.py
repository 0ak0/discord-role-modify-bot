import discord
import os
from discord.ext import commands
from discord.ext.commands import has_permissions
from dotenv import load_dotenv
import asyncio

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='role!')

# Bot should allow for the following (role = users own personal cosmetic role unique to them):
# Change color using basic names or hex codes
# Change name of the role
# Should NOT be able to change own perms in any way
# Should NOT be able to modify anyone elses role in any way (server admins have the server settings to do this)


@client.event
async def on_ready():
    print(f'{client.user} connected.')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="role!help"))
