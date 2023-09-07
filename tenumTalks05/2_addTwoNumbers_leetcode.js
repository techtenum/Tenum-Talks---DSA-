/**
 * You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 * View Challenge here - https://leetcode.com/problems/add-two-numbers/
 */

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
  let l3 = new ListNode(0);
  let sumList = l3;
  let sumArr = [];
  let sum = 0,
    carry = 0;
  while (l1 !== null || l2 !== null || carry) {
    sum = 0;
    if (l1 !== null && l2 !== null) {
      sum = l1.val + l2.val + carry;
    } else if (l1 !== null && l2 === null) {
      sum = l1.val + carry;
    } else if (l1 === null && l2 !== null) {
      sum = l2.val + carry;
    } else {
      sum = carry;
      carry = 0;
    }
    carry = Math.floor(sum / 10);
    sum = sum - carry * 10;
    //    sumArr.push(sum);
    sumList.next = new ListNode(sum);
    sumList = sumList.next;
    l1 = l1 ? l1.next : null;
    l2 = l2 ? l2.next : null;
  }
  return l3.next;
};
