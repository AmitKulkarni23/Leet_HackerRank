# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# Your algorithm should run in O(n) complexity.
#
# Example:
#
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # Credits -> https://leetcode.com/problems/longest-consecutive-sequence/solution/
    # Time Complexity -> O(n)
    # Space COmplexity -> O(n) for set
    # Note : set() is implemented as a hashtable in Python
    # lookups are O(1) on avarage

    answer = 0
    num_set = set(nums)

    for item in num_set:
        if item - 1 not in num_set:
            current_streak = 1
            current_num = item


            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            answer = max(answer, current_streak)

    return answer

# Examples:
input = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(input))
