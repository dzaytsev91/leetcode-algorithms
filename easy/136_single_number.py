from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        result = {}
        for num in nums:
            if num in result:
                result[num] += 1
            else:
                result[num] = 1

        for key in result:
            if result[key] == 1:
                return key

        return -1


if __name__ == '__main__':
    solution = Solution()
    nums1 = [2, 2, 1]
    nums2 = [4, 1, 2, 1, 2]
    assert solution.singleNumber(nums1) == 1
    assert solution.singleNumber(nums2) == 4

