def classificar_temperatura(temperatura):
    if temperatura < 15:
        return "Frio"
    elif temperatura <= 25:
        return "Agradável"
    else:
        return "Quente"

assert classificar_temperatura(10) == "Frio"

assert classificar_temperatura(14) == "Frio"

assert classificar_temperatura(15) == "Agradável"

assert classificar_temperatura(25) == "Agradável"

assert classificar_temperatura(26) == "Quente"

# Explicação de um teste:
# No teste assert classificar_temperatura(15) == "Agradável",
# eu estou verificando o limite de 15 graus.
# Como a regra diz que de 15 até 25 a temperatura é Agradável,
# o resultado esperado é "Agradável".
#
# Todos os testes passaram.
