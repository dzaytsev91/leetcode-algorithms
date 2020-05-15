from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        if not candies:
            return []
        max_candies = max(candies)
        for candy in candies:
            if candy+extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        return result
