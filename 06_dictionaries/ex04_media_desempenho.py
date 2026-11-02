# Exercise 04 — Average performance
#
# HR keeps each employee's three most recent performance ratings.
# A manager has requested Paula's average rating.
# Given performance = {"Lira": [8, 9, 7], "Paula": [10, 9, 10], "Tiago": [6, 7, 8]}, access
# "Paula"'s ratings and calculate the average by dividing their sum by the number of ratings.
# Display: "Paula's average was [average]".

# Your solution:

performance = {"Lira": [8, 9, 7], "Paula": [10, 9, 10], "Tiago": [6, 7, 8]}
paula = performance["Paula"]
average = sum(paula) / len(paula)

print(f"These were Paula's ratings: {paula}")
print(f"Paula's average was: {average:.2f}")
