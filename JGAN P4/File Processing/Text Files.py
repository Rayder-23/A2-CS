# Writing to a text file:

# Open a file in write mode ('w')
file = open( 'output.txt', 'w')
# Write a line of text to the file
file.write( "This is a line of text.")
# Close the file
file.close()


# Reading from a text file:

# Open a file in read mode ('r')
file = open ('output. txt', 'r')
# Read a line of text from the file
line = file. readline()
print(line) # Prints the read line
# Close the file
file.close()


# Appending to a text file:

# Open a file in append mode ('a')
file = open( 'output. txt', 'a' )
# Append a line of text to the file
file write("\nThis is another line of text.")
# Close the file
file.close()
