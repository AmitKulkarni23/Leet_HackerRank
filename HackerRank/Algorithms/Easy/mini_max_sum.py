"""
Given five positive integers, find the minimum and maximum 
values that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values as a single line of two space-separated long integers.
"""


#!/bin/python3

import sys


# Simple Solution
# x = sum(arr)
# print((x - max(arr)), (x - min(arr)))

# My solution - Very large
def miniMaxSum(arr):
    # Complete this function
    
    # Logic is min sum will involve the minimum number
    # and exlude the max number. Similarly max sum will 
    # include max number and exclude min number
    
    # Initializing min_sum and max_sum
    min_sum, max_sum = 0, 0
    
    min_num = min(arr)
    max_num = max(arr)
    
    
    # Now there could be duplicate max_numb and min_numb
    # Creating flags so that such numbers are excluded only once
    min_exc, max_exc = False, False
    
    # Iterating through the array list
    # for calculating max_sum
    for ele in arr:
        if ele != min_num:
            max_sum += ele
        else:
            if min_exc:
                # min_num is excluded once
                # Therefore add it to the sum
                max_sum += ele
            else:
                # Excluding the minimum number for the first time
                min_exc = True
    
    # Iterating through the array list
    # for calculating min_sum
    for ele in arr:
        if ele != max_num:
            min_sum += ele
        else:
            if max_exc:
                # min_num is excluded once
                # Therefore add it to the sum
                min_sum += ele
            else:
                # Excluding the minimum number for the first time
                max_exc = True
        
    
    print(min_sum, max_sum) 
            
            
        

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)