class Stack(object):
    def __init__(self):
        self.myList = []
    
    #add element to the stack
    def push(self, element):
        self.myList.append(element)
        return
    
    #check the top element
    def peek(self):
        if len(self.myList) == 0:
            return None
        
        return self.myList[-1]

    #pop the top element
    def pop(self):
        if len(self.myList) == 0:
            return None
        
        value = self.myList.pop(-1) 
        return value
    
    #return all elements in the stack
    def elements(self):
        return self.myList
 
#queue: [1 2 3 4]
#pop [2 3 4]    
 
stack = Stack()
stack.push(5)
stack.push(2)
stack.push(1)
stack.push(7)

#5 2 1 7
element1 = stack.peek()
print(element1)
elements = stack.elements()
print(elements)

element2 = stack.pop()
print(element2)
elements = stack.elements()
print(elements)