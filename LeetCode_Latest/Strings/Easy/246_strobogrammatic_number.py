# https://leetcode.com/problems/strobogrammatic-number/description/

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # Pseudo Code
        # rotated_string = an empty string
    
        # for each character in num_string, going in reverse:
        #     if character is 0, 1, or 8:
        #         append character to rotated_string
        #     else if character is 6:
        #         append 9 to rotated_string
        #     else if character is 9:
        #         append 6 to rotated_string
        #     else (character is invalid):
        #         return false

        # if rotated_string is the same as num_string:
        #     return true
        # return false

        # Time - O(N)
        # Space - O(N)

        rotated_digits = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        
        rotated_string_builder = []
        
        for c in reversed(num):
            if c not in rotated_digits:
                return False
            rotated_string_builder.append(rotated_digits[c])
        
        rotated_string = "".join(rotated_string_builder)
        return rotated_string == num
