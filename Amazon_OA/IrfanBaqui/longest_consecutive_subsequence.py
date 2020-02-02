# You are given an array of integers.
# Find the lenght of the longest consecutive subsequence in that array

# Eg: [2, 1, 6, 9, 4, 3]
# Ouput : 4 -> becuause of the subsequence [1, 2, 3, 4]

# Time Complexity - O(n)
# Note: The below implementation only goes through the next element if the
# element is the first one. For example: [1, 2, 3, 4, 8, 9]
# This will go into the if branch for only 1 and 8.
# Therefore, it checks only n elements.

# Space Complexity - O(1)

def lcs(arr):
    numb_dict = {}
    longest = 0

    for num in arr:
        numb_dict[num] = True

    for num in numb_dict:
        if num - 1 not in numb_dict:
            count = 0
            curr = num

            while curr in numb_dict:
                count += 1
                curr += 1

            longest = max(longest, count)

    return longest


# Example
arr = [2, 1, 6, 9, 4, 3, 5, 6]
print(lcs(arr))
