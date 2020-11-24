from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for idx in range(len(nums)):
            target.insert(index[idx], nums[idx])
        return target
