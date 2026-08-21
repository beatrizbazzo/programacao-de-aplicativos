def calcular_desconto(preco, percentual):
    return preco - percentual

assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 20) == 160
assert calcular_desconto(50, 10) == 45

# FUNÇÃO CORRIGIDA

def calcular_desconto(preco, percentual):
    desconto = preco * percentual / 100
    return preco - desconto

assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 20) == 160
assert calcular_desconto(50, 10) == 45

# Breve explicação:
# A função original tinha um erro porque diminuía o percentual
# diretamente do preço. Depois da correção, ela calcula primeiro
# o valor correspondente à porcentagem e só depois tira esse
# valor do preço.
#
# Um teste que eu posso explicar para a turma é:
# assert calcular_desconto(100, 10) == 90
#
# Nesse caso, 10% de R$ 100 é R$ 10. Então:
# R$ 100 - R$ 10 = R$ 90.