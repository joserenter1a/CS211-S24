import random 
import time 
def bit_gen() -> str:
    return ''.join(random.choice('01') for _ in range(16))

print(bit_gen())

def nano():
    try:
        while 1:
            print(''.join(random.choice('01') for _ in range(32)))
            time.sleep(1)
    except KeyboardInterrupt:
        print("STOP")
        return None
    
print(nano())