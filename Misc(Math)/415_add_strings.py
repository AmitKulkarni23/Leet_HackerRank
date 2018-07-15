# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Runtime -> 632ms
def addStrings(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    return str(convert_to_int(num1) + convert_to_int(num2))

def convert_to_int(num):
    """
    Helper function to convert a given string to an intger
    """
    ans = 0

    for i, x in enumerate(num[::-1]):
        if x == "0":
            x = 0
        elif x == "1":
            x = 1
        elif x == "2":
            x = 2
        elif x == "3":
            x = 3
        elif x == "4":
            x = 4
        elif x == "5":
            x = 5
        elif x == "6":
            x = 6
        elif x == "7":
            x = 7
        elif x == "8":
            x = 8
        elif x == "9":
            x = 9
        ans += x * (10 ** i)

    return ans

# Runtime : 148ms
def best_leet_code_sol(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    # Credits -> https://leetcode.com/problems/add-strings/discuss/90461/Python-Solution-simply-using-ord()-and-chr()

    # Note ord("0") = 48
    # ord("1") = 49

    # Initialize varaibles
    i = 0
    j = 0
    carry = 0

    # Append to this result
    res = []

    while i < len(num1) or j < len(num2) or carry:
        if i < len(num1):
            # Geth the last digit fron num1
            carry += ord(num1[::-1][i]) - 48
            i += 1
        if j < len(num2):
            # Geth the last digit fron num1
            carry += ord(num2[::-1][j]) - 48
            j += 1

        # Now adjust carry
        res += [carry % 10]

        # Carry over to the next digit
        carry = carry // 10
    # Now add 48 to all the charcters in res
    return "".join(str(x) for x in res[::-1])

print(addStrings("1741", "2918"))
print(best_leet_code_sol("1741", "2918"))
