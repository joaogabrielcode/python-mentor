# Exercício 02 — Consulta de estoque
#
# A equipe de logística precisa consultar a disponibilidade de produtos a partir de um nome digitado pelo usuário.
# Dado estoque = {"teclado": 50, "mouse": 120, "monitor": 30}, peça o nome de um produto, tratando maiúsculas e espaços extras.
# Se existir, exiba sua quantidade disponível; caso contrário, exiba "Produto não encontrado no sistema".

# Sua solução:

estoque = {"teclado": 50, "mouse": 120, "monitor": 30}
produto = input("Qual produto você quer consultar? ").strip().lower()

if produto in estoque:
  print(f"Quantidade disponivel: {estoque[produto]}")
else:
  print("Produto não encontrado no sistema")