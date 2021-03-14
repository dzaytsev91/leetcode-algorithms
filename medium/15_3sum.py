from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for index in range(n - 2):
            if nums[index] > 0:
                break

            if index > 0 and nums[index] == nums[index - 1]:
                continue

            left, right = index + 1, n - 1

            while left < right:
                val = nums[index] + nums[left] + nums[right]

                if val < 0:
                    left += 1
                elif val > 0:
                    right -= 1
                else:
                    result.append([nums[index], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result

