from data_structures_and_algorithms.challenges.insertion_sort.insertion_sort import *


def test_revers():
    ar=[20,18,12,8,5,-2]
    assert insertion_sort(ar)== [-2,5,8,12,18,20]

def test_few_uniques():
    assert insertion_sort(ar)== [5,5,5,7,7,12]

ar=[5,12,7,5,5,7]
def test_nearly():
    assert insertion_sort([2,3,5,7,13,11])== [2,3,5,7,11,13]