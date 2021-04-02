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

keep_alive()
client.run(os.getenv('TOKEN'))