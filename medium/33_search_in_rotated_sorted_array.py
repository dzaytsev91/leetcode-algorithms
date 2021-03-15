from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        n = len(nums) - 1
        if nums[0] > target:
            index = n
            while index >= 0:
                if nums[index] == target:
                    return index

                if index == 0:
                    return -1

                if nums[index] < nums[index - 1]:
                    return -1

                index -= 1
        else:
            index = 0
            while index <= n:
                if nums[index] == target:
                    return index

                if index == n:
                    return -1

                if nums[index] > nums[index + 1]:
                    return -1

                index += 1

        return -1

