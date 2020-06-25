class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.recents = []

    def get(self, key: int) -> int:
        if key in self.cache:
            if key in self.recents:
                self.recents.remove(key)
            self.recents.insert(0, key)
        return self.cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if self.capacity <= len(self.cache) and key not in self.cache:
            del self.cache[self.recents.pop()]
        self.cache[key] = value
        if key in self.recents:
            self.recents.remove(key)
        self.recents.insert(0, key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
