class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root):
    def height(node):
        if not node:
            return 0
        left_height = height(node.left)
        right_height = height(node.right)
       
        diameter[0] = max(diameter[0], left_height + right_height)
       
        return 1 + max(left_height, right_height)

    if not root:
        return 0

    diameter = [0]  

    height(root)
    
    return diameter[0]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


diameter = diameterOfBinaryTree(root)
print("Diameter of the binary tree:", diameter)
