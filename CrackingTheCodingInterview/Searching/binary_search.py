"""
Python file which implements binary search algorithm
"""


def binary_search(arr, item):
    """
    Function that searches for the given item in the given arr
    :param arr: The arr to search the item in
    :param item: The item to search for in the array
    :return: True iff the item is found
    """

    first = 0
    last = len(arr) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if arr[mid] == item:
            found = True
        else:
            if item < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found

# Note arr should be sorted for binary search to work
arr = [-10, -2, 1, 4, 17, 19, 23]
print(binary_search(arr, 23))