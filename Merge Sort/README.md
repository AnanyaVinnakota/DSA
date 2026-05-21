## MergeSort Algorithm

Merge Sort is a Divide and Conquer sorting algorithm.

It works in 3 steps:

1. Divide the array into smaller halves
2. Sort the smaller halves
3. Merge the sorted halves

# Pseudo Code

```text
FUNCTION merge(X, Y)
    
    p1 = 0
    p2 = 0
    out = empty list
    
    WHILE p1 is less than len(X) AND p2 is less than len(Y)
        IF X[p1] is less than Y[p2] THEN
            add X[p1] to the end of out
            p1 = p1 + 1
        ELSE
            add Y[p2] to the end of out
            p2 = p2 + 1
        ENDIF
    ENDWHILE

MERGE_SORT(array):

    IF array size <= 1
        RETURN array

    FIND mid index

    left_half = first half
    right_half = second half

    left_sorted = MERGE_SORT(left_half)
    right_sorted = MERGE_SORT(right_half)

    RETURN MERGE(left_sorted, right_sorted)
```
# Time Complexity
 For all the cases, it is O(n logn)

 # Space Complexity
 O(n) --to store all the splitted arrays it requires more space
 
