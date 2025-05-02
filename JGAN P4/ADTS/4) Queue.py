# Queue:
# FIFO, First In, First Out
# Insert -> at Tail
# Remove -> at Head
# Circular Queues, they loop


# defining a queue variable

front_of_queue = 0
end_of_queue = -1
number_in_queue = 0
max_queue_size = 5

my_queue = [None]*max_queue_size


# making a function to add a new item in the queue
def add_to_queue(newItem):
    global number_in_queue, end_of_queue # fix: globalise

    if number_in_queue < max_queue_size:    # checking if queue is full or not
        end_of_queue = end_of_queue +1 # '-1 +1 = 0' move end_of_queue up 

        if end_of_queue > max_queue_size:   # circular queue code
            end_of_queue = 0    # goes back to the start of queue, as it knows the queue is not full
        
        my_queue[end_of_queue] = newItem # puts the new value at the new end_of_queue
        number_in_queue = number_in_queue +1 # adds to the total value count


# making a function to remove an item in the queue and return it
def remove_from_queue():
    global number_in_queue, end_of_queue, front_of_queue # fix: globalise

    if number_in_queue > 0: # check if queue is empty, if not then

        item = my_queue[front_of_queue] # take out the current item
        my_queue[front_of_queue] = None # Addition: setting the current value to None

        number_in_queue = number_in_queue -1 # subtract from the total value count

        if number_in_queue == 0:    # if queue is empty, then reset the queue
            front_of_queue = 0  # Original positions
            end_of_queue = -1   

        else:
            front_of_queue = front_of_queue +1 # move front up as the previous front value has been removed

            if front_of_queue > max_queue_size -1: # circular queue code
                front_of_queue = 0  # goes back to start of queue

    return item



add_to_queue("Z")
add_to_queue("A")
print(my_queue) # ['Z', 'A', None, None, None]

removedValue = remove_from_queue()
print(removedValue) # Z
print(my_queue) # [None, 'A', None, None, None]


add_to_queue("Saand")
add_to_queue("Bun Kebab")
print(my_queue)     # [None, 'A', 'Saand', 'Bun Kebab', None]

remove_from_queue()
remove_from_queue()
print(my_queue)     # [None, None, None, 'Bun Kebab', None]