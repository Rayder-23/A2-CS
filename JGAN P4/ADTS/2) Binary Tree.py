# A hierahical data structure where each node has at most 2 children, referred to as the left child and 
# right child

# Root Node(1st) -> Parent/Child Node(2nd) -> Leaf Node(3rd layer)

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None   # in linked list, only one pointer, here we have 2

# making a function to add a node/value
def add_node(root,value):
    if root is None:    # if the first node is empty, then add the value to that node
        return Node(value)  # return it
    
    current = root  # puts the root value in current, 'G'
    while True:
        if value < current.data:    # compares if the value to be added is lesser than the current value
            # 'D' < 'G'
            if current.left is not None:    # checks the left node, is it empty?
                # if it is None, it will return False
                current = current.left  
                # if not/True, then select the left node as the new current/root node to be compared too

            else:
                current.left = Node(value)  # if yes/False, then places the value to be added at the left
                break   # stops the loop as the value has been placed

            # 'J' < 'G', False, so else block will play
        else:
            if current.right is not None:   # checks the right node, is it empty?
                current = current.right
                # if not/True, then select the right node as the new current/root node to be compared too

            else:
                current.right = Node(value) # if yes/False, then places the value to be added at the right
                break   # stops the loop as the value has been placed
    
    return root

# Example usage:
binary_tree_root = Node('G')    # Creates a node with value 'G' and no children nodes

# Adding 6 nodes to the tree in a balanced manner
values_to_add = ['D','J','B','F','H','L']

for value in values_to_add:
    binary_tree_root = add_node(binary_tree_root,value)


#--------------------------------------------Separator----------------------------------------------


# Finding a node

# making a function to find a node/value
def find_node(root,value):
    current = root  # sets root to current

    while current is not None:  # if the root is not empty then
        if current.data == value:   # if the current node matches with the value, 
            return current  # then return the current node, this also ends the while loop
        
        elif value < current.data:  # if the value is lesser than the current value,
            current = current.left  # set current to the left node
        else:
            current = current.right # else set current to the right node

    return None # if the value is not found, return None

# Assuming binary_tree_root is the root of the binary tree (aka using previous code)

value_to_find = 'H'
found_node = find_node(binary_tree_root, value_to_find)

if found_node is not None:
    print(f"Node with value '{value_to_find}' found.")
else:
    print(f"Node with value '{value_to_find}' not found.")

# Code works aka outputs correctly, Python version 3.12.6, should work in lower versions as well