
import socket

def main():
    print("client start")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("192.168.178.63", 8888))
    # client_socket.connect(("127.0.0.1", 8888))
    

    

    while True:
        nachricht = input("nachricht: ")
        client_socket.sendall(nachricht.encode("utf-8"))
        
      

main()
