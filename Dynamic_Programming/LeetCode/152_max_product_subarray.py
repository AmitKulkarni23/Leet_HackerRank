# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# Example 1:
#
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:
#
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


# Time Complexity : O(n)
# Space Complexity: O(1)

# Credits -> https://ide.geeksforgeeks.org/tjPzPrwffG
def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if not nums:
        return 0

    # Initialize varaibles
    max_ending_here = nums[0]
    min_ending_here = nums[0]
    max_so_far = nums[0]

    # Iterate through the array
    for i in range(1, len(nums)):
        max_ele = max(max(max_ending_here * nums[i], min_ending_here * nums[i]), nums[i])
        min_ele = min(min(min_ending_here * nums[i], max_ending_here * nums[i]), nums[i])

        max_so_far = max(max_ele, max_so_far)

        max_ending_here = max_ele
        min_ending_here = min_ele


    return max_so_far

# Examples:
a = [2,3,-2,4]
b = [-2, 0, -1]
print(maxProduct(a))
