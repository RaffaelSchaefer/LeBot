import discord
import os
import random
import asyncio
from replit import db
from keep_alive import keep_alive
from dbcommands import update_dbEntry,delete_dbEntry,get_dbEntry,tranfer_db,reset_db
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice

client = discord.Client()
slash = SlashCommand(client, sync_commands=True)

eightball = ["It is certain","It is decidedly so","Without a doubt","Yes – definitely","You may rely on it","As I see it, yes","Most likely","Outlook good","Yes","Signs point to yes","Don’t count on it","My reply is no","My sources say no","Outlook not so good","Very doubtful"]

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

option_eb = [
  create_option(
    name="question", description="The Question for the eight ball",option_type=3,required=True
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
    ),
      create_choice(
      name="Topics",
      value="topics"
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
    ),
      create_choice(
      name="Topics",
      value="topics"
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
    ),
      create_choice(
      name="Topics",
      value="topics"
    )
    ]
  )
]

option_migrate = [
  create_option(
    name="serverid", description="Server ID",option_type=3,required=True
  ),create_option(
    name="masterpassword", description="Master Password",option_type=3,required=True
  )
]

option_reset = [
  create_option(
    name="masterpassword", description="Master Password",option_type=3,required=True
  )
]

##Commands Database

@slash.slash(name="new", description="Adds a new entry to a specific database",options=option_New)
async def new(ctx, mode: str, input: str):
  dbFragen = "Fragen_"+str(ctx.guild.id)
  dbPflicht = "Pflicht_"+str(ctx.guild.id)
  dbMostlikely = "Mostlikely_"+str(ctx.guild.id)
  dbTopics = "Topics_"+str(ctx.guild.id)
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
  if mode == "topics":
      update_dbEntry(input,dbTopics)
      print("New Topic added: "+input)
      await ctx.send(content="New Topic added: "+input)

@slash.slash(name="delete", description="Adds a new entry to a specific database",options=option_del)
async def delete(ctx,mode: str, index: int):
  dbFragen = "Fragen_"+str(ctx.guild.id)
  dbPflicht = "Pflicht_"+str(ctx.guild.id)
  dbMostlikely = "Mostlikely_"+str(ctx.guild.id)
  dbTopics = "Topics_"+str(ctx.guild.id)
  if mode == "question":
    if dbFragen in db.keys():
      delete_dbEntry(index,dbFragen)
      print('{0.author.name} deleted a Question'.format(ctx))
      await ctx.send(content='{0.author.name} deleted a Question'.format(ctx))
  if mode == "dare":
    if dbPflicht in db.keys():
      delete_dbEntry(index,dbPflicht)
      print('{0.author.name} deleted a Dare'.format(ctx))
      await ctx.send(content='{0.author.name} deleted a Dare'.format(ctx))
  if mode == "mostlikely":
    if dbMostlikely in db.keys():
      delete_dbEntry(index,dbMostlikely)
      print('{0.author.name} deleted a Most likely is to Question'.format(ctx))
      await ctx.send(content='{0.author.name} deleted a Most likely is to Question'.format(ctx))
  if mode == "topics":
    if dbTopics in db.keys():
      delete_dbEntry(index,dbTopics)
      print('{0.author.name} deleted a Topic'.format(ctx))
      await ctx.send(content='{0.author.name} deleted a deleted a Topic'.format(ctx))

@slash.slash(name="get", description="Get a specific entry",options=option_del)
async def get(ctx,mode: str, index: int):
  dbFragen = "Fragen_"+str(ctx.guild.id)
  dbPflicht = "Pflicht_"+str(ctx.guild.id)
  dbMostlikely = "Mostlikely_"+str(ctx.guild.id)
  dbTopics = "Topics_"+str(ctx.guild.id)
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
  if mode == "topics":
    if index <= len(db[dbTopics]):
      await ctx.send(content=get_dbEntry(dbTopics,index))
    else:
      await ctx.send(content="Entry does not exist")

@slash.slash(name="info", description="Shows the Stats of the bot on your server")
async def info(ctx):
  dbFragen = "Fragen_"+str(ctx.guild.id)
  dbPflicht = "Pflicht_"+str(ctx.guild.id)
  dbMostlikely = "Mostlikely_"+str(ctx.guild.id)
  dbTopics = "Topics_"+str(ctx.guild.id)
  await ctx.send(content="Amount of Questions: "+str(len(db[dbFragen]))+"\nAmount of Dares: "+str(len(db[dbPflicht]))+"\nAmount of Most likely is to Questions: "+str(len(db[dbMostlikely]))+"\nAmount of Topics: "+str(len(db[dbTopics])))

@slash.slash(name="list", description="Lists all entrys",options=option_List)
async def list(ctx,mode: str):
  dbFragen = "Fragen_"+str(ctx.guild.id)
  dbPflicht = "Pflicht_"+str(ctx.guild.id)
  dbMostlikely = "Mostlikely_"+str(ctx.guild.id)
  dbTopics = "Topics_"+str(ctx.guild.id)
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
  if mode == "topics":
    for i in range(0,len(db[dbTopics])):
      await asyncio.sleep(2)
      await ctx.send(content=get_dbEntry(dbTopics,i))

@slash.slash(name="migrate", description="Migrate a db",options=option_migrate)
async def migrate(ctx, serverid: str, masterpassword: str):
  print('{0.author.name} wants to migrate a db'.format(ctx))
  tranfer_db(str(ctx.guild.id), serverid, masterpassword)
  await ctx.send(content="Transfer complete")

@slash.slash(name="reset", description="Resets all dbs",options=option_reset)
async def reset(ctx, masterpassword: str):
  print('{0.author.name} wants to reset the db'.format(ctx))
  reset_db(str(ctx.guild.id), masterpassword)
  await ctx.send(content="Reset complete")

#Commands Gamemodes

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

@slash.slash(name="MostLikelyTo", description="Starts a new round of Most likely to",options = [])
async def MostLikelyTo(ctx):
  dbMostlikely = "Mostlikely_"+str(ctx.guild.id)
  print('{0.author.name} wants to play a who is the most likely to'.format(ctx))
  await ctx.send(content=random.choice(db[dbMostlikely]))

@slash.slash(name="Topic", description="Starts a new round of Most likely to",options = [])
async def Topic(ctx):
  dbTopics = "Topics_"+str(ctx.guild.id)
  print('{0.author.name} wants to have a topic'.format(ctx))
  await ctx.send(content=random.choice(db[dbTopics]))

@slash.slash(name="eb", description="Asks the magic Eight ball",options = option_eb)
async def eb(ctx, question: str):
  print('{0.author.name} asked the eight ball'.format(ctx))
  await ctx.send("The Question for the eight ball was: "+question+"\nHis Answer is: "+random.choice(eightball))

keep_alive()
client.run(os.getenv('TOKEN'))