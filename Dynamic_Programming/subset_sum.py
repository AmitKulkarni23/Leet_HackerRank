# Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
#
# Examples: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
# Output:  True  //There is a subset (4, 5) with sum 9.

import pprint

def subset_sum(S, total):
    """
    Function that returns whether the total can be formed
    using a subset of set S
    """

    if total == 0 and set:
        # Can use empty set
        return True

    if not set and total:
        # There are not elements in teh set and total > 0
        return False

    # Create a cache adn initiliaze all values as False
    cache = [[False for _ in range(total + 1)] for _ in range(len(S) + 1)]

    # Initiliaze the first column as True
    for i in range(len(S) + 1):
        cache[i][0] = True

    # Now iterate
    for i in range(1, len(S) + 1):
        for j in range(1, total + 1):
            if j < S[i-1]:
                cache[i][j] = cache[i-1][j]
            else:
                cache[i][j] = cache[i-1][j] or cache[i-1][j-S[i - 1]]

    # pprint.pprint(cache)
    return cache[-1][-1]


S=[2, 3, 7, 8, 10]
total = 47

print(subset_sum(S, total))
