# Invert a binary tree.
#
# Example:
#
# Input:
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # Time COmplexity : O(n) -> n is teh number of nodes in teh tree
    # Space COmplexity -> O(n) -> The queue can contain all nodes in each level
                                # in the worst case
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        # We will try to use a iterative approach

        if root is None:
            return None

        queue = [root]

        while queue:
            current_node = queue.pop(0)

            # Swap the nodes
            temp = current_node.left
            current_node.left = current_node.right
            current_node.right = temp

            # Add left and right nodes to teh queue if they are present
            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)


        return root
