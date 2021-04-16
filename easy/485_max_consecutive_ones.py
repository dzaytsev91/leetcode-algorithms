from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_value = 0
        result = 0
        for num in nums:
            if num == 1:
                max_value += 1
                result = max(result, max_value)
            else:
                max_value = 0
        return result
