"""


You can either delete  elements of a dictionay or  individual elements
"""
#!usr/bin/python
# Define a dictionary
my_dict = {'Name': 'vincenttommi', 'Age': 24, 'profession': 'coder'}

# Remove a specific key-value pair from the dictionary
del my_dict['Name']

# Clear all entries in the dictionary
my_dict.clear()

# Delete the entire dictionary
del my_dict

# Attempting to access keys in the deleted dictionary will result in errors
# You should avoid trying to access or perform operations on a deleted dictionary
# The following lines will raise errors and should be removed:
# print("dict['Age']:", my_dict['Age'])
# print("dict['profession']", my_dict['profession'])

    