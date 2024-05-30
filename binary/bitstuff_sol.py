"""
Bit Stuffing and Un-Stuffing methods

Author: Jose Renteria

"""
import secrets

class BitStuff():

    def bit_gen() -> str:
        """
        Generates a random 32-bit binary string.
        """
        return str(bin(secrets.SystemRandom().randint(2147483648,4294967295)))[2:]
    

    def stuff(data):
        """
        Stuffs
        
        """
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

    def unstuff(stuffed_data):
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


