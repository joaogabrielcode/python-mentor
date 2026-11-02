# Exercício 01 — Bônus de vendas
#
# A equipe de vendas receberá uma bonificação calculada sobre o faturamento da empresa.
# Determine o impacto desse pagamento no valor que ficará disponível.
# Dado um faturamento de R$ 50.000 e um bônus de 10% (0.10), calcule e exiba o bônus e o faturamento após descontá-lo.

# Sua solução:

faturamento = 50000
percentual_bonus = 0.10

bonus = faturamento * percentual_bonus
valor_restante = faturamento - bonus

print(f"Bônus da equipe: R$ {bonus:.2f}")
print(f"Faturamento após pagar o bônus: R$ {valor_restante:.2f}")