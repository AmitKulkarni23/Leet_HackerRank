# Given an integer array, find three numbers whose product is maximum and output the maximum product.

# Example 1:
# Input: [1,2,3]
# Output: 6

# Example 2:
# Input: [1,2,3,4]
# Output: 24
# Given:
# The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].

def maximumProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # Design Strategy :
    # Find 1st max, 2nd max and 3rd max
    # Find 1st min and 2nd min

    # Return max(max1st max * 2nd max * 3rd max, 1st max * 1st min * 2nd min)

    max_1, max_2, max_3 = float("-inf"), float("-inf"), float("-inf")
    min_1, min_2 = float("inf"), float("inf")

    len_of_arr = len(nums)
    # If the lenght of teh given array is 3, tehn simply return teh product
    if len_of_arr == 3:
        return nums[0] * nums[1] * nums[2]

    for i in range(len_of_arr):

        # Replace the 1st max, 2nd max and 3rd max
        if nums[i] > max_1:
            max_3 = max_2
            max_2 = max_1
            max_1 = nums[i]

        # Replace max_2 and max_3
        elif nums[i] > max_2:
            max_3 = max_2
            max_2 = nums[i]

        elif nums[i] > max_3:
            max_3 = nums[i]


        # Updating minimums
        if nums[i] < min_1:
            min_2 = min_1
            min_1 = nums[i]

        elif nums[i] < min_2:
            min_2 = nums[i]


    return max(max_1 * max_2 * max_3, max_1 * min_1 * min_2)

arr = [1,2,3,4]
arr_2 = [1, 4, 3, -6, -7, 0]
print(maximumProduct(arr_2))
