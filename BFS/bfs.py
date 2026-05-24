from collections import deque

def bfs(graph, start):

    visited = set()
    queue = deque()
    result=[]

    visited.add(start)
    queue.append(start)

    while queue:

        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:

            if neighbor not in visited:

                visited.add(neighbor)
                queue.append(neighbor)

    return result