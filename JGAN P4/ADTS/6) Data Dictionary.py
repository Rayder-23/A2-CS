# Define a dictionary
student_info = {
    "name": "Alice",
    "age": 25,
    "grade": "A",
    "subject": "Math"
}

# Access values using keys
print("Name:", student_info["name"])
print("Age:", student_info["age"])
print("Grade:", student_info["grade"])
print("Subject:", student_info["subject"])
# Name: Alice
# Age: 25
# Grade: A
# Subject: Math


# Modify a value
student_info["age"] = 26

# Add a new key-value pair
student_info["city"] = "New York"

# Print the updated dictionary
print("Updated Student Info:", student_info)
# Updated Student Info: {'name': 'Alice', 'age': 26, 'grade': 'A', 'subject': 'Math', 'city': 'New York'}