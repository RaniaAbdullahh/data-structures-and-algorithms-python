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

