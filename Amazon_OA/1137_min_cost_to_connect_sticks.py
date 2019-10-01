# https://leetcode.com/problems/minimum-cost-to-connect-sticks/
import heapq


def connectSticks(sticks):
    # Credits -> https://leetcode.com/problems/minimum-cost-to-connect-sticks/discuss/365865/Python-Greedy-Solution
    # Use a heap / priority queue to get 2 sticks with lower lengths/costs .
    # Add the cost of each of these and push the sum back into the heap
    # Do this until there is only one such stick in the list

    # heapq.heapify modifies the list in place
    # Time Complexity - 2 push, 1 pop for N such items.
    # Each push and pop takes O(log N) time.
    # O(N log N)

    # Space -> O(sticks). Building a heap from a list takes O(number_of_elements_in_list) time

    heapq.heapify(sticks)
    cost = 0

    while len(sticks) > 1:
        first, second = heapq.heappop(sticks), heapq.heappop(sticks)
        cost += first + second
        heapq.heappush(sticks, first + second)

    return cost

