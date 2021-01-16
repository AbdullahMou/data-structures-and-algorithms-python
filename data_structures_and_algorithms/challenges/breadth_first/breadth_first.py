from data_structures_and_algorithms.data_structures.tree.tree import *

def breadth_first_traversal(self, tree):
    queue = []
    lst = []
    if not tree:
        return 'There is no tree ...'
    else:
        if tree:
            queue.append(tree)
        while queue:
            current = queue.pop(0)
            lst.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    return lst   

tre=[1,2,3]
tr=[]    
tre.append(tr)
print(tre)