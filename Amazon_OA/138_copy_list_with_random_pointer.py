# https://leetcode.com/problems/copy-list-with-random-pointer/

# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


# Credits -> https://leetcode.com/problems/copy-list-with-random-pointer/solution/
# Need to take care of cycles

###############################################
# Brute Force Approach:
# Time: O(N)
# Space : O(N) -> mainting hasmap and the stack space for recursion calls
# if head in self.visitedHash:
#     return self.visitedHash[head]
#
# # create a new node
# # with the value same as old node.
# node = Node(head.val, None, None)
#
# # Save this value in the hash map. This is needed since there might be
# # loops during traversal due to randomness of random pointers and this would help us avoid them.
# self.visitedHash[head] = node
#
# # Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer.
# # Thus we have two independent recursive calls.
# # Finally we update the next and random pointers for the new node created.
# node.next = self.copyRandomList(head.next)
# node.random = self.copyRandomList(head.random)
#
# return node
###############################################

# Time Complexity : O(N)
# Space Complexity : O(1)

class Solution:

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        old_head = head

        # The below while loop will create something like
        # A->A'->B->B'->C->C' i.e. place new nodes adjacent to their old nodes by using the next pointer
        while old_head:
            new_node = Node(old_head.val, None, None)

            new_node.next = old_head.next
            old_head.next = new_node

            old_head = new_node.next

        old_head = head

        # Correctly linking the random pointers
        while old_head:
            # i.e A'.random = A.random.next if A.random else None
            old_head.next.random = old_head.random.next if old_head.random else None
            old_head = old_head.next.next

        old_list_head = head
        new_list_head = head.next
        answer = head.next

        # Separating the lists
        # A->B->C
        # A'->B'->C'
        while old_list_head:
            old_list_head.next = old_list_head.next.next
            new_list_head.next = new_list_head.next.next if new_list_head.next else None

            # Move to the next item
            old_list_head = old_list_head.next
            new_list_head = new_list_head.next

        # return the head of the newly created list
        return answer

