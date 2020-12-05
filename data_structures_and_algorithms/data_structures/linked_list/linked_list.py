
class Node:
    def __init__(self,val,next=None):
        self.value=val
        self.next=next


#-------------------------------------------------------------------------

class LinkedList:
    """
 This class creates new Linked List and append items to it using insert method
    that accepts 1 Argument, Can search for 1 Argument at a time in the Linked Lust created,
    And can retrn a string of the linked list
   """
    def __init__(self):
       self.head = None


    def insert(self,val):
        node = Node(val)

        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def includes(self,val):
        current = self.head
        while current !=None:
            if current.value ==val:
                return True
            else:
                current=current.next
        return False            

       
             

    def __str__(self):
        """
        "{ a } -> { b } -> { c } -> NULL"
        """
        string =''
        current = self.head
        while current!=None:
                string+=f'{{ {current.value} }} -> '
                current=current.next
                if current == None:
                    string+= 'NULL'
        return string


#-------------------------------------------------------------------------
if __name__ == "__main__":
    node1 = Node(5)
    node=LinkedList()
    print(node1.value)
    node.insert(5)
    node.insert(7)
    node.insert(6)
    print(node.includes(6))
    print(node)
