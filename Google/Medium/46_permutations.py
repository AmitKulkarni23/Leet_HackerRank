# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

# Runtime -> 68 ms
def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    # Credits -> https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/

    # Base Cases
    if len(nums) == 0:
        return []

    # There is only 1 permutation possible
    if len(nums) == 1:
        return [nums]

    final_list = []

    for i in range(len(nums)):
        curr_numb = nums[i]

        rem_list = nums[:i] + nums[i+1:]

        for p in permute(rem_list):
            final_list.append([curr_numb] + p)


    return final_list

# Examples:
x = [10, 20, 30]
print(permute(x))


def permuteUtil(nums,result,level):
    if level == len(nums) - 1:
        result.append(nums[:])
        return
    for i in range(level,len(nums)):
        temp = nums[:]
        temp[i],temp[level] = temp[level],temp[i]
        permuteUtil(temp,result,level+1)

def permute_best_leet_code(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = []
    level = 0
    permuteUtil(nums,result,level)
    return result
