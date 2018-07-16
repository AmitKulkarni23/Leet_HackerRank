# Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary representation of N.
#
# If there aren't two consecutive 1's, return 0.
#
#
#
# Example 1:
#
# Input: 22
# Output: 2
# Explanation:
# 22 in binary is 0b10110.
# In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
# The first consecutive pair of 1's have distance 2.
# The second consecutive pair of 1's have distance 1.
# The answer is the largest of these two distances, which is 2.
# Example 2:
#
# Input: 5
# Output: 2
# Explanation:
# 5 in binary is 0b101.
# Example 3:
#
# Input: 6
# Output: 1
# Explanation:
# 6 in binary is 0b110.
# Example 4:
#
# Input: 8
# Output: 0
# Explanation:
# 8 in binary is 0b1000.
# There aren't any consecutive pairs of 1's in the binary representation of 8, so we return 0.
#
#
# Note:
#
# 1 <= N <= 10^9

def convert_to_binary(x):
    """
    Function to convert an integer to binary
    """
    if x == 0:
        return 0


    bit = ""
    while x:
        bit += str(x % 2)
        x >>= 1

    return bit[::-1]

def find_longest_consecutive_ones(n):
    """
    find and return the longest distance between two
    consecutive 1's in the binary representation of N
    """
    # Check if number is a power of 2
    if n and not (n & (n - 1)):
        # is a power of 2
        return 0


    bin_rep = convert_to_binary(n)
    start = 0
    end = 0
    i, j = 0, 0
    max_dist = 0

    while i < len(bin_rep) - 1:
        if bin_rep[i] == "1":
            start = i
            j = i + 1
            while j < len(bin_rep) and bin_rep[j] == "0":
                j += 1

            end = j
            if end < len(bin_rep):
                max_dist = max(max_dist, end - start)

            start = j
            end = 0
        i += 1

    return max_dist

print(convert_to_binary(8))
print(find_longest_consecutive_ones(8))
