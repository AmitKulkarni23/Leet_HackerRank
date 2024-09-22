# https://leetcode.com/problems/path-sum/

class Solution:
    def hasPathSum(self, root, targetSum):
        def helper(node, target):
            if node:
                if self.isLeaf(node) and target - node.val == 0:
                    return True
                return helper(node.left, target - node.val) or helper(node.right, target - node.val)
        
        return helper(root, targetSum)
        

    def isLeaf(self, node):
        return node.left is None and node.right is None