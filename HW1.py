from Tree import TreeNode

# Given the TreeNode root
# Use recursion
# return whether root is a BST

# def checkTreeValues(node):
#     rootval = node.val
#     if node.left is not None:
#         if node.left.val > rootval:
#             return False
#         checkTreeValues(node.left)
    

# def isBST(root):
#     if root.left is not None:      
#         if len([filter(lambda x: x > root.val, root.left.preTraversePrint())]) > 0:
#             print(root.left.preTraversePrint())
#             print([filter(lambda x: x > root.val, root.left.preTraversePrint())])
#             return False
#         isBST(root.left)
#     if root.right is not None:
#         if len([filter(lambda x: x < root.val, root.right.preTraversePrint())]) > 0:
#             print(root.right.preTraversePrint())
#             print([filter(lambda x: x < root.val, root.right.preTraversePrint())])
#             return False
#         isBST(root.right)
#     return True

# def isBST(root):
#     print(root.val)
#     if root.left is not None:
#         if len(list(x for x in root.left.preTraversePrint() if x > root.val)) > 0:
#             print("left branch")
#             print(root.left.preTraversePrint())
#             print("eval")
#             print(list(x for x in root.left.preTraversePrint() if x > root.val))
#             print(len(list(x for x in root.left.preTraversePrint() if x > root.val)))
#             print("f")
#             return False
#         isBST(root.left)
#     if root.right is not None:
#         if len(list(x for x in root.right.preTraversePrint() if x < root.val)) > 0:
#             print("right branch")
#             print(root.right.preTraversePrint())
#             print("eval")
#             print(list(x for x in root.right.preTraversePrint() if x < root.val))
#             print(len(list(x for x in root.right.preTraversePrint() if x < root.val)))
#             return False
#         isBST(root.right)
#     #print('t')
#     else:
#         return True

def isBSThelper(root):
    output = 0
    if root.left is not None:
        if len(list(x for x in root.left.preTraversePrint() if x > root.val)) > 0:
            return 1
        output = output + isBSThelper(root.left)
    if root.right is not None:
        if len(list(x for x in root.right.preTraversePrint() if x < root.val)) > 0:
            return 1
        output = output + isBSThelper(root.right)
    return output

def isBST(root):
    if isBSThelper(root) == 0:
        return True
    else:
        return False

# def isBST(root):
#     if root.left is not None:
#         if len(list(x for x in root.left.preTraversePrint() if x > root.val)) > 0:
#             return False
#         isBST(root.left)
#     if root.right is not None:
#         if len(list(x for x in root.right.preTraversePrint() if x < root.val)) > 0:
#             return False
#         isBST(root.right)
#     return True


root1 = TreeNode(2)
node1 = TreeNode(1)
node2 = TreeNode(4)
root1.left = node1
root1.right = node2

print(root1.levelOrderTraverse())
print(isBST(root1))

# Can you add more test case?
Test5 = TreeNode(5)
node6 = TreeNode(6)
node8 = TreeNode(8)
node3 = TreeNode(3)
node10 = TreeNode(10)

Test5.left  = node3
Test5.right = node6
node6.right  = node8
node8.right = node10
print(Test5.levelOrderTraverse())
print(isBST(Test5))

