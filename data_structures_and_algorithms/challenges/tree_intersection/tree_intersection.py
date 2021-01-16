from data_structures_and_algorithms.data_structures.tree.tree import *

def tree_intersection(bt1,bt2):
    # bt1=Binary_tree
    # bt2=Binary_tree
    arr_set=[]
    arr= bt1.preorder()
    arr2= bt2.preorder()
    for i in arr:
        if i in arr2:
            arr_set.append(i)
    return arr_set

if __name__ == "__main__":
    bt = Binary_tree()
    bt.root = Node(6)
    bt.root.left = Node(-1)
    bt.root.left.left = Node(10)
    bt.root.right = Node(5)
    bt.root.right.left = Node(7)
    bt.root.right.right = Node(3)

    bt1 = Binary_tree()
    bt1.root = Node(1)
    bt1.root.left = Node(-1)
    bt1.root.left.left = Node(11)
    bt1.root.right = Node(8)
    bt1.root.right.left = Node(5)
    bt1.root.right.right = Node(3) 
     
    print(tree_intersection(bt,bt1)          )