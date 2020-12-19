
class Node :
    def __init__(self,val):
        self.value=val
        self.left=None
        self.right=None


class Binary_tree:
    def __init__(self):
        self.root=None

    
    def preorder(self):
        lst=[]
        def _walk(node):
            lst.append(node.value)
            if node.right:
                _walk(node.right)
            if node.left:
                _walk(node.left)

        _walk(self.root)
        return lst


    def inorder(self):
        lst=[]
        def _walk(node):

            if node.left:
                _walk(node.left)

            lst.append(node.value)

            if node.right:
                _walk(node.right)

        _walk(self.root)
        return lst


    def post_order():
        lst=[]
        def _walk(node):

            if node.left:
                _walk(node.left)
            
            if node.right:
                _walk(node.right)
            
            lst.append(node.value)

        _walk(self.root)
        return lst


class B_s_t(Binary_tree):

    def add(self,val):
        if not self.root:
            self.root=Node(val)
        else:    
            def _walk(node):
                if val<node.value:
                    if not node.left:
                        node.left=Node(val)
                        return
                    else: _walk(node.left)
                if val> node.value:
                    if not node.right:
                        node.right=Node(val)
                        return
                    else: _walk(node.right)    
            _walk(self.root)


    def contains(self,val):
        if not self.root:
            return False
        else:    
            curr=(self.root)
            def _walk(curr):
                if val == curr.value:
                    return True
                if val<curr.value:
                    curr=curr.left
                    if curr:
                        return _walk(curr)
                if val> curr.value:
                    curr=curr.right
                    if curr:
                        return _walk(curr.right)  
                    
            if _walk(curr)==True:
                return True
            else: 
                return False        






if __name__ == "__main__":

    bt = Binary_tree()
    bt.root = Node(6)
    bt.root.right = Node(5)
    bt.root.left = Node(-1)
    bt.root.right.left = Node(7)
    bt.root.left.left = Node(10)
    bt.root.right.right = Node(3)
    # print(bt.inorder())

    bst = B_s_t()
    bst.add(4)
    bst.add(9)
    bst.add(-1)
    bst.add(6)
    bst.add(3)
    bst.add(8)
    bst.add(5)
    print(bst.contains(0))
