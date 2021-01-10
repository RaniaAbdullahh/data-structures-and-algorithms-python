from data_structures_and_algorithms.challenges.repeated_word import repeated_word

def test_repeated_string():
    actual = repeated_word("Once upon a time, there was a brave princess who..")
    assert actual == "a"

def test_not_repeated_string():
    actual = repeated_word("it is rainy today")
    assert actual == "No repeating words found"


