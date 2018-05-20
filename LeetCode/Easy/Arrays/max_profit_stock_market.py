# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Note that you cannot sell a stock before you buy one.

# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # Inspired by : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/131442/python-code-beats-99
    buyin = float('inf')
    profit = 0

    # We need to minimize the buyin and maximize the profit
    for i in range(len(prices))  :
        if prices[i] < buyin:
            buyin = prices[i]
        elif prices[i] - buyin > profit:
            profit = prices[i] - buyin
    return profit

def best_sol_leetcode(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
            return 0
        buy = prices[0]
        res = 0
        for p in prices:
            if p > buy:
                res = max(res, p-buy)
            else:
                buy = p
        return res

# Examples
my_array = [7,1,5,3,6,4]
my_array_2 = [7,6,4,3,1]
m3 = [2, 4, 1]
print(maxProfit(my_array_2))
