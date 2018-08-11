# Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.
#
#
#
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
#
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
#
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
#
#
#
# Note:
#
# Both of the given trees will have between 1 and 100 nodes.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        # Credits -> https://leetcode.com/problems/leaf-similar-trees/solution/

        # Note: There is atleast 1 node in both binary trees
        # Idea : We will do a DFS search and add all the elements of root1
        # in 1 list and elements of root2 in another list
        # Finally return r1_list == l2_list
        r1_list = []
        r2_list = []

        self.dfs(root1, r1_list)
        self.dfs(root2, r2_list)

        return r1_list == r2_list

    def dfs(self, node, leaf_values):
        """
        Helper function which performs a DFS search and adds leaft values to
        the list 'leaf_values'
        """

        if node:
            # Base Case
            if node.left is None and node.right is None:
                leaf_values.append(node.val)

            self.dfs(node.left, leaf_values)
            self.dfs(node.right, leaf_values)
