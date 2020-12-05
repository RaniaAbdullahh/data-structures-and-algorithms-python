class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList :
    def __init__(self):
        self.head=None
        self.size=0

    def insert(self,value):
        node=Node(value)
        if self.head == None:
            self.head = node
        else:
            node.next=self.head
            self.head=node
        self.size+=1      


    def includes (self,value):
        current=self.head
        while current and current.next != None:
            if current.value == value:
                return True
            current=current.next
        return False


    def __str__(self):
        current=self.head
        result=''

        if current == None:
            return 'Empty List'
        else:
            while current:
                result += f'{{{current.value}}}->'
                current=current.next   
            result += f'NULL'
        return result      






if __name__ == "__main__":
    pass
    # brothers = LinkedList()
    # node1=Node('rania')
    # node2=Node('Moh')
    # node2.next=node1
    # brothers.insert('rania')
    # brothers.insert('moh')
    # brothers.insert('Malk')
    # brothers.insert('aml')
    # print(brothers)
    # if brothers.includes('rania'): 
    #     print ('True') 
    # else: 
    #     print ('false')
