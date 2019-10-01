# https://leetcode.com/discuss/interview-question/233724

# Approach -> We will count the vowels that are at the beginning of the string and the end
# end of the string and store it in a variable

# Example
# aecdefghio

# start = 2 ( "ae")
# end = 2 ("io")

# total_boundary_vowels = 4 ( start + str_len - 1 - end )

# Then in the range [start + 1 : end + 1] count the largest substring made up of only vowels(let's call this middle_vowels)

# return total_boundary_vowels + middle_vowels

# Time -> O(N)
# Space -> O(1)

# Credits -> Python solution by user anuragkr in the link https://leetcode.com/discuss/interview-question/233724

##################################################################################


def findLongestString(data):
    # store the string length as it will be used repeatedly
    str_len = len(data)
    # check for an empty string
    if str_len == 0: return 0
    start, end, vowels = 0, len(data) - 1, set('aeiou')
    # count the vowels from the beginning (if any)
    for c in data:
        if c in vowels:
            start += 1
        else:
            break
    # return the original string length if it has only vowels
    if start >= str_len: return str_len
    # count the vowels from the end (if any)
    while end >= 0:
        if data[end] in vowels:
            end -= 1
        else:
            break
    # keep the sum of count of vowels from the boundaries
    boundary_vowels_len = start + str_len - 1 - end
    middle_vowels_len, largest = 0, 0
    # start points to the last vowel from the beginning. So the middle substring starts from the next index.
    # even if the first one is not a vowel, we dont mind starting from the next index as its not a vowel

    # count the largest vowel substring in the middle string
    for c in data[start + 1:end + 1]:
        if c in vowels:
            middle_vowels_len += 1
        else:
            middle_vowels_len = 0
        largest = max(largest, middle_vowels_len)
    # return the total count
    return boundary_vowels_len + largest

print(findLongestString("earthproblem"))
print(findLongestString("letsgosomewhere"))
print(findLongestString("aaaaaaaaaaa"))
