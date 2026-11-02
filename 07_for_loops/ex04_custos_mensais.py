# Exercise 04 — Monthly costs
#
# The finance department wants to compare monthly expenses with planned limits and identify the
# excess when the budget is exceeded.
# Given targets = {"jan": 1000, "fev": 1200, "mar": 1100} and expenses = {"jan": 900, "fev":
# 1350, "mar": 1100}, iterate over the months.
# For expenses less than or equal to the target, display "Month [month]: Within budget.".
# If the target is exceeded, display "Month [month]: Budget exceeded by R$[difference].".
# The sample month label fev means February.

# Your solution:

targets = {"jan": 1000, "fev": 1200, "mar": 1100}
expenses = {"jan": 900, "fev": 1350, "mar": 1100}

for month in targets:
  difference = expenses[month] - targets[month]
  if expenses[month] <= targets[month]:
    print(f"Month {month}: Within budget.")
  else:
    print(f"Month {month}: Budget exceeded by R${difference:.2f}.")
