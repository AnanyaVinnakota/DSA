# BubbleSort Algorithm

Bubble Sort is one of the simplest sorting algorithms.

It repeatedly compares adjacent elements in a list and swaps them if they are in the wrong order.

# Pseudocode

BubbleSort(arr):

    n = length of arr

    for i from 0 to n-1:

        swapped = false

        for j from 0 to n-i-2:

            if arr[j] > arr[j+1]:

                swap arr[j] and arr[j+1]

                swapped = true

        if swapped == false:

            break

# Time Complexity

1. Best Case -- O(n)
2. Average Case -- O(n²)
3. Worst Case -- O(n²)
