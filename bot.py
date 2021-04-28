import discord
import os
from dotenv import load_dotenv

# load env variables from .env file
load_dotenv()

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged in as {0}!'.format(self.user))

  async def on_message(self, message):
    print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run(os.getenv('TOKEN', 'Token not found'))
