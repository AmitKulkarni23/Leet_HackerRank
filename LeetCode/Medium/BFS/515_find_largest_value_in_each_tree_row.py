# You need to find the largest value in each row of a binary tree.
#
# Example:
# Input:
#
#           1
#          / \
#         3   2
#        / \   \
#       5   3   9
#
# Output: [1, 3, 9]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        final_answer = []
        queue = []

        # If there is no element present in the tree
        if root is None:
            return final_answer

        queue.append(root)

        while len(queue):
            final_answer.append(max(node.val for node in queue))

            # Create a copy of the queue
            temp_queue = queue[:]
            queue = []

            for node in temp_queue:
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return final_answer
