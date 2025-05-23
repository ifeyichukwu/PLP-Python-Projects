# create an empty list
my_list = []

# Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert the value 15 at the second position in the list.
my_list.extend([50, 60, 70])

# Extend my_list with another list: [50, 60, 70].
my_list.pop()

# Remove the last element from my_list.
my_list.sort()

# Sort my_list in ascending order.
index = my_list.index(30)

# Find and print the index of the value 30 in my_list.
print(my_list)
print(f'The index of 30 is: {index}')