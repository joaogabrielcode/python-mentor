# Exercício 05 — Triagem de e-mails
#
# O atendimento precisa direcionar reclamações aos departamentos responsáveis de acordo com palavras presentes no assunto de cada e-mail.
# Peça o assunto do e-mail.
# Se contiver "pagamento" ou "boleto", exiba "Encaminhado para o Financeiro".
# Se contiver "entrega" ou "atraso", exiba "Encaminhado para a Logística".
# Caso não se enquadre nessas condições, exiba "Encaminhado para o Suporte Geral".

# Sua solução:
assunto_email = input("Qual o assunto do email?").lower().strip()

if "pagamento" in assunto_email or "boleto" in assunto_email:
  print("Encaminhado para o Financeiro")
elif "entrega" in assunto_email or "atraso" in assunto_email:
  print("Encaminhado para a Logística")
else:
  print("Encaminhado para o Suporte Geral")


