"""
Client-Side TCP Socket that sends bit string requests to server.
Utilizes Python Socket API.

Author: Jose Renteria
For CS211 Class Encore

"""
import socket
import time
from bitstuff import BitStuff


def main():
    while 1:
        # Establish TCP socket connection
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port, host = 9000, '127.0.0.1'
        client.connect((host, port))

        # generate a new bit string to stuff, and wait 1 second
        original_data = BitStuff.bit_gen()
        time.sleep(3)

        # print the original data
        print(f"Original Data: {original_data}")
        
        # send the data as a byte encoded object
        client.send(original_data.encode())
        # receive and decode the bit stuffed data
        stuffed_data = client.recv(1024).decode()
        # print the bit stuffed data
        print(f"Received Bit-Stuffed Data: {stuffed_data}")
        # print the unstuffed data
        unstuffed_data = BitStuff.unstuff(stuffed_data)
        print(f"Unstuffed Data: {unstuffed_data}")



if __name__ == "__main__":
    main()