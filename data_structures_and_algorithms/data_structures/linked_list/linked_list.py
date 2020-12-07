
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

        
    def append(self,val):
        current = self.head
        node = Node(val)
        if self.head==None:
            self.head=node
        else:
            while current.next:
                current=current.next
            current.next=node    

        


    def insert_before(self,val, newVal):
        node = Node(newVal)
        if self.head ==None:
            self.head = node
        else:
            if self.head.value==val:
                node.next=self.head
                self.head=node
            else:
                current=self.head
                while current.next:
                    if current.next.value==val:
                        node.next=current.next
                        current.next=node
                        break
                    current=current.next
                    return f'{val} dosent exist'




    def insert_after(self,val, newVal):
        node= Node(newVal)
        if not self.head:
            self.head=node
        else:
            current=self.head
            while current!= None:
                if current.value==val:
                    node.next = current.next
                    current.next=node
                    break
                current=current.next
                return f'{val} dosent exist'

           



#-------------------------------------------------------------------------
if __name__ == "__main__":
    # node1 = Node(5)
    node=LinkedList()
    # print(node1.value)
    # node.insert(5)
    # node.insert(7)
    # node.insert(6)
    # node.append(1)
    node.append(3)
    node.append(5)
    # node.insert_after(5,2)
    # node.insert_before(1,4)
    # print(node.includes(6))
    print(node)
