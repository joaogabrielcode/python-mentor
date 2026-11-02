# Exercise 01 — Sales bonus
#
# The sales team will receive a bonus calculated from the company's revenue.
# Determine how that payment affects the amount left over.
# Given revenue of R$50,000 and a bonus rate of 10% (0.10), calculate and display the bonus and
# the revenue remaining after paying it.

# Your solution:


revenue = 50000
bonus_rate = 0.10

bonus = revenue * bonus_rate
remaining_revenue = revenue - bonus

print(f"Team bonus: R$ {bonus:.2f}")
print(f"Revenue after paying the bonus: R$ {remaining_revenue:.2f}")
