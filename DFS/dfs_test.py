from dfs import dfs


# Simple connected graph
def test_simple_graph():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': []
    }

    assert dfs(graph, 'A') == ['A', 'B', 'D', 'E', 'C', 'F']


# Graph with cycle
def test_graph_with_cycle():
    graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['A', 'D'],
        'D': []
    }

    assert dfs(graph, 'A') == ['A', 'B', 'C', 'D']


# Disconnected graph
def test_disconnected_graph():
    graph = {
        'A': ['B'],
        'B': [],
        'C': ['D'],
        'D': []
    }

    assert dfs(graph, 'A') == ['A', 'B']


# Graph with self loop
def test_self_loop():
    graph = {
        'A': ['A', 'B'],
        'B': ['C'],
        'C': []
    }

    assert dfs(graph, 'A') == ['A', 'B', 'C']


# Complex graph with multiple cycles
def test_complex_graph():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': ['C'],
        'E': ['F', 'G'],
        'F': ['A'],
        'G': []
    }

    assert dfs(graph, 'A') == ['A', 'B', 'D', 'C', 'F', 'E', 'G']