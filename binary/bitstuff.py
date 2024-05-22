"""
Bit Stuffing and Un-Stuffing methods

Author: Jose Renteria

"""
import random

class BitStuff():

    def bit_gen() -> str:
        """
        Generates a random 32-bit binary string.
        """
        # Why are these the min and max values for a string to be 32 bits?
        # What are they?
        return str(bin(random.randint(32768,65535)))[2:]
    

    def stuff(data):
        """
        As data is being transmitted, the sender continuously monitors the data stream.

        Whenever it detects a sequence of five consecutive 1 bits in the data, it 
        automatically inserts a 0 bit after these six 1s.

        This insertion prevents the accidental formation of a flag pattern (e.g., 01111110 or 0x7E) 
        in the data payload.
        """
        # initialize empty accumulator string to 'stuff' it
        stuffed_data = ''
        # keep track of number of consecutive ones
        ones = 0

        # iterate through the bit string
        for bit in data:
            # if the bit is a 1
            if bit == '1':
                # update your ones counter
                ones += 1
                # accumulate the bit to our stuffed string
                stuffed_data += bit 
                # if our count of ones reaches 6
                if ones == 6:
                    # we stuff a 0 to delimit the end of a frame, start of the next one
                    stuffed_data += '0'
                    # reset the ones count
                    ones = 0
            # else the bit is a 0
            else:
                # keep accumulating the bit
                # ones count is unaffected
                stuffed_data += bit
                ones = 0 
        # return your stuffed string
        return stuffed_data

    def unstuff(stuffed_data):
        """
        The receiver monitors the incoming data stream for sequences of five consecutive 1 bits.

        Upon detecting five 1s followed by a 0, the receiver understands that the 0 was inserted 
        for bit stuffing purposes and removes it.
        
        This restoration process ensures that the original data is correctly reconstructed without the stuffed bits
        """
        # initialize empty accumulator string to 'unstuff' it
        # keep track of number of consecutive ones

        # initialize index variable
        unstuffed_data = ''
        ones = 0

        i = 0
        # while index less than the length of your stuffed bit string
        while i < len(stuffed_data):
            # bit is the current index
            bit = stuffed_data[i]
            # if the bit is on
            if bit == '1':
                # increment your ones count
                # accumulate the bit to the unstuffed string
                ones += 1
                unstuffed_data += bit 
                # if you reach a count of 6 consecutive ones
                    # skip to the next index
                    # and reset your count
                if ones == 6:
                    i += 1
                    ones = 0
            # else
            else:
                # the bit is a 0 so we just accumulate it to the string and the ones count is 0
                unstuffed_data += bit 
                ones = 0 
            # increment the index
            i += 1
        # return your unstuffed strings
        return unstuffed_data


