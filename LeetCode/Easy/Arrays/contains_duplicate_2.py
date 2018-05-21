# Given an array of integers and an integer k, find out whether there are two distinct indices
# i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

# Example 1:
# Input: [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: [1,0,1,1], k = 1
# Output: true

# Example 3:
# Input: [1,2,1], k = 0
# Output: false

def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """


    # Insert elements in a dictionary
        # With key value pair being numb -> index

    my_dict = {}

    for i, numb in enumerate(nums):
        if numb in my_dict and i - my_dict[numb] <= k:
            return True

        my_dict[numb] = i

    return False


arr = [1,2,3,1]
k = 3

arr_2 = [1,0,1,1]
k_2 = 1

arr_3 = [1,2,1]
k_3 = 0
print(containsNearbyDuplicate(arr_3, k_3))
