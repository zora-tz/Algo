from Tree import TreeNode

# Given the TreeNode root
# Use recursion
# return whether root is a BST
def isBST(root):
       
    return True


root1 = TreeNode(3)
node1 = TreeNode(2)
node2 = TreeNode(4)
root1.left = node1
root1.right = node2

print(root1.levelOrderTraverse())
print(isBST(root1))

# Can you add more test case?