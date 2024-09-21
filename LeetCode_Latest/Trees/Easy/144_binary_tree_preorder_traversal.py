# https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        # Time Complexity - O(n) - need to visit all nodes
        # Space Complexity - O(n) - runtime recursion stack will include 1 call to the recursive function each time we visit a node
        # PreOrder traversal in-case of Binary Search Tree will result in ascending order
        if not root:
            # Base condition
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
    