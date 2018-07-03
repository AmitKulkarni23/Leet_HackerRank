# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
# Given s = "hello", return "holle".
#
# Example 2:
# Given s = "leetcode", return "leotcede".
#
# Note:
# The vowels does not include the letter "y".

def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    if len(s) == 1:
        return s

    vowels_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    # Take 2 pointers, 1 pointer starting from the string array and another
    # starting from the end of the array
    #
    # If no vowels found increment teh 2 pointers, else if vowel found
    # swap them

    # Convert the string to a list, since strings are immutable
    final_list = list(s)

    i = 0
    j = len(final_list) - 1
    while i < j:
        if final_list[i] in vowels_list and final_list[j] in vowels_list:
            # Then swap
            final_list[i], final_list[j] = final_list[j], final_list[i]

            i += 1
            j -= 1

        if final_list[j] not in vowels_list:
            # Decrement j
            j -= 1

        if final_list[i] not in vowels_list:
            # Increment i
            i += 1

    return "".join(final_list)

print(reverseVowels("aA"))
