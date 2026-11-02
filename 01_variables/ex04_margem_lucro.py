# Exercise 04 — Profit margin
#
# A consultancy wants to evaluate a project's financial result and check whether its
# profitability met the target.
# Given revenue of R$15,000, fixed costs of R$5,000 and a tax of 15% on revenue, calculate the
# tax, net profit and profit margin (profit / revenue).
# Create a boolean variable named target_met to indicate whether the margin is greater than 0.30
# (30%).

# Your solution:


revenue = 15000
fixed_costs = 5000
tax = 0.15 * revenue
net_profit = revenue - fixed_costs - tax
profit_margin = net_profit / revenue
target_met = profit_margin > 0.30

print(f"Revenue: {revenue:.2f}")
print(f"Fixed costs: {fixed_costs:.2f}")
print(f"Tax: {tax:.2f}")
print(f"Net profit: {net_profit:.2f}")
print(f"Was the target met?: {target_met}")
