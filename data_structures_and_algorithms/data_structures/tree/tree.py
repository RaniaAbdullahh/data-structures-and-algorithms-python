class Node_q:
    def __init__(self,value):
        self.value=value
        self.next=None
class Queue :
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self,data):
        ''' takes any value as an argument and adds a new node with that value to the back of the queue '''
        node = Node_q(data)
        if self.rear:
            self.rear.next = node
            self.rear = node
        else:
            self.front = node
            self.rear = node

    def dequeue(self):
        '''  removes the node from the front of the queue, and returns the node’s value.'''
        try:
            val=self.front
            self.front=self.front.next
            val.next=None
            return val.value
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



class Node:
    def __init__(self, data=None, left=None, right=None, next=None):
        self.data = data
        self.left = left
        self.right = right
        self.next = next

class BinaryTree:
    def __init__(self, data=None):
        if data:
            data = Node(data)
        self.root = data


    def post_order(self, node=None, result=[]):
        '''Return an array from tree in post-order order'''
        
        node = node or self.root

        if node.left:
            self.post_order(node.left, result)

        if node.right:
            self.post_order(node.right, result)

        result.append(node.data)

        return result

    def pre_order(self, node=None, result=[]):
        '''Return an array from tree in pre-order order'''
        
        node = node or self.root
        result.append(node.data)

        if node.left:
            self.pre_order(node.left, result)

        if node.right:
            self.pre_order(node.right, result)

        return result


    def in_order(self, node=None, result=[]):
        '''Return an array from tree in in_order order.'''
        
        node = node or self.root
        
        if node.left:
            self.in_order(node.left, result)

        result.append(node.data)

        if node.right:
            self.in_order(node.right, result)

        return result



    def find_maximum_value(self, root):  
        
        if(self.root == None):  
            return 'Tree is empty'  
                
        else:      
            maximum = root.data  
                
            
            if(root.left != None):

                leftMax = self.find_maximum_value(root.left)  
                maximum = max(maximum, leftMax)  
                 
            if(root.right != None):  
                rightMax = self.find_maximum_value(root.right)   
                maximum = max(maximum, rightMax) 
                
            return maximum  



class BinarySearchTree(BinaryTree):
    '''Create a Binary Search Tree by importing a Binary Tree'''
    def __init__(self, data=None):
        super().__init__(data)

    def add(self, data):
        '''Adds new node to BST'''

        node = Node(data)

        if not self.root:
            self.root = node

            return

        current = self.root

        while True:
            if node.data < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = node

                    return

            else:
                if current.right:
                    current = current.right
                else:
                    current.right = node

                    return

    def contains(self, data):
        ''' Return Boolean indicating existence (but not location) of value on tree '''

        if not self.root:
            return False

        current = self.root

        while True:
            if data == current.data:
                
                return True

            
            if data < current.data:
                if current.left:
                    current = current.left
                else:

                    return False

           
            else:
                if current.right:
                    current = current.right
                else:
                    return False

   



if __name__ == "__main__":
    tree = BinaryTree()
    tree.root=Node(5)
    tree.root.left = Node(3)
    tree.root.right = Node(7) 
    print(tree.post_order())
    print('maximum value : ' ,tree.find_maximum_value(tree.root)) 