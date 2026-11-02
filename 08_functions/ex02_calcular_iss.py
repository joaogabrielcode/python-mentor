# Exercise 02 — ISS calculation
#
# The tax department needs to calculate ISS (Brazilian service tax) using a rate that varies with the invoice amount.
# Create calculate_iss, which receives a service amount and returns the tax.
# The rate is 5% for amounts above R$ 5,000 and 3% otherwise.
# Use the function for invoices of R$ 8,000 and R$ 2,000 and display the taxes.

# Your solution:

def calculate_iss(amount):
  if amount > 5000:
    return amount * 0.05
  else:
    return  amount * 0.03

print(calculate_iss(2000))
print(calculate_iss(8000))
