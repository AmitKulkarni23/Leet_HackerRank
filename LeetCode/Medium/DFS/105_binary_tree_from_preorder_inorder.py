#
# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # NOTE: Draw and binary tree and write down pre-order and inorder traversals
        # Credits -> https://articles.leetcode.com/construct-binary-tree-from-inorder-and-preorder-postorder-traversal/

        # tree's root node always correspons to 1st element in pre-order traversal
        if len(preorder) == 0:
            return None

        # First we will build our root node
        root_node = TreeNode(preorder[0])

        # Ok, what are the left and right subtrees of this node?

        # All elements to the left of this node( in the inorder list)
        # appear in the left-subtree. Similarly all elemnst to the right
        # appear in the right subtree

        # We need to find the index of this value in the inorder list
        # Lets call this j

        j = inorder.index(preorder[0])

        # Now recurse
        root_node.left = self.buildTree(preorder[1:j], inorder[0:j])
        root_node.right = self.buildTree(preorder[j+1:], inorder[j+1:])

        return root_node
