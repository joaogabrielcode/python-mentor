# Exercise 04 — Delivery route
#
# A delivery service has received new cities from a partner company.
# Update the route and report where Sorocaba appears.
# Given route = ["Sao Paulo", "Campinas", "Jundiai", "Sorocaba"] and new_cities = ["Itu",
# "Valinhos"], combine the lists with extend.
# Find the index of "Sorocaba" and display the full list and that index.
# Also display: "Sorocaba is city number X on the route".

# Your solution:

route = ["Sao Paulo", "Campinas", "Jundiai", "Sorocaba"]
new_cities = ["Itu", "Valinhos"]
route.extend(new_cities)
print(route)

index = route.index("Sorocaba")
print(index)

print(f"Sorocaba is city number {index + 1} on the route")
