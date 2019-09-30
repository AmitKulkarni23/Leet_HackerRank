# https://leetcode.com/discuss/interview-question/356960

# Given a list of positive integers nums and an int target, return indices of the two numbers such that they add up to a target - 30.
#
# Conditions:
#
# You will pick exactly 2 numbers.
# You cannot pick the same element twice.
# If you have muliple pairs, select the pair with the largest number.

# Time -> O(N)
# Space -> O(N)


def pair_with_given_sum(nums, target):
    max_num = float("-inf")
    complement_dict = {} # Stores target-nums[i] : i as the key-value pair

    res = [-1, -1]

    for i, num in enumerate(nums):
        if num in complement_dict:
            if num > max_num or nums[complement_dict[num]] > max_num:
                res[0] = complement_dict[num]
                res[1] = i
                max_num = max(num, nums[complement_dict[num]])
        complement_dict[target - num - 30] = i

    return res

a = [20, 50, 40, 25, 30, 10]
print(pair_with_given_sum(a, target=90))

b = [50, 20, 10, 40, 25, 30]
print(pair_with_given_sum(b, target=90))