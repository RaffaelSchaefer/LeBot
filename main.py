import discord
import os
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

def update_fragen(fragen_message,dbKey):
  if dbKey in db.keys():
    fragen = db[dbKey]
    fragen.append(fragen_message)
    db[dbKey] = fragen
  else: 
    db[dbKey] = [fragen_message]

def delete_fragen(index,dbKey):
  fragen = db[dbKey]
  if len(fragen) > index:
    del fragen[index]
    db[dbKey] = fragen

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  dbFragen = "Fragen_"+str(message.guild.id)
  
  if msg.startswith("$newQ"):
    fragen_message = msg.split("$NeuFrage ",1)[1]
    update_fragen(fragen_message,dbFragen)
    print("Neue Frage hinzugefügt: "+ fragen_message)
    await message.channel.send("Neue Frage hinzugefügt: "+ fragen_message)
  
  if msg.startswith("$delQ"):
    fragen = []
    if dbFragen in db.keys():
      index = int(msg.split("$EntFrage",1)[1])
      delete_fragen(index,dbFragen)
      fragen = db[dbFragen]
    print('{0.author.name} loeschte eine Frage'.format(message))
    await message.channel.send(fragen)

  if msg.startswith("$listQ"):
    fragen = db[dbFragen]
    print('{0.author.name} moechte alle Fragen wissen'.format(message))
    await message.channel.send(fragen)

  if msg.startswith("$question"):
    print('{0.author.name} moechte eine Frage haben'.format(message))
    await message.channel.send(random.choice(db[dbFragen]))
  
  if msg.startswith("$TruthOrDrink"):
    print('{0.author.name} moechte eine Runde Truth or Drink spieln'.format(message))
    await message.channel.send(random.choice(db[dbFragen]))

keep_alive()
client.run(os.getenv('TOKEN'))