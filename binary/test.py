import random 
import time 
def bit_gen() -> str:
    return ''.join(random.choice('01') for _ in range(32))

def nano():
    try:
        while 1:
            inp = bit_gen()
            print(inp)
    except KeyboardInterrupt:
        print("STOP")
        return None

def read_file_line_by_line(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            i = (line.strip())  # Print the line without the newline character
            time.sleep(1)  # Wait for 1 second before reading the next line
    return i

if __name__ == "__main__":
    file_path = 'packets.txt'  # Replace with your file path
    read_file_line_by_line(file_path)
