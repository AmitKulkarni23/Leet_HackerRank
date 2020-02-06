# Given an array with +ve and -ve integers, what is the maximum
# contiguous subarray sum?

# Time: O(n)
# Space: O(1)
def max_contiguous_subarray_sum(arr):
    max_ending_here = arr[0]
    max_so_far = arr[0]

    for i in range(1, len(arr)):
        max_ending_here = max(max_ending_here + arr[i], arr[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_contiguous_subarray_sum(arr))
