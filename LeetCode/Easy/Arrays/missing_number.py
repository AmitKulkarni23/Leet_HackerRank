# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# Input: [3,0,1]
# Output: 2

# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8

# TIME LIMIT EXCEEDED
def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums:
        len_of_arr = len(nums)
        for i in range(len_of_arr + 1):
            if i not in nums:
                return i

def best_leet_code_sol(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Design strategy: Sum upto n numbers and then subtract the sum(nums) to get the missing number
    n = len(nums)
    sum_upto_n = n * (n + 1) / 2
    actual_sum = sum(nums)

    return int(sum_upto_n - actual_sum)
# Test Examples
arr = [3, 0, 1]
arr_2 = [9,6,4,2,3,5,7,0,1]
print(missingNumber(arr_2))
