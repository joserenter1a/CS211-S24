import random 
import time 
import keyboard

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

def rando():
    while  True:
        try:
            if keyboard.is_pressed('b'):
                bit_gen()
                print(bit_gen())
        except  KeyboardInterrupt:
            break
rando()