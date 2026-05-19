# Brute Force Algorithm

## Definition

A **Brute Force Algorithm** is the simplest and most direct approach to solving a problem.

It works by:

1. Trying all possible solutions
2. Checking which solution satisfies the condition
3. Returning the correct or best solution

## Pseudo Code

START

INPUT array
INPUT target

FOR each element in array
    IF element == target
        PRINT "Element found"
        STOP

PRINT "Element not found"

END

# Time Complexity

Brute force algorithms often have higher time complexities such as:

- O(n) --General
- O(n²) --Nested loops
- O(2ⁿ) --Subsets
- O(n!) --Permutations

depending on the problem.