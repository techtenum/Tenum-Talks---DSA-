# https://leetcode.com/problems/remove-element/
"""
Assumptions:
* Ensure the array has at least one element.

Pseudocode:
- Keep track of two pointers (Variable i and j).
    - Their initial state is when (i) is at the start of the array while j is at the end.
- Iterate from the first element of the array till the last one.
    - Incase the current element is equal to the value to remove (Value k).
        - Swap the current element to where the element at index j is.
        - Reduce the space of j
        - Incement i only if the last element is not equal to k
    - Otherwise: Increment i
    NOTE: j should always be greater than or equal to i, otherwise, exit the iteration.
- i refers to the number of elements that are not equal to the value k
"""


def removeElement(nums: list[int], val: int) -> int:
    arrlen = len(nums)
    if arrlen == 0:
        return 0
    i = 0
    last_index = arrlen - 1
    while (i < arrlen):
        tmp = nums[i]
        if tmp == val:
            last_val = nums[last_index]
            nums[i] = last_val
            nums[last_index] = tmp
            if last_val != val:
                i += 1
            last_index -= 1
        else:
            i += 1
        # Incase the indices overlap
        if (last_index < i):
            break
    return i
