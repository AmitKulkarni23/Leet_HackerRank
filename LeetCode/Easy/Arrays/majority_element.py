# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.


# Examples:
# Input: [3,2,3]
# Output: 3

# Input: [2,2,1,1,1,2,2]
# Output: 2
def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    floor_count = len(nums) // 2
    my_dict = {}

    # Iterate through the array and stroe the occurrence count in a dictionary
    for item in nums:
        if item in my_dict:
            # Increment teh occurrence count for this element
            my_dict[item] += 1
        else:
            # Set the count of this number to be 1
            my_dict[item] = 1

        # Check if the occurrence count has exceeded teh floor_count
        if my_dict[item] > floor_count:
            # We have found teh majority element
            return item

# Time Complexity: O(n)
# Space Complexity: O(1)
def best_leet_code_sol(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums_set = set(nums)

    for item in nums_set:
        if nums.count(item) > len(nums) // 2:
            return item

arr = [2,2,1,1,1,2,2]
arr_2 = [3,2,3]
print(majorityElement(arr))
print(best_leet_code_sol(arr))
