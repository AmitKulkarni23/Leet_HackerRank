# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# Example:
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Credits -> https://leetcode.com/problems/merge-k-sorted-lists/solution/

        # Idea -> We know how to merge 2 sorted lists
        # So we will do pairwise merging of lists
        # Suppose there are 8 lists
        # merge(1,2), merge(3, 4), merge(5, 6), merge(7, 8)
        # So 8 reduced to 4 and 4 reduced to 2..
        # So in each merge operation we traverse N nodes
        # And we do merge operations for logk times

        # Time COmplexity -> O(N log k)

        k = len(lists)

        interval = 1

        while interval < k:
            for i in range(0, k - interval, interval * 2):
                lists[i] = self.merge_2_lists(lists[i], lists[i + interval])
            interval *= 2

        if k > 0:
            return lists[0]
        else:
            return lists


    def merge_2_lists(self, l1, l2):
        """
        Helper function
        """
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

        if l1 == None:
            prev.next = l2
        else:
            prev.next = l1


        # Finally return the prehead
        return prehead.next
