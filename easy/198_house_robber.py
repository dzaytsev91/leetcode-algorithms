# repeat

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        last, now = 0, 0
        for val in nums:
            last, now = now, max(last + val, now)
        return now


if __name__ == '__main__':
    solution = Solution()
    assert solution.rob([1,2,3,1]) == 4
