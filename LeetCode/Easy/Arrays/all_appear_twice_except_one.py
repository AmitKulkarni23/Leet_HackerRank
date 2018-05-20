# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Input: [2,2,1]
# Output: 1

# Input: [4,1,2,1,2]
# Output: 4

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Inspired by: https://leetcode.com/problems/single-number/solution/
    
    # Design strategy: use XOR
    # If we take XOR of zero and some bit, it will return that bit
    # a xor a = a

    # If we take XOR of two same bits, it will return 0
    # a xor a = 0

    # Therefore a xor a xor b = a xor a xor b = b
    a = 0

    for item in nums:
        a = a ^ item

    # Finally return a
    return a

print(singleNumber([4,1,2,1,2]))
