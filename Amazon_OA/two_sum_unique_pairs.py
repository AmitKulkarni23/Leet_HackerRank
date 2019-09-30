# Given an int array nums and an int target, find how many unique pairs in the array such that their sum is equal to target. Return the number of pairs.
#
# Example 1:
#
# Input: nums = [1, 1, 2, 45, 46, 46], target = 47
# Output: 2
# Explanation:
# 1 + 46 = 47
# 2 + 45 = 47
# Example 2:
#
# Input: nums = [1, 1], target = 2
# Output: 1
# Explanation:
# 1 + 1 = 2
# Example 3:
#
# Input: nums = [1, 5, 1, 5], target = 6
# Output: 1
# Explanation:
# [1, 5] and [5, 1] are considered the same.


def unique_pais(nums, target):
    # Time -> O(N)
    # Space -> O(N)
    answer = set()
    comp = set()

    for num in nums:
        c = target - num

        if c in comp:
            # Why are doing a comparison operation?
            # The problem statement says that [1, 5] and [5, 1] are considered the same

            # Therefore we want to add (greater_num, lesser_num) tuple to the set.
            res = (num, c) if num > c else (c, num)

            if res not in answer:
                answer.add(res)

        comp.add(num)

    return len(answer)

# nums = [1, 1, 2, 45, 46, 46]
# target = 47

nums = [1, 5, 1, 5]
target = 6


print(unique_pais(nums, target))