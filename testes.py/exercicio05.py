def frete_gratis(valor):
 	return valor >= 200

def pode_votar(idade):
 	return idade >= 16

def senha_valida(senha):
 	return len(senha) >= 8

assert frete_gratis(199.99) is False
assert frete_gratis(200) is True
assert frete_gratis(200.01) is True
assert pode_votar(15) is False
assert pode_votar(16) is True
assert pode_votar(17) is True
assert senha_valida(34268457) is False
assert senha_valida(82423938) is True
assert senha_valida(2535749) is True
