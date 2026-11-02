# Exercício 04 — Rota de entregas
#
# Uma operação de entregas recebeu novas cidades de uma empresa parceira.
# Atualize a rota e informe onde Sorocaba aparece no percurso.
# Dados rota = ["Sao Paulo", "Campinas", "Jundiai", "Sorocaba"] e novas_cidades = ["Itu", "Valinhos"], una as listas usando extend.
# Identifique o índice de "Sorocaba" e exiba a lista completa e esse índice.
# Exiba também: "Sorocaba é a Xª cidade da rota".

# Sua solução:
rota = ["Sao Paulo", "Campinas", "Jundiai", "Sorocaba"]
novas_cidades = ["Itu", "Valinhos"]
rota.extend(novas_cidades)
print(rota)

indice = rota.index("Sorocaba")
print(indice)

print(f"Sorocaba é a {indice + 1}ª cidade da rota")