# Exercício 04 — Extração de usuário
#
# Um registro de acessos precisa identificar o usuário a partir do e-mail corporativo, sem incluir o domínio.
# Dado o e-mail "beatriz.oliveira@grupocorp.com", extraia e exiba apenas o nome de usuário, a parte anterior ao @.
# Use .find() e fatiamento de texto.

# Sua solução:

email = "beatriz.oliveira@grupocorp.com"
posicao = email.find("@")
nome = email[:posicao]
print(nome)