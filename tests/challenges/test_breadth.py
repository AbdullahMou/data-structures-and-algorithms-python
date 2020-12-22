from data_structures_and_algorithms.challenges.breadth_first.breadth_first import *
import pytest

def test_breadth_first_traversal_tree(prep):
    actual = prep.breadth_first_traversal(prep.root)
    expected = [0,1,2,3,4,5]
    assert actual == expected

@pytest.fixture
def prep():
    bt = Binary_tree()
    bt.root = Node(0)
    bt.root.right = Node(2)
    bt.root.left = Node(1)
    bt.root.left.left = Node(3)
    bt.root.right.left = Node(4)
    bt.root.right.right = Node(5)
    return bt    