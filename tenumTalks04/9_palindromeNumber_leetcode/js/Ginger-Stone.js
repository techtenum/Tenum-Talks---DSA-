/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
  (x = x.toString()), (i = 0), (j = x.length - 1);
  while (i < j) {
    if (x[i] !== x[j]) return false;
    k;
    i++;
    j--;
  }
  return true;
};
