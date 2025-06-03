# --- FILE HANDLING ---

# Write to a file (overwrites if exists)
with open("example.txt", "w") as file:
    file.write("This is a line.\n")

# Append to a file
with open("example.txt", "a") as file:
    file.write("Another line.\n")

# Read entire file
with open("example.txt", "r") as file:
    content = file.read()  # Returns string

# Read lines into a list
with open("example.txt", "r") as file:
    lines = file.readlines()  # Returns list of lines