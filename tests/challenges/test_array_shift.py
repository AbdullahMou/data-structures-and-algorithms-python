from data_structures_and_algorithms.challenges.array_shift.array_shift import insertShiftArray

def test():
    act=insertShiftArray([2,4,6,8], 5)
    exp=[2,4,5,6,8]
    assert act==exp

    
def test1():
    act=insertShiftArray([4,8,15,23,42], 16)
    exp=[4,8,15,16,23,42]
    assert act==exp