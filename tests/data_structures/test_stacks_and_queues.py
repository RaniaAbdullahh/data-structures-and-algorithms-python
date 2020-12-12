from data_structures_and_algorithms.data_structures.stacks_and_queues.stacks_and_queues import Stack,Queue
import pytest

def test_push_multiple_items(prep_stack):
    '''Can successfully push multiple values onto a stack'''
    assert prep_stack.peek() == 3

def test_pop_an_item(prep_stack):
    '''Can successfully pop off the stack'''
    assert  prep_stack.pop()== 3
def  test_empty_stack():
    ''' Calling dequeue or peek on empty queue raises exception'''
    stack = Stack()
    assert stack.peek()=='Empty stack'

@pytest.fixture
def prep_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    return stack

def test_enqueue_multiple_items(prep_queue):
    '''Can successfully push multiple values onto a queue'''
    assert prep_queue.peek() == 1

def test_dequeue_an_item(prep_queue):
    assert  prep_queue.dequeue()== 1

def  test_empty_queue():
    ''' Calling dequeue or peek on empty queue raises exception'''
    queue = Queue()
    assert queue.dequeue()=='Empty Queue'



@pytest.fixture
def prep_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    return queue

