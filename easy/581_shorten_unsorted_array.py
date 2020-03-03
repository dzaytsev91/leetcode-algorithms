# repeat

from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        new_nums = nums[::]
        new_nums.sort()
        start, end = 0, 0
        is_sorted = True
        for index in range(len(nums)):
            if is_sorted and nums[index] != new_nums[index]:
                start = index
                is_sorted = False
            if not is_sorted and nums[index] != new_nums[index]:
                end = index

        return end - start+1 if end - start else 0



if __name__ == '__main__':
    solution = Solution()
    solution.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])
