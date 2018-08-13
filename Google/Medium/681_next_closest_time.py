# Given a time represented in the format "HH:MM", form the next closest time
# by reusing the current digits. There is no limit on how many times a digit can be reused.

# You may assume the given input string is always valid.
# For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.
#
# Example 1:
#
# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39,
# which occurs 5 minutes later.  It is not 19:33, because
# this occurs 23 hours and 59 minutes later.
# Example 2:
#
# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
# It may be assumed that the returned time is next day's time sinc

def nextClosestTime(time):
    """
    :type time: str
    :rtype: str
    """

    # Credits -> https://leetcode.com/problems/next-closest-time/solution/
    # Time COmplexity -> O(1)
    # Space COmplexity -> O(1)
    # Move the clock forward by 1 minute
    # Each time it moves forward, if all the digits are allowed,
    # then return the current time


    # Represent time as a function of minutes
    # For example 19:22 = 60 * 19 + 22
    curr_time = 60 * int(time[:2]) + int(time[3:])

    allowed_digits = {int(x) for x in time if x != ':'}

    # Now we increment the time by 1 minute
    while True:
        curr_time = (curr_time + 1) % (24 * 60)

        # Note: divmod(num, denom) -> (qoutient, remainder)
        # So divmod(curr_time, 60) -> Returns(hours, minutes)

        # We can find each digit in hours and minutes by -> (hours // 10 and hours % 10)
        # and (minutes // 10 and minutes % 10)

        # if all of such digits are in curr_time, return that time
        if all(digit in allowed_digits for block in divmod(curr_time, 60) for digit in divmod(block, 10)):
            # We have got the next closes time
            # Note *divmod -> means a variable number of arguments( similar to *argv)
            # Note: Similary kwargs -> means key -> value pairs of arguments
            # Note: :02d -> Integer of max lenght 2 with 0 padding on left
            return "{:02d}:{:02d}".format(*divmod(curr_time, 60))
