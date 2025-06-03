# --- LIST (ARRAY) FUNCTIONS ---

# 1. append(item) - Adds item to the end of the list
fruits = ["apple", "banana"]
fruits.append("cherry")  # ['apple', 'banana', 'cherry']

# 2. pop(index) - Removes and returns item at given index; if index is not given, removes last item
removed_item = fruits.pop()  # Removes 'cherry'; returns 'cherry'

# 3. insert(index, item) - Inserts item at specified index
fruits.insert(1, "orange")  # ['apple', 'orange', 'banana']

# 4. remove(item) - Removes the first occurrence of the item
fruits.remove("orange")  # ['apple', 'banana']

# 5. slice (list[start:end]) - Returns a sublist from start to end-1
subset = fruits[0:2]  # ['apple', 'banana']

# 6. index(item) - Returns index of first occurrence of item
index = fruits.index("banana")  # 1

# 7. count(item) - Returns number of occurrences of item
count = fruits.count("apple")  # 1