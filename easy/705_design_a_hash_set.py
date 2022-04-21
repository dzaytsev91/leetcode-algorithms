# idea: create an array of linked lists and calculate hash number of each key
# and put this key into linked list, design add, delete, exists functions
# for linked list


class MyHashSet:

    def __init__(self):
        self.capacity = 1024
        self.array = [Bucket() for x in range(self.capacity)]

    def hash(self, key):
        return key % self.capacity

    def add(self, key: int) -> None:
        bucket_index = self.hash(key)
        self.array[bucket_index].insert(key)

    def remove(self, key: int) -> None:
        bucket_index = self.hash(key)
        self.array[bucket_index].delete(key)

    def contains(self, key: int) -> bool:
        bucket_index = self.hash(key)
        return self.array[bucket_index].exists(key)


class Node:
    def __init__(self, val, next_node=None):
        self.value = val
        self.next = next_node


class Bucket:

    def __init__(self):
        self.head = Node(0)

    def insert(self, val):
        if not self.exists(val):
            new_node = Node(val, self.head.next)
            self.head.next = new_node

    def delete(self, val):
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.value == val:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def exists(self, val):
        curr = self.head.next
        while curr is not None:
            if curr.value == val:
                return True
            curr = curr.next
        return False
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
