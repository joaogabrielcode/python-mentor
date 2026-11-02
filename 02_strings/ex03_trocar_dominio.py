# Exercise 03 — Email domain replacement
#
# The company has adopted a new domain for employee email addresses.
# Update the supplied address to use that domain.
# Given "andre_silva@empresa.com.br", automatically replace the domain "@empresa.com.br" with
# "@grupocorp.com".
# Display the new email address.

# Your solution:


email = "andre_silva@empresa.com.br"
email = email.replace("@empresa.com.br", "@grupocorp.com")

print(f"New email: {email}")
