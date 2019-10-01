# https://leetcode.com/discuss/interview-question/373202
# Solution Credits -> https://leetcode.com/discuss/interview-question/373202 by user tomaling


# Approach: Sort the lists a & b by their values
# We will use 2 pointers here, left and right so that we traverse both the arrays only once.
# left = 0 # For traversing list a from left to right
# right = len(b) - 1 # for traversing list a from right to left

# Maintain a currDiff:
# currDiff = target - i - j; where i & j are the value fields in a[left] and b[right]
# This currDiff will always be the closest to the target
# If we wind a currDiff that is closer to the target; clear the answer list and add the id fields of a[left] and a[right]

# if target - i - j == currDiff:
#     append to answer


# Move in the forward direction when target > i + j
# Move in the reverse direction when target < i + j
# if target == i + j
    # Capture the left pointer in a temp variable
    # Continue appending a[left][0], a[right][0] and incrementing the left pointer


def findPairs(a, b, target):
    a.sort(key=lambda x: x[1])
    b.sort(key=lambda x: x[1])
    l, r = 0, len(b) - 1
    ans = []
    curDiff = float('inf')
    while l < len(a) and r >= 0:
        id1, i = a[l]
        id2, j = b[r]
        if (target - i - j == curDiff):
            ans.append([id1, id2])
        elif (i + j <= target and target - i - j < curDiff):
            ans.clear()
            ans.append([id1, id2])
            curDiff = target - i - j
        if (target > i + j):
            l += 1
        else:
            if target == i + j:
                tmp_l = l
                while a[tmp_l][1] + b[r][1] == target:
                    tmp_l += 1
                    if tmp_l == len(a):
                        break
                    if a[tmp_l][1] + b[r][1] == target:
                        ans.append([a[tmp_l][0], b[r][0]])
            r -= 1

    ans.sort(key=lambda x: x[1])
    ans.sort(key=lambda x: x[0])
    return ans


# test 1
a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7
expected = [[2, 1]]
assert findPairs(a, b, target) == expected

# test 2
a = [[1, 8], [2, 7], [3, 14]]
b = [[1, 5], [2, 10], [3, 14]]
target = 20
expected = [[3, 1]]
assert findPairs(a, b, target) == expected

# test 3
a = [[1, 8], [2, 15], [3, 9]]
b = [[1, 8], [2, 11], [3, 12]]
target = 20
expected = [[1, 3], [3, 2]]
assert findPairs(a, b, target) == expected

# test 4
a = [[1, 5], [2, 5]]
b = [[1, 5], [2, 5]]
target = 10
expected = [[1, 1], [1, 2], [2, 1], [2, 2]]
assert findPairs(a, b, target) == expected