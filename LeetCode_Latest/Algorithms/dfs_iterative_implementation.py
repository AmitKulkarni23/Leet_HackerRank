def dfs(graph, start_node):
    visited = [False] * len(graph)

    stack = [start_node]
    while stack:
        top_node = stack[-1]
        stack.pop()

        if visited[top_node] == False:
            print("Visiting ", top_node)
            visited[top_node] = True

        if top_node in graph:
            for neighbor in graph[top_node]:
                if not visited[neighbor]:
                    stack.append(neighbor)


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

dfs(graph, 1)

