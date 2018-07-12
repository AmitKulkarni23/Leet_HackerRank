# Reverse bits of a given 32 bits unsigned integer.
#
# Example:
#
# Input: 43261596
# Output: 964176192
# Explanation: 43261596 represented in binary as 00000010100101000001111010011100,
#              return 964176192 represented in binary as 00111001011110000010100101000000.
# Follow up:
# If this function is called many times, how would you optimize it?

def reverseBits(n):
    """
    @param n, an integer
    @return an intege
    """
    # First, you pop the right most bit from n.
    # Second, push it in the right most position of result.
    # Third, move result one bit leftward, so you can push a new bit in next time(except the last time).

    # Initilaize result = 0
    result = 0

    for i in range(32):
        # Pop the right most bit from n
        # How? -> n & 1
        # Add it to teh right most bit of result
        result = (result << 1) + (n & 1)

        # Now half the value of n ( beacuse we have already accounted for the last bit)
        n = n >> 1

    return result

n = 12
print(reverseBits(n))
