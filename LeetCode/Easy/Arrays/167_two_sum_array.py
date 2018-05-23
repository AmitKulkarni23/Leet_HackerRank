# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
#
# Note:
#
# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may not use the same element twice.
# Example:
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """

    # Stratgey: Scan through teh array and subtract the element from teh target

    if len(numbers) < 2:
        return None
        
    my_dict = {}

    for i, item in enumerate(numbers):
            my_dict[item] = i + 1

    print(my_dict)
    for j in range(len(numbers)):
        rem_target = target - numbers[j]

        if rem_target in my_dict:
            return sorted([j + 1, my_dict[rem_target]])

numb = [2,7]
target = 9

print(twoSum(numb, target))
