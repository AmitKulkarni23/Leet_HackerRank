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
