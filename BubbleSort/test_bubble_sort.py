from bubblesort import bubblesort


def test_case_1():
    assert bubblesort([5, 3, 8, 6, 2]) == [2, 3, 5, 6, 8]


def test_case_2():
    assert bubblesort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_case_3():
    assert bubblesort([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9]