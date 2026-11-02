# Exercise 02 — Employee registration
#
# HR needs a registration record that identifies an employee by their first name for a badge and
# displays a normalized login email address.
# Ask for the employee's full name and personal email address.
# Extract the first name and capitalize its first letter.
# Remove surrounding whitespace from the email and convert it to lowercase.
# Display: "Registration complete: [First Name].
# Login email: [Normalized Email]".

# Your solution:

name = input('What is your full name?')
email = input('What is your email address?')

names = name.split()
first_name = names[0]
first_name = first_name.capitalize()
email = email.strip().lower()
print(f"Registration complete: {first_name}")
print(f"Login email: {email}")
