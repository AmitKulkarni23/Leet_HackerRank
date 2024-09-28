def bfs(graph, start_node):
    visited = [False] * len(graph)

    queue = [start_node]

    while len(queue):
        first_node = queue.pop(0)

        if not visited[first_node]:
            print("Visiting ", first_node)
            visited[first_node] = True
        
        # Check if there is an outgoing edge from this graph
        if first_node in graph:
            for neighbor in graph[first_node]:
                if not visited[neighbor]:
                    queue.append(neighbor)

# Example
graph = {
    0: [1],
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [6],
    6: []
}

bfs(graph, 1)
    