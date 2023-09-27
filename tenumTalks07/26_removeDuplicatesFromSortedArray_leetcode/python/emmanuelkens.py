"""
 * View challenge here:- https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
 * Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        '''Method 1: converting to set to remove duplicates'''
        expectedNums = list(set(nums))
        k = len(expectedNums)

        nums.clear()

        for num in expectedNums:
            nums.append(num)
        
        '''Method 2: iterating through the list and checking whether it exits in the already non duplicate list'''
        
        expectedNums = []
        duplicateNums = []
        for i in nums:
            if i not in expectedNums:
                expectedNums.extend([i])
            else:
                duplicateNums.append(i)
        k = len(expectedNums)
        
        expectedNums.extend(duplicateNums)

        nums.clear()

        for num in expectedNums:
            nums.append(num)

        return k

if __name__ == "__main__":
    s = Solution()

    #test case 1
    k = s.removeDuplicates(nums=[1,1,2])
    print(k) # expected result = 2

    #test case 2
    k = s.removeDuplicates(nums=[0, 0, 1, 1, 2, 3, 4, 4, 5])
    print(k) # expected result = 6