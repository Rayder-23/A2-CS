# Creating a Linked List
class Node:
    def __init__(self):
        self.data = None
        self.pointer = None

# Create a linked list with 5 nodes
head = Node()
current_node = head

for i in range(4):
    new_node = Node()
    current_node.data = i * 2
    current_node.pointer = new_node
    current_node = new_node


#--------------------------------------------Separator----------------------------------------------


# Find an element in an ordered linked list

def find_in_ordered_list(head, target):
    current_node = head

    while (current_node is not None) and (current_node.data < target):
        current_node = current_node.next_node

    if (current_node is not None) and (current_node.data == target):
        return current_node
    else:
        return None
    
target_value = 5
found_node = find_in_ordered_list(head, target_value)

if found_node is not None:
    print(f"Node with value {target_value} found.")
else:
    print(f"Node with value {target_value} not found.")