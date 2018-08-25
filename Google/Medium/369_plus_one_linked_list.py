# Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.
#
# You may assume the integer do not contain any leading zero, except the number 0 itself.
#
# The digits are stored such that the most significant digit is at the head of the list.
#
# Example:
# Input:
# 1->2->3
#
# Output:
# 1->2->4

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # We will use 2 pointers i and j for this problem
        # Create a dummy node

        dummy = ListNode(0)
        dummy.next = head
        i = dummy
        j = dummy

        # Example:
        # 1->2->8->9
        #       i  j

        while j.next is not None:
            j = j.next

            if j.val != 9:
                i = j

        if j.val != 9:
            j.val += 1
        else:
            i.val += 1

            i = i.next
            # Move i to the next value wher ei t is not 9
            while i is not None:
                i.val = 0
                i = i.next
        # Final Answer
        # 0->1->2->9->0
        if dummy.val == 0:
            return dummy.next

        return dummy
