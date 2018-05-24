# In a given integer array nums, there is always exactly one largest element.
#
# Find whether the largest element in the array is at least twice as much as every other number in the array.
#
# If it is, return the index of the largest element, otherwise return -1.


# Input: nums = [3, 6, 1, 0]
# Output: 1
# Explanation: 6 is the largest integer, and for every other number in the array x,
# 6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
#
#
# Example 2:
#
# Input: nums = [1, 2, 3, 4]
# Output: -1
# Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.

#Runtime : 40ms
def dominantIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if len(nums) == 1:
        return 0

    max_num = max(nums)

    for item in nums:
        if 2 * item > max_num and item != max_num:
            return -1

    return nums.index(max_num)

#Runtime : 35ms
def best_leet_code_sol(nums):
    """
    :type nums: List[int]
    :rtype: int
    """:
    if not nums:
            return -1
        if len(nums) == 1:
            return 0

        maxNum = max(nums)
        maxIndex = nums.index(maxNum)
        nums.remove(maxNum)
        if maxNum >= 2 * max(nums):
            return maxIndex
        return -1


# Examples:
arr = [1, 2, 3, 4]
print(dominantIndex(arr))
