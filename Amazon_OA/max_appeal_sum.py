# https://leetcode.com/discuss/interview-question/355698

# Find pair with maximum Appeal value.
#
# Input: Array
# Output: index {i, j} ( i = j allowed) with maximum Appeal
# Appeal = A[i] +A[j] + abs(i-j)
#
# Example 1:
#
# Input: [1, 3, -1]
# Output: [1, 1]
# Explanation: Appeal = A[1] + A[1] + abs(0) = 3 + 3 + 0 = 6
# Example 2:
#
# Input: [1, 6, 1, 1, 1, 1, 7]
# Output: [1, 6]
# Explanation 6 + 7 + abs(1 - 6) = 18
# Example 3:
#
# Input: [6, 2, 7, 4, 4, 1, 6]
# Output: [0, 6]

# Explanation: 6 + 6 + abs(0 - 6) = 18

# Solution Credits -> https://leetcode.com/playground/EFw7cewr


###############################

def max_appeal_sum(arr):
    left, right = 0, 0
    max_val = float("-inf")

    # left to right
    for i, num in enumerate(arr):
        value = num - i
        if value > max_val:
            left = i
            max_val = value

    # Right to left
    max_val = float("-inf")
    for i in range(len(arr) - 1, -1, -1):
        value = arr[i] - (len(arr) -1 - i)
        if value > max_val:
            right = i
            max_val = value

    return [left, right]


input = [1, 3, -1]
print(max_appeal_sum(input))

arr2 = [1, 6, 1, 1, 1, 1, 7]
print(max_appeal_sum(arr2))

arr3 = [6, 2, 7, 4, 4, 1, 6]
print(max_appeal_sum(arr3))
