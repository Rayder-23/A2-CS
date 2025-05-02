# Creating a Linked List
class Node:
    def __init__(self):
        self.data = None
        self.pointer = None

# Create a linked list with 5 nodes
head = Node()
current_node = head
current_node.data = 0

for i in range(1, 4):
    new_node = Node()   # makes a new node
    new_node.data = i * 2   # sets data to the new node
    current_node.pointer = new_node # sets the pointer of the current node to the new node
    current_node = new_node # sets current node to the new node
    # repeats 4 times, 5 nodes total (head + 4 new)



# Addition: Linked List Visualized
def print_linked_list(head):
    current = head  # start from the head of the list
    while current is not None:  # loop until we reach the end of the list
        print(current.data, end=" -> ")  # print the current node's data with an arrow
        current = current.pointer  # move to the next node using the pointer
    print("None")  # print 'None' to mark the end of the linked list

print_linked_list(head)