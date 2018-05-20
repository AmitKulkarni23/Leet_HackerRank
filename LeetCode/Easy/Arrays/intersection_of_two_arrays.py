# Given two arrays, write a function to compute their intersection.
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
#
# Note:
# Each element in the result must be unique.
# The result can be in any order.

# RUNTIME -> 46ms
def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """

    # Design strategy
    # Put all the elements of 1 array in a dictionary, so taht lookup is
    # O(1)

    if nums1 is [] and nums2 is []:
        return []

    # If either one is empty whiel the other is not
    if nums1 is [] and nums2:
        return []

    if nums2 is [] and nums1:
        return []


    my_dict = {}
    final_list = []

    # Put all the elements of nums1 in a dict
    for i in range(len(nums1)):
        # Note the key is the actual number
        if nums1[i] not in my_dict:
            my_dict[nums1[i]] = i

    # Now traverse through nums2 and check if an element is present in the dictionary
    # If yes, append it to the final_list
    for item in nums2:
        if item in my_dict:
            final_list.append(item)

    return list(set(final_list))

# RUN TIME -> 35 ms
def best_leet_code_sol(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    return list(set(nums1) & set(nums2))

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection(nums1, nums2))
