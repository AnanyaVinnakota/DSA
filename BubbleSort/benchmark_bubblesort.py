import time
import tracemalloc
import random
import matplotlib.pyplot as plt

from bubblesort import bubblesort


# ---------------------------------------
# Generate an array of a given size
# ---------------------------------------

def generate_array(n):
    random.seed(42)

    return [random.randint(1, 100000) for _ in range(n)]


# ---------------------------------------
# Measure execution time
# ---------------------------------------

def measure_time(arr, repetitions=10):

    times = []

    for _ in range(repetitions):

        # Bubble Sort modifies the array,
        # so every run needs a fresh copy.
        test_arr = arr.copy()

        start = time.perf_counter()

        bubblesort(test_arr)

        end = time.perf_counter()

        times.append(end - start)

    average_time = sum(times) / len(times)

    return average_time


# ---------------------------------------
# Measure memory usage
# ---------------------------------------

def measure_memory(arr):

    # Bubble Sort modifies the array,
    # so give it a fresh copy.
    test_arr = arr.copy()

    tracemalloc.start()

    bubblesort(test_arr)

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    return peak


# ---------------------------------------
# Input sizes
# ---------------------------------------

input_sizes = [10, 50, 100, 500, 1000, 5000]

execution_times = []
memory_usages = []


# ---------------------------------------
# Run benchmark
# ---------------------------------------

for n in input_sizes:

    arr = generate_array(n)

    # Measure execution time
    time_taken = measure_time(arr)

    # Measure memory usage
    memory_used = measure_memory(arr)

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

plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")

plt.title("Bubble Sort - Time Complexity")

plt.grid(True)

plt.savefig(
    "../graphs/bubble_sort_time.png",
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

plt.xlabel("Input Size (n)")
plt.ylabel("Peak Memory Usage (bytes)")

plt.title("Bubble Sort - Space Complexity")

plt.grid(True)

plt.savefig(
    "../graphs/bubble_sort_space.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()