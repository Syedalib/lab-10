class AVLNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.height = 1  

def height(node):
    return node.height if node else 0

def update_height(node):
    node.height = 1 + max(height(node.left), height(node.right))

def balance_factor(node):
    return height(node.left) - height(node.right)

def left_rotate(y):
    x = y.right
    T2 = x.left

    x.left = y
    y.right = T2

    update_height(y)
    update_height(x)

    return x

def right_rotate(x):
    y = x.left
    T2 = y.right

    y.right = x
    x.left = T2

    update_height(x)
    update_height(y)

    return y

def insert(root, key):
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    update_height(root)

    balance = balance_factor(root)

    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    
    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

def get_min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

def delete(root, key):
    if not root:
        return root

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        temp = get_min_value_node(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)

    update_height(root)

    balance = balance_factor(root)

    if balance > 1:
        if balance_factor(root.left) >= 0:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    
    if balance < -1:
        if balance_factor(root.right) <= 0:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

def inorder_traversal(root):
    result = []
    if root:
        result.extend(inorder_traversal(root.left))
        result.append(root.key)
        result.extend(inorder_traversal(root.right))
    return result


avl_root = None

keys_to_insert = [9, 5, 10, 0, 6, 11, -1, 1, 2]
for key in keys_to_insert:
    avl_root = insert(avl_root, key)

print("AVL Tree after insertion:", inorder_traversal(avl_root))

key_to_delete = 10
avl_root = delete(avl_root, key_to_delete)
print("AVL Tree after deletion of", key_to_delete, ":", inorder_traversal(avl_root))
