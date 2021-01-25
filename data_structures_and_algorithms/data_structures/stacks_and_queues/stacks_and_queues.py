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


# if __name__ == "__main__":
    # queue=Queue()
    # queue.enqueue(3)
    # queue.enqueue(1)
    # queue.enqueue(5)
    # print(queue.peek())
    # print(queue.isempty())
    # print(queue.dequeue())

    # stack=Stack()
    # stack.push(1)
    # stack.push(3)
    # stack.push(5)
    # print(stack.is_empty())
    # print(stack.peek())
    # stack.pop()
    # print(stack.peek())
    # stack.pop()
    # print(stack.peek())
    # stack.pop()
    # print(stack.peek())
