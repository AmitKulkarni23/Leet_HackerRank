# Given an array, cyclically rotate the array clockwise by one.
# Example:
# arr[] = {1, 2, 3, 4, 5}
# arr[] = {5, 1, 2, 3, 4}

def cyclically_rotate_array_by_1(arr):
    """
    Function to cyclically rotate array by 1
    """
    length_arr = len(arr)
    last_ele = arr[-1]

    new_arr = [last_ele] + arr[:(length_arr - 1)]

    return new_arr

# Examples:
arr = [1, 2, 3, 4, 5, 6]
new_arr = cyclically_rotate_array_by_1(arr)
print(new_arr)
