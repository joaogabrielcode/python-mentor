# Exercício 02 — Comissão de vendas
#
# Um vendedor recebe comissão sobre cada venda, com uma taxa maior para operações que ultrapassam o limite definido.
# Dada vendas = [2000, 5000, 1000, 8000, 3000], percorra a lista.
# Cada venda acima de R$ 4.000 gera comissão de 10%; vendas de até R$ 4.000 geram comissão de 5%.
# Ao final, exiba o total de comissão do vendedor.

# Sua solução:

vendas = [2000, 5000, 1000, 8000, 3000]


comissao_total = 0
for venda in vendas:
  if venda > 4000:
    comissao = venda * 0.10
  else:
    comissao = venda * 0.05
  comissao_total += comissao
print(f"Comissão total das vendas: R$ {comissao_total:.2f}")
