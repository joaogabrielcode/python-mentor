# Exercise 05 — Customer greeting
#
# A welcome message should greet a customer by their first name, although the record contains
# their full name.
# Given the full name "lucas ferreira souza", find the first space and use slicing to extract
# the first name.
# Capitalize its first letter and display: "Hello, [First Name], welcome to our club!".

# Your solution:


full_name = "lucas ferreira souza"
position = full_name.find(" ")
name = full_name[:position].capitalize()

print(f"Hello, {name}, welcome to our club!")
