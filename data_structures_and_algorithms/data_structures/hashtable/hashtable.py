# from data_structures_and_algorithms.data_structures.linked_list.linked_list import*
class Node:
    def __init__(self,val):
        self.value=val
        self.next=None


#-------------------------------------------------------------------------

class LinkedList:
    def __init__(self):
       self.head = None


    def append(self,val):
        node = Node(val)

        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current=current.next
            current.next=node    

#-------------------------------------------------------------------------

class Hashtable:
    def __init__(self,size):
        self.size=size
        self.arr=[None]*size

    def add(self,key,val):
        indx=self.hash(key)
        # node=LinkedList()
        # if not self.arr[indx]:
        #     self.arr[indx]=[node.append(val,key)]
        #     print(node.append(val,key))
        # else:
        #         self.arr[indx]=[node.append(val,key)]
        # return self.arr
        if not self.arr[indx]:
            self.arr[indx] = LinkedList()
            self.arr[indx].append([key, val])
        self.arr[indx].append([key, val])  

    def get(self,key):
        indx=self.hash(key)
        if self.arr[indx]:    
            cur=self.arr[indx].head
            while cur:
                if cur.value[0]==key:
                    return cur.value[1]
                cur=cur.next    
        return "key isn't exist"

    def contains(self,key):
        indx=self.hash(key)
        if self.arr[indx]:
            return True
        return False    


    def hash(self,key):
        ascii_sum=0
        for char in key:
            ascii_sum+=ord(char)
        indx=(ascii_sum*11)%self.size
        return indx    


if __name__ == "__main__":
    sad=Hashtable(1024)
    
    sad.append('aba',4)
    sad.append('aab',3)
    assert ['aba',4] in sad.arr[sad.hash('aba')]
    assert ['aab',3] in sad.arr[sad.hash('aab')]
    print('Test passed Successfully')
