# Program for array rotation
# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.

# Example:
# a = [1, 2, 3, 4, 5, 6, 7]
#
# rotate(a, 2, 7 ) => a = [3, 4, 5, 6, 7, 1, 2]


# My method
import time
def rotate(arr, d, n):
    """
    Function to rotate an array arr, of size n by d elements
    """

    if arr and d <= n:
        arr = arr[d:] + arr[:d]

    return arr

# Example
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
d = 2
n = len(arr)


new_arr = rotate(arr, d, n)
print(new_arr)
