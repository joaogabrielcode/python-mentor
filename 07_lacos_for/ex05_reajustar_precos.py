# Exercício 05 — Reajuste de preços
#
# O catálogo comercial receberá um reajuste geral para compensar a inflação.
# O usuário deve escolher o percentual aplicado a todos os produtos.
# Dado precos = {"celular": 1500, "tablet": 2500, "notebook": 5000}, peça o percentual de aumento (por exemplo, 10 para 10%).
# Use um laço para atualizar cada preço no dicionário.
# Exiba o novo catálogo de preços formatado.

# Sua solução:

produtos = {"celular": 1500, "tablet": 2500, "notebook": 5000}
print(f"Esse são os preços dos produtos: {produtos}")

percentual = float(input("Qual percentual de ajuste dos preços? ")) / 100

for item in produtos:
  aumento = produtos[item] * percentual
  produtos[item] = produtos[item] + aumento
  print(f"{item}: R$ {produtos[item]:.2f}")
