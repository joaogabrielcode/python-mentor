# Exercise 03 — Margin analysis
#
# The finance department wants to classify a product's profitability using revenue and cost.
# Create analyze_margin, which receives revenue and cost and calculates the profit margin (profit / revenue).
# Return "Healthy Margin" if the margin is at least 30% and "Low Margin" if it is lower.
# Display the result for revenue of R$ 10,000 and cost of R$ 6,000.

# Your solution:

def analyze_margin(revenue, cost):
  profit = revenue - cost
  margin = profit / revenue
  if margin >= 0.3:
    return "Healthy Margin"
  else:
    return "Low Margin"

print(analyze_margin(10000,6000))
