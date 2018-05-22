# Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
#
# Example 1:
# Input: [1,4,3,2]
#
# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

def arrayPairSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # Strategy: Sort the array and pair teh numbers together.
    # We know that there are even number of elements(2n)

    # NOTE: Instead of finding minumum after sorted, could have just added the
    # all teh even elements using slicing as below
    # return sum(sorted(nums)[::2])

    nums.sort()

    i = 0
    j = 1

    final_sum = 0

    while i <= len(nums) - 2:
        final_sum += min(nums[i], nums[j])
        i = i + 2
        j = i + 1

    return final_sum



arr = [1, 4, 3, 2]
arr_2 = [2, 7, 11, 15, 1, 4]
print(arrayPairSum(arr_2))
