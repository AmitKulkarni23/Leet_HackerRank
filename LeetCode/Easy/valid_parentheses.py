# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" 
# are all valid but "(]" and "([)]" are not.

# My solution
# Run time : 44ms in LeetCode
# Design Strategy: use stack data structure
# and perform operations pop and append
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
               
        # Storing the closing and opening brackets as key-value pairing
        # in a dictionary brackets
        
        brackets = {")" : "(", "}" : "{", "]" : "["}
                        
        # A stack data structure should be used
        stack_brackets = []
        
        for i in range(len(s)):
            
            # If stack is empty and we encounter a closing bracket then 
            # there is something wrong
            if not stack_brackets and s[i] in brackets.keys():
                return False
            
            if s[i] in brackets.values():
                # Pushing all the opening brackets values into
                # a stack
                stack_brackets.append(s[i])
            
            else:
                # Must be a closing bracket
                # Pop the stack and check if the corresponding
                # bracket matches
                if stack_brackets.pop() != brackets[s[i]]:
                    return False
        
        
        # If after all the operations, stack is not empty then there
        # is a mismatch
        if stack_brackets:
            return False
        
        
        return True
            
        
        