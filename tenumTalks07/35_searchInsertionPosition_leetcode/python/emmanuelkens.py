"""
 * View challenge here:- https://leetcode.com/problems/search-insert-position/description/ 
 * Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

"""

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        '''Method 1: using binary search 0(log n) time complexity'''
        last_index = len(nums) - 1
        last_value = nums[last_index]
        mid_index = int(last_index / 2)
        mid_value = nums[mid_index]
        left = nums[:mid_index]
        right = nums[mid_index:]
        print('find ' + str (target) + ' in ' + str(nums))
        print(str(left) + ' ' + str(right))
        if (last_value < target):
            return last_index + 1
        elif (mid_value < target):
            return self.searchInsert(right, target) + mid_index
        elif (mid_value > target):
            return self.searchInsert(left, target) + mid_index - 1
        else:
            return mid_index
        
        '''Method 1: using standard search'''
        mid_index = 0
        for index, num in enumerate(nums):
            if (num < target):
                mid_index = index + 1
            print(str(num) + ' ' + str(index) + ' ' + str(i))
            
            
        return mid_index

if __name__ == "__main__":
    s = Solution()

    #test case 1
    k = s.searchInsert(nums=[1,3,5,6], target=5)
    print(k) # expected result = 2

    #test case 2
    k = s.searchInsert(nums=[1,3,5,6], target=2)
    print(k) # expected result = 1
    
    #test case 2
    k = s.searchInsert(nums=[1,3,5,6], target=7)
    print(k) # expected result = 4