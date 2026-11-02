# Exercício 04 — Custos mensais
#
# O setor financeiro quer comparar os gastos mensais com os limites planejados e identificar quanto foi excedido quando houver estouro do orçamento.
# Dados metas = {"jan": 1000, "fev": 1200, "mar": 1100} e gastos = {"jan": 900, "fev": 1350, "mar": 1100}, percorra os meses.
# Para gasto menor ou igual à meta, exiba "Mês [mês]: Dentro do orçamento.".
# Se ultrapassar a meta, exiba "Mês [mês]: Orçamento estourado em R$[valor da diferença].".

# Sua solução:
metas = {"jan": 1000, "fev": 1200, "mar": 1100}
gastos = {"jan": 900, "fev": 1350, "mar": 1100}

for mes in metas:
  diferenca = gastos[mes] - metas[mes]
  if gastos[mes] <= metas[mes]:
    print(f"Mês {mes}: Dentro do orçamento.")
  else:
    print(f"Mês {mes}: Orçamento estourado em R${diferenca:.2f}.")



