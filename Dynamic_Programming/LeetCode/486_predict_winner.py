# Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.
#
# Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.
#
# Example 1:
# Input: [1, 5, 2]
# Output: False
# Explanation: Initially, player 1 can choose between 1 and 2.
# If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2).
# So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
# Hence, player 1 will never be the winner and you need to return False.


# Example 2:
# Input: [1, 5, 233, 7]
# Output: True
# Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
# Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.


# Note:
# 1 <= length of the array <= 20.
# Any scores in the given array are non-negative integers and will not exceed 10,000,000.
# If the scores of both players are equal, then player 1 is still the winner.


# Explanation:
# After we decide that dp[i][j] saves how much more scores that the first-in-action player
# will get from i to j than the second player, the next step is how we update the
# dp table from one state to the next. Going back to the question, each player can
# pick one number either from the left or the right end of the array.
# Suppose they are picking up numbers from position i to j in the array
# and it is player A's turn to pick the number now. If player
# A picks position i, player A will earn nums[i] score instantly.
# Then player B will choose from i + 1 to j. Please note that dp[i + 1][j] already
# saves how much more score that the first-in-action player will get from i + 1 to j
# than the second player. So it means that player B will eventually earn dp[i + 1][j]
# more score from i + 1 to j than player A. So if player A picks position i,
# eventually player A will get nums[i] - dp[i + 1][j] more score than player B after
# they pick up all numbers. Similarly, if player A picks position j, player A will earn
# nums[j] - dp[i][j - 1] more score than player B after they pick up all numbers.
# Since A is smart, A will always choose the max in those two options, so:
#
#
# dp[i][j] = Math.max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1]);

# However, if you are interviewing with a good company,
# they may challenge you to further improve your code, probably in the aspect of space complexity.
# So far, we are using a n x n matrix so the space complexity is O(n^2).
# It actually can be improved to O(n).
# That can be done by changing our way of filling the table.
# We may use only one dimensional dp[i] and we start to
# fill the table at the bottom right corner where dp[4] = nums[4].
# On the next step, we start to fill the second to the last line,
# where it starts from dp[3] = nums[3].
# Then dp[4] = Math.max(nums[4] - dp[3], nums[3] - dp[4]).
# Then we fill the third to the last line where dp[2] = nums[2] and
# so on... Eventually after we fill the first line and after the filling, dp[4] will be the answer.


# Space Complexity -> O(n ^ 2)
def PredictTheWinner(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    arr_len = len(nums)

    # Create a cache
    cache = [[0 for _ in range(arr_len)] for _ in range(arr_len)]

    # Fill the diagonal elements
    for i in range(arr_len):
        cache[i][i] = nums[i]

    # Fill the cache in top_down approach
    for l in range(1, arr_len):
        for i in range(0, arr_len - l):
            j = i + l
            cache[i][j] = max(nums[i] - cache[i+1][j], nums[j] - cache[i][j-1])

    print(cache)
    return cache[0][arr_len-1] >= 0

# Space Complexity -> O(N)
def PredictTheWinner_ON(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    n = len(nums)

    dp = [0 for _ in range(n)]

    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if i == j:
                dp[i] = nums[i]
            else:
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])

    return dp[n - 1] >= 0



# Examples:
arr = [8, 15, 3, 7]

print(PredictTheWinner(arr))
