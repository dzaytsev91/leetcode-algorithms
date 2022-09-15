# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        stack = [(root, {})]
        result = 0
        while stack:
            node, freq_count = stack.pop()
            if not node:
                continue

            if freq_count.get(node.val):
                freq_count[node.val] += 1
            else:
                freq_count[node.val] = 1
                
            if node.left:
                stack.append([node.left, freq_count.copy()])
            if node.right:
                stack.append([node.right, freq_count.copy()])
            
            if not node.left and not node.right:
                if self.check_pseudo_palindrome(freq_count):
                    result += 1
        return result

    def check_pseudo_palindrome(self, nums_map):
        odd_count = 0
        for num in nums_map:
            if nums_map[num] % 2 != 0:
                odd_count += 1
        return odd_count < 2
            
        
        
