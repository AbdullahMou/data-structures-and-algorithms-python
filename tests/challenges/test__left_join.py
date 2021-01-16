from data_structures_and_algorithms.challenges.left_join.left_join import *


def test_left_join_normal():
    h1 = Hashtable(1024)
    h1.add('one','one')        
    h1.add('tow', 'one')          
    h1.add('three', 'one')    
    h1.add('four', 'one')           

    h2 = Hashtable(1024)
    h2.add('one', 'tow')
    h2.add('tow', 'tow')
    h2.add('three', 'tow')
    h2.add('five', 'tow')

    assert  left_join(h1,h2) == [ ['fond', 'enamored', 'averse'], ['outfit', 'garb', None], ['diligent', 'employed', 'idle'], ['wrath', 'anger', 'delight'], ['guide', 'usher', 'follow']]

def test_left_join_1st_empty():
    h1 = Hashtable(1024)
    h2 = Hashtable(1024)
    h2.add('one', 'tow')
    h2.add('tow', 'tow')
    h2.add('three', 'tow')
    h2.add('five', 'tow')

    assert left_join(h1,h2) == []

def test_left_join_no_matches():
    h1 = Hashtable(1024)
    h1.add('one','one')        
    h1.add('tow', 'one')          
    h1.add('three', 'one')    
    h1.add('four', 'one')           

    h2 = Hashtable(1024)
    h2.add('six', 'tow')
    h2.add('seven', 'tow')
    h2.add('eight', 'tow')
    h2.add('five', 'tow')

    assert left_join(h1,h2) == [['rath', 'anger', None], ['pond', 'enamored', None], ['hangguide', 'usher', None], ['adiligent', 'employed', None], ['poutfit', 'garb', None]] 

