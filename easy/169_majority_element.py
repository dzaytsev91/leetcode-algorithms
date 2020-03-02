from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        data = {}
        majority_val = len(nums) / 2
        for val in nums:
            if val not in data:
                data[val] = 1
            else:
                data[val] += 1

        for value in data:
            if data[value] >= majority_val:
                return value


if __name__ == '__main__':
    solution = Solution()
    nums1 = [3, 2, 3]
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    assert solution.majorityElement(nums1) == 3
    assert solution.majorityElement(nums2) == 2
