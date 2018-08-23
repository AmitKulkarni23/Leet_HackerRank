# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#     ...
# Example 1:
#
# Input: "A"
# Output: 1
# Example 2:
#
# Input: "AB"
# Output: 28
# Example 3:
#
# Input: "ZY"
# Output: 701

def titleToNumber(s):
    """
    :type s: str
    :rtype: int
    """

    # This is similar to base 26
    # reverse the string
    rev_str = s[::-1]

    # Initialize sum
    excel_sum = 0

    for i, ch in enumerate(rev_str):
        excel_sum += (ord(ch) - 65 + 1) * ( 26 ** i)

    return excel_sum

# Examples
s1 = "A"
s2 = "AB"
s3 = "ZY"
print(titleToNumber(s1))
print(titleToNumber(s2))
print(titleToNumber(s3))
