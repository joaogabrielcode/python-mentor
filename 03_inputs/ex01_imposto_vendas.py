# Exercise 01 — Sales tax
#
# A service company's tax department needs to calculate tax on invoices whose amounts may be
# copied from spreadsheets as formatted currency.
# Ask for an invoice's gross amount, accepting Brazilian currency formatting such as "R$
# 5.000,00".
# Remove "R$", handle numeric separators, replace the decimal comma with a period and convert
# the value to float.
# Calculate 15% tax on the gross amount and display the tax to two decimal places in an f-string
# message.

# Your solution:


gross_amount = input('What is the gross invoice amount?')
gross_amount = gross_amount.replace("R$", "").strip()
# Remove R$ and surrounding whitespace.

gross_amount = gross_amount.replace(".", "").replace(",", ".")
# Remove thousands separators and replace the decimal comma with a period.

gross_amount = float(gross_amount)
# Convert the string value to a float (decimal number).

tax = gross_amount * 0.15
# Calculate the 15% tax.

print(f"The tax is R$ {tax:.2f}")
# Display the calculated tax to two decimal places.
