# Alice has a hand of cards, given as an array of integers.
#
# Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.
#
# Return true if and only if she can.
#
#
#
# Example 1:
#
# Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
# Example 2:
#
# Input: hand = [1,2,3,4,5], W = 4
# Output: false
# Explanation: Alice's hand can't be rearranged into groups of 4.

# 1 <= hand.length <= 10000
# 0 <= hand[i] <= 10^9
# 1 <= W <= hand.length

import collections
def isNStraightHand(self, hand, W):
    """
    :type hand: List[int]
    :type W: int
    :rtype: bool
    """

    # Credits -> https://leetcode.com/problems/hand-of-straights/solution/

    # We will create a Counter dictionary
    my_dict =  collections.Counter(hand)

    while my_dict:
        # Iterate through the given list
        min_ele = min(my_dict)
        for i in range(min_ele, min_ele + W):
            freq = my_dict[i]

            # If no such item is present
            if not freq:
                return False

            if freq == 1:
                del my_dict[i]
            else:
                my_dict[i] = freq - 1

    return True
