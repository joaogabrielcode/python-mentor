# Exercise 05 — Price updates
#
# A wine shop stores product names and prices in two corresponding lists.
# Allow the user to choose a wine and change its price.
# Given prices = [100.0, 250.0, 500.0] and wines = ["Branco", "Tinto", "Champagne"] with
# corresponding positions, ask for a product name and its new price.
# Update the price in the list and display both full lists.
# The Portuguese wine labels Branco and Tinto mean white and red.

# Your solution:

prices = [100.0, 250.0, 500.0]
wines = ["Branco", "Tinto", "Champagne"]
print(wines)
print(prices)
answer = input('Which wine price would you like to change?')
position = wines.index(answer)
new_price = float(input('What is the new price?'))
prices[position] = new_price
print(wines)
print(prices)
