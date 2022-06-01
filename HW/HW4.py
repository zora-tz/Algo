from ListNode import Linkedlist
from ListNode import ListNode

# merge sort a linked list

def mergeSort(head):
    if head is None:
        return head
    if head.next is None:
        return head
    firsthead = head
    secondhead = midNode(head).next
    midNode(head).next = None
    head1 = mergeSort(firsthead)
    head2 = mergeSort(secondhead)

    if head1.val>head2.val:
        sortedHead = head2
        head2 = head2.next
    else:
        sortedHead = head1
        head1 = head1.next
    current = sortedHead
    
    while head1 is not None and head2 is not None:
        if head1.val > head2.val:
            current.next = head2
            current = current.next
            head2 = head2.next
        else:
            current.next = head1
            current = current.next
            head1 = head1.next
    
    if head2 is None:
        current.next = head1
    else:
        current.next = head2
    
    return sortedHead

# def index(head, i):
#     current = head
#     for n in range(i):
#         current = current.next
#     return current

def midNode(head):
    current = head
    i = 1
    while i < int(length(head)/2):
        current = current.next
        i += 1
    return current
        
def length(head):
    length = 0
    current = head
    while current != None:
        length += 1
        current = current.next
    return length


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

# print(length(head))
# print(midNode(head).val)
listSorted = mergeSort(head)
while listSorted is not None:
    print(listSorted.val)
    listSorted = listSorted.next
    
    
    
    
    
    

