import socket
from bitstuff import *


def handle_client(client_socket):
    data = client_socket.recv(1024).decode()
    print(f'Received Data: {data}')

    stuffed_data = bit_stuffing(data)
    print(f'Bit Stuffed Data: {stuffed_data}')

    client_socket.send(stuffed_data.encode())

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port, host = 9000, '127.0.0.1'
    server.bind((host, port))
    server.listen(1)
    print(f"Server listening on http://{host}:{port}")
    try: 
        while 1:
            client_socket, addr = server.accept()
            print(f'Accepted connection from {addr}')
            handle_client(client_socket)
    except KeyboardInterrupt:
        print("Server stopped")
        server.close()

if __name__ == '__main__':
    main()