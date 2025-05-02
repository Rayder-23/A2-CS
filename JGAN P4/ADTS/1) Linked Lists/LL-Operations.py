# Creating a Linked List
class Node:
    def __init__(self):
        self.data = None
        self.pointer = None

# Create a linked list with 5 nodes
head = Node()
current_node = head
current_node.data = 0

for i in range(1,4):
    new_node = Node()
    new_node.data = i * 2
    current_node.pointer = new_node
    current_node = new_node

# Addition: Linked List Visualized
def print_linked_list(head):
    current = head  # start from the head of the list
    while current is not None:  # loop until we reach the end of the list
        print(current.data, end=" -> ")  
        # end="\n" (default): prints a newline after each item.
        # end=" -> ": stays on the same line, adds " -> " instead of jumping to the next line.

        current = current.pointer  # move to the next node using the pointer
    print("None")  # print 'None' to mark the end of the linked list



#--------------------------------------------Separator----------------------------------------------



print("Before Insertion:")
print_linked_list(head) # 0 -> 2 -> 4 -> 6 -> None

# Inserting a new Node into an ordered(sorted) linked list

def insert_into_ordered_list(head,new_data):    # function to insert a new node
    new_node = Node()   # create a new node for the provided data/value
    new_node.data = new_data    # set the value to that node's data

    if (head is None) or (new_data < head.data):    
        # checkes if there is a head or if the new data is lesser than head's data
        new_node.pointer = head # sets the new_node to point at the head, aka node is placed behind head
        return new_node
    
    current_node = head # selects the head node

    # Find the correct position to insert the new node
    while (current_node.pointer is not None) and (current_node.pointer.data < new_data):
        # while the current node is pointing at something AND 
        # the data of the node (.data part) where current_node is pointing (current_node.pointer part)
        # is less than the new value

        current_node = current_node.pointer   # FIX: changed from next_node to pointer
        # moves current node up, to the next node

        # this will keep moving till one of those 2 conditions are False

    # Insert the new node into the correct positon
    new_node.pointer = current_node.pointer   # FIX: changed from next_node to pointer
    # sets the pointer of the new node to the next node

    current_node.pointer = new_node # set the pointer of the current node to the new node

    return head

ordered_list_head = insert_into_ordered_list(head, 5)
# print(ordered_list_head) # will only show the memory location of the next node

print("After Insertion:")
print_linked_list(ordered_list_head) # 0 -> 2 -> 4 -> 5 -> 6 -> None



#--------------------------------------------Separator----------------------------------------------
print("\t")



# Find an element in an ordered linked list

def find_in_ordered_list(head, target):
    current_node = head # selects the head node

    while (current_node is not None) and (current_node.data < target):
        # while the current node is not empty and it's data is lesser than the target value
        current_node = current_node.pointer # FIX: changed from next_node to pointer
        # move to the next node

    if (current_node is not None) and (current_node.data == target):
        # c-node is not empty and the c-data matches the target value
        return current_node
    else:
        return None
    
# Change target_value if you like
target_value = 5
found_node = find_in_ordered_list(head, target_value)

print(f"Finding value '{target_value}'...")

if found_node is not None:
    print(f"Node with value {target_value} found.")
else:
    print(f"Node with value {target_value} not found.")


    
#--------------------------------------------Separator----------------------------------------------
print("\t")



# Deleting a Node in an ordered linked list

def delete_node(head, target):
    # Handle the case where the head itself needs to be deleted
    if (head is not None) and (head.data == target):
        # if the head is not empty and it's data matching the target
        new_head = head.pointer # FIX: changed from next_node to pointer
        # moves the head to the next node/node which head.pointer is pointing at
        del head # Delete the original head
        return new_head
    
    current_node = head # selects the head node
    previous_node = None

    # Traverse the list to find the node to be deleted
    while (current_node is not Node) and (current_node.data < target):  # same conditions as in find
        previous_node = current_node    # set the p-node to the c-node
        current_node = current_node.pointer # FIX: changed from next_node to pointer
        # set the c-node to the next node/node which it is pointing at

    # If the target node is found, delete it
    if (current_node is not None) and (current_node.data == target):
        previous_node.pointer = current_node.pointer # FIX: changed from next_node to pointer
        # replace the pointer in p-node to use the value of c-node
        # this connects the p-node to the next node, now c-node can be deleted
        del current_node
    else:
        print(f"Node with value {target} not found.")
    return head

target_value = 5
ordered_list_head = delete_node(ordered_list_head, target_value)
print_linked_list(ordered_list_head)    # 0 -> 2 -> 4 -> 6 -> None