import socket
import random
import time
from bitstuff import *

# Generates a random bit string
def bit_gen() -> str:
    return str(bin(random.randint(2147483648,4294967295)))[2:]


def main():
    while 1:
        # Establish socket connection
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port, host = 9000, '127.0.0.1'
        client.connect((host, port))

        # generate a new bit string to stuff, and wait 1 second
        original_data = bit_gen()
        time.sleep(1)

        # print
        print(f"Original Data: {original_data}")

        client.send(original_data.encode())
        stuffed_data = client.recv(1024).decode()
        print(f"Received Bit-Stuffed Data: {stuffed_data}")

        unstuffed_data = bit_unstuffing(stuffed_data)
        print(f"Unstuffed Data: {unstuffed_data}")



if __name__ == "__main__":
    main()