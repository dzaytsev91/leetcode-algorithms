from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        result = 0
        zero_count = 0
        while right < len(nums):
            if nums[right] == 1:
                right += 1
                result = max(result, right-left)
            else:
                if zero_count < k:
                    right += 1
                    zero_count += 1
                    result = max(result, right-left)
                else:
                    while left <= right and zero_count >= k:
                        if nums[left] == 0:
                            zero_count -= 1
                        left += 1
        return result
