# Merge 2 sorted linked lists
# Return the new merged list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# My Solution - Very poor performance - beats only 26% of python submissions
# Runtime for 208 test cases = 88ms
# Sometimes - this is giving a runtime of 60ms

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # Iterate through the first list
        # and store all the values of nodes in a
        # list
        first_ll_values = []
        
        # If the second list is empty, return the
        # first list
        if not l2:
            return l1
        
        # If the first list is empty, return the
        # second list        
        if not l1:
            return l2
        
        # Iterate through the first list and capture all the values
        # in a list
        
        first_ll_values = []
        
        while l1:
            first_ll_values.append(l1.val)
            l1 = l1.next
        
        # Iterate through the second list and capture all the values
        # in a list
        
        second_ll_values = []
        
        while l2:
            second_ll_values.append(l2.val)
            l2 = l2.next
            
        # Now we have all the values in 2 lists
        # These lists should be merged and sorted
        sorted_merged_list = sorted(first_ll_values + second_ll_values)
        
        
        # Iterate through this sorted_merged_list and create
        # a new ListNode for each item and link the next for this item as the
        # next item in the list
        
        for i in range(len(sorted_merged_list) - 1):
            ListNode(sorted_merged_list[i]).next = sorted_merged_list[i+1]
            
        
        return sorted_merged_list
        
		
		# # Recursive Solution from discussion portal in
		# # Leetcode ( https://leetcode.com/problems/merge-two-sorted-lists/discuss/9735/Python-solutions-(iteratively-recursively-iteratively-in-place).)
		# # NOT MY SOLUTION
		# # Runtime : 76ms
		# if not l1 or not l2:
            # return l1 or l2
        # if l1.val < l2.val:
            # l1.next = self.mergeTwoLists(l1.next, l2)
            # return l1
        # else:
            # l2.next = self.mergeTwoLists(l1, l2.next)
            # return l2
        
        
        
		
		# # Iterative solution, in-place
		# # NOT MY SOLUTION
		# # Runtime : 68ms
		# if None in (l1, l2):
        # return l1 or l2
		# dummy = cur = ListNode(0)
		# dummy.next = l1
		# while l1 and l2:
			# if l1.val < l2.val:
				# l1 = l1.next
			# else:
				# nxt = cur.next
				# cur.next = l2
				# tmp = l2.next
				# l2.next = nxt
				# l2 = tmp
			# cur = cur.next
		# cur.next = l1 or l2
		# return dummy.next