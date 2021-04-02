import discord
import os
import random
import asyncio
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

option_del = [
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
    name="index", description="The index of the entry",option_type=4,required=True
  )
]

option_List = [
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
  )
]

##Commands Database

@slash.slash(name="new", description="Adds a new entry to a specific database",options=option_New)
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
      await ctx.send(content="New Most likely is to Question added: "+input)

@slash.slash(name="delete", description="Adds a new entry to a specific database",options=option_del)
async def delete(ctx,mode: str, index: int):
  dbFragen = "Fragen_"+str(ctx.guild.id)
  dbPflicht = "Pflicht_"+str(ctx.guild.id)
  dbMostlikely = "Mostlikely_"+str(ctx.guild.id)
  if mode == "question":
    if dbFragen in db.keys():
      delete_dbEntry(index,dbFragen)
      print('{0.author.name} delete a Question'.format(ctx))
      await ctx.send(content='{0.author.name} delete a Question'.format(ctx))
  if mode == "dare":
    if dbPflicht in db.keys():
      delete_dbEntry(index,dbPflicht)
      print('{0.author.name} delete a Dare'.format(ctx))
      await ctx.send(content='{0.author.name} delete a Dare'.format(ctx))
  if mode == "mostlikely":
    if dbMostlikely in db.keys():
      delete_dbEntry(index,dbMostlikely)
      print('{0.author.name} delete a Most likely is to Question'.format(ctx))
      await ctx.send(content='{0.author.name} delete a Most likely is to Question'.format(ctx))

@slash.slash(name="get", description="Get a specific entry",options=option_del)
async def get(ctx,mode: str, index: int):
  dbFragen = "Fragen_"+str(ctx.guild.id)
  dbPflicht = "Pflicht_"+str(ctx.guild.id)
  dbMostlikely = "Mostlikely_"+str(ctx.guild.id)
  if mode == "question":
    if index <= len(db[dbFragen]):
      await ctx.send(content=get_dbEntry(dbFragen,index))
    else:
      await ctx.send(content="Entry does not exist")
  if mode == "dare":
    if index <= len(db[dbPflicht]):
      await ctx.send(content=get_dbEntry(dbPflicht,index))
    else:
      await ctx.send(content="Entry does not exist")
  if mode == "mostlikely":
    if index <= len(db[dbMostlikely]):
      await ctx.send(content=get_dbEntry(dbMostlikely,index))
    else:
      await ctx.send(content="Entry does not exist")

@slash.slash(name="info", description="Shows the Stats of the bot on your server")
async def info(ctx):
  dbFragen = "Fragen_"+str(ctx.guild.id)
  dbPflicht = "Pflicht_"+str(ctx.guild.id)
  dbMostlikely = "Mostlikely_"+str(ctx.guild.id)
  await ctx.send(content="Amount of Questions: "+str(len(db[dbFragen]))+"\nAmount of Dares: "+str(len(db[dbPflicht]))+"\nAmount of Most likely is to Questions: "+str(len(db[dbMostlikely])))

@slash.slash(name="list", description="Lists all entrys",options=option_List)
async def list(ctx,mode: str):
  dbFragen = "Fragen_"+str(ctx.guild.id)
  dbPflicht = "Pflicht_"+str(ctx.guild.id)
  dbMostlikely = "Mostlikely_"+str(ctx.guild.id)
  if mode == "question":
    for i in range(0,len(db[dbFragen])):
      await asyncio.sleep(2)
      await ctx.send(content=get_dbEntry(dbFragen,i))
  if mode == "dare":
    for i in range(0,len(db[dbPflicht])):
      await asyncio.sleep(2)
      await ctx.send(content=get_dbEntry(dbPflicht,i))
  if mode == "mostlikely":
    for i in range(0,len(db[dbMostlikely])):
      await asyncio.sleep(2)
      await ctx.send(content=get_dbEntry(dbMostlikely,i))

#Commands Gamemodes

@slash.slash(name="truthordare", description="Starts a new round of Truth or Dare",options=option_TruthOrDare)
async def truthordare(ctx,mode: str):
  dbFragen = "Fragen_"+str(ctx.guild.id)
  dbPflicht = "Pflicht_"+str(ctx.guild.id)
  print('{0.author.name} wants to play a round Truth or Dare'.format(ctx))
  if mode == "truth":
    print('{0.author.name} choose truth'.format(ctx))
    await ctx.send(content="Truth: "+random.choice(db[dbFragen]))
  if mode == "dare":
    print('{0.author.name} choose dare'.format(ctx))
    await ctx.send(content="Dare: "+random.choice(db[dbPflicht]))

@slash.slash(name="mostlikelyto", description="Starts a new round of Most likely to")
async def mostlikelyto(ctx):
  dbMostlikely = "Mostlikely_"+str(ctx.guild.id)
  print('{0.author.name} wants to play a round Truth or Drink'.format(ctx))
  await ctx.send(content=random.choice(db[dbMostlikely]))

keep_alive()
client.run(os.getenv('TOKEN'))