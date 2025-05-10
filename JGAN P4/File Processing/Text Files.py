# Writing to a text file:

# Open a file in write mode ('w')
file = open('output.txt', 'w')
# Write a line of text to the file
file.write("This is a line of text.")
# Close the file
file.close()


# Reading from a text file:

# Open a file in read mode ('r')
file = open('output.txt', 'r')
# Read a line of text from the file
line = file. readline()
print(line) # Prints the read line
# Close the file
file.close()


# Appending to a text file:

# Open a file in append mode ('a')
file = open('output.txt', 'a' )
# Append a line of text to the file
file.write("\nThis is another line of text.")
# Close the file
file.close()



# Write Multiple Lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
# with open("example.txt", "w") as file:
#     file.writelines(lines)

# OR
with open("example.txt", "w") as file:
    for line in lines:
        file.write(line)


# Append Multiple Lines
more_lines = ["Line 4\n", "Line 5\n"]
# with open("example.txt", "a") as file:
#     file.writelines(more_lines)

# OR
with open("example.txt", "a") as file:
    for line in more_lines:
        file.write(line)


# Read Multiple Lines
with open('output.txt', 'r') as file:
    for line in file:
        print(line)

# OR
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip()) 
        # .strip() removes any leading and trailing whitespace (including \n) from a string.

# To add to an Array, use .append()