# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
#
# Example:
#
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# Note:
#
# 1 is typically treated as an ugly number.
# n does not exceed 1690.

# Time Complexity: O(n logn)

from heapq import heappush, heappop
def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """

    # Idea
    # 1 is the samllest ugly number
    # Any other ugly number is either a multiple of 2, 3, 5
    # For example: 1, 2, 3, 4, 5, 6, 7, 8,9 10, 11, 12

    # 10 is a ugly number
    # What is the next ugly number?? -> 12
    # 6 * 2 = 12
    # 6 was the previous ugly number

    # Simlarly 15 is an ugly number
    # 5 * 3 = 15

    # Similarly 4 * 3 = 12

    # But we should consider the minimum
    # i.e min(12, 15, 12)
    # use property of heap to get the next ugly number

    # Credits -> https://leetcode.com/problems/ugly-number-ii/discuss/146881/A-unique-Java-n*log(n)-solution-beats-98.59
    # Credits -> https://leetcode.com/problems/ugly-number-ii/discuss/129552/Python-Elegant-solution-using-min-heap

    my_heap = [1]

    my_set = {1}

    # Iterate through all the lements
    for i in range(n-1):
        min_ele = heappop(my_heap)

        # Consider all possiblities
        for ele in [2 * min_ele, 3 * min_ele, 5 * min_ele]:
            if ele not in my_set:
                my_set.add(ele)
                heappush(my_heap, ele)
    return heappop(my_heap)


def leet_code_sol(n):
    """
    :type n: int
    :rtype: int
    """
#
    # Credits -> https://leetcode.com/submissions/detail/162794643/
    ugly = [1]

    i2=i3=i5=0

    idx = 1
    while idx < n:
        i2_val = ugly[i2] * 2
        i3_val = ugly[i3] * 3
        i5_val = ugly[i5] * 5
        ugly_val = min(i2_val,i3_val,i5_val)
        if ugly_val == i2_val:
            i2 += 1
        if ugly_val == i3_val:
            i3 += 1
        if ugly_val == i5_val:
            i5 +=1
        ugly.append(ugly_val)
        idx+=1
    return ugly[n-1]

print(nthUglyNumber(10))
print(leet_code_sol(10))
