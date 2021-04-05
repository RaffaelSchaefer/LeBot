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
  #Logic
  if currentDbFragen in db.keys():
    db[currentDbFragen] = db[currentDbFragen]+db[targetDbFragen]
  else: 
    db[currentDbFragen] = db[targetDbFragen]
  if currentDbPflicht in db.keys():
    db[currentDbPflicht] = db[currentDbPflicht]+db[targetDbPflicht]
  else: 
    db[currentDbPflicht] = db[targetDbPflicht]
  if currentDbMostlikely in db.keys():
    db[currentDbMostlikely] = db[currentDbMostlikely]+db[targetDbMostlikely]
  else: 
    db[currentDbMostlikely] = db[targetDbMostlikely]
  if currentDbTopics in db.keys():
    db[currentDbTopics] = db[currentDbTopics]+db[targetDbTopics]
  else: 
    db[currentDbTopics] = db[targetDbTopics]