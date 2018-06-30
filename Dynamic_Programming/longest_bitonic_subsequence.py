# Given an array arr[0 … n-1] containing n positive integers, a subsequence of arr[] is
# called Bitonic if it is first increasing,
# then decreasing.
# Write a function that takes an array as argument
# and returns the length of the longest bitonic subsequence.
# A sequence, sorted in increasing order is considered Bitonic with
# the decreasing part as empty. Similarly, decreasing order sequence is considered
# Bitonic with the increasing part as empty.

# Examples:
# Input arr[] = {1, 11, 2, 10, 4, 5, 2, 1};
# Output: 6 (A Longest Bitonic Subsequence of length 6 is 1, 2, 10, 4, 2, 1)
#
# Input arr[] = {12, 11, 40, 5, 3, 1}
# Output: 5 (A Longest Bitonic Subsequence of length 5 is 12, 11, 5, 3, 1)
#
# Input arr[] = {80, 60, 30, 40, 20, 10}
# Output: 5 (A Longest Bitonic Subsequence of length 5 is 80, 60, 30, 20, 10)


# Idea -> Similar to LIS problem
# We will create 2 lists
# lis -> Longest increasing Subsequence
# lds -> Longest Decreasing Subsequence
#
# and we will finally return lis[i] + lds[i] - 1

# Why -1? -> Because the end of teh lis array and teh beginning of teh lds array are counted twice

###############################################

def bitonic_seq(arr):
    """
    Function that returns the lenght of teh maximum bitonic sequence in the given array
    """

    n = len(arr)

    lis = [1] * n
    lds = [1] * n

    # Update lis array
    for i in range(1, n):
        for j in range(i):
            # Compare and update
            if arr[j] < arr[i] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    # Now update lds array
    for i in reversed(range(n-1)):
        for j in reversed(range(i-1, n)):
            if arr[j] < arr[i] and lds[i] < lds[j] + 1:
                lds[i] = lds[j] + 1

    # Now return
    max_val = lis[0] + lds[0] - 1
    for i in range(1, n):
        max_val = max((lis[i] + lds[i] - 1), max_val)

    return max_val

# Test examples:
arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5,13, 3, 11, 7, 15]
print("Bitonic Lenght is", bitonic_seq(arr))
