# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .
#
# Example 1:
#
# Input: "1 + 1"
# Output: 2
# Example 2:
#
# Input: " 2-1 + 2 "
# Output: 3
# Example 3:
#
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23

# Note:
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.

def calculate(s):
    """
    :type s: str
    :rtype: int
    """
    # Credits -> https://leetcode.com/problems/basic-calculator/discuss/62344/Easy-18-lines-C++-16-lines-Python

    # We will maintain a stack of signs
    # So until a digit is encountered we will pop from this signs stack and multiply
    # it with the digit and add it to our total

    # If either of +-( is encountered, we will append to the stack
    # What to append. We need to append a sign( i.e. either 1 or -1)
    # So if a '-' occurs then append signs[-1] * -1
    # else append signs[-1] * 1

    # if ")", then pop from stack

    i = 0
    signs = [1, 1]
    total = 0

    while i < len(s):
        c = s[i]

        if c.isdigit():
            # This is a digit
            # We will march on until we do not encounter a digit

            # Store this index as start of digit sequence
            start = i

            while i < len(s) and s[i].isdigit():
                i += 1

            # We have come to the end of teh digit sequence
            # Now add to total
            total += signs.pop() * int(s[start:i])
            continue
        if c in "(+-":
            if c == "-":
                signs += signs[-1] * -1,
            else:
                signs+= signs[-1] * 1,

        if c == ")":
            signs.pop()

        i += 1
    return total

# Examples:
s = "(1+(2+3)-10)"
print(calculate(s))
