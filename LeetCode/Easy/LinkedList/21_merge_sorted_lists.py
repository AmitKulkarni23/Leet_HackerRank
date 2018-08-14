# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # Credits -> https://leetcode.com/problems/merge-two-sorted-lists/solution/
        # Time COmplexity -> O(m + n)

        # Create a dummy head called as  "prehead" whose .next will be returned after
        # we have sorted the lists
        prehead = ListNode(-1)

        # Create a previous pointer
        prev = prehead

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                # Point previ's next to this node
                prev.next = l1
                # Increment l1
                l1 = l1.next
            else:
                # Point previ's next to this node
                prev.next = l2
                l2 = l2.next

            # Move previous 1 step ahead
            prev = prev.next

        # Once we are out of this loop, exactly 1 of l1 or l2 is null
        # And we have the final list in sorted order
        # Whichever, list is no-null, it means that all teh elements in that list
        # are greater than the final sorted list
        # Just add the non-null list elements to teh final sorted list

        if l1 == null:
            prev.next = l2
        else:
            prev.next = l1


        # Finally return the prehead
        return prehead.next
