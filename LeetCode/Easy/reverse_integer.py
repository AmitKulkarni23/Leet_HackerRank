# Given a 32-bit signed integer, reverse the integer
# If teh integer overflows then return 0

def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        
        # Initilaizing the reverse number to 0
        rev_num = 0
        
        if x < 0:
            # If the number is a negative number
            # Then changing the number to be positive
            # Finally a negative reversed number will be returned
            neg = True
            x = -1 * x
            
            
        while x > 0:
            rev_num = rev_num * 10 + x % 10
            x = x // 10
        
        if abs(rev_num) > (1 << 31) - 1:
            # Checking for integer overflow
            return 0
        
        if neg:
            return -1 * rev_num
        else:
            return rev_num