# Exercise 01 — Sales by team
# A team wants to identify who reached the sales target.
# Use sales = {"Ana": 1200, "Bruno": 800, "Carla": 1500} and target = 1000.
# Create a function that receives the dictionary and target and returns a list
# of the names of those who reached or exceeded the target. Iterate with for.
# Call the function and display the names. Also test a target nobody reaches.

# Your solution:
sales = {"Ana": 1200, "Bruno": 800, "Carla": 1500}
target = 1000

def sales_target(sales, target):
  salespeople = []
  for salesperson in sales:
    if sales[salesperson] >= target:
      salespeople.append(salesperson)
  return salespeople

names = sales_target(sales, target)
print(f"The salespeople who reached the targets were: {names}")

target = 2000
names = sales_target(sales, target)
print(f"The salespeople who reached the targets were: {names}")
