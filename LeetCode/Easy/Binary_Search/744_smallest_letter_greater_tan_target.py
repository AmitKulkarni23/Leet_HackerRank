# Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.
#
# Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.
#
# Examples:
# Input:
# letters = ["c", "f", "j"]
# target = "a"
# Output: "c"
#
# Input:
# letters = ["c", "f", "j"]
# target = "c"
# Output: "f"
#
# Input:
# letters = ["c", "f", "j"]
# target = "d"
# Output: "f"
#
# Input:
# letters = ["c", "f", "j"]
# target = "g"
# Output: "j"
#
# Input:
# letters = ["c", "f", "j"]
# target = "j"
# Output: "c"
#
# Input:
# letters = ["c", "f", "j"]
# target = "k"
# Output: "c"
# Note:
# letters has a length in range [2, 10000].
# letters consists of lowercase letters, and contains at least 2 unique letters.
# target is a lowercase letter.


def nextGreatestLetter(letters, target):
    """
    :type letters: List[str]
    :type target: str
    :rtype: str
    """

    left = 0
    right =len(letters) - 1

    while left < right:
        mid = (left + right) // 2
        if letters[mid] <= target:
            left = mid + 1
        elif letters[mid] > target:
            right = mid

    if target >= letters[left]:
        return letters[0]
         
    return letters[left]

# Examples:
# letters = ["c", "f", "j"]
# target = "a"

# letters = ["c", "f", "j"]
# target = "c"

# letters = ["c", "f", "j"]
# target = "d"

# letters = ["c", "f", "j"]
# target = "g"

letters = ["c", "f", "j"]
target = "k"

print(nextGreatestLetter(letters, target))
