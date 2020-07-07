# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.data = []
        self.pushAll(root)

    def pushAll(self, node):
        while node is not None:
            self.data.append(node)
            node = node.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if not self.hasNext():
            return -1
        temp = self.data.pop()
        self.pushAll(temp.right)
        return temp.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.data) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
