# from data_structures_and_algorithms.challenges.array_shift import insertShiftArray
from data_structures_and_algorithms.challenges.array_shift.array_shift import insertShiftArray

def test_type_of_list():
    actual= insertShiftArray(5,4)
    expected= 'Invalid Input'
    assert actual==expected


def test_type_of_num():
    actual= insertShiftArray([5,4,2],'r')
    expected= 'Invalid Input'
    assert actual==expected


def test_add_to_even():
    actual= insertShiftArray([5,4,2,1],3)
    expected= [5,4,3,2,1]
    assert actual==expected


def test_add_to_odd():
    actual= insertShiftArray([6,5,4,2,1],3)
    expected= [6,5,4,3,2,1]
    assert actual==expected