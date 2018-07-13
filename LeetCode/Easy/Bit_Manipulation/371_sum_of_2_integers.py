# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
#
# Example:
# Given a = 1 and b = 2, return 3.

# 1 AND 1 = 1
# 1 XOR 0 = 1

# carry = and operation
# residue = xor operation

def getSum(a, b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    # Corner cases
    if a == 0:
        return b
    if b == 0:
        return a

    if a == -b:
        # Example : a = 1, b = -1
        return 0

    if abs(a) > abs(b):
        # We want a to be the bigger number
        a, b = b, a

    # If a is negative
    if a < 0:
        return getSum(-a, -b)

    while b != 0:

        # Calculate carry
        carry = a & b
        # Assign the differnt bits to a
        a = a ^ b

        b = carry << 1

    return a
print(getSum(-1, 1))
