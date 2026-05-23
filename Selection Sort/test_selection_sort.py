from selectionsort import selection_sort


# Random unsorted array
def test_random_numbers():
    assert selection_sort([64, 25, 12, 22, 11]) == [11, 12, 22, 25, 64]


# Already sorted array
def test_already_sorted():
    assert selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


# Reverse sorted array
def test_reverse_sorted():
    assert selection_sort([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9]


# Array with duplicate elements
def test_duplicates():
    assert selection_sort([4, 2, 5, 2, 1, 4]) == [1, 2, 2, 4, 4, 5]


# Array with negative numbers and zero
def test_negative_numbers():
    assert selection_sort([0, -1, 5, -10, 8, -3]) == [-10, -3, -1, 0, 5, 8]