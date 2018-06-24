# You are given coins of different denominations and a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins,
# return -1.

# Example 1:
#
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:
#
# Input: coins = [2], amount = 3
# Output: -1
# Note:
# You may assume that you have an infinite number of each kind of coin.


###########################


def min_amount(coins_arr, amount):
    """
    Function that returns the minimum number of coins required to achieve
    the amount

    Consider for the sake of example
    amount = 10
    coins = [1, 2, 6]

    Answer: 3(6, 2, 2)


    """
    # The iterative relation is:
    # F(i) = min F(i - Cj) + 1
    # where j = 0....n-1 and n is teh total number of coins
    #
    # For instance F(3) = F(2) + F(1) + F(0)

    cache = [0] + [float('inf')] * amount

    # So initilally, the cache will be
    # [0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]

    # Now clacultae cache[i] for all coins
    for coin in coins:
        for i in range(coin, amount + 1):
            cache[i] = min(cache[i], cache[i - coin] + 1)

    if cache[-1] != float('inf'):
        return cache[-1]
    else:
        # this means that there was no such combination
        return -1


# Examples:
coins = [1, 2, 6]
amt = 10
print(min_amount(coins, amt))
