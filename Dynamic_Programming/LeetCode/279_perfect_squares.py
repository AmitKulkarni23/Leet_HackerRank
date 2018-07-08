# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#

def recursive_numSquares(n):
    """
    :type n: int
    :rtype: int
    """
    print("Calling function with n = ", n)
    if n <= 3:
        return n

    res = n

    for x in range(1, n):
        temp = x * x

        if temp > n:
            break

        else:
            res = min(res, 1 + recursive_numSquares(n - temp))


    return res


def numSquares(n):
    """
    :type n: int
    :rtype: int
    """

    # Credits -> https://www.geeksforgeeks.org/minimum-number-of-squares-whose-sum-equals-to-given-number-n/

    # Crete a 1D array
    dp = [0] * (n + 1)

    # Initialize teh first 4 elements for thsi array
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3


    # Now iterate
    for i in range(4, n+1):
        dp[i] = i

        for x in range(1, i+1):
            temp = x * x

            if temp > i:
                break
            else:
                dp[i] = min(dp[i], 1 + dp[i - temp])

    return dp[n]

# Examples
n = 4
# print(recursive_numSquares(n))
print(numSquares(n))
