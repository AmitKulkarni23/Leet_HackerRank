# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
#
# Example:
#
# Input: 3
# Output:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

####################################


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def generate_trees_helper(self, start, end):
        """
        A helper function to construct all unique BSTs
        :type start: int
        :type: end: int
        :rtype: List[TreeNode]
        """
        # Initilaizing list of BSTs as empty
        bst_list = []

        # Base Condition
        if start > end:
            bst_list.append(None)
            return bst_list

        # Itearting thorugh all the values from 1 to N
        for i in range(start, end+1):

            # Constructing the left subtree
            left_subtree = self.generate_trees_helper(start, i - 1)

            right_subtree = self.generate_trees_helper(i+1, end)


            # Now loop through the left_subtree and right_subtree lists
            # that are recursive generated and connect them to the ith node

            for j in range(len(left_subtree)):
                left = left_subtree[j]

                # Loop through the right subtree
                for k in range(len(right_subtree)):
                    right = right_subtree[k]

                    # Make i as a node
                    new_node = TreeNode(i)
                    new_node.left = left
                    new_node.right = right
                    bst_list.append(new_node)

        return bst_list

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        my_list = self.generate_trees_helper(1, n)

        for i in my_list:
            self.pre_order_traversal(i)
            print("Done")

    def pre_order_traversal(self, root):
        """
        Helper function taht prints the peroder traversal of a tree
        """
        if root:
            print(root.val)
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)


my_solution_object = Solution()
my_solution_object.generateTrees(3)
