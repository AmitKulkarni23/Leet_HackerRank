# Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.
#
# Example 1:
# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 9
#
# Output: True
# Example 2:
# Input:
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 28
#
# Output: False

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        # Time Complexity -> O(n) -> We might traverse through the whole binary tree
        # Space Complexity -> O(n) -> For the list and the set

        # We will use a BFS approach
        ele_set = set()

        # Initialize a queue
        my_q = []
        my_q.append(root)

        while my_q:
            if my_q[0] is not None:
                node = my_q.pop(0)

                if (k - node.val) in ele_set:
                    # There are 2 such elements
                    return True

                # If not, add this node to the set
                ele_set.add(node.val)
                # Add the left and right nodes to the queue
                my_q.append(node.left)
                my_q.append(node.right)

            else:
                my_q.pop(0)


        return False
