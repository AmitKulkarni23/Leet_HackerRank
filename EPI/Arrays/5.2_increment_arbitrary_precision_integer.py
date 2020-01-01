"""
Input : Array of digits encoding a non-negative decimal D and updates the array
to represent D + 1.
Eg: input = [1, 2, 9]
output = [1, 3, 0]
"""

# Brute Force Implementation: Convert the arry to an integer and add 1.
# Convert the new integer back to array.

# But this is language dependent and may cause overflows

# Better Approach: Grade school arithmetic. Add from the least-significant bit

def plus_one(A):
    A[-1] += 1

    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1

    if A[0] == 10:
        # This can only happen when D = 9999 or 999 or 99 etc..
        A[0] = 1
        A.append(0)

arr = [1, 2, 9]
arr2 = [9, 9, 9]
arr3 = [9]

arg = arr3
plus_one(arg)
print(arg)
