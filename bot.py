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

@bot.command()
async def role(ctx, arg):
  all_roles = await ctx.guild.fetch_roles()
  print(all_roles)
  user = ctx.message.author
  role = get(user.guild.roles)
  print(role)
  if arg in all_roles:
    await user.add_roles(new_role)
    await ctx.send(f"{arg} role assigned to {user}.")
  else:
    new_role = await ctx.guild.create_role(name=arg)
    await user.add_roles(new_role)
    await ctx.send(f"{arg} role created and assigned to {user}.")

# async def role(ctx, arg):
#   print('Start')
#   roles = await ctx.guild.fetch_roles()
#   if arg not in roles:
#       await ctx.guild.create_role(name=arg)
#   member = ctx.message.author
#   role = get(member.guild.roles, name=arg)
#   await member.add_roles(role)
#   print('Done')
  # get all server roles.
  # check if arg role already exists.
  # if not create arg role.





# This is my dashing start to 2022! Here I come fuckers.


bot.run(os.getenv('TOKEN', 'Token not found'))
