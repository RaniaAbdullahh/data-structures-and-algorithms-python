from data_structures_and_algorithms.challenges.fizz_buzz_tree.fizz_buzz_tree import fizzbuzzTree


def test_fizzbusstree():
    result= fizzbuzzTree([3,15,21,30,4,8])
    assert result == ['Fizz', 'FizzBuzz', 'Fizz', 'FizzBuzz', '4', '8']
