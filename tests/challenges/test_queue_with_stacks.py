from data_structures_and_algorithms.challenges.queue_with_stacks.queue_with_stacks.py import psueodoQueue,Stack

def test_enqueue():
    q = psueodoQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(5)
    actual = q.A.peek()
    assert actual == 5

def test_dequeue():
   
    q = PseudoQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(5)
    assert q.dequeue() == 1