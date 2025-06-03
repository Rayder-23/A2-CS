# --- CUSTOM FUNCTIONS FOR POP AND APPEND ---

# Custom pop: Removes and returns the last element from the list
def custom_pop(my_list):
    """
    Mimics the .pop() method.
    Removes the last item from the list and returns it.
    Returns None if the list is empty.
    """
    if len(my_list) == 0:
        return None  # Handle empty list safely
    last_item = my_list[-1]  # Get last item
    del my_list[-1]          # Remove last item from list
    return last_item         # Return removed item

# Custom append: Adds an item to the end of the list
def custom_append(my_list, item):
    """
    Mimics the .append() method.
    Adds an item to the end of the list.
    """
    my_list += [item]  # Add item using list addition




# --- EXAMPLES OF USING CUSTOM FUNCTIONS ---

# Initial list
nums = [10, 20, 30]
print("Original list:", nums)  # Output: [10, 20, 30]

# Append an item
custom_append(nums, 40)
print("After custom_append(40):", nums)  # Output: [10, 20, 30, 40]

# Pop the last item
last_item = custom_pop(nums)
print("Item removed with custom_pop():", last_item)  # Output: 40
print("List after custom_pop():", nums)  # Output: [10, 20, 30]

# Pop again
another = custom_pop(nums)
print("Another item removed:", another)  # Output: 30
print("List now:", nums)  # Output: [10, 20]

# Try to pop until the list is empty
custom_pop(nums)  # Removes 20
custom_pop(nums)  # Removes 10
empty_result = custom_pop(nums)  # Now list is empty
print("Result of pop on empty list:", empty_result)  # Output: None