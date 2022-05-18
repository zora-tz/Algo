from ListNode import Linkedlist
from ListNode import ListNode

#merge sort a linked list
def mergeSort(head):
    
    return head

head = ListNode(55)
node4 = ListNode(4)
node1 = ListNode(1)
node5 = ListNode(5)
node3 = ListNode(3)
node200 = ListNode(200)
node100 = ListNode(100)
node2 = ListNode(2)

head.next = node4
node4.next = node1
node1.next = node5
node5.next = node3
node3.next = node200
node200.next = node100
node100.next = node2

listSorted = mergeSort(head)
