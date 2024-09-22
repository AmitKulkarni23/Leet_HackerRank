# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        # Space Complexity in a Balanced Tree:
        # The space complexity is driven by the recursion stack, and in the case of a balanced tree, the maximum depth of recursive calls is limited by the height of the tree.

        # Why is Space Complexity O(log N)?
        # In a recursive depth-first search (DFS), the recursive calls go down one path of the tree at a time. The maximum depth of the recursive stack corresponds to the height of the tree. In a balanced binary tree, the height of the tree is approximately log(N)

        # Since the tree is balanced, every level of the tree roughly doubles the number of nodes. This results in a height of approximately log(N)

        # The recursive stack will store information for each level of the tree as it traverses down a path. For a balanced tree, the maximum number of levels (and thus the maximum recursion depth) is approximately log(N)
        if not root:
            return 0

        # If one of the subtrees is None, consider only the other subtree
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1

        # If both subtrees exist, take the minimum depth of both
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1