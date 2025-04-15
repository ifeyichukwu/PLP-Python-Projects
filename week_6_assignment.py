# Challenge: Use popular Python libraries to perform useful tasks!

# 📌 Task Requirements:

# Import the following libraries:

# pandas (for data manipulation)
# numpy (for numerical operations)
# matplotlib (for data visualization)
# requests (for making web requests)

# Complete the following tasks using the libraries:

# Create a NumPy array of numbers from 1 to 10 and calculate the mean.
# Load a small dataset into a pandas DataFrame and display summary statistics.
# Fetch data from a public API using requests and print a key piece of information.
# Plot a simple line graph using matplotlib (e.g., a list of numbers).

# Make sure to include comments in your code to explain what each part does.
# Importing necessary libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
import random

# 1. Create a NumPy array of numbers from 1 to 10 and calculate the mean.
numbers = np.array(range(1, 11))  # Create a NumPy array from 1 to 10
mean_value = np.mean(numbers) # Calculate the mean of the array
print("Mean of numbers from 1 to 10: ", mean_value) # Output the mean value

# 2. Load a small dataset into a pandas DataFrame and display summary statistics.
# Creating a small Dataset 
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 30, 22, 35],
    'City': ['Burundi', 'Botswana', 'Lagos', 'Nairobi'],
    'Position': ['Senior DevOps Engineer', 'Junior ML Engineer', 'Senior Data Scientist', 'Junior Embedded Systems Engineer']
}

# Creating a DataFrame from the dataset
df = pd.DataFrame(data) # Load the dataset into a pandas DataFrame
print("\nDataFrame:\n", df) # Output the DataFrame
print("\nSummary Statistics:\n", df.describe()) # Display summary statistics of the DataFrame

# 3. Fetch data from a public API using requests and print a key piece of information.
# Making a GET request to a public API (JSONPlaceholder)
response = requests.get('https://jsonplaceholder.typicode.com/posts/1') # Fetch data from the API
data = response.json() # Parse the JSON response
print("\nTitle of the first post from JSONPlaceholder API: ", data['title']) # Output the title of the first post

# 4. Plot a simple line graph using matplotlib (e.g., a list of numbers).
# Creating a simple line graph using matplotlib
x = np.array(range(1, 11)) # X-axis values (1 to 10)
y = np.random.randint(1, 100, size=10) # Y-axis values (random integers between 1 and 100)
plt.plot(x,y) # Plotting the line graph
plt.xlabel = 'X-axis' # Label for X-axis
plt.ylabel = 'Y-axis' # Label for Y-axis
plt.title = 'Simple line graph' # Title of the graph
plt.show() # Display the graph


