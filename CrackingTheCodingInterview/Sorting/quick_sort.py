"""
Python file which implements the quick sort algorithm
Not: here the pivot element is teh first element of the array
"""


def quick_sort(arr):
    """
    Performs a quick sort on the given array
    :param arr: The array to be sorted
    :return: Sorted array
    """
    quick_sort_helper(arr, 0, len(arr) - 1)


def quick_sort_helper(arr, first, last):
    if first < last:

        # Find the split point
        split_point = partition(arr, first, last)

        # Recusrively call split quick sort algorithm
        quick_sort_helper(arr, first, split_point - 1)
        quick_sort_helper(arr, split_point+1,last)


def partition(arr, first, last):
    """
    Method that returns the actual split point in the arr
    """

    # Making the first element as the pivot element
    pivot = arr[first]

    left_mark = first + 1
    right_mark = last

    finished = False

    while not finished:
        while left_mark <= right_mark and arr[left_mark] <= pivot:
            left_mark += 1

        while left_mark <= right_mark and arr[right_mark] >= pivot:
            right_mark -= 1

        if right_mark < left_mark:
            # We are done here
            finished = True

        else:
            # keep exchanging the values
            temp = arr[left_mark]
            arr[left_mark] = arr[right_mark]
            arr[right_mark] = temp

    # Now exchange the pivot value and the rightmark value
    temp = arr[first]
    arr[first] = arr[right_mark]
    arr[right_mark] = temp

    return right_mark


arr = [43, 32, 47, 16, 24, 89, 0, -1, 11, 2, 4, 3]
quick_sort(arr)
print(arr)