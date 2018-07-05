# Given a sequence of words, and a limit on the number of characters that can be put
# in one line (line width). Put line breaks in the given sequence such that the
# lines are printed neatly
#
# Solution:
# Badness - We define badness has square of empty spaces in every line. So 2 empty space
# on one line gets penalized as 4 (2^2) while 1 each empty space on 2 lines gets
# penalized as 2(1 + 1). So we prefer 1 empty space on different lines over 2 empty space on
# one line.


def justify(words, width):
    """
    Function that returns the optimal string with badness minimized

    Credits -> https://github.com/mission-peace/interview/blob/master/src/com/interview/dynamic/TextJustification.java
    Time Complexity : O(n ^ 2)
    Space Complexity : O(n ^ 2)
    """
    # Create a list out of the strings
    words_matrix = words.split()

    # Ge the actual number of words in the given string
    str_len = len(words_matrix)

    # Build the costmatrix
    cost = [[0 for _ in range(str_len)] for _ in range(str_len)]

    for i in range(str_len):
        cost[i][i] = width - len(words_matrix[i])

        for j in range(i+1, str_len):
            # The -1 is to accomodate for 1 space to separate the words
            cost[i][j] = cost[i][j-1] - len(words_matrix[j]) - 1

    # Now cacluate teh badness in teh cost array
    for i in range(str_len):
        for j in range(str_len):
            if cost[i][j] < 0:
                cost[i][j] = float("inf")
            else:
                cost[i][j] = (cost[i][j]) ** 2


    # Initilaize 2 different 1 D arrays
    min_cost = [0] * str_len
    result = [0] * str_len

    # Now caclulate where to split so that we minimze badness
    # Start from teh end of the array
    for i in range(str_len-1, -1, -1):
        min_cost[i] = cost[i][str_len - 1]
        result[i] = str_len

        for j in range(str_len -1, i, -1):
            if cost[i][j-1] == float("inf"):
                continue

            if min_cost[i] > min_cost[j] + cost[i][j-1]:
                min_cost[i] = min_cost[j] + cost[i][j-1]
                result[i] = j


    # Now, print the string
    str = ""

    i, j = 0,0

    while j  < str_len:
        j = result[i]
        for k in range(i, j):
            str += words_matrix[k]
            str += " "

        str += "\n"
        i = j
    print(str)

words = "Amit Kulkarni likes to code"
width = 10
justify(words, width)
