import random


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
