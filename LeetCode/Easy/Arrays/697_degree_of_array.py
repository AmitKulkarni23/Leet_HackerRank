# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
#
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
#
# Example 1:
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation:
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:
# Input: [1,2,2,3,1,4,2]
# Output: 6

# Idea -> An array that has degree d, must have some element x occur d times. If some subarray has the same degree, then some element x (that occured d times), still occurs d times. The shortest such subarray would be from the first occurrence of x until the last occurrence.

# For each element in the given array,
# let's know left, the index of its first occurrence;
# and right, the index of its last occurrence.
# For example, with nums = [1,2,3,2,5] we have left[2] = 1 and right[2] = 3.
#
# Then, for each element x that occurs the maximum number of times,
# right[x] - left[x] + 1 will be our candidate answer,
# and we'll take the minimum of those candidates.


def findShortestSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # Credits -> https://leetcode.com/problems/degree-of-an-array/solution/

    # Time Complexity -> O(N)
    # Space COmplexity -> O(N)

    # Create three dictionaries to maintain left index, right index and count of the array
    left = {}
    right = {}
    count = {}

    # Itearte through the array

    for i, item in enumerate(nums):
        # Store the first occurrence in the left array
        if item not in left:
            left[item] = i

        # Store the last occurrence in the right dict
        right[item] = i

        # Increment the count by 1
        count[item] = count.get(item, 0) + 1

    # Now we have created the three dictionaries
    # Get the degree of the array

    arr_len = len(nums)
    deg_arr = max(count.values())

    for item in count:
        if count[item] == deg_arr:
            # We will take the minimum
            arr_len = min(arr_len, right[item] - left[item] + 1)

    return arr_len
