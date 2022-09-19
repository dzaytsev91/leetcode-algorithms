# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        stack = [(p, q)]
        while stack:
            left, right = stack.pop()
            if not left and right:
                return False
            if not right and left:
                return False
            
            if left.val != right.val:
                return False
            
            if not left.left and right.left:
                return False
            if not right.left and left.left:
                return False
            if not left.right and right.right:
                return False
            if not right.right and left.right:
                return False
            
            if left.left:
                stack.append([left.left, right.left])
            if left.right:
                stack.append([left.right, right.right])
            
        return True
