# Exercise 01 — Profit report
#
# A store's finance department needs to present a product's profitability in a message with
# formatted currency and percentage values.
# Given revenue of R$45,000 and a cost of R$23,500, calculate the profit and profit margin
# (profit / revenue).
# Display a message with the profit using a thousands separator and two decimal places, and the
# margin as a whole-number percentage.

# Your solution:

revenue = 45000
cost = 23500

profit = revenue - cost
margin = profit / revenue

print(f"The profit was R${profit:,.2f} and the margin was {margin:.0%}")
