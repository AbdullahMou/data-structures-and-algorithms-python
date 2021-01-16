class Node:
 
    def __init__(self, data):
         
        self.data = data
        self.next = None
 
class LinkedList:
 
    def __init__(self):
         
        self.head = None
 
    def isPalindrome(self, head):
         
        slow_ptr = head
        fast_ptr = head
        prev_of_slow_ptr = head
         
        midnode = None
         
        res = True 
         
        if (head != None and head.next != None):
             
            while (fast_ptr != None and
                   fast_ptr.next != None):
                       
                fast_ptr = fast_ptr.next.next
                prev_of_slow_ptr = slow_ptr
                slow_ptr = slow_ptr.next
                 
            if (fast_ptr != None):
                midnode = slow_ptr
                slow_ptr = slow_ptr.next
                 
            second_half = slow_ptr
             
            prev_of_slow_ptr.next = None
             
            second_half = self.reverse(second_half) 
             
            res = self.compareLists(head, second_half)  
             
            second_half = self.reverse(second_half)
             
            if (midnode != None):
                 
                prev_of_slow_ptr.next = midnode
                midnode.next = second_half
            else:
                prev_of_slow_ptr.next = second_half
        return res
     
    def reverse(self, second_half):
         
        prev = None
        current = second_half
        next = None
         
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
             
        second_half = prev
        return second_half
 
class Node:
    def __init__(self, data):
         
        self.data = data
        self.next = None
 
class LinkedList:
 
  def __init__(self):
         
        self.head = None


  def palind(self):
    list2 = []
    current =self.head
    while current:
        list2.append(current.value)
        current= current.next

    isPalind =True
    while current:

        value= list2.pop()
        if current.value == value :
            isPalind = True
        else:
            isPalind=False
        current = current.next
    return isPalind

vals=[1,2,3,4,5,6,7]
def ll_kth_from_end(vals,k):

    for i in range(len(vals)//2):
        vals[i],vals[-i-1]= vals[-i-1],vals[i]    
    try:
        return vals[k]
    except IndexError:
        return (f"index doesn't exist")

print(ll_kth_from_end(vals,7))
# v=[]
# a='aa'
# s=6
# d='d'
# v+=[a]
# v+=[d]
# v+=[s]
# print(v[::-1][0])
# print(v)    