"""
Write a program which takes in input a sorted array and updates it so that all
duplicates have been removed and the remaining elements have been shifted left
to fill the emptied indices. Return the number of valid elements
NOTE: Sorted array
"""
# Time: O(n)
# Space: O(1)

# Use write index

def delete_duplicates(A):
    if not A:
        return 0

    write_index = 1

    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1

    return write_index # The number of unique elements

arr = [2, 3, 5, 5, 7, 11, 11, 11, 13]
print("Number of unique elements = ", delete_duplicates(arr))
