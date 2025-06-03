# --- DICTIONARY FUNCTIONS ---

student = {"name": "Ali", "grade": "A"}

# 1. get(key) - Returns value for key or None
grade = student.get("grade")  # 'A'

# 2. keys() - Returns a list-like view of keys
keys = list(student.keys())  # ['name', 'grade']

# 3. values() - Returns a list-like view of values
values = list(student.values())  # ['Ali', 'A']

# 4. items() - Returns (key, value) pairs
items = list(student.items())  # [('name', 'Ali'), ('grade', 'A')]

# 5. update(dict) - Updates with another dict
student.update({"grade": "A*", "age": 18})  # {'name': 'Ali', 'grade': 'A*', 'age': 18}

# 6. pop(key) - Removes and returns the value for key
age = student.pop("age")  # 18; student is now {'name': 'Ali', 'grade': 'A*'}