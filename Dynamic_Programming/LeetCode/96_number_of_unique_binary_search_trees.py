# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
#
# Example:
#
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

#####################

# Time Complexity -> O( n ^ 2)
# Space COmplexity : O(n)
def numTrees(n):
    """
    :type n: int
    :rtype: int
    """

    G = [0 for _ in range(n+1)]

    G[0] = G[1] = 1

    for i in range(2, n+1):
        for j in range(1, i+1):
            G[i] += G[j-1] * G[i-j]

    return G[n]

def num_trees_rec_helper(start, end):
    """
    A helper function for finding teh number of unique BSTs
    """

    # Base Condition
    if start >= end:
        return 1

    total_count = 0
    for i in range(start, end):
        total_count += num_trees_rec_helper(start, i - 1) + num_trees_rec_helper(i+1, end)

    return total_count

def num_trees_recursive_solution(n):
    """
    A recurisve solution to finding teh number of unique BSTs
    """
    return num_trees_rec_helper(1, n)

# Examples
print(numTrees(3))
print(num_trees_recursive_solution(3))
