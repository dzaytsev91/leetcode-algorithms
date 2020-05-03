from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 2:
            return False
        data = {}
        for num in nums:
            if num in data:
                return True
            else:
                data[num] = True
        return False
