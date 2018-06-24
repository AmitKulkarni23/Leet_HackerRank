# The following is a description of the instance of this famous puzzle
# involving n=2 eggs and a building with k=36 floors.
#
# Suppose that we wish to know which stories in a 36-story
# building are safe to drop eggs from, and which will cause the eggs to break on landing

##############################

def egg_drop_recursive(n, k):
    """
    Function that returns the minimum number of trials needed
    to determine what is maximum floor from which an egg can be dropped
    without it breaking

    n -> number of eggs
    k -> number of floors
    """
    # If the number of floors is 0, 0 trials needed
    # If the number of floors is 1, then 1 trial is needed
    if k == 1 or k == 0:
        return k

    # If there is only egg, then we have to do k trials
    # Go 1 floor up each time the egg doesn't break
    if n == 1:
        return k

    min = float("inf")
    result = 0;

    for x in range(1, k):
        result = max(egg_drop_recursive(n -1, x -1), egg_drop_recursive(n, k-x))

        if result < min:
            min = result

    return min + 1


def egg_drop_memoized(n,k):
    """
    Function that returns the minimum number of trials needed
    to determine what is maximum floor from which an egg can be dropped
    without it breaking

    n -> number of eggs
    k -> number of floors
    Time COmplexity : O(n * k ^ 2)
    Space Complexity : O(nk)
    """

    # Construct a cache of n x k
    cache = [[0 for _ in range(k+1)] for _ in range(n+1)]

    # Ok, cache is constructed
    # One trial for 1 floor
    # 0 trial for 0 floors
    for i in range(1,n+1):
        cache[i][0] = 0
        cache[i][1] = 1

    # We need k trials for 1 egg
    for j in range(1, k+1):
        # Means we have only 1 egg and k fllors to test it against
        cache[1][j] = j

    for i in range(2, n+1):
        for j in range(2, k+1):
            cache[i][j] = float("inf")
            for x in range(1, j+1):
                result = 1 + max(cache[i-1][x -1], # breaks
                            cache[i][j - x] # doesn't break
                            )

                if result < cache[i][j]:
                    cache[i][j] = result
    # print(cache)
    return cache[-1][-1]


# Examples:
n = 2
k = 10
# print("Min trials required = ", egg_drop_recursive(n, k))
print(egg_drop_memoized(n, k))
