# Program for array rotation
# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.

# Example:
# a = [1, 2, 3, 4, 5, 6, 7]
#
# rotate(a, 2, 7 ) => a = [3, 4, 5, 6, 7, 1, 2]


# My method
def rotate(arr, d, n):
    """
    Function to rotate an array arr, of size n by d elements
    """

    if arr and d <= n:
        arr = arr[d:] + arr[:d]

    return arr

# Method using GCD:
# Time Complexity : O(n)
# Space COmplexity: O(1)
# One of the methods is to left rotate the array one by one for d times
# Store arr[0] in temp
# Move arr[1] -> arr[0], arr[2] -> arr[1] and finally temp -> arr[n-1]
# Example:
# arr = [1, 2, 3, 4, 5, 6, 7], d = 2

# After first iteration we get -> [2, 3, 4, 5, 6, 7, 1]
# After second iteration we get -> [ 3, 4, 5, 6, 7, 1, 2]

# Time Complexity: O(n * d)
# Space COmplexity : O(1)

# METHOD 3: Extension of method 2
# Steps:
# Instead of moving one by one, divide the array in different sets
# where number of sets is equal to GCD of n and d and move the elements within sets.
# Example:arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# d = 3

# gcd(n , d) = gcd(12, 3) = 3
# 1st iteration => arr = [4 2 3 7 5 6 10 8 9 1 11 12]
# 2nd iteration => arr = [4 5 3 7 8 6 10 11 9 1 2 12]
# 3rd iteration => arr = [4 5 6 7 8 9 10 11 12 1 2 3]

def rotate_array_by_gcd_method(arr, d, n):
    """
    Function to rotate an array arr, of size n by d elements
    """
    for i in range(gcd(d, n)):

        # Store the first variable in temp
        temp = arr[i]
        j = i

        while True:
            k = j + d
            if k >= n:
                k = k -n
            if k == i:
                break

            arr[j] = arr[k]

            j = k

        arr[j] = temp

def gcd(a, b):
    """
    Helper function to find GCD of 2 numbers a and b
    """
    if a == 0 or b == 0:
        print("No GCD")
        return None

    if a == b:
        return a

    if (a > b):
        return gcd(a - b, b)

    return gcd(a, b - a)

# Example
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
d = 2
n = len(arr)


# new_arr = rotate(arr, d, n)
print("Array before rotation is ", arr)
rotate_array_by_gcd_method(arr, d, n)
print(arr)


# Example 2:
arr_2 = [1, 2, 3, 4, 5, 6, 7]
d_2 = 3
n_2 = len(arr_2)

print("Array before rotation is ", arr_2)
rotate_array_by_gcd_method(arr_2, d_2, n_2)
print(arr_2)
