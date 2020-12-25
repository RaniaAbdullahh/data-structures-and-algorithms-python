from data_structures_and_algorithms.data_structures.tree.tree import BinaryTree,Node




def fizz_buzz_tree(tree):
    ''' takes a k-ary tree as an argument 
    determine whether or not the value of each node is
    divisible by 3, 5 or both. 
    '''
    new_tree = BinaryTree()
    new_node = Node()

    if tree.root == None:
        return new_tree
        
    old_node = tree.root   # root is ref to first node



    def visit_node(old_node, new_node):

        new_node.data = fizz_buzz(old_node.data)
        if old_node.left:
            new_node.left = Node()
            visit_node(old_node.left, new_node.left)

        if old_node.right:
            new_node.right = Node()
            visit_node(old_node.right, new_node.right)

    def fizz_buzz(old_value):

        result = ''
        if old_value % 3 == 0:
            result += 'Fizz'

        if old_value % 5 == 0:
            result += 'Buzz'

        return result or str(old_value)

    visit_node(old_node, new_node)

    new_tree.root = new_node

    return new_tree

# if __name__ == "__main__":
  
#     tree = BinaryTree()
#     tree.root = Node(3)
#     tree.root.left = Node(5)
#     tree.root.right = Node(7)
#     tree.root.left.left = Node(15)
#     print(fizz_buzz_tree(tree))