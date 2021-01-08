from data_structures_and_algorithms.challenges.hashtable.hashtable import Hashmap



def test_hash_key():
    ''' function that  test the conversion to ascii number ''' 
    hashtab=Hashmap(1024)
    actual =hashtab.hash('gen')
    assert actual == 218


def test_contain_key():
    ''' test  to check if a sertain key is exist or not '''
    hashtab=Hashmap(1024)
    hashtab.add('color','blue')
    actual =hashtab.contains('color')
    assert actual == True


def test_get_key_and_value():
    ''' function to test if the get methoud return the value of a spesific key '''
    hashtab=Hashmap(1024)
    hashtab.add('name','Rania')
    actual = hashtab.get('name')
    assert actual == 'Rania'
             
