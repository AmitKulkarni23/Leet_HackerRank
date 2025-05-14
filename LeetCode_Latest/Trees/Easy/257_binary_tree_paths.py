# https://leetcode.com/problems/binary-tree-paths/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        stack = [(root, "")] # node, path
        result = []
        
        while stack:
            node, path = stack.pop()
            
            if node.left is None and node.right is None:
                result.append(path + str(node.val))
            
            if node.left:
                stack.append((node.left, path + str(node.val) + "->"))
                
            if node.right:
                stack.append((node.right, path + str(node.val) + "->"))
        
        print(result)
        return result
            
            