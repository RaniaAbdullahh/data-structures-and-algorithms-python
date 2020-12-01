from  data_structures_and_algorithms.challenges.array_binary_search.array_binary_search import binary_search


"""
test empty array
test the odd  number in sotred array
test the even number in sotred array

"""
def  test_works_if_empty_arr():
   
    actual = binary_search([], 2)
    expected = -1
    assert expected == actual
  

def test_finds_indexed_odd_num():
    expected = 4
    actual = binary_search([1, 2, 3, 4, 5, 6], 5)
    assert expected == actual

def test_finds_indexed_even_num_():
    expected = 4
    actual = binary_search([1, 2, 4, 5, 6, 7], 6)
    assert expected == actual


