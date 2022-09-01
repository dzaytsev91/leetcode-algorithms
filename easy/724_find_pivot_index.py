class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        index = 0
        for num in nums:
            right -= num
            if right == left:
                return index
            left += num
            index += 1
        return -1
