# Exercise 03 — Sales by product
#
# Each tuple in the daily sales record stores a product, its unit price, and the quantity sold.
# Display the total for each sale.
# Given daily_sales = [("Monitor", 900, 2), ("Teclado", 150, 5), ("Mouse", 80, 10)], each tuple contains (product, unit_price, quantity).
# Teclado means keyboard in Portuguese.
# Use a for loop with unpacking directly in the loop to display each item: "Product: [name] | Total: R$[price * quantity]".

# Your solution:

daily_sales = [("Monitor", 900, 2), ("Teclado", 150, 5), ("Mouse", 80, 10)]
for product, price, quantity in daily_sales:
  print(f"Product: {product} | Total: R${price * quantity}")
