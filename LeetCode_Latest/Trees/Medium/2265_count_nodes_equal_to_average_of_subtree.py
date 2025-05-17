# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root) -> int:
        self.result = 0

        def helper(node):
            if not node:
                # Sum, count
                return [0, 0]

            left_tree_sum, left_count = helper(node.left) 
            right_tree_sum, right_count = helper(node.right)

            # Need to add the current node.val and 1 to the denominator
            avg = (left_tree_sum + right_tree_sum + node.val) // (left_count + right_count + 1)

            if avg == node.val:
                self.result += 1

            return [left_tree_sum + right_tree_sum + node.val, left_count + right_count + 1]
        
        helper(root)
        return self.result

        