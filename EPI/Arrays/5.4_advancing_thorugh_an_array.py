"""
Write a program which takes an array of integers, where A[i] denotes, the maximum
you can advance from index i, and returns whether it is possible to reach the
last index starting from the beginning of the array
"""

def advance_by_offsets(arr):
    furthest_so_far = 0
    last_index = len(arr) - 1

    i = 0
    while i <= furthest_so_far and furthest_so_far < last_index:
        furthest_so_far = max(furthest_so_far, i + arr[i])
        i += 1
    return furthest_so_far >= last_index

print(advance_by_offsets([3, 3, 1, 0, 2, 0, 1]))
print(advance_by_offsets([3, 2, 0, 0, 2, 0, 1]))
