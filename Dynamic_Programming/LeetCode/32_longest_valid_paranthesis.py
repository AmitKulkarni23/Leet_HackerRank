# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
#
# Example 1:
#
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# Example 2:
#
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"

###########################

def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """

    # Credits -> https://leetcode.com/problems/longest-valid-parentheses/discuss/123926/Best-Python-Solution-(Beats-100)
    stack = [0]

    total_count = 0

    for ch in s:
        if ch == "(":
            stack.append(0)
        else:
            if len(stack) > 1:
                value = stack.pop()

                # Adding 2 here, because 1 valid bracket () accounts for a total count
                # of 2
                stack[-1] = stack[-1] + value + 2
                total_count = max(total_count, stack[-1])
            else:
                stack = [0]

    return total_count

# Examples:
input = ")()())"
input_2 = "(((())))"
print(longestValidParentheses(input_2))
