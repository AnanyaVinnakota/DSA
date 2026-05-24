## Depth-First-Search(DFS)

WORKING:

1. It is a stack traversal.Start from the parent node and go down until the last child. 
2. After the last child, backtrack to the previous parent and go to the unvisited neighbour.
3. Repeat the process until the entire graph or tree is traversed and every node is visited.

## Pseudocode
DFS(node):

    Mark node as visited
    Print node

    FOR each neighbor of node:
        IF neighbor is not visited:
            DFS(neighbor)

## Time Complexity
O(V+E) --Each node is visited once and each edge is checked once
O(V) --In a tree, Edges=Vertices-1

# Special Cases
Sparse Graph --O(V) -- Very few edges
Dense Graph --O(V²) --Almost every node is connected to every other node

## Space Complexity
O(V) --Stores all the visited nodes
