# Exercício 05 — Tempo de contrato
#
# Um cliente quer consultar a duração de seu contrato de manutenção de software em anos e meses, em vez de receber apenas o total de meses.
# Converta a duração de um contrato de 40 meses para o formato "X anos e Y meses", usando divisão inteira e resto da divisão.

# Sua solução:

tempo = 40
anos = tempo // 12
meses = tempo % 12

print(f"{anos} anos e {meses} meses")