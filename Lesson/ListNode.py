class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Linkedlist(object):
    def __init__(self):
        self.head = None
        
    def insert(self, x):
        if self.head == None:
            self.head = ListNode(x)
        else:
            lastnode = self.head
            while lastnode.next is not None:
                lastnode = lastnode.next
            lastnode.next = ListNode(x)
            
    def print(self):
        current = self.head
        while current is not None:
            print(current.val)
            current = current.next
            
    def remove(self, x):
        if self.head == None:
            return
        if self.head.val == x:
            self.head = self.head.next
            return
        last = self.head
        current = last.next
        while current is not None:
            if current.val == x:
                last.next = current.next
                break
            else:
                last = current
                current = current.next
                
    def reverse(self):
        self.head = self.reverse2(self.head)

    def reverse2(self, node):
        if node.next is None:
            return node
        #node=12345
        nextReversedHead = self.reverse2(node.next) #5432
        
        current = nextReversedHead
        while current.next is not None:
            current = current.next
        current.next = node
        node.next = None
        
        return nextReversedHead
    
    def removeIndex(self, index):
        if self.length() < index:
            return
        if index == 1:
            self.head = self.head.next
            return
        current = self.head
        nextNode = self.head.next
        for i in range(index-2):
            current = current.next
            nextNode = nextNode.next
        current.next = nextNode.next
            
    def length(self):
        if self.head is None:
            return 0
        len = 1
        current = self.head
        while current.next is not None:
            len += 1
            current = current.next
        #print(len)
        return len
    
    def lengthR(self):
        if self.head is None:
            return 0
        return self.lengthR2(self.head)
    
    def lengthR2(self, node):
        if node.next == None:
            return 1
        return self.lengthR2(node.next) + 1
        
        
            
# list = Linkedlist()
# list.insert(1)
# list.insert(2)
# list.insert(3)
# list.insert(4)
# list.print()
# print(list.lengthR())
#list.removeIndex(5)
#list.print()
