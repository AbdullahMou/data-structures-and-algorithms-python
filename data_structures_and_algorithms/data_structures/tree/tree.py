
class Node :
    def __init__(self,val):
        self.value=val
        self.left=None
        self.right=None


class Binary_tree:
    def __init__(self):
        self.root=None
        self.max=0

    
    def preorder(self):
        lst=[]
        def _walk(node):
            lst.append(node.value)
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)    

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


    def post_order(self):
        lst=[]
        def _walk(node):

            if node.left:
                _walk(node.left)
            
            if node.right:
                _walk(node.right)
            
            lst.append(node.value)

        _walk(self.root)
        return lst


    def find_maximum(self):
        if not self.root:
            return 'no binary tree'
        else:
            def _walk(node):
                if node.value>self.max:
                    self.max=node.value    
                if node.left:
                    _walk(node.left)
                if node.right:
                   _walk(node.right)
            _walk(self.root)   
            return self.max                 

    def mergeTrees(self, t1, t2):
        if not t1 and not t2: return None
        newroot = Node((t1.value if t1 else 0) + (t2.value if t2 else 0))
        print(newroot.value)

        newroot.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        newroot.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return newroot                 


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
            if self.root == val:
                return True
            else:
                def _walk(node):
                    if node:
                        if val == node.value :
                            return True
                        elif val<node.value:
                            return _walk(node.left)
                        elif val>node.value:
                            return _walk(node.right)
                    return False
                return _walk(self.root)       






if __name__ == "__main__":
    
    bt = Binary_tree()
    bt.root =     Node(6)
    bt.root.left = Node(-1)
    bt.root.left.right = Node(10)
    bt.root.right = Node(5)
    bt.root.right.left = Node(7)
    bt.root.right.right = Node(3)

    bt1 = Binary_tree()
    bt1.root = Node(6)
    bt1.root.left = Node(-1)
    bt1.root.left.left = Node(10)
    bt1.root.right = Node(5)
    bt1.root.right.left = Node(7)
    bt1.root.right.right = Node(3)

    # print(bt.preorder())
    # print(bt.inorder())
    # print(bt.post_order())

    bst = B_s_t()
    bst.add(4)
    bst.add(9)
    bst.add(-1)
    bst.add(6)
    bst.add(3)
    bst.add(8)
    bst.add(5)

   
    bt1.mergeTrees(bt.root,bt1.root)
    # print(bs2.preorder())

    # print(bst.contains(-5))
    # assert bt.root.value == 6
    # assert bt.root.left.value == -1
    # assert bt.root.left.left.value == 10
    # assert bt.root.right.value == 5
    # assert bt.root.right.left.value == 7
    # assert bt.root.right.right.value == 3
    # print('######## all good #######')
    # assert bt.inorder == [10, -1, 6, 7, 5, 3]
    # assert bt.post_order == [10, -1, 7, 3, 5, 6]
    # assert print(bt.preorder) == [6,-1,10,5,7,3]
