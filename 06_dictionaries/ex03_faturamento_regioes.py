# Exercise 03 — Regional revenue
#
# The finance department gathers revenue from four regions and needs to consolidate the values
# to evaluate the company's results.
# Given regional_sales = {"Norte": 15000, "Sul": 22000, "Leste": 18000, "Oeste": 25000}, extract
# the revenue values into a list.
# Calculate and display total revenue and the average across regions.
# The region labels Norte, Sul, Leste and Oeste mean North, South, East and West.

# Your solution:


regional_sales = {"Norte": 15000, "Sul": 22000, "Leste": 18000, "Oeste": 25000}
revenue = list(regional_sales.values())
total = sum(revenue)
average = total / len(revenue)

print(f"Total revenue: R${total:.2f}\nAverage revenue: R${average:.2f}")
