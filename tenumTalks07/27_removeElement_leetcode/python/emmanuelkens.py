"""
 * View challenge here:- https://leetcode.com/problems/remove-element/description/
 * Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

"""

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        '''Method 1: using list comprehension'''
        expectedNums = [element for element in nums if element != val]
        
        nums.clear()
        # nums = [num for num in without_duplicates]
        # print(nums)
        for num in expectedNums:
            nums.append(num)
            
        print(nums)

        k = len(expectedNums)

        return k

if __name__ == "__main__":
    s = Solution()

    #test case 1
    k = s.removeElement(nums=[3,2,2,3], val=3)
    print(k) # expected result = 2

    #test case 2
    k = s.removeElement(nums=[0,1,2,2,3,0,4,2], val=2)
    print(k) # expected result = 5