from Tree import TreeNode

# Given the TreeNode root
# Use recursion
# return whether root is a BST

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

# return min, max, isBST
# minLeft, maxLeft, isBSTLeft = isBSThelperV2(root.left)
# minRight, maxRight, isBSTRight = isBSThelperV2(root.right)
#check isBSTLeft, isBSTRight
#check minLeft < root.val, maxRight > root.val
def isBSTHelperV2(root):
    isBST = True
    minLeft = root.val
    maxLeft = root.val
    minRight = root.val
    maxRight = root.val
    
    if root.left is not None:
        minLeft, maxLeft, isBSTLeft = isBSTHelperV2(root.left)
        if isBSTLeft is False:
           isBST = False 

    if root.right is not None:
        minRight, maxRight, isBSTRight = isBSTHelperV2(root.right)
        if isBSTRight is False:
           isBST = False 
    
    if root.right is not None and minRight < root.val:
        isBST = False

    if root.left is not None and maxLeft > root.val:
        isBST = False
        
    minRoot = min(minLeft, minRight, root.val)
    maxRoot = max(maxLeft, maxRight, root.val)
    
    return minRoot, maxRoot, isBST

def checkBST(root):
    _, _, isBST = isBSTHelperV2(root)
    
    return isBST
    # if isBSThelper(root) == 0:
    #     return True
    # else:
    #     return False


root1 = TreeNode(2)
node1 = TreeNode(1)
node2 = TreeNode(4)
root1.left = node1
root1.right = node2

print(root1.levelOrderTraverse())
print(checkBST(root1))

# Can you add more test case?
Test5 = TreeNode(5)
node6 = TreeNode(6)
node8 = TreeNode(8)
node3 = TreeNode(3)
node10 = TreeNode(10)
node4 = TreeNode(4)

Test5.left  = node3
Test5.right = node6
node6.right  = node8
node8.right = node10
node8.left = node4
print(Test5.levelOrderTraverse())
print(checkBST(Test5))

#  5
#3   6
#      8
#    4   10




