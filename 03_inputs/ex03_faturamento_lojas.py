# Exercise 03 — Store revenue
#
# A manager wants to compare two branches' revenues using values entered while the program runs.
# Ask for the revenues of Store A and Store B, accepting decimal numbers.
# Calculate the combined revenue and the average of the two stores.
# Display both in a single message, with thousands separators and two decimal places.

# Your solution:


store_a = float(input('What is the revenue of Store A?'))
store_b = float(input('What is the revenue of Store B?'))

revenue = store_a + store_b
average = revenue / 2


print(f"Total revenue was: {revenue:,.2f} and the average was: {average:,.2f}")
