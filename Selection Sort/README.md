## Selection Sort 
Working:
1. Finding the smallest element
2. Swapping it with the first element
3. Leaving the first element as it is already sorted and finding the smallest element in the rest of the array
4. Swapping positions again
5. Repeat the process until the entire array is sorted

## Pseudo Code

```text
START

INPUT arr

FOR i = 0 to length(arr) - 1

    min_index = i

    FOR j = i + 1 to length(arr) - 1

        IF arr[j] < arr[min_index]

            min_index = j

    SWAP arr[i] and arr[min_index]

PRINT arr

END
```

## Time Complexity
For all cases it is, O(n²)

## Space Complexity
O(1) -- No extra space

