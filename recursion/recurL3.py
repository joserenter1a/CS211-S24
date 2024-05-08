"""
Recursion Madness Level III: Binary Search (Recursive solution)
Author: Jose Renteria
for CS211 Class Encore

Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

"""
from typing import List 

def search( nums: List[int], target: int) -> int:
    def binary_search(nums, target, l, r):
        # if left > right
            # list is not sorted, this cannot be true
        # calculate the mid point
        # if we found our target, we return it
        # else if the mid point is less than the target
            # we know it must be on the right, so we 
            # recursively search the right half of the list
            # notice how the new left becomes the element after the mid point
            # and the right half stays the same as it's the remaining elements
            # we just cut our list in half.
            # same goes for the other case.
            # Our left stays the same as we will be searching
            # the left half of the list, and the mid point moves down one
            # since we don't need to check that point again
    # Now we recursively call the binary search function
    # on our list with our initial left and right pointers being
    # 0 index and the last inedx or N - 1th index

        pass
    pass