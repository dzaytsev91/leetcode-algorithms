# idea: to iterate through array and count numbers and store it to hashmap
# thatn iterate one more time and check n-1 and n+1 not in array
# and counts.get(num) < 2

from typing import List


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        result = []
        for num in nums:
            if not count.get(num - 1) and not count.get(num + 1) and count.get(
                    num, 0) < 2:
                result.append(num)
        return result
