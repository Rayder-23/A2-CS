# Stack:
# LIFO, Last In First Out
# Insert = push()
# Remove = pop()


# defining a stack variable
base_of_stack = 0
top_of_stack = -1   # -1 means stack is empty
max_stack_size = 5

my_stack = [None]*max_stack_size # = [None,None,None,None,None], using array/list data type

# making a function to add a new item in the stack
def push(newItem):
    global top_of_stack  # **fix applied: global declaration** 
    if top_of_stack < max_stack_size -1:   # checks if stack is full or not 
        # '-1 < 5-1', True
        top_of_stack = top_of_stack +1  # -1 +1 = 0, new top_of_stack value
        my_stack[top_of_stack] = newItem # puts the value at my_stack[0], aka the 1st position

push("A")
push("Z")
push("C")
print(my_stack) # ['A', 'Z', 'C', None, None]


# making a function to remove an item in the stack and return it
def pop():
    global top_of_stack  # **fix applied: global declaration** 
    if top_of_stack > -1:   # checks if stack is empty or not
        # '2 > -1', True
        item = my_stack[top_of_stack]   # puts the top value in item
        top_of_stack = top_of_stack -1  
        # moves top_of_stack down one value, basically ignoring the above value
        return item # returns the item removed

removedValue = pop()
print(removedValue) # C
print(my_stack) # ['A', 'Z', 'C', None, None], C is still there 
# but it is ignored as the top_of_stack pointer is below it.
# check out MAK code for stack to see another angle, he also deletes the variable from the stack


# Info regarding the fix applied:

# In Python, reading a global variable inside a function is allowed without declaring it as global.
# But modifying (assigning to) it requires a global declaration.

# In contrast, when you do this:
# top_of_stack = top_of_stack + 1

# Python sees top_of_stack on the left side of =, and so assumes it's a new local variable.
# But you're also trying to read it first (top_of_stack + 1), and at that point, the 
# local version hasn't been assigned yet — hence the UnboundLocalError.