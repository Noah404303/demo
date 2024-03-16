import sys
import time 
import json

def benutzer_name_abfragen():
    print("Benutzername: ", end="")
    user = sys.stdin.readline()
    user = user.strip()
    return user 


def nachricht_erstellen(user, text):
    zeit = time.strftime("%H:%M", time.localtime())
    nachricht = {"zeit": zeit, "user": user, "text": text}
    return json.dumps(nachricht) 

def nachricht_lesen(nachricht):
    return json.loads(nachricht)
