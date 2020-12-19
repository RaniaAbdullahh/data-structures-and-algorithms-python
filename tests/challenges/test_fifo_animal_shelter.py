from data_structures_and_algorithms.challenges.fifo_animal_shelter.fifo_animal_shelter import AnimalShelter


def test_dequeue_no_pref():
  shelter = AnimalShelter()
  shelter.enqueue_dog_or_cat('Dog')
  shelter.enqueue_dog_or_cat('Cat')
  shelter.enqueue_dog_or_cat('Dog')
  shelter.enqueue_dog_or_cat('Dog')
  shelter.enqueue_dog_or_cat('Cat')

  assert shelter.dequeue_dog_or_cat() == "Dog"