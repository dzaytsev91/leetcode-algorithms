from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        tmp = sorted(nums)

        start, stop = 0, 0
        for indx in range(len(nums)):
            if nums[indx] != tmp[indx]:
                start = indx
                break

        for indx in range(len(nums)):
            if nums[indx] != tmp[indx]:
                stop = indx

        if stop == 0:
            return 0

        return (stop - start) + 1
