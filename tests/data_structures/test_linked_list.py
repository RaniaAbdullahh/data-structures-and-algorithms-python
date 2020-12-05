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
    


@pytest.fixture
def prep_ll():
    ll = LinkedList()
    ll.insert('Rania')
    ll.insert('Moh')
    return ll


