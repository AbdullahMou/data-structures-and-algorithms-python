# from data_structures_and_algorithms.data_structures.linked_list.linked_list import*
class Node:
    def __init__(self,val,key):
        self.value=val
        self.key=key
        self.next=None


#-------------------------------------------------------------------------

class LinkedList:
    def __init__(self):
       self.head = None


    def insert(self,val,key):
        node = Node(val,key)

        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node


class Hashtable:
    def __init__(self,size):
        self.size=size
        self.arr=[None]*size

    def add(self,key,val):
        indx=self.hash(key)
        # node=LinkedList()
        # if not self.arr[indx]:
        #     self.arr[indx]=[node.insert(val,key)]
        #     print(node.insert(val,key))
        # else:
        #         self.arr[indx]=[node.insert(val,key)]
        # return self.arr
        if not self.arr[indx]:
            self.arr[indx] = [[key, val],]
        else:
            self.arr[indx].append([key, val])  

    def get(self,key):
    
        pass    

    def contains(self,key):
        pass

    def hash(self,key):
        ascii_sum=0
        for char in key:
            ascii_sum+=ord(char)
        indx=(ascii_sum*11)%self.size
        return indx    


if __name__ == "__main__":
    sad=Hashtable(1024)
    
    sad.add('aba',4)
    sad.add('aab',3)
    assert ['aba',4] in sad.arr[sad.hash('aba')]
    assert ['aab',3] in sad.arr[sad.hash('aab')]
    print('Test passed Successfully')
