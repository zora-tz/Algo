from ListNode import Linkedlist
from ListNode import ListNode

# Bubble sort for linked list
# For each iteration, find the smallest element and put it to the leftmost

def smallestNode(head):
    smallest = head
    current = head.next
    while current is not None:
        if current.val < smallest.val:
            smallest = current
            current = current.next
        else:
            current = current.next
    return smallest

    
def bubbleSortH(head):
    if head.next is not None:
        small = smallestNode(head.next)
        if head.val < small.val:
            bubbleSortH(head.next)
        if head.val > smallestNode(head.next).val:
            temp = head.val
            head.val = small.val
            small.val = temp 
            bubbleSortH(head.next)
        return head
        
    
def bubbleSort(linkedList):
    linkedList.head = bubbleSortH(linkedList.head)

    return linkedList



list = Linkedlist()
list.insert(3)
list.insert(10)
list.insert(4)
list.insert(25)
list.insert(7)
list.insert(2)
list.print()
# print(smallestNode(list.head).val)
print("bubble sort")
bubbleSort(list).print()

