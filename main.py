import discord
import os
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

def update_db(fragen_message,dbKey):
  if dbKey in db.keys():
    fragen = db[dbKey]
    fragen.append(fragen_message)
    db[dbKey] = fragen
  else: 
    db[dbKey] = [fragen_message]

def delete_db(index,dbKey):
  fragen = db[dbKey]
  if len(fragen) > index:
    del fragen[index]
    db[dbKey] = fragen

def create_list(dbKey,index):
  out = str(index)+": "+str(db[dbKey][index])+"\n"
  print(out)
  return out

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  dbFragen = "Fragen_"+str(message.guild.id)
  dbPflicht = "Pflicht_"+str(message.guild.id)
  
  if msg.startswith("$newQ"):
    fragen_message = msg.split("$newQ ",1)[1]
    update_db(fragen_message,dbFragen)
    print("Neue Frage hinzugefügt: "+ fragen_message)
    await message.channel.send("Neue Frage hinzugefügt: "+ fragen_message)

  if msg.startswith("$newD"):
    pflicht_message = msg.split("$newD ",1)[1]
    update_db(pflicht_message,dbPflicht)
    print("Neue Pflicht hinzugefügt: "+ pflicht_message)
    await message.channel.send("Neue Pflicht hinzugefügt: "+ pflicht_message)
  
  if msg.startswith("$delQ"):
    fragen = []
    if dbFragen in db.keys():
      index = int(msg.split("$delQ",1)[1])
      delete_db(index,dbFragen)
      fragen = db[dbFragen]
    print('{0.author.name} loeschte eine Frage'.format(message))
    for i in range(0, len(db[dbFragen])):
      await message.channel.send(create_list(dbFragen,i))
    print("Listen Ausgabe fertig")

  if msg.startswith("$delD"):
    pflicht = []
    if dbPflicht in db.keys():
      index = int(msg.split("$delQ",1)[1])
      delete_db(index,dbPflicht)
      pflicht = db[dbPflicht]
    print('{0.author.name} loeschte eine Frage'.format(message))
    for i in range(0, len(db[dbPflicht])):
      await message.channel.send(create_list(dbPflicht,i))
    print("Listen Ausgabe fertig")

  if msg.startswith("$listQ"):
    print('{0.author.name} moechte alle Fragen wissen'.format(message))
    for i in range(0, len(db[dbFragen])):
      await message.channel.send(create_list(dbFragen,i))
    print("Listen Ausgabe fertig")
  
  if msg.startswith("$listD"):
    print('{0.author.name} moechte alle Fragen wissen'.format(message))
    for i in range(0, len(db[dbPflicht])):
      await message.channel.send(create_list(dbPflicht,i))
    print("Listen Ausgabe fertig")

  if msg.startswith("$question"):
    print('{0.author.name} moechte eine Frage haben'.format(message))
    await message.channel.send(random.choice(db[dbFragen]))
  
  if msg.startswith("$TruthOrDrink"):
    print('{0.author.name} moechte eine Runde Truth or Drink spieln'.format(message))
    await message.channel.send(random.choice(db[dbFragen]))

keep_alive()
client.run(os.getenv('TOKEN'))