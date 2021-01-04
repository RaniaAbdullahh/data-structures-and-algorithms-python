from data_structures_and_algorithms.challenges.mergesort.mergesort import mergeSort


def test_empty_list():
   
    array = []
    mergeSort([])
    assert array == []

def test_many_item_list():
    
    array = [3,5,2,-7,8]
    mergeSort(array)
    expected = [-7,2,3, 5,8]
    assert array == expected