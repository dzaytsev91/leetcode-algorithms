import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.data = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already
        contain the specified element.
        """
        if val not in self.nums:
            self.nums.append(val)
            self.data[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the
        specified element.
        """
        if val in self.nums:
            idx, last_num = self.data[val], self.nums[-1]
            self.nums[idx], self.data[last_num] = last_num, idx
            self.nums.pop()
            self.data.pop(val, 0)
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
