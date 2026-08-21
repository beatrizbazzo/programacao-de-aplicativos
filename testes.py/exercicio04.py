def eh_par(numero):
    return numero % 2 == 0

assert eh_par(3) is False
assert eh_par(2) is True
assert eh_par(4) is True
assert eh_par(5) is False

# Justificativa:
# O erro estava apenas no teste.
# Eu corrigi o True para False, porque 3 não é um número par.
# Não foi necessário mudar a função, pois ela já estava correta.