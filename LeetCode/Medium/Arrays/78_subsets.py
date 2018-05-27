# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # Refer to: https://www.hackerearth.com/practice/notes/bit-manipulation/
    fina_list = []
    # We know that there are total of 2 ^ n subsets possible
    for i in range(2 ** len(nums)):
        inter= []
        for j, num in enumerate(nums):
            if i & (1 << j):
                inter.append(num)
        fina_list.append(inter)
    return fina_list

# Test Examples
nums = [1,2,3]
print(subsets(nums))
