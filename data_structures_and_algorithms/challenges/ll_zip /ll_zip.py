# class Node():
#     """
#     this class will create a new node  
#     """
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class LinkedList:

#      def __init__(self):
#         self.head=None
#         self.size=0


#     def __str__(self) :

#         current=self.head
#         result=''

#         if current == None:
#             return 'Empty List'
#         else:
#             while current:
#                 result += f'{{{current.value}}}->'
#                 current=current.next   
#             result += f'NULL'
#         return result 

#     def append(self, data):
        
#         node = Node(data)
#         if self.head == None:
#             self.head = node
#         else:
#             current = self.head
#             while current.next != None:
#                 current = current.next
#             current.next = node




#     @staticmethod
#     def zipLists(list1,list2):
#         """
#         akes two linked lists as arguments. Zip the two linked lists together into one so that
#         the nodes alternate between the two lists and return a reference to the head of the zipped list. 
#         """
#         try:
#             nodes_counter_li1 = 0
#             nodes_counter_li2 = 0
#             current = list1.head
#             while current != None:
#                 current = current.next
#                 nodes_counter_li1 = nodes_counter_li1 + 1 

#             current = list2.head
#             while current != None:
#                 current = current.next
#                 nodes_counter_li2 = nodes_counter_li2 + 1 

#             if nodes_counter_li1>nodes_counter_li2:
#                 curr = list1.head 
#                 list2_curr = list2.head 
#                 while curr != None and list2_curr != None: 
#                     list1_next = curr.next
#                     list2_next = list2_curr.next
        
#                     list2_curr.next = list1_next 
#                     curr.next = list2_curr 

#                     curr = list1_next 
#                     list2_curr = list2_next 

#                 list2.head = list2_curr 
#                 return list1
#             else:
#                 curr = list2.head 
#                 list1_curr = list1.head 
#                 while curr != None and list1_curr != None: 
#                     list2_next = curr.next
#                     list1_next = list1_curr.next
        
#                     list1_curr.next = list2_next 
#                     curr.next = list1_curr 

#                     curr = list2_next 
#                     list1_curr = list1_next 

#                 list1.head = list1_curr 
#                 return list2
#         except Exception as err:
#             print(f'error line 247 __str__ {err}')

# if __name__=="__main__":
#     pass            