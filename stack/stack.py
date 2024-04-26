"""
Simple implementation of a stack class using a deque.

Author: Jose Renteria

For CS211 Class Encore

Run-time complexity of stack operations
For all the standard stack operations (push, pop, is_empty, size), 
the worst-case run-time complexity can be O(1).

More information about stacks here
https://www.geeksforgeeks.org/time-and-space-complexity-analysis-of-stack-operations/

documentation on deques
https://docs.python.org/3/library/collections.html#collections.deque

"""


from collections import deque

class Stack(deque):
    def __init__(self):
        """
        Constructor. 

        You can initiliaze a stack as such
        >>> st = Stack()
        """
        self.stack = deque()

    def __str__(self):
        return f"{list(self.stack)}"

    def __repr__(self):
        return f"Stack({list(self.stack)})"
    
    def is_empty(self):
        """
        Returns a boolean to check if the stack is empty.

        >>> st = Stack([])
        >>> st.is_empty()
        >>> True
        """
        return len(self.stack) == 0

    def append(self, item):
        """
        Pushes element item onto the stack.

        >>> st.append('A')7
        """
        self.stack.append(item)

    def __len__(self):
        return len(self.stack)

    def pop(self):
        """
        Pops the element on top of the stack and returns it. Raises an IndexError if the
        Stack is empty

        >>> st = Stack(['A'])
        >>> st.pop()
        >>> 'A'
        >>> st = Stack([])
        """
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self.stack.pop()

    def peek(self):
        """
        Returns the element on the top of the stack without removing it from the stack
        >>> st = Stack(['A'])
        >>> st.peek()
        >>> 'A'
        st = Stack(['A'])
        """
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self.stack[-1]


 