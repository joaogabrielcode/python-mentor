# Exercise 02 — System access
#
# A control panel should allow access only to users whose email addresses are registered as
# administrators.
# Given admins = ["ana@empresa.com", "guilherme@empresa.com", "felipe@empresa.com"], ask for the
# user's email and normalize it to lowercase without surrounding whitespace.
# If it is in admins, display "Access granted!
# Welcome to the control panel".
# Otherwise, display "Access denied.
# You do not have administrator permissions".

# Your solution:

admins = ["ana@empresa.com", "guilherme@empresa.com", "felipe@empresa.com"]
email_user = input('What is your email address?')
email_user = email_user.lower().strip()

if email_user in admins:
  print('Access granted! \nWelcome to the control panel')
else:
  print('Access denied. \nYou do not have administrator permissions')
