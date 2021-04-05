from replit import db

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

def tranfer_db(currentServerID,targetServerID):
  #Current Server Keys
  currentDbFragen = "Fragen_"+str(currentServerID)
  currentDbPflicht = "Pflicht_"+str(currentServerID)
  currentDbMostlikely = "Mostlikely_"+str(currentServerID)
  currentDbTopics = "Topics_"+str(currentServerID)
  #Target Server Keys
  targetDbFragen = "Fragen_"+str(targetServerID)
  targetDbPflicht = "Pflicht_"+str(targetServerID)
  targetDbMostlikely = "Mostlikely_"+str(targetServerID)
  targetDbTopics = "Topics_"+str(targetServerID)
  #Fragen
  if currentDbFragen in db.keys():
    for i in range(0,len(db[targetDbFragen])):
      db[currentDbFragen].append(db[targetDbFragen][i])
  else: 
    db[currentDbFragen] = db[targetDbFragen]
  #Pflicht
  if currentDbPflicht in db.keys():
    for i in range(0,len(db[targetDbPflicht])):
      db[currentDbPflicht].append(db[targetDbPflicht][i])
  else: 
    db[currentDbPflicht] = db[targetDbPflicht]
  #Mlt
  if currentDbMostlikely in db.keys():
    for i in range(0,len(db[targetDbMostlikely])):
      db[currentDbMostlikely].append(db[targetDbMostlikely][i])
  else: 
    db[currentDbMostlikely] = db[targetDbMostlikely]
  #Topics
  if currentDbTopics in db.keys():
    for i in range(0,len(db[targetDbTopics])):
      db[currentDbTopics].append(db[targetDbTopics][i])
  else: 
    db[currentDbTopics] = db[targetDbTopics]

def reset_db(serverid,password):
  if db["PW_"+serverid] == password:
    del db["Fragen_"+str(serverid)]
    del db["Pflicht_"+str(serverid)]
    del db["Mostlikely_"+str(serverid)]
    del db["Topics_"+str(serverid)]
    print("Reset done")
  else:
    print("Wrong password")