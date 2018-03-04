# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # The roman numerals represent the following numbers in the
        # decimal system
        # I = 1, V = 5, X = 10, L = 50 , C = 100, D = 500, M = 1000
        
        # Creating a dicitionary to hold the values corresponding to these
        # roman symbols
        
        roman_int_dict = {"M": 1000, "D":500, "C":100, "L": 50, "X" : 10, "V": 5, "I" : 1}
        
        
        # Initlaizing int_total to 0
        int_total = 0
        # Counter to keep track of the index
        i = 0
        
        # Now start from index 0.
        
        while i < len(s):
            
            first_value = roman_int_dict[s[i]]
            
            if i+1 < len(s):
                
                second_value = roman_int_dict[s[i+1]]
                if first_value >= second_value:
                    # If the roman numeral at the current index is greater than or equal to the
                    # next symbol, add the symbol to int_total
                    int_total += first_value

                    # Incrementing i
                    i += 1
                else:
                    # Subtract the current numeral from the next neighbor and add this value
                    # to int total
                    int_total += second_value - first_value

                    # Skipping twice
                    i += 2
            else:
                int_total += first_value
                i += 1
        
        return int_total
                            
            