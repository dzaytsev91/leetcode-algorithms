from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for index in range(n):
            result.append(nums[index])
            result.append(nums[index + n])
        return result
