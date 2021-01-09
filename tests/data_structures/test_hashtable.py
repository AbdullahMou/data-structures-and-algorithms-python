from data_structures_and_algorithms.data_structures.hashtable.hashtable import *

def test_value():
    table = Hashtable(1024)
    table.add('car','BMW')
    table.add('car','Firari')
    assert table.arr[table.hash('car')].head.value[1] == 'BMW'

def test_add():
    table = Hashtable(1024)
    table.add('Mercedes','G class')
    assert table.arr[table.hash('Mercedes')].head.value == ['Mercedes','G class']


def test_get():
    table = Hashtable(1024)
    table.add('BMW','x5')
    assert table.get('BMW') ==  'x5'

def test_key_dosnt_exist():
    table = Hashtable(1024)
    assert table.get('Audi') == "key isn't exist"

def test_collision():
    table = Hashtable(1024)
    table.add('Tesla','2')
    table.add('Tasle','4')
    assert table.arr[table.hash('Tesla')].head.value == ['Tesla','2']
    # assert table.arr[table.hash('Tasle')].head.value == ['Tasle','4']


def test_retrieve():
    table = Hashtable(1024)
    table.add('Tesla','3')
    table.add('Tasle','1')
    assert table.get('Tesla') == '3'
    assert table.get('Tasle') == '1'