# Exercício 03 — Divisão de cargas
#
# Uma transportadora está planejando o envio de caixas em caminhões pequenos.
# Determine a quantidade de cargas completas e o restante para outra viagem.
# Distribua 1.250 caixas em caminhões com capacidade de 12 caixas cada.
# Calcule quantos caminhões ficarão completamente cheios usando // e quantas caixas sobrarão para uma última viagem menor usando %.

# Sua solução:

caixas = 1250
capacidade_caminhoes = 12
caminhoes_cheios = caixas // capacidade_caminhoes
caixas_restantes = caixas % capacidade_caminhoes
print(f"CAMINHOES CHEIOS: {caminhoes_cheios}")
print(f"Caixas restantes: {caixas_restantes}")
