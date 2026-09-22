import time
import tracemalloc
import matplotlib.pyplot as plt

from dfs import dfs


# ---------------------------------------
# Generate a graph of a given size
# ---------------------------------------

def generate_graph(n):
    graph = {i: [] for i in range(n)}

    # Create a graph with limited depth
    # so recursive DFS does not exceed
    # Python's recursion limit.
    for i in range(1, n):
        parent = (i - 1) // 2
        graph[parent].append(i)

    return graph


# ---------------------------------------
# Measure execution time
# ---------------------------------------

def measure_time(graph, repetitions=10):

    times = []

    for _ in range(repetitions):

        start = time.perf_counter()

        dfs(graph, 0)

        end = time.perf_counter()

        times.append(end - start)

    average_time = sum(times) / len(times)

    return average_time


# ---------------------------------------
# Measure memory usage
# ---------------------------------------

def measure_memory(graph):

    tracemalloc.start()

    dfs(graph, 0)

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    return peak


# ---------------------------------------
# Input sizes
# ---------------------------------------

input_sizes = [10, 50, 100, 200, 500, 800]

execution_times = []
memory_usages = []


# ---------------------------------------
# Run benchmark
# ---------------------------------------

for n in input_sizes:

    graph = generate_graph(n)

    # Measure execution time
    time_taken = measure_time(graph)

    # Measure memory usage
    memory_used = measure_memory(graph)

    execution_times.append(time_taken)
    memory_usages.append(memory_used)

    print(
        f"Input size: {n:5d} | "
        f"Time: {time_taken:.8f} seconds | "
        f"Memory: {memory_used} bytes"
    )


# =======================================
# GRAPH 1: TIME COMPLEXITY
# =======================================

plt.figure(figsize=(8, 5))

plt.plot(
    input_sizes,
    execution_times,
    marker="o"
)

plt.xlabel("Number of Vertices (V)")
plt.ylabel("Execution Time (seconds)")

plt.title("DFS - Time Complexity")

plt.grid(True)

plt.savefig(
    "../graphs/dfs_time.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# =======================================
# GRAPH 2: SPACE COMPLEXITY
# =======================================

plt.figure(figsize=(8, 5))

plt.plot(
    input_sizes,
    memory_usages,
    marker="o"
)

plt.xlabel("Number of Vertices (V)")
plt.ylabel("Peak Memory Usage (bytes)")

plt.title("DFS - Space Complexity")

plt.grid(True)

plt.savefig(
    "../graphs/dfs_space.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()