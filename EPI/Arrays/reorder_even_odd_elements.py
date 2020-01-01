"""
Input : Array of integers
Output: Reorder array so that even entries appear first
"""

# Time : O(n)
# Space : O(1)

def reorder_arr(arr):
    next_even = 0
    next_odd = len(arr) - 1

    while next_even < next_odd:
        if arr[next_even] % 2 == 0:
            next_even += 1
        else:
            arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
            next_odd -= 1

arr = [1, 2, 3, 4, 5, 6, 7, 8]
arr2 = [1, 3, 5, 7, 9]

arg = arr2
reorder_arr(arg)
print(arg)
