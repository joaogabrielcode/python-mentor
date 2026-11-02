# Exercício 03 — Estoque crítico
#
# A logística precisa emitir alertas para os produtos cujo estoque está abaixo do mínimo.
# Cada quantidade corresponde ao produto na mesma posição.
# Dados estoque_produtos = ["monitor", "teclado", "mouse", "headset", "gabinete"] e estoque_quantidades = [5, 12, 2, 8, 15], com posições correspondentes, percorra as listas e identifique produtos abaixo do mínimo de 8 unidades.
# Para cada um, exiba: "ALERTA: O produto [nome] está com apenas [quantidade] unidades no estoque!".

# Sua solução:

estoque_produtos = ["monitor", "teclado", "mouse", "headset", "gabinete"]
estoque_quantidades = [5, 12, 2, 8, 15]

for posicao in range(len(estoque_produtos)):
    if estoque_quantidades[posicao] < 8:
      print(f"ALERTA: O produto {estoque_produtos[posicao]} está com apenas {estoque_quantidades[posicao]} unidades no estoque!")