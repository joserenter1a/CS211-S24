"""
Initialize a Character object class, implement functionality of all char methods

The char data type was designed to hold a single character .
A character can be a single letter, number, symbol, or whitespace

"""


class Char(str):

    def __new__(cls, char):
        """
        Creates a new instance of a class and returns it. Allows for
        customization of object creation
        """
        if len(char) != 1:
            raise Exception(TypeError("Expected single character"))
        else:
              # ensure correct usage
            return super().__new__(cls, char)
        # inherits from built in string class
        # super creates a temporary str object, which allows you to call methods
        # on the 'super' class or parent class, str

    def __init__(self, c):
        """
        Constructor function
        """
        self.c = c

    def __str__(self):
        """
        Casts type to a string. Also used for printing
        """
        return f"{self.c}"

    def __eq__(self, other):
        """
        Checks equality
        """
        # checks that other, is of type Char
        if isinstance(other, Char):
            return self.c == other.c
        elif isinstance(other, str):
            return self.c == other
        else:
            return False
    
