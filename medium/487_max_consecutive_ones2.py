from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # k is the number of possible replacements
        k = 1
        left = 0
        result = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            result = max(result, right - left + 1)
        return result
