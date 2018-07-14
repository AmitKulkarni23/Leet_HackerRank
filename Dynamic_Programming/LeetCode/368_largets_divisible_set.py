# Given a set of distinct positive integers, find the largest subset such that
# every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.
#
# If there are multiple solutions, return any subset is fine.
#
# Example 1:
#
# nums: [1,2,3]
#
# Result: [1,2] (of course, [1,3] will also be ok)
# Example 2:
#
# nums: [1,2,4,8]
#
# Result: [1,2,4,8]


def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    # Credits -> https://leetcode.com/problems/largest-divisible-subset/discuss/83998/C++-Solution-with-Explanations
    # @meng.careers

    result = []
    if len(nums) == 0:
        return result

    if len(nums) == 1:
        result.append(nums[0])
        return result

    # Sort the nums array
    nums.sort()

    # Create a cache
    dp = [0] * len(nums)

    # Create another parent array
    parent = [-1] * len(nums)

    # Initialize 2 variables
    largest = 0
    largest_at = 0

    dp[0] = 1

    for j in range(1, len(dp)):
        dp[j] = 1
        for i in range(j-1, -1, -1):
            if nums[j] % nums[i] == 0 and dp[j] < dp[i] + 1:
                dp[j] = dp[i] + 1
                parent[j] = i

        if dp[j]> largest:
            largest = dp[j]
            largest_at = j
            
    for i in range(largest):
        result = [nums[largest_at]] + result
        largest_at = parent[largest_at]

    # print(dp)
    return result

# Examples
# arr = [1,2,4, 5, 8, 16, 32]
# arr = [1]
arr = [2,3,4,9,8]
print(largestDivisibleSubset(arr))
