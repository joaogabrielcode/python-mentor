# Exercício 01 — Relatório de vendas
#
# Uma equipe comercial registrou suas vendas diárias ao longo da semana.
# Prepare os indicadores que serão apresentados em seu relatório de desempenho.
# Dada a lista vendas = [1500, 2000, 800, 3500, 1200], exiba um relatório com o total de vendas da semana, a média diária e os valores da melhor e da pior venda do período.

# Sua solução:

vendas = [1500, 2000, 800, 3500, 1200]
total = sum(vendas)
quantidade = len(vendas)
media = total / quantidade
melhor = max(vendas)
menor = min(vendas)

print(">>> RELATORIO DE VENDAS <<< ")
print("--------------------------")
print(f"Faturamento da semana: {total}")
print(f"Média diaria: {media:,.2F}")
print(f"Melhor venda: {melhor:,.2F}")
print(f"Pior venda: {menor:,.2F}")