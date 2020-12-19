from data_structures_and_algorithms.challenges.fifo_animal_shelter.fifo_animal_shelter import AnimalShelter,Dog,Cat


def test_dequeue_and_enqueue():
    mylo = Dog('mylo')
    reixy = Dog('mylo')
    luna = Dog('luna')
    kitty = Cat('kitty')
    lily = Cat('lily')
    a = AnimalShelter()
    a.enqueue(mylo)
    a.enqueue(reixy)
    a.enqueue(luna)
    a.enqueue(kitty)
    a.enqueue(lily)

    assert a.dequeue('cat') == 'kitty'
    assert a.dequeue('cat') == 'lily'
    assert a.dequeue('dog') == 'mylo'
    assert a.dequeue('dog') == 'mylo'
    assert a.dequeue('dog') == 'luna'