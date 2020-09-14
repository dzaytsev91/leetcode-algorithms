import bisect


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.data, num)

    def findMedian(self) -> float:
        if len(self.data) % 2 == 0:
            return (self.data[len(self.data) // 2] + self.data[
                len(self.data) // 2 - 1]) / 2
        else:
            return self.data[len(self.data) // 2]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
