# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
#
# Example 1:
#
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.
# Example 2:
#
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.


def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # Credits -> https://leetcode.com/problems/house-robber/discuss/146633/Python-DP
    arr_len = len(nums)

    if arr_len == 0:
        # No elements in the array
        return 0

    if arr_len == 1:
        # Only one element
        return nums[0]

    if arr_len == 2:
        # If there are 2 elements
        return max(nums)

    # Else create an array of lenght = 3
    my_arr = [0, 0, 0]
    my_arr[0] = nums[0]
    my_arr[1] = max(nums[0], nums[1])

    for i in range(2, arr_len):
        # get the maximum robbery
        my_arr[2] = max(my_arr[0] + nums[i], my_arr[1])

        # now swap
        my_arr[0], my_arr[1] = my_arr[1], my_arr[2]


    return my_arr[2]

# Examples:
houses = [1,2,3,1]
houses_2 = [2,7,9,3,1]
houses_3 = [2, 1, 1, 2]
print(rob(houses_3))
