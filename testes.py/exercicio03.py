
def calcular_desconto(preco, percentual):
    desconto = preco * percentual / 100
    return preco - desconto

assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 20) == 160
assert calcular_desconto(50, 10) == 45

print("todos os testes pssaram")

