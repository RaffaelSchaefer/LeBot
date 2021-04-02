import discord
import os
import random
from replit import db
from keep_alive import keep_alive
from discord_slash import SlashCommand, SlashCommandOptionType, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice

client = discord.Client()
slash = SlashCommand(client, sync_commands=True)

##Functions

##Startup

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

##Options

option_TruthOrDare = [
  create_option(
    name="mode",
    description="choose an entry based on mode selection",
    option_type=3,
    required=True,
    choices=[
      create_choice(
      name="Truth",
      value="truth"
    ),
      create_choice(
      name="Dare",
      value="dare"
    )
    ]
  )
]

##Commands

@slash.slash(name="TruthOrDrink", description="Starts a new round of Truth or Drink")
async def TruthOrDrink(ctx):
  dbFragen = "Fragen_"+str(ctx.guild.id)
  print('{0.author.name} wants to play a round Truth or Drink'.format(ctx))
  await ctx.send(content=random.choice(db[dbFragen]))

@slash.slash(name="TruthOrDare", description="Starts a new round of Truth or Dare",options=option_TruthOrDare)
async def TruthOrDare(ctx,mode: str):
  dbFragen = "Fragen_"+str(ctx.guild.id)
  dbPflicht = "Pflicht_"+str(ctx.guild.id)
  print('{0.author.name} wants to play a round Truth or Dare'.format(ctx))
  if mode == "truth":
    print('{0.author.name} choose truth'.format(ctx))
    await ctx.send(content="Truth: "+random.choice(db[dbFragen]))
  if mode == "dare":
    print('{0.author.name} choose dare'.format(ctx))
    await ctx.send(content="Dare: "+random.choice(db[dbPflicht]))

#keep_alive()
client.run(os.getenv('TOKEN'))