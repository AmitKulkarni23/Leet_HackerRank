"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # Approach: Recursively traverse through
        # left and right subtrees
        
        if root is None:
            return 0
        
        # Base Case
        # If either right node or teh left node is a leaf node
        # tehn this accounts for height==1
        if root.right is None and root.left is None:
            return 1
        
        # If the right subtree is None
        # Recurse through the left subtree
        if root.right is None:
            return self.minDepth(root.left) + 1
        
        # Recurse through the right subtree
        if root.left is None:
            return self.minDepth(root.right) + 1
        
        left_count = self.minDepth(root.left)
        right_count = self.minDepth(root.right)
        
        # Select the min among these 2 values
        # Adding 1(to account for this node) and returning this value 
        return min(left_count, right_count) + 1