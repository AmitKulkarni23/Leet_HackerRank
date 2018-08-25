# Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.
#
# What is the most number of chunks we could have made?
#
# Example 1:
#
# Input: arr = [4,3,2,1,0]
# Output: 1
# Explanation:
# Splitting into two or more chunks will not return the required result.
# For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
# Example 2:
#
# Input: arr = [1,0,2,3,4]
# Output: 4
# Explanation:
# We can split into two chunks, such as [1, 0], [2, 3, 4].
# However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.

# arr will have length in range [1, 10].
# arr[i] will be a permutation of [0, 1, ..., arr.length - 1].

def maxChunksToSorted(arr):
    """
    :type arr: List[int]
    :rtype: int
    """

    # https://leetcode.com/problems/max-chunks-to-make-sorted/solution/

    # IDEA:
    # 1) We will try to find the smallest left most chunk
    # 2) if the 1st k elements are [0, 1, 2, ....k -1], then this can be broken into k chunks
    # 3) We can check whether k+1 elements chosen from [0, 1, ..., n-1] are [0, 1, ..., k]
    # by checking whether the maximum of that choice is k.

    # Example: [1, 0, 2, 3, 4]
    # [1, 0] -> max(1, 0) = 1 = len([1, 0])


    answer = 0
    my_max = 0

    for ind, item in enumerate(arr):
        my_max = max(my_max, item)

        if my_max == ind:
            answer += 1

    return answer

# Examples:
x = [1, 0, 2, 3, 4]
print(maxChunksToSorted(x))
