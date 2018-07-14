# Given a List of words, return the words that can be typed using letters of alphabet
# on only one row's of American keyboard like the image below.

# Example 1:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]

# Note:
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.

def findWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    output = []
    if not input:
        return output

    # Create a dictionary with keys as keys on the keyoboard and values
    # as row number on the keyboard

    row_1 = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
    row_2 = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]
    row_3 = ["z", "x", "c", "v", "b", "n", "m"]

    my_dict = {}
    for ch in row_1:
        my_dict[ch] = 1

    for ch in row_2:
        my_dict[ch] = 2

    for ch in row_3:
        my_dict[ch] = 3


    # Now iterate through the input array
    for item in words:
        n = len(item)
        should_append = True
        if my_dict[item[0].lower()] == 1:
            for j in range(1, n):
                if my_dict[item[j].lower()] != 1:
                    should_append = False
                    break
            if should_append:
                output.append(item)
            continue

        if my_dict[item[0].lower()] == 2:
            for k in range(1, n):
                if my_dict[item[k].lower()] != 2:
                    should_append = False
                    break
            if should_append:
                output.append(item)
            continue

        if my_dict[item[0].lower()] == 3:
            for l in range(1, n):
                if my_dict[item[l].lower()] != 3:
                    should_append = False
                    break
            if should_append:
                output.append(item)
            continue

    return output

def concise_leet_code_solution(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    # Credits -> https://leetcode.com/submissions/detail/163674415/

    # In python :
    # set a & set b - Intersection
    # set a | set b -> union
    # set a - set b -> difference

    a=set('qwertyuiop')
    b=set('asdfghjkl')
    c=set('zxcvbnm')

    res = []

    for word in words:
        t=set(word.lower())
        if (t & a) == t:
            res.append(word)
        if (t & b) == t:
            res.append(word)
        if (t & c) == t:
            res.append(word)

    return res

# Examples:
input = ["Hello", "Alaska", "Dad", "Peace"]
print(findWords(input))
print(concise_leet_code_solution(input))
