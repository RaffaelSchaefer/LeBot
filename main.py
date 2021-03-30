import discord
import os
import random
from replit import db

client = discord.Client()

default_fragen = ["Wie alt bist ?"]

if "responding" not in db.keys():
  db["responding"] = True

def update_fragen(fragen_message):
  if "fragen" in db.keys():
    fragen = db["fragen"]
    fragen.append(fragen_message)
    db["fragen"] = fragen
  else: 
    db["fragen"] = [fragen_message]

def delete_fragen(index):
  fragen = db["fragen"]
  if len(fragen) > index:
    del fragen[index]
    db["fragen"] = fragen

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if db["responding"]:
    options = default_fragen
    if "fragen" in db.keys():
      options = options + db["fragen"]
  
  if msg.startswith("$Neu"):
    fragen_message = msg.split("$Neu ",1)[1]
    update_fragen(fragen_message)
    await message.channel.send("Neue Frage hinzugefügt")
  
  if msg.startswith("$Entfernen"):
    fragen = []
    if "fragen" in db.keys():
      index = int(msg.split("$Entfernen",1)[1])
      delete_fragen(index)
      fragen = db["fragen"]
    await message.channel.send(fragen)
  
  if msg.startswith("$Frage"):
    await message.channel.send(random.choice(options))

client.run(os.getenv('TOKEN'))