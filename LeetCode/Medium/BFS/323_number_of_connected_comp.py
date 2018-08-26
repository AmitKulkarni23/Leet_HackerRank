# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.
#
# Example 1:
#
# Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
#
#      0          3
#      |          |
#      1 --- 2    4
#
# Output: 2
# Example 2:
#
# Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
#
#      0           4
#      |           |
#      1 --- 2 --- 3
#
# Output:  1
# Note:
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
#

def countComponents(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: int
    """
    # We will use DFS traversal methods to solve this problem
    # Create a list with booleans False to show that none of the nodes have been visited first

    visited_nodes = [False] * n

    # One nod ecna have multiple edges
    adj_dict = {x : [] for x in range(n)}

    final_answer = 0

    # Create a dictionary
    # Create a reverse edge as well
    for x, y in edges:
        adj_dict[x].append(y)
        adj_dict[y].append(x)


    for i in range(n):
        if not visited_nodes[i]:
            # Call the DFS method and increment the count
            dfs(i, visited_nodes, adj_dict)
            final_answer += 1

    return final_answer


def dfs(node, visited_nodes, adj_dict):
    """
    Method which performs a DFS traversal
    """
    if visited_nodes[node]:
        return

    # Else this node was never visited
    visited_nodes[node] = True

    for neighbor in adj_dict[node]:
        # Do a DFS
        dfs(neighbor, visited_nodes, adj_dict)


# Example:
n = 5
edges = [[0, 1], [1, 2], [3, 4]]


n = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 4]]


n = 2
edges = [[1, 0]]
print("The number of connected components are ", countComponents(n, edges))
