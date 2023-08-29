/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  // // using loops -- use 2 pointers from left and from right
  // for(let num in nums){
  //     let i = nums.length
  //     while(i>0){
  //     if(num>=i) break;
  //     if(nums[num]+nums[--i]===target && num!=i) return [num, i];
  //     }
  // }

  // using hashMaps (object) -- Find if complement of no. exists then thats the answer
  let numsObj = {};
  let result = []; // Initialize the result variable
  nums.forEach((num, index) => {
    numsObj[num] == undefined
      ? (numsObj[num] = [index])
      : numsObj[num].push(index);
    let complement = target - num;

    if (numsObj[complement] !== undefined && numsObj[complement][0] !== index) {
      result = [
        numsObj[complement][0],
        numsObj[num].length > 1 ? numsObj[num][1] : numsObj[num][0],
      ];
    }
  });

  return result;
};
