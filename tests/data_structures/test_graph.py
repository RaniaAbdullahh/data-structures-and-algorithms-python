import pytest
from data_structures_and_algorithms.data_structures.graph.graph import Node,Graph


def test_add_node(): 
    
    graph = Graph()

    actual = graph.add_node('hello').value

    assert actual ==  'hello' 

def test_add_edge_start():
    
    graph = Graph()

    start = Node('start')

    end = graph.add_node('end')

    actual = graph.add_edge(start, end)
    assert actual =='Start node is not exist in Graph'


def test_add_edge_end():
    
    graph = Graph()

    end = Node('end')

    start = graph.add_node('start')

    actual = graph.add_edge(start, end)
    assert actual == 'End node is not exist in Graph'

       
def test_add_edge_other_case():
    
    graph = Graph()

    end = graph.add_node('end')

    start = graph.add_node('start')

    graph.add_edge(start, end)



def test_get_nodes():

    graph = Graph()

    hi = graph.add_node('hi')

    hello = graph.add_node('hello')


    actual = len(graph.get_nodes())
    
    assert actual == 2




def test_get_neighbors():

    graph = Graph()

    hi = graph.add_node('hi')
    hello = graph.add_node('hello')

    graph.add_edge(hi, hello)

    actual = graph.get_neighbors(hi)

    assert actual == [(hello, 0)]

def test_size():

    graph = Graph()

    graph.add_node('hello')

    expected = 1

    actual = graph.size()

    assert actual == expected







def test_size_empty(): 

    graph = Graph()

    expected = 0

    actual = graph.size()

    assert actual == expected