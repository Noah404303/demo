
import socket

from caesar import *

import threading

def client_verbindung(client_socket, schlüssel):
    

    # entlos schlife zum entfanegn von nachrichten 
    while True:
        # empfange nachricht über netzwerk von client
        # bereite auf verbindungs fehler vor mit try except
        try: 
            buffer = client_socket.recv(1000)
        except socket.error as fehler:
            print("verbindung getrennt: %s" % fehler)
            break

        # wandle netzwerk nachricht in lesbaren text um 
        nachricht = buffer.decode("utf-8")
        klartext = entschlüsseln(nachricht, schlüssel)
        print(klartext)

def main():
    print("server start")
    schlüssel = caeser_setup()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 8888))
    server_socket.listen()

    while True:
        # warte auf eingehende verbindung von client 
        client_socket, client_address = server_socket.accept()
        print(" neue verbindung: %s:%s" % ( client_address[0],client_address[1]))

        client_thread = threading.Thread(
            target=client_verbindung,
            args=(client_socket, schlüssel,)
            )
        client_thread.start()
    
main()
