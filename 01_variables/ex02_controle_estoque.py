# Exercise 02 — Inventory balance
#
# An online store needs to calculate its final smartphone inventory after the day's
# transactions: sales remove units and supplier deliveries add them.
# The starting stock is 250 smartphones.
# The store sold 78 units and received 100 more.
# Update the stock variable and display the final balance.

# Your solution:


inventory = 250
sales = 78
restocking = 100

inventory = inventory - sales + restocking

print(f"Updated inventory: {inventory}")
