# Given a linked list, rotate the list to the right by k places, where k is non-negative.
#
# Example 1:
#
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
# Example 2:
#
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL


##########################################################

# My solution : Runtime 24ms
# Beats -> 100 %
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if k == 0:
            # There is no need to rotate
            return head

        # Find teh lenght of teh linked list
        ll = self.findLength(head)

        if ll == 0:
            # There is no element in teh linked list
            return None

        if k % ll == 0:
            # If k is a multiple of linked list lenght
            # just return head
            return head

        if ll == 1:
            # If there is only one element in teh linked list
            return head

        if ll == k:
            return head
        elif ll > k:
            return self.rotate_helper_function(head, k, ll)
        else:
            # here teh value of k is higher than the value of ll
            # Take k % ll
            return self.rotate_helper_function(head, (k % ll), ll)

    def rotate_helper_function(self, head, k, ll):
        """
        A helper function that will work both when k > ll and k < ll
        """
        # Now traverse to ll - k position in teh linked list
        cur = head

        inner_count = 0
        while inner_count != (ll - k - 1):
            cur = cur.next
            inner_count += 1

        # Now we have reached teh node wherein we want to make
        # teh next value as NULL
        # Should do temp.next = None
        temp = cur

        # Now the list is disconnected
        # Iterate through to teh end of teh linked list and connect tot to the head
        # SHOULD RETURN temp_head
        temp_head = cur.next
        # Move to the last node in the list
        while cur.next != None:
            cur = cur.next

        # Reconnect the last node of teh broken list to teh initial head
        cur.next = head
        temp.next = None

        # Return the new head of the list
        return temp_head



    def findLength(self, node):
        """
        Function to find teh lenght of the linked list
        """
        count = 0
        curr = node
        while curr:
            curr = curr.next
            count += 1

        return count

    def printList(self, node):
        """
        Helper function to print teh linked list
        """
        temp = node

        while temp:
            print(temp.val)
            temp = temp.next



# Examples:
x1 = ListNode(1)
x2 = ListNode(2)
x3 = ListNode(3)
x4 = ListNode(4)
x5 = ListNode(5)

x1.next = x2
x2.next = x3
x3.next = x4
x4.next = x5


sol = Solution()
sol.printList(x1)


new_head = sol.rotateRight(x1, 10)
sol.printList(new_head)

print("##################")

a1 = ListNode(0)
a2 = ListNode(1)
a3 = ListNode(2)

a1.next = a2
a2.next = a3


sol.printList(a1)
new_head_2 = sol.rotateRight(a1, 4)
print("Done rotating")
sol.printList(new_head_2)
