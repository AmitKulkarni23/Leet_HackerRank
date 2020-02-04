# Given 3 sorted arrays, find the intersection of these arrays
# Example:
# arr_1 = [2, 6, 9, 11, 13, 17]
# arr_2 = [3, 6, 7, 10, 13, 18]
# arr_3 = [4, 5, 6, 9, 11, 13]

# Output: [6, 13]

# Time Complexity : O(n1 + n2 + n3) where n1 = len(arr_1), n2 = len(arr_2),
# n3 = len(arr_3)
# Space Complexity: O(1)

def find_intersection(arr_1, arr_2, arr_3):
    result = []
    x, y, z = 0, 0, 0

    while x < len(arr_1) and y < len(arr_2) and z < len(arr_3):
        if arr_1[x] == arr_2[y] == arr_3[z]:
             result.append(arr_1[x])
             x += 1
             y += 1
             z += 1

        elif arr_1[x] < arr_2[y]:
            x += 1
        elif arr_2[y] < arr_2[z]:
            y += 1
        else:
            z += 1

    return result

arr_1 = [2, 6, 9, 11, 13, 17]
arr_2 = [3, 6, 7, 10, 13, 18]
arr_3 = [4, 5, 6, 9, 11, 13]

print(find_intersection(arr_1, arr_2, arr_3))
