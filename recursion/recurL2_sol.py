"""
Recursion Madness Level II
Author: Jose Renteria
for CS211 Class Encore

Notice the Node class is initialized and used slightly differently than 
Level 1. Work with what you got.

"""


# Program to count leaf nodes in a Binary Tree
# What are some properties of a leaf node?
# Seen this anywhere before ?

# A binary tree Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# work your way down the tree
# leaf count of a tree = leaf count of left subtree + leaf count of right subtree
def get_leaf_count(node):
    if node is None:
        return 0
    if (node.left is None and node.right is None):
        return 1
    else:
        return get_leaf_count(node.left) + get_leaf_count(node.right)


def test_leaf_count():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(4)
    root.left.right = Node(5)
    print(f'Leaf count of the tree is {get_leaf_count(root)}')


if __name__ == '__main__':
    test_leaf_count()