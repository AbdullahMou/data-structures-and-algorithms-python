from data_structures_and_algorithms.challenges.array_binary_search.array_binary_search import BinarySearch

def test_binary():
    actual = BinarySearch([4,8,15,16,23,42], 15)
    expected = 2
    assert actual == expected

def test_binary1():
    actual = BinarySearch([11,22,33,44,55,66,77], 90)
    expected = -1
    assert actual == expected
