# Exercício 03 — Faturamento por região
#
# O setor financeiro reúne o faturamento de quatro regiões e precisa consolidar esses valores para avaliar o resultado da empresa.
# Dado vendas_regiao = {
#     "Norte": 15000, "Sul": 22000, "Leste": 18000, "Oeste": 25000
# }, extraia os faturamentos para uma lista.
# Calcule e exiba o faturamento total e a média das regiões.

# Sua solução:

vendas_regiao = {"Norte": 15000, "Sul": 22000, "Leste": 18000, "Oeste": 25000}
faturamento = list(vendas_regiao.values())
total = sum(faturamento)
media = total / len(faturamento)

print(f"Faturamento total: R${total:.2f}\nMedia do faturamento: R${media:.2f}")