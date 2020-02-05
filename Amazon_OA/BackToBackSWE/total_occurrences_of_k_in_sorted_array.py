# Total Occurrences of K in a Sorted Array

# Approach: Do 2 binary searches
# Time: O(logn)
# Space: O(logn) recursive stack space.

def get_total_occurrences_of_k(arr, k):
    first_occurrence = binary_search(arr, k , 0, len(arr) - 1, "FIRST")

    if first_occurrence == -1:
        return 0

    last_occurrence = binary_search(arr, k , 0, len(arr) - 1, "LAST")

    return last_occurrence - first_occurrence + 1

def binary_search(arr, k, left, right, type):
    if len(arr) == 0 or left > right:
        return -1

    mid = left + (right - left) // 2
    if arr[mid] == k:
        if type == "FIRST":
            # If the item to the left of us is the same as us,
            # go search left
            if mid - 1 >= 0 and arr[mid] == arr[mid - 1]:
                return binary_search(arr, k , left, mid - 1, type)
        if type == "LAST":
            # If the item to the right of us is the same as us,
            # go search right
            if mid - 1 < len(arr) and arr[mid] == arr[mid + 1]:
                return binary_search(arr, k , mid + 1, right, type)

        # We have found the first or lasty occurrence of the item
        return mid
    elif arr[mid] < k:
        return binary_search(arr, k, mid + 1, right, type)
    else:
        return binary_search(arr, k, left, mid - 1, type)

    return -1

arr = [1, 1, 1, 2, 3]
print(get_total_occurrences_of_k(arr, 1))
