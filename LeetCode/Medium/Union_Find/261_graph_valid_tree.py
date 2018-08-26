# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
#
# Example 1:
#
# Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
# Output: true
# Example 2:
#
# Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: false
# Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.


def validTree(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: bool
    """

    # Note: In tree there are no cycles
    # Note: In tree there is only one path between 2 node

    # We will use union find method to find if there are cycles
    if n - 1 != len(edges):
        # There are NOT (n - 1) edges
        return False

    # Create aprent list
    parent = list(range(n))

    # Iterate through the edges
    for x, y in edges:
        p_x = find(parent, x)
        p_y = find(parent, y)

        if p_x == p_y:
            # They have the same parent
            # There exists a cycle
            return False

        # Change the parent of the second elemnet to being the first element
        parent[p_y] = p_x

    return True

def find(parent, i):
    """
    The union find method
    """
    if parent[i] != i:
        parent[i] = find(parent, parent[i])

    return parent[i]


# Examples:
n = 5
edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
print(validTree(n, edges))
