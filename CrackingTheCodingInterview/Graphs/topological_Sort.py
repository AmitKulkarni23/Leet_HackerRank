# Inspired by:
# https://algocoding.wordpress.com/2015/04/05/topological-sorting-python/

from collections import deque

def kahn_topological_sort(graph):
    """
    Implementing Kahn's algorithm for topological sorting
    """

    # Initially marking the in_degree of all the vertices as 0
    in_degree = { u : 0 for u in graph}

    # Marking appropriately the in-degree of vertices
    for u in graph:
        for v in graph[u]:
            # Increment the in_degree of all such vertices
            in_degree[v] += 1

    # Initialize a double ended queue

    Q = deque()

    # Add all the elements from the graph to queue whose in degree is 0
    for node in in_degree:
        if in_degree[node] == 0:
            # Append such a node
            Q.appendleft(node)


    # Initialize an empty list
    final_list = []

    while Q:
        u = Q.pop()
        final_list.append(u)

        for v in graph[u]:
            # Decrememnting the in-degree of all the vertices connected from u
            # bcause we are removing the vertex u
            in_degree[v] -= 1
            if in_degree[v] == 0:
                Q.appendleft(v)


    # If the length of the final_list and the number of vertices match then we
    # have a topological sort
    if len(final_list) == len(graph):
        return final_list
    else:
        return []


# Example:
graph4 = { 0 : [1, 2],
           1 : [3, 4],
           2 : [],
           3 : [],
           4 : [],
           5 : [6, 7],
           6 : [],
           7 : [] }

print("Starting the Kahn topological sort")

result = kahn_topological_sort(graph4)
print(result)
for item in result:
    print(item)
