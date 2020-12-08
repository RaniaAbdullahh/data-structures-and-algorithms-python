from data_structures_and_algorithms.data_structures.linked_list.linked_list import LinkedList
import pytest



def test_instantiate_linked_list():
    """
    empty linked list
    """
    ll = LinkedList()
    
    assert ll.head == None


def test_str(prep_ll):
   
    assert prep_ll.__str__() == '{Moh}->{Rania}->NULL'

def test_incloud_value(prep_ll):
    """"
     Will return true when finding a value within the linked list that exists
    """
  
    assert prep_ll.includes('Moh')
    

def test_incloud_false_value(prep_ll):
    """"
     Will return False when finding a value within the linked list that not exists
    """
   
    assert prep_ll.includes('aml')==False
    
def test_append(app_ll):
    '''
    to check if  can successfully add a node to the end of the linked list
    ''' 
    assert app_ll.head.value == 'Rania'
    assert app_ll.head.next.value == 'Moh'
    assert app_ll.head.next.next == None

def test_insert_before_middle():
    """
      to check if Can successfully insert a node before a node located in the middle of a linked list
    """
    ll = LinkedList()
    ll.append('rania')
    ll.append('Moh')
    ll.append('aml')
    ll.insert_before('Moh', 33)
    assert ll.head.next.value == 33

def test_insert_after_middle():
    """
      to check if Can successfully insert after a node in the middle of the linked list
    """
    ll = LinkedList()
    ll.append('rania')
    ll.append('Moh')
    ll.append('aml')
    ll.insert_after('Moh', 33)
    assert ll.head.next.next.value == 33   


@pytest.fixture
def prep_ll():
    ll = LinkedList()
    ll.insert('Rania')
    ll.insert('Moh')
    return ll

@pytest.fixture
def app_ll():
    ll = LinkedList()
    ll.append('Rania')
    ll.append('Moh')
    return ll

def test_kth_from_end_0():
    '''
    Where k and the length of the list are the same

    '''
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    expected = "The Value Not Exist"
    actual =ll.kth_from_end(3)
    assert expected == actual
    
def test_kth_from_end_6():
    '''
     Where k is greater than the length of the linked list

    '''
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    expected = "The Value Not Exist"
    actual =ll.kth_from_end(6)
    assert expected == actual

def test_kth_from_end_2():
    '''
     Happy Path” where k is not at the end, but somewhere in the middle of the linked list

    ''' 
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    expected = 3
    actual =ll.kth_from_end(2)
    assert expected == actual


def test_kth_from_end_size_one():
    '''
     Where the linked list is of a size 1 

    '''
    ll = LinkedList()
    ll.append(1)
    expected = 1
    actual =ll.kth_from_end(0)
    assert expected == actual

def test_kth_from_end_negative():
    '''
     Where k is not a positive intege

    ''' 
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    expected = "The Value Not Exist"
    actual =ll.kth_from_end(-2)
    assert expected == actual

def test_zipLists1():
    llist = LinkedList() 
    llist1 = LinkedList() 
    llist2 = LinkedList() 
    llist1.append(3) 
    llist1.append(2) 
    llist1.append(1) 
  
    llist2.append(8) 
    llist2.append(7) 
    llist2.append(6)
    assert llist.zipLists(llist1,llist2).__str__() =='{8}->{3}->{7}->{2}->{6}->{1}->NULL'

def test_zipLists2():
    llist = LinkedList() 
    llist1 = LinkedList() 
    llist2 = LinkedList() 
    llist1.append(3) 
    llist1.append(2) 
    llist1.append(1) 
    llist1.append(0) 
    llist1.append(0) 
  
    llist2.append(8) 
    llist2.append(7) 
    llist2.append(6)
    assert llist.zipLists(llist1,llist2).__str__() =="{3}->{8}->{2}->{7}->{1}->{6}->{0}->{0}->NULL"

def test_zipLists3():
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
    assert llist.zipLists(llist1,llist2).__str__() =="{8}->{3}->{7}->{2}->{6}->{1}->{5}->{5}->NULL"
