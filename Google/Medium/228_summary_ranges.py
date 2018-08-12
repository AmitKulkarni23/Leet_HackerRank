# Given a sorted integer array without duplicates, return the summary of its ranges.
#
# Example 1:
#
# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
# Example 2:
#
# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.

def summaryRanges(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    # Credits -> https://leetcode.com/problems/summary-ranges/solution/
    # A range covers consecutive elements.
    # If two adjacent elements have difference larger than 1,
    # the two elements does not belong to the same range.
    # Time Complexity: O(n)
    # Space COmplexity : O(1)
    
    summary = []

    i = 0
    for j in range(len(nums)):
        if j + 1 < len(nums) and nums[j+1] == nums[j] + 1:
            # They are in the same range
            # Continue
            continue

        if i == j:
            summary.append(str(nums[i]))
        else:
            summary.append(str(nums[i]) + "->" + str(nums[j]))

        i = j + 1
    return summary

# Examples:
input = [0,1,2,4,5,7]
print(summaryRanges(input))
