# Exercise 04 — Sales by branch
#
# A sales report must show total and average sales for each branch using a function that returns both indicators.
# Create analyze_sales, which receives a list of sales and returns the total and average.
# Given branch_data = {"Matriz": [10000, 15000, 20000], "Filial Sul": [5000, 7000]}, iterate through the dictionary, call the function for each branch, and unpack the return value.
# Matriz means headquarters; Filial Sul means South branch.
# Display: "Branch [Name] -> Total: R$[value], Average: R$[value]".

# Your solution:

branch_data = {"Matriz": [10000, 15000, 20000], "Filial Sul": [5000, 7000]}

def analyze_sales(sales):
  total = sum(sales)
  average = total / len(sales)
  return total, average

for name in branch_data:
  sales = branch_data[name]
  total, average = analyze_sales(sales)
  print(f"Branch {name} -> Total: R${total:.2f}, Average: R${average:.2f}")
