# Exercício 03 — Ordenação de fretes
#
# Uma importadora quer apresentar os valores de frete em ordem decrescente e destacar as duas opções mais caras.
# Dada a lista de fretes em dólar fretes = [50, 80, 20, 150, 40], ordene-a do maior para o menor.
# Use fatiamento para guardar os dois fretes mais caros em top_fretes.
# Exiba a lista original ordenada e a lista top_fretes.

# Sua solução:
fretes = [50, 80, 20, 150, 40]
fretes.sort(reverse=True)
top_fretes = fretes[:2]
print(fretes)
print(top_fretes)