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



class Cat():
    def __init__(self,name):
        self.name = name
        self.kind = 'cat'

class Dog():
    def __init__(self,name):
        self.name = name
        self.kind = 'dog'


class AnimalShelter:
    def __init__(self):
        self.cat_queue = Queue()
        self.dog_queue = Queue()

    def enqueue(self,animal):
        if animal.kind == 'cat':
            self.cat_queue.enqueue(animal)
            
        if animal.kind == 'dog':
            self.dog_queue.enqueue(animal)
              
    def dequeue (self,kind):

        if kind == 'cat':

            cat = self.cat_queue.dequeue()
            return cat.name

        elif kind == 'dog':        
            dog = self.dog_queue.dequeue()
            return dog.name


if __name__ == "__main__":
    mylo = Dog('mylo')
    reixy = Dog('reixy')
    luna = Dog('luna')
    kitty = Cat('kitty')
    lily = Cat('lily')
    a = AnimalShelter()
    a.enqueue(mylo)
    a.enqueue(reixy)
    a.enqueue(luna)
    a.enqueue(kitty)
    a.enqueue(lily)
    #a.enqueue(sno)
    print(a.dequeue('dog'))
    #a.dequeue('dog')
    print(a.dequeue('dog'))
    print(a.dequeue('dog'))