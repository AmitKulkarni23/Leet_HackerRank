# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

def guessNumber(n):
    """
    :type n: int
    :rtype: int
    """

    # Create the array
    # We will use binary search

    # note that my_arr is sorted
    left = 1
    right = n

    while left <= right:

        mid = (left + right) // 2
        result = guess(mid)
        if not result:
            # We guessed the correct number
            return mid
        elif result == -1:
            right = mid - 1
        else:
            left = mid + 1
