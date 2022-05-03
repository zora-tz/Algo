class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def preTraversePrint(self):
        answer = [self.val]
        if self.left is not None:
            answer.extend(self.left.preTraversePrint())
        if self.right is not None:
            answer.extend(self.right.preTraversePrint())
        return answer
    
    def inTraversePrint(self):
        answer = []
        if self.left is not None:
            answer.extend(self.left.inTraversePrint())
        answer.extend([self.val])
        if self.right is not None:
            answer.extend(self.right.inTraversePrint())
        return answer
            
    def postTraversePrint(self):
        answer = []
        if self.left is not None:
            answer.extend(self.left.postTraversePrint())
        if self.right is not None:
            answer.extend(self.right.postTraversePrint())
        answer.extend([self.val])
        return answer
    
    def insertNode(self, x):
        if self is None:
            self = TreeNode(x)
        if x < self.val:
            if self.left is None:
                self.left = TreeNode(x)
            self.left.insertNode(x)
        if x > self.val:
            if self.right is None:
                  self.right = TreeNode(x)
            self.right.insertNode(x)
    
    def levelOrderTraverse(self):
        currentLevel = [self]
        answer = []
        while len(currentLevel) > 0:
            nextLevel = []
            currentLevelAnswer = []
            for node in currentLevel:
                if node is None:
                    currentLevelAnswer.append(node)
                    continue
                
                currentLevelAnswer.append(node.val)
                nextLevel.append(node.left)
                nextLevel.append(node.right)
                
            answer.append(currentLevelAnswer)
            currentLevel = nextLevel              
        
        return answer
    
class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        
    def insert(self, x):
        if self.root is None:
            self.root = TreeNode(x)
        self.root.insertNode(x)           
            
    def levelPrint(self):
        if self.root is not None:
            print(self.root.levelOrderTraverse())
       
# Node8 = TreeNode(8)
# Node3 = TreeNode(3)
# Node1 = TreeNode(1)
# Node6 = TreeNode(6)
# Node10 = TreeNode(10)
# Node8.left = Node3
# Node3.left = Node1
# Node8.right = Node10
# print(Node8.levelOrderTraverse())
BSTree = BinarySearchTree()
BSTree.insert(5)
BSTree.insert(8)
BSTree.insert(2)
BSTree.insert(1)
BSTree.insert(9)
BSTree.insert(4)

BSTree.levelPrint()
print(BSTree.root.preTraversePrint())
print(BSTree.root.inTraversePrint())
print(BSTree.root.postTraversePrint())

            