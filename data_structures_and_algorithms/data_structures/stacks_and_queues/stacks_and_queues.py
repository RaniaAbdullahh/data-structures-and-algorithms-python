class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
        
    def push(self, data):
        ''' takes any value as an argument and adds a new node with that value to the top of the stack '''
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node

    def pop(self):
        ''' removes the node from the top of the stack, and returns the node’s value.'''
        try:
            temp=self.top
            self.top=self.top.next
            temp.next=None
            return temp.value
        except:
            return 'Empty stack'      
            
       

    def peek(self):
        '''that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.'''
        try:
            return self.top.value
        except:
            return 'Empty stack'   
    def isEmpty(self):
        if  not self.top:
            return True  
        else:
            return False                 

class Queue :
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self,data):
        ''' takes any value as an argument and adds a new node with that value to the back of the queue '''
        node = Node(data)
        if self.rear:
            self.rear.next = node
            self.rear = node
        else:
            self.front = node
            self.rear = node

    def dequeue(self):
        '''  removes the node from the front of the queue, and returns the node’s value.'''
        try:
            temp=self.front
            self.front=self.front.next
            temp.next=None
            return temp.value
        except:
            return 'Empty Queue'  

    def peek(self):
        ''' returns the value of the node located in the front of the queue, without removing it from the queue.'''
        try:
            return self.front.value
        except:
            return 'Empty Queue'   
    def isEmpty(self):
        ''' returns a boolean indicating whether or not the queue is empty.'''
        if  not self.front:
            return True  
        else:
            return False        




if __name__ == "__main__":
    stack = Stack()
    # stack.push(1)
    # stack.push(2)
    # stack.push(3)
    print(stack.peek())# 2  
    print(stack.pop()) # 3
    print(stack.peek()) #2  
    print(stack.isEmpty())#false

    queue = Queue()
    # queue.enqueue('ran')
    # queue.enqueue('moh')
    print(queue.peek())#ran
    print(queue.dequeue())#ran  





