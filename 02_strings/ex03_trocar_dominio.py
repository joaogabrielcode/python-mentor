# Exercício 03 — Troca de domínio
#
# A empresa adotou um novo domínio para os e-mails dos funcionários.
# Atualize o endereço informado para usar esse domínio.
# Dado o e-mail "andre_silva@empresa.com.br", substitua automaticamente o domínio "@empresa.com.br" por "@grupocorp.com".
# Exiba o novo endereço de e-mail.

# Sua solução:

email = "andre_silva@empresa.com.br"
email = email.replace("@empresa.com.br", "@grupocorp.com")

print(f"Novo Email: {email}")