import socket
import random
import time

def bit_unstuffing(stuffed_data):
    unstuffed_data = ''
    ones = 0

    i = 0

    while i < len(stuffed_data):
        bit = stuffed_data[i]
        if bit == '1':
            ones += 1
            unstuffed_data += bit 
            if ones == 5:
                i += 1
                ones = 0
        else:
            unstuffed_data += bit 
            ones = 0 
        i += 1
    return unstuffed_data

def bit_gen() -> str:
    return ''.join(random.choice('01') for _ in range(16))


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port, host = 80, 'localhost' or '127.0.0.1'

    client.connect((host, port))
    try:
        while 1:
            original_data = bit_gen()
            
            print(f"Original Data: {original_data}")

            client.send(original_data.encode())
            stuffed_data = client.recv(1024).decode()
            print(f"Received Bit-Stuffed Data: {stuffed_data}")

            unstuffed_data = bit_unstuffing(stuffed_data)
            print(f"Unstuffed Data: {unstuffed_data}")


            time.sleep(3)
            
    except KeyboardInterrupt:
        print('Stopping bit stream')
    finally:
        client.close()

if __name__ == "__main__":
    main()