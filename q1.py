class TreeNode:
    def _init_(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    def encode(node):
        if node:
            vals.append(str(node.val))
            encode(node.left)
            encode(node.right)
        else:
            vals.append("#")

    vals = []
    encode(root)
    return ",".join(vals)

def deserialize(data):
    def decode():
        val = next(vals)
        if val == "#":
            return None
        node = TreeNode(int(val))
        node.left = decode()
        node.right = decode()
        return node

    vals = iter(data.split(","))
    return decode()