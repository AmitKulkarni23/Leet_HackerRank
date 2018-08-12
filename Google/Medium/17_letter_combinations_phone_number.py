# Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons)
# is given below. Note that 1 does not map to any letters.
#
#
# Example:
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
#
# Although the above answer is in lexicographical order, your answer could be in any order you want.

def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """

    # Credits -> https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8120/AC-Python-solution

    # Create a dictionary first
    my_dict = {"1" : "", "2" : "abc", "3" : "def",
    "4" : "ghi", "5" : "jkl", "6": "mno",
    "7": "pqrs", "8" : "tuv", "9" : "wxyz", "0":" "}


    result = [""]

    if not digits:
        return []

    for d in digits:
        temp_list = my_dict[d]

        new_res = []

        for c in temp_list:
            for s in result:
                new_res.append(s + c)

        result = new_res

    return result
