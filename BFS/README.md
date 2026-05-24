# Breadth First Search
Working:
1. Instead of going deep, we are going to traverse level by level.
2. Supppose we have 3 levels, we are going to first visit Level 1. That will be the starting node.
3. Next the neighbours of starting node. Next, we go down to level 2 and visit the neighbours of neighbours.
4. We will go on like this until the entire graph is traversed.
5. Even though we have DFS, BFS exists because it finds the shortest path.
6. Both of them are used for different purposes and problems.

## Pseudo code
BFS(graph, start):

    create empty queue
    create visited set

    enqueue start node
    mark start as visited

    while queue is not empty:

        node = dequeue from queue

        print node

        for each neighbor of node:

            if neighbor not visited:

                mark neighbor visited
                enqueue neighbor

## Time complexity
O(V+E) -- Visits every vertex once and checks every edge once

## Space Complexity
O(V) -- stores all the visited nodes