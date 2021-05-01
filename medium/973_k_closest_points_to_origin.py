from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        data = {}
        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            if distance in data:
                data[distance].append(point)
            else:
                data[distance] = [point]

        for key, val in sorted(data.items()):
            for p in val:
                result.append(p)
                if len(result) == k:
                    return result
