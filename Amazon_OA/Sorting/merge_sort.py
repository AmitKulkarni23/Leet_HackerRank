"""
Merge Sort
You recursively divide the given input array into 2 halves. Dividing the array can only be done O(log n) times
Merge Step : Takes 2 arrays as input, compares them and returns a new array as output O(n)

Time Complexity " O(n * log n)
Space Complexity : O(n)
"""


def merge_sort(arr):
    if len(arr) > 1:
        # Recursively divide the array
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        merge(arr, left_half, right_half)


def merge(arr, left_half, right_half):
    left_len, right_len = len(left_half), len(right_half)

    i = j = k = 0

    while i < left_len and j < right_len:
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1

        k += 1

    # Copy left-over elements
    while i < left_len:
        arr[k] = left_half[i]
        k += 1
        i += 1

    while j < right_len:
        arr[k] = right_half[j]
        k += 1
        j += 1


my_array = [17, 6, 3, 24, 14]
merge_sort(my_array)
print(my_array)

