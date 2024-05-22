import socket

def bit_stuffing(data):
    stuffed_data = ''
    ones = 0

    for bit in data:
        if bit == '1':
            ones += 1
            stuffed_data += bit 
            if ones == 5:
                stuffed_data += '0'
                ones = 0
        else:
            stuffed_data += bit
            ones = 0 
    return stuffed_data

def handle_client(client_socket):
    data = client_socket.recv(1024).decode()
    print(f'Received Data: {data}')

    stuffed_data = bit_stuffing(data)
    print(f'Bit Stuffed Data: {stuffed_data}')

    client_socket.send(stuffed_data.encode())
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port, host = 80, 'localhost' or '127.0.0.1'
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

if __name__ == '__main__':
    main()