# Given a string, find the minimum number of characters to be inserted to convert it to palindrome.
#
# Before we go further, let us understand with few examples:
#     ab: Number of insertions required is 1. bab
#     aa: Number of insertions required is 0. aa
#     abcd: Number of insertions required is 3. dcbabcd
#     abcda: Number of insertions required is 2. adcbcda which is same as number of insertions in the substring bcd(Why?).
#     abcde: Number of insertions required is 4. edcbabcde


# Dp -> bottom up approach
# Space Complexity -> O(n ^ 2)
# Time Complexity -> O(n ^ 2)

def get_min_insertions(str):
    """
    Function that returns teh minimum number of insertiosn
    required to make a string a palindrome
    """

    if len(str) == 0:
        return 0

    n = len(str)

    # Create a cache to store results of sub problems
    cache = [[0 for _ in range(n)] for _ in range(n)]

    for l in range(1, n):
        x = 0
        for h in range(l, n):
            # Now we need to make a record in the cache
            # So as to save repeated calculations
            if str[x] == str[h]:
                cache[x][h] = cache[x+1][h-1]
            else:
                # So for 0..2 entry we are looking at min of
                # entry from 0..1 or entry from 1..2

                #            0..2
                         # 0..1    1..2
                cache[x][h] = min(cache[x][h-1], cache[x+1][h]) + 1
            x += 1

    # The result is stored at the very end
    return cache[0][n-1]

# str = "geeks"
# str = "a"
str = "abcda"
print(get_min_insertions(str))
