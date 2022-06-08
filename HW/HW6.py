from ListNode import Linkedlist
from ListNode import ListNode

class Stack(object):
    def __init__(self):
        self.linkedList = Linkedlist()
    
    #add element to the stack
    def push(self, element):
        return
    
    #check the top element
    def peek(self):
        return

    #pop the top element
    def pop(self):
        return
    
    #return all elements in the stack
    def elements(self):
        return
    
stack = Stack()
stack.push(5)
stack.push(2)
stack.push(1)
stack.push(7)

element1 = stack.peek()
print(element1)
elements = stack.elements()
print(elements)

element2 = stack.pop()
print(element2)
elements = stack.elements()
print(elements)