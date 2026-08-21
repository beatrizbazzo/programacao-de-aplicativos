def pode_votar(idade):
    return idade >= 16

assert pode_votar(15) is False
assert pode_votar(16) is True
assert pode_votar(17) is True