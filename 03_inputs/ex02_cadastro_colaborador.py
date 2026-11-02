# Exercício 02 — Cadastro de colaborador
#
# O RH precisa de um cadastro que identifique o colaborador pelo primeiro nome para o crachá e apresente seu e-mail de acesso padronizado.
# Peça o nome completo e o e-mail pessoal do colaborador.
# Extraia o primeiro nome e deixe sua primeira letra em maiúscula.
# Remova os espaços extras do e-mail e deixe-o em minúsculas.
# Exiba: "Cadastro concluído: [Primeiro Nome].
# E-mail de acesso: [E-mail padronizado]".

# Sua solução:
nome = input("Qual seu nome completo?")
email = input("Qual seu email?")

nomes = nome.split()
primeiro_nome = nomes[0]
primeiro_nome = primeiro_nome.capitalize()
email = email.strip().lower()
print(f"Cadastro concluido: {primeiro_nome}")
print(f"Email de acesso: {email}")
