# Count the number of prime numbers less than a non-negative number, n.
#
# Example:
#
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """
    # Sieve of Erathosthenes
    p = 2

    # Create a list from 0 to n
    prime_list = [True for i in range(n + 1)]

    while p * p <= n:
        if prime_list[p] == True:
            for i in range(2*p, n+1, p):
                prime_list[i] = False

        p += 1

    count = 0
    # Count the number of primes:
    for p in range(2, n):
        if prime_list[p]:
            count += 1

    return count

print(countPrimes(14))
