"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        
        # Approach: Get the middle of the array and make it the
        # root of the tree - Step 1
        
        # Get the mid point of the left_half of the array and make
        # it the left of the node obtained in Step1
        
        # Get the mid point of the right_half of the array and make
        # it the right of the node obtained in Step1
        
        
        # NOTE: THIS SOLUTION IS AN INSPIRATION FROM ONE
        # OF THE PYTHON SOLUTIONS PROVIDED IN THE DISCUSSION FORM
        # Citation: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/discuss/35343/Python-7-line-solution
        
        # Base Case
        if not nums:
            return None
			
		# Get the mid point first
        
        mid = len(nums) // 2
        
        # Creating the root node
		# Make the mid point as the root node
        root_node = TreeNode(nums[mid])
        
        # Creating the left node
        # Recurse through the left half of the array
        root_node.left = self.sortedArrayToBST(nums[:mid])
        
        # Creating the right node
        # Recurse through the right half of the array
        root_node.right = self.sortedArrayToBST(nums[mid + 1:])
        
        
        return root_node