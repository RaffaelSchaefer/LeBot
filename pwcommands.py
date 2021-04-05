import os
from replit import db

def create_pw(serverid,password):
  if not db["PW_"+serverid]:
    db["PW_"+serverid] = password
  else:
    print("Password allready made please use change_pw instead")

def change_pw(serverid, oldPassword, newPassword):
  if db["PW_"+serverid] == oldPassword:
    db["PW_"+serverid] = newPassword
    print("Password change made")
  else: 
    print("Wrong password")

def reset_pw(serverid, masterPassword, newPassword):
  if masterPassword == os.getenv('MASTERPASSWORD'):
    db["PW_"+serverid] = newPassword
  else: 
    print("Wrong master password")