# The set S originally contains numbers from 1 to n. But unfortunately,
# due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

#
# Given an array nums representing the data status of this set after the error.
# Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

#
# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]

# Note:
# The given array size will in the range [2, 10000].
# The given array's numbers won't have any order.

def findErrorNums(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # Create a dictionary
    my_dict = {}
    output_list = [0] * 2

    new_list = [i for i in range(1, len(nums) + 1)]

    for i in range(len(nums)):
        if nums[i] in my_dict:
            output_list[0] = nums[i]
        else:
            my_dict[nums[i]] = 1

    output_list[1] = list(set(new_list) - set(nums))[0]
    return output_list

def best_leet_code_sol(nums):
    """
    """
    # Credits -> https://leetcode.com/submissions/detail/163683924/
    Sum,n=sum(nums),len(nums)
    valid=set(nums)
    return [Sum-sum(valid),(n*(n+1)/2)-sum(valid)]

my_list = [1, 2, 3, 4, 4, 5]
# my_list = [1, 1]
print(findErrorNums(my_list))
