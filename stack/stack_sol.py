from stack import Stack # import our Stack class

# it should work the same with this import
# from collections import deque as Stack

def reverse_string(s: str):
    """
    Reverses a string s

    >>> reverse_string("reverse")
    >>> 'esrever'
    """
    # Initialize empty stack
    st = Stack()

    for char in s:  # every char in our string
        st.append(char)  # push the char onto the stack
    reversed_string = ""  # create an empty reverse string

    while len(st) != 0:  
        reversed_string += st.pop()  # pop returns whatever is on the top of the stack,
        # accumulation to an empty string ^

    return reversed_string  # return new string

print(reverse_string('stack'))