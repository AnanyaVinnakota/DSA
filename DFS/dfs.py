def dfs(graph, start):

    visited = []

    def dfs_func(node):

        if node not in visited:

            visited.append(node)

            for neighbor in graph[node]:
                dfs_func(neighbor)

    dfs_func(start)

    return visited
    
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    result = dfs(graph, 'A')
    print("DFS Traversal:")
    print(result)