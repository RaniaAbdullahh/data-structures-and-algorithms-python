## table of content 
|  challange name   |                                  pull request                                  |  
|-------------------|--------------------------------------------------------------------------------|
| arry_reverse      | https://github.com/RaniaAbdullahh/data-structures-and-algorithms-python/pull/1 |
| arry_shift        | https://github.com/RaniaAbdullahh/data-structures-and-algorithms-python/pull/2 |
|  arry_binary_shift|https://github.com/RaniaAbdullahh/data-structures-and-algorithms-python/pull/3  |





# Reverse an Array
Python provides us with various ways of reversing a list, We will go through very  simple  technique on how a list in python can be reversed.
## Challenge
the challage is that we are given a list as input and we have to reverse it as an output 
## Approach & Efficiency
I used a simple technique which depends on  looping through the list and print the element with an index i which i the decreased length by 1 rank 
## Solution
<!-- Embedded whiteboard image -->
![Embedded whiteboard image](assets/array-reverse.png)

# shift an array 
shift an array means to change the places of the the list element either to the right or left by adding a new element to it 

## Challenge Description
Write a function called insertShiftArray which takes in an array and the value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

## Approach & Efficiency
we worked depending on the indexes and the length of the list, if the list length is evevn we will add it to the [len/2] and f the length is odd will add the num to index [len/2+1]

## Solution
![Embedded whiteboard image](assets/array_shift.png)


# array binary search
  function takes in 2 parameters: a sorted array and the search key.  return the index of the array’s element that is equal to the search key, or -1 if the element does not exist.
## Challenge Description
 function takes in 2 parameters: a sorted array and the search key.  return the index of the array’s element that is equal to the search key, or -1 if the element does not exist.

## Approach & Efficiency
* to return the index of the wanted number if exist and return -1 if doesnt exist
*  use simple technique which depends on the binary search 
* we worked depending on the indexes and the length of the list..

## Solution
![Embedded whiteboard image](assets/binary_shift.png)



# linked list
to Create a linked list with  Nodes  that has properties for the value stored in the Node, and a pointer to the next Node.also with ability to add new nodes in the head of tke linked list 
## Challenge Description
to Create a linked list with  Nodes  that has properties for the value stored in the Node, and a pointer to the next Node.also with ability to add new nodes in the head of tke linked list 

## Approach & Efficiency
* first I will  define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance
* then define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
* finally define a method called toString (or __str__ in Python) which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"

## Solution
![Embedded whiteboard image](assets/linked_list_1.png)