/**
 * View challenge here:- https://leetcode.com/problems/remove-element/description/
 * Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function (nums, val) {
  let i = 0;
  while (i != -1) {
    i = nums.indexOf(val);
    if (i != -1) {
      let removed = nums.pop();
      if (nums.length > 0 && i < nums.length) nums[i] = removed;
    }
  }
  return nums.length;
};
