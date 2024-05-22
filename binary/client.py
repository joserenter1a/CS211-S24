import socket
import random
import time
from bitstuff import *


def bit_gen() -> str:
    return ''.join(random.choice('01') for _ in range(16))


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port, host = 9000, 'localhost' or '127.0.0.1'

    client.connect((host, port))
    try:
        while 1:
            original_data = input()
            time.sleep(1)
            print(f"Original Data: {original_data}")

            client.send(original_data.encode())
            stuffed_data = client.recv(1024).decode()
            print(f"Received Bit-Stuffed Data: {stuffed_data}")

            unstuffed_data = bit_unstuffing(stuffed_data)
            print(f"Unstuffed Data: {unstuffed_data}")


            time.sleep(3)
            
    except KeyboardInterrupt:
        print('Stopping bit stream')
        client.close()

if __name__ == "__main__":
    main()