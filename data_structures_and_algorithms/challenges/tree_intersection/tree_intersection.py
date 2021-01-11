#from data_structures_and_algorithms.data_structures.tree.tree import Node,BinaryTree

class Node:
    def __init__(self, data=None, left=None, right=None, next=None):
        self.data = data
        self.left = left
        self.right = right
        self.next = next

class BinaryTree:
    def __init__(self):
        self.root = None 


    def pre_order(self):
        
     
        output = []
        def traverse(node):
            output.append(node.data)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)

        traverse(self.root)
        return output

  


def tree_intersection(first_tree,sec_tree):
   

    data1 = first_tree.pre_order()
    data2 = sec_tree.pre_order()
    lst = []
    for i in data1:
        for j in data2:
            if i == j:
                lst.append(i)
                j =+1
        i +=1 

    return set(lst)

    

if __name__ == "__main__":
    Bt1 = BinaryTree()
    Bt1.root = Node(6)
    Bt1.root.right = Node(9)
    Bt1.root.left = Node(2)
    Bt1.root.left.left = Node(0)
    Bt1.root.right.left = Node(10)

    Bt2 = BinaryTree()
    Bt2.root = Node(6)
    Bt2.root.right = Node(2)
    Bt2.root.left = Node(10)
    Bt2.root.left.left = Node(18)



    print(tree_intersection(Bt1,Bt2)) 
