# repeat


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        current_max = None
        max_sum = None

        for index in range(len(nums)):
            if index == 0:
                current_max = nums[index]
                max_sum = nums[index]
                continue

            current_max = max(nums[index], current_max + nums[index])
            if current_max > max_sum:
                max_sum = current_max

        return max_sum


if __name__ == '__main__':
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4] # 6
    nums2 = [-2] # -2
    nums3 = [1, 2, 3, 4, 5, 6, 7, 8] # 36
    nums4 = [-1, 0, -2]
    solution = Solution()
    assert solution.maxSubArray(nums1) == 6
    assert solution.maxSubArray(nums2) == -2
    assert solution.maxSubArray(nums3) == 36
    assert solution.maxSubArray(nums4) == 0

