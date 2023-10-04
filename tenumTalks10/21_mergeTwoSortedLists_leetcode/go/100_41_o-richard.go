package main

type ListNode struct {
	Val int
	Next *ListNode
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	list := ListNode{}
	head := &list
	for list1 != nil && list2 != nil {
		if list1.Val <= list2.Val {
			head.Next = list1
			head = head.Next
			list1 = list1.Next
		} else {
			head.Next = list2
			head = head.Next
			list2 = list2.Next
		}
	}

	if list1 != nil {
		head.Next = list1
	} else {
		head.Next = list2
	}

	return list.Next
}

func main() {
	/*
	Sample Usage

	myList1 := &ListNode{
		Val: 1,
		Next: &ListNode{
			Val: 2,
			Next: &ListNode{
				Val: 4,
				Next: nil,
			},
		},
	}
	myList2 := &ListNode{
		Val: 1,
		Next: &ListNode{
			Val: 3,
			Next: &ListNode{
				Val: 4,
				Next: nil,
			},
		},
	}

	newList := mergeTwoLists(myList1, myList2)
	*/
}