# Given an array of n positive integers.
# Write a program to find the sum of maximum sum subsequence of the given array such that the intgers in
# the subsequence are sorted in increasing order. For example, if input is {1, 101, 2, 3, 100, 4, 5},
# then output should be 106 (1 + 2 + 3 + 100),
# if the input array is {3, 4, 5, 10}, then output should be 22 (3 + 4 + 5 + 10) and
# if the input array is {10, 5, 4, 3}, then output should be 10

# Source -> https://www.geeksforgeeks.org/dynamic-programming-set-14-maximum-sum-increasing-subsequence/

def max_sum_incr_subseq(arr):
    """
    Function that returns  the sum of teh maximum sum increasing subsequence of
    the given array

    Example:
    max_sum_incr_subseq([1, 101, 2, 3, 100, 4, 5] ) -> 106
    """

    # Copy/ Clone the entire array into a different array
    msis = arr[:]

    # Iterate through the arr
    for i in range(1, len(arr)):
        for j in range(i):
            # Do what?
            # Compare the elements
            # Then check the sum
            if arr[j] < arr[i] and msis[i] < msis[j] + arr[i]:
                # Then update
                msis[i] = msis[j] + arr[i]

    # Return the max value in msis array
    return max(msis)

# Test Examples:
arr = [1, 101, 2, 3, 100, 4, 5]
arr_2 = [3, 4, 5, 10]
print("MSIS is ", max_sum_incr_subseq(arr_2))
