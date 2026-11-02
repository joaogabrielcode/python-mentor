# Exercise 02 — Sales commission
#
# A salesperson earns a commission on each sale, with a higher rate for transactions above a
# defined threshold.
# Given sales = [2000, 5000, 1000, 8000, 3000], iterate over the list.
# Each sale above R$4,000 earns a 10% commission; sales of R$4,000 or less earn 5%.
# At the end, display the salesperson's total commission.

# Your solution:


sales = [2000, 5000, 1000, 8000, 3000]


total_commission = 0
for sale in sales:
  if sale > 4000:
    commission = sale * 0.10
  else:
    commission = sale * 0.05
  total_commission += commission
print(f"Total sales commission: R$ {total_commission:.2f}")
