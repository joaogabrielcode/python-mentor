# Exercício 01 — Atualização de clientes
#
# O sistema de relacionamento com clientes registra o faturamento acumulado por pessoa e precisa incorporar uma nova compra e um novo cliente.
# Dado clientes = {"Lira": 5000, "Alon": 3000, "Julia": 4500}, some uma nova compra de R$ 1.500 ao faturamento de "Alon".
# Adicione "Marcos" com faturamento inicial de R$ 2.000.
# Exiba o dicionário atualizado.

# Sua solução:

dado_clientes = {"Lira": 5000, "Alon": 3000, "Julia": 4500}
dado_clientes["Marcos"] = 2000
dado_clientes["Alon"] += 1500

print(dado_clientes)