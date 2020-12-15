# from data_structures_and_algorithms.challenges.queue_with_stacks.queue_with_stacks import *
class Node :
    def __init__(self,val,next=None):
        self.value=val
        self.next=next

class Queue :
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,val):
        node=Node(val)
        if self.rear:
            self.rear.next=node
            self.rear=node
        else:
            self.rear=node
            self.front=node


    def dequeue(self):
        if self.rear==self.front :
            temp=self.front
            self.front=None
            self.rear=None
            return temp
    
        elif self.front:
            temp=self.front
            self.front=self.front.next
            temp.next=None
            return temp

        return 'queue is empty'
        


    def peek(self):
        if not self.front:
            return 'queue is empty' 
        return self.front.value
        # try :
        #     return self.front.value
        # except AttributeError:
        #     return 'queue is empty'

    def is_empty(self):
        if self.rear:
            return False
        return True    

        

class Stack :
    def __init__(self):
        self.top=None

    def push(self,val):
        node=Node(val)
        if self.top:
            node.next=self.top
            self.top=node
        self.top=node    

    def pop(self):
        if not self.top:
            return 'stack is empty'

        if not self.top.next:
            temp=self.top
            self.top=None
            return temp
    
        if self.top:
            temp=self.top
            self.top=self.top.next
            temp.next=None
            return temp



    def peek(self):
        if not self.top:
            return 'stack is empty' 
        return self.top.value

    def is_empty(self):
        if self.top:
            return False
        return True


class PseudoQueue :
    def __init__(self):
      self.stack1 = Stack()
      self.stack2 = Stack()


    def enqueu(self,data):
      self.stack1.push(data)

    def dequeue(self):

      if not self.stack1.top:
        return 'Stack is empty'

      while self.stack1.top:
        self.stack2.push(self.stack1.pop())

      temp =  self.stack2.pop()

      while self.stack2.top:
        self.stack1.push(self.stack2.pop())
      
      return temp

if __name__ == "__main__":
  queue = PseudoQueue()

  queue.enqueu(1)
  queue.enqueu(2)
  queue.enqueu(3)
  queue.enqueu(4)

  print(queue.dequeue())
  print(queue.dequeue())
  print(queue.dequeue())
  print(queue.dequeue())
  print(queue.dequeue())