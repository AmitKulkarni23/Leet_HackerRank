# Given a non-empty array of integers, return the third maximum number
# in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

# Example 1:
# Input: [3, 2, 1]
#
# Output: 1
#
# Explanation: The third maximum is 1.

# Example 2:
# Input: [1, 2]
#
# Output: 2
#
# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

# Example 3:
# Input: [2, 2, 3, 1]
#
# Output: 1
#
# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.


def thirdMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n_list = list(set(nums))

    # If the length of the list is less than 3
    # return max of the list
    if len(n_list) < 3:
        return max(n_list)

    max_1, max_2, max_3 = float("-inf"), float("-inf"), float("-inf")
    for i in range(len(n_list)):
        if n_list[i] > max_1:
            max_3 = max_2
            max_2 = max_1
            max_1 = n_list[i]

        elif n_list[i] > max_2:
            max_3 = max_2
            max_2 = n_list[i]

        elif n_list[i] > max_3:
            max_3 = n_list[i]

    return max_3

# Credits : https://leetcode.com/submissions/detail/155135649/
def best_leet_code_sol(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums=set(nums)
    if len(nums)<3: return max(nums)
    a=max(nums)
    nums.remove(a)
    b=max(nums)
    nums.remove(b)
    return max(nums)

print(thirdMax([3, 2, 1]))
print(thirdMax([1, 2]))
print(thirdMax([2, 2, 3, 1]))
print(best_leet_code_sol([2, 2, 3, 1]))
