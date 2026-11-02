# Exercise 05 — Currency conversion
#
# An importer receives a list of prices in US dollars and needs to display them in Brazilian reais using an exchange rate passed to the function.
# Create convert_to_real, which receives a price in dollars and the exchange rate and returns the amount in reais.
# Create process_price_list, which receives a list of dollar prices and the exchange rate, uses the first function to convert each item, and displays "The item costs R$[amount]" for each one.
# Test with prices_usd = [100, 50, 250] and an exchange rate of 5.20.

# Your solution:

def convert_to_real(amount, exchange_rate):
  return amount * exchange_rate

def process_price_list(prices, exchange_rate):
  for price in prices:
    print(f"The item costs R$ {convert_to_real(price, exchange_rate):.2f}")

prices_usd = [100,50, 250]
process_price_list(prices_usd, 5.20)
