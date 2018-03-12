"""
Python file to implement the merge sort algorithm
"""


def merge_sort(arr):
    """
    Recursive function that divides the array and merges them
    :param arr: the array to sort
    :param left: the left index
    :param right: the right index
    :return:
    """

    if len(arr) > 1:
        # Recursively call this function to the left half of the array and the
        # the right half of the array

        # Calculating the midpoint
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        merge(arr, left_half, right_half)


def merge(arr, left_half, right_half):
    """
    The actual merge function which checks compares 2 elements and does the merging
    :return: Nothing
    """
    left_len = len(left_half)
    right_len = len(right_half)

    # Merge the 2 temp arrays back into the arr
    i, j, k = 0, 0, 0

    while i < left_len and j < right_len:
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1

        k += 1

    # If there are any remaining elements in l_arr copy them
    while i < left_len:
        arr[k] = left_half[i]
        k += 1
        i += 1

    # If there are any remaining elements in the r_arr copy them
    while j < right_len:
        arr[k] = right_half[j]
        k += 1
        j += 1


arr = [10, 19, 7, 5, 2, 12, 14, -1, 0]
merge_sort(arr)

print(arr)
