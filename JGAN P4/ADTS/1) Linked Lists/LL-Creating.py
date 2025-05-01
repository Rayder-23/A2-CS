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