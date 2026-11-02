# Exercício 01 — Perfil de investimento
#
# Uma corretora quer apresentar uma sugestão de investimento de acordo com a faixa do valor informado pelo usuário.
# Peça o valor a investir, tratando entradas com "R$" ou vírgula.
# Abaixo de R$ 1.000, exiba "Perfil iniciante: Sugerimos Tesouro Direto".
# De R$ 1.000 a R$ 5.000, inclusive, exiba "Perfil moderado: Sugerimos Fundos Imobiliários".
# Acima de R$ 5.000, exiba "Perfil arrojado: Sugerimos Ações".

# Sua solução:

investimento = input("Qual valor deseja investir? ")
investimento = investimento.replace("R$", "").replace(",", ".")
investimento = float(investimento)

if investimento > 5000:
  print("Perfil arrojado: Sugerimos Ações")
elif investimento >= 1000 and investimento <= 5000:
  print("Perfil moderado: Sugerimos Fundos Imobiliários")
else: 
  print("Perfil iniciante: Sugerimos Tesouro Direto")