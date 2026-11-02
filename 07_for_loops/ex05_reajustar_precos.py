# Exercise 05 — Price adjustment
#
# A sales catalog needs an across-the-board price increase to account for inflation.
# The user chooses the percentage applied to all products.
# Given prices = {"celular": 1500, "tablet": 2500, "notebook": 5000}, ask for the increase
# percentage, such as 10 for 10%.
# Use a loop to update each price in the dictionary.
# Display the new catalog with formatted prices.
# The sample label celular means cellphone.

# Your solution:


products = {"celular": 1500, "tablet": 2500, "notebook": 5000}
print(f"These are the product prices: {products}")

percentage = float(input('What percentage should prices increase by? ')) / 100

for item in products:
  increase = products[item] * percentage
  products[item] = products[item] + increase
  print(f"{item}: R$ {products[item]:.2f}")
