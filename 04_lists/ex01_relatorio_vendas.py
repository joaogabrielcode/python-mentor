# Exercise 01 — Sales report
#
# A sales team recorded its daily sales during the week.
# Prepare the figures for its performance report.
# Given sales = [1500, 2000, 800, 3500, 1200], display a report with total weekly sales, the
# daily average, and the highest and lowest sale values.

# Your solution:


sales = [1500, 2000, 800, 3500, 1200]
total = sum(sales)
quantity = len(sales)
average = total / quantity
highest_sale = max(sales)
lowest_sale = min(sales)

print('>>> SALES REPORT <<< ')
print("--------------------------")
print(f"Weekly revenue: {total}")
print(f"Daily average: {average:,.2F}")
print(f"Highest sale: {highest_sale:,.2F}")
print(f"Lowest sale: {lowest_sale:,.2F}")
