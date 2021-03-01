from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = [int(x) for x in list(boxes)]
        result = []
        for index in range(len(boxes)):
            max_movements = 0
            for indx in range(len(boxes)):
                if index == indx:
                    continue
                if boxes[indx] == 0:
                    continue
                max_movements += abs(index-indx)
            result.append(max_movements)
        return result
