# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
# Example 1:
#
# Given 1->2->3->4, reorder it to 1->4->2->3.
# Example 2:
#
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # Credits: https://leetcode.com/problems/reorder-list/discuss/129896/One-Short-and-Humorous-Python-Solution

        my_list = []
        while head:
            my_list.append(head)
            head = head.next

        left, right = 0, len(my_list) - 1
        while left <= right:
            my_list[left].next = my_list[right]

            if left + 1 < right:
                my_list[right].next = my_list[left+1]
            else:
                my_list[right].next = None

            # Increment left index and decrement right index
            left, right = left + 1, right - 1


    def printList(self, node):
        """
        Helper function to print teh linked list
        """
        temp = node

        while temp:
            print(temp.val)
            temp = temp.next


x1 = ListNode(1)
x2 = ListNode(2)
x3 = ListNode(3)

x1.next = x2
x2.next = x3

sol = Solution()

print("BEFORE")
sol.printList(x1)


print("AFTER")
sol.reorderList(x1)
sol.printList(x1)
