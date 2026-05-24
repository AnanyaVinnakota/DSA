from bfs import bfs


# Basic connected graph
def test_basic_graph():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': []
    }

    assert bfs(graph, 'A') == ['A', 'B', 'C', 'D', 'E', 'F']


# Graph containing a cycle
def test_graph_with_cycle():
    graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A', 'D'],
        'D': []
    }

    assert bfs(graph, 'A') == ['A', 'B', 'C', 'D']


# Disconnected graph
def test_disconnected_graph():
    graph = {
        'A': ['B'],
        'B': [],
        'C': ['D'],
        'D': []
    }

    assert bfs(graph, 'A') == ['A', 'B']


# Graph with duplicate neighbors
def test_duplicate_neighbors():
    graph = {
        'A': ['B', 'B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }

    assert bfs(graph, 'A') == ['A', 'B', 'C', 'D']


# Single node graph
def test_single_node():
    graph = {
        'A': []
    }

    assert bfs(graph, 'A') == ['A']


# Empty adjacency lists everywhere
def test_all_empty_lists():
    graph = {
        'A': [],
        'B': [],
        'C': []
    }

    assert bfs(graph, 'A') == ['A']


# Large branching graph
def test_large_branching_graph():
    graph = {
        1: [2, 3, 4],
        2: [5, 6],
        3: [7, 8],
        4: [9],
        5: [],
        6: [],
        7: [],
        8: [],
        9: []
    }

    assert bfs(graph, 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Graph with self loop
def test_self_loop():
    graph = {
        'A': ['A', 'B'],
        'B': ['C'],
        'C': []
    }

    assert bfs(graph, 'A') == ['A', 'B', 'C']


# Integer graph with cycles
def test_integer_graph_with_cycle():
    graph = {
        1: [2, 3],
        2: [4],
        3: [4],
        4: [1, 5],
        5: []
    }

    assert bfs(graph, 1) == [1, 2, 3, 4, 5]


# Deep graph
def test_deep_graph():
    graph = {
        1: [2],
        2: [3],
        3: [4],
        4: [5],
        5: [6],
        6: []
    }

    assert bfs(graph, 1) == [1, 2, 3, 4, 5, 6]