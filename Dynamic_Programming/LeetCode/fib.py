
def fibonacci(n):
    """
    The nth fibonacci number using iterative approach
    """
    # Memoization
    memo = {}

    # Initilaize memo elements
    memo[0] = 0
    memo[1] = 1

    # Return teh appropriate fibonacci number
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]


print(fibonacci(6))
