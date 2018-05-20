"""
Given an array and a value, remove all instances of that value in-place and return the new length.

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

"""

def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """

    if not nums:
        # If the nums array is empty
        return 0

    prev_ind = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[prev_ind] = nums[i]
            prev_ind += 1

    return prev_ind

nums = [3,2,2,3]
val = 3

print(removeElement(nums, val))
print(nums)
