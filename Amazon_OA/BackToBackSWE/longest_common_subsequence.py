# Find the lenght of the longest common subsequence between 2 strings

# Example:
# s1 = "AGGTAB"
# s2 = "GXTXAYB"
#
# lcs(s1, s2) = 4
# Credits -> https://www.youtube.com/watch?v=ASoaQq66foQ
# Time - O(m*n)
# Space - O(m*n)  where m, n = len(s1), len(s2)

def lcs(s1, s2):
    # s2 is the rows
    # s1 is the cols
    cache = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]

    for s2_row in range(len(s2) + 1):
        for s1_col in range(len(s1) + 1):
            if s2_row == 0 or s1_col == 0:
                # Base Case
                # Empty strings being evaluated
                cache[s2_row][s1_col] = 0
            elif s2[s2_row - 1] == s1[s1_col - 1]:
                # Characters match
                cache[s2_row][s1_col] = cache[s2_row - 1][s1_col - 1] + 1
            else:
                cache[s2_row][s1_col] = max(cache[s2_row - 1][s1_col], cache[s2_row][s1_col - 1])

    return cache[-1][-1]

s1 = "AGGTAB"
s2 = "GXTXAYB"
print(lcs(s1, s2))
