# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#
# Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
#
#         _______6______
#        /              \
#     ___2__          ___8__
#    /      \        /      \
#    0      _4       7       9
#          /  \
#          3   5
# Example 1:
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:
#
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself
#              according to the LCA definition.
# Note:
#
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the BST.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Given p and q will exist in the BST, therefore no need to check
        # if the root covers both the values

        return self.ancestor_helper(root, p, q)


    def ancestor_helper(self, root, p, q):
        """
        Helper Function
        """
        # Root is teh common ancestor
        if root == None or root == p or root == q:
            return root

        # Else check if p is on left or q is on left
        # If they both are on the left side, branch left
        # If they both are on the right branch right

        # If one is on left and one is on right
        # we have found the common ancestor

        is_p_on_left = self.covers(root.left, p)
        is_q_on_left = self.covers(root.left, q)

        if is_p_on_left != is_q_on_left:
            # That means they are on different bramnches of the tree
            return root

        # On the same branch
        if is_p_on_left:
            child_side = root.left
        else:
            child_side = root.right
        # Now wrecurse
        return self.ancestor_helper(child_side, p, q)

    def covers(self, root, p):
        """
        Helper function
        """
        if root is None:
            return False

        if root == p:
            return True

        return self.covers(root.left, p) or self.covers(root.right, p)

    # Runtime 68ms
    # Credits -> https://leetcode.com/submissions/detail/164512886/
    def best_leetcode_sol(self, root, p, q):
        if not root or not p or not q:
            return None
        while root:
            if root.val>p.val and root.val >q.val:
                root=root.left
            elif root.val<p.val and root.val<q.val:
                root=root.right
            else:
                return root
