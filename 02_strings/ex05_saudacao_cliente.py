# Exercício 05 — Saudação ao cliente
#
# Uma mensagem de boas-vindas deve cumprimentar o cliente pelo primeiro nome, embora o cadastro contenha seu nome completo.
# Dado o nome completo "lucas ferreira souza", encontre a posição do primeiro espaço e use fatiamento para extrair o primeiro nome.
# Deixe a primeira letra do nome em maiúscula e exiba a mensagem: "Olá, [Primeiro Nome], seja bem-vindo ao nosso clube!"

# Sua solução:

nome_completo = "lucas ferreira souza"
posicao = nome_completo.find(" ")
nome = nome_completo[:posicao].capitalize()

print(f"Olá, {nome}, seja bem-vindo ao nosso clube!")
