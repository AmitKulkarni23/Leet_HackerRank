# https://leetcode.com/problems/random-pick-with-weight/description/

class Solution:

    def __init__(self, w: List[int]):
        total = 0
        self.prefix_sums = []

        # What is the meaning of prefix sums
        # Index 0: occupies interval [0, 1)
        # Index 1: occupies interval [1, 4)
        # Index 2: occupies interval [4, 6)

        for weight in w:
            total += weight
            self.prefix_sums.append(total)
        self.total = total

    def pickIndex(self) -> int:
        # random.random() generates a float between 0 and 1
        # So target is a float between 0 and total_sum
        # In the first example:
        # If target = 0.9 → falls in [0, 1) → index 0
        # If target = 1.5 → falls in [1, 4) → index 1
        # If target = 4.2 → falls in [4, 6) → index 2

        # O log(n) because we are using binary search here

        target = self.total * random.random()
        low, high = 0, len(self.prefix_sums)
        while low < high:
            mid = low + (high - low) // 2
            if target > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low

    # def pickIndex(self) -> int:
    #     # random.random() generates a float between 0 and 1
    #     # So target is a float between 0 and total_sum
    #     # In the first example:
    #     # If target = 0.9 → falls in [0, 1) → index 0
    #     # If target = 1.5 → falls in [1, 4) → index 1
    #     # If target = 4.2 → falls in [4, 6) → index 2

    #     # This is O(n) solution

    #     target = self.total * random.random()

    #     for idx, item in enumerate(self.prefix_sums):
    #         if target < item:
    #             # You're finding the first index where target is less than the prefix sum — meaning, it falls inside that index's weighted zone.
    #             return idx

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()