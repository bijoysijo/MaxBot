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

@bot.event
async def on_raw_reaction_add(payload):
  # print(f"channel_id: {payload.channel_id}, emoji: {payload.emoji}, event_type: {payload.event_type}, guild_id: {payload.guild_id}, member: {payload.member}, message_id: {payload.message_id}, user_id: {payload.user_id}")
  channel = bot.get_channel(payload.channel_id)
  message = await channel.fetch_message(payload.message_id)
  message_author = message.author
  await channel.send(f"{payload.member} just reacted to a message from {message_author}")

bot.run(os.getenv('TOKEN', 'Token not found'))
