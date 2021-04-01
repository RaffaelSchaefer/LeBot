import discord
import os
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

helptext = "All commands:\n$newQ/D -> A new question/dare is added to the question/dare database\n$delQ/D -> The question/dare at the index is deleted from the database\n$listQ/D -> Lists all the question/dare in the database\n$getQ/D -> Shows the question/dare a the index point\n$question -> Selects a random question from the database\n$dare -> Selects a random dare from the database\n$TruthOrDrink -> Outputs a truth or drink question\n$TruthOrDare -> Starts a new round of Truth or Dare (incomplete)\n$help -> Shows all the commands\n$info -> Shows all the stats\n\nD = Dare\nQ = Question"

def update_db(fragen_message,dbKey):
  if dbKey in db.keys():
    fragen = db[dbKey]
    fragen.append(fragen_message)
    db[dbKey] = fragen
  else: 
    db[dbKey] = [fragen_message]

def create_info(dbKey1,dbKey2):
  out = "Anzahl der Fragen: "+str(len(db[dbKey1]))+"\nAnzahl der Pflichten: "+str(len(db[dbKey2]))
  return out

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
    if dbFragen in db.keys():
      index = int(msg.split("$delQ",1)[1])
      delete_db(index,dbFragen)
    print('{0.author.name} loeschte eine Frage'.format(message))
    for i in range(0, len(db[dbFragen])):
      await message.channel.send(create_list(dbFragen,i))
    print("Listen Ausgabe fertig")

  if msg.startswith("$delD"):
    if dbPflicht in db.keys():
      index = int(msg.split("$delQ",1)[1])
      delete_db(index,dbPflicht)
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

  if msg.startswith("$getQ"):
    index = int(msg.split("getQ",1)[1])
    print("Frage ")
    await message.channel.send("Frage "+create_list(dbFragen,index))
  
  if msg.startswith("$getD"):
    index = int(msg.split("getD",1)[1])
    print("Pflicht ")
    await message.channel.send("Pflicht "+create_list(dbPflicht,index))

  if msg.startswith("$question"):
    print('{0.author.name} moechte eine Frage haben'.format(message))
    await message.channel.send(random.choice(db[dbFragen]))
  
  if msg.startswith("$dare"): 
    print('{0.author.name} moechte eine Pflicht haben'.format(message))
    await message.channel.send(random.choice(db[dbPflicht]))
  
  if msg.startswith("$TruthOrDrink"):
    print('{0.author.name} moechte eine Runde Truth or Drink spieln'.format(message))
    await message.channel.send(random.choice(db[dbFragen]))
  
  if msg.startswith("$TruthOrDare"):
    print('{0.author.name} moechte eine Runde Truth or Dare spieln'.format(message))
    await message.channel.send("Start a new round Truth or Dare")
  
  if msg.startswith("$help"):
    print(helptext)
    await message.channel.send(helptext)
  
  if msg.startswith("$info"):
    print(create_info(dbFragen,dbPflicht))
    await message.channel.send(create_info(dbFragen,dbPflicht))

keep_alive()
client.run(os.getenv('TOKEN'))