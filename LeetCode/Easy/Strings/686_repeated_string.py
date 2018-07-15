# Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.
#
# For example, with A = "abcd" and B = "cdabcdab".
#
# Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").
#
# Note:
# The length of A and B will be between 1 and 10000.
#
#

def repeatedStringMatch(A, B):
    """
    :type A: str
    :type B: str
    :rtype: int
    """

    if B in A:
        # There is no need to repeat, already a substring
        return 1

    if A not in B:
        # No matter how many times we repeat A, B is not a substring
        return -1

    count = 1

    new_str = A
    while 1:
        new_str += A
        count += 1
        if B in new_str:
            return count

# Examples:
A = "abcd"
B = "cdabcdab"

print(repeatedStringMatch(A, B))
