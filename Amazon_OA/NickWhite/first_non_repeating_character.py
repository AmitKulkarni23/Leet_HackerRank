# Q) First non-repeating charcter
# Input: a string, only a-z lowercase characters
# No empty strings
# Objective: First non-repeating charcters

# Eg: "aaabccc" -> b
# Eg: "aaabbcccdeeef" -> d
# Eg: "abcabc" -> "_" -> No such character

# Time: O(n)
# Space: O(n)

import collections
def find_repeating_character(s):
    freqMap = collections.Counter(s)

    for ch in s:
        if freqMap.get(ch) == 1:
            return ch

    return "_"


x = "aaabcc"
y = "aaabbcccdeeef"
z = "abcabc"
print(find_repeating_character(z))
