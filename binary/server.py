"""
Server Side TCP Socket that stuffs bit strings and awaits requests from clients.
Utilizes Python Socket API.

Author: Jose Renteria
For CS211 Class Encore

"""
import socket
from bitstuff import BitStuff

# function to receive data from the client, stuff it, and send it back via TCP socket
def handle_client(client_socket):
    data = client_socket.recv(1024).decode()
    print(f'Received Data: {data}')

    stuffed_data = BitStuff.stuff(data)
    print(f'Bit Stuffed Data: {stuffed_data}')

    client_socket.send(stuffed_data.encode())

def main():
    # establish connection
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port, host = 9000, '127.0.0.1'
    server.bind((host, port))
    server.listen(1)
    # Listen for requests
    print(f"Server listening on http://{host}:{port}")
    try: 
        while 1:
            # Accept connection from client socket
            client_socket, addr = server.accept()
            print(f'Accepted connection from {addr}')
            handle_client(client_socket)
    # Keep server running until CTRL + C is pressed
    except KeyboardInterrupt:
        print("Server stopped")
        server.close()

if __name__ == '__main__':
    main()