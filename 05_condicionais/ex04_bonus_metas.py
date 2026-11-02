# Exercício 04 — Bônus por metas
#
# A bonificação de um vendedor depende tanto de seu resultado individual quanto do resultado da loja.
# Verifique as duas metas antes de definir o bônus.
# Peça as vendas e a meta individual do vendedor, além das vendas totais e da meta da loja.
# Se ambas as metas forem atingidas, o bônus será de 20% das vendas do vendedor; caso contrário, será zero.
# Exiba: "Seu bônus este mês é de: R$[valor]".

# Sua solução:

vendas_loja = float(input("Quanto a loja vendeu?"))
meta_loja = float(input("Qual era a meta de vendas da loja?"))

vendas_vendedor = float(input("Quanto o vendedor vendeu"))
meta_vendedor = float(input("Qual era a meta de vendas do vendedor?"))

if vendas_loja >= meta_loja and vendas_vendedor >= meta_vendedor:
  bonus = vendas_vendedor * 0.20
  print(f"Seu bônus este mês é de: R${bonus:.2f}")
else:
  print(f"Seu bônus este mês é de: R$ 0,00")