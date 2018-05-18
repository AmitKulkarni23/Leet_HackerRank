# Program to search for an element in a sorted and rotated array
# Note : An element can be found in a sorted array in O(log n) time
# But suppose a sorted ascending array is rotated at an unknown pivot point
# before-hand. Seacrh and find an element in O(log n) time

#  Strategy
# Idea : Find teh pivot point / element, divide the array into 2 subarrays
# and call binary -search. But how to find teh pivot element?
# Pivot element is the element for which teh next element to it is smaller
# than it.

# Examples:
# arr = [3, 4, 5, 1, 2]
# key = 1
# Output : 3


# Credits : geek for Geeks -> https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

def binary_search(low, high, arr, search_key):
    """
    Function that implements the binary search
    """

    if high < low:
        return -1

    mid = int((low + high) / 2)

    if arr[mid] == search_key:
        return mid

    if search_key > arr[mid]:
        return binary_search(mid+1, high, arr, search_key)

    # Condition when key < arr[mid]
    return binary_search(low, mid - 1, arr, search_key)

def find_pivot_element(low, high, arr):
    """
    Function to find teh pivot element in a given array
    """

    if high < low:
        print("No such pivot element")
        return -1
    if high == low:
        return low

    mid = int((low + high) / 2)

    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid -1]:
        return mid - 1

    if arr[low] >= arr[mid]:
        return find_pivot_element(low, mid - 1, arr)

    return find_pivot_element(mid + 1, high, arr)



def search_ele_sorted_rotated_arr(arr, search_key):
    """
    Function to find the index of the search_key in the sorted rotated array
    """

    if arr:
        pivot_index = find_pivot_element(0, len(arr) - 1, arr)

        print("The pivot index is ", pivot_index)
        if pivot_index == -1:
            # This means that the arry is not rotated at all
            return binary_search(0, len(arr) - 1, arr, search_key)

        # ELse, teh array is rotated
        if arr[pivot_index] == search_key:
            return pivot_index

        if arr[0] <= search_key:
            return binary_search(0, pivot_index - 1, arr, search_key)

        return binary_search(pivot_index + 1, len(arr) - 1, arr, search_key)

# Example 1
arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
search_key = 3
print(search_ele_sorted_rotated_arr(arr, search_key))


# Example 2
arr_2 = [30, 40, 50, 10, 20]
search_key_2 = 10
print(search_ele_sorted_rotated_arr(arr_2, search_key_2))
