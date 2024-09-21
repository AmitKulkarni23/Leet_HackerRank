# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
class Solution:
    def postorderTraversal(self, root):
        # Time Complexity - O(n) - need to visit all nodes
        # Space Complexity - O(n) - runtime recursion stack will include 1 call to the recursive function each time we visit a node
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
    