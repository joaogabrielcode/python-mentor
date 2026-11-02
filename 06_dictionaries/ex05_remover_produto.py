# Exercise 05 — Product removal
#
# An online store has discontinued a product and needs to remove it from the catalog, record its
# value and check that another product is still listed.
# Given products = {"celular": 1500, "camera": 800, "radio": 200, "fone": 100}, remove "radio"
# using .pop() and print the removed product's value.
# Check whether "celular" still exists in the dictionary and print True or False.
# The sample labels celular and fone mean cellphone and headphones.

# Your solution:


products = {"celular": 1500, "camera": 800, "radio": 200, "fone": 100}
print(f"Removed product value: {products.pop("radio")}")

print(f"Is the cellphone in the catalog? {"celular" in products}")
