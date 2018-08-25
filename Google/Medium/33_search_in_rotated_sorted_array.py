# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    num_len = len(nums)

    pivot = find_pivot_index(nums, 0, num_len - 1)

    if pivot == -1:
        # The array was not sorted at all
        return binary_search(nums, 0, num_len - 1, target)


    # Check against pivot index itself
    if nums[pivot] == target:
        return pivot

    if nums[0] <= target:
        return binary_search(nums, 0, pivot - 1, target)

    return binary_search(nums, pivot + 1, num_len - 1, target)


def find_pivot_index(nums, low, high):
    """
    Helper function which returns the index of the pivot element in
    sorted rotated array
    """

    if high < low:
        return -1

    if high == low:
        return low

    mid = (high + low) // 2

    if mid < high and  nums[mid] > nums[mid + 1]:
        return mid

    if mid > low and nums[mid] < nums[mid - 1]:
        return mid - 1

    if nums[low] >= nums[mid]:
        return find_pivot_index(nums, low, mid - 1)

    return find_pivot_index(nums, mid + 1, high)


def binary_search(nums, low, high, target):
    """
    Function that actually performs the binary search
    """

    if high < low:
        return -1

    mid = (high + low) // 2

    if nums[mid] == target:
        return mid

    if nums[mid] < target:
        return binary_search(nums, mid + 1, high, target)

    return binary_search(nums, low, mid - 1, target)


# Examples:
arr = [4,5,6,7,0,1,2]
target = 18
print(search(arr, target))
