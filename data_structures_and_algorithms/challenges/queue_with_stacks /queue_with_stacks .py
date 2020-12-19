#from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import Stack,Node

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
        
    def push(self, data):
      
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node

    def pop(self):
      
        try:
            temp=self.top
            self.top=self.top.next
            temp.next=None
            return temp.value
        except:
            return 'Empty stack'      
            
       

    def peek(self):

        try:
            return self.top.value
        except:
            return 'Empty stack'   
    def isEmpty(self):
        if  not self.top:
            return True  
        else:
            return False    

   
class PseudoQueue:

    def __init__(self):
      
        self.stackA = Stack()
        self.stackB = Stack()
       

    def enqueue(self,value):
        self.stackA.push(value) 
    


    def dequeue(self):
        
     
        while self.stackA.top:
             last_changed_value = self.stackA.pop()
             self.stackB.push(last_changed_value)
        return self.stackB.pop()

   
    
  
    

if __name__ == "__main__":
    # stack = Stack()
    # stack.push(1)
    # stack.push(2)
    # stack.push(3)
    # print(stack.peek())# 2  
    # print(stack.pop()) # 3
    # print(stack.peek()) #2  
    # print(stack.isEmpty())#false
    new_q=PseudoQueue()
    new_q.enqueue(5)
    new_q.enqueue(10)
    new_q.enqueue(15)
    new_q.enqueue(20)
    print(new_q.dequeue())#5
    print(new_q.dequeue())#10
    print(new_q.stackB.peek())#15

  
