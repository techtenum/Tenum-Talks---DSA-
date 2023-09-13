# https://leetcode.com/problems/remove-duplicates-from-sorted-array
"""
Assumptions:
* Ensure the number of elements in the array is greater than one to have duplicates.
* The array is sorted in an ASCENDING order.

Pseudocode:
- Keep track of my true state of non duplicates (Using variable i)
- Iterate from the second element as along as it is not greater than the last element.
    > (This works out since the array is assumed to be sorted in an ascending order)
    - Keep track of the current element in the iteration (Using variable k)
    - Incase an element is greater than the element at the index at i (Element j):
        - Swap j with the next element after i.
        - Increment i
    - Increment j while ensuring that it remains in the valid range of indices to avoid an IndexError.
    - Incase there is no change between k and the value of the last element, there is no need to proceed.
        > (This works out since the array is assumed to be sorted in an ascending order)
- Return the index of my true state (i) + 1 since indices start from 0 and I need the number of unique values.
"""


def removeDuplicates(nums: list[int]) -> int:
    arrlen = len(nums)
    if arrlen <= 1:
        return arrlen
    else:
        i, j, last = 0, 1, nums[-1]
        while (nums[j] <= last):
            prev = nums[j]
            if (nums[j] > nums[i]):
                next_index = i + 1
                tmp = nums[next_index]
                nums[next_index] = nums[j]
                nums[j] = tmp
                i += 1
            j += 1
            if j == arrlen:
                j -= 1
            # Minimize iterations when the last value == the current one
            if prev == last:
                break
        return i + 1
