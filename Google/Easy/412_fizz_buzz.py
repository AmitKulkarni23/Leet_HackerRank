# Write a program that outputs the string representation of numbers from 1 to n.
#
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
#
# Example:
#
# n = 15,
#
# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]


def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """

    ans = []
    if n <= 0:
        return []

    for i in range(1, n+1):
        if i % 15 == 0:
            ans.append("FizzBuzz")
            continue
        if i % 5 == 0:
            ans.append("Buzz")
            continue
        if i % 3 == 0:
            ans.append("Fizz")
            continue
        ans.append(str(i))

    return ans

# Examples
n = 1
print(fizzBuzz(n))
