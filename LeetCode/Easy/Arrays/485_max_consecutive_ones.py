#
# Given a binary array, find the maximum number of consecutive 1s in this array.
#
# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
# Note:
#
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000


def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    max_until_now = 0
    inner_max = 0

    for item in nums:
        if item == 1:
            inner_max += 1

        if item == 0:
            max_until_now = max(max_until_now, inner_max)
            inner_max = 0

    return max(max_until_now, inner_max)

arr = [1,1,0,1,1,1,1, 0, 0]
arr_2 = [0, 1, 0]
print(findMaxConsecutiveOnes(arr_2))
