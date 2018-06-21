# Python file to print teh nth fibonnacci number using recursion
# Question to ask: 1-based indexing or 0-based indexing

def get_nth_fib_numb_without_memoization(n):
    """
    Function that prints out the nth fibonacci number
    Consider 1 based index

    Time Complexity -> O(n)
    Recursive Formula -> T(n) = T(n-1) + T(n-2) + O(1)
    """

    # Base Cases
    if n == 1:
        return 0

    if n == 2:
        return 1

    return get_nth_fib_numb_without_memoization(n-1) + get_nth_fib_numb_without_memoization(n-2)


def fib_with_memoization(n, look_up):
    """
    Function that returns the nth Fibonacci number
    This function uses memoization i.e it uses a list to store an
    already calculated fibonacci number

    0 -> based indexing

    look_up : list

    Time Complexity -> O(n)
    Space Complexity -> O(n)
    """

    if n == 0 or n == 1:
        look_up[n] = n

    if look_up[n] == None:
        look_up[n] = fib_with_memoization(n - 1, look_up) + fib_with_memoization(n - 2, look_up)

    return look_up[n]


def fib_iterative_solution(n):
    """
    An iterative solution for finding teh nth fibonacci number

    Time COmplexity -> O(n)
    Space Complexity : O(1)

    Consider 1-based indexing
    """

    if n == 1:
        return 0

    if n == 2:
        return 1

    i = 0
    j = 1
    sum = 0

    while (n-2) != 0:
        sum = i + j
        i = j
        j = sum

        n -= 1

    return sum

# print(get_nth_fib_numb_without_memoization(50))


# n = 5
# look_up = [None] * (n + 1)
# print(fib_with_memoization(n, look_up))


n = 101
print(fib_iterative_solution(n))
