from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        last = -1
        distance = 0
        for index in range(len(seats)):
            if seats[index]:
                if last < 0:
                    distance = index
                else:
                    distance = max(distance, (index-last)//2)
                last = index
        return max(distance, ((len(seats)-1) - last))
