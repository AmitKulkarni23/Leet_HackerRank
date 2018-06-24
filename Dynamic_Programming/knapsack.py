# Given weights and values of n items, put these items in a knapsack of capacity
# W to get the maximum total value in the knapsack.
# In other words, given two integer arrays val[0..n-1] and wt[0..n-1]
# which represent values and weights associated with n items respectively

# Example:
# val = [60, 100, 120]
# weight = [10, 20, 30]
#
# W = 50

def knapsack_recursive(val, weights, W, n):
    """
    Function that returns teh maximum value that can be obtained
    for the knapsack problem

    Idea: There are 2 possibilites
    1- either teh nth item is in the knapsack
    2 - Or not

    n -> len(val)
    val -> list
    weights -> list
    W -> int

    Time Complexity : O(2 ^ n) - as subproblems are calculated again and again
    """

    if n == 0 or W == 0:
        return 0

    if weight[n-1] > W:
        # Such a weight cannot be in the knapsack at all
        return knapsack_recursive(val, weights, W, n-1)

    else:
        return max(val[n-1] + knapsack_recursive(val, weights, W - weights[n-1], n - 1), # In teh knapsack
         knapsack_recursive(val, weights, W, n -1)) # Not in teh knapsack



def knapsack_cached(val, weights, W, n):
    """
    Function that returns teh maximum value that can be obtained
    for the knapsack problem

    Time Complexity -> O(nW)
    """

    # Create a cache
    cache = [[0 for _ in range(W+1)] for _ in range(n+1)]

    # Iterate through the matrix
    for i in range(n+1):
        for j in range(W+1):

            if i == 0 or j == 0:
                cache[i][j] = 0
            elif weights[i - 1] <= j:
                cache[i][j] = max(val[i-1] + cache[i-1][j - weights[i-1]], cache[i-1][j])
            else:
                cache[i][j] = cache[i-1][j]

    return cache[n][W]

# Examples:
value = [60, 100, 120]
weight = [10, 20, 30]
n = len(value)
W = 50
print(knapsack_recursive(value, weight, W, n))
print(knapsack_cached(value, weight, W, n))
