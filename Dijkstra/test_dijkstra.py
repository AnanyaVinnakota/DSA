from dijkstra import dijkstra


# Basic weighted graph
def test_basic_graph():

    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    assert dijkstra(graph, 'A') == {
        'A': 0,
        'B': 1,
        'C': 3,
        'D': 4
    }


# Graph with disconnected node
def test_disconnected_graph():

    graph = {
        'A': {'B': 2},
        'B': {'A': 2},
        'C': {}
    }

    assert dijkstra(graph, 'A') == {
        'A': 0,
        'B': 2,
        'C': float('inf')
    }


# Graph with single node
def test_single_node():

    graph = {
        'A': {}
    }

    assert dijkstra(graph, 'A') == {
        'A': 0
    }


# Graph with multiple shortest updates
def test_multiple_relaxations():

    graph = {
        'A': {'B': 10, 'C': 1},
        'B': {'D': 2},
        'C': {'B': 1, 'D': 8},
        'D': {}
    }

    assert dijkstra(graph, 'A') == {
        'A': 0,
        'B': 2,
        'C': 1,
        'D': 4
    }


# Graph with zero weight edges
def test_zero_weight_edges():

    graph = {
        'A': {'B': 0, 'C': 2},
        'B': {'C': 1},
        'C': {'D': 0},
        'D': {}
    }

    assert dijkstra(graph, 'A') == {
        'A': 0,
        'B': 0,
        'C': 1,
        'D': 1
    }