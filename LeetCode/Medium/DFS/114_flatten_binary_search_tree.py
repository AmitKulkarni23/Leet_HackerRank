# Given a binary tree, flatten it to a linked list in-place.
#
# For example, given the following tree:
#
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like:
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        # Credits -> https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/36991/Accepted-simple-Java-solution-iterative
        if not root:
            return None

        # We will use DFS and set left child to None
        stack = []
        stack.append(root)

        while len(stack):
            curr = stack.pop()

            # Append the right node first to the stack
            if curr.right:
                stack.append(curr.right)

            # Append left node next
            if curr.left:
                stack.append(curr.left)

            if len(stack):
                # If there is some elemnet in the stack
                # The top of the stack( usually the left element) should be set as
                # this node's right child
                curr.right = stack[-1]

            # Set curr.left as null
            curr.left = None
