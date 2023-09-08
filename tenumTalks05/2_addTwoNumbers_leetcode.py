"""
 * You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order, and each of their nodes contains a single digit.
    Add the two numbers and return the sum as a linked list.
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 * View Challenge here - https://leetcode.com/problems/add-two-numbers/

 * The two linked lists are tranversed to return the two intergers. The sum is done.
 * A linked list is construted based on the sum.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def tranversal(ll: ListNode) -> int:
    index = 0
    sum = 0

    while ll:
        sum += ll.val * pow(10, index)
        index += 1
        ll = ll.next

    return sum


def construct(number: int) -> ListNode:
    total_ordered_nodes: list[ListNode] = []
    while number != 0:
        remainder = number % 10
        number = number // 10
        node = ListNode(remainder, None)
        total_ordered_nodes.append(node)

    # No node was inserted into the array (Input was 0).
    try:
        last_node = total_ordered_nodes.pop()
    except IndexError:
        return ListNode(0, None)

    first_node = last_node
    while len(total_ordered_nodes) > 0:
        tmp_node = total_ordered_nodes.pop()
        tmp_node.next = first_node
        first_node = tmp_node
    return first_node


class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        int1 = tranversal(ll=l1)
        int2 = tranversal(ll=l2)
        sum = int1 + int2
        return construct(sum)
