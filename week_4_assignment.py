# Week 4 Assignment - PLP python module

# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.


# Question 1 :  Create a program that reads a file and writes a modified version to a new file.

# Step 1: read the contents of the input file
with open('input.txt', 'r') as input_file:
    content = input_file.read()

# Step 2: Modify the content of the input file.
updated_content = content + '\nThis is an update to the file input.txt, to be sent to the new_file.txt'

# Step 3: Write the modified content to a new file
with open('new_file.txt', 'w') as new_file:
    new_file.write(updated_content)

# Step 4: Read the new file and print words
with open('new_file.txt', 'r') as new_file:
    final_read = new_file.read()
    print(final_read)