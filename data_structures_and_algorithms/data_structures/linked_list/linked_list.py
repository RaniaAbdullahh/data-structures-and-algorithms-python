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

    def append(self, data):
        
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node

    
    def insert_before(self, value, newvalue):
        '''
        Add a new node with  new Value before the first value node

        '''
        node = Node(newvalue)
        current = self.head
        while current != None:
            if current.value == value:
                node.next = current
                self.head = node
                return
            if current.next:
                if current.next.value == value:
                    node.next = current.next
                    current.next = node
                    return 'secssfuly added'
                current = current.next

    def insert_after(self, value, newvalue):
        '''
        Add a new node with newVal after the first value node

        '''
        node = Node(newvalue)
        current = self.head
        while current != None:
            if current.value == value:
                node.next = current.next
                current.next = node
                return 'secssfuly added'
            current = current.next 

    def kth_from_end(self, k):
        '''
        Return node value (k) from the end of the list

        '''

        try:
                
            n = -1
            current = self.head
            while current:
                current = current.next
                n = n + 1
            if n >= k:
                current = self.head
                for i in range(n - k):
                    current = current.next
            return current.value
        except:
            return "The Value Not Exist"

    @staticmethod
    def zipLists(list1,list2):
        """
        akes two linked lists as arguments. Zip the two linked lists together into one so that
        the nodes alternate between the two lists and return a reference to the head of the zipped list. 
        """
        try:
            nodes_counter_li1 = 0
            nodes_counter_li2 = 0
            current = list1.head
            while current != None:
                current = current.next
                nodes_counter_li1 = nodes_counter_li1 + 1 

            current = list2.head
            while current != None:
                current = current.next
                nodes_counter_li2 = nodes_counter_li2 + 1 

            if nodes_counter_li1>nodes_counter_li2:
                curr = list1.head 
                list2_curr = list2.head 
                while curr != None and list2_curr != None: 
                    list1_next = curr.next
                    list2_next = list2_curr.next
        
                    list2_curr.next = list1_next 
                    curr.next = list2_curr 

                    curr = list1_next 
                    list2_curr = list2_next 

                list2.head = list2_curr 
                return list1
            else:
                curr = list2.head 
                list1_curr = list1.head 
                while curr != None and list1_curr != None: 
                    list2_next = curr.next
                    list1_next = list1_curr.next
        
                    list1_curr.next = list2_next 
                    curr.next = list1_curr 

                    curr = list2_next 
                    list1_curr = list1_next 

                list1.head = list1_curr 
                return list2
        except Exception as err:
            print(f'error : {err}')

              







if __name__ == "__main__":
    # #pass
    # brothers = LinkedList()
    # # node1=Node('rania')
    # # node2=Node('Moh')
    # # node2.next=node1
    # brothers.append('rania')
    # brothers.append('moh')
    # brothers.append('Malk')
    # # brothers.insert('aml')
    # print(brothers)
    # if brothers.includes('rania'): 
    #     print ('True') 
    # else: 
    #     print ('false')
    llist = LinkedList() 
    llist1 = LinkedList() 
    llist2 = LinkedList() 
    llist1.append(3) 
    llist1.append(2) 
    llist1.append(1) 

  
    llist2.append(8) 
    llist2.append(7) 
    llist2.append(6)
    llist2.append(5) 
    llist2.append(5)
    print(llist.zipLists(llist1,llist2).__str__())