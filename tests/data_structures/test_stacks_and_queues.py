from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import *

def test_enqueue():
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(3)
    act=queue.peek()
    exp=1
    assert act==exp

def test_dequeue():
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(3)
    queue.dequeue()
    queue.dequeue()
    act=queue.peek()
    exp='queue is empty'
    assert act==exp

def test_isempty():
        stack=Stack()
        stack.push(1)
        stack.push(3)
        act=stack.is_empty()
        exp=False
        assert act==exp

def test_push():
        stack=Stack()
        stack.push(1)
        stack.push(3)
        act=stack.peek()
        exp=3
        assert act == exp 


def test_pop():
        stack=Stack()
        stack.push(1)
        stack.push(3)
        stack.pop()
        stack.pop()
        stack.pop()
        act=stack.peek()
        exp='stack is empty'
        assert act == exp 
        
