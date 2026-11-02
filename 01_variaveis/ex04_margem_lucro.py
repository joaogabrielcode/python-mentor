# Exercício 04 — Margem de lucro
#
# Uma consultoria quer avaliar o resultado financeiro de um projeto e verificar se a rentabilidade alcançou a meta definida.
# Dados faturamento de R$ 15.000, custos fixos de R$ 5.000 e imposto de 15% sobre o faturamento, calcule o imposto, o lucro líquido e a margem de lucro (lucro / faturamento).
# Crie a variável booleana meta_atingida para indicar se a margem é superior a 0.30 (30%).

# Sua solução:

faturamento = 15000
custos_fixos = 5000
imposto = 0.15 * faturamento
lucro_liquido = faturamento - custos_fixos - imposto
margem_lucro = lucro_liquido / faturamento
meta_atingida = margem_lucro > 0.30

print(f"Faturamento: {faturamento:.2f}")
print(f"Custos Fixos: {custos_fixos:.2f}")
print(f"Imposto: {imposto:.2f}")
print(f"Lucro Liquido: {lucro_liquido:.2f}")
print(f"Meta foi atingida?: {meta_atingida}")

