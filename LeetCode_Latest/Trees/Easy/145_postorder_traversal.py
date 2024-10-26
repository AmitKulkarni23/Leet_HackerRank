# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
class Solution:
    def postorderTraversal(self, root):
        # Time Complexity - O(n) - need to visit all nodes
        # Space Complexity - O(n) - runtime recursion stack will include 1 call to the recursive function each 
        # time we visit a node
        # Why O(h)??
        # Recursion follows only one path at a time (from root to a leaf node).
        # The deepest path in the tree determines the maximum depth of the recursion, which is the height of the tree.
        # Therefore, the space required by the recursion stack is proportional to the height of the tree: 
        # O(logn) for a balanced tree and 
        # O(n) for a skewed tree.


        # At any given time, the recursion only processes nodes along a single path from the root to a leaf node.
        # The maximum number of recursive calls on the stack is equal to the height of the tree. Each recursive call corresponds to visiting one level deeper.
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
    