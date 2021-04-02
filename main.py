import discord
import os
import random
from replit import db
from keep_alive import keep_alive
from discord_slash import SlashCommand

client = discord.Client()
slash = SlashCommand(client, sync_commands=True)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@slash.slash(name="info",
             description="Shows all the stats from the bot")
async def info(ctx):
  await ctx.send(content="Hello World!")

#keep_alive()
client.run(os.getenv('TOKEN'))