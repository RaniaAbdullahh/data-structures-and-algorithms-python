from data_structures_and_algorithms.challenges.insertion_sort.insertion_sort import InsertionSort

def test_insert_sort():
    actual = InsertionSort([8,4,23,42,16,15])
    assert actual == [4, 8, 15, 16, 23, 42]
def test_reversed_list_sort():
    actual = InsertionSort([20,18,12,8,5,-2])
    assert actual == [-2,5,8,12,18,20]
def test_Few_uniques_sort():
    actual = InsertionSort([5,12,7,5,5,7])
    assert actual ==  [5,5,5,7,7,12]
def test_Nearly_sorted_sort():
    actual = InsertionSort([2,3,5,7,13,11])
    assert actual == [2,3,5,7,11,13]
