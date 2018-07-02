# We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
#
# Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
# Example:
# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# Note: The input number n will not exceed 100,000,000. (1e8)

def checkPerfectNumber(num):
    """
    :type num: int
    :rtype: bool
    """
    # Credits -> https://leetcode.com/problems/perfect-number/solution/
    # Idea -> Only iterate upto sqrt(n) and find all factors
    # Why -> because we know that the maximum number n for the pair
    # ni * nj to be equal to num is sqrt(num) * *sqrt(num)

    if num <= 1:
        return False

    i = 2
    sum = 1
    while i * i <= num:
        if num % i == 0:
            sum += i

            if i * i != num:
                # Add the other factor as well
                sum += num / i
        i += 1


    return sum == num

# Examples:
print(checkPerfectNumber(29))
