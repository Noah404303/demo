
import socket

def main():
    print("server start")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 8888))
    server_socket.listen()

    client_socket, client_address = server_socket.accept()

    while True:
        
        buffer = client_socket.recv(1000)
        nachricht = buffer.decode("utf-8")
        print(nachricht)

main()
