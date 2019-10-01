# https://leetcode.com/discuss/interview-question/330356
import heapq
# Time Complexity -> O(N log D)
# where N is the total number of characters ( A + B + C)
# D is the number of unique / distinct characters


def ls3(A, B, C):
    pq = []
    res = ""
    # Use a heap data structure.
    # heapq inserts values based on the 0th element in the tuple.
    # We are going to use a min heap
    # In a heap, for every node x with parent p, the key in p is smaller than or equal to the key in x

    # Creating/Building a heap - O(n)
    # Insert - O(log N)
    # Delete - O(log N)
    # Search - O(N)

    # Approach we will keep on building a string
    # During the process of building the string we will check if the result[-2:] == k * 2,
    # where k is either 'a', 'b' or 'c'
    # In such a case we, we cannot append k to the string because we problem condition is that no 3 consecutive
    # characters should be the same.

    # Start the string building process choosing character(k) that corresponds to max(A, B, C)
    # This is where the Heap comes in.

    # After each itearation decrement the number of characters(k) that should be incorporated into the final result
    # And push the same into the heap/pq
    # If the frequency of k == 1, don't push such a character

    for k, v in ('a', A), ('b', B), ('c', C):
        heapq.heappush(pq, (-v, k))
    # print("Priority Queue = ", pq)
    preV, preK = 0, ''
    while pq:
        v, k = heapq.heappop(pq)
        print("v = ", v, "k = ", k)
        if preV:
            heapq.heappush(pq, (preV, preK))
            preV, preK = 0, ''
        if res[-2:] == k * 2:
            preV, preK = v, k
            print("preV = ", preV, "prevK = ", k)
        else:
            res += k
            print(res)
            if v != -1:
                heapq.heappush(pq, (v + 1, k))
        print("-------")
    return res


A, B, C = 1, 1, 6
print(ls3(A, B, C))
# A, B, C = 1, 2, 3
# print(ls3(A, B, C))
