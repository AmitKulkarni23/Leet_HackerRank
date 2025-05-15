# https://leetcode.com/problems/print-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root):
        height = self.get_tree_height(root)

        m = height + 1
        n = (2 ** m) - 1

        result = [["" for _ in range(n)] for _ in range(m)]
        self.fill(result, root, 0, 0, n - 1)

        return result
    

    def fill(self, result, node, row, left, right):
        if not node:
            return
        
        # The key insight is the calculation of mid here
        # We have to know that res[0][(n-1)/2] is essentially mid
        mid = (left + right) // 2
        result[row][mid] = str(node.val)

        self.fill(result, node.left, row + 1, left, mid - 1)
        self.fill(result, node.right, row + 1, mid + 1, right)
    
    def get_tree_height(self, node):
        if not node:
            return -1
        left_height = self.get_tree_height(node.left)
        right_height = self.get_tree_height(node.right)

        return max(left_height, right_height) + 1