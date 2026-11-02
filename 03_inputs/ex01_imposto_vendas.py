# Exercício 01 — Imposto sobre vendas
#
# O setor fiscal de uma prestadora de serviços precisa calcular o imposto de notas cujos valores podem ser copiados de planilhas com formatação monetária.
# Peça o valor bruto de uma nota fiscal, aceitando "R$ 5.000,00".
# Remova "R$", trate os separadores numéricos, troque a vírgula por ponto e converta o valor para float.
# Calcule o imposto de 15% sobre o valor bruto e exiba o imposto com duas casas decimais em uma mensagem com f-string.

# Sua solução:

valor_bruto = input("Qual o valor bruto da nota Fiscal?")
valor_bruto = valor_bruto.replace("R$", "").strip()
# Remove o R$ e remove os espaços das pontas

valor_bruto = valor_bruto.replace(".", "").replace(",", ".")
# remove o "." e tambem troca a virgula do final por "."

valor_bruto = float(valor_bruto)
# Transforma o valor que estava em string em float (Numero decimal)

imposto = valor_bruto * 0.15
# Calcula o imposto de 15%

print(f"O imposto é de R$ {imposto:.2f}")
# Mostra o imposto calculado ja formatado para 2 casas decimais. 