# We are given head, the head node of a linked list containing unique integer values.
#
# We are also given the list G, a subset of the values in the linked list.
#
# Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.
#
# Example 1:
#
# Input:
# head: 0->1->2->3
# G = [0, 1, 3]
# Output: 2
# Explanation:
# 0 and 1 are connected, so [0, 1] and [3] are the two connected components.
# Example 2:
#
# Input:
# head: 0->1->2->3->4
# G = [0, 3, 1, 4]
# Output: 2
# Explanation:
# 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
# Note:
#
# If N is the length of the linked list given by head, 1 <= N <= 10000.
# The value of each node in the linked list will be in the range [0, N - 1].
# 1 <= G.length <= 10000.
# G is a subset of all values in the linked list.
# Definition for singly-linked list.

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        # Credits: https://leetcode.com/problems/linked-list-components/solution/

        if head and G:

            # Transfer all elements from list to a dictionary
            my_dict = {}
            for i, item in enumerate(G):
                my_dict[item] = i

            current_node = head
            connected_components = 0


            while current_node:
                if current_node.val in my_dict and (current_node.next is None or current_node.next.val not in my_dict):
                    connected_components += 1

                current_node = current_node.next


        return connected_components


        def best_leet_code_sol(self, head, G):
            """
            :type head: ListNode
            :type G: List[int]
            :rtype: int
            """
            # The above method makes 2 passes through teh linked list
            # The below method does only 1 pass

            # Use 2 pointers. Maintain distance of n nodes between the 1st and 2nd pointer
            # second + n = first

            # Move first pointer to teh last node
            # Now the second pointer is at the nth node from the last
            # Delete the node pointed by teh second pointer


            # Intially create a dummy node
            dummy = ListNode(0)
            dummy.next = head
            first = dummy
            second = dummy

            for i in range(1, n + 2):
                first = first.next

            while first is not None:
                first = first.next
                second = second.next

            second.next = second.next.next

            return dummy.next
