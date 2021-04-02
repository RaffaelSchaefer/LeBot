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

def update_dbEntry(fragen_message,dbKey):
  if dbKey in db.keys():
    fragen = db[dbKey]
    fragen.append(fragen_message)
    db[dbKey] = fragen
  else: 
    db[dbKey] = [fragen_message]

def delete_dbEntry(index,dbKey):
  fragen = db[dbKey]
  if len(fragen) > index:
    del fragen[index]
    db[dbKey] = fragen

def get_dbEntry(dbKey,index):
  out = str(index)+": "+str(db[dbKey][index])+"\n"
  print(out)
  return out

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

option_New = [
  create_option(
    name="mode",
    description="choose a mode",
    option_type=3,
    required=True,
    choices=[
      create_choice(
      name="Question",
      value="question"
    ),
      create_choice(
      name="Dare",
      value="dare"
    ),
      create_choice(
      name="Mostlikely",
      value="mostlikely"
    )
    ]
  ),
  create_option(
    name="input", description="The value of the entry",option_type=3,required=True
  )
]

##Commands Database

@slash.slash(name="new", description="adds a new entry to a specific database",options=option_New)
async def new(ctx, mode: str, input: str):
  dbFragen = "Fragen_"+str(ctx.guild.id)
  dbPflicht = "Pflicht_"+str(ctx.guild.id)
  dbMostlikely = "Mostlikely_"+str(ctx.guild.id)
  if mode == "question":
      update_dbEntry(input,dbFragen)
      print("New Question added: "+input)
      await ctx.send(content="New Question added: "+input)
  if mode == "dare":
      update_dbEntry(input,dbPflicht)
      print("New Dare added: "+input)
      await ctx.send(content="New Dare added: "+input)
  if mode == "mostlikely":
      update_dbEntry(input,dbMostlikely)
      print("New Most likely is to Question added: "+input)
      await ctx.send(content="New Most likely is to added: "+input)

#Commands Gamemodes
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

keep_alive()
client.run(os.getenv('TOKEN'))