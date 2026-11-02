# Exercise 01 — Product name standardization
#
# An online store receives product names with extra spaces and mixed letter cases.
# The standardization must be reusable.
# Create standardize_text, which takes a string and returns it without leading or
# trailing spaces and with the first letter of each word capitalized.
# Test with messy_products = [
#     " celular 13 ", "NOTEBOOK PRO ", " fOnEs Pro", "tAblet mini ",
#     " caixa de som sem fio "
# ].
# Sample product names are in Portuguese and must be preserved.

# Your solution:

def standardize_text(text):
  return text.lower().strip().title()

messy_products = [" celular 13 ", "NOTEBOOK PRO ", " fOnEs Pro", "tAblet mini "," caixa de som sem fio "]

for text in messy_products:
  print(standardize_text(text))
