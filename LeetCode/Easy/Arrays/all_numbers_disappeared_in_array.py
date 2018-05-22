# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]

def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # Credits :https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/128815/Simple-and-efficient-python3-code!

    # Create a final_list( that will be returnde) initialized with all numbers
    # from 1 to len(nums)

    final_list = set(list(range(1, len(nums) + 1)))

    # Now scan through the nums array and discard numbers from the final_list,
    # all those numbers which are present in the nums array

    for item in nums:
        final_list.discard(item)

    # Finally return the list
    return list(final_list)



# Examples:
arr = [1, 2, 4, 4]
print(findDisappearedNumbers(arr))
