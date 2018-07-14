# Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.
#
# Example:
# Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])

def countNumbersWithUniqueDigits(n):
    """
    :type n: int
    :rtype: int
    """
    # Credits -> https://www.youtube.com/watch?v=OkJKxoDbQ_c

    # base Cases
    if n == 0:
        return 1

    if n == 1:
        return 10

    if n == 2:
        return 91


    # Keep track of the running product
    # to avoid computing it again and again

    prod = 81

    # End -> next thing to multiply
    end = 8

    # keep track of current value and previous value
    cur_val = 91
    prev_val = 91 # for n = 2 value is 91

    k = 3

    while k <= n:
        prod = prod * end

        # Each iteration we go through we 1 less option
        end = end - 1

        prev_val = cur_val
        cur_val = prod

        cur_val += prev

        k += 1

    return cur_val
