# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # Idea -> Get all the root-to-leaf paths
        # Check if there is atleast 1 root-to-leaf path with sum of node values = sum
        # If yes, break out of the loop and return True

        # Idea -> Get all the root-to-leaf paths
        # Check if there is atleast 1 root-to-leaf path with sum of node values = sum
        # If yes, break out of the loop and return True

        stack = []

        if root:
            stack.append((root, root.val))

        while stack:
            node, actual_value = stack.pop()

            if node:
                if node.left is None and node.right is None:
                    # That means we are at the leaf nodes, there are
                    # no more nodes to traverse
                    if actual_value == sum:
                        return True

                # Else, append these nodes to stack
                if node.left:
                    stack.append((node.left, node.left.val + actual_value))
                if node.right:
                    stack.append((node.right, node.right.val + actual_value))


        return False
