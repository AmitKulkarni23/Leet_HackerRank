# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.
#
# You need to find the shortest such subarray and output its length.
#
# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Note:
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=.

def findUnsortedSubarray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Idea: Create a copy of the array and sort this copy
    # Compare the 2 arrays
    # Find teh leftmost and rightmost mismatch

    nums_copy = nums[:]
    start = len(nums)
    end = 0

    nums_copy.sort()

    for i in range(len(nums)):
        if nums[i] != nums_copy[i]:
            start = min(i, start)
            end = max(end, i)

    if (end - start) >= 0:
        return end - start + 1
    else:
        return 0

# Test Examples
arr = [2, 6, 4, 8, 10, 9, 15]
arr_2 = [1, 3, 2]
print(findUnsortedSubarray(arr))
