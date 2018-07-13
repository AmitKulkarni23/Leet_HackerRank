def integerReplacement(n):
    """
    :type n: int
    :rtype: int
    """

    # Credits -> https://leetcode.com/problems/integer-replacement/discuss/87966/JAVA-3ms-Bit-Manipulation-Solution
    # Explanation by @kotomi_null

    # When N is odd, only the second bit matters.
    #
    # If the bit is '1', N+1 will remove at least one '1' in N. 1011 + 1 = 1100,
    # 1111 + 1 = 10000. However, N - 1 will remove only one '1'. 1011 - 1 = 1010
    # or 1111 - 1 = 1110. So we favor N + 1 here.
    #
    # If the bit is '0', N+1 will remove zero '1'. 1001 + 1 = 1010. N -1 will
    # remove one '1'. 1001 - 1 = 1000.

    if n == 1:
        return 0

    if n < 1:
        return None

    count = 0
    while n != 1:
        if n & 1:

            # Special Case n == 3:
            if n == 3:
                count += 2
                break
                
            # The number is odd
            if n & 2 == 2:
                # The 2nd LSB is 1
                # Then we favor n + 1
                n = n + 1
            else:
                # Favor n - 1
                n = n - 1
        else:
            n = n // 2

        count += 1

    return count

def is_power_of_2(numb):
    """
    Function that returns if teh given number is a power of 2
    """
    return not (numb & (numb - 1))

# Examples:
n = 10000
# print("is power of 2 n - 1", is_power_of_2(n-1))
# print("is power of 2 n + 1", is_power_of_2(n+1))
print(integerReplacement(n))
