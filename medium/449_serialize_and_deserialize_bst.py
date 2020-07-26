# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """

        data = []

        def helper(node):
            if node:
                val = str(node.val)
                data.append(val)
                helper(node.left)
                helper(node.right)

        helper(root)

        return "#".join(data)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if data == "":
            return

        vals = list(map(int, data.split('#')))
        root = TreeNode(vals.pop(0))
        while vals:
            node = TreeNode(vals.pop(0))
            current_node = root

            while True:
                if node.val > current_node.val:
                    if not current_node.right:
                        current_node.right = node
                        break
                    else:
                        current_node = current_node.right
                else:
                    if not current_node.left:
                        current_node.left = node
                        break
                    else:
                        current_node = current_node.left
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

