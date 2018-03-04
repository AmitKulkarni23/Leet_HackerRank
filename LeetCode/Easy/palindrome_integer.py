# Given an intger check if thge integer is a palindrome or not
# Note: We have to do it without using any extra space
# So, best not to convert it to a string
# Also, 32-bit integer overflow has to be handled

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        # Note: a negative number cannot be a palindrome
        # Also, we are concerned with 32 bit integers only
        # Therfore considering only integers which are less than 
        # 2 ^ 31 - 1
        
        
        if x >= 0 and x < (1 << 31) - 1:
            # A valid number
            # If the given number == reverse of the same number
            # Then, its a palindrome
            return x == self.reverse_num(x)
        else:
            return False
    
    def reverse_num(self, num):
        """
        Method that returns he reversed num
        :type num: positive int
        :rtype: positive int
        """
        
        rev_num = 0
        while num > 0:
            rev_num = rev_num * 10 + num % 10
            num = num // 10;
        
        
        return rev_num