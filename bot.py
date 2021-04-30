import discord
from discord.ext import commands
from discord.utils import get
import os
from dotenv import load_dotenv

# load env variables from .env file
load_dotenv()

# set required discord intents
intents = discord.Intents.all()
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)

#intializer event
@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_member_join(member):
  channel = bot.get_channel(782892132959518732)
  await channel.send(f"Heya! {member.name}, Welcome to {member.guild.name}.")

bot.run(os.getenv('TOKEN', 'Token not found'))
