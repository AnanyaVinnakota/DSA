from mergesort import mergeSort


def test_case_1():
    assert mergeSort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]


def test_case_2():
    assert mergeSort([5, 3, 8, 3, 9, 1, 5, 2]) == [1, 2, 3, 3, 5, 5, 8, 9]


def test_case_3():
    assert mergeSort([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_case_4():
    assert mergeSort([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_case_5():
    assert mergeSort([-5, 12, 0, -3, 8, -1, 7]) == [-5, -3, -1, 0, 7, 8, 12]