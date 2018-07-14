# You have a number of envelopes with widths and heights given as a pair of integers (w, h).
# One envelope can fit into another if and only if both the width and height of one envelope
# is greater than the width and height of the other envelope.
#
# What is the maximum number of envelopes can you Russian doll? (put one inside other)
#
# Example:
# Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes
# you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).


def maxEnvelopes(envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """
    # Idea Credits -> https://leetcode.com/problems/russian-doll-envelopes/discuss/82763/Java-NLogN-Solution-with-Explanation
    # Longest Increasing Subsequence -> O(nlogn) -> https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
    # Time COmplexity -> O(n logn)

    if not envelopes or not envelopes[0]:
        return 0

     # We will do in-pace sorting
     # First sort the heights in reverse order
    envelopes.sort(key=custom_comparator_heights, reverse=True)

    # Then sort the envelopes in ascending order of heights
    envelopes.sort(key=custom_comparator_width)

    # Now we have to perform LIS on the heights
    heights_list = []
    for item in envelopes:
        heights_list.append(item[1])

    return longest_increasing_sub_seq(heights_list)

def custom_comparator_heights(item):
    """
    Function that acts as a Comparator for sorting
    """
    return item[1]

def custom_comparator_width(item):
    return item[0]


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

# Examples
env = [[5,4],[6,4],[6,7],[2,3]]
print(maxEnvelopes(env))
