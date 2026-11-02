# Exercício 03 — Desconto progressivo
#
# Uma loja virtual concede descontos conforme o valor do carrinho.
# Determine o abatimento e quanto o cliente deverá pagar.
# Receba o valor total da compra e aplique o desconto: a partir de R$ 500, 15%; de R$ 200 até menos de R$ 500, 10%; abaixo de R$ 200, nenhum desconto.
# Exiba o valor do desconto e o valor final a pagar, formatados em R$.

# Sua solução:

valorCompra = float(input("Qual o valor da sua compra?"))
desconto15 = 0.15
desconto10 = 0.10

if valorCompra < 200:
  print(f"Seu desconto: R$0,00\nValor da compra: R${valorCompra:.2f}")
elif valorCompra < 500:
  valorDesconto = valorCompra * desconto10
  valorCompra = valorCompra - valorDesconto
  print(f"Seu desconto: R${valorDesconto:.2f}\nValor da compra: R${valorCompra:.2f}")
else:
  valorDesconto = valorCompra * desconto15
  valorCompra = valorCompra - valorDesconto
  print(f"Seu desconto: R${valorDesconto:.2f}\nValor da compra: R${valorCompra:.2f}")
