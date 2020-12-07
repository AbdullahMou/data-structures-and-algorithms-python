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



def test_append():
    ll = LinkedList()
    ll.append(3)
    ll.append(5)
    ll.append(7)

    assert ll.head.value == 3
    assert ll.head.next.value ==5
    assert ll.head.next.next.value ==7
    assert ll.head.next.next.next ==None

def test_insert_before():
    ll = LinkedList()
    ll.insert_before(3,1)

    assert ll.head.value == 1

def test_insert_before_1():
    ll = LinkedList()
    ll.append(5)
    ll.append(7)
    ll.insert_before(5,1)

    assert ll.head.value == 1


def test_insert_after():
    ll = LinkedList()
    ll.insert_after(5,1)

    assert ll.head.value == 1

def test_insert_after_1():
    ll = LinkedList()
    ll.append(5)
    ll.append(7)
    ll.insert_after(5,1)

    assert ll.head.next.value == 1

def test_from_end(ll):
  
    assert ll.ll_kth_from_end(99) =="index doesn't exist"
    assert ll.ll_kth_from_end(1) ==7
    assert ll.ll_kth_from_end(-11) =="nigative value is'nt acceptable"

def test_from_end_1():
    ll = LinkedList()
    assert ll.ll_kth_from_end(0) =="Sorry No lenked list available"

    ll.append(5)    
    assert ll.ll_kth_from_end(0) ==5
    

@pytest.fixture
def ll():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(7)
    ll.insert(9)
    return ll

# @pytest.fixture
# def ll_2():
#     ll = LinkedList()
#     ll.append(3)
#     ll.append(5)
#     ll.append(7)
