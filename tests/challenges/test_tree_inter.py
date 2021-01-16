from data_structures_and_algorithms.challenges.tree_intersection.tree_intersection import *

def test_test_three_common():
    tr1=Binary_tree()
    tr2 = Binary_tree()
    tr1.root = Node(5)
    tr1.root.right = Node(10)
    tr1.root.left = Node(-2)
    tr1.root.right.left = Node(15)
    tr1.root.left.left = Node(17)
    tr2.root = Node(5)
    tr2.root.right = Node(11)
    tr2.root.left = Node(-2)
    tr2.root.right.left = Node(15)
    tr2.root.left.left = Node(111)
    assert tree_intetsaction(tr1,tr2) == [5,-2,15]

def test_test_empty_tree():
    tr1=Binary_tree()
    tr2 = Binary_tree()
    assert tree_intetsaction(tr1,tr2) == []

def test_test_with_string():
    tr1=Binary_tree()
    tr2 = Binary_tree()
    tr1.root = Node(5)
    tr1.root.right = Node(7)
    tr1.root.left = Node(-2)
    tr1.root.right.left = Node(15)
    tr1.root.left.left = Node(17)
    tr2.root = Node(5)
    tr2.root.right = Node(11)
    tr2.root.left = Node(-2)
    tr2.root.right.left = Node(15)
    tr2.root.left.left = Node(7)
    assert tree_intetsaction(tr1,tr2) == [5,-2,7,15]

def test_test_with_one_node():
    tr1=Binary_tree()
    tr2 = Binary_tree()
    tr1.root = Node(5)
    assert tree_intetsaction(tr1,tr2) == []