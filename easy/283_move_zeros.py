from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                nums[index], nums[zero_index] = nums[zero_index], nums[index]
                zero_index += 1
        return


if __name__ == '__main__':
    solution = Solution()
    nums1 = [0, 1, 0, 3, 12]
    nums2 = [0, 0, 3, 0]
    solution.moveZeroes(nums1)
    solution.moveZeroes(nums2)
    assert nums1 == [1,3,12,0,0]
    assert nums2 == [3, 0, 0, 0]
