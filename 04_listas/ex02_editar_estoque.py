# Exercício 02 — Edição de estoque
#
# Uma loja de eletrônicos precisa atualizar seu cadastro de estoque com a chegada de um produto, uma mudança de nome e a retirada de outro item.
# Dado estoque = ["monitor", "teclado", "mouse", "headset"], adicione "webcam" ao final e altere "teclado" para "teclado mecanico".
# Exiba True ou False para indicar se "impressora" está no estoque.
# Remova "mouse" da lista.

# Sua solução:

estoque = ["monitor", "teclado", "mouse", "headset"]
estoque.append("webcam")
print(estoque)

estoque[1] = "teclado mecanico"
print(estoque)

tem_impressora = "impressora" in estoque
print(tem_impressora)

estoque.remove("mouse")
print(estoque)