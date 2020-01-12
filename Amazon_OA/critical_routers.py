# https://leetcode.com/discuss/interview-question/436073/

"""

You are given an undirected connected graph. An articulation point (or cut vertex)
is defined as a vertex which, when removed along with associated edges,
makes the graph disconnected (or more precisely, increases the number of
connected components in the graph). The task is to find all articulation points
in the given graph.

Input:
The input to the function/method consists of three arguments:

numNodes, an integer representing the number of nodes in the graph.
numEdges, an integer representing the number of edges in the graph.
edges, the list of pair of integers - A, B representing an edge between the nodes A and B.
Output:
Return a list of integers representing the critical nodes.

"""

from collections import defaultdict
def findcriticalnodes(n, edges):
    # Tarjan's algorithm
    # Keep track of visited time and low time for all vertices in the graph
    # A vertex is an articulation point if:
        # - it is a root vertex with atleast 2 independent children
        # - visited time of vertex <= low time of any adjacent vertex

    # Time Complexity: O(V + E) - DFS algortihm
    # Create the graph
    g = defaultdict(list)
    for conn in edges:
        g[conn[0]].append(conn[1])
        g[conn[1]].append(conn[0])

    visited = [0]* n
    isarticulationpoints = [0]*n
    order = [0]*n
    low = [0]*n
    seq = 0

    def dfs(u, p):
        nonlocal seq
        visited[u] = 1
        order[u] = low[u] = seq
        seq = seq + 1
        children = 0
        for to in g[u]:
            if to == p:
                continue
            if visited[to]:
                low[u] = min(low[u], low[to])
            else:
                dfs(to, u)
                low[u] = min(low[u], low[to])
                if order[u] <= low[to] and p!= -1:
                    isarticulationpoints[u] = 1
                children += 1

        if p == -1 and children > 1:
            isarticulationpoints[u] = 1

    dfs(0, -1)
    ans = []
    for i in range(len(isarticulationpoints)):
        if isarticulationpoints[i]:
            ans.append(i)
    return ans

if __name__ == "__main__":
    a = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
    b = [[0, 1], [0, 2], [2, 1], [0, 3], [3, 4]]
    c = [[0, 1], [1, 2], [2, 3]]
    d = [[0, 1], [1, 2], [2, 0], [1, 3], [1, 4], [1, 6], [3, 5], [4, 5]]
    print(findcriticalnodes(7, d))
