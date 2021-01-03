class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class Binary_tree:
    def __init__(self):
        self.root = None
    
    def fizz_buzz_tree(self ,ary):
        fizz_buzz_arr=[]
        def divid(node):
            if self.node %3 and self.node %5 :
                fizz_buzz_arr.append('FizzBuzz')

            elif self.node %3 :
                fizz_buzz_arr.append('Fizz')   

            elif self.node  %5 :
                fizz_buzz_arr.append('Buzz')   

            else :
                fizz_buzz_arr.append(self.node.value)      

            if self.node.left :
                divid(self.node.left)

            if self.node.left :
                divid(self.node.right)

        divid(tree.root)
        return print(fizz_buzz_arr)        


# if __name__ == "__main__":
#     tree = Binary_tree()
#     tree.root = Node(1)
#     tree.root.left = Node(2)
#     tree.root.right = Node(3)
#     tree.root.left.left = Node(4)
#     tree.root.left.right = Node(5)
#     tree.root.right.right = Node(7)
#     tree.root.right.left = Node(6)
#     fizz_buzz_tree(tree)