# Exercise 03 — Progressive discount
#
# An online store grants discounts based on the cart total.
# Calculate the discount and the amount the customer must pay.
# Read the purchase total and apply a 15% discount for R$500 or more, a 10% discount from R$200
# up to but not including R$500, and no discount below R$200.
# Display the discount amount and final payment amount, formatted as R$ currency.

# Your solution:


purchase_amount = float(input('What is the purchase amount?'))
discount_rate_15 = 0.15
discount_rate_10 = 0.10

if purchase_amount < 200:
  print(f"Your discount: R$0.00\nPurchase amount: R${purchase_amount:.2f}")
elif purchase_amount < 500:
  discount_amount = purchase_amount * discount_rate_10
  purchase_amount = purchase_amount - discount_amount
  print(f"Your discount: R${discount_amount:.2f}\nPurchase amount: R${purchase_amount:.2f}")
else:
  discount_amount = purchase_amount * discount_rate_15
  purchase_amount = purchase_amount - discount_amount
  print(f"Your discount: R${discount_amount:.2f}\nPurchase amount: R${purchase_amount:.2f}")
