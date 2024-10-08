# https://leetcode.com/problems/binary-tree-inorder-traversal/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Inorder traversal - Visit the left child + visit the node + visit the right child
    # Time Complexity - O(n) - need to visit all nodes
    # Space Complexity - O(n) - runtime recursion stack will include 1 call to the recursive function each time we visit a node
    def inorderTraversal(self, root):
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)