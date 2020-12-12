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
                    print(f'nomber : {val} dosent exist')




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
                print(f'nomber : {val} dosent exist')


  
    def ll_kth_from_end(self,k):
        vals=[]
        current = self.head
        if current == None: return ("Sorry No lenked list available")
        elif k<0: return ("nigative value is'nt acceptable")
        else:
            while current:
                vals += [current.value]
                current = current.next
                
            try:
                return vals[::-1][k]
            except IndexError:
                return (f"index doesn't exist")

 
    def zipLists(self,list1,list2):
        list3 =LinkedList()
        current1 =list1.head
        current2 =list2.head
        while current1 and current2:
            list3.append(current1.value)
            list3.append(current2.value)
            current1=current1.next
            current2=current2.next
        while current2 :
            list3.append(current2.value)
            current2=current2.next     
        while current1 :
            list3.append(current1.value)
            current1=current1.next
        return list3


    # def palind(self):
    #     list2 = []

    #     current =self.head

    #     while current:

    #         list2.append(current)

    #         current= current.next



        # isPalind =True

        # current =self.head

        # while current:

                

        #     value= list2.pop()

        #     if current == value :

        #         isPalind = True

        #     else:
        #         isPalind=False
            
        #     current = current.next



        # return isPalind


#-------------------------------------------------------------------------
if __name__ == "__main__":
    # node1 = Node(5)
    node=LinkedList()
    node2=LinkedList()

    node.append(1)
    node.append(3)
    # print(node1.value)
    # node.insert(5)
    # node.insert(7)
    # node.insert(6)
    # node.append(5)
    # node.append(7)
    # node.insert_after(5,2)
    # node.insert_before(1,4)
    # print(node.includes(6))
    # print(node.ll_kth_from_end(-1))
    # print(node)
    node.append(4)
    node.append(3)
    node.append(1)
    # node2.append(10)

    print(node.palind())
    