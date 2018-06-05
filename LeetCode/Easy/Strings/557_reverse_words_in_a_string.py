# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.
#

def reverseWords(self, s):
    """
    :type s: str
    :rtype: str
    """

    # Idea -> Convert the sentence into a list of words using split()
    # Reverse all words in the list and join them using teh join operator separated by spaces

    if s:
        z_list = s.split()

        # Reverse each element in z_list
        for i, item in enumerate(z_list):
            z_list[i] = item[::-1]

        # Join elements of z_list
        return " ".join(z_list)
    else:
        return s
