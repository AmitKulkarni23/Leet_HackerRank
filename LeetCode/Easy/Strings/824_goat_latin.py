# A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.
#
# We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)
#
# The rules of Goat Latin are as follows:
#
# If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
# For example, the word 'apple' becomes 'applema'.
#
# If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
# For example, the word "goat" becomes "oatgma".
#
# Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
# For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
# Return the final sentence representing the conversion from S to Goat Latin.

# Example 1:
#
# Input: "I speak Goat Latin"
# Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

def toGoatLatin(S):
    """
    :type S: str
    :rtype: str
    """
    word_list = []
    vowel_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    word_list = S.split()

    # Iterate through the list items
    for i, item in enumerate(word_list):
        # Word begins with vowel
        if item[0] in vowel_list:
            word_list[i] = item + "ma" + "a" * (i + 1)

        else:
            word_list[i] = item[1:] + item[0] + "ma" + "a" * (i + 1)

    return " ".join(word_list)
