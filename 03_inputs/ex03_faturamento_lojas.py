# Exercício 03 — Faturamento das lojas
#
# Um gerente quer comparar o faturamento de duas filiais usando valores informados durante a execução do programa.
# Peça os faturamentos da Loja A e da Loja B, aceitando números decimais.
# Calcule o faturamento total e a média entre as duas lojas.
# Exiba ambos em uma única mensagem, com separador de milhar e duas casas decimais.

# Sua solução:

lojaA = float(input("Qual o faturamento da loja A?"))
lojaB = float(input("Qual o faturamento da loja B?"))

faturamento = lojaA + lojaB
media = faturamento / 2


print(f"O faturamento total foi de: {faturamento:,.2f} e a média foi: {media:,.2f}")