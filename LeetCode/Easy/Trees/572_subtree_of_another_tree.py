# Given two non-empty binary trees s and t, check whether tree t
# has exactly the same structure and node values with a subtree of s.
# A subtree of s is a tree consists of a node in s and all of this node's descendants.
# The tree s could also be considered as a subtree of itself.

#
# Example 1:
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree of s.
# Example 2:
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# Given tree t:
#    4
#   / \
#  1   2
# Return false.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        #Credits -> https://leetcode.com/problems/subtree-of-another-tree/discuss/102729/Short-Python-by-converting-into-strings

        return self.do_pre_order_traversal(t) in self.do_pre_order_traversal(s)

    def do_pre_order_traversal(self, node, x_string):
        """
        Helper function
        """
        if not node:
            return "$"

        return "^" + str(node.val) + "#" + self.do_pre_order_traversal(node.left) + self.do_pre_order_traversal(node.right)

    # Time Complexity O(m * n)
    # Space Complexity : O(n) -> where n is the number of nodes in s
    def best_leetcode_sol(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return traverse(s,t);

    def equals(x, y):
        """
        Helper function
        """
        if not x and not y:
            return True
        if x is None or y is None:
            return False
        return x.val==y.val and equals(x.left,y.left) and equals(x.right,y.right)

    def traverse(s, t):
        """
        Helper Function
        """
        return s is not None and ( equals(s,t) or traverse(s.left,t) or traverse(s.right,t))
