from heapq import *


# Definition for a binary tree node.
from typing import List
from heapq import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        result = []
        heap = []
        heapify(heap)
        nodes = [root1, root2]
        for node in nodes:
            stack = [node]
            while stack:
                node = stack.pop()
                if not node:
                    continue
                heappush(heap, node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        while heap:
            result.append(heappop(heap))
        return result

