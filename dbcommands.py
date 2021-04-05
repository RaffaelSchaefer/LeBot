from replit import db

##Add something to the db
def update_dbEntry(fragen_message,dbKey):
  if dbKey in db.keys():
    fragen = db[dbKey]
    fragen.append(fragen_message)
    db[dbKey] = fragen
  else: 
    db[dbKey] = [fragen_message]

##Delete something to the db
def delete_dbEntry(index,dbKey):
  fragen = db[dbKey]
  if len(fragen) > index:
    del fragen[index]
    db[dbKey] = fragen

##Get a db entry
def get_dbEntry(dbKey,index):
  out = str(index)+": "+str(db[dbKey][index])+"\n"
  print(out)
  return out