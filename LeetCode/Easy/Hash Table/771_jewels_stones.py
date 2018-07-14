# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
# Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
#
# The letters in J are guaranteed distinct, and all characters in J and S are letters.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".
#
# Example 1:
#
# Input: J = "aA", S = "aAAbbbb"
# Output: 3
# Example 2:
#
# Input: J = "z", S = "ZZ"
# Output: 0
# Note:
#
# S and J will consist of letters and have length at most 50.
# The characters in J are distinct.

# Time Complexity -> max(O(S), O(J))
# Space Complexity -> O(S)  

def numJewelsInStones(J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    # Cant do intersection between stes beacuse there might be
    # repeated number of jewels
    # Use a dictionary

    if not J:
        # No jewels at all, all are stones
        return 0

    if not S:
        # No stones to consider from
        return 0

    my_dict = {}

    for ch in S:
        if ch in my_dict:
            my_dict[ch] += 1
        else:
            my_dict[ch] = 1

    total_count = 0

    for ch in J:
        # in operator for dictionary is O(1)
        # Reference -> https://stackoverflow.com/questions/17539367/python-dictionary-keys-in-complexity
        if ch in my_dict:
            total_count += my_dict[ch]

    return total_count

# Examples
# J = "aA"
# S = "aAAbbbb"

J = "z"
S = "ZZ"

print(numJewelsInStones(J, S))
