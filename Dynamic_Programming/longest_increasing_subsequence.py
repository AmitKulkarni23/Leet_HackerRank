# Find the length of the longest subsequence of a given sequence
# such that all elements of the subsequence are sorted in increasing order.

# Examples:
# Input  : arr[] = {3, 10, 2, 1, 20}
# Output : Length of LIS = 3
# The longest increasing subsequence is 3, 10, 20
#
# Input  : arr[] = {3, 2}
# Output : Length of LIS = 1
# The longest increasing subsequences are {3} and {2}
#
# Input : arr[] = {50, 3, 10, 7, 40, 80}
# Output : Length of LIS = 4
# The longest increasing subsequence is {3, 7, 40, 80}


#####################


def lis(D):
    """
    Function that returns teh lenght of teh longest increasing subsequence of
    the array

    arr: list
    """

    if len(D) == 1:
        return 1

    # Create another 2-D array L

    # So the recursive relation that we will be using is as follows:
    # L[i] = max(L[j] | j < i and D[j] < D[i]) + "D[i]"

    L = [1] * len(D)



    # Now iterate through the given D array
    for i in range(1, len(D)):
        for j in range(i):

            # We will only append to L[i]if  D[j] < D[i]
            # That is the tail element(the last element) of D[j] < D[i]

            if D[j] < D[i] and L[i] < L[j] + 1:
                L[i] = L[j] + 1

    return max(L)


# D = [3, 2, 6, 4, 5]
D = [10, 22, 9, 33, 21, 50, 41, 60]
print(lis(D))
