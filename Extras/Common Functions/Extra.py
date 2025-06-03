# --- ADVANCED BUT SYLLABUS-FRIENDLY EXAMPLES ---

# List comprehension: Squares of numbers
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Dictionary comprehension: Number to square mapping
square_dict = {x: x**2 for x in range(5)}  # {0:0, 1:1, 2:4, ...}

# Check if a key exists in a dictionary
student = {"name": "Ali", "grade": "A"}
if "name" in student:
    print("Name exists!")

# String concatenation with +=
message = ""
for word in ["Hello", "World"]:
    message += word + " "  # 'Hello World '

# f-string formatting (recommended)
name = "Ali"
marks = 90
result = f"Student {name} scored {marks}"  # 'Student Ali scored 90'

# Character <-> ASCII code
code = ord('A')  # 65
char = chr(66)   # 'B'