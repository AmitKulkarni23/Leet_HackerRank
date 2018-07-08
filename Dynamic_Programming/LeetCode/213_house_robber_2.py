# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
#
# Example 1:
#
# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
#              because they are adjacent houses.
# Example 2:
#
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.


def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Corner cases
    arr_len = len(nums)
    if arr_len == 0:
        # No houses to rob
        return 0

    if arr_len == 1:
        # Only 1 house to rob
        return nums[0]

    if arr_len <= 3:
        return max(nums)


    # The first house is robbed or not is constrained by the last house
    # Both 1st and last houses cannot be robbed

    # Call helper function including first and excluding second
    first_include = rob_helper(nums[:len(nums) - 1])

    # Call helper function excluding the first house and including the last house
    last_include = rob_helper(nums[1:])

    # Return the max of these 2
    return max(first_include, last_include)

def rob_helper(nums):
    """
    A helper function
    """
    arr_len = len(nums)
    # Create a 1d array
    val = [0, 0, 0]

    val[0] = nums[0]
    val[1] = max(nums[0], nums[1])

    for i in range(2, arr_len):
        val[2] = max(nums[i] + val[0], val[1])

        val[0], val[1] = val[1], val[2]

    return val[2]


# Examples:
input = [2,3,2]
input_2 = [1,2,3,1]
input_3 = [1]
input_4 = [2,3,2]
print(rob(input_4))
