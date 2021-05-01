class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].update({timestamp: value})
        else:
            self.data[key] = {timestamp: value}

    def get(self, key: str, timestamp: int) -> str:
        values = self.data.get(key)
        if not values:
            return ""
        if timestamp in values:
            return values[timestamp]
        while timestamp != 0:
            timestamp -= 1
            if values.get(timestamp):
                return values[timestamp]
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
