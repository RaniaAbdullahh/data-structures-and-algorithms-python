#from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import Queue,Node
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

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



class AnimalShelter(Queue):
    def __init__(self):
        self.front = None
        self.rear = None
        self.length=0
    
    def enqueue(self,animal):
        if animal == 'Dog' or animal == 'Cat':
            print('welcome to our shelter')
            self.enqueue(animal)
       
        else:
            print('we cant accept this animal ')   
    
    def dequeue(self,pref):
        if pref == 'Dog' or pref == 'Cat':
           temp = self.front 
           while(temp.next is not None and  temp.next.value != pref):
               temp = temp.next
               break


              
            
          
        else:
            return None


# class Cat:
#     def __init__(self,name):
#         self.name = name
#         self.kind = 'cat'

# class Dog:
#     def __init__(self,name):
#         self.name = name
#         self.kind = 'dog'

if __name__ == "__main__":
    shelter = AnimalShelter()
    shelter.enqueue('Dog')
    shelter.enqueue('Dog')
    shelter.enqueue('X')
    shelter.enqueue('S')
    #shelter.dequeue("fish")