# Exercise 04 — Target verification
#
# The sales team needs to identify which salespeople met the revenue target and announce only their names.
# Create who_met_target, which receives a dictionary of salespeople (name: revenue) and a target amount.
# Iterate over the dictionary and print "Salesperson [Name] met the target!" only for those who meet or exceed it.
# Use sales_team = {
#     "João": 12000, "Maria": 9500, "Ricardo": 10000,
#     "Fernanda": 15200, "Paulo": 5000
# } and revenue_target = 10000.

# Your solution:

def who_met_target(team, target):
  for name in team:
    if team[name] >= target:
      print(f"Salesperson {name} met the target!")

sales_team = {
  "João": 12000,
  "Maria": 9500,
  "Ricardo": 10000,
  "Fernanda": 15200,
  "Paulo": 5000
}
revenue_target = 10000

who_met_target(sales_team, revenue_target)
