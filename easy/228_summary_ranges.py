from typing import List


class Solution:
    def formatter(self, f, l):
        if f == l:
            return str(f)
        return "{}->{}".format(f, l)

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        if len(nums) < 2:
            return [str(nums[0])]
        nums.sort()
        result = []
        start_interval = nums[0]
        end_interval = nums[0]
        for index in range(1, len(nums)):
            if nums[index] == end_interval + 1:
                end_interval = nums[index]
            else:
                result.append(self.formatter(start_interval, end_interval))
                start_interval = nums[index]
                end_interval = nums[index]

        result.append(self.formatter(start_interval, end_interval))

        return result
