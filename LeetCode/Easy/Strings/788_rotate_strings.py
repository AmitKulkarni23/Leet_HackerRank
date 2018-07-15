# X is a good number if after rotating each digit individually by 180 degrees,
# we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.
#
# A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate
# to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other,
# and the rest of the numbers do not rotate to any other number and become invalid.
#
# Now given a positive number N, how many numbers X from 1 to N are good?
#
# Example:
# Input: 10
# Output: 4
# Explanation:
# There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
# Note:
#
# N  will be in range [1, 10000].

# Runtime - 168 ms
def rotatedDigits(N):
    """
    :type N: int
    :rtype: int
    """

    if N <= 1:
        return 0

    total_count = 0
    for i in range(1, N+1):
        i_str = str(i)
        if "4" in i_str or "3" in i_str or "7" in i_str:
            continue
        else:
            rot_numb = rotate_numbers(i)
            if rot_numb != i:
                # print(rot_numb)
                total_count += 1

    return total_count


def rotate_numbers(numb):
    """
    Function that actually rotates the number
    """

    numb_str = str(numb)

    my_list = list(numb_str)

    for i, ch in enumerate(numb_str):
        if ch == "2":
            my_list[i] = "5"

        elif ch == "5":
            my_list[i] = "2"

        elif ch == "6":
            my_list[i] = "9"

        elif ch == "9":
            my_list[i] = "6"

    return int("".join(my_list))

# Runtime -> 66ms
def better_leetcode_sol(N):
    """
    :type N: int
    :rtype: int
    """
    count=0
    for i in range(1,N+1):
        s =str(i)
        if '3' in s or '4' in s or'7' in s :
            continue
        elif '2' in s or '5' in s or'6' in s or '9' in s:
            count+=1
    return count

# Examples:
print(rotatedDigits(2))
