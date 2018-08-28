# Given a string representing arbitrarily nested ternary expressions, calculate the result of the expression. You can always assume that the given expression is valid and only consists of digits 0-9, ?, :, T and F (T and F represent True and False respectively).
#
# Note:
#
# The length of the given string is ≤ 10000.
# Each number will contain only one digit.
# The conditional expressions group right-to-left (as usual in most languages).
# The condition will always be either T or F. That is, the condition will never be a digit.
# The result of the expression will always evaluate to either a digit 0-9, T or F.
# Example 1:
#
# Input: "T?2:3"
#
# Output: "2"
#
# Explanation: If true, then result is 2; otherwise result is 3.
# Example 2:
#
# Input: "F?1:T?4:5"
#
# Output: "4"
#
# Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:
#
#              "(F ? 1 : (T ? 4 : 5))"                   "(F ? 1 : (T ? 4 : 5))"
#           -> "(F ? 1 : 4)"                 or       -> "(T ? 4 : 5)"
#           -> "4"                                    -> "4"
# Example 3:
#
# Input: "T?T?F:5:3"
#
# Output: "F"
#
# Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:
#
#              "(T ? (T ? F : 5) : 3)"                   "(T ? (T ? F : 5) : 3)"
#           -> "(T ? F : 3)"                 or       -> "(T ? F : 5)"
#           -> "F"                                    -> "F"
# Runtime : 76ms
def parseTernary(expression):
    """
    :type expression: str
    :rtype: str
    """
    # Credits -> https://leetcode.com/problems/ternary-expression-parser/discuss/92185/Short-Python-solutions-one-O(n)
    # Time COmplexity -> O(n)
    stack = []
    for c in reversed(expression):
        stack.append(c)
        # print("Stack is ", stack)
        if stack[-2:-1] == ['?']:
            # print("We are here")
            # print("stack[-3]", stack[-3])
            # print("stack[-5]", stack[-5])
            # print("stack[-1]", stack[-1])
            stack[-5:] = stack[-3 if stack[-1] == 'T' else -5]
    return stack[0]

# Runtime : 32 ms
def parseTernary(expression):
    """
    :type expression: str
    :rtype: str
    """
    while len(expression) > 2:
        count = 0
        for x in range(2, len(expression)):
            if expression[x] == '?':
                count += 1
            elif expression[x] == ':':
                count -= 1
                if count == -1:
                    if expression[0] == 'T':
                        expression = expression[2:x]
                    else:
                        expression = expression[x+1:]
                    break
        else:
            return expression

    return expression

# Examples:
express = "T?2:3"
print(parseTernary(express))
