# https://leetcode.com/problems/sum-of-left-leaves/description/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # Time Complexity - O(n) - need to visit the whole tree
        # Space Complexity - O(n) - runtime recursion stack will be helper() calss to the whole length of the tree
        
        def helper(node, isLeft):
            if node is None:
                return 0
            if node.left is None and node.right is None and isLeft:
                return node.val
            return helper(node.left, True) + helper(node.right, False)

        
        return helper(root, False)


