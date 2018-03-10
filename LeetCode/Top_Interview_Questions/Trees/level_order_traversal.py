"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7]

Return:
[
  [3],
  [9,20],
  [15,7]
]

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    # Maintaining a list here, so that it is accessible
    # to all the member functions
    
    def __init__(self):
        self.level_list = []
    
    
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        # Call the helper function
        return self.levelOrderHelper(root, 0)
        
        
    
    def levelOrderHelper(self,node, level):
        """
        Recursively call this function
        """
        if not node:
            return []
        
        if level < len(self.level_list):
            self.level_list[level].append(node.val)
        else:
            # Create a new sub-list
            self.level_list.append([node.val])
            
        # Recurse
        self.levelOrderHelper(node.left, level + 1)
        self.levelOrderHelper(node.right, level + 1)
        
        return self.level_list