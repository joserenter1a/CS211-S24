"""
Recursion Madness Level 1: Largest node in a BST
Author: Jose Renteria
for CS211 Class Encore

• Write a recursive method(s) to find the
largest number stored in a BST.
• Add its use in the main function.

"""
class Node():
    def __init__(self, value: int):
        self.value = value 

    def __str__(self):
        raise NotImplementedError("Not Implemented")
    
class Leaf(Node):
    def __init__(self, value: int):
        super().__init__(value)

    def __str__(self):
        return f'{self.value}'
    
class Internal(Node):
    def __init__(self, value: int, left: Node, right: Node):
        super().__init__(value)
        self.left = left
        self.right = right 
    def __str__(self):
        return f'Node({self.value}, {self.left.__str__()},  {self.right.__str__()})'

def largest_node(root: Internal):
    if root.right.value is None:
        return root.value
    return largest_node(root.right)


def main():
    l1 = Leaf(3)
    l2 = Leaf(6)
    n = Leaf(None)
    i = Internal(7, l2, n)
    root = Internal(5, l1, i)
    print(root)
    print(largest_node(root))

if __name__ == '__main__':
    main()