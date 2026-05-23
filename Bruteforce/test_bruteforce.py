from bruteforce import linear_search

# Target present in the middle
def test_target_in_middle():
    assert linear_search([5, 2, 9, 1, 7], 9) == 2

# Target not present in array
def test_target_not_found():
    assert linear_search([1, 3, 5, 7, 9], 4) == -1

# Empty array
def test_empty_array():
    assert linear_search([], 10) == -1

# Mixed positive and negative numbers
def test_mixed_numbers():
    assert linear_search([-100, 50, -20, 70, 0], 70) == 3

# Very large negative target
def test_large_negative():
    assert linear_search([-99999, -5000, -1], -99999) == 0

# String elements
def test_string_array():
    assert linear_search(["apple", "banana", "mango"], "banana") == 1