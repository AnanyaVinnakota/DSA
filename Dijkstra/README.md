# Dijkstra Algorithm
Working:
1. It is a greedy algorithm which finds the shortest distance of the node all the time.
2. We have to take a starting node and find the distances of the node itself and other nodes from it.
3. Then we have to go to the neighbouring nodes and if we find any distance shorter, then we have to update the old distance.
4. The main motive of this algorithm is to find shortest distances of nodes from the starting node.

## Pseudo Code
DIJKSTRA(graph, start):

    create distance dictionary
    set all distances = infinity

    dist[start] = 0

    create priority queue
    insert (0, start)

    while priority queue != empty:

        remove node with smallest distance

        for each neighbor:

            new_distance = current_distance + edge_weight

            if new_distance < known distance:

                update distance
                push into priority queue

    return distances

## Time complexity
O((V+E)log V)
Algorithm does two main things:
1. Remove minimum node from heap
2. Insert updated distances to heap
And heap uses O(log V) and normal graph is O(V+E)

## Space Complexity
O(V) --stores distance dictionary