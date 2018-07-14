# We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.
#
# Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.
#
# Example 1:
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].

# Time COmplexity -> O(n)
# Space Complexity -> O(n)
import collections
def findLHS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Credits -> https://leetcode.com/problems/longest-harmonious-subsequence/solution/
    if not nums:
        return 0

    res = 0

    # Create a dictionary
    my_dict = {}

    for item in nums:
        if item in my_dict:
            my_dict[item] += 1
        else:
            my_dict[item] = 1

        if (item + 1) in my_dict:
            res = max(res, my_dict[item] + my_dict[item + 1])

        if (item - 1) in my_dict:
            res = max(res, my_dict[item] + my_dict[item - 1])

    return res

nums = [1,3,2,2,5,2,3,7, 8, 8, 8, 8, 8, 7, 7, 7]
print(findLHS(nums))
