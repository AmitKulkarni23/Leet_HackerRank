# Given an array of random numbers. Find longest increasing subsequence (LIS) in the array.

# Algorithm:
# 1. If A[i] is smallest among all end
#    candidates of active lists, we will start
#    new active list of length 1.
# 2. If A[i] is largest among all end candidates of
#   active lists, we will clone the largest active
#   list, and extend it by A[i].
#
# 3. If A[i] is in between, we will find a list with
#   largest end element that is smaller than A[i].
#   Clone and extend this list by A[i]. We will discard all
#   other lists of same length as that of this modified list.

# Time Complexity: W eare itearting through N elements in the array
# Worst Case -> We are calling the get_ceil_index function for all teh N elements
# get_ceil_index -> binary search -> logn

# Therefore -> Time Complexity = O(n logn)

def longest_increasing_sub_seq(A):
    """
    Function to find the longest increasing subsequence in an array
    """

    # boundary cases

    # The lenght the of the given list
    arr_len = len(A)

    if arr_len <= 1:
        return arr_len

    # Create an auxiliary array that will hold the "end elements"
    # of the intermeditae LIS' that we will be creating

    aux_array = [0 for _ in range(arr_len + 1)]

    # Initialize aux_array[0] = A[0]
    aux_array[0] = A[0]

    # l acts as our pointer, always points to an empty slot
    l = 1

    # Now iterate through the array
    for i in range(1, arr_len):
        if A[i] < aux_array[0]:
            # This is the new smallest value
            # Replace aux_array[0] = A[i]

            # i.e we are starting over again, creating a new active list of lenght 1
            # Case 1
            aux_array[0] = A[i]

        elif A[i] > aux_array[l - 1]:
            # Case 2: A[i] is largets among all active lists
            aux_array[l] = A[i]
            l += 1

        else:
            # Case 3
            # A[i] is in between
            # A[i] wants to be current end candidate of an existing subsequence
            index = get_ceil_index(-1, l - 1, A[i], aux_array)
            aux_array[index] = A[i]


    return l


def get_ceil_index(left, right, key, A):
    """
    Function that returns the ceil index of an array
    """
    while right - left > 1:
        mid = left + ( right - left) // 2

        if A[mid] >= key:
            right = mid
        else:
            left = mid


    return right


# Examples:
A = [ 0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15 ]
print("The lenght of LIS is ", longest_increasing_sub_seq(A))
