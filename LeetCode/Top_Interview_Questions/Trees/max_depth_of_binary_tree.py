"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example:
Given binary tree [3,9,20,null,null,15,7]

return depth = 3

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # If the root node is None return the
        # depth of the tree as -1
        if not root:
            return 0
        
        # Recurse through left and right sub-trees
        left_count = self.maxDepth(root.left)
        right_count = self.maxDepth(root.right)
        
        
        # Adding 1 here so as to account for this current node
        return max(left_count, right_count) + 1