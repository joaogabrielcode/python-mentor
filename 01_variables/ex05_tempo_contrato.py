# Exercise 05 — Contract duration
#
# A customer wants to see the duration of a software maintenance contract in years and months
# instead of a total number of months.
# Convert a 40-month contract into the format "X years and Y months", using floor division and
# modulo.

# Your solution:


duration_months = 40
years = duration_months // 12
months = duration_months % 12

print(f"{years} years and {months} months")
