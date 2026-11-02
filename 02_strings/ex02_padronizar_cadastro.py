# Exercício 02 — Padronização de cadastro
#
# Um cadastro de cliente foi registrado com espaços e capitalização irregulares.
# Padronize o nome e o e-mail para uso no sistema de vendas.
# Dados nome = " mArCoS aNtOnIo rOcHa " e email = " MARCOS.ROCHA@GMAIL.COM ", remova os espaços das extremidades.
# Deixe a primeira letra de cada palavra do nome em maiúscula e o e-mail em minúsculas.
# Exiba os dois resultados.

# Sua solução:
nome = " mArCoS aNtOnIo rOcHa "
email = " MARCOS.ROCHA@GMAIL.COM "

nome = nome.strip().title()
email = email.strip().lower()

print(nome)
print(email)