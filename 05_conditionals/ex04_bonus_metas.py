# Exercise 04 — Target-based bonus
#
# A salesperson's bonus depends on both their individual result and the store's overall result.
# Check both targets before deciding the bonus.
# Ask for the salesperson's sales and individual target, as well as the store's total sales and
# target.
# If both targets are met, the bonus is 20% of the salesperson's sales; otherwise, it is zero.
# Display: "Your bonus this month is: R$[amount]".

# Your solution:


store_sales = float(input('How much did the store sell?'))
store_target = float(input('What was the store sales target?'))

salesperson_sales = float(input('How much did the salesperson sell?'))
salesperson_target = float(input('What was the salesperson sales target?'))

if store_sales >= store_target and salesperson_sales >= salesperson_target:
  bonus = salesperson_sales * 0.20
  print(f"Your bonus this month is: R${bonus:.2f}")
else:
  print(f"Your bonus this month is: R$ 0.00")
