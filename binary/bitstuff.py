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
        # What are the min and max values for an int to be 32 bits long?
        # TODO    
        pass

    def stuff(data):
        """
        As data is being transmitted, the sender continuously monitors the data stream.

        Whenever it detects a sequence of five consecutive 1 bits in the data, it 
        automatically inserts a 0 bit after these six 1s.

        This insertion prevents the accidental formation of a flag pattern (e.g., 01111110 or 0x7E) 
        in the data payload.
        """
        # initialize empty accumulator string to 'stuff' it
        # keep track of number of consecutive ones
        # iterate through the bit string
            # if the bit is a 1
                # update your ones counter
                # accumulate the bit to our stuffed string
                # if our count of ones reaches 6
                    # we stuff a 0 to delimit the end of a frame, start of the next one
                    # reset the ones count
            # else the bit is a 0
                # keep accumulating the bit
                # ones count is unaffected
        # return your stuffed string
        # TODO
        pass

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
        # while index less than the length of your stuffed bit string
            # bit is the current index
            # if the bit is on
                # increment your ones count
                # accumulate the bit to the unstuffed string
                # if you reach a count of 6 consecutive ones
                    # skip to the next index
                    # and reset your count
            # else
                # the bit is a 0 so we just accumulate it to the string and the ones count is 0
            # increment the index
        # return your unstuffed strings
        # TODO
        pass