from typing import List


class NestedInteger:

    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class Solution:
    def get_max_depth(self, nested):
        max_depth = 0
        for num in nested:
            stack = [(num, 1)]
            while stack:
                node, lvl = stack.pop()
                max_depth = max(max_depth, lvl)
                if node.isInteger():
                    continue
                for node in node.getList():
                    stack.append([node, lvl + 1])
        return max_depth

    def get_result(self, nested, max_depth):
        result = 0
        for num in nested:
            stack = [(num, 1)]
            while stack:
                node, lvl = stack.pop()
                if node.isInteger():
                    weight = max_depth - lvl + 1
                    result += weight * node.getInteger()
                for node in node.getList():
                    stack.append([node, lvl + 1])
        return result

    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        return self.get_result(nestedList, self.get_max_depth(nestedList))
