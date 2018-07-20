# Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.
#
# Example:
#
# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13
#
# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13


# IDEA :
# REVERSE IN-ORDER-TRAVERSAL
# The key to such a solution would be a way to visit nodes in descending order,
# keeping a sum of all values that we have already visited and adding that
# sum to the node's values as we traverse the tree. This method for tree
# traversal is known as a reverse in-order traversal, and allows us to guarantee
# visitation of each node in the desired order. The basic idea of such a traversal is
# that before visiting any node in the tree, we must first visit all nodes with
# greater value. Where are all of these nodes conveniently located? In the right subtree.



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Credits -> https://leetcode.com/problems/convert-bst-to-greater-tree/solution/

        total = 0
        stack = []

        node = root

        while stack or node is not None:
            # Push all the right nodes onto teh stack including thsi node
            stack.append(node)
            node - node.right

        # Now modify the node's value
        node = stack.pop()
        # Get the total of all teh greater-nodes that we have visited
        total += node.val

        # Reassign this node's value
        node.val = total

        # Now move to the left-subtrees of all the nodes
        node = node.left

    return root
