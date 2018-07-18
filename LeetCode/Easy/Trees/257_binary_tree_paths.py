# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Input:
#
#    1
#  /   \
# 2     3
#  \
#   5
#
# Output: ["1->2->5", "1->3"]
#
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        final_list = []

        if root == None:
            return []

        self.binary_tree_helper(root, final_list, "")
        return final_list

    def binary_tree_helper(self, root, final_list, path):
        """
        A helper function
        """

        if root.left == None and root.right == None:
            final_list.append(path + str(root.val))

        if root.left != None:
            self.binary_tree_helper(root.left, final_list, path + str(root.val) + "->")

        if root.right != None:
            self.binary_tree_helper(root.right, final_list, path + str(root.val) + "->")

    # Iterative Solution
    # Credits -> https://leetcode.com/submissions/detail/164483866/
    def binaryTreePaths_iterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans=[]
        stack=[]
        stack.append((root,""))

        while stack:

            node,path=stack.pop()

            if node:
                if node.left is None and node.right is None:
                    ans.append(path+str(node.val))

                stack.append((node.left,path+str(node.val)+"->"))
                stack.append((node.right,path+str(node.val)+"->"))

        return ans
