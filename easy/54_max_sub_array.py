# repeat


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        res_max_sum = None
        max_sum = None
        for val in nums:
            if max_sum is None:
                max_sum = val
                res_max_sum = val
            else:
                max_sum = max(max_sum + val, val)
                if max_sum > res_max_sum:
                    res_max_sum = max_sum
        return res_max_sum


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

