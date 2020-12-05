from data_structures_and_algorithms.data_structures.linked_list.linked_list import *
import pytest

def test_instance():
    ll = LinkedList()
    assert isinstance(ll, LinkedList)


def test_empty():
    ll = LinkedList()
    assert ll.head == None

def test_insert(ll):
    
    assert ll.head.value == 9

def test_insert_multipal(ll):
  
    assert ll.head.value ==9
    assert ll.head.next.value ==7
    assert ll.head.next.next.value ==5
    assert ll.head.next.next.next ==None

def test_include_true(ll):
 
    assert ll.includes(7)==True

def test_include_false(ll):
  
    assert ll.includes(6) == False

def test_string(ll):
 
    assert ll.__str__()=="{ 9 } -> { 7 } -> { 5 } -> NULL"



@pytest.fixture
def ll():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(7)
    ll.insert(9)
    return ll