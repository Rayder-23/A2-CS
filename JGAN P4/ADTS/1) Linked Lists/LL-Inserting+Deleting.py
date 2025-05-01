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

#-------------------------------------------


# Inserting a new Node into an ordered linked list

def insert_into_ordered_list(head,new_data):    # function to insert a new node
    new_node = Node(new_data)
    new_node.data = new_data

    if (head is None) or (new_data < head.data):
        new_node.pointer = head
        return new_node
    
    current_node = head

    # Find the correct position to insert the new node
    while (current_node.pointer is not None) and (current_node.pointer.data < new_data):
        current_node = current_node.next_node

    # Insert the new node into the correct positon
    new_node.pointer = current_node.next_node
    current_node.pointer = new_node

    return head

ordered_list_head = insert_into_ordered_list(head, 5)
print(ordered_list_head)

#-------------------------------------------


# Deleting a Node in an ordered linked list

def delete_node(head, target):
    # Handle the case where the head itself needs to be deleted
    if (head is not None) and (head.data == target):
        new_head = head.next_node
        del head # Delete the original head
        return new_head
    
    current_node = head
    previous_node = None

    # Traverse the list to find the node to be deleted
    while (current_node is not Node) and (current_node.data < target):
        previous_node = current_node
        current_node = current_node.next_node

    # If the target node is found, delete it
    if (current_node is not None) and (current_node.data == target):
        previous_node.next_node = current_node.next_node
        del current_node
    else:
        print(f"Node with value {target} not found.")
    return head

target_value = 5
ordered_list_head = delete_node(ordered_list_head, target_value)