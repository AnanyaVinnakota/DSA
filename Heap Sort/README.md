## Heap Sort
Sorting is done using a binary tree
Working:
1. Build Max Heap(A heap where parent is always greater than children)
2. Swap Root with last element
3. Heapify again. We have to leave the last element and make tree with the array. Make into a max heap.
4. Again swap and heapify until array is sorted

## Time Complexity
For building heap --O(n)
Heapify Process --O(logn)
Overall --O(n logn)

## Space Complexity
O(1) --No extra space