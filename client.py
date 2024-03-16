
import socket
from chat import * 
from caesar import *






def main():
    print("client start")
    user = benutzer_name_abfragen()
    schlüssel = caeser_setup()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client_socket.connect(("192.168.178.63", 8888))
    client_socket.connect(("127.0.0.1", 8888))
    

    

    while True:
        text = input("nachricht: ")
        nachricht = nachricht_erstellen(user,text) 
        geheimtext = verschlüsseln(nachricht, schlüssel)
        client_socket.sendall(geheimtext.encode("utf-8"))
        
      

main()
