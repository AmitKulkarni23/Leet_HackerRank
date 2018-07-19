# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum_recursive(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        final_ans = []
        self.dfs(root, sum, [], final_ans)

        return final_ans

    def dfs(self, node, sum, sum_list, final_ans):
        """
        Helper Function
        """
        if not node.left and not node.right and sum == node.val:
            # We ahev reached the end and the sum of root to leaf nodes equals the given sum
            sum_list.append(node.val)
            final_ans.append(sum_list)

        if node.left:
            self.dfs(node.left, sum - node.val, sum_list + [node.val], final_ans)
        if node.right:
            self.dfs(node.right, sum - node.val, sum_list + [node.val], final_ans)


    def path_sum_iterative(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        # Iterative SOlution to the above problem
        ans = []
        stack = []

        if root:
            stack = [(root, sum - root.val, [root.val])]

        while stack:
            # Now consider an element one by one
            node, val, sum_list = stack.pop()

            # If we have reached the leaf node
            if node.left is None and node.right is None and val == 0:
                # Then append the intermediate list ot the outer list
                ans.append(sum_list)

            if node.left:
                stack.append((node.left, val - node.left.val, sum_list + [node.left.val]))

            if node.right:
                stack.append((node.right, val - node.right.val, sum_list + [node.right.val]))

        return ans
