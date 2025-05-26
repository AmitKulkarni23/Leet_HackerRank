# https://leetcode.com/problems/design-hashset/description/


# Complexity - O(1) for add, remove, and contains operations on average.
# Complexity - O(n/b) for worst case, where n is the number of elements and b is the number of buckets.
class MyHashSet:

    def __init__(self):
        self.size = 1009  # A prime number for better hash distribution
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        h = self._hash(key)
        if key not in self.buckets[h]:
            self.buckets[h].append(key)

    def remove(self, key: int) -> None:
        h = self._hash(key)
        if key in self.buckets[h]:
            self.buckets[h].remove(key)

    def contains(self, key: int) -> bool:
        h = self._hash(key)
        return key in self.buckets[h]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)