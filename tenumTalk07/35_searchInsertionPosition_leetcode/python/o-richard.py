# https://leetcode.com/problems/search-insert-position/
"""
Assumptions:
* Ensure there is at least one element in the array, otherwise the target can be inserted at the first index.
* The array is sorted in an ASCENDING order.
* The array could have duplicates.

Pseuodcode:
- Keep track of the following:
    - The correct index of insertion (variable index)
    - The starting index of searching (varaible i. Initialized to the first index of the array - 0)
    - The last index of searching (varaible j. Initialized to the last index of the array)
- Iterate
    Base Case:
        - j should always be greater than i.
            - Incase the element at index i is greater than or equal to the target:
                - Assign index to i
            - Otherwise: Assign index to the next index after i (i + 1)
            Stop the iteration
    - Find the middle index - The largest interger that is less than or equal to the value of midpoint ((i + j) / 2).
    Incase the value at the middle index is greater than the target:
        - Adjust the value of j by (middle index - 1)
    Incase the value at the middle index is lesser than the target:
        - Adjust the value of i by (middle index + 1)
    Incase the value at the middle index is equal to the target:
        - Assign the variable index to the middle index.
        - Stop the iteration.
Return the index
"""


import math


def searchInsert(nums: list[int], target: int) -> int:
    arrlen = len(nums)
    if (arrlen == 0):
        return 0

    index, mid, i, j = 0, 0, 0, arrlen - 1
    while True:
        if j <= i:
            if (nums[i] >= target):
                index = i
            elif (nums[i] < target):
                index = i + 1
            break
        mid = math.floor((i + j) / 2)
        if (nums[mid] > target):
            j = mid - 1
        elif (nums[mid] < target):
            i = mid + 1
        else:
            index = mid
            break
    return index
