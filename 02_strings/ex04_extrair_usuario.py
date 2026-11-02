# Exercise 04 — Username extraction
#
# An access log needs to identify a user from their corporate email address, without the domain.
# Given "beatriz.oliveira@grupocorp.com", extract and display only the username, which is the
# part before @.
# Use .find() and string slicing.

# Your solution:


email = "beatriz.oliveira@grupocorp.com"
position = email.find("@")
name = email[:position]
print(name)
