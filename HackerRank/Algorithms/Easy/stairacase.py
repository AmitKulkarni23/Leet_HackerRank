# Sample Input: 6
# Sample Output:
	 #
    ##
   ###
  ####
 #####
######


#!/bin/python3

import sys

def staircase(n):
    # Complete this function
    if n == 1:
        print("#")
    else:
        # Print from the reverse order
        for i in range(n-1, 0, -1):
            # This gets us the number of spaces that we
            # need to print before printing the # symbol
            numb_of_hashes = n - i
            print(" " * i + "#" * numb_of_hashes)
        
        # Finally print all the hashes on the last line
        print("#" * n)

if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)
