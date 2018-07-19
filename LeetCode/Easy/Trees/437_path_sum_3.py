# You are given a binary tree in which each node contains an integer value.
#
# Find the number of paths that sum to a given value.
#
# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
#
# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
#
# Example:
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
#
# Return 3. The paths that sum to 8 are:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # Running time : 800ms
    def pathSum_nlogn(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        # Time Complexity : O(N log N)

        if root is None:
            return 0

        # Get the number of paths starting from root
        paths_from_root = self.count_paths_from_given_node(root, sum, 0)


        # Get the number of paths starting from root.left
        paths_from_left = self.pathSum(root.left, sum)

        # Get the number of paths starting from root.left
        paths_from_right = self.pathSum(root.right, sum)

        return paths_from_root + paths_from_left + paths_from_right


    def count_paths_from_given_node(self, node, target_sum, current_sum):
        """
        Helper function
        """
        if node is None:
            return 0

        current_sum += node.val

        total_paths = 0
        if current_sum == target_sum:
            total_paths += 1

        total_paths += self.count_paths_from_given_node(node.left, target_sum, current_sum)
        total_paths += self.count_paths_from_given_node(node.right, target_sum, current_sum)


        return total_paths

    # Time COmplexity -> O(N)
    # Running time : 72 ms
    def pathSum_on(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        # Time Complexity : O(N)

        return self.count_paths_with_sum(root, sum, 0, {})


    def count_paths_with_sum(self, node, target_sum, running_sum, path_count):
        """
        A helper function
        """

        if node is None:
            return 0

        # Count all the paths with sum ending at the current node
        running_sum += node.val
        x = running_sum - target_sum
        total_paths = path_count.get(x, 0)

        # If running_sum == target_sum, we have to increment the total path count
        if running_sum == target_sum:
            total_paths += 1


        self.increment_dict(path_count, running_sum, 1)
        total_paths += self.count_paths_with_sum(node.left, target_sum, running_sum, path_count)
        total_paths += self.count_paths_with_sum(node.right, target_sum, running_sum, path_count)

        self.increment_dict(path_count, running_sum, -1)

        return total_paths


    def increment_dict(self, path_count, key, delta):
        """
        Another helper function
        """
        new_count = path_count.get(key, 0) + delta
        if new_count == 0:
            path_count.pop(key, None)
        else:
            path_count[key] = new_count
